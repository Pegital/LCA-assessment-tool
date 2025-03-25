import requests
from pprint import pprint



# this function returns the material's LCIA results, for any material uuid found within that database and datastocks
def material_lcia(database_name, datastock_uuid ):
    resp = requests.get("https://oekobaudat.de/" + database_name + "/resource/datastocks/"+ datastock_uuid +"/processes/" + "categories/" +type_+"/" +subcategory+"/"+specific+"?format=json&lang=en")
    tree = resp.json()
    print(tree["totalCount"])
    return tree




# first of all we use this database
database_name= "OEKOBAU.DAT"

# second we use this datastock
datastock_uuid= "cd2bda71-760b-4fcc-8a0b-3877c10000a8"




# # we choose a material/process
#materials_uuid = "bdf06e12-4ed3-4f87-b935-9cbbd23a7f6d"






n=int(input("which category of material:0.mineral 1.Insulation 2.wood 3.metal 4.covering 5.plastic 6.window&curtain wall 7.services 8.Others 9.composites 10.end of life:"))
if n==0:
    type_="Mineral%20building%20products"
if n==1:
    type_="Insulation%20materials"
if n==2:
    type_="Wood"
    subcategory=input("write the subcategory")
    specific=input("write the exact product group")

result_of_categories= material_lcia(database_name, datastock_uuid)
names=[]
item_=result_of_categories["data"]
for i in range(len(item_)):
    
    eachitem=item_[i]
    classification=eachitem["name"]
    classification_UUID=eachitem["uuid"]
    names.append((classification,classification_UUID))
pprint(names)
print(len(names))

