
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
