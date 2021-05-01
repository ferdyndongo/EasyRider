#!/usr/bin/env python3

import re


def check_correct_syntax(json_string):

    error = {'stop_name': 0, 'stop_type': 0, 'a_time': 0}
    for line in json_string:
        if not re.match(r"([A-Z][a-z]+ )+(Road|Avenue|Boulevard|Street)$", str(line['stop_name'])):
            error['stop_name'] += 1
        if str(line['stop_type']) not in "SOF":
            error['stop_type'] += 1
        if not re.match(r"(([01]\d)|(2[0-4])):[0-5]\d$", str(line['a_time'])):
            error['a_time'] += 1
    total = 0
    for key in error:
        total += error[key]
    print(f"""Format validation: {total} errors
    stop_name: {error['stop_name']}
    stop_type: {error['stop_type']}
    a_time: {error['a_time']}""")

    return error
