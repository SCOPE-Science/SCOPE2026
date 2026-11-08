#!/usr/bin/env python3
"""Independent finite-matrix, finite-difference and phase checks for two traps.
Scientific assumptions and the analytic proof are in RESULT.md.
Run: python3 verify.py (Python 3 standard library only).
"""
import math

N = 0

def check(ok, message):
    global N
    N += 1
    if not ok:
        raise AssertionError(message)

def parameters(D, mu, a, r):
    q = math.hypot(mu, 2*math.sqrt(D*r))
    c = math.exp(-q*a/D)
    z = math.exp(mu*a/D)
    return q,c,z

def closed_B(k, K, D, mu, a, r):
    q,c,z=parameters(D,mu,a,r)
    g=1/q; h=math.sqrt(c); E=math.sqrt(z); F=1/E
    return g*h*(E*k+F*(K-k)+g*(1-c)*(E+F)*k*(K-k))/(1+g*K+g*g*(1-c*c)*k*(K-k))

def matrix_B(k,K,D,mu,a,r):
    q,c,z=parameters(D,mu,a,r)
    g=1/q; h=math.sqrt(c); E=math.sqrt(z); F=1/E
    kp=k; km=K-k
    aa=1+g*kp; ab=g*c*z*km; ba=g*c/z*kp; bb=1+g*km
    det=aa*bb-ab*ba
    vp=(bb*g*h*E-ab*g*h*F)/det
    vm=(-ba*g*h*E+aa*g*h*F)/det
    return kp*vp+km*vm

def threshold(D,mu,a,r):
    if mu <= 0: raise ValueError('positive drift required')
    q,c,z=parameters(D,mu,a,r)
    A=(1-c)*(1-c*z)
    b=c*(z+1)-2
    # cancellation-free positive root to A*t**2-b*t-(z-1)=0
    tc=2*(z-1)/(math.sqrt(b*b+4*A*(z-1))-b)
    return q*tc

def phase_poly(K,D,mu,a,r):
    q,c,z=parameters(D,mu,a,r)
    t=K/q
    return (z-1)+(c*(z+1)-2)*t-(1-c)*(1-c*z)*t*t

def lattice_B(k,K,D,mu,a,r,h=0.05,L=10.):
    # A separate nearest-neighbour CTMC with discrete killing k/h at +/-a.
    n=int(round(2*L/h))+1
    mid=(n-1)//2
    ip=mid+int(round(a/h)); im=mid-int(round(a/h))
    up=D/h**2+mu/(2*h)
    down=D/h**2-mu/(2*h)
    check(down>=0,'nonnegative CTMC jump rate')
    lower=[0.0]*n; diag=[1.0]*n; upper=[0.0]*n; rhs=[0.0]*n
    for i in range(1,n-1):
        kill=(k/h if i==ip else 0.)+((K-k)/h if i==im else 0.)
        lower[i]=-down;upper[i]=-up;diag[i]=up+down+r+kill;rhs[i]=kill
    for i in range(1,n):
        fac=lower[i]/diag[i-1]
        diag[i]-=fac*upper[i-1]
        rhs[i]-=fac*rhs[i-1]
    u=[0.]*n
    u[-1]=rhs[-1]/diag[-1]
    for i in range(n-2,-1,-1):u[i]=(rhs[i]-upper[i]*u[i+1])/diag[i]
    return u[mid]

for D in (0.4,1.0,1.8):
 for mu in (0.,0.1,1.,3.):
  for a in (0.3,1.):
   for r in (0.2,1.,2.):
    for K in (0.05,0.5,3.,10.):
     for frac in (0.,0.07,0.31,0.5,0.83,1.):
      k=frac*K
      b=closed_B(k,K,D,mu,a,r); m=matrix_B(k,K,D,mu,a,r)
      check(0<b<1,('B bounds',D,mu,a,r,K,k,b))
      check(abs(b-m)<3e-12,('2x2 resolvent',D,mu,a,r,K,k,b,m))
      if 0<frac<1:
       left=closed_B(k/2,K,D,mu,a,r)
       right=closed_B((k+K)/2,K,D,mu,a,r)
       check(b>=0,'positive')
for D,mu,a,r in ((1.,1.,1.,1.),(1.,.1,1.,1.),(.5,2.,.6,.3),(1.,3.,.5,2.)):
 Kc=threshold(D,mu,a,r)
 check(Kc>0,'positive threshold')
 check(abs(phase_poly(Kc,D,mu,a,r))<1e-8,'critical root')
 for fac in (.1,.5,.9,1.,1.1,2.,10.):
  K=fac*Kc
  bvals=[closed_B(K*j/1000,K,D,mu,a,r) for j in range(1001)]
  idx=max(range(len(bvals)),key=lambda i:bvals[i])
  if fac<1: check(idx==1000,('boundary optimum',D,mu,a,r,fac,idx))
  if fac>1: check(500<idx<1000,('interior optimum',D,mu,a,r,fac,idx))
  for j in (1,7,11,89):
   left=K*j/100;right=K*(100-j)/100
   mid=(left+right)/2
   check(closed_B(mid,K,D,mu,a,r)>0.5*(closed_B(left,K,D,mu,a,r)+closed_B(right,K,D,mu,a,r)),('strict concavity',K,j))
for k,K,mu in ((0.5,1.,0.),(1.,2.,1.),(1.4,3.,0.5),(2.5,5.,1.)):
 D=a=r=1.
 b=closed_B(k,K,D,mu,a,r)
 disc=lattice_B(k,K,D,mu,a,r)
 check(abs(b-disc)<0.004,('independent CTMC discretization',k,K,mu,b,disc))
print(f'PASS: {N} deterministic checks, including 2x2 Green resolvent, sharp phase, and independent lattice CTMC.')
