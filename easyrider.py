#!/usr/bin/env python3

import json
from check_data_type import check_data_type
from check_correct_syntax import check_correct_syntax
from bus_line_info import lines_stops, check_start_final_stops, lines_info, check_arrival_time, check_on_demand_stops

json_string = input()
dict_string = json.loads(json_string)

data_type_errors = check_data_type(dict_string)

syntax_errors = check_correct_syntax(dict_string)

lines_stops = lines_stops(dict_string)

if check_start_final_stops(dict_string):
    start_final_transfer_stops = lines_info(dict_string)

time_line = check_arrival_time(dict_string)

on_demand_stops = check_on_demand_stops(dict_string)
