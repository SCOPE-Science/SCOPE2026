"""Exact rational phase-cell verification for triangular-grid crossing counts.
No external packages are required. Run: python3 triangular_crossing_check.py
"""
from fractions import Fraction as Q
from itertools import product
from math import isclose


def clip(poly, a, b, c):
    """Clip a rational polygon by a*u + b*v <= c."""
    if not poly:
        return []
    out=[]
    for p,r in zip(poly,poly[1:]+poly[:1]):
        fp=a*p[0]+b*p[1]-c
        fr=a*r[0]+b*r[1]-c
        if fp <= 0:
            out.append(p)
        if (fp<0 and fr>0) or (fp>0 and fr<0):
            t=fp/(fp-fr)
            out.append((p[0]+t*(r[0]-p[0]),p[1]+t*(r[1]-p[1])))
    return out


def area(poly):
    if len(poly)<3:return Q(0)
    a=sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly, poly[1:]+poly[:1]))
    return abs(a)/2


def phase_probability(alpha,beta,bits):
    gamma=(alpha+beta)%1
    sq=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    # Event I1 corresponds to u >= 1-alpha; likewise v.
    pol=sq
    if bits[0]: pol=clip(pol,-1,0,-(1-alpha))
    else: pol=clip(pol,1,0,1-alpha)
    if bits[1]: pol=clip(pol,0,-1,-(1-beta))
    else: pol=clip(pol,0,1,1-beta)
    total=Q(0)
    for k in [0,1]:
        base=clip(clip(pol,-1,-1,-k),1,1,k+1)
        if bits[2]: base=clip(base,-1,-1,-(k+1-gamma))
        else: base=clip(base,1,1,k+1-gamma)
        total+=area(base)
    return total


def expected_cumulant(alpha,beta):
    if alpha+beta<=1:
        return alpha*beta*(1-alpha-beta)
    return -(alpha+beta-1)*(1-alpha)*(1-beta)


def main():
    cases=[(Q(1,3),Q(1,3)),(Q(2,3),Q(2,3)),(Q(1,4),Q(1,2)),
           (Q(5,6),Q(1,3)),(Q(1,3),Q(2,3)),(Q(0),Q(3,7)),
           (Q(1,6),Q(11,12)),(Q(1,5),Q(4,5))]
    for alpha,beta in cases:
        gam=(alpha+beta)%1
        probs={bits:phase_probability(alpha,beta,bits) for bits in product(range(2),repeat=3)}
        assert sum(probs.values())==1,(alpha,beta,sum(probs.values()))
        p=lambda i:sum(v for bits,v in probs.items() if bits[i])
        assert [p(i) for i in range(3)]==[alpha,beta,gam]
        for i in range(3):
            for j in range(i+1,3):
                assert sum(v for bits,v in probs.items() if bits[i] and bits[j])==p(i)*p(j)
        t=sum(v for bits,v in probs.items() if bits==(1,1,1))-alpha*beta*gam
        assert t==expected_cumulant(alpha,beta),(alpha,beta,t,expected_cumulant(alpha,beta))
        from math import comb
        prod_probs={j:Q(0) for j in range(4)}
        for bits in product(range(2),repeat=3):
            v=Q(1)
            for b,p0 in zip(bits,(alpha,beta,gam)):
                v*=p0 if b else 1-p0
            prod_probs[sum(bits)]+=v
        for j in range(4):
            discrepancy=sum(v for bits,v in probs.items() if sum(bits)==j)-prod_probs[j]
            assert discrepancy==t * (-1)**(3-j)*comb(3,j)
        tv=sum(abs(t*(-1)**(3-j)*comb(3,j)) for j in range(4))/2
        assert tv==4*abs(t)
        assert tv<=Q(4,27)
    assert expected_cumulant(Q(1,3),Q(1,3))==Q(1,27)
    assert expected_cumulant(Q(2,3),Q(2,3))==-Q(1,27)
    print('TRIANGULAR_LINE_CROSSING_THIRD_ORDER_RATIONAL_CHECK_OK',len(cases),'cases')

if __name__=='__main__':main()
