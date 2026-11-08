from oct3 import *
from itertools import permutations
from collections import defaultdict
import time, json
from pathlib import Path
E=octgraph(); B=make_basis(3); cols=differential(B)
R=[{z:i for i,z in enumerate(b)} for b in B]
base_eds={frozenset(e):i for i,e in enumerate(E)}

def perms():
 for p in permutations(range(3)):
  for flip in product(range(2),repeat=3):
   g=tuple(2*p[v//2]+((v%2)^flip[v//2]) for v in range(6))
   yield g
G=sorted(perms()); assert len(set(G))==48

def gp_data(g):
 edgep=tuple(base_eds[frozenset((g[u],g[v]))] for u,v in E)
 assert sorted(edgep)==list(range(ne))
 return edgep

def apply(g,deg,index):
 """Return full integer expression of an automorphism on a weight-3 chain basis element."""
 vs,ch,mon=B[deg][index]; ep=gp_data(g)
 moved=[g[v] for v in vs]
 inv=sum(moved[i]>moved[j] for i in range(len(vs)) for j in range(i+1,len(vs)))
 sign=(-1)**inv
 pairs=sorted(zip(moved, [ep[e] for e in ch], [ep[refs[v]] for v in vs]))
 # local difference (h_e - h_f) = (h_e-h_ref) - (h_f-h_ref)
 opts=[]
 for v,e,f in pairs:
  t=[]
  if e!=refs[v]: t.append((e,1))
  if f!=refs[v]: t.append((f,-1))
  opts.append(t)
 newvs=tuple(sorted(moved)); newmon=tuple(sorted(ep[e] for e in mon)); result=defaultdict(int)
 for x in product(*opts):
  nch=tuple(a for a,coef in x); c=sign
  for a,coef in x: c*=coef
  result[R[deg][(newvs,nch,newmon)]]+=c
 return {i:v for i,v in result.items() if v}

def chaintrace(g,deg):
 return sum(apply(g,deg,i).get(i,0) for i in range(len(B[deg])))

def integer_image_basis(columns):
 piv={}; dependent=0; maxabs=0; maxlen=0
 for col in columns:
  x=col.copy()
  while x:
   row=max(x)
   if row not in piv:
    if abs(x[row])!=1:raise ArithmeticError(('nonunit pivot',row,x[row]))
    a=x[row];piv[row]={r:v*a for r,v in x.items()}
    maxlen=max(maxlen,len(x));break
   fac=x[row]
   for r,c in piv[row].items():
    new=x.get(r,0)-fac*c
    if new:x[r]=new;maxabs=max(maxabs,abs(new))
    else:x.pop(r,None)
  if not x:dependent+=1
 return piv,dependent,maxlen,maxabs

def image_trace(g,piv,deg):
 s=0
 for target,p in piv.items():
  x=defaultdict(int)
  for j,c in p.items():
   for r,cc in apply(g,deg,j).items():x[r]+=c*cc
  x={r:v for r,v in x.items() if v}
  # reduce in descending highest row, using rational/integer pivot basis
  while x:
   r=max(x)
   if r not in piv:raise ArithmeticError(('image not invariant',r))
   coef=x[r]
   if r==target:s+=coef
   for rr,cc in piv[r].items():
    new=x.get(rr,0)-coef*cc
    if new:x[rr]=new
    else:x.pop(rr,None)
 return s

def conj_table(G):
 inv={g:i for i,g in enumerate(G)}
 def mult(a,b):return tuple(a[b[j]] for j in range(6))
 identity=tuple(range(6));ini={g:tuple(g.index(i) for i in range(6)) for g in G}
 rem=set(G);classes=[]
 while rem:
  rep=min(rem)
  orb={mult(mult(h,rep),ini[h]) for h in G}
  assert orb<=rem
  classes.append((rep,sorted(orb)))
  rem.difference_update(orb)
 return classes

def main():
 t=time.monotonic();pivs=[]
 for d in range(1,4):
  piv,depend,mx,mv=integer_image_basis(cols[d]);pivs.append(piv)
  print('INTEGRAL',d,len(piv),depend,mx,mv,flush=True)
 for d in (2,3):
  assert len(pivs[d-1])+len(pivs[d-2])<=len(B[d-1])
 print('CHAIN LENGTHS',*[len(x) for x in B],flush=True)
 classes=conj_table(G);print('CLASS COUNT',len(classes), 'sizes',[len(x) for _,x in classes],flush=True)
 outputs=[]
 for rep,orb in classes:
  c=[chaintrace(rep,d) for d in range(4)]
  im2=image_trace(rep,pivs[1],1)
  h1=c[1]-c[0]+1-im2
  h2=c[2]-im2-c[3]
  assert c[0]-c[1]+c[2]-c[3]==1-h1+h2
  outputs.append(dict(rep=list(rep),class_size=len(orb),chain_traces=c,im_d2=im2,H1=h1,H2=h2))
  print('CLASS',outputs[-1],flush=True)
 assert outputs[0]['rep']==list(range(6))
 assert outputs[0]['H1']==8 and outputs[0]['H2']==47
 assert sum(o['class_size']*o['H1'] for o in outputs)%48==0
 assert sum(o['class_size']*o['H2'] for o in outputs)%48==0
 print('INVARIANTS',sum(o['class_size']*o['H1'] for o in outputs)//48,sum(o['class_size']*o['H2'] for o in outputs)//48,flush=True)
 with open(Path(__file__).resolve().parent / 'oct3_chars.json','w') as f: json.dump(outputs,f,indent=2)
 print('CHECKING_ALL_CHAIN_EQUIVARIANCE',flush=True)
 for g in G:
  for d in range(1,4):
   for i, col in enumerate(cols[d]):
    left=defaultdict(int);right=defaultdict(int)
    for r,c in col.items():
     for j,a in apply(g,d-1,r).items(): left[j]+=c*a
    for j,a in apply(g,d,i).items():
     for r,c in cols[d][j].items(): right[r]+=a*c
    assert {j:v for j,v in left.items() if v}=={j:v for j,v in right.items() if v}
 print('ALL_48_CHAIN_EQUIVARIANCE_PASS',flush=True)
 for data,(rep,orb) in zip(outputs,classes):
  for g in orb:
   a=[chaintrace(g,d) for d in range(4)]
   im2=image_trace(g,pivs[1],1)
   assert a[1]-a[0]+1-im2==data['H1']
   assert a[2]-im2-a[3]==data['H2']
 print('ALL_48_CLASS_CHARACTERS_PASS',flush=True)
 print('OCT3_SYMMETRY_CHARACTER_PASS',flush=True)
if __name__=='__main__':main()
