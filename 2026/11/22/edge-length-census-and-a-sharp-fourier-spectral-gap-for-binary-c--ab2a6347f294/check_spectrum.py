from itertools import product
from math import comb,prod

def edges_by_length(d,n):
 q=2**d
 a={2:(q-1)*comb(n,2)}
 for s in range(3,min(n,d+1)+1):
  a[s]=comb(n,s)*prod(q-2**j for j in range(s-1))
 return a

def is_minimal(seq):
 v=[x for x in seq if x]
 if not v:return False
 for mask in range(1,(1<<len(v))-1):
  z=0
  for j,x in enumerate(v):
   if mask>>j&1:z^=x
  if z==0:return False
 return True

def check_exact_edge(d,n):
 q=2**d; counts={}
 for pre in product(range(q), repeat=n-1):
  end=0
  for x in pre:end^=x
  delta=pre+(end,)
  if is_minimal(delta):counts[len([x for x in delta if x])]=counts.get(sum(x!=0 for x in delta),0)+1
 assert counts==edges_by_length(d,n),(d,n,counts,edges_by_length(d,n))
 return sum(counts.values())

def eig(n,m):
 e2=sum(comb(x,2) for x in m)
 e3=sum(comb(x,3) for x in m)
 return 16*e3+4*(3-n)*e2-comb(n,2)+2*comb(n,3)

def histograms(n):
 for a in range(n+1):
  for b in range(n-a+1):
   for c in range(n-a-b+1):yield (a,b,c,n-a-b-c)

def spectral_gap_certificate(n):
 degree=3*comb(n,2)+6*comb(n,3)
 best=-10**20; mx=[]
 for m in histograms(n):
  if max(m)==n:continue
  val=eig(n,m)
  if val>best:best=val;mx=[m]
  elif val==best:mx.append(m)
 assert degree-best==4*(n-1)**2,(n,degree,best,mx)
 if n>=4:assert all(sorted(m)==[0,0,1,n-1] for m in mx)
 return len(mx)

for d,n in [(1,2),(1,3),(1,7),(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3),(4,4)]:
 degree=check_exact_edge(d,n)
 q=2**d
 if n<=3:assert degree==q**(n-1)-1
 else:assert degree<q**(n-1)-1
for n in range(2,16):
 spectral_gap_certificate(n)
# direct character transform over every character of code for n=3,4
for n in (3,4):
 delta=[]
 for pre in product(range(4),repeat=n-1):
  end=0
  for x in pre:end^=x
  vv=pre+(end,)
  if is_minimal(vv):delta.append(vv)
 for pre in product(range(4),repeat=n-1):
  a=pre+(0,)
  val=0
  for vv in delta:
   dot=0
   for x,y in zip(a,vv):dot^=((x&1)&(y&1))^(((x>>1)&1)&((y>>1)&1))
   val+=1 if dot==0 else -1
  mm=[a.count(i) for i in range(4)]
  assert val==eig(n,mm),(n,a,val,eig(n,mm))
print('FULL_CTP_EDGE_AND_FOURIER_EXACT_PASS')
