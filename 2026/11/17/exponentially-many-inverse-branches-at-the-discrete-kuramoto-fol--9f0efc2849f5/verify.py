"""Reproduce algebraic and finite checks for the coupled phase-map inverse branches.

The analytical claims are proved separately; this finite checker does not certify them.
"""
import itertools
import math
import sympy as sp


def root_d(K):
    assert K > 1
    # The strictly decreasing function sin(d)/d crosses 1/K once on (0, pi).
    a, b = 1.0e-12, math.pi
    for _ in range(100):
        mid = (a+b)/2
        if K*math.sin(mid) > mid:
            a = mid
        else:
            b = mid
    return (a+b)/2


def test_branches():
    count = 0
    for n in range(2,9):
        frequencies = [(i - n/3)/11.0 for i in range(n)]
        for K in [1.01, 1.12, 1.75, 4.0, 10.0]:
            d = root_d(K)
            assert 0 < d < math.pi and abs(d - K*math.sin(d)) < 1.e-11
            # The 0-input and the two-cluster inputs are pairwise distinct by signs.
            seen = set()
            for bits in itertools.product([False, True], repeat=n):
                m = sum(bits)
                if m == n:
                    continue
                if m == 0:
                    xs = [0.0]*n
                else:
                    xs = [(n-m)*d/n if bits[i] else -m*d/n for i in range(n)]
                signs = tuple(0 if abs(z)<1.e-14 else (1 if z>0 else -1) for z in xs)
                assert signs not in seen
                seen.add(signs)
                if m:
                    assert abs(sum(xs)) < 2.e-13
                    assert abs(sum(z*z for z in xs) - m*(n-m)*d*d/n)<3.e-12
                output = [xs[i]+frequencies[i] + K/n*sum(math.sin(xs[j]-xs[i]) for j in range(n)) for i in range(n)]
                assert max(abs(output[i]-frequencies[i]) for i in range(n))<5.e-12
                count += 1
            assert len(seen) == 2**n -1
    return count


def test_spectrum():
    d,t=sp.symbols('d t',real=True)
    k=d/sp.sin(d)
    ls=1-k*(t+(1-t)*sp.cos(d))
    lc=1-k*((1-t)+t*sp.cos(d))
    cross=1-k*sp.cos(d)
    assert sp.simplify(sp.limit(ls/d**2,d,0)-(2-3*t)/6)==0
    assert sp.simplify(sp.limit(lc/d**2,d,0)-(3*t-1)/6)==0
    assert sp.simplify(sp.limit(ls.subs(t,sp.Rational(2,3))/d**4,d,0)+sp.Rational(1,180))==0
    assert sp.simplify(sp.limit(lc.subs(t,sp.Rational(1,3))/d**4,d,0)+sp.Rational(1,180))==0
    assert sp.simplify(sp.limit(cross/d**2,d,0)-sp.Rational(1,3))==0
    q=(sp.sin(d)/d-sp.cos(d))/(1-sp.cos(d))
    assert sp.simplify(sp.limit(q,d,0)-sp.Rational(2,3))==0
    assert sp.simplify(sp.limit(q,d,sp.pi)-sp.Rational(1,2))==0
    return True


def test_jacobians():
    import numpy as np
    checks=0
    for n in range(2,8):
      K=1.2
      d=root_d(K)
      for m in range(1,n):
        xs=np.array([(n-m)*d/n]*m+[-m*d/n]*(n-m))
        J=np.eye(n)
        for i in range(n):
          for j in range(n):
            if i != j:
                v=K/n*math.cos(xs[j]-xs[i])
                J[i,j]+=v
                J[i,i]-=v
        spec=sorted(np.linalg.eigvalsh(J))
        formula=sorted([1.0,1-K*math.cos(d)]
                  + [1-K/n*(m+(n-m)*math.cos(d))]*(m-1)
                  + [1-K/n*((n-m)+m*math.cos(d))]*(n-m-1))
        assert np.max(np.abs(np.array(spec)-formula))<3e-12
        checks+=1
    return checks


if __name__ == '__main__':
    assert test_spectrum()
    trials=test_branches()
    spec=test_jacobians()
    print(f'VERIFY_OK exact_eigenvalue_expansions=5 q_endpoints=2 two_cluster_preimages={trials} numerical_jacobian_spectra={spec}')
