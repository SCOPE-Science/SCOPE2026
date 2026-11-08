"""Exact coefficient and numerical Gram checks for cyclic cubic-phase Gabor ambiguity."""
import cmath
import math
from collections import Counter
import numpy as np


def predicted(n, a, b):
    k = n.bit_length() - 1
    if a == 0:
        return n if b == 0 else 0.0
    t = (a & -a).bit_length() - 1
    B = (3*a*a - b) % n
    if t == k-1:
        return float(n) if B % n == n//2 else 0.0
    if B % (2**(t+1)):
        return 0.0
    return 2**((k+t+1)/2)


def exact_zero(n, a, b):
    exponents = Counter((3*a*x*x + (3*a*a-b)*x + a*a*a) % n for x in range(n))
    return all(exponents[j] == exponents[j+n//2] for j in range(n//2))


def run():
    for k in range(1,8):
        n=2**k
        support=Counter()
        for a in range(n):
            for b in range(n):
                mag=predicted(n,a,b)
                assert exact_zero(n,a,b) == (mag==0), (k,a,b,mag)
                if mag: support[round(mag*mag,8)]+=1
        target=Counter({float(n*n):2})
        for t in range(k-1):
            target[float(2**(k+t+1))] += 4**(k-t-1)
        assert support==target,(n,support,target)
        assert sum(support.values())==(n*n+2)//3
        print('EXACT_ZERO_AND_LEVELS',n,dict(sorted(support.items())))
        if n<=32:
            for a in range(n):
                for b in range(n):
                    z=sum(cmath.exp(2j*math.pi*((x+a)**3-x**3-b*x)/n) for x in range(n))
                    assert abs(abs(z)-predicted(n,a,b))<1e-7,(n,a,b,z)
            print('COMPLEX_AMBIGUITY_PASS',n)
        if n<=8:
            g=np.array([cmath.exp(2j*math.pi*x**3/n) for x in range(n)])
            Ps=[]
            for a in range(n):
                for b in range(n):
                    h=np.array([cmath.exp(2j*math.pi*b*x/n)*g[(x+a)%n] for x in range(n)])
                    Ps.append(np.outer(h,np.conj(h)).ravel())
            gram=np.array(Ps)@np.array(Ps).conj().T
            vals=np.linalg.eigvalsh(gram)
            expected=sorted([0.0]*(n*n-sum(support.values()))+[n*v for v,c in support.items() for _ in range(c)])
            assert max(abs(x-y) for x,y in zip(vals,expected))<1e-7,(n,vals,expected)
            print('PROJECTOR_GRAM_SPECTRUM_PASS',n)
    print('DYADIC_CUBIC_GABOR_CERTIFICATE_PASS')
if __name__=='__main__':run()
