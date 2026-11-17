#!/usr/bin/env python3
"""Reproducible finite checks for the quadratic-map basin-edge laws.
The asymptotic theorem is analytic; these calculations are consistency checks.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def affine_parts(a, b, s):
    q = a * (1 - s*s) + b * s * (2-s)
    return q/2, b*s*(2-s)/q


def logarithmic_deficit(a, b, s, steps=260):
    a, b, s = Decimal(str(a)), Decimal(str(b)), Decimal(str(s))
    original = a/2
    result = Decimal(0)
    weight = Decimal(1)/2
    for _ in range(steps):
        h, new_s = affine_parts(a, b, s)
        result += weight * (h/original).ln()
        s = new_s
        weight /= 2
    return result


def critical_radius(a, b, s):
    a,b,s=Decimal(str(a)),Decimal(str(b)),Decimal(str(s))
    with localcontext() as ctx:
        ctx.prec = 100
        return (Decimal(2)/a)*(-logarithmic_deficit(a,b,s)).exp()


def run():
    # Direct exact decomposition of the given two-coordinate quadratic map.
    for a,b,s,t in [(Fraction(3,4),Fraction(5,4),Fraction(3,7),Fraction(9,5)),
                    (Fraction(3,2),Fraction(1,1),Fraction(1,11),Fraction(5,4))]:
        x,y=t*(1-s),t*s
        xn=a*x*(x+2*y)/2
        yn=b*y*(y+2*x)/2
        h,sp=affine_parts(a,b,s)
        assert xn+yn==t*t*h
        assert yn/(xn+yn)==sp
    with localcontext() as ctx:
        ctx.prec=110
        T=Decimal(3)
        def delta(a,b,k): return logarithmic_deficit(a,b,Decimal(10)**(-k))
        # Below the corner resonance the exact linear coefficient is 3.
        v1=delta(1,Decimal('0.75'),8)/Decimal('1e-8')
        v2=delta(1,Decimal('0.75'),24)/Decimal('1e-24')
        assert abs(v2-T)<abs(v1-T) and abs(v2-T)<Decimal('0.00001')
        # At resonance the slope has the universal reciprocal-log-2 coefficient.
        goal=Decimal(1)/Decimal(2).ln()
        d1=delta(1,1,8)/(Decimal('1e-8')*Decimal('1e8').ln())
        d2=delta(1,1,44)/(Decimal('1e-44')*Decimal('1e44').ln())
        assert abs(d2-goal)<abs(d1-goal) and abs(d2-goal)<Decimal('0.02')
        # Above resonance the sharp exponent, not necessarily an asymptotic constant,
        # controls the deficit; compare separated logarithmic secants.
        alpha=Decimal(2).ln()/Decimal(3).ln()
        a1=delta(1,Decimal('1.5'),16)
        a2=delta(1,Decimal('1.5'),40)
        slope=(a2/a1).ln()/(Decimal('1e-40')/Decimal('1e-16')).ln()
        assert abs(slope-alpha)<Decimal('0.004'), (slope,alpha)
        assert a1>0 and a2>0
        # Both positive endpoint equilibria and finite-part iterates agree.
        for a,b,s in [('1','0.75','0.025'),('1','1','0.025'),('1','1.5','0.025')]:
            sa=Decimal(s);aa=Decimal(a);bb=Decimal(b)
            h,ss=affine_parts(aa,bb,sa)
            rr=critical_radius(aa,bb,sa)
            rnext=critical_radius(aa,bb,ss)
            assert abs((h*rr*rr/rnext)-1)<Decimal('1e-35')
        assert critical_radius('1','1','0') == Decimal(2)
        assert abs(critical_radius('1','1','1') - Decimal(2))<Decimal('1e-70')
    print('QUADRATIC_MAP_ENDPOINT_REGULARITY_CHECK_OK')

if __name__=='__main__':
    run()
