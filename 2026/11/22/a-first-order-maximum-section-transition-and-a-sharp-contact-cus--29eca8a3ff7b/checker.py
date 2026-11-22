"""Complementary finite numerical diagnostics for capped-paraboloid centroidal sections.

The analytic proof is in RESULT.md; these tests do not certify global claims.
Run with Python 3: python checker.py
"""
import math

PI = math.pi
C = 2.0/3.0
E = 1.0/3.0


def projected_area(s):
    """Exact circular-segment expression, dimensionless projected area."""
    if s <= E:
        return PI*(C+s*s/4.0)
    rho = math.sqrt(C+s*s/4.0)
    z = max(-1.0,min(1.0,(E/s-s/2.0)/rho))
    return rho*rho*(math.acos(-z)+z*math.sqrt(max(0.0,1-z*z)))


def projected_area_integral(s, subdivisions=8192):
    """Independent Simpson integral of cross-sectional widths in original xy coordinates."""
    lo = -2*C/(s+math.sqrt(s*s+4*C)) if s>0 else -math.sqrt(C)
    hi = (s+math.sqrt(s*s+4*C))/2.0
    if s > E:
        hi = min(hi, E/s)
    if s == 0:
        lo = -math.sqrt(C)
    h=(hi-lo)/subdivisions
    total=0.0
    for j in range(subdivisions+1):
        x=lo+h*j
        height=2*math.sqrt(max(0,C+s*x-x*x))
        w=1 if (j==0 or j==subdivisions) else (4 if j%2 else 2)
        total+=w*height
    return total*h/3


def projected_area_stable(s):
    """Numerically stable integral at steep angles, used only for diagnostics."""
    if s<=E: return projected_area(s)
    lo=-2*C/(1+math.sqrt(1+4*C/s**2))
    n=32768
    step=(E-lo)/n
    acc=0.0
    for j in range(n+1):
        v=lo+j*step
        f=math.sqrt(max(0,C+v-v*v/s**2))
        acc+=(1 if j==0 or j==n else (4 if j%2 else 2))*f
    return (2/s)*step*acc/3


def section_area(s,kappa):
    return math.hypot(1,kappa*s)*projected_area(s)


def critical_square(s):
    area=projected_area_stable(s) if s>=5 else projected_area(s)
    return 1/((4/(3*area))**2-s*s)


def check():
    tests=0
    def confirm(condition,message):
        nonlocal tests
        assert condition,message
        tests+=1

    for s in [0.0,0.02,0.1,0.25,0.3333333,0.334,0.34,0.35,0.367,0.4,0.5,0.7,1,2,4]:
        a=projected_area(s)
        b=projected_area_integral(s)
        confirm(abs(a-b)<2.5e-6+2e-5*a, f'area quadrature failed at {s}: {a}, {b}')

    rho=5/6
    coeff=24*math.sqrt(6)/5
    for delta in [3e-3,1e-3,4e-4,1e-4]:
        s=E+delta
        base=PI*(C+s*s/4)
        loss=base-projected_area(s)
        ratio=loss/(coeff*delta**1.5)
        confirm(abs(ratio-1)<0.06, f'contact coefficient failed: {delta}: {ratio}')

    for s in [0,0.1,0.3,E,0.34,0.35,0.367,0.40,0.5,1,2,4,10]:
        k2=critical_square(s)
        confirm(k2>0, f'critical square positive {s}')
        if s>0:
            compare=section_area(s,math.sqrt(k2))
            confirm(abs(compare-4*math.sqrt(k2)/3)<2e-5, f'exact vertical tie {s}: {compare}')

    confirm(critical_square(E)>3.8, 'critical bound lower')
    confirm(critical_square(0.367)>3.92, 'interior sup lower')
    confirm(critical_square(0.367)>critical_square(E),'interior maximum versus contact')
    confirm(critical_square(0.367)>critical_square(0.5),'interior maximum versus farther tilted')
    for kappa in [0.2,0.8,1.3,1.6,1.9,1.95]:
        confirm(section_area(0.367,kappa)>4*kappa/3,'pre-transition sample')
    for kappa in [2.1,3,5]:
        for s in [0,0.1,0.33,0.367,0.5,1,2,4,10]:
            confirm(section_area(s,kappa)<4*kappa/3,'post-transition sample')
    for kappa in [0.1,0.5,1.0,2.0,5,10]:
        p=1/math.sqrt(1+kappa*kappa/9)
        inferred=3*math.sqrt(1/p**2-1)
        confirm(abs(inferred-kappa)<2e-12,'contact probability inverse')
    # Large-s expansion: s S(s)=4/3-2/(5s^2)+o(s^-2).
    for s in [8,12,20,40]:
        scaled=(4/3-s*projected_area_stable(s))*s*s
        confirm(abs(scaled-0.4)<0.022,'asymptotic coefficient')
    print(f'{tests} deterministic checks passed')

if __name__=='__main__':
    check()
