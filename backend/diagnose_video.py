import numpy as np
import cv2
import os
from PIL import Image
from app.ml.deepfake.pipeline import DeepfakePipeline

p = DeepfakePipeline(device="cpu")

# The video the user says is real but flagged as fake
video_path = "/app/uploads/deepfake/fake.mp4"
cap = cv2.VideoCapture(video_path)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
duration = frame_count / fps if fps > 0 else 0
cap.release()

print(f"=== fake.mp4 File Properties ===")
print(f"Size: {os.path.getsize(video_path):,} bytes")
print(f"Resolution: {width}x{height}")
print(f"FPS: {fps}")
print(f"Duration: {duration:.1f}s")
print(f"Total frames: {frame_count}")

frames = p.preprocessor.extract_frames(video_path, max_frames=20)
items = p.preprocessor.detect_and_crop_faces(frames, return_metadata=True)
face_items = [it for it in items if it["is_face"]]

print(f"\nFaces detected: {len(face_items)} out of {len(frames)} frames")
print(f"\nPer-frame breakdown:")
for it in items:
    r = p.analyzer.analyze_face_authenticity(it["image"])
    w, h = it["image"].size
    face_tag = "FACE" if it["is_face"] else "NO_FACE"
    print(f"  Frame {it['frame_idx']:02d} [{face_tag}] {w}x{h} | ViT={r['vit_score']:.3f} | Custom={r['custom_model_score']:.3f} | Combined={r['fake_prob']:.3f}")

# Now compare with hello.mp4 (known real)
print(f"\n=== hello.mp4 (Known Real) File Properties ===")
video_path2 = "/app/uploads/deepfake/hello.mp4"
cap2 = cv2.VideoCapture(video_path2)
w2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
h2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps2 = cap2.get(cv2.CAP_PROP_FPS)
fc2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
cap2.release()
print(f"Size: {os.path.getsize(video_path2):,} bytes")
print(f"Resolution: {w2}x{h2}")
print(f"FPS: {fps2}")
print(f"Duration: {fc2/fps2:.1f}s")
