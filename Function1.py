import cv2
class movility:
    
    def __init__(self, x, y, f):
        self.coo1=x
        self.coo2=y
        self.f=f

    def mov(self, d, f):
        self.coo1 = self.coo1 + 1
        d=self.coo1
        print("Point", d)