class SessionState:
    def __init__(self, session):
        self.session = session

    def key_handler(self, key):
        raise NotImplementedError


class RunningState(SessionState):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def key_handler(self, key):
        if key == ord("q"):
            self.session._state = FinishState(self.session)
        
        if key == ord("a"):
            self.session._state = SessionStateA(self.session)

        if key == ord("b"):
            self.session._state = SessionStateB(self.session)


class SessionStateA(RunningState):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def key_handler(self, key):
        RunningState.key_handler(self, key)
        if key == ord("c"):
            print("I'm in state A")


class SessionStateB(RunningState):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def key_handler(self, key):
        RunningState.key_handler(self, key)
        if key == ord("c"):
            print("I'm in state B")


class FinishState(SessionState):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Finishing!")

