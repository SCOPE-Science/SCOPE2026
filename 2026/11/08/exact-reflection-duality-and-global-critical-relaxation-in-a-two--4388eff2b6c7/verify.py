"""Reproduce exact coefficients and numerical dynamics of the symmetric cutoff map.
Standard-library only; numerical probes supplement, not replace, the all-parameter proof.
"""
import math
from fractions import Fraction


def phi(p, d):
    return ((1.0+d)/2.0)**p - ((1.0-d)/2.0)**p


def phi_inverse(p, y):
    assert -1.0 <= y <= 1.0
    if y == 0: return 0.0
    sg = 1.0 if y >= 0 else -1.0
    target = abs(y)
    lo, hi = 0.0, 1.0
    for _ in range(57):
        mid=(lo+hi)/2.0
        if phi(p,mid) < target: lo=mid
        else:hi=mid
    return sg*(lo+hi)/2.0


def step(p,gamma,d):
    return phi_inverse(p, (1.0-gamma)*d)


for p in range(3,13):
    c0 = Fraction(p,2**(p-1))
    c2 = Fraction(math.comb(p,3),2**(p-1))
    assert c2/c0 == Fraction((p-1)*(p-2),6)
    # Coefficient of d and d^3 in exact odd-power difference.
    assert sum(Fraction(math.comb(p,j),2**(p-1)) for j in range(1,p+1,2))==1
    assert 0 < c0 < 1
print('EXACT_OK binomial_degree_range=3..12 cubic_coefficient=10 boundary_identity=10')

count=0
for p in [3.0, 3.5, 4.0, 6.0]:
    for gamma in [0.05,0.4,0.8,1.0,1.2,1.7,1.95]:
        for d0 in [-0.9,-0.4,0.12,0.79]:
            a,b=d0,d0
            for n in range(1,21):
                a=step(p,gamma,a)
                b=step(p,2-gamma,b)
                assert abs(b-((-1)**n)*a)<1e-12,(p,gamma,d0,n,a,b)
                count+=1
print(f'DUALITY_OK signed_reflected_pairs={count}')

for p in [3,3.3,4,5]:
    c0=p/(2.0**(p-1))
    for gamma in [0, 1-c0/2, 1, 1+c0/2, 2]:
        d0=0.17
        for _ in range(100):d0=step(p,gamma,d0)
        # Gamma 0 and 2 converge to endpoints, otherwise center is stable for chosen middle values
        expected=1.0 if gamma in (0,2) else 0.0
        assert abs(abs(d0)-expected)<2e-6,(p,gamma,d0)
    for gamma in [1-c0-0.1*(1-c0), 1+c0+0.1*(1-c0)]:
        s=abs(1-gamma)
        lo,hi=0.,1.
        for _ in range(55):
            mid=(lo+hi)/2
            ratio=phi(p,mid)/mid if mid>0 else c0
            if ratio<s:lo=mid
            else:hi=mid
        dstar=(lo+hi)/2
        z=0.1
        for _ in range(1200):z=step(p,gamma,z)
        assert abs(abs(z)-dstar)<2e-8,(p,gamma,z,dstar)
        assert s < p/(2**p)*((1+dstar)**(p-1)+(1-dstar)**(p-1))
    print(f'PHASE_OK p={p} central_threshold={c0:.12f}')

for p in [3.0,3.5,5.0]:
    c0=p/(2.0**(p-1))
    limit=math.sqrt(3/((p-1)*(p-2)))
    for gamma in [1-c0,1+c0]:
        d=0.75
        n=16000
        for _ in range(n):d=step(p,gamma,d)
        observed=abs(d)*math.sqrt(n)
        assert abs(observed/limit-1)<0.04,(p,gamma,observed,limit)
        print(f'CRITICAL_OK p={p} gamma={gamma:.12f} observed={observed:.8f} predicted={limit:.8f}')
print('VERIFY_OK all_exact_and_numerical_checks_passed')
