######################################
# Script identifier les informations 
# concernant les positions des vertices, 
# faces et texturage
######################################

'''Les vertices sont stockées dans : bpy.data.meshes.vertices[i]
On peut obtenir les coordonnées de chaque vertices avec ___.vertices[i].co[0]...[1]...[2] (x,y,z)

Les bords (edges) du mesh sont stockés dans : bpy.data.meshes.edges[i]
On peut obtenir les points (p1,p2) qui construisent chaque edge avec ____.edges[i].vertices

Pour calculer la triangulisation du mesh, il faut utiliser bpy.data.meshes.calc_looptriangles()
Les triangles sont stockés dans : bpy.data.meshes.loop_triangles
On peut obtenir les couples (p1,p2,p3) qui construisent chaque triangle avec ___.loop_triangle.vertices[0]..[1]..[2] (p1,p2,p3)'''

import bpy, bpy_extras
import numpy as np


name = bpy.data.objects[1].name
me = bpy.data.meshes[name]
print("Voici les caractéristiques de votre mesh nommé :",name)

# génération matrice des coordonées des vertices :
vts = []
for vert in me.vertices :
    vts.append([vert.co[0],vert.co[1],vert.co[2]])
vts_mtx = np.matrix(vts)

print("Matrice des coordonnées des vertices : bpy.data.meshes.vertices[i].vertices[i].co[0]...[1]...[2] x=0,y=1,z=2")
for i in range(len(vts_mtx)):
    if i > 2 and i < len(vts_mtx)-1:
        pass
    elif i == len(vts_mtx)-1:
        print("...")
        print("Vert_"+str(i),vts_mtx[i])
    else :
        print("Vert_"+str(i),vts_mtx[i])
print("\n")


# génération matrice de la triangulisation du mesh :
trgl = []
print("CALCULE DE LA TRIANGULISATION DU MESH : bpy.data.meshes.calc_looptriangles()")
me.calc_loop_triangles()

for triangle in me.loop_triangles:
    trgl.append(list(triangle.vertices))
trgl_mtx = np.matrix(trgl)

print("Matrice de la triangulisation du mesh : bpy.data.meshes.loop_triangles.loop_triangle.vertices[0]..[1]..[2]")
for i in range(len(trgl_mtx)):
    if i > 2 and i < len(trgl_mtx)-1:
        pass
    elif i == len(trgl_mtx)-1:
        print("...")
        print("Triangle_"+str(i),"vertices",trgl_mtx[i])
    else :
        print("Triangle_"+str(i),"vertices",trgl_mtx[i])
print("\n")

print("Affichage faces par faces des vertices de chaques faces")
for f in me.polygons:
    print('Face', f.index, 'vertices', list(f.vertices))

print("Les coordonnees des textures : bpy.data.meshes.uv_layers[i].data[i].uv.xy")

obj = bpy.context.scene.objects['Cube']
mm = obj.to_mesh()

coord_list= []
for uv_layer in mm.uv_layers:
    for coord in uv_layer.data:
        coord_list.append([coord.uv.xy[0],coord.uv.xy[1]])

for i in range(len(coord_list)):
    if i%4==0 :
        print("\n")
        print("Face",i//4)
    print('Vert_'+str(i)+" :", "x= "+str(coord_list[i][0]),"y= "+str(coord_list[i][1]))
