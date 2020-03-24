import numpy as np

class Loader:

    def __init__(self, session, video_dir=None):
        self.session = session
        self.video_dir = video_dir

    def load(self):
        if self.session.verbose:
            print("step {}: loading".format(self.session.step))
        
        self.session.inputs = {
            "background": self.black_image(height=720, width=1280, channels=3)
        }

    @staticmethod
    def black_image(height, width, channels):
        return np.zeros((height, width, channels), dtype=np.uint8)

