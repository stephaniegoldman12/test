from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom trained

# Export the model
model.export(format='saved_model', export_dir='yolov8n_saved_model')
