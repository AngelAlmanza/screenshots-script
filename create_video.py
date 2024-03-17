import cv2
import os

def main(): 
  image_folder = './screenshots_draw_6'
  video_name = 'video_salida.mp4'

  images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
  frame = cv2.imread(os.path.join(image_folder, images[0]))
  height, width, layers = frame.shape
  video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height))

  for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

  cv2.destroyAllWindows()
  video.release()


if __name__ == "__main__":
  main()