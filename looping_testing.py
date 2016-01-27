import json
import csv


f = open('Clos_du_Bois_data_pull.json', 'r')
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
# print(parsed[0]['data'][20]['targetingsentencelines']['targetingsentencelines'][3]['children'][0])
""" For grabbing the gender we will have to loop through """
# print(parsed[0]['data'][20]['targetingsentencelines']['targetingsentencelines'])
# arr = parsed[0]['data'][20]['targetingsentencelines']['targetingsentencelines']
# print(arr, '\n')
# for i in arr:
#     print(i)
# if {'content': 'Gender:', 'children': ['Female']} in arr:
#     print('found it')

# print(parsed[0]['data'][20]['targetingsentencelines']['targetingsentencelines'])

# print(parsed[0]['data'][0]['start_time'][0:10])
# print(parsed[0]['data'][0]['end_time'][0:10])
# print(parsed[1]['data'][0]['name'])


# for i in parsed[0]['data']:
#     print(i['name'])

# for i in parsed[25]['data']:
#     new_list = []
#     new_list.append(i['name'])
#     new_list.append(i['start_time'][0:10])
#     gender_arr = i['targetingsentencelines']['targetingsentencelines']

#     try:
#         new_list.append(i['end_time'][0:10])
#     except KeyError:
#         try:
#             new_list.append(i['insights']['data'][0]['date_stop'])
#         except KeyError:
#             new_list.append('Date Not Available')

#     try:
#         new_list.append(i['targeting'])
#     except KeyError:
#         new_list.append('No Targeting Information')

#     try:
#         if {'content': 'Gender:', 'children': ['Female']} in gender_arr:
#             new_list.append('Female')
#         elif {'content': 'Gender:', 'children': ['Male']} in gender_arr:
#             new_list.append('Male')
#         else:
#             new_list.append('No Gender Data')
#     except KeyError:
#         new_list.append('No Gender Data Available')

#     new_list.append(i['name'][0:10])
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

# print(arr_for_csv[14])


arr_for_csv = []

counter = 0
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



