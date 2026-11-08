#!/usr/bin/env python3
"""Independent finite checks of an exact Apéry computation.

The general theorem requires the invariant-ring argument in RESULT.md.
"""
from math import gcd

def verify(p,n):
    assert p in (3,5,7,11,13) and n>=2
    D=2*(p-1)
    m=p**(2*n)+1
    assert (m-2*p)%D==0
    L=(m-2*p)//D
    assert L>0 and gcd(p,L)==1
    # Independent residue-class minima from all invariant monomials of y-degree <p.
    invariant=[]
    for b in range(p):
        for a in range(15*D+1):
            if (a+2*b)%D==0:
                pole_upstairs=p*a+m*b
                assert pole_upstairs%D==0
                invariant.append((pole_upstairs//D,a,b))
    residue_min={r:min(t for t,a,b in invariant if t%p==r) for r in range(p)}
    expected={0:0}
    for b in range(1,p):
        w=p+b*L
        assert w%p not in expected
        expected[w%p]=w
    assert residue_min==expected
    F=max(expected.values())-p
    H=lambda t: t>=0 and t>=expected[t%p]
    gaps=[t for t in range(1,F+1) if not H(t)]
    G=(p**(2*n)-1)//4
    assert len(gaps)==G==(p-1)*(L+1)//2
    assert all(H(t) for t in range(F+1,F+10*p))
    PF={t for t in gaps if all(H(t+w) for w in [p]+[p+b*L for b in range(1,p)])}
    assert PF=={b*L for b in range(1,p)}
    assert 2*G==F+len(PF)
    generators=[p]+[p+b*L for b in range(1,p)]
    assert all(not any(H(t) and H(w-t) for t in range(1,w)) for w in generators)
    W=sum(gaps)-G*(G+1)//2
    assert 24*W==(p*p-1)*(L*L-1)
    # Invariant pole orders must be exactly one of the predicted progressions.
    for t,a,b in invariant:
        assert H(t)
        assert t==(p*((a+2*b)//D) + b*L)
    return dict(p=p,n=n,L=L,genus=G,conductor=F+1,type=len(PF),weight=W)

if __name__=='__main__':
    cases=[(3,2),(3,3),(5,2),(5,3),(7,2),(11,2)]
    for p,n in cases: print(verify(p,n))
    print('VERIFY_OK')
