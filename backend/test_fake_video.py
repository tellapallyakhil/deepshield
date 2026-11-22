import os
from app.ml.deepfake.pipeline import DeepfakePipeline

p = DeepfakePipeline(device='cpu')
video_path = '/app/uploads/deepfake/fake_video.mp4'

frames = p.preprocessor.extract_frames(video_path, max_frames=20)
items = p.preprocessor.detect_and_crop_faces(frames, return_metadata=True, min_face_size=40)
face_items = [it for it in items if it['is_face']]
print(f"fake_video.mp4: Detected {len(face_items)} faces with min_face_size=40")
for it in face_items[:5]:
    res = p.analyzer.analyze_face_authenticity(it['image'])
    print(f"Size: {it['image'].size} | ViT={res.get('vit_score', 0):.3f} | Custom={res.get('custom_model_score', 0):.3f}")

