import numpy as np
import cv2

from .loader import Loader
from .updater import Updater
from .producer import Producer
from .displayer import Displayer
from .session_states import RunningState



class Session():
    def __init__(
            self,
            video_dir=None,
            pose_dir=None,
    ):

        self._state = RunningState(self)

        self.loader = Loader(
            session=self,
            video_dir=video_dir
        )

        self.updater = Updater(
            session=self,
            pose_dir=pose_dir
        )

        self.producer = Producer(
            session=self
        )

        self.displayer = Displayer(
            session=self
        )

        self.step = 0
        self.verbose = False

        self.inputs = {}
        self.key = None


    @staticmethod
    def say_hi():
        print("Hi, I'm the session")


    def loop(self):
        """
        Main loop iteration for the session
        """
        # # 1 load sensors
        self.load()
        # 2 update real world objects
        self.update()
        # 3 produce outputs
        self.produce()
        # 4 display outputs
        self.display()

        self.step += 1


    def run(self):
        """
        Function to run the main loop of the session
        """
        self.say_hi()
        while isinstance(self._state, RunningState):
            self.loop()
        return "Closing the app, session has finished"


    def load(self, *args, **kwargs):
        """
        Load information from sensors such as cameras, microphones, 
        frames from video...
        """
        return self.loader.load(*args, **kwargs)

    def update(self, *args, **kwargs):
        """
        Update represented physical world objects based on loaded information,
        infere pose from image, notes from sound, or load previously inferred from json files...
        """
        return self.updater.update(*args, **kwargs)

    def produce(self, *args, **kwargs):
        """
        Produce animation, sounds, etc, using the information of the physical world objects
        """
        return self.producer.produce(*args, **kwargs)

    def display(self, *args, **kwargs):
        """
        Display, reproduce, actuate, given the 
        """
        return self.displayer.display(*args, **kwargs)

