from ultralytics import YOLO
import cv2

# Load YOLOv5 model
model = YOLO('yolov5s.pt')

cap = cv2.VideoCapture('video.mp4')

# Line position and offset for counting
line_position = 550
offset = 30

# Track vehicle centroids and IDs
vehicle_tracks = {}
vehicle_id = 0

# Count variables
up_count = 0
down_count = 0

# Utility to get center point
def get_center(x1, y1, x2, y2):
    return int((x1 + x2) / 2), int((y1 + y2) / 2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    current_centers = []
    for box in results.boxes:
        cls_id = int(box.cls)
        label = model.names[cls_id]
        if label in ['car', 'bus', 'truck', 'motorcycle']:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = get_center(x1, y1, x2, y2)
            current_centers.append((cx, cy))

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)

    # Match current centers with previous tracked vehicles
    new_tracks = {}
    for cx, cy in current_centers:
        matched = False
        for vid, (pcx, pcy) in vehicle_tracks.items():
            if abs(cx - pcx) < 40 and abs(cy - pcy) < 40:
                new_tracks[vid] = (cx, cy)

                # Check movement direction
                if pcy < line_position <= cy:
                    down_count += 1
                    print(f"Vehicle {vid} moved down. Count: {down_count}")
                elif pcy > line_position >= cy:
                    up_count += 1
                    print(f"Vehicle {vid} moved up. Count: {up_count}")

                matched = True
                break

        if not matched:
            # New vehicle
            new_tracks[vehicle_id] = (cx, cy)
            vehicle_id += 1

    vehicle_tracks = new_tracks.copy()

    # Draw count line
    cv2.line(frame, (25, line_position), (1200, line_position), (255, 0, 255), 2)

    # Display counts
    cv2.putText(frame, f"Up: {up_count}", (800, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
    cv2.putText(frame, f"Down: {down_count}", (100, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("YOLO Bidirectional Counter", frame)
    if cv2.waitKey(1) & 0xFF == 13:  # Press Enter to exit
        break

cap.release()
cv2.destroyAllWindows()
