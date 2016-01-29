import json
import csv
import requests
import second_pass

'''
# Arbor_Mist 800316826685080
# Black_Box 1380947658816783
# Clos_du_Bois 813429925373770
# Constellation_Brands (retargeting, trade, walgreens) 728442737205823
# Dreaming_Tree 833425423374220

# Estancia 1381091345468800
# Franciscan 852503464799749
# Kim_Crawford 807247179325378
# Marathon 830940790289350
# Mark_West 1374542932792679

# Mark_West_DLX2016 968506049866156
# Mark_West_DLX 728442070539223
# Milestone 843446492372113
# Mouton_Cadet 946615285388566
# Nobilo 815532661830163

# PopCrush 933960369987391
# Ravage 984030844980343
# Rex_Goliath 805588439491252
# RMPS 800317280018368
# Robert_Mondavi Winery(RMW) 832124100171019

# Robert_Mondavi 832124100171019
# Rosatello 915039361879492
# Ruffino 867733226610106
# Simi 852245011492261
# Thorny_Rose 1378201735758977

# Toasted_Head 714007831982647
# Tom_Gore 903219059728189
# Wine_Social_Content_Marketing (905853179464777)
# Woodbridge 800317096685053
# Constellation_Catch_All 108294695945331

SVEDKA 886755114707917
Milestone 843446492372113
'''

accounts_arr = [
    ['SVEDKA', 886755114707917],
    ['Milestone', 843446492372113],
]
for i in accounts_arr:
    second_pass.get_data(i[1], i[0])

for i in accounts_arr:
    second_pass.paginated_json_to_csv(i[0] + '_data_pull.json')





