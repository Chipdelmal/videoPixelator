import cv2


def pixelateImage(img, gridSize, gridOverlay=True, gridOverlayColor=(0, 0, 0)):
    # Run through the image and apply a mean filter function
    for r in range(0, img.shape[0], gridSize):
        for c in range(0, img.shape[1], gridSize):
            block = img[r:r+gridSize, c:c+gridSize, :]
            shp = block.shape
            blurred = cv2.blur(block, (shp[0]*2, shp[1]*2))
            img[r:r+gridSize, c:c+gridSize, :] = blurred
            # Could export here if the blocks were needed
    # Overlay the grid if requested
    if gridOverlay is True:
        # Add Gridlines
        height, width, channels = img.shape
        for x in range(0, width - 1, gridSize):
            cv2.line(img, (x, 0), (x, height), gridOverlayColor, 1, 1)

        for x in range(0, height - 1, gridSize):
            cv2.line(img, (0, x), (width, x), gridOverlayColor, 1, 1)

    return img
