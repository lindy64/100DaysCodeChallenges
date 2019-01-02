'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    return datetime.strptime(line.split(sep=" ")[1], "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines):
    lines_to_check = []
    for i in loglines:
        if "Shutdown initiated" in i:
            lines_to_check.append(i)
    return convert_to_datetime(lines_to_check[-1]) - convert_to_datetime(lines_to_check[0])
