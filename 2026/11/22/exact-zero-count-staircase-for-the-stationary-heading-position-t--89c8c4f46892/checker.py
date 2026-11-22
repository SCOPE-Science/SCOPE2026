import math,cmath,random
import mpmath as mp
import sympy as sp

def params(k,d,w):
 Z=((k-d)**2+w*w)*((k+d)**2+w*w)
 a=2*d*(d*d-k*k+w*w)/Z
 b=2*w*(d*d+k*k+w*w)/Z
 return a,b

def zero_formula(k,d,w):
 if not(0<k<d and w>0):raise ValueError
 a,b=params(k,d,w)
 phi=math.atan2(b,a)
 h=math.cos(phi)
 lam=d-k
 delta=math.atan(lam/w)
 z=((w/lam)*math.log(math.cos(delta)/h)+delta+phi)/(2*math.pi)
 N=max(0,math.ceil(z)-1)
 T= 1 if (z>=1 and abs(z-round(z))<1e-11) else 0
 return 2*N+T,z,phi

def A(k,d,w,t):
 a,b=params(k,d,w)
 return a*(math.exp(-k*t)-math.exp(-d*t)*math.cos(w*t))+b*math.exp(-d*t)*math.sin(w*t)

# Independent stationary-past and forward covariance integration.
random.seed(8549)
mp.mp.dps=35
for i in range(70):
 k=10**random.uniform(-1,0.7);d=10**random.uniform(-1,0.5);w=10**random.uniform(-1,1);t=random.uniform(.03,4)
 q=mp.re(mp.exp((-d+1j*w)*t)/(k+d-1j*w))
 p=mp.exp(-k*t)*mp.re(1/(k+d-1j*w))+mp.quad(lambda s:mp.exp(-k*(t-s)-d*s)*mp.cos(w*s),[0,t])
 assert abs(float(p-q)-A(k,d,w,t))<4e-9,(k,d,w,t,float(p-q),A(k,d,w,t))
print('PASS: 70 independent stationary-past/forward-integral identities')

for i in range(150):
 d=10**random.uniform(-.6,.4);k=d*random.uniform(.05,.95);w=d*random.uniform(.02,14)
 n,z,phi=zero_formula(k,d,w)
 # exactly count roots via strictly monotone per positive lobe using endpoints and derivative maximum
 a,b=params(k,d,w);lam=d-k
 delta=math.atan(lam/w);h=math.cos(phi)
 found=0
 # each j>=1 has two if max exceeds h, one if equals h. Compute 20 extra lobes.
 for j in range(1,int(max(4,n/2+10))):
  tj=(2*math.pi*j-delta-phi)/w
  peak=math.exp(-lam*tj)*math.cos(delta)
  if peak>h+1e-11:found+=2
  elif abs(peak-h)<1e-11: found+=1
 assert n==found,(k,d,w,z,n,found)
print('PASS: 150 exact positive-lobe zero-count comparisons')

# Representative off-resonance regimes.
for k,d,w in [(0.5,1,1),(0.5,1,3),(.5,1,10),(.9,1,5),(.2,1,10)]:
 print('case',k,d,w,'positive zeros',zero_formula(k,d,w)[:2])
# symbolic nonstationary kernel equality from complex fractions
k,d,w,t=sp.symbols('k d w t',real=True,positive=True)
Z=((k-d)**2+w**2)*((k+d)**2+w**2)
a=2*d*(d**2-k**2+w**2)/Z;b=2*w*(d**2+k**2+w**2)/Z
realB=sp.factor(sp.re(1/(k+d-sp.I*w)-1/(k-d+sp.I*w))-a)
imagB=sp.factor(sp.im(1/(k+d-sp.I*w)-1/(k-d+sp.I*w))-b)
assert realB==0 and imagB==0,(realB,imagB)
print('PASS: symbolic amplitude coefficients')
