

import requests
from pprint import pprint

type_="category"#getting it from humanUI user inteface
subcategory="subcategory"#getting it from humanUI user inteface
specific="specefic material"#getting it from humanUI user inteface
        
        


def material_lcia(database_name, datastock_uuid ):
    resp = requests.get("https://oekobaudat.de/" + database_name + "/resource/datastocks/"+ datastock_uuid +"/processes/" + "categories/" +type_+"/" +subcategory+"/"+specific+"?format=json&lang=en")
    tree = resp.json()
    print(tree["totalCount"])
    return tree




# first of all we use this database
database_name= "OEKOBAU.DAT"

# second we use this datastock
datastock_uuid= "cd2bda71-760b-4fcc-8a0b-3877c10000a8"






result_of_categories= material_lcia(database_name, datastock_uuid)
names=[]
uuids=[]
Name_uuid=[]
item_=result_of_categories["data"]
for i in range(len(item_)):
    
    eachitem=item_[i]
    classification=eachitem["name"]
    classification_UUID=eachitem["uuid"]
    names.append(classification)
    uuids.append(classification_UUID)
    Name_uuid.append((classification+" / "+classification_UUID))
pprint(names)
print(len(names))
