import os
import shutil

from google_images_download import google_images_download

def dowload_matting_dataset(output_dir):

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    proxy="127.0.0.1:10808"

    response = google_images_download.googleimagesdownload()
    response.download({
        "keywords": "portrait transparent background",
        "color_type": "transparent",
        "size": "medium",
        "limit": 500,
        "output_directory": output_dir,
        # "proxy": proxy,
        "chromedriver": "C:\\chromedriver.exe"})

    response = google_images_download.googleimagesdownload()
    response.download({
        "keywords": "texture background",
        "color_type": "full-color",
        "size": "medium",
        "limit": 500,
        "output_directory": output_dir,
        # "proxy": proxy,
        "chromedriver": "C:\\chromedriver.exe"})

if __name__ == "__main__":
    output_dir = os.path.join("data", "matting")
    dowload_matting_dataset(output_dir)
