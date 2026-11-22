"""Finite sanity checks for dihedral quotients of first-critical polygon Rips complexes."""
from collections import defaultdict
from itertools import combinations

def complexes(k):
 n=3*k
 A=set()
 for i in range(n):
  arc=tuple((i+j)%n for j in range(k+1))
  for t in range(1,k+2):
   A.update(tuple(sorted(S)) for S in combinations(arc,t))
 E={tuple(sorted((i,i+k,i+2*k))) for i in range(k)}
 return A,A|E

def dihedral(n):
 return [tuple((sgn*i+a)%n for i in range(n)) for sgn in (1,-1) for a in range(n)]

def orbit_chain(chain,P):
 return min(tuple(tuple(sorted(p[v] for v in s)) for s in chain) for p in P)

def chains(F):
 # Each order complex simplex is an increasing chain of nonempty faces
 by_dim=defaultdict(set)
 for f in F:
  by_dim[0].add((f,))
 for dim in range(1,max(len(f) for f in F)):
  for c in by_dim[dim-1]:
   for f in F:
    if len(f)>len(c[-1]) and set(c[-1]).issubset(f):
     by_dim[dim].add(c+(f,))
 return {d:C for d,C in by_dim.items() if C}

def rank_mod(cols,p):
 pivots={}
 for col in cols:
  v={r:x%p for r,x in col.items() if x%p}
  while v:
   j=max(v)
   if j not in pivots:
    a=pow(v[j],-1,p)
    pivots[j]={r:(a*x)%p for r,x in v.items() if (a*x)%p}
    break
   scale=v[j]
   w=pivots[j]
   for r,x in w.items():
    z=(v.get(r,0)-scale*x)%p
    if z:v[r]=z
    elif r in v:del v[r]
 return len(pivots)

def quotient_homology(F,n,p):
 P=dihedral(n); by_dim=chains(F)
 bases={d:sorted({orbit_chain(c,P) for c in C}) for d,C in by_dim.items()}
 index={d:{c:i for i,c in enumerate(B)} for d,B in bases.items()}
 ranks={0:0}
 for d,B in bases.items():
  if not d:continue
  cols=[]
  for c in B:
   col=defaultdict(int)
   for a in range(len(c)):
    face=c[:a]+c[a+1:]
    key=orbit_chain(face,P)
    col[index[d-1][key]]+= (-1)**a
   cols.append(col)
  ranks[d]=rank_mod(cols,p)
 euler=sum((-1)**d*len(B) for d,B in bases.items())
 bettis=[len(bases.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0) for d in range(max(bases)+1)]
 return {'euler':euler,'cells':{d:len(B) for d,B in bases.items()},'betti':bettis}

if __name__=='__main__':
 for k in (2,3,4,5):
  A,K=complexes(k)
  n=3*k
  assert len(K-A)==k
  for r in range(1,k+2):
   for face in combinations(range(n),r):
    is_clique=all(min((i-j)%n,(j-i)%n)<=k for i,j in combinations(face,2))
    assert is_clique==(face in K), (k,face)
  exceptional=tuple(sorted((0,k,2*k)))
  assert sum(tuple(sorted(p[i] for i in exceptional))==exceptional for p in dihedral(n))==6
  a=quotient_homology(A,3*k,2)
  b=quotient_homology(K,3*k,2)
  c=quotient_homology(K,3*k,3)
  print('k=',k,'A',a,'K mod2',b,'K mod3',c,flush=True)
  assert a['betti']==[1]+[0]*(len(a['betti'])-1)
  assert b['betti']==[1]+[0]*(len(b['betti'])-1)
  assert c['betti']==[1]+[0]*(len(c['betti'])-1)
 print('FIRST_CRITICAL_DIHEDRAL_CHAIN_CHECKS_OK')
