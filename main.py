import requests
import json
import csv

# Get adset targeting through acct num
# targetingsentencelines gives more depth

act_num = 108294695945331
act_name = 'Constlltn_Mar_Sep_14'

def get_data(act_id, act_name):
    my_access_token = 'CAAN4vFUE2ZAgBAHaZA6dmP6v4eIxOcV8TtA2crGjLG47ZCEllpjUSUlGFGDIFCX0KQrWBw8OGY9I7vi087ekgpaoldSyaya3HtIJgzC7oR2GQnpE8TfWi8uAB7LqtjMGqtgmvzFXZBTytZCkMDVm9WTC9vBqQZAuxVpj10yyQZC0WigZBaxvKfvG'

    # url with act_id and access_token that pulls all necessary data
    url = 'https://graph.facebook.com/v2.5/act_%d/adsets?fields=name,start_time,end_time,targeting,targetingsentencelines,insights{spend}&limit=25&access_token=%s' % (act_id, my_access_token)
    # make the http request to the url and encode as json

    f = open('%s_data_pull.json' % act_name, 'a')
    f.write('[\n')

    fb_data = requests.get(url).json()
    json.dump(fb_data, f, indent=4, separators=(',', ':'))
    print('json written to file')
    f.write(',\n')

    """ big improvement over the last version. key here is we are assigning the request to the same variable, and then checking that newly updated varibale each time for the [paging][next] data point. if it's not there, we will get a KeyError. """

    while True:
        try:
            fb_data = requests.get(fb_data['paging']['next']).json()
            json.dump(fb_data, f, indent=4, separators=(',', ':'))
            print('json written in while loop')
            f.write(',\n')
        except KeyError:
            print('no more data')
            break

    f.write(']\n')
    f.close()
    return fb_data

# get_data(act_num, act_name)




""" this is for paginated data from facebook """

def paginated_json_to_csv(file):
    name_len = len(act_name)
    f = open(file, 'r')
    arr_for_csv = []
    parsed = json.load(f)

    # Need to reset the index to zero every time this function runs
    for i in parsed[11]['data']:
        new_list = []
        gender_arr = i['targetingsentencelines']['targetingsentencelines']
        new_list.append(i['name'])
        new_list.append(i['start_time'][0:10])

        try:
            new_list.append(i['end_time'][0:10])
        except KeyError:
            try:
                new_list.append(i['insights']['data'][0]['date_stop'])
            except KeyError:
                new_list.append('Date Not Available')

        try:
            new_list.append(i['targeting'])
        except KeyError:
            new_list.append('No Targeting Information')

        # for gender
        try:
            if {'content': 'Gender:', 'children': ['Female']} in gender_arr:
                new_list.append('Female')
            elif {'content': 'Gender:', 'children': ['Male']} in gender_arr:
                new_list.append('Male')
            else:
                new_list.append('No Gender Data')
        except KeyError:
            new_list.append('No Gender Data Available')

        # This is for the account name
        new_list.append(i['name'][0:name_len])

        try:
            new_list.append(i['insights']['data'][0]['spend'] * 1.15)
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
        print('completed loop')
        arr_for_csv.append(new_list)

    # open CSV and get ready to append stuff
    with open('master.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in arr_for_csv:
            writer.writerow(i)

    f.close()
    return arr_for_csv

# paginated_json_to_csv('Constlltn_Mar_Sep_14_data_pull.json')
