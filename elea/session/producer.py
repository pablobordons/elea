class Producer:

    def __init__(self, session):
        self.session = session

    def produce(self):
        if self.session.verbose:
            print("step {}: producing".format(self.session.step))