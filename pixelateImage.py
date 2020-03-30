import os
import cv2
import functions as fun

(PATH_IN, PATH_OUT, IMG, GRID_SIZE, FRM, FRAME_COL) = (
        './', './', 'test.jpg',
        8, True, [0, 0, 0]
    )
img = cv2.imread(PATH_IN+IMG)
img = fun.pixelateImage(img, GRID_SIZE, True, (0, 0, 0))
# Export the resulting image
filename = os.path.splitext(IMG)[0]
cv2.imwrite(PATH_OUT+filename+'_{}.png'.format(str(1).zfill(4)), img)
