import os
import cv2
import glob
import functions as fun

(PATH_IN, PATH_OUT, GRID_SIZE, FRM, FRAME_COL) = (
        './media/image/', './media/imageOut/',
        10, True, [0, 0, 0]
    )
images = glob.glob(PATH_IN+'*.jpg')
images.sort()
for path in images:
    img = cv2.imread(path)
    name = path.split('/')[-1].split('.')[0]
    img = fun.pixelateImage(img, GRID_SIZE, True, (0, 0, 0))
    # Export the resulting image
    filename = os.path.splitext(path)[0]
    cv2.imwrite(PATH_OUT+name+'.png', img)
