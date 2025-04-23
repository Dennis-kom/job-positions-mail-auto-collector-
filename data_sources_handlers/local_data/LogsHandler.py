import logging
from os.path import exists
import datetime

from data_sources_handlers.inner_data_protocols.activity_date_time import ActivityDate


class LogsParser:

    logs_file_path: str = ""
    today_data: str = ""
    def __init__(self, logs_path: str = 'default'):

        # validating that the path is correct and the logs file exists there
        if exists(logs_path):
            self.logs_file_path = logs_path
            self.today_date = str(datetime.date.today())
            self.logs_inputs = []

            # opening the logs file for reading
            with open(self.logs_file_path, "r") as log:
                for line in log.readlines():
                    self.logs_inputs.append(line)


    def get_last_activity_date(self) -> ActivityDate:
        pass
