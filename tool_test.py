# -*- coding: utf-8 -*-

import unittest
from CutImageFromVideo import CutImageFromVideo
from DetectFaces import DetectFace

class TestClient(unittest.TestCase):

    def test_create_a_user(self):
        sourceVideo = r'C:\temp\video\花咲舞が黙ってない2 第1話 720p HDTV x264 AAC-DoA.mkv'
        imageDest = "C:/temp/video/images/"
        cut = CutImageFromVideo()
        cut.extract(sourceVideo,imageDest,60,60)

    def test_detect_face(self):
        detect = DetectFace()
        imagePath = r'C:\temp\video\faces\frame008.jpg'
        desti = r'C:\temp\video\faces\faces/'
        detect.detct_face_save(imagePath,desti)