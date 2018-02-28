# -*- coding: utf-8 -*-

import unittest
from CutImageFromVideo import CutImageFromVideo

class TestClient(unittest.TestCase):

    def test_create_a_user(self):
        sourceVideo = r'C:\temp\video\花咲舞が黙ってない2 第1話 720p HDTV x264 AAC-DoA.mkv'
        imageDest = "C:/temp/video/images/"
        cut = CutImageFromVideo()
        cut.extract(sourceVideo,imageDest,60,60)