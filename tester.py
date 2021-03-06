import requests
import json
import csv

act_num =
act_name = ''

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
