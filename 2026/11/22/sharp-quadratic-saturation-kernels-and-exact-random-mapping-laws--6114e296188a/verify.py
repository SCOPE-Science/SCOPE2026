"""Independent exact enumerative checks for bounded unary orbit-type saturation.
Requires Python 3 standard library only. No external files or network.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial

MAX_N=6

def zero(n):return [Q(0) for _ in range(n+1)]
def const(v,n): a=zero(n);a[0]=Q(v);return a
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def scale(a,c):return [x*c for x in a]
def mul(a,b):
 n=len(a)-1;c=zero(n)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:n+1-i]):
    if y:c[i+j]+=x*y
 return c
def powp(a,m):
 r=const(1,len(a)-1)
 for _ in range(m): r=mul(r,a)
 return r
def exp(a):
 n=len(a)-1
 assert a[0]==0
 b=const(1,n)
 for k in range(1,n+1):b[k]=sum(Q(i)*a[i]*b[k-i] for i in range(1,k+1))/k
 return b
def inv(a):
 n=len(a)-1
 assert a[0]==1
 b=const(1,n)
 for k in range(1,n+1):b[k]=-sum(a[i]*b[k-i] for i in range(1,k+1))
 return b

def egf_sat(d,n):
 z=zero(n);z[1]=1
 T=zero(n)
 for k in range(1,n+1):T[k]=Q(k**(k-1),factorial(k))
 height={-1:zero(n)}
 for h in range(d): height[h]=mul(z,exp(height[h-1]))
 ALL=inv(sub(const(1,n),T))
 good=ALL
 for c in range(1,d+1):
  L=d-c
  g=scale(sub(powp(T,c),powp(height[L-1],c)),Q(1,c))
  good=mul(good,sub(const(1,n),exp(scale(g,-1))))
 # Exception: no-repetition profile absent, despite realizing all repeating profiles.
 short=zero(n)
 for c in range(1,d+1):
  L=d-c
  short=add(short,scale(powp(height[L],c),Q(1,c)))
 bad=exp(short)
 for c in range(1,d+1):
  L=d-c
  g=scale(sub(powp(height[L],c),powp(height[L-1],c)),Q(1,c))
  bad=mul(bad,sub(const(1,n),exp(scale(g,-1))))
 count=sub(good,bad)
 return [int(a*factorial(k)) for k,a in enumerate(count)]

def orbit_type(f,x,d):
 seen={x:0};v=x
 for j in range(1,d+1):
  v=f[v]
  if v in seen:return (seen[v],j-seen[v])
  seen[v]=j
 return None

def observed(f,d):return {orbit_type(f,x,d) for x in range(len(f))}
def all_types(d):return {None}|{(i,c) for c in range(1,d+1) for i in range(d-c+1)}

def brute(n,d):
 ans=0
 target=all_types(d)
 for f in product(range(n),repeat=n):
  if observed(f,d)==target:ans+=1
 return ans

def constructed(d,extra):
 # one length-c cycle + one inward chain of depth d-c for each c,
 # with a single extra depth at c=extra.
 f=[]
 for c in range(1,d+1):
  st=len(f)
  f.extend(st+(i+1)%c for i in range(c))
  pred=st
  for _ in range(d-c+(c==extra)):
   t=len(f);f.append(pred);pred=t
 return tuple(f)


def run():
 tests=0
 for d in range(1,4):
  for n in range(1,MAX_N+1):
   exact=egf_sat(d,n)[n]
   empirical=brute(n,d)
   assert exact==empirical,(d,n,exact,empirical)
   tests+=1
 for d in range(1,12):
  assert len(all_types(d))==1+d*(d+1)//2
  for e in range(1,d+1):
   f=constructed(d,e)
   assert len(f)==d*d+1
   assert observed(f,d)==all_types(d)
   tests+=1
 assert egf_sat(1,6)==[0,0,2,18,174,2100,31030]
 assert egf_sat(2,6)==[0,0,0,0,0,180,4500]
 # two inequivalent minimized models d=2, total 5!=120 and 5!/2=60
 assert egf_sat(2,5)[5]==factorial(5)*3//2
 print('VERIFY_OK',tests,'counts_d1',egf_sat(1,6),'counts_d2',egf_sat(2,6))

if __name__=='__main__':run()
