import json
import csv
import requests
import time

# act_id = 
# act_name = ''

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
            time.sleep(.25)
            break

    f.seek(0,2)                 # end of file
    size=f.tell()               # the size of the file
    """ f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
    """
    print('size: ', size)
    f.truncate(size-1)          # delete 1 from end of file
    time.sleep(.25)
    f.write(']\n')              # write a closing bracket
    f.close()                   # close file
    return fb_data

# get_data(act_id, act_name)



def paginated_json_to_csv(file):
    name_len = len(file) - 15
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

                if 'post' in i['name'].lower():
                    continue         # Continue goes to the next loop iteration
                else:
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
                    if i['targeting']['geo_locations'] == {'location_types': ['home', 'recent'], 'countries': ['US']}:
                        new_list.append('National')
                    else:
                        new_list.append('Geographic')
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
                    if i['targeting'].get('connections') != None:
                        new_list.append('Keyword')
                    elif i['targeting'].get('flexible_spec') != None:
                        new_list.append('Keyword')
                    elif i['targeting'].get('interests') != None:
                        new_list.append('Keyword')
                    elif i['targeting'].get('custom_audiences') != None:
                        new_list.append('Keyword')
                    elif i['targeting'].get('friends_of_connections') != None:
                        new_list.append('Keyword')
                    elif i['targeting'].get('behaviors') != None:
                        new_list.append('Behavioral')
                    elif 'dlx' in i['name'].lower():
                        new_list.append('Purchase')
                    else:
                        new_list.append('Demo')
                except KeyError:
                    new_list.append('No Methodology')

                arr_for_csv.append(new_list)
            counter += 1
        except IndexError:
            print('exiting while loop')
            break

    # open CSV and get ready to append stuff
    with open('new_master.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        print('about to write to csv')
        for i in arr_for_csv:
            writer.writerow(i)

    print('csv file closing')
    f.close()
    return arr_for_csv

# paginated_json_to_csv('Rex_Goliath_data_pull.json')









