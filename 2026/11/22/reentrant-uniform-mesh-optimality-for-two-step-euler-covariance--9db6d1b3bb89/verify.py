from fractions import Fraction as Q
import math,random
random.seed(17)
N=0
for i in range(5000):
 d=Q(random.randrange(1,200),100);T=Q(random.randrange(1,501),100)
 h=Q(random.randrange(0,1001),1000)*T
 f=lambda x:1-d*x+x*x
 z=h*(T-h);B=d*d-d*T-2
 exact=f(h)*f(T-h)
 asserted=f(T)+z*(z+B)
 assert exact==asserted
 zstar=max(Q(0),min(T*T/4, (2-d*d+d*T)/2))
 vstar=f(T)+zstar*(zstar+B)
 assert exact>=vstar
 N+=2
for d in [0.3,1.0,math.sqrt(2),1.6,1.75,1.9]:
 T0=max(0,d-2/d)
 Tminus=d-math.sqrt(4-d*d)
 Tplus=d+math.sqrt(4-d*d)
 for T in [0.05,0.5*T0 if T0>0 else 0.05, 0.5*(T0+Tminus) if Tminus>T0 else 0.1, max(0.001,(Tminus+Tplus)/2),Tplus+1]:
  if T<=0:continue
  zstar=max(0,min(T*T/4,(2-d*d+d*T)/2))
  f=lambda t:1-d*t+t*t
  u=[(j/10000)*T*(1-j/10000)*T for j in range(10001)]
  vi=min(f(j*T/10000)*f(T-j*T/10000) for j in range(10001))
  theoretical=f(T)+zstar*(zstar+d*d-d*T-2)
  assert vi>=theoretical-1e-10
  assert vi<=theoretical+1e-6
  N+=2
print('VERIFY_OK',N)
