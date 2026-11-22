"""Supplementary finite checks for exact BV sensitivity of sliding Aitken acceleration.

Uses only Python's standard library. The universal theorem relies on the analytic
argument in RESULT.md; the finite tests are supporting diagnostics.
"""
from fractions import Fraction as F
from random import Random


def bound(n, q):
    q = F(q)
    assert 0 < q < 1 and n >= 3
    d = (1-q)**2
    if n == 3: return F(0)
    if n == 4: return max(F(1), 2*q)/d
    if n == 5: return (1+2*q)/d
    return (1+q)**2/d


def weights(t):
    d=(1-t)**2
    return (t*t/d, -2*t/d, 1/d)


def tv(z):
    return sum(abs(z[i+1]-z[i]) for i in range(len(z)-1))


def derivative_step(n, ratios, k):
    assert len(ratios) == n-2
    h = [F(int(i >= k)) for i in range(n)]
    return [sum(w*v for w,v in zip(weights(ratios[j]), h[j:j+3]))
            for j in range(n-2)]


def expected_extremal_step(n,q):
    if n == 3:return None
    if n == 4:return 3 if q <= F(1,2) else 2
    return 3


def aitken(x):
    out=[]
    for j in range(len(x)-2):
        u=x[j+1]-x[j];v=x[j+2]-x[j+1]
        assert u>0 and 0<v<u
        out.append(x[j]+u*u/(u-v))
    return out


def seq_from_ratios(ratios, u0, shift=F(0)):
    u=u0
    x=[shift]
    for j in range(len(ratios)+1):
        x.append(x[-1]+u)
        if j < len(ratios): u*=ratios[j]
    return x


def run():
    qvals=[F(1,10),F(1,3),F(1,2),F(2,3),F(4,5),F(9,10)]
    # Exact rational case analysis of EVERY input jump for homogeneous ratios,
    # with extrema approached at the ratio cap q.
    checks=0
    for q in qvals:
        for n in range(3,16):
            vals=[tv(derivative_step(n,[q]*(n-2),k)) for k in range(1,n)]
            assert max(vals) == bound(n,q),(n,q,max(vals),bound(n,q))
            checks+=n-1
    print('EXACT_RATIONAL_STEP_AND_BOUNDARY_IDENTITIES_PASS',checks)

    # Nonhomogeneous ratio patterns, checked using exact rational arithmetic;
    # the upper formula is universal, not just a homogeneous-row calculation.
    rng=Random(421073)
    trials=0
    for q in qvals:
        for n in range(3,15):
            for _ in range(50):
                ratios=[q*F(rng.randrange(1,100),100) for _ in range(n-2)]
                for k in range(1,n):
                    assert tv(derivative_step(n,ratios,k)) <= bound(n,q)
                    trials+=1
    print('EXACT_HETEROGENEOUS_DERIVATIVE_STEP_BOUNDS_PASS',trials)

    # Global two-input tests (not merely Jacobian tests); the admissible cone
    # is convex. Rational arithmetic avoids near-constant cancellation.
    trials=0
    for q in qvals:
        for n in range(3,12):
            for _ in range(50):
                ra=[q*F(rng.randrange(1,100),100) for _ in range(n-2)]
                rb=[q*F(rng.randrange(1,100),100) for _ in range(n-2)]
                x=seq_from_ratios(ra,F(rng.randrange(1,30),10),F(rng.randrange(-20,21)))
                y=seq_from_ratios(rb,F(rng.randrange(1,30),10),F(rng.randrange(-20,21)))
                h=[a-b for a,b in zip(x,y)]
                a=aitken(x); b=aitken(y)
                assert tv([v-w for v,w in zip(a,b)])<=bound(n,q)*tv(h)
                trials+=1
    print('EXACT_RATIONAL_TWO_INPUT_INEQUALITIES_PASS',trials)

    # Explicit geometric-baseline perturbations approach each sharp value.
    # Use exact fractions for a perturbation that preserves the cone.
    witnesses=0
    for q in qvals:
        for n in (4,5,6,9):
            k=expected_extremal_step(n,q)
            t=q*(1-F(1,1000000))
            base=seq_from_ratios([t]*(n-2),F(1))
            h=[F(int(i>=k)) for i in range(n)]
            # sufficiently tiny positive perturbation, keeping all ratios < q
            # and all increments positive, checked directly.
            delta=F(1,10**14)
            pert=[v+delta*w for v,w in zip(base,h)]
            for j in range(n-2):
                u=pert[j+1]-pert[j]; v=pert[j+2]-pert[j+1]
                assert u>0 and 0<v<q*u
            num=tv([a-b for a,b in zip(aitken(pert),aitken(base))])
            actual=num/(delta*tv(h))
            assert actual <= bound(n,q)
            assert actual > bound(n,q)*F(99998,100000),(n,q,actual,bound(n,q))
            witnesses+=1
    print('EXACT_NEAR_SHARPNESS_PERTURBATIONS_PASS',witnesses)
    print('ALL_SLIDING_AITKEN_VARIATION_CHECKS_PASS')


if __name__=='__main__':run()
