import json
import csv


f = open('Ruffino_data_pull.json', 'r')
arr_for_csv = []
parsed = json.load(f)
# print(parsed['data'][0]['end_time'])

# for i in parsed['data']:
#     new_list = []
#     new_list.append(i['name'])
#     new_list.append(i['start_time'][0:10])
#     try:
#         new_list.append(i['end_time'][0:10])
#     except KeyError:
#         new_list.append(i['insights']['data'][0]['date_stop'])
#     try:
#         new_list.append(i['targeting'])
#     except KeyError:
#         new_list.append('No Targeting Information')
#     new_list.append('N/A')
#     new_list.append(i['name'])
#     try:
#         new_list.append(i['insights']['data'][0]['spend'])
#     except KeyError:
#         new_list.append('Spend Not Available')
#     try:
#         new_list.append(i['targeting']['age_min'])
#     except KeyError:
#         new_list.append('No Targeting')
#     try:
#         new_list.append(i['targeting']['age_max'])
#     except KeyError:
#         new_list.append('No Targeting')
#     try:
#         new_list.append(i['targetingsentencelines'])
#     except KeyError:
#         new_list.append('No Targeting Sentence Lines')

#     arr_for_csv.append(new_list)

# print(arr_for_csv[7])

""" for when json had to be put together into an array form """

# first index is for big json, second index is for adset obj
# print(parsed[0]['data'])
# print(parsed[0]['data'][0]['start_time'])
# print(parsed[1]['data'][0]['name'])
# print(parsed[2]['data'][0]['name'])
# print(len(parsed[0]['data']))


# for i in parsed[0]['data']:
#     print(i['name'])

for i in parsed[1]['data']:
    new_list = []
    new_list.append(i['name'])
    new_list.append(i['start_time'][0:10])
    try:
        new_list.append(i['end_time'][0:10])
    except KeyError:
        new_list.append(i['insights']['data'][0]['date_stop'])
    try:
        new_list.append(i['targeting'])
    except KeyError:
        new_list.append('No Targeting Information')
    new_list.append('N/A')
    new_list.append(i['name'][0:7])
    try:
        new_list.append(i['insights']['data'][0]['spend'])
    except KeyError:
        new_list.append('Spend Not Available')
    try:
        new_list.append(i['targeting']['age_min'])
    except KeyError:
        new_list.append('No Targeting')
    try:
        new_list.append(i['targeting']['age_max'])
    except KeyError:
        new_list.append('No Targeting')
    try:
        new_list.append(i['targetingsentencelines'])
    except KeyError:
        new_list.append('No Targeting Sentence Lines')

    arr_for_csv.append(new_list)

print(arr_for_csv[9])
