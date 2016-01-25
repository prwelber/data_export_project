import csv
import json

data = {'paging': {'cursors': {'after': 'NjAyNTk2ODIyMTI1NQZDZD', 'before': 'NjAyNTk2ODIyMTI1NQZDZD'}}, 'data': [{'id': '6025968221255', 'targeting': {'age_min': 21, 'geo_locations': {'countries': ['US'], 'location_types': ['home', 'recent']}, 'interests': [{'name': 'Lake Tahoe', 'id': '6002968743692'}, {'name': 'Wine', 'id': '6003148544265'}, {'name': 'California', 'id': '6003419041839'}, {'name': 'San Diego', 'id': '6003734568553'}, {'name': 'Palm Springs, California', 'id': '6003979723748'}, {'name': 'Travel', 'id': '6004160395895'}], 'age_max': 65, 'page_types': ['rightcolumn']}, 'name': 'PopCrush 2016 RHS', 'start_time': '2015-04-01T12:00:00-0400', 'targetingsentencelines': {'targetingsentencelines': [{'children': ['United States'], 'content': 'Location:'}, {'children': ['Lake Tahoe, Wine, California, San Diego, Palm Springs, California or Travel'], 'content': 'Interests:'}, {'children': ['21 - 65+'], 'content': 'Age:'}, {'children': ['Right column on desktop computers'], 'content': 'Placements:'}], 'id': '/targetingsentencelines'}, 'end_time': '2015-05-31T23:59:00-0400', 'insights': {'paging': {'cursors': {'after': 'MAZDZD', 'before': 'MAZDZD'}}, 'data': [{'spend': 8695.6499999999996, 'date_start': '2015-04-01', 'date_stop': '2015-05-31'}]}}]}

# data = data['data'][0]
# insights = data['insights']
# targeting = data['targeting']
# print(data)
# print(data['name'])
# print(insights['data'][0]['date_start'])
# print(insights['data'][0]['date_stop'])
# print(targeting)
# print('n/a')
# print(data['name'][0:8])
# print('$' + str(insights['data'][0]['spend'] * 1.15))
# print(targeting['age_min'])
# print(targeting['age_max'])
# print(targeting['interests'])
arr_for_csv = []
for i in data['data']:
  arr_for_csv.append(i['name'])
  arr_for_csv.append(i['insights']['data'][0]['date_start'])
  arr_for_csv.append(i['insights']['data'][0]['date_stop'])
  arr_for_csv.append(i['targeting'])
  arr_for_csv.append('no gender')
  arr_for_csv.append(i['name'][0:8])
  arr_for_csv.append('$' + str(round(i['insights']['data'][0]['spend'] * 1.15)))
  arr_for_csv.append(i['targeting']['age_min'])
  arr_for_csv.append(i['targeting']['age_max'])
  arr_for_csv.append(i['targeting']['interests'])


print(arr_for_csv)

with open('some.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(arr_for_csv)




