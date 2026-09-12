import json, sys
sys.path.insert(0,'output/artifacts')
from faceutil import faces
rep=json.load(open('output/artifacts/census.json'))
rotA,rotB=rep['rotA'],rep['rotB']
fl=faces(rotA,rotB)
# vertex cycles: sequence of head-vertices
vfaces=[]
for f in fl:
    vfaces.append([(u[0]+str(u[1]), v[0]+str(v[1])) for (u,v) in f])
# also check each face alternates A-B-A-B and corresponds to 4-cycle in K(4,8): distinct endpoints pattern
for i,f in enumerate(fl):
    assert len(f)==4
    verts=[u for (u,v) in f]
    assert sum(1 for x in verts if x[0]=='A')==2 and sum(1 for x in verts if x[0]=='B')==2
print("faces (dart tails -> heads):")
for i,f in enumerate(fl):
    print(i, [(u,v) for (u,v) in f])
json.dump({'rotA':rotA,'rotB':rotB,
 'dart_faces':[[[u[0],u[1],v[0],v[1]] for (u,v) in f] for f in fl]},
 open('output/artifacts/representative.json','w'),indent=1)
print("wrote representative.json")
