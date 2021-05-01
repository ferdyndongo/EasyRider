#!/usr/bin/env python3
import re


def check_data_type(json_string):
    error = {'bus_id': 0, 'stop_id': 0, 'stop_name': 0, 'next_stop': 0, 'stop_type': 0, 'a_time': 0}
    for line in json_string:
        if type(line['bus_id']) != int:
            error['bus_id'] += 1
        if type(line['stop_id']) != int:
            error['stop_id'] += 1
        if not re.match(r"[A-Za-z]+", str(line['stop_name'])):
            error['stop_name'] += 1
        if type(line['next_stop']) != int:
            error['next_stop'] += 1
        if str(line['stop_type']) not in "SOF":
            error['stop_type'] += 1
        if not re.match(r"\d\d:\d\d", str(line['a_time'])):
            error['a_time'] += 1
    total = 0
    for key in error:
        total += error[key]
    print(f"""Type and required field validation: {total} errors
    bus_id: {error['bus_id']}
    stop_id: {error['stop_id']}
    stop_name: {error['stop_name']}
    next_stop: {error['next_stop']}
    stop_type: {error['stop_type']}
    a_time: {error['a_time']}""")

    return error
