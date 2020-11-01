class underframe(object):
    """This is a bare underframe object"""
    def __init__(self, *args, **kwargs): 
        pass

    def __call__(self):
        print(self.__doc__)

class security(underframe):
    """This is about memory safety, thread safety, workplace safety,
    you name it, this should also do the error stuffs.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.this = "this"
        self.that = "this"

    def wrap(self, thing):
        print(f"Got it {thing.__doc__}")

class engine(underframe):
    """async framework for running concurrent tasks"""
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.that = "that"

# these underframes will load sequentially and override any
# previously stored functions or variables by name.
FRAMEWORK = (security, engine)

class adventworks(*FRAMEWORK):
    def __init__(self, *args, **kwargs):
        security.__init__(self, *args, **kwargs)
        engine.__init__(self, *args, **kwargs)
        print(self.this, self.that)

    def __call__(self):
        print("Ruckusist.com Advent of Code 2020.")