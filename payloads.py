import json
from variables import Uuid as v126


def get_payload(json_file):
    with open(json_file) as f:
        payload = f.read()
    return payload


def put_parameter(json_file, parameter, value):
    with open(json_file) as f:
        file = f.read()
    data = json.loads(file)
    try:
        data[parameter] = value
        with open(json_file, 'w') as f:
            f.write(json.dumps(data))
    except Exception:
        pass


def correct_start_time(json_file):
    put_parameter(json_file, 'startTime', v126.time_now)


def correct_code(json_file, value):
    put_parameter(json_file, 'code', value)


#def correct_end_time(json_file):
    #put_parameter(json_file, 'endTime', v126.time_now)


#def correct_sampling_date(json_file):
    #put_parameter(json_file, 'sampleAnalysisRequests[*].samplingDate', v126.time_now)


def correct_dates(json_file, start_time=None, end_time=None, sampling_date=None):
    if start_time is not None:
        correct_start_time(json_file)
    #if end_time is not None:
        #correct_end_time(json_file)
    #if sampling_date is not None:
        #correct_sampling_date(json_file)


class Payloads:
    def __init__(self):
        self.material = v126.material
        self.st = v126.sample_template
        self.subdivision = v126.subdivision
        self.sample_point = v126.sampling_point


