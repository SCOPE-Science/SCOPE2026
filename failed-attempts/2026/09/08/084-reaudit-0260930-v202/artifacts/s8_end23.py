import json,sys
sys.path.insert(0,str(__import__('pathlib').Path(__file__).resolve().parent / '.'))
from s2_bricks import enddim
D=json.load(open(str(__import__('pathlib').Path(__file__).resolve().parent / 's7_enum23.json')))
def bits6(x): return [[(x>>(2*i+j))&1 for j in range(2)] for i in range(3)]
dist={}; indec=0; rows=[]
for x,s,k0,k1,k2 in D['reps']:
    Mk=[bits6(k0),bits6(k1),bits6(k2)]
    d=enddim(2,3,Mk)
    dist[d]=dist.get(d,0)+1
    rows.append([x,s,d])
print('enddim dist:',dist)
json.dump({'dist':dist,'rows':rows},open(str(__import__('pathlib').Path(__file__).resolve().parent / 's8_end23.json'),'w'))
