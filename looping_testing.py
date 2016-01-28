import json
import csv


f = open('Rex_Goliath_data_pull.json', 'r')
arr_for_csv = []
parsed = json.load(f)




arr_for_csv = []
counter = 0
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
            new_list.append(i['name'][0:19])

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
        break

for i in arr_for_csv:
    print(i)
    print('\n')








"""

Maybe we can do something like if targeting['geo_locations'] == countries:['US']
or something like that to get national vs geo



"targeting":{
                "geo_locations":{
                    "countries":[
                        "US"
                    ],
                    "location_types":[
                        "home",
                        "recent"
                    ]
                },
                "age_max":65,
                "age_min":21,
                "page_types":[
                    "desktopfeed",
                    "mobilefeed"
                ],
                "connections":[
                    {
                        "id":"58905582846",
                        "name":"Woodbridge by Robert Mondavi"
                    }
                ]
            }

"""
