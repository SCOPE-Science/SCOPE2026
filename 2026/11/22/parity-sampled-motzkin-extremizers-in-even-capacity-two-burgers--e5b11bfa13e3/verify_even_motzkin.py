"""Independent near-critical even-ring last-entry census and Motzkin operator identity.

No external dependencies. The proof for unbounded lengths is in RESULT.md.
"""
from itertools import product
from collections import Counter
from math import comb

def F(v):
 n=len(v)
 return tuple(v[j]+min(v[(j-1)%n],2-v[j])-min(v[j],2-v[(j+1)%n]) for j in range(n))
def recurrent(v):
 n=len(v)
 vals=[v[j]+v[(j+1)%n] for j in range(n)]
 return max(vals)<=2 or min(vals)>=2

def M(k):
 return sum(comb(k,2*j)*comb(2*j,j)//(j+1) for j in range(k//2+1))

def special_peaks(v):
 n=len(v); m=n//2
 assert n%2==0 and sum(v)==n-1
 # h_i-h_(i-1)=x_i-1, lifted heights h_(i+n)=h_i-1.
 h=[0]
 for i in range(1,n):h.append(h[-1]+v[i]-1)
 return [i for i in range(n) if all(h[i]>=h[(i+2*j)%n]-(i+2*j>=n)+2 for j in range(1,m))]

for n in (4,6,8,10,12):
 seen=Counter(); mass_states=Counter();npeaks=0
 for v in product(range(3),repeat=n):
  k=sum(v)
  if k not in (n-1,n+1):continue
  mass_states[k]+=1
  y=v
  for _ in range(n//2-2):y=F(y)
  at_max=not recurrent(y)
  seen[k]+=at_max
  if k==n-1:
   peaks=special_peaks(v)
   assert at_max == bool(peaks)
   assert len(peaks)<=1
   npeaks+=len(peaks)
 predicted=2*n*M(n-3)
 assert seen[n-1]==seen[n+1]==predicted,(n,seen,predicted)
 print('n=',n,'states by mass',dict(mass_states),'last-entry each mass',predicted,'unique exceptional peaks',npeaks)

# Operator K: two-step {-1,0,+1} walks inspected only at even times,
# including one permitted negative odd intermediate between two zero endpoints.
def Kstep(v):
 out=Counter()
 for h,num in v.items():
  for a,b in product((-1,0,1),repeat=2):
   if h+a+b>=0:out[h+a+b]+=num
 return out
state=Counter({0:1})
for L in range(18):
 rooted=2*state[0]+state[1]
 assert rooted==2*M(2*L+1),(L,rooted,2*M(2*L+1))
 state=Kstep(state)
print('Two-step transfer / Motzkin identity: PASS for L=0,...,17')
print('Near-critical even-ring Motzkin exact extrema checks: PASS')
