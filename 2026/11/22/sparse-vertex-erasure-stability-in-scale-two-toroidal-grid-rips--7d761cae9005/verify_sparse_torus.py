"""Standalone exact simplicial certificate for sparse vertex deletion in toroidal Rips complexes."""
from itertools import combinations
from pathlib import Path
import json

OFFSETS={
 'N':(0,1), 'S':(0,-1), 'E':(1,0), 'W':(-1,0),
 'N2':(0,2), 'S2':(0,-2), 'E2':(2,0), 'W2':(-2,0),
 'NE':(1,1), 'NW':(-1,1), 'SE':(1,-1), 'SW':(-1,-1)}
EXPECTED_FACETS=[
 ('N','S','E','W'), ('N','N2','NE','NW'),('S','S2','SE','SW'),
 ('E','E2','NE','SE'), ('W','W2','NW','SW'),
 ('N','E','NE'), ('N','W','NW'),('S','E','SE'),('S','W','SW')]

def ftuple(xs): return tuple(sorted(xs))
def subsets(v):
 for k in range(len(v)+1):
  for x in combinations(v,k): yield ftuple(x)
def complete(facets): return {f for fac in facets for f in subsets(fac)}
def torusdist(a,b,m,n):
 x=abs(a[0]-b[0]);y=abs(a[1]-b[1]);return min(x,m-x)+min(y,n-y)
def facets(m,n):
 out=[]
 for x in range(m):
  for y in range(n):
   p=lambda a,b:((x+a)%m,(y+b)%n)
   out.append(ftuple([p(0,0),p(1,0),p(-1,0),p(0,1),p(0,-1)]))
   out.append(ftuple([p(0,0),p(1,0),p(1,1),p(0,1)]))
 return out

def link_at_origin(m,n):
 origin=(0,0)
 offset_to_label={((a%m),(b%n)):name for name,(a,b) in OFFSETS.items()}
 candidates=list(offset_to_label)
 cliques=set()
 for ss in subsets(candidates):
  if all(torusdist(a,b,m,n)<=2 for a,b in combinations(ss,2)):
   cliques.add(ftuple(offset_to_label[p] for p in ss))
 return cliques

def validate_pair(cells, small, large):
 small=ftuple(small); large=ftuple(large)
 assert len(large)==len(small)+1 and set(small)<set(large), (small,large)
 assert small in cells and large in cells,(small,large)
 assert all(not(set(large)<set(x)) for x in cells), (small,large,'large not facet')
 assert sum(set(small).issubset(x) and len(x)==len(large) for x in cells)==1,(small,large,'not free')
 cells.remove(small);cells.remove(large)

def link_certificate():
 cells=complete(EXPECTED_FACETS)
 pairs=[]
 while len(cells)>2:
  found=None
  for big in sorted(cells,key=lambda v:(-len(v),v)):
   if len(big)<2 or any(set(big)<set(other) for other in cells): continue
   for small in combinations(big,len(big)-1):
    if sum(set(small).issubset(other) and len(other)==len(big) for other in cells)==1:
     found=(ftuple(small),big);break
   if found:break
  assert found is not None, ('link fails to collapse',len(cells))
  validate_pair(cells,*found);pairs.append(found)
 assert len(pairs)==35 and len(cells)==2 and () in cells,cells
 assert len(pairs)==35
 return {'pairs':[[list(a),list(b)] for a,b in pairs], 'survivor':next(x[0] for x in cells if len(x)==1)}

def verify():
 cert_path=Path(__file__).resolve().parent/'link_certificate.json'
 cert=json.loads(cert_path.read_text(encoding='utf-8'))
 local=link_at_origin(9,9)
 assert local==complete(EXPECTED_FACETS)
 assert [sum(len(f)==k for f in local) for k in range(5)]==[1,12,30,24,5]
 witness=set(local)
 for a,b in cert['pairs']:validate_pair(witness,a,b)
 assert witness=={(),(cert['survivor'],)}
 assert len(cert['pairs'])==35
 verified=[]
 for m,n,S in [
  (7,7,[(0,0)]),(7,8,[(0,0),(3,0),(0,3)]),
  (8,8,[(0,0),(0,3),(3,0),(3,3)]),
  (10,10,[(i,j) for i in range(10) for j in range(10) if (i+2*j)%5==0])]:
  for a,b in combinations(S,2):assert torusdist(a,b,m,n)>=3,(m,n,a,b)
  fs=complete(facets(m,n))
  N=m*n
  assert [sum(len(f)==k for f in fs) for k in range(6)]==[1,N,6*N,10*N,6*N,N],(m,n)
  before=len(fs)
  for x,y in S:
   translate=lambda a:((x+OFFSETS[a][0])%m,(y+OFFSETS[a][1])%n)
   v=(x,y)
   for a,b in cert['pairs']:
    validate_pair(fs,[v]+[translate(z) for z in a],[v]+[translate(z) for z in b])
   validate_pair(fs,[v],[v,translate(cert['survivor'])])
  intended=complete([f for f in facets(m,n) if not any(set(f)&set(S))])
  # The induced complex also contains faces of original facets that meet S.
  original=complete(facets(m,n))
  intended={f for f in original if not set(f).intersection(S)}
  assert fs==intended,(m,n,len(fs),len(intended))
  assert before-len(fs)==72*len(S)
  verified.append((m,n,len(S),len(fs),36*len(S)))
 # Verify local obstruction for two adjacent deletions (Euler characteristic changes).
 L=link_at_origin(9,9)
 LX={f for f in L if 'N' not in f}
 chi=sum((-1)**(len(f)-1) for f in LX if f)
 assert chi==0,chi
 print('LOCAL_LINK_FACE_COUNTS 1,12,30,24,5; LINK_COLLAPSE 35 PAIRS')
 for m,n,k,remaining,steps in verified:
  print(f'GRID {m}x{n} REMOVED {k} VERTICES COLLAPSES {steps} REMAINING_FACES {remaining}')
 print('ADJACENT_PAIR_LINK_EULER 0; INDUCED_EULER -1')
 print('VERIFY_OK')

if __name__=='__main__':verify()
