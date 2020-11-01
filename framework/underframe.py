class underframe(object):
    """This is a bare underframe object"""
    def __init__(self, *args, **kwargs): 
        pass

    def __call__(self):
        print(self.__doc__)