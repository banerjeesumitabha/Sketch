import numpy as np
import cv2
import os.path
class PencilSketch:
    """Pencil sketch effect
        A class that applies a pencil sketch effect to an image.
        The processed image is overlayed over a background image for visual
        effect.
    """

    def __init__(self, bg_gray='bg\img_canvas.jpg'):
        """Initialize parameters

            :param bg_gray: Optional background image to improve the illusion
                            that the pencil sketch was drawn on a canvas.
        """

        # try to open background canvas (if it exists)
        self.canvas = cv2.imread(bg_gray, cv2.CV_8UC1)

    def render(self, img_rgb):
        """Applies pencil sketch effect to an RGB image
            :param img_rgb: RGB image to be processed
            :returns: Processed RGB image
        """
        img_rgb = cv2.imread(img_rgb)
        height, width = img_rgb.shape[:2]
        height , width = height , width
        img_rgb = cv2.resize(img_rgb, (width, height))
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
        img_blend = cv2.divide(img_gray, img_blur, scale=256)

        # if available, blend with background canvas
        if self.canvas is not None:
            self.canvas = cv2.resize(self.canvas, (width, height))
            img_final = cv2.addWeighted(img_blend,0.8, self.canvas,0.2,1)
        
        result = cv2.cvtColor(img_final, cv2.COLOR_GRAY2RGB)
        cv2.imshow("Image",result)
        cv2.waitKey(0)
        save_path = 'sketches/'
        name_of_file = raw_input("What should be the name of the file: ")
        complete_path = os.path.join(save_path, name_of_file+".jpg")
        cv2.imwrite(complete_path,result)
        print 'File saved'
        x=raw_input('Press Enter to exit')
