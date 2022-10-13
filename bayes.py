import sys
import cv2 as cv
import random
import itertools
import numpy as np

MAP_FILE = "cape_python.png"

# Search Area Corners for OpenCV
SA1_CORNERS = (130, 265, 180, 315) # (UL-X, UL-Y, LR-X, LR-Y)
SA2_CORNERS = (80, 255, 130, 305) # (UL-X, UL-Y, LR-X, LR-Y)
SA3_CORNERS = (105, 205, 155, 255) # (UL-X, UL-Y, LR-X, LR-Y)


class Search:
    def __init__(self, name):
        self.name = name
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print('Could not load map file {}'.format(MAP_FILE), file=sys.stderr)
            sys.exit(1)

        self.area_actual = 0
        self.sailor_actual = [0, 0]

        self.sa1 = self.img[SA1_CORNERS[1]: SA1_CORNERS[3], SA1_CORNERS[0], SA1_CORNERS[4]]
        self.sa2 = self.img[SA2_CORNERS[1]: SA2_CORNERS[3], SA2_CORNERS[0], SA2_CORNERS[4]]
        self.sa3 = self.img[SA3_CORNERS[1]: SA3_CORNERS[3], SA3_CORNERS[0], SA3_CORNERS[4]]

        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0

    def draw_map(self, last_known):
        """ Displays map with scale, last known x/y coordinates and search areas """
        cv.line(self.img, (20, 370), (70, 370), (0, 0, 0), 2) # Line for Map Scale
        # Text Surrounding Line Scale
        cv.putText(self.img, '0', (8, 370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
        cv.putText(self.img, '50 Nautical Miles', (71, 370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

