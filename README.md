# videoPixelator



##  Useful [ffmpeg](https://www.ffmpeg.org/) commands

Convert video to frames:

```bash
ffmpeg -i ./videoIn/bodysnatchers.mp4 -vf fps=24 ./imageIn/out%04d.png
```

Convert frames to video:

```bash
ffmpeg -r 24 -i ./imageOut/out%04d.png -c:v libx264 -vf fps=24 -pix_fmt yuv420p ./videoOut/out.mp4
```


##  Author

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
