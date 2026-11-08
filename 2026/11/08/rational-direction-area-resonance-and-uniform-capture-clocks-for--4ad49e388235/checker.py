"""Exact rational checker for the two-sheet, one-sided-barrier return dynamics.

Standalone: python3 checker.py. All input values and calculations use Fraction.
The proof of the theorem is mathematical; this script is finite stress testing.
"""
from fractions import Fraction as Q
from math import gcd

def mod1(x):
    return x - x.numerator // x.denominator

def inside(y,a,b):
    return a < y < a+b

def phase_update(u,s,alpha,a,b):
    v=mod1(u+alpha)
    return v, (0 if s==1 or inside(v,a,b) else 1)

def classify(u,alpha,a,b,q):
    # A phase is hit when some one of the next q samples is in the barrier.
    hit=any(inside(mod1(u+j*alpha),a,b) for j in range(1,q+1))
    if not hit:
        return False, None
    # Periodic label after q steps: both initial sheets map to same state.
    out=[]
    for s in (0,1):
        v, t=u,s
        for j in range(q):
            v,t=phase_update(v,t,alpha,a,b)
        out.append(t)
    assert out[0]==out[1]
    survivor=out[0]
    # The only sheet periodic from this initial phase has that survivor label.
    v,t=u,survivor
    for j in range(q):
        v,t=phase_update(v,t,alpha,a,b)
    assert v==u and t==survivor
    # The transient sheet merges after the first positive barrier visit.
    wait=next(j for j in range(1,q+1) if inside(mod1(u+j*alpha),a,b))
    v,t=u,1-survivor
    for j in range(wait):
        v,t=phase_update(v,t,alpha,a,b)
    w,rec=u,survivor
    for j in range(wait):
        w,rec=phase_update(w,rec,alpha,a,b)
    assert (v,t)==(w,rec)
    return True, wait

def test(p,q,a,b):
    alpha=Q(p,q)
    # Partition by all rational endpoints of translated barriers (mod 1).
    cuts={Q(0),Q(1)}
    for j in range(q):
        cuts.add(mod1(a-j*alpha))
        cuts.add(mod1(a+b-j*alpha))
    cuts=sorted(cuts)
    area=Q(0)
    waits={i:Q(0) for i in range(1,q+1)}
    for l,r in zip(cuts, cuts[1:]):
        mid=(l+r)/2
        hit,t=classify(mid,alpha,a,b,q)
        if hit:
            area+=r-l
            waits[t]+=r-l
        else:
            # Both sheets must be periodic: period q when q is even, 2q otherwise.
            for s in (0,1):
                v,w=mid,s
                for _ in range(2*q):
                    v,w=phase_update(v,w,alpha,a,b)
                assert (v,w)==(mid,s)
    assert area==min(Q(1),q*b),(p,q,a,b,area)
    if q*b<Q(1):
        assert all(w==b for w in waits.values()),(p,q,a,b,waits)
    return len(cuts)-1

def main():
    cases=0; strata=0
    for q in range(1,19):
        for p in range(1,2*q+1):
            if gcd(p,q)!=1: continue
            for b in (Q(1,5*q),Q(3,5*q),Q(1,2*q),Q(3,2*q),Q(1,3),Q(2,3)):
                if not (0<b<1): continue
                for a in (Q(0), (Q(1)-b)/3):
                    strata+=test(p,q,a,b)
                    cases+=1
    print(f'PASS: {cases} rational-angle/barrier tests; {strata} exact phase strata')
    print('Validated rational phase classification, finite-time coalescence, area law, and uniform hitting clocks in non-overlap regime.')
if __name__=='__main__': main()
