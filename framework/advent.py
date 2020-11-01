import time
import asyncio
from .engine import engine
from .security import security
from .general import general

# these underframes will load sequentially and override any
# previously stored functions or variables by name.
FRAMEWORK = (security, engine, general)

class adventworks(*FRAMEWORK):
    def __init__(self, *args, **kwargs):
        security.__init__(self, *args, **kwargs)
        engine.__init__(self, *args, **kwargs)
        print(self.this, self.that)

    async def long_func(self, x):
        await asyncio.sleep(2*x)
        print('long func {} complete.'.format(x))

    async def short_func(self, x):
        await asyncio.sleep(.6*x)
        print('short func {} complete'.format(x))

    def sht_func(self, x):
        time.sleep(.6*x)
        print(f"non async func finished {x} secs")

    def __call__(self):
        self.sink(
            self.sink([self.long_func(0), self.short_func(0), self.long_func(1), 
                   self.short_func(1), self.long_func(2), self.short_func(2)]),
            self.sink(self.whoami)
            )
        # time.sleep(5)
        print("Ruckusist.com Advent of Code 2020.")