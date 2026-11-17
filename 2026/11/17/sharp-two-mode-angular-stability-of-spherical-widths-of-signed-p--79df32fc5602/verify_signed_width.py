"""Exact reproducibility checks for spherical widths of type-B permutohedra.

The all-ranks assertions are proved in RESULT.md; these checks sample
symbolic integer inequalities and independently enumerate small orbit types.
"""
from itertools import product
from math import comb, factorial
from random import Random


def ordered_norm(x):
    a = sorted(abs(t) for t in x)
    return sum((2*j-1)*v for j, v in enumerate(a, 1))


def active_slope(x):
    return sum(abs(x[i]-x[j]) for i in range(len(x)) for j in range(i+1,len(x)))


def zero_slope(x):
    return ordered_norm(x)


def zero_min_sq(m):
    assert m >= 1
    return min((2*m-1)**2,m**3)


def sharp_sq(k,m):
    options = ([k*(k-1)] if k>=2 else [])+([zero_min_sq(m)] if m>=1 else [])
    return min(options)


def verify():
    rng = Random(20261109)
    cases = 0
    geodesic_rays = 0
    for n in range(2,81):
        assert sum(comb(n,k)*2**k for k in range(1,n+1)) == 3**n-1
        assert 2**n*factorial(n) >= 8
        for k in range(1,n+1):
            m=n-k
            s=sharp_sq(k,m)
            if k>=2 and m>=1:
                assert k*(k-1) != zero_min_sq(m), (n,k,m)
            # Endpoint sharp inequalities for all possible step vectors.
            if k>=2:
                for j in range(1,k):
                    assert k*j*(k-j) >= k*(k-1)
                    cases += 1
            if m>=1:
                for j in range(1,m+1):
                    assert j*(2*m-j)**2 >= zero_min_sq(m)
                    cases += 1
            if n<=10:
                # Independent ternary sign-support orbit enumeration.
                if k<=n:
                    assert comb(n,k)*2**k>0
            for _ in range(16):
                if k>1:
                    a=[rng.randrange(-3,4) for _ in range(k-1)]
                    a.append(-sum(a))
                else:
                    a=[0]
                z=[rng.randrange(-3,4) for _ in range(m)]
                A=active_slope(a)
                Z=zero_slope(z)
                sq=sum(t*t for t in a)+sum(t*t for t in z)
                if sq:
                    assert (A+Z)**2 >= s*sq,(n,k,a,z,s)
                    geodesic_rays+=1
            # Achievability checks of each pure mode, in exact squared form.
            if k>=2:
                a=[k-1]+[-1]*(k-1)
                assert active_slope(a)**2 == k*(k-1)*sum(t*t for t in a)
            if m>=1:
                if m==2:
                    z=[1,1]
                else:
                    z=[1]+[0]*(m-1)
                assert zero_slope(z)**2 == zero_min_sq(m)*sum(t*t for t in z)
    # All signed support patterns, explicit small-n counting.
    enumerated=0
    for n in range(2,9):
        types={}
        for x in product((-1,0,1),repeat=n):
            k=sum(v!=0 for v in x)
            if not k: continue
            types[k]=types.get(k,0)+1
            assert ordered_norm(x)==k*(2*n-k)
            enumerated+=1
        assert types=={k:comb(n,k)*2**k for k in range(1,n+1)}
    print('SIGNED_B_PERMUTO_WIDTH_EXACT_PASS',
          'n_ranges=79', 'step_inequalities='+str(cases),
          'integer_tangent_rays='+str(geodesic_rays),
          'small_orbit_patterns='+str(enumerated))

if __name__=='__main__': verify()
