from django.conf import settings
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

def EdgeDetection(path):
    frame = cv2.imread(path)
    blur = cv2.blur(frame,(5,5))
    edged = cv2.Canny(blur, 100, 250)
    kernel_remove_vertical = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(1, 1))# remove vertical parts
    edged_hor = cv2.erode(edged, kernel_remove_vertical)
    pixels = np.argwhere(edged_hor == 255)
    x = (pixels[:, 1])
    y = (pixels[:, 0])
    fig = plt.figure()
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.plot(x,y,'r.', markersize=0.3)
    plt.savefig(os.path.join(settings.MEDIA_ROOT,'ml_output/process.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)





