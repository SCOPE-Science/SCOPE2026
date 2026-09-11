"""Dain-trial upper bound on MOTS principal eigenvalue along exact Kerr horizon (analytic).
m=1, r=r+(a), Sig=r^2+a^2 cos^2, P=2mr=2r.
Analytic: R=2P(r^2-3a^2 cos^2)/Sig^3; trial alpha=sqrt(Sig), |D alpha|^2=a^4 s^2 c^2/Sig^2.
1/W (rotation LB integrand) = 2 P^3 s^3/(pi Sig^2); LB=(8J)^2/int(1/W).
All integrands regular (pole-safe). Simpson quadrature. Stdlib only.
"""
import math

def horizon_Qup(a, n=20000):
    m = 1.0
    r = m+math.sqrt(m*m-a*a)
    P = 2*m*r
    h = math.pi/n
    N0 = 0.0; D = 0.0; Winv = 0.0
    for i in range(n+1):
        t = i*h
        s = math.sin(t); c = math.cos(t)
        S = r*r+a*a*c*c
        R = 2*P*(r*r-3*a*a*c*c)/(S**3)
        al2 = S
        grad2 = (a**4)*(s*s)*(c*c)/(S*S)
        w = P*s*2*math.pi
        fN = (grad2+0.5*R*al2)*w
        fD = al2*w
        fW = 2*(P**3)*(s**3)/(math.pi*S*S)
        coef = 1 if (i == 0 or i == n) else (4 if i % 2 == 1 else 2)
        N0 += coef*fN; D += coef*fD; Winv += coef*fW
    N0 *= h/3; D *= h/3; Winv *= h/3
    J = a*m
    LB = (8*J)**2/Winv
    Qup = (N0-LB)/D
    A = 8*math.pi*m*r
    delta = r/a-1.0
    return dict(a=a, r=r, A=A, J=J, delta=delta, N0=N0, D=D, LB=LB, Qup=Qup,
                QupA=Qup*A, Hup=1.0/math.sqrt(Qup) if Qup > 0 else float('inf'))

print(f"{'a':>8} {'delta':>12} {'N0':>10} {'LB':>10} {'D':>10} {'Qup':>12} {'Qup*A':>9} {'Hup/Hfl':>8}")
for a in [0.5, 0.7, 0.9, 0.95, 0.99, 0.999, 0.9999, 0.99999]:
    q = horizon_Qup(a)
    Hf = math.sqrt(q['A'])/(8*math.sqrt(q['delta']))
    print(f"{a:8.5f} {q['delta']:12.4e} {q['N0']:10.4f} {q['LB']:10.4f} {q['D']:10.4f} "
          f"{q['Qup']:12.5e} {q['QupA']:9.5f} {q['Hup']/Hf:8.4f}")
