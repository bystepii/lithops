
from lithops.seercloud.scheduler.data import Data

from . import Operation


class Collect(Operation):

    is_conservative = True

    def __init__(self, **kwargs):

       super(Collect, self).__init__(**kwargs)

    def run(self, data: Data):

        data.return_value = data.data
