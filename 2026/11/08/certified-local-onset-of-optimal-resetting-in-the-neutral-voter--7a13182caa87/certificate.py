"""Exact rational interval certificate for neutral Wright--Fisher reset onset.
All upper/lower bounds are rational; no floating point evaluations used to certify signs.
"""
from fractions import Fraction as Q
from functools import lru_cache

KLOG=26; KDILOG=35; KPI=16

def add(A,B):return (A[0]+B[0],A[1]+B[1])
def sub(A,B):return (A[0]-B[1],A[1]-B[0])
def times(A,B):
 v=[a*b for a in A for b in B]
 return (min(v),max(v))
def divpos(A,q):assert q>0;return (A[0]/q,A[1]/q)
def const(q):return (q,q)
def atanh_log_z(z):
 # logarithm (1+z)/(1-z); all terms same sign, tail explicit
 s=sum((2*z**(2*i+1)/Q(2*i+1) for i in range(KLOG)),Q(0))
 absz=abs(z); tail=2*absz**(2*KLOG+1)/((2*KLOG+1)*(1-absz**2))
 return (s-tail,s) if z<0 else (s,s+tail)
L2=atanh_log_z(Q(1,3))
@lru_cache(maxsize=None)
def ln(t):
 assert 0<t<=1
 if t==1:return const(Q(0))
 n=0
 while t<Q(1,2):t*=2;n+=1
 z=(t-1)/(t+1)
 return sub(atanh_log_z(z),times(const(Q(n)),L2))

def atan_pos(z):
 s=sum(((-1)**i*z**(2*i+1)/Q(2*i+1) for i in range(KPI)),Q(0))
 e=z**(2*KPI+1)/Q(2*KPI+1)
 return (s,s+e) if KPI%2==0 else (s-e,s)
PI=sub(times(const(Q(16)),atan_pos(Q(1,5))),times(const(Q(4)),atan_pos(Q(1,239))))
PI2=times(PI,PI)
ZETA2=divpos(PI2,Q(6))
@lru_cache(maxsize=None)
def li2(t):
 assert 0<=t<=1
 if t==0:return const(Q(0))
 if t==1:return ZETA2
 if t<=Q(1,2):
  ss=sum((t**i/Q(i*i) for i in range(1,KDILOG+1)),Q(0))
  err=t**(KDILOG+1)/((KDILOG+1)**2*(1-t))
  return (ss,ss+err)
 return sub(sub(ZETA2,times(ln(t),ln(1-t))),li2(1-t))
@lru_cache(maxsize=None)
def U1(t):
 if t==0 or t==1:return const(Q(0))
 return sub(const(Q(0)),add(times(const(t),ln(t)),times(const(1-t),ln(1-t))))
@lru_cache(maxsize=None)
def U2(t):
 if t==0 or t==1:return const(Q(0))
 s=add(add(times(const(1-t),li2(1-t)),times(const(t),li2(t))),U1(t))
 return sub(divpos(PI2,Q(3)),times(const(Q(2)),s))

def midpoint(A):return float((A[0]+A[1])/2)
def positive(A):assert A[0]>0,('not positive',float(A[0]),float(A[1]))
def negative(A):assert A[1]<0,('not negative',float(A[0]),float(A[1]))

def c1(t):return sub(times(U1(t),U1(t)),divpos(U2(t),Q(2)))

def u3_lower(t,M=128):
 i1=Q(0);i2=Q(0)
 for j in range(M):
  l=Q(j,M);h=Q(j+1,M)
  if l<t:
   b=min(h,t)
   mn=min(U2(l)[0],U2(b)[0]);assert mn>=0
   i1+=(b-l)*mn/(1-l)
  if h>t:
   a=max(l,t)
   mn=min(U2(a)[0],U2(h)[0]);assert mn>=0
   i2+=(h-a)*mn/h
 return Q(3)*((1-t)*i1+t*i2)

def run():
 a=Q(1019,1250);b=Q(4077,5000)
 ca=c1(a);cb=c1(b)
 positive(ca);negative(cb)
 # c1'(x)=2U1(x)log((1-x)/x)+Li2(x)-Li2(1-x).
 # On [a,b], U1 decreasing, log((1-x)/x) decreasing,
 # and Li2(x)-Li2(1-x) increasing.
 upper=2*U1(b)[0]*ln((1-a)/a)[1]+li2(b)[1]-li2(1-b)[0]
 assert upper<-Q(1,2),float(upper)
 # U3 is positive, symmetric and concave (U3''=-3 U2/(x(1-x))).
 # Hence U3(x)>=U3(b) for 1/2<=x<=b.
 low=u3_lower(b)
 upper6=Q(6)*U1(a)[1]**3
 assert low>upper6,(float(low),float(upper6))
 print('BRACKET A',float(a),'B',float(b))
 print('c1(A) interval',list(map(float,ca)))
 print('c1(B) interval',list(map(float,cb)))
 print('c1prime upper',float(upper))
 print('U3(B) rigorous lower',float(low))
 print('6*U1(A)^3 upper',float(upper6))
 print('c2 at critical lower',float(low/Q(6)-U1(a)[1]**3))
 print('CERTIFIED: unique c1 root on [A,B], transverse negative crossing, c2>0 at root')
if __name__=='__main__':run()
