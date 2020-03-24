class Updater:

    def __init__(self, session):
        self.session = session

    def update(self):
        if self.session.verbose:
            print("step {}: update".format(self.session.step))

        pass