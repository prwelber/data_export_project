import requests
import json
import csv
import os

# Get adset targeting through acct num
# targetingsentencelines gives more depth

act_num = 852503464799749
act_name = 'Franciscan'

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
            f.write(',')
        except KeyError:
            print('no more data')
            break

    f.seek(0,2)                 # end of file
    size=f.tell()               # the size...
    print('size: ', size)
    f.truncate(size-1)          # delete byte 2 bytes from end of file
    f.write(']\n')              # write a closing bracket
    f.close()                   # close file
    return fb_data

get_data(act_num, act_name)






""" this is for paginated data from facebook """

"""
What's happening here is first we're referencing the length of the account name to use to slice a string. Then we're opening the json file that was written in the previous function. then we're opening an empty array which will eventually be written to a csv file. Then we parse the JSON. Then we set a counter to zero and enter a while loop. In the while loop we try a for loop over the parsed JSON. We use the counter variable to reference an index in the parsed JSON which is just a big list. We begin each loop with a new empty array. We try/except various data points and at the end of each loop we append the [new_list] to the [arr_for_csv] that we created at the beginning of the function. When the for loop is over, the counter increases by one and the while loop, which is running because we set it to True, will run another for loop, but with an increased counter (index value), and so on. When the index throws an error, we break out of the Whlie loops. Then we open to the csv and write to it, looping over the [arr_for_csv] we just created with the while and for loops. arr_for_csv is a list with lots of lists inside it. each interior list will be a row.
"""

def paginated_json_to_csv(file):
    name_len = len(act_name)
    f = open(file, 'r')
    arr_for_csv = []
    parsed = json.load(f)
    counter = 0
    print('entering while loop')
    while True:
        try:
            for i in parsed[counter]['data']:
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

                arr_for_csv.append(new_list)
            counter += 1
        except IndexError:
            print('exiting while loop')
            break

    # open CSV and get ready to append stuff
    with open('test.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        print('about to write to csv')
        for i in arr_for_csv:
            writer.writerow(i)

    print('csv file closing')
    f.close()
    return arr_for_csv

paginated_json_to_csv('Franciscan_data_pull.json')
