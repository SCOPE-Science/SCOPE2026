"""Finite numerical diagnostics for two-scale zeros of harmonic trinomials.

The infinite theorem is established analytically; these tests do not certify
an exhaustive root count or an asymptotic limit.
"""
import cmath
import math


def solve(A_kind, n, k, eps, seed):
    z = seed
    for _ in range(80):
        if A_kind == 'inner':
            f = eps*z**n + z.conjugate()**k - 1
            A = eps*n*z**(n-1)
            B = k*z.conjugate()**(k-1)
        else:
            f = z**n + z.conjugate()**k - eps
            A = n*z**(n-1)
            B = k*z.conjugate()**(k-1)
        jac = abs(A)**2-abs(B)**2
        if abs(jac) < 1e-13:
            raise ArithmeticError('near-singular Newton Jacobian')
        delta = (-A.conjugate()*f+B*f.conjugate())/jac
        z += delta
        if abs(delta) < 1e-14:
            break
    if A_kind == 'inner':
        residual = abs(eps*z**n+z.conjugate()**k-1)
    else:
        residual = abs(z**n+z.conjugate()**k-eps)
    assert residual < 4e-10, (A_kind,n,k,eps,residual)
    return z


def check(n, k, c):
    assert math.gcd(n,k)==1 and n > k >=1
    ein = c**(-n/k)
    eout = c**(-n/(n-k))
    inner=[];outer=[]
    for j in range(k):
        omega=cmath.exp(2j*math.pi*j/k)
        pred=omega-ein*omega**(1-n)/k
        z=solve('inner',n,k,ein,pred)
        inner.append(z)
        assert abs(z-pred)<(15+n+k)*ein**2+2e-11
    for j in range(n+k):
        zeta=cmath.exp(1j*(2*j+1)*math.pi/(n+k))
        phase=zeta**(-n)
        h=eout*(phase.real/(n-k)+1j*phase.imag/(n+k))
        pred=zeta*(1+h)
        z=solve('outer',n,k,eout,pred)
        outer.append(z)
        assert abs(z-pred)<(15+n+k)*eout**2+2e-11
    for roots in [inner,outer]:
        assert len(roots)==len(set((round(z.real,7),round(z.imag,7)) for z in roots))
    # Positive-root lower triangle bound is attained exactly, and uniquely.
    rho=solve('inner',n,k,ein,1-ein/k)
    assert abs(rho.imag)<1e-10
    assert abs(rho-min(inner,key=abs))<1e-8
    # The outer extremal coefficient has an arithmetic parity split.
    best=max(outer,key=abs)
    sigma=1 if n%2==0 else math.cos(math.pi/(n+k))
    if eout > 1e-9:
        assert abs((abs(best)-1)/eout-sigma/(n-k))<(12+n+k)*eout+1e-6
    if n%2==0:
        # The opposite real axis exactly reaches the triangle bound.
        assert abs(best.imag)<1e-7 and best.real<0
    else:
        # Exactly two conjugate outer zeros maximize the modulus.
        tied=[z for z in outer if abs(abs(z)-abs(best))<max(1e-12,eout*1e-4)]
        assert len(tied)==2 and abs(tied[0]-tied[1].conjugate())<2e-8
    return len(inner)+len(outer)


def main():
    tests=[(3,1),(3,2),(4,1),(5,2),(5,3),(6,1),(6,5),
           (7,2),(7,3),(7,4),(8,3),(9,4),(10,3)]
    cases=0
    for n,k in tests:
        for c in [20.0,80.0,200.0]:
            result=check(n,k,c)
            assert result==n+2*k
            cases+=1
    print('PASS:',cases,'finite root-configuration diagnostic cases')

if __name__=='__main__':
    main()
