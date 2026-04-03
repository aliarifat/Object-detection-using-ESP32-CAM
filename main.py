import cv2
import numpy as np
import urllib.request
import requests  # For sending HTTP requests to ESP32-CAM

# ESP32-CAM control URL
ESP32_CAM_URL = "http://192.168.1.101/control?state="

# Paths to YOLO model files
weights_path = r"F:\object_detection\YOLO\yolov3.weights"
config_path = r"F:\object_detection\YOLO\yolov3.cfg"
names_path = r"F:\object_detection\YOLO\coco.names"

# Load YOLO model and COCO class names
net = cv2.dnn.readNet(weights_path, config_path)
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] if isinstance(i, list) else layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

def detect_objects(frame):
    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_outputs = net.forward(output_layers)

    boxes, confidences, class_ids = [], [], []

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.3:
                center_x, center_y = int(detection[0] * width), int(detection[1] * height)
                w, h = int(detection[2] * width), int(detection[3] * height)
                x, y = int(center_x - w / 2), int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.4)

    face_detected = False
    if len(indexes) > 0 and isinstance(indexes, np.ndarray):
        indexes = indexes.flatten()
        for i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]

            if label == "person":  # Detecting faces or persons
                face_detected = True

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confidences[i]:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return frame, face_detected

def main():
    url = "http://192.168.1.101/cam-hi.jpg"

    face_active = False
    while True:
        try:
            img_resp = urllib.request.urlopen(url)
            imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            frame = cv2.imdecode(imgnp, -1)

            result_frame, face_detected = detect_objects(frame)

            if face_detected and not face_active:
                requests.get(ESP32_CAM_URL + "on")
                face_active = True
            elif not face_detected and face_active:
                requests.get(ESP32_CAM_URL + "off")
                face_active = False

            cv2.imshow("Object Detection", result_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            print(f"Error occurred: {e}")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
