from collections import namedtuple
from dataclasses import dataclass
from PIL import Image
import numpy as np
import math
import io
import base64

@dataclass
class BoundingBox:
    x: int
    y: int
    width: int
    height: int

class HeatMapGenerator():
    mFeathering = 40
    mMaxContrib = 10
    mContribClip = 300.0

    def __init__(self, width, height, boundingBoxes):
        self.mWidth = width
        self.mHeight = height
        self.mBoundingBoxes = boundingBoxes
        self.mSumTable = np.zeros(shape=(height, width))
        self.mHeatMap = np.zeros((height, width, 3), dtype=np.uint8)

    def computeHeatMap(self):
        for bb in self.mBoundingBoxes:
            width = bb.width
            height = bb.height
            x = bb.x
            y = bb.y

            cX = int(x + width/2)
            cY = int(y + height/2)
            for a in range(cX - self.mFeathering, cX + self.mFeathering):
                # print(a)
                if a < 0 or a >= self.mWidth:
                    continue
                distA = (cX - a)**2
                # print(distA)
                for b in range(cY - self.mFeathering, cY + self.mFeathering):
                    if b < 0 or b >= self.mHeight :
                        continue
                    distB = (cY - b)**2
                    dist = math.sqrt(distA + distB)
                    if dist <= self.mFeathering:
                        self.mSumTable[b,a] += (float(self.mFeathering) - dist)/float(self.mFeathering) * self.mMaxContrib

        for i in range(0, self.mHeight-1):
            for j in range(0, self.mWidth-1):
                val = float(self.mSumTable[i,j])/self.mContribClip * 255
                grayscale = max(0, min(255, int(val)))
                if grayscale > 255:
                    print(f'Val {i} {j} {val}')
                self.mHeatMap[i,j] = [grayscale, grayscale, grayscale]

        self.mImg = Image.fromarray(self.mHeatMap, 'RGB')
        buf = io.BytesIO()
        self.mImg.save(buf, format="PNG")
        print('SAVED IMAGE')
        return base64.b64encode(buf.getvalue())
