import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
from PIL import Image

# ---------------------------
# STREAMLIT APP CONFIG
# ---------------------------
st.set_page_config(page_title="YOLOv8 Object Detection", layout="wide")
st.title("🔍 YOLOv8 Object Detection App")

# ---------------------------
# DEBUG / STATUS LOG
# ---------------------------
log = st.container()
log.write("🚀 App started...")

# ---------------------------
# LOAD MODEL
# ---------------------------
with st.spinner("Loading YOLOv8 model..."):
    MODEL_PATH = "yolov8n.pt"
    model = YOLO(MODEL_PATH)
log.write("✅ Model loaded successfully.")

# ---------------------------
# FILE UPLOADER
# ---------------------------
uploaded_file = st.file_uploader("Upload an Image or Video", type=["jpg", "jpeg", "png", "mp4", "avi", "mov"])

if uploaded_file is None:
    st.info("👆 Please upload an image or video file to get started.")
else:
    file_type = uploaded_file.type
    log.write(f"📂 File uploaded: `{uploaded_file.name}` ({file_type})")

    if "image" in file_type:
        # ---------------- IMAGE ----------------
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_container_width=True)

        log.write("⚡ Running object detection on image...")
        results = model(img)
        annotated_img = results[0].plot()

        st.image(annotated_img, caption="Detection Result", use_container_width=True)
        log.write("✅ Image detection complete.")

        # Show detection details
        st.subheader("📋 Detection Details")
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            st.write(f"**Class:** {model.names[cls_id]}, **Confidence:** {conf:.2f}")

    elif "video" in file_type:
        # ---------------- VIDEO ----------------
        log.write("⚡ Preparing video for detection...")
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        cap = cv2.VideoCapture(tfile.name)
        output_path = "detected_output.mp4"

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS),
                              (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                               int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

        stframe = st.empty()
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            annotated_frame = results[0].plot()
            stframe.image(annotated_frame, channels="BGR", use_container_width=True)

            out.write(annotated_frame)
            frame_count += 1

            if frame_count % 10 == 0:
                log.write(f"Processed {frame_count} frames...")

        cap.release()
        out.release()
        log.write("✅ Video processing complete.")

        with open(output_path, "rb") as f:
            st.download_button("⬇️ Download Processed Video", f,
                               file_name="detected_output.mp4",
                               mime="video/mp4")
