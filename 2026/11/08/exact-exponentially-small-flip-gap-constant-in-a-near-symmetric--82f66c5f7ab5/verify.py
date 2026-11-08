"""Finite exact and high-precision checks for the sharp exponential flip gap.

Run with: python3 verify.py (Python 3.11+, standard library only).
The analytic uniform theorem is proved in RESULT.md, not by finite tests.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def check_identity():
    num = 0
    for k in range(2, 14):
        d = Fraction(1, k)
        b = (1-d)/2
        a = Fraction(k+5, 2)
        for m in range(1, 12):
            x = b*Fraction(m, 17)
            y = 2*b-x
            qx = x*(1-x)
            qy = y*(1-y)
            u = b-x
            c = b*(1-b)
            product = (1-a*qx)*(1-a*qy)
            transformed = (1-a*(c-u*u))**2-(a*d*u)**2
            assert product == transformed
            num += 1
    return num


def cycle_point(a, d):
    b = (1-d)/2
    x0 = ((1-d)/d)*(-a*b).exp()
    z = x0.ln()
    for i in range(65):
        x = z.exp()
        if not (0 < x < b):
            raise AssertionError('cycle-point iteration left admissible interval')
        resid = (1-x).ln()+(1-d-x).ln()-(d+x).ln()-z-a*(b-x)
        deriv = -1+x*(a-1/(1-x)-1/(1-d-x)-1/(d+x))
        step = resid/deriv
        z -= step
        if abs(step) < Decimal('1e-75'):
            break
    x = z.exp()
    rel = (1-x).ln()+(1-d-x).ln()-(d+x).ln()-z-a*(b-x)
    assert abs(rel) < Decimal('1e-70')
    return x


def multiplier(a, d):
    x = cycle_point(a,d)
    y = 1-d-x
    return (1-a*x*(1-x))*(1-a*y*(1-y))


def check_asymptotics():
    ds = ['0.125','0.1','0.08','0.06','0.05','0.04']
    ratios = []
    with localcontext() as ctx:
        ctx.prec = 92
        for val in ds:
            d=Decimal(val)
            base=2/(d*(1-d))
            pred=4/(d*d*(1-d))*(-1/d).exp()
            lo=base
            hi=base+3*pred
            assert multiplier(lo,d)>-1 and multiplier(hi,d)<-1
            for k in range(150):
                mid=(lo+hi)/2
                if multiplier(mid,d)>-1:
                    lo=mid
                else:
                    hi=mid
            af=(lo+hi)/2
            xf=cycle_point(af,d)
            xb=cycle_point(base,d)
            relgap=(af-base)/pred
            relx=xf/((1-d)/d*(-1/d).exp())
            margin=(multiplier(base,d)+1)/(4/d*(-1/d).exp())
            assert abs(multiplier(af,d)+1)<Decimal('1e-38')
            assert Decimal('0.75') < relgap < Decimal('1.3')
            assert Decimal('0.75') < relx < Decimal('1.1')
            assert Decimal('0.75') < margin < Decimal('1.3')
            ratios.append((float(d),float(relgap),float(relx),float(margin)))
        assert abs(ratios[-1][1]-1)<1e-4
        assert abs(ratios[-1][2]-1)<1e-4
        assert abs(ratios[-1][3]-1)<1e-4
    return ratios


if __name__=='__main__':
    count=check_identity()
    results=check_asymptotics()
    for d,gap,coord,margin in results:
        print(f'd={d:.3f} normalized_gap={gap:.10f} normalized_coordinate={coord:.10f} normalized_margin={margin:.10f}')
    print(f'VERIFY_OK rational_multiplier_identites={count} high_precision_parameters={len(results)}')
