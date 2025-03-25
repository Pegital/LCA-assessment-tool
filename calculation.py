import rhinoscriptsyntax as rs
# getting unite from previouse scope
#geting geometry from rhino
#geting value from GWP
unite=unite[0]
outCome_List=[]
if unite=="Volumen" or unite=="Masse":
    for i in Geometry:
        volume,point=rs.SurfaceVolume(i)
        
        outCome=value*volume
        outCome_List.append(outCome)

if unite=="Fläche":
    for i in Geometry:
        Area,pt=rs.SurfaceArea(i)
        outCome=value*Area
        outCome_List.append(outCome)