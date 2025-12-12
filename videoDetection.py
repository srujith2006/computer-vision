!pip install ultralytics
from ultralytics import yolo
!yolo detect predict model=yolov9m.pt source="/content/video4.mp4"
!ffmpeg -i {"copy path"} -vcodec libx264 {"final.avi"}
