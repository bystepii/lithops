from typing import Callable

from lithops.seercloud.scheduler.data import Data

from . import Operation


class Filter(Operation):

    is_conservative = False

    def __init__(self, action: Callable, **kwargs):

        super(Filter, self).__init__(**kwargs)
        self.action = action

    def run(self, data: Data):
        data.data = self.action(data.data)
