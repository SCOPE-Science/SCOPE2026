from fractions import Fraction
import random

def theoretical(a,b):
    a,b=Fraction(a),Fraction(b)
    pi0=b/(a+b);pi1=a/(a+b)
    entries=[((1-a)*b,pi0*a+pi1*(1-b)),((1-a)*(1-b),pi0*a+pi1*b),(a*b,pi0*(1-a)+pi1*(1-b)),(a*(1-b),pi0*(1-a)+pi1*b)]
    mean=sum(w*v for w,v in entries)
    var=sum(w*(v-mean)**2 for w,v in entries)
    assert sum(w for w,_ in entries)==1
    assert mean==2*a*b*(2-a-b)/(a+b)
    assert var==b*b*a*(1-a)*(1-2*a)**2/(a+b)**2+a*a*b*(1-b)*(1-2*b)**2/(a+b)**2
    return entries
for i in range(1,10):
 for j in range(1,10): theoretical(Fraction(i,10),Fraction(j,10))

# Calculate the nearest-neighbor reference next-letter FNN count
# for an irreducible two-state Markov trajectory using exact binary data.
def simulate(a,b,n,seed):
 rng=random.Random(seed)
 xs=[0 if rng.random()<b/(a+b) else 1]
 for _ in range(n): xs.append(1 if rng.random()< (a if xs[-1]==0 else 1-b) else 0)
 first={}; firstnext={}
 for k in range(n):
  if xs[k] not in first:
   first[xs[k]]=k
   firstnext[xs[k]]=xs[k+1]
  if len(first)==2:break
 assert len(first)==2
 fails=0
 for k in range(n):
  cand=first[xs[k]]
  if cand==k:
   cand=next((j for j in range(n) if j!=k and xs[j]==xs[k]),None)
   if cand is None:continue
  fails+=xs[k+1]!=xs[cand+1]
 pi0=b/(a+b);pi1=a/(a+b)
 p=[[1-a,a],[b,1-b]]
 value=pi0*(1-p[0][firstnext[0]])+pi1*(1-p[1][firstnext[1]])
 return fails/n,value,firstnext
for a,b in [(0.15,0.65),(0.7,0.2),(0.5,0.5),(0.5,0.6)]:
 for seed in [3,15,48,99]:
  empirical,limit,first=simulate(a,b,100000,seed)
  assert abs(empirical-limit)<0.012,(a,b,seed,empirical,limit,first)
print('PASS: 81 rational moment identities and 16 Markov long-orbit comparisons')
