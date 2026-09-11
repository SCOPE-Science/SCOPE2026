"""Compute I(a)=int|eta|^2 for Kerr horizon r=r+, m=1, and Q proxy upper bound on lam1.
g_phiphi = (2r)^2 sin^2/(r^2+a^2 cos^2) with m=1 (2mr=2r).
dmu = 2r sin th dth dphi.
int|eta|^2 = int g_phiphi dmu = (2r)^3 *2pi * int_0^pi sin^3/(r^2+a^2 cos^2) dth.
Q = 4pi/A - (8pi J)^2/(A*IntEta2); lamQ = Q (upper bound ignoring other negative terms).
Compare sqrt(A)/sqrt? H_Q = 1/sqrt(max(Q,0)); H_floor=sqrt(A)/(8 sqrt(delta)).
"""
import math
def quad(f,a,b,n=200000):
    h=(b-a)/n; s=0.0
    for i in range(n+1):
        x=a+i*h; w=4 if i%2==1 else 2
        if i==0 or i==n: w=1
        s+=w*f(x)
    return s*h/3
m=1.0
print(f"{'a':>8} {'delta':>12} {'A':>9} {'IntEta2':>10} {'16piJ2':>10} {'Q*A/(4pi)':>12} {'H_Q':>8} {'H_floor':>9} {'H_Q/H_fl':>9}")
for a in [0.5,0.7,0.9,0.95,0.99,0.999,0.9999,0.99999]:
    r=m+math.sqrt(m*m-a*a)
    A=8*math.pi*m*r
    J=a*m
    def f(th):
        s=math.sin(th); c=math.cos(th)
        return s**3/(r*r+a*a*c*c)
    I=quad(f,0.0,math.pi,n=20000)
    IntEta2=(2*m*r)**3*2*math.pi*I
    ref=16*math.pi*J*J
    QA=(1.0-ref/IntEta2)  # Q*A/(4pi)
    Q=4*math.pi/A*QA
    HQ=1.0/math.sqrt(Q) if Q>0 else float('inf')
    delta=r/a-1.0
    Hf=math.sqrt(A)/(8*math.sqrt(delta))
    print(f"{a:8.5f} {delta:12.4e} {A:9.4f} {IntEta2:10.3f} {ref:10.3f} {QA:12.5f} {HQ:8.4f} {Hf:9.4f} {HQ/Hf:9.4f}")
