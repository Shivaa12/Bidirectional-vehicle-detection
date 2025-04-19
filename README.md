# Bidirectional Vehicle Counting using YOLOv5 and OpenCV

This project implements a real-time bidirectional vehicle counting system using the **YOLOv5** object detection model and **OpenCV**. It detects and tracks vehicles in a video, counts the number of vehicles moving **upward** and **downward** across a predefined line, and displays the count in real-time.

## Features

- Vehicle detection using **YOLOv5** (`yolov5s.pt` pre-trained model)
- Bidirectional vehicle counting (up and down movement)
- Real-time object tracking using centroids
- Bounding box and label rendering for detected vehicles
- Line-crossing logic to detect direction of movement
- Simple and efficient implementation with OpenCV

## Classes Detected

This project detects and counts the following vehicle classes:
- Car
- Bus
- Truck
- Motorcycle

## Technologies Used

- **Python 3**
- **OpenCV** for video processing
- **Ultralytics YOLOv5** for vehicle detection
- **NumPy** (optional, depending on use)

## Project Structure

```
├── yolov5_vehicle_counter.py  # Main script
├── video.mp4                  # Input video file
├── yolov5s.pt                 # YOLOv5 small model weights
```

## How It Works

1. Loads a video file and YOLOv5 model.
2. Detects vehicles frame by frame.
3. Tracks vehicle centroids to identify movement direction.
4. Updates vehicle counts when they cross a virtual line.
5. Displays real-time bounding boxes, labels, and counters.

## How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/bidirectional-vehicle-counter.git
   cd bidirectional-vehicle-counter
   ```

2. **Install dependencies**:
   ```bash
   pip install ultralytics opencv-python
   ```

3. **Download YOLOv5s model weights**:
   The script automatically downloads `yolov5s.pt` if not available, or you can manually download it from [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5).

4. **Run the script**:
   ```bash
   python yolov5_vehicle_counter.py
   ```

## Output

- Live detection window with vehicle count.
- Vehicles are highlighted with bounding boxes and class labels.
- Count of vehicles moving "Up" and "Down" is updated in real time.

## Notes

- Adjust `line_position` and `offset` for different videos to fine-tune accuracy.
- The current vehicle matching logic uses Euclidean distance thresholds — consider integrating more robust tracking methods (like Kalman Filters or Deep SORT) for crowded scenes or complex movement.

## Sample Demo

*Coming Soon: Add your video or GIF demo here*

## License

This project is open-source and free to use under the [MIT License](LICENSE).
