import requests
import json
import csv

# Get adset targeting through acct num
# targetingsentencelines gives more depth

# Ruffino
acct_num = 867733226610106

def get_data(act_id, act_name):
    my_access_token = 'CAAN4vFUE2ZAgBAHaZA6dmP6v4eIxOcV8TtA2crGjLG47ZCEllpjUSUlGFGDIFCX0KQrWBw8OGY9I7vi087ekgpaoldSyaya3HtIJgzC7oR2GQnpE8TfWi8uAB7LqtjMGqtgmvzFXZBTytZCkMDVm9WTC9vBqQZAuxVpj10yyQZC0WigZBaxvKfvG'
    # open a json file with act_id in the file name and make it read/write

    # url with act_id and access_token that pulls all necessary data
    url = 'https://graph.facebook.com/v2.5/act_%d/adsets?fields=name,start_time,end_time,targeting,targetingsentencelines,insights{spend}&limit=100&access_token=%s' % (act_id, my_access_token)
    # make the http request to the url and encode as json
    fb_data = requests.get(url).json()

    f = open('%s_data_pull.json' % act_name, 'a')

    # put JSON into the opened file with indentation
    json.dump(fb_data, f, indent=4, separators=(',', ':'))
    print('json sent to file')

    more_data = requests.get(fb_data['paging']['next']).json()
    json.dump(more_data, f, indent=4, separators=(',', ':'))
    print('data written to file')

    more_data2 = requests.get(more_data['paging']['next']).json()
    json.dump(more_data2, f, indent=4, separators=(',', ':'))
    print('data written to file')

    f.close()
    return fb_data

# get_data(acct_num, 'Ruffino')

# for a single adset
def json_to_csv(file):
    f = open(file, 'r')
    arr_for_csv = []
    parsed = json.load(f)
    print(parsed['data'])

    for i in parsed['data']:
        arr_for_csv.append(i['name'])
        arr_for_csv.append(i['insights']['data'][0]['date_start'])
        arr_for_csv.append(i['insights']['data'][0]['date_stop'])
        arr_for_csv.append(i['targeting'])
        arr_for_csv.append('N/A')
        arr_for_csv.append(i['name'][0:8])
        arr_for_csv.append('$' + str(round(i['insights']['data'][0]['spend'] * 1.15)))
        arr_for_csv.append(i['targeting']['age_min'])
        arr_for_csv.append(i['targeting']['age_max'])
        arr_for_csv.append(i['targeting']['interests'])

    # open CSV and get ready to append stuff
    with open('master.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(arr_for_csv)

    f.close()

# json_to_csv('Popcrush_data_pull.json')

""" function here is for multiple adsets, but not pagination - the loop will try each data point and if it doesn't exist, it will try an equivalent or print none """
def json_to_csv(file):
    f = open(file, 'r')
    arr_for_csv = []
    parsed = json.load(f)
    print(parsed['data'])

    for i in parsed['data']:
        new_list = []
        new_list.append(i['name'])

        try:
            new_list.append(i['start_time'][0:10])
        except KeyError:
            new_list.append(i['insights']['data'][0]['date_stop'])

        try:
            new_list.append(i['end_time'][0:10])
        except KeyError:
            new_list.append(i['insights']['data'][0]['date_stop'])

        try:
            new_list.append(i['targeting'])
        except KeyError:
            new_list.append('No Targeting Information')
        # this is for gender
        new_list.append('N/A')
        # This is for the account name
        new_list.append(i['name'])

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

    # open CSV and get ready to append stuff
    with open('master.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in arr_for_csv:
            writer.writerow(i)

    f.close()

# json_to_csv('')



""" this is for paginated data from facebook """

def paginated_json_to_csv(file):
    f = open(file, 'r')
    arr_for_csv = []
    parsed = json.load(f)

    for i in parsed[2]['data']:
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
        # This is for gender when it is not available
        new_list.append('N/A')
        # This is for the account name
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



    # open CSV and get ready to append stuff
    with open('master.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in arr_for_csv:
            writer.writerow(i)

    f.close()
    return arr_for_csv

# paginated_json_to_csv('Ruffino_data_pull.json')
