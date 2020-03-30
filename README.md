# videoPixelator

These scripts can "pixelate" an image or video by taking the means of regular-sized pixels blocks and adding frames to them.

<img src="./media/test.jpg" width='100%'>
<img src="./media/testOut.png" width='100%'>

##  Instructions

1. Download the video an place it in the [videoIn](./videoIn/) folder.
2. Run the following [ffmpeg](https://www.ffmpeg.org/) command: `ffmpeg -i ./videoIn/VIDEO_NAME.mp4 -vf fps=24 ./imageIn/out%04d.png` to split the video into frames (stored in the [imageIn](./imageIn/) folder.
3. Run the [pixelateImageBatch](./pixelateImageBatch.py) to pixelate the frames.
4. Run the `ffmpeg -r 24 -i ./imageOut/out%04d.png -c:v libx264 -vf fps=24 -pix_fmt yuv420p ./videoOut/out.mp4` to re-stitch the video together (stored in the [imageOut](./imageOut/) folder.
5. Output video can be found in the [videoOut](./videoOut))

##  Files' Description

* `pixelateImageBatch.py`: Script to batch-pixelate images in a folder.
* `pixelateImage.py`: Pixelate one image.
* `functions.py`: Auxiliary functions for the scripts.

##  Dependencies

* [ffmpeg](https://www.ffmpeg.org/)
* [open-cv](https://pypi.org/project/opencv-python/)

##  Author

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
