# videoPixelator



##  Instructions

1. Download the video an place it in the [videoIn](./videoIn/) folder.
2. Run the following [ffmpeg](https://www.ffmpeg.org/) command: `ffmpeg -i ./videoIn/VIDEO_NAME.mp4 -vf fps=24 ./imageIn/out%04d.png` to split the video into frames (stored in the [imageIn](./imageIn/) folder.
3. Run the [pixelateImageBatch](./pixelateImageBatch.py) to pixelate the frames.
4. Run the `ffmpeg -r 24 -i ./imageOut/out%04d.png -c:v libx264 -vf fps=24 -pix_fmt yuv420p ./videoOut/out.mp4` to re-stitch the video together (stored in the [imageOut](./imageOut/) folder.
5. Output video can be found in the [videoOut](./videoOut))

##  Author

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
