from .underframe import underframe


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