"""Finite diagnostics for two extinction clocks of a Ricker predator–prey map.

Python 3 standard library only. The analytic proof is in RESULT.md.
"""
from decimal import Decimal, localcontext
import math


def subcritical():
    with localcontext() as ctx:
        ctx.prec = 90
        R = Decimal('0.7'); alpha = Decimal('1.5')
        x = Decimal('0.2'); y = Decimal('0.07')
        xs = []
        for n in range(140):
            assert 0 < y < R * (-x).exp()
            xs.append(x)
            x, y = x * (R*(-x).exp()-y), alpha*x*y
        cs = [xs[n]/R**n for n in (65, 80, 100, 130)]
        assert abs(cs[-1]/cs[-2]-1) < Decimal('1e-12')
        C = cs[-1]
        logD = Decimal('0.07').ln()+sum((xs[k]/(C*R**k)).ln() for k in range(139))
        observed = y.ln()-140*(alpha*C).ln()-Decimal(140*139//2)*R.ln()
        assert abs(observed-logD) < Decimal('1e-12')
        return 'subcritical C=%.15g; D=%.15g' % (C,logD.exp())


def critical():
    alpha=1.5; x=0.2; logy=math.log(0.08)
    snap={}
    for n in range(1,100001):
        y=math.exp(logy) if logy>-700 else 0.0
        assert y<math.exp(-x)
        xnew=x*(math.exp(-x)-y)
        logy+=math.log(alpha*x)
        x=xnew
        if n in (1000,10000,50000,100000):
            H=1/x-n-.5*math.log(n)
            snap[n]=(x,logy,H)
    H=snap[100000][2]
    assert abs(H-snap[50000][2]) < .0002
    vals={}
    for n,(x,logy,h) in snap.items():
        ln=math.log(n)
        vals[n]=logy-n*math.log(alpha)+math.lgamma(n)+.25*ln*ln+H*ln
    assert abs(vals[100000]-vals[50000]) < .005
    return 'critical H~%.12f; log D~%.12f; samples=%s'%(H, vals[100000],[(n,round(v,9)) for n,v in vals.items()])

if __name__=='__main__':
    print(subcritical())
    print(critical())
    print('diagnostic PASS; no finite test substitutes for the proof')
