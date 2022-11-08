from lithops.seercloud.scheduler.data import Data

from . import Operation


class Sort(Operation):

    is_conservative = True
    key: str

    def __init__(self, key: str, **kwargs):

        super(Sort, self).__init__(**kwargs)
        self.key = key

    def run(self, data: Data):

        data.data.sort_values(self.key, inplace=True)




