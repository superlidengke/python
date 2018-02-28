# -*- coding: utf-8 -*-
import cv2
import math

class CutImageFromVideo:
    """extract image from video"""

    def extract(self,sourceVideo,imageDest,interval,total):
        """extract image from video, save it as jpg every interval second, stop when having images as total """
        vidcap = cv2.VideoCapture(sourceVideo)
        frame_rate = math.floor(vidcap.get(cv2.CAP_PROP_FPS))
        success = True
        count = 1
        frame = -1
        while success and count <= total:
            success, image = vidcap.read()
            frame += 1
            if frame % (frame_rate*interval) == 0:
                file_path = imageDest + "frame%03d.jpg" % count
                cv2.imwrite(file_path, image)     # save frame as JPEG file
                print('Save image to %s' % file_path)
                count += 1

