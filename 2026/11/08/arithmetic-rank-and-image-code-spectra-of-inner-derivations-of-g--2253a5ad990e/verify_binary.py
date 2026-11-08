from collections import Counter
from itertools import product
from math import gcd

def add(a,b,orders,s=1):return tuple((x+s*y)%o for x,y,o in zip(a,b,orders))
def algebra(orders):
 base=list(product(*[range(o) for o in orders])); group=[(a,e) for e in (0,1) for a in base]; idx={g:i for i,g in enumerate(group)}
 n=len(group); mult=[[None]*n for _ in range(n)]
 for i,(g,e) in enumerate(group):
  for j,(h,f) in enumerate(group):mult[i][j]=idx[(add(g,h,orders,-1 if e else 1),e^f)]
 return mult

def rank_binary(cols):
 p={}
 for a in cols:
  while a:
   j=a.bit_length()-1
   if j in p:a^=p[j]
   else:p[j]=a;break
 return len(p)

def exp_order(vec,orders):
 from math import lcm
 return lcm(*(o//gcd(a,o) for a,o in zip(vec,orders)))

def pred_poly(orders,q):
 from math import lcm
 E=lcm(*orders)
 cnt=Counter(exp_order(g,orders) for g in product(*[range(o) for o in orders]))
 poly={0:1};fac=[]
 for m,a in sorted(cnt.items()):
  if m==1:continue
  assert gcd(m,q)==1
  d=1
  while pow(q,d,m) not in (1,m-1):d+=1
  assert a%(2*d)==0, (m,a,d)
  e=a//(2*d);fac.append((m,d,e))
  for k in range(e):
   nex=poly.copy()
   for rank,v in poly.items():nex[rank+2*d]=nex.get(rank+2*d,0)+v*(q**(3*d)-1)
   poly=nex
 return poly,fac

def census_binary(orders, include_images=False):
 mult=algebra(orders);n=len(mult);assert n<=18
 c=[[0]*n for _ in range(n)]
 for i in range(n):
  for j in range(n):c[i][j]=(1<<mult[i][j])^(1<<mult[j][i])
 # iterate x as Gray code updating n commutator columns
 cols=[0]*n; counter=Counter();last=0;seen=set();image_hist=Counter()
 for z in range(1<<n):
  x=z^(z>>1)
  if z:
   delta=(last^x).bit_length()-1
   for j in range(n):cols[j]^=c[delta][j]
  rr=rank_binary(cols)
  counter[rr]+=1
  if include_images:
   piv={}
   for a in cols:
    while a:
     j=a.bit_length()-1
     if j in piv:a^=piv[j]
     else:piv[j]=a;break
   for j in sorted(piv):
    for i in sorted(piv):
     if i!=j and ((piv[i]>>j)&1):piv[i]^=piv[j]
   key=tuple(piv[j] for j in sorted(piv))
   if key not in seen:seen.add(key);image_hist[len(key)]+=1
  last=x
 return (counter,image_hist) if include_images else counter

if __name__=='__main__':
 for orders in [(3,),(5,),(7,),(3,3)]:
  q=2
  poly,fac=pred_poly(orders,q)
  N=2
  for o in orders:N*=o
  centerdim=N-3*sum(f[1]*f[2] for f in fac)
  direct,images=census_binary(orders,True)
  predicted={r:v*q**centerdim for r,v in poly.items()}
  print(orders,'factors',fac,'pred',poly,'direct',direct,'center dimension',centerdim,flush=True)
  assert predicted==direct,(predicted,direct)
  image_expected={0:1}
  for _,d,k in fac:
   for _ in range(k):
    new=image_expected.copy()
    for r,a in image_expected.items():new[r+2*d]=new.get(r+2*d,0)+a*(q**(2*d)+q**d+1)
    image_expected=new
  assert image_expected==images,(image_expected,images)
  print("images",dict(images),flush=True)
 print('VERIFY_OK')
