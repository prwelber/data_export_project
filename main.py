import requests
import json
import csv

# Get adset targeting through acct num
# targetingsentencelines gives more depth

act_num = 968506049866156
act_name = 'Mark_West_DLX2016'

def get_data(act_id, act_name):
    my_access_token = 'CAAN4vFUE2ZAgBAHaZA6dmP6v4eIxOcV8TtA2crGjLG47ZCEllpjUSUlGFGDIFCX0KQrWBw8OGY9I7vi087ekgpaoldSyaya3HtIJgzC7oR2GQnpE8TfWi8uAB7LqtjMGqtgmvzFXZBTytZCkMDVm9WTC9vBqQZAuxVpj10yyQZC0WigZBaxvKfvG'
    # open a json file with act_id in the file name and make it read/write

    # url with act_id and access_token that pulls all necessary data
    url = 'https://graph.facebook.com/v2.5/act_%d/adsets?fields=name,start_time,end_time,targeting,targetingsentencelines,insights{spend}&limit=25&access_token=%s' % (act_id, my_access_token)
    # make the http request to the url and encode as json
    fb_data = requests.get(url).json()

    f = open('%s_data_pull.json' % act_name, 'a')
    f.write('[\n')

    # put JSON into the opened file with indentation
    json.dump(fb_data, f, indent=4, separators=(',', ':'))
    print('json written to file')
    f.write(',\n')

    """ This is what happens when you don't understand pagination quite yet """

    more_data = requests.get(fb_data['paging']['next']).json()
    json.dump(more_data, f, indent=4, separators=(',', ':'))
    print('json written to file')
    f.write(',\n')

    try:
        more_data2 = requests.get(more_data['paging']['next']).json()
        json.dump(more_data2, f, indent=4, separators=(',', ':'))
        print('json written to file')
        f.write(',\n')
    except KeyError:
        print('no data2 and no more json available')

    # try:
    #     more_data3 = requests.get(more_data2['paging']['next']).json()
    #     json.dump(more_data3, f, indent=4, separators=(',', ':'))
    #     print('json written to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('no data3 and no more json')


    # more_data4 = requests.get(more_data3['paging']['next']).json()
    # json.dump(more_data4, f, indent=4, separators=(',', ':'))
    # print('json written to file')
    # f.write(',\n')

    # more_data5 = requests.get(more_data4['paging']['next']).json()
    # json.dump(more_data5, f, indent=4, separators=(',', ':'))
    # print('json written to file')
    # f.write(',\n')

    # more_data6 = requests.get(more_data5['paging']['next']).json()
    # json.dump(more_data6, f, indent=4, separators=(',', ':'))
    # print('json written to file')
    # f.write(',\n')

    # more_data7 = requests.get(more_data6['paging']['next']).json()
    # json.dump(more_data7, f, indent=4, separators=(',', ':'))
    # print('json written to file')
    # f.write(',\n')

    # try:
    #     more_data8 = requests.get(more_data7['paging']['next']).json()
    #     json.dump(more_data8, f, indent=4, separators=(',', ':'))
    #     print('json written to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('this is the end, no data8 and no more json!')

    # try:
    #     more_data9 = requests.get(more_data8['paging']['next']).json()
    #     json.dump(more_data9, f, indent=4, separators=(',', ':'))
    #     print('json written to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('this is the end, no data9 and no json!')


    # try:
    #     more_data10 = requests.get(more_data9['paging']['next']).json()
    #     json.dump(more_data10, f, indent=4, separators=(',', ':'))
    #     print('json written to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('this is the end, no data10 and no more json!')

    # try:
    #     more_data11 = requests.get(more_data10['paging']['next']).json()
    #     json.dump(more_data11, f, indent=4, separators=(',', ':'))
    #     print('json wrote out to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('no data11 and no more json')

    # try:
    #     more_data12 = requests.get(more_data11['paging']['next']).json()
    #     json.dump(more_data12, f, indent=4, separators=(',', ':'))
    #     print('json wrote out to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('no data12 and no more json')

    # try:
    #     more_data13 = requests.get(more_data12['paging']['next']).json()
    #     json.dump(more_data13, f, indent=4, separators=(',', ':'))
    #     print('json written to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('no data13 and no more json')

    # try:
    #     more_data14 = requests.get(more_data13['paging']['next']).json()
    #     json.dump(more_data14, f, indent=4, separators=(',', ':'))
    #     print('json written to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('no data14 and no more json')

    # try:
    #     more_data15 = requests.get(more_data14['paging']['next']).json()
    #     json.dump(more_data15, f, indent=4, separators=(',', ':'))
    #     print('json written to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('no data15 and no more json')

    # try:
    #     more_data16 = requests.get(more_data15['paging']['next']).json()
    #     json.dump(more_data16, f, indent=4, separators=(',', ':'))
    #     print('json written to file')
    #     f.write(',\n')
    # except KeyError:
    #     print('no data16 and no more json')

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

    for i in parsed[1]['data']:
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

# paginated_json_to_csv('Mark_West_DLX2016_data_pull.json')
