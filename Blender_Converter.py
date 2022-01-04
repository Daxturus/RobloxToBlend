import bpy
import math

#Put worlddata from the Partgetter script here! Copying straight from the console will leave some junk at the front and back of the output -- remove anything separated by a space (including the spaces) from the big chunk of blocks in the middle.
inputText = "" 
outTxt = inputText.split(";")
dataList = []
for x in outTxt:
    dataList.append(x.split(","))

generatedMaterialsList = []
testingMaterialsList = []

for cube in dataList:
    
    
    px = float(cube[4])
    pz = float(cube[5])
    py = float(cube[6])
    sx = float(cube[7]) / 2
    sz = float(cube[8]) / 2
    sy = float(cube[9]) / 2
    
    if cube[0] == "Block":
        ox = float(cube[10]) / 180 * math.pi
        oz = float(cube[11]) / 180 * math.pi
        oy = -float(cube[12]) / 180 * math.pi
        bpy.ops.mesh.primitive_cube_add(location=(px, py, pz), rotation=(ox, oy, oz), scale=(sx, sy, sz))
        obj = bpy.context.object
        obj.color = (float(cube[1])/255,float(cube[2])/255,float(cube[3])/255,1)
    if cube[0] == "Cylinder":
        px = float(cube[4])
        pz = float(cube[5])
        py = float(cube[6])
        sx = float(cube[7]) / 2
        sz = float(cube[8]) / 2
        sy = float(cube[9]) / 2
        oy = -float(cube[10]) / 180 * math.pi
        ox = float(cube[11]) / 180 * math.pi
        oz = float(cube[12]) / 180 * math.pi
        bpy.ops.mesh.primitive_cylinder_add(location=(px, py, pz), rotation=(ox, oy, oz), scale=(sx, sy, sz))
        obj = bpy.context.object
        obj.color = (float(cube[1])/255,float(cube[2])/255,float(cube[3])/255,1)
    if cube[0] == "Ball":
        px = float(cube[4])
        pz = float(cube[5])
        py = float(cube[6])
        sx = float(cube[7]) / 2
        sz = float(cube[8]) / 2
        sy = float(cube[9]) / 2
        ox = float(cube[10]) / 180 * math.pi
        oz = float(cube[11]) / 180 * math.pi
        oy = float(cube[12]) / 180 * math.pi
        bpy.ops.mesh.primitive_ico_sphere_add(location=(px, py, pz), rotation=(ox, oy, oz), scale=(sx, sy, sz))
        obj = bpy.context.object
        obj.color = (float(cube[1])/255,float(cube[2])/255,float(cube[3])/255,1)
    
    found = False
    foundMat = None
    r = float(cube[1])/255
    g = float(cube[2])/255
    b = float(cube[3])/255
    t = 1-math.sqrt(math.sqrt(float(cube[13])))
    s = math.sqrt(math.sqrt(float(cube[14])))
    i = 0
    for mat in testingMaterialsList:
        if found == False:
            if mat[0] == r:
                if mat[1] == g:
                    if mat[2] == b:
                        if mat[3] == t:
                            if mat[4] == s:
                                found = True
                                foundMat = generatedMaterialsList[i]
        i = i + 1
                            
    if found == False:
        mat = bpy.data.materials.new("Material")
        mat.use_nodes = True
        principled = mat.node_tree.nodes['Principled BSDF']
        principled.inputs['Base Color'].default_value = (r,g,b,1)
        principled.inputs['Alpha'].default_value = t
        principled.inputs['Specular'].default_value = s
        obj.data.materials.append(mat)
        matOut = []
        matOut.append(r)
        matOut.append(g)
        matOut.append(b)
        matOut.append(t)
        matOut.append(s)
        testingMaterialsList.append(matOut)
        generatedMaterialsList.append(mat)
    if found == True:
        obj.data.materials.append(foundMat)
