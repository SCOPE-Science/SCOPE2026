from collections import Counter, defaultdict
from itertools import permutations,product
from math import factorial,comb

def polys(maxn):
 # count unordered multisets of (a,b) weighted size 1+a+2*b, with #roots r and transpositions s
 dp={(0,0,0):1}
 for a in range(maxn):
  for b in range((maxn-1-a)//2+1):
   d=1+a+2*b
   # geometric product: can add any number copies of type (a,b)
   arr=dict(dp)
   for (n,r,s),v in sorted(arr.items()):
    c=1
    while n+c*d<=maxn:
     key=(n+c*d,r+c,s+c*b)
     dp[key]=dp.get(key,0)+v
     c+=1
 return dp

def gen_invol(n):
 for p in permutations(range(n)):
  if all(p[p[i]]==i for i in range(n)):
   yield p

def maps_idemp_for_t(t):
 n=len(t);fixed=[i for i in range(n) if t[i]==i];orbits=[];seen=set()
 for i in range(n):
  if i in seen:continue
  if t[i]==i: orbits.append((i,)); seen.add(i)
  else: orbits.append((i,t[i]));seen|={i,t[i]}
 for flag in product((0,1),repeat=len(fixed)):
  roots=tuple(x for x,f in zip(fixed,flag) if f)
  if not roots:continue
  # select e-values for every nonroot orbit, rooted orbits fixed
  non=[orb for orb in orbits if orb[0] not in roots]
  for tgt in product(roots,repeat=len(non)):
   e=list(range(n))
   for orb,q in zip(non,tgt):
    for x in orb:e[x]=q
   yield tuple(e),len(roots)

def canonical(t,e):
 n=len(t); comps=[]
 for r in range(n):
  if e[r]!=r:continue
  a=sum(1 for x in range(n) if t[x]==x and x!=r and e[x]==r)
  b=sum(1 for x in range(n) if t[x]!=x and e[x]==r)//2
  comps.append((a,b))
 return tuple(sorted(comps))

def summary(n):
 c=Counter(); cls=defaultdict(set)
 for t in gen_invol(n):
  s=sum(t[i]!=i for i in range(n))//2
  for e,r in maps_idemp_for_t(t):
   c[(r,s)]+=1
   cls[(r,s)].add(canonical(t,e))
 return c,{k:len(v) for k,v in cls.items()}

if __name__=='__main__':
 dp=polys(7)
 for n in range(1,7):
  c,cl=summary(n)
  for (r,s),v in c.items():
   j=n-2*s
   expected=factorial(n)//(2**s*factorial(s)*factorial(j))*comb(j,r)*r**(n-s-r)
   assert v==expected,(n,r,s,v,expected)
   assert cl[(r,s)]==dp.get((n,r,s),0),(n,r,s,cl[(r,s)],dp.get((n,r,s),0))
  print('n',n,'maps',sum(c.values()),'orbits',sum(cl.values()),'classes-by-rs',sorted(cl.items()))
 print('UNITAL_ENDOMORPHISM_ORBIT_CHECKS_PASSED')
