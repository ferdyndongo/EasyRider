#!/usr/bin/env python3


def lines_stops(json_string):

    lines = {}
    for line in json_string:
        if line['bus_id'] in lines:
            lines[line['bus_id']] += 1
        else:
            lines[line['bus_id']] = 1
    print("Line names and number of stops:")
    for key in lines:
        print(f"bus_id: {key}, stops: {lines[key]}")

    return lines


def check_start_final_stops(json_string):
    stop_lines = {}
    for bus_line in json_string:
        line = bus_line['bus_id']
        stop_type = bus_line['stop_type']
        if line in stop_lines:
            if stop_type not in stop_lines[line]:
                stop_lines[line][stop_type] = 1
            else:
                stop_lines[line][stop_type] += 1
        else:
            stop_lines[line] = {stop_type: 1}
    for line in stop_lines:
        if 'S' not in [stop for stop in stop_lines[line]] or 'F' not in [stop for stop in stop_lines[line]]:
            print(f"There is no start or end stop for the line: {line}")
            return False


def lines_info(json_string):
    stops = {}
    start_stops = []
    finish_stops = []
    for line in json_string:
        stop = line['stop_name']
        if stop not in stops:
            stops[stop] = 1
        else:
            stops[stop] += 1
        if line['stop_type'] == 'S':
            if stop not in start_stops:
                start_stops.append(stop)
        elif line['stop_type'] == 'F':
            if stop not in finish_stops:
                finish_stops.append(stop)
    transfer_stops = {key: value for key, value in stops.items() if value > 1}
    print(f"""Start stops: {len(start_stops)} {sorted(start_stops)}
Transfer stops: {len(transfer_stops)} {sorted([stop for stop in transfer_stops])}
Finish stops: {len(finish_stops)} {sorted(finish_stops)}""")


def check_arrival_time(json_string):
    time_line = {}
    time_error = {}
    for bus_lines in json_string:
        line = bus_lines['bus_id']
        stop_name = bus_lines['stop_name']
        arr_time = bus_lines['a_time']
        if line not in time_line:
            time_line[line] = {stop_name: arr_time}
            current_time = arr_time
        else:
            time_line[line][stop_name] = arr_time
            if arr_time <= current_time:
                if line not in time_error:
                    time_error[line] = stop_name

            current_time = arr_time
    if len(time_error) == 0:
        print("""Arrival time test:
    OK""")
    else:
        print("Arrival time test:")
        for key, value in time_error.items():
            print(f"bus_id line {key}: wrong time on {value}")
    return time_line


def check_on_demand_stops(json_string):
    on_demand_stops = []
    error_stops = []
    for bus_lines in json_string:
        if bus_lines['stop_type'] == 'O':
            on_demand_stops.append(bus_lines['stop_name'])
    for stop in on_demand_stops:
        for bus_lines in json_string:
            if bus_lines['stop_name'] == stop and bus_lines['stop_type'] in 'SF':
                error_stops.append(stop)
    if len(error_stops) == 0:
        print("On demand stops test:\nOK")
    else:
        print(f"On demand stops test:\nWrong stop type: {sorted(error_stops)}")

    return on_demand_stops
