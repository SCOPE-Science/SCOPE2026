"""Exact closed-form check for Kerr horizon rotation integral and Q-proxy limit.
m=1, r=r+(a), I(a)=int_0^pi sin^3/(r^2+a^2 cos^2) dth
      = 2(a^2+r^2)/(r a^3) atan(a/r) - 2/a^2.
IntEta2 = (2r)^3 2pi I, QA = 1 - 16 pi J^2/IntEta2, J=a.
Extremal limit a,r->1: I -> pi-2, QA -> 1-1/(pi-2) ~ 0.12403.
Cross-checks quadrature in kerr_etaWhit.py. Stdlib only.
"""
import math

def I_exact(a, r):
    return 2*(a*a+r*r)/(r*a**3)*math.atan(a/r) - 2/(a*a)

def I_quad(a, r, n=20000):
    h = math.pi/n
    s = 0.0
    for i in range(n+1):
        th = i*h
        w = 1 if (i == 0 or i == n) else (4 if i % 2 == 1 else 2)
        sn, cs = math.sin(th), math.cos(th)
        s += w*sn**3/(r*r+a*a*cs*cs)
    return s*h/3

m = 1.0
print(f"{'a':>8} {'I_exact':>10} {'I_quad':>10} {'|diff|':>10} {'QA':>9} {'HQ/Hf':>8}")
for a in [0.5, 0.7, 0.9, 0.95, 0.99, 0.999, 0.9999, 0.99999]:
    r = m+math.sqrt(m*m-a*a)
    Ie, Iq = I_exact(a, r), I_quad(a, r)
    A = 8*math.pi*m*r
    J = a*m
    IntEta2 = (2*m*r)**3*2*math.pi*Ie
    QA = 1.0-16*math.pi*J*J/IntEta2
    Q = 4*math.pi/A*QA
    HQ = 1.0/math.sqrt(Q)
    delta = r/a-1.0
    Hf = math.sqrt(A)/(8*math.sqrt(delta))
    print(f"{a:8.5f} {Ie:10.6f} {Iq:10.6f} {abs(Ie-Iq):10.2e} {QA:9.5f} {HQ/Hf:8.4f}")
I_ext = math.pi-2
print("extremal: I=pi-2 =", I_ext, " QA -> 1-1/(pi-2) =", 1-1/I_ext)
