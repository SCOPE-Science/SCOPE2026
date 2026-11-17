import math, random
from scipy.integrate import quad

def tail(n,k):
 d=math.pi/n
 if k == 1: return 1.
 if k<1 or k> (n+1)//2: return 0.
 a=2*(k//2)*d; s=1 if k%2 else -1
 lo=max(0.,a-math.pi/2) if s==-1 else 0.
 hi=d if s==-1 else min(d,math.pi/2-a)
 if hi<=lo: return 0.
 return ((hi-lo)+(math.sin(2*a+2*s*hi)-math.sin(2*a+2*s*lo))/(2*s))/math.sin(2*d)

def radial(n,theta):
 d=math.pi/n
 t=abs((theta+d)%(2*d)-d)
 return math.cos(d)/math.cos(d-t)

def direct(n,k):
 d=math.pi/n
 def f(t):
  r=radial(n,t)
  h=sorted((max(0.,math.cos(t-2*math.pi*j/n)) for j in range(n)),reverse=True)[k-1]
  return min(r*r,h*h)
 return quad(f,-d,d,epsabs=1e-11,limit=300,points=[0.0])[0]/math.sin(2*d)
for n in range(3,31):
 a=[tail(n,k) for k in range(1,n+2)]
 assert abs(a[0]-1)<1e-12
 assert all(-1e-12<=x<=1+1e-12 for x in a)
 assert all(a[i]>=a[i+1]-1e-12 for i in range(len(a)-1))
 assert a[(n+1)//2] == 0
 for k in range(1,n+1):
  b=direct(n,k)
  assert abs(a[k-1]-b)<1e-9,(n,k,a[k-1],b)
print('PASS',sum(n for n in range(3,31)),'independent quadrature comparisons; samples', [(n,[round(tail(n,k),8) for k in range(1,(n+1)//2+1)]) for n in [3,4,5,6,7,8,12]])
