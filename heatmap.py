from collections import namedtuple
from dataclasses import dataclass
from PIL import Image
import numpy as np
import math

@dataclass
class BoundingBox:
    x: int
    y: int
    width: int
    height: int

class HeatMapGenerator():
    mFeathering = 40
    mMaxContrib = 10
    mContribClip = 100.0

    def __init__(self, width, height, boundingBoxes):
        self.mWidth = width
        self.mHeight = height
        self.mBoundingBoxes = boundingBoxes
        self.mSumTable = np.zeros(shape=(height, width))
        self.mHeatMap = np.zeros((width, height, 3), dtype=np.uint8)

    def computeHeatMap(self):
        for bb in self.mBoundingBoxes:
            width = bb.width
            height = bb.height
            x = bb.x
            y = bb.y

            cX = int(x + width/2)
            cY = int(y + height/2)
            for a in range(cX - self.mFeathering, cX + self.mFeathering):
                print(a)
                if a < 0 or a >= self.mWidth:
                    continue
                distA = (cX - a)**2
                print(distA)
                for b in range(cY - self.mFeathering, cY + self.mFeathering):
                    if b < 0 or b >= self.mHeight :
                        continue
                    distB = (cY - b)**2
                    dist = math.sqrt(distA + distB)
                    if dist <= self.mFeathering:
                        self.mSumTable[b,a] += (float(self.mFeathering) - dist)/float(self.mFeathering) * self.mMaxContrib

        for i in range(0, self.mHeight):
            for j in range(0, self.mWidth):
                val = float(self.mSumTable[i,j])/self.mContribClip * 255
                if val > 0.0:
                    print(f'Val {i} {j} {val}')
                self.mHeatMap[i,j] = [val, val, val]

        self.mImg = Image.fromarray(self.mHeatMap, 'RGB')
        self.mImg.save('heatmap.png')
        self.mImg.show()


bbs = [
    BoundingBox(128, 128, 40, 40),
    BoundingBox(138, 128, 40, 40),
    BoundingBox(148, 128, 40, 40),
    BoundingBox(158, 128, 40, 40),
    BoundingBox(168, 128, 40, 40),
    BoundingBox(178, 128, 40, 40),
    BoundingBox(188, 128, 40, 40),
    BoundingBox(198, 128, 40, 40),
    BoundingBox(128, 128, 40, 40),
    BoundingBox(138, 128, 40, 40),
    BoundingBox(148, 128, 40, 40),
    BoundingBox(158, 128, 40, 40),
    BoundingBox(168, 128, 40, 40),
    BoundingBox(178, 128, 40, 40),
    BoundingBox(188, 128, 40, 40),
    BoundingBox(198, 128, 40, 40)
]
hm = HeatMapGenerator(512, 512, bbs)
hm.computeHeatMap()



