from grouped_general import model
from itertools import combinations
edges=list(combinations(range(4),2));cc=model(4,edges,(2,2,2)); idx={c:i for i,c in enumerate(cc[1])}
rows=[{} for i in cc[1]];cols=[{} for i in cc[2]]
for j,c in enumerate(cc[2]):
 for col,(vs,es) in enumerate(c):
  for z,ei in enumerate(es):
   for k,v in enumerate(edges[ei]):
    a=list(c);a[col]=(tuple(sorted(vs+(v,))),tuple(q for q in es if q!=ei));i=idx[tuple(a)];sgn=(-1)**(sum(len(t[1]) for t in c[:col])+z+k)
    rows[i][j]=rows[i].get(j,0)+sgn;cols[j][i]=cols[j].get(i,0)+sgn
assert all(0 not in x.values() for x in rows)
print('built',len(rows),len(cols),sum(len(x) for x in rows),flush=True)
# perform unimodular pivots at unit entries preferential least fill-in
ct=0
while True:
 choice=None; cost=10**30
 for i,row in enumerate(rows):
  if not row: continue
  for j,a in row.items():
   if abs(a)!=1:continue
   v=(len(row)-1)*(len(cols[j])-1)
   if v<cost: cost=v;choice=(i,j)
 if choice is None: break
 i,j=choice;sgn=rows[i][j]
 # clear column j by row ops: for row r, add -a/sgn times row i
 pivot=list(rows[i].items())
 for r,a in list(cols[j].items()):
  if r==i:continue
  factor=-a*sgn
  for k,b in pivot:
   nv=rows[r].get(k,0)+factor*b
   if nv: rows[r][k]=nv;cols[k][r]=nv
   else: rows[r].pop(k,None);cols[k].pop(r,None)
 # clear row i via column operations; since other rows col j now zero, remove both rows/cols directly
 for k in list(rows[i]): cols[k].pop(i,None)
 for r in list(cols[j]): rows[r].pop(j,None)
 rows[i]={};cols[j]={}
 ct+=1
# verify residual all entries even; /2 residual Smith factors must be units
assert all(v % 2 ==0 for row in rows for v in row.values())
rr=[{j:v//2 for j,v in row.items()} for row in rows];cc2=[{i:v//2 for i,v in col.items()} for col in cols]
r2=0
while True:
 pair=next(((i,j) for i,row in enumerate(rr) for j,v in row.items() if abs(v)==1),None)
 if pair is None:break
 i,j=pair; a=rr[i][j]
 for k,v in list(cc2[j].items()):
  if k==i:continue
  factor=-a*v
  for l,w in list(rr[i].items()):
   q=rr[k].get(l,0)+factor*w
   if q:rr[k][l]=q;cc2[l][k]=q
   else:rr[k].pop(l,None);cc2[l].pop(k,None)
 for l in list(rr[i]):cc2[l].pop(i,None)
 for k in list(cc2[j]):rr[k].pop(j,None)
 rr[i]={};cc2[j]={};r2+=1
assert r2==2 and not any(rr) and not any(cc2)
print('RESULT','cell_counts',[len(cc[k]) for k in sorted(cc)],'unit_factors',ct,'twos',r2,'remaining_zero',True,flush=True)
# verify squared boundary independently
# verify d1d2 0
v0={c:i for i,c in enumerate(cc[0])};D1=[]
for c in cc[1]:
 d={};
 for col,(vs,es) in enumerate(c):
  for ei in es:
   for z,x in enumerate(edges[ei]):
    f=list(c);f[col]=(tuple(sorted(vs+(x,))),());j=v0[tuple(f)];d[j]=d.get(j,0)+((-1)**z)
 D1.append(d)
for c in cc[2]:
 d={}
 for col,(vs,es) in enumerate(c):
  for k,ei in enumerate(es):
   for z,x in enumerate(edges[ei]):
    f=list(c);f[col]=(tuple(sorted(vs+(x,))),tuple(y for y in es if y!=ei));j=idx[tuple(f)];a=(-1)**(sum(len(t[1]) for t in c[:col])+k+z)
    for v,b in D1[j].items():d[v]=d.get(v,0)+a*b
 assert all(v==0 for v in d.values())
print('D2_ZERO_OK',flush=True)
# Connectedness of the cellular one-skeleton: the rank of its incidence map is 113.
parent=list(range(len(cc[0])))
def root(i):
 while parent[i]!=i:
  parent[i]=parent[parent[i]];i=parent[i]
 return i
for pair in D1:
 a,b=pair.keys()
 aa,bb=root(a),root(b)
 if aa!=bb:parent[aa]=bb
assert len({root(i) for i in range(len(parent))})==1
assert len(cc[1])- (len(cc[0])-1)-(ct+r2)==12
assert len(cc[2])-(ct+r2)==71
print('CONNECTED_0_SKELETON_OK')
print('HOMOLOGY H0=Z H1=Z^12+(Z/2)^2 H2=Z^71')
