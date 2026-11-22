import os
import cv2
import numpy as np
from .preprocess import VideoPreprocessor
from .model import DeepfakeAuthenticityAnalyzer

class DeepfakePipeline:
    def __init__(self, device='cpu'):
        self.device = device
        self.preprocessor = VideoPreprocessor(device=self.device)
        self.analyzer = DeepfakeAuthenticityAnalyzer(device=self.device)

    def process_video(self, video_path: str, output_dir: str = "/tmp"):
        """Processes video frames through fine-tuned ViT Deepfake Classifier."""
        frames = self.preprocessor.extract_frames(video_path, max_frames=20)
        if not frames:
            return {"status": "error", "fake_probability": 0.01, "label": "Real", "confidence": 0.99}
            
        items = self.preprocessor.detect_and_crop_faces(frames, return_metadata=True)
        # Prioritize actual face crops over scenery/establishing shots
        face_items = [it for it in items if it["is_face"]]
        eval_items = face_items if face_items else items[:5]
            
        fake_scores = []
        frame_preds = []
        vit_scores = []
        
        for it in eval_items:
            res = self.analyzer.analyze_face_authenticity(it["image"])
            res["is_face"] = it["is_face"]
            res["frame_idx"] = it.get("frame_idx", 0)
            fake_scores.append(res["fake_prob"])
            vit_scores.append(res.get("vit_score", 0.0))
            frame_preds.append(res)
                
        total_eval = len(eval_items)
        sorted_scores = sorted(fake_scores, reverse=True)
        median_fake_prob = float(np.median(fake_scores))
        mean_fake_prob = float(np.mean(fake_scores))
        
        # Forensic cluster metrics:
        k = min(3, max(1, total_eval // 4))
        top_k_avg = float(np.mean(sorted_scores[:k])) if sorted_scores else 0.0
        
        strong_fake_count = sum(1 for s in fake_scores if s >= 0.60)
        strong_fake_ratio = strong_fake_count / total_eval if total_eval > 0 else 0.0
        
        # Robust Forensic Decision Logic:
        # A video is flagged as Fake if:
        # 1. Multiple faces show strong synthetic artifacts (>=2 faces, >=18% ratio, top-k avg >=0.65)
        # 2. Or top-k detections show extreme synthetic manipulation (>=0.75) with >=2 elevated frames
        # 3. Or median or mean probability exceeds 0.50
        if strong_fake_count >= 2 and strong_fake_ratio >= 0.18 and top_k_avg >= 0.65:
            is_fake = True
            final_prob = max(top_k_avg * 0.70 + mean_fake_prob * 0.30, 0.65)
        elif top_k_avg >= 0.75 and strong_fake_count >= 2:
            is_fake = True
            final_prob = top_k_avg
        elif median_fake_prob > 0.50:
            is_fake = True
            final_prob = median_fake_prob
        elif mean_fake_prob > 0.50:
            is_fake = True
            final_prob = mean_fake_prob
        else:
            is_fake = False
            final_prob = median_fake_prob
            
        final_label = "Fake" if is_fake else "Real"
        final_confidence = final_prob if is_fake else (1.0 - final_prob)
        
        return {
            "fake_probability": round(final_prob, 3),
            "label": final_label,
            "confidence": round(final_confidence * 100, 1),
            "frame_predictions": frame_preds,
            "status": "success",
            "frames_analyzed": len(eval_items),
            "faces_detected": len(face_items)
        }
