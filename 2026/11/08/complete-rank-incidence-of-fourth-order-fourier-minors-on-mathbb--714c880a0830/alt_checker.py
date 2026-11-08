"""Exact cyclotomic determinant census for Fourier minors on F_5^2."""
from itertools import combinations,permutations
from collections import defaultdict,Counter
from math import factorial
p=5
points=[(x,y) for x in range(p) for y in range(p)]
idx={x:i for i,x in enumerate(points)}
S=list(combinations(range(p*p),4))
def determinant2(a,b):return (a[0]*b[1]-a[1]*b[0])%p
def key4(rows):
  v=[points[i] for i in rows]
  keys=[]
  for pi in permutations(range(4),4):
    a,b,c,d=(v[i] for i in pi)
    u=((b[0]-a[0])%p,(b[1]-a[1])%p)
    w=((c[0]-a[0])%p,(c[1]-a[1])%p)
    dd=determinant2(u,w)
    if dd:
      z=((d[0]-a[0])%p,(d[1]-a[1])%p)
      e=(determinant2(z,w)*pow(dd,-1,p))%p
      f=(determinant2(u,z)*pow(dd,-1,p))%p
      keys.append((e,f))
  return min(keys) if keys else ('line',)
classes=defaultdict(list)
for z in S:classes[key4(z)].append(z)
print('number of affine classes:',len(classes))
print('classes:',[(x,len(y),y[0]) for x,y in classes.items()],flush=True)
# each determinant is in Z[zeta_5]: 5-coefficient vector whose sum translates zero iff vector constant
perm=[]
for perm0 in permutations(range(4)):
 sign=(-1)**sum(perm0[i]>perm0[j] for i in range(4) for j in range(i+1,4))
 perm.append((perm0,sign))
def zerodet(rows,cols):
 # compute dot product table mod 5
 v=[points[i] for i in rows]; w=[points[j] for j in cols]
 ex=[[sum(a*b for a,b in zip(v[i],w[j]))%5 for j in range(4)] for i in range(4)]
 count=[0]*5
 for pi,sgn in perm:
  val=(ex[0][pi[0]]+ex[1][pi[1]]+ex[2][pi[2]]+ex[3][pi[3]])%5
  count[val]+=sgn
 return count[0]==count[1]==count[2]==count[3]==count[4]
class_counts={}
for key,sets in classes.items():
 rep=sets[0]; tally=Counter()
 for col in S:
  tally[key4(col) if zerodet(rep,col) else 'NONZERO']+=1
 class_counts[key]=tally
 print('ROW',str(key),'population',len(sets),'zero',sum(n for c,n in tally.items() if c!='NONZERO'),'nonzero',tally['NONZERO'],'by orbits',{str(k):n for k,n in tally.items() if k!='NONZERO'},flush=True)
print('OVERALL',sum(len(cls)*sum(v for k,v in class_counts[key].items() if k!='NONZERO') for key,cls in classes.items()),'TOTAL',len(S)**2,flush=True)
assert len(classes)==5
assert sum(len(cls)*sum(v for k,v in class_counts[key].items() if k!='NONZERO') for key,cls in classes.items()) == 26478750
assert len(S)**2 == 160022500
print('F5_INDEPENDENT_ORBIT_SINGULARITY_CHECK_PASS')
