import json
import csv


f = open('ConstellationBrands_data_pull.json', 'r')
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

            # try:
            #     new_list.append(i['targeting']['geo_locations'])
            # except KeyError:
            #     new_list.append('No Targeting Information')

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


            """
            FOR GETTING TARGETING METHODOLOGY
            One option is to use chained gets:
            value = myDict.get('lastName', myDict.get('firstName', myDict.get('userName')))
            But if you have keySet defined, this might be clearer:
            value = None
            for key in keySet:
                if key in myDict:
                    value = myDict[key]
                    break

            my_dict={'account_0':123445,'seller_account':454545,'seller_account_0':454676, 'seller_account_number':3433343}

            for key, value in my_dict.items():   # iter on both keys and values
                    if key.startswith('seller_account'):
                            print key, value


            flexible_spec --> keyword
            friends_of_connections
            interests --> keyword
            custom_audence --> keyword
            """

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


            # try:
            #     new_list.append(i['targetingsentencelines'])
            # except KeyError:
            #     new_list.append('No Targeting Sentence Lines')


            arr_for_csv.append(new_list)
        counter += 1
    except IndexError:
        break

for i in arr_for_csv:
    print(i, '\n\n')








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
