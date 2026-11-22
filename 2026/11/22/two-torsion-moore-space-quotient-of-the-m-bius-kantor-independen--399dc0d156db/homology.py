import sympy as s,time,collections
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
cells={};byd=collections.defaultdict(list)
for line in open('residual_cells.txt'):
 left,right=line.strip().split('|');x=left.split();i=int(x[1]);d=int(x[2]);b=[(int(v.split(':')[0]),int(v.split(':')[1])) for v in right.strip().split()];cells[i]=(d,b);byd[d].append(i)
print('dims',{k:len(v) for k,v in byd.items()},flush=True)
mat={};rank={};tors={}
for d in range(1,5):
 rows=byd[d-1];cols=byd[d];ri={c:j for j,c in enumerate(rows)};a=s.zeros(len(rows),len(cols))
 for j,c in enumerate(cols):
  for b,sg in cells[c][1]:a[ri[b],j]+=sg
 mat[d]=a
 t=time.time();inv=smith_normal_form(a,domain=ZZ);ds=[abs(int(inv[i,i])) for i in range(min(inv.shape)) if inv[i,i]]
 rank[d]=len(ds);tors[d-1]=[i for i in ds if i!=1];print('B',d,'shape',a.shape,'rank',rank[d],'torsion',tors[d-1],'secs',time.time()-t,flush=True)
print('betti',[(d,len(byd[d])-rank.get(d,0)-rank.get(d+1,0)) for d in range(5)])
for d in range(2,5):
 assert mat[d-1]*mat[d]==s.zeros(*((mat[d-1]*mat[d]).shape))
print('BDRY2 OK'); assert [len(byd[d])-rank.get(d,0)-rank.get(d+1,0) for d in range(5)]==[1,0,0,0,0];assert tors[3]==[2] and all(not tors[d] for d in [0,1,2]); print('MK_INTEGRAL_HOMOLOGY_OK')
