from lithops.seercloud.IO.write import write_obj
from lithops.seercloud.scheduler.data import Data
from lithops.seercloud.utils.serialize import serialize

from . import Operation


class Write(Operation):

    out: str
    key: None

    def __init__(self, bucket: str = None, key: str = None, **kwargs):

        super(Write, self).__init__(**kwargs)

        self.bucket = bucket
        self.key = key

    def run(self, data: Data):

        self.storage = self.data_info.storage

        body = serialize(data.data)

        if self.bucket is None:
            self.bucket = self.task_info.write_bucket

        if self.key is None:
            write_obj(storage=self.storage,
                      Bucket=self.bucket,
                      Key=self.task_info.read_path,
                      suffixes=["out", str(self.task_info.surname_out), str(self.task_info.task_id)],
                      delimiter="/",
                      Body=body)
        else:
            write_obj(storage=self.storage,
                      Bucket=self.bucket,
                      Key=self.key,
                      suffixes=["%d" % self.task_info.task_id],
                      Body=body,
                      delimiter="/")
