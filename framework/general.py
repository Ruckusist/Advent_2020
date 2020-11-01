import os
from .underframe import underframe

class general(underframe):
    def whoami(self):
        print(os.getcwd())

    def fib(self, x): pass

    def factor(self, x): pass