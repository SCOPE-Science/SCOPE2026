from collections import deque
from itertools import permutations
from orbit_census import gen_invol,maps_idemp_for_t,canonical,polys
from math import factorial

def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):
 b=[0]*len(a)
 for i,j in enumerate(a):b[j]=i
 return tuple(b)
def conj(f,g):return compose(compose(inverse(g),f),g)
def parity(a):return (sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a))))%2
def mul(x,y):
 if x[0]=='u' and y[0]=='u':return ('u',compose(x[1],y[1]))
 if x[0]=='u' and y[0]=='s':return y
 if x[0]=='s' and y[0]=='u':return ('s',conj(x[1],y[1]),conj(x[2],y[1]))
 if x[0]=='s' and y[0]=='s':
  if x[1]==x[2]==tuple(range(len(x[1]))): return x
  return y if parity(x[1])==1 else ('s',tuple(range(len(y[1]))),y[2])
 raise AssertionError

def test(n):
 I=tuple(range(n))
 universe={('u',p) for p in permutations(range(n))}
 singular=[]; orbit_rep={}; essential={}
 for t in gen_invol(n):
  for e,r in maps_idemp_for_t(t):
   z=('s',t,e);universe.add(z);singular.append(z)
   cl=canonical(t,e)
   if t!=I: orbit_rep.setdefault(cl,z)
   elif all(1+a<=2 for a,b in cl):essential.setdefault(cl,z)
 trans=tuple([1,0]+list(range(2,n)))
 cycle=tuple((i+1)%n for i in range(n))
 gens=[('u',trans),('u',cycle)]+list(orbit_rep.values())+list(essential.values())
 # BFS right multiplication generates all positive-length words
 closure=set(gens); queue=deque(gens)
 while queue:
  a=queue.popleft()
  for b in gens:
   c=mul(a,b)
   if c not in closure:
    assert c in universe,(n,'not in universe',a,b,c)
    closure.add(c);queue.append(c)
 assert closure==universe,(n,len(closure),len(universe),len(universe-closure))
 assert len(gens)==2+len(orbit_rep)+len(essential)
 print('n',n,'generators',len(gens),'nontrivial-orbits',len(orbit_rep),'essential-e-orbits',len(essential),'monoid-order',len(universe),'closure',len(closure))
 # For a sample of products, check triple associativity
 arr=gens+list(orbit_rep.values())[:2]
 for x in arr:
  for y in arr:
   for z in arr:
    assert mul(mul(x,y),z)==mul(x,mul(y,z))
 return len(gens)

if __name__=='__main__':
 for n in (5,6):test(n)
 print('UNITAL_GENERATOR_CLOSURE_CHECKS_PASSED')
