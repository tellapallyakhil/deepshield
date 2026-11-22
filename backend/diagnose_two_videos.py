import cv2
import os
from PIL import Image
from app.ml.deepfake.pipeline import DeepfakePipeline

p = DeepfakePipeline(device="cpu")

videos = [
    ("EV 52: fake.mp4", "/app/uploads/deepfake/fake.mp4"),
    ("EV 51: video_20260829_095706.mp4", "/app/uploads/deepfake/video_20260829_095706.mp4"),
    ("EV 39: hello.mp4", "/app/uploads/deepfake/hello.mp4"),
    ("EV 50: Oneiric (AI film)", "/app/uploads/deepfake/Oneiric _ AI Sci-Fi Short Film _ Higgsfield Originals (2026).mp4"),
]

for label, vpath in videos:
    if not os.path.exists(vpath):
        print(f"Skipping {label}, file not found")
        continue
    cap = cv2.VideoCapture(vpath)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fc = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    size_mb = os.path.getsize(vpath) / (1024 * 1024)
    print(f"\n=======================================================")
    print(f"{label}")
    print(f"File: {vpath} ({size_mb:.2f} MB), {w}x{h}, {fps:.1f} fps, {fc} frames")
    
    frames = p.preprocessor.extract_frames(vpath, max_frames=20)
    items = p.preprocessor.detect_and_crop_faces(frames, return_metadata=True)
    face_items = [it for it in items if it["is_face"]]
    skipped = [it for it in items if it.get("skip_reason")]
    print(f"Frames extracted: {len(frames)}, Faces kept: {len(face_items)}, Skipped (too small): {len(skipped)}")
    
    result = p.process_video(vpath)
    print(f"PIPELINE RESULT: {result['label']} (fake_prob={result['fake_probability']}, confidence={result['confidence']}%)")
    print("Frame scores (ViT / Custom / Combined):")
    for fp in result.get("frame_predictions", []):
        print(f"  Frame {fp.get('frame_idx', 0):02d}: ViT={fp.get('vit_score', 0):.3f}, Custom={fp.get('custom_model_score', 0):.3f} -> FakeProb={fp.get('fake_prob', 0):.3f}")
