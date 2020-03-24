import cv2

class Displayer:

    def __init__(self, session):
        self.session = session

    def display(self):
        if self.session.verbose:
            print("step {}: displaying".format(self.session.step))  

        cv2.imshow("", self.session.inputs["background"])

        key = cv2.waitKey(1)   
        self.session._state.key_handler(key)