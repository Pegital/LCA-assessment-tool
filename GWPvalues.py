import requests
from pprint import pprint

materials_uuid="getting the material UUID from previouse scope"

# this function returns the material's LCIA results, for any material uuid found within that database and datastocks
def material_lcia(database_name, datastock_uuid , material_uuid):
    resp = requests.get("https://oekobaudat.de/" + database_name + "/resource/datastocks/"+ datastock_uuid +"/processes/" + material_uuid  + "?format=json")
    tree = resp.json()
    LCA=tree["LCIAResults"]["LCIAResult"]
    unit=tree["exchanges"]["exchange"][0]["referenceToFlowDataSet"]["refObjectId"]
    return LCA,unit


def material_unit1(database_name, unit):
    resp = requests.get("https://oekobaudat.de/" + database_name +"/resource/flows/" + unit  + "?format=json")
    tree = resp.json()
    refid=tree["flowProperties"]["flowProperty"][0]["referenceToFlowPropertyDataSet"]["refObjectId"]
    return refid

def material_unit2(database_name, refid):
    resp = requests.get("https://oekobaudat.de/" + database_name +"/resource/flowproperties/" + refid  + "?format=json")
    tree = resp.json()
    un=tree["flowPropertiesInformation"]["dataSetInformation"]["name"][0]["value"]
    return un

# first of all we use this database
database_name= "OEKOBAU.DAT"

# second we use this datastock
datastock_uuid= "cd2bda71-760b-4fcc-8a0b-3877c10000a8"









result_of_first_lcia= material_lcia(database_name, datastock_uuid, materials_uuid)

refid=material_unit1(database_name, result_of_first_lcia[1])
unite_=material_unit2(database_name, refid)
# # printing the first result of common:other epd's

#flattening
chosen_result=result_of_first_lcia[0][1]

pprint(chosen_result)
print(len(chosen_result))
ex1=chosen_result['other']
ex2=ex1['anies']
number=(len(ex2))

if number>1:
    print("yay")
    ex3=ex2[1]
    A1_A3=ex3["value"]
if number>2:
    ex4=ex2[2]
    C1=ex4["value"]
if number>3:
    ex5=ex2[3]
    C2=ex5["value"]
if number>4:
    ex6=ex2[4]
    C3=ex6["value"]
if number>5:
    ex7=ex2[5]
    C4=ex7["value"]
if number>6:
    ex8=ex2[6]
    D=ex8["value"]

