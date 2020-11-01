import asyncio
import inspect, concurrent
from .underframe import underframe

class engine(underframe):
    """async framework for running concurrent tasks"""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.loop = asyncio.get_event_loop()
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
        self.that = "that"

    def sink(self, fn, *args, **kwargs):
        """calls either a non async function, or a stack of async functions"""
        if type(fn) is list:
            async def run_all(fnz):
                await asyncio.wait(fnz, return_when=asyncio.ALL_COMPLETED)

            self.loop.run_until_complete(run_all(fn))
        else:
            if inspect.iscoroutinefunction(fn):
                self.loop.run_until_complete(fn, *args, **kwargs)
            else:
                self.loop.run_in_executor(self.executor, fn, *args, **kwargs)