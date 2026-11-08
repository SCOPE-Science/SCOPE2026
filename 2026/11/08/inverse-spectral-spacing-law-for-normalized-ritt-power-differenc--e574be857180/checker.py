"""Finite numerical diagnostics for normal ray-spectrum Ritt contractions.
These checks sample finite diagonal truncations and are not proofs of the
infinite-dimensional extremal limits.
"""
import math


def normalized_difference(n, radii, cosine):
    out = 0.0
    for r in radii:
        v = -2.0 * cosine*r + r*r
        if v <= -1.0:
            raise ValueError('nonpositive squared modulus')
        a = n*r * math.exp(0.5*n*math.log1p(v))
        out = max(out, a)
    return out


def limit_constants(q, cosine):
    if q == 0:
        fraction = 0.0
    elif q == 1:
        fraction = 1.0
    else:
        L = -math.log(q)/(1-q)
        fraction = math.e*L*math.exp(-L)
    return fraction/(math.e*cosine), 1/(math.e*cosine)


def run():
    assertions=0
    for phi in (0.0, math.pi/6, math.pi/4):
        b=math.cos(phi)
        for q in (0.25,0.50,0.80):
            rs=[0.08*q**k for k in range(130)]
            lo,hi=limit_constants(q,b)
            L=-math.log(q)/(1-q)
            for k in (12,20,30):
                if rs[k] < 1e-14:continue
                np=max(1,round(1/(b*rs[k])))
                nv=max(1,round(L/(b*rs[k])))
                peak=normalized_difference(np,rs,b)
                valley=normalized_difference(nv,rs,b)
                assert abs(peak-hi)<0.005,(phi,q,k,'peak',peak,hi)
                assert abs(valley-lo)<0.005,(phi,q,k,'valley',valley,lo)
                assert peak>=valley-1e-8
                assertions+=3
        rs=[0.15*math.exp(-math.sqrt(k)) for k in range(1,1201)]
        lo,hi=limit_constants(1,b)
        for k in (180,400,700):
            n=round(1/(b*rs[k]))
            value=normalized_difference(n,rs,b)
            assert abs(value-hi)<0.004,(phi,k,value,hi)
            assertions+=1
        rs=[0.20*math.exp(-2**k) for k in range(0,11)]
        lo,hi=limit_constants(0,b)
        for j in (3,4,5):
            npeak=round(1/(b*rs[j]))
            nvalley=round(1/(b*math.sqrt(rs[j]*rs[j+1])))
            peak=normalized_difference(npeak,rs,b)
            valley=normalized_difference(nvalley,rs,b)
            assert abs(peak-hi)<0.006,(phi,j,peak,hi)
            assert valley<0.12,(phi,j,valley)
            assertions+=2
    # Analytic finite adjacent-crossing calculations, away from machine limits.
    for q in [i/100 for i in range(1,100)]:
        L=-math.log(q)/(1-q)
        assert 1<L<1/q
        assert abs(L*math.exp(-L) - q*L*math.exp(-q*L))<1e-12
        assertions+=2
    print('finite_diagnostics_passed',assertions)

if __name__=='__main__':run()
