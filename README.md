# videoPixelator



##  Useful [ffmpeg](https://www.ffmpeg.org/) commands

Convert video to frames:

```bash
ffmpeg -i ./videoIn/bodysnatchers.mp4 -vf fps=24 ./imageIn/out%04d.png
```

Convert frames to video:

```bash
ffmpeg -r 1/5 -i ./imageOut/out%04d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p ./videoOut/out.mp4
```


##  Author
