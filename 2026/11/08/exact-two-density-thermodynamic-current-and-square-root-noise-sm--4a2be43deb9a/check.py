"""Independent finite-coefficient and limiting-law checks (Python 3 stdlib only).

The mathematical proof, not these finite tests, establishes the infinite limit.
"""
from fractions import Fraction as Fr
from math import comb, sqrt


def original(H, B, L, a):
    C, A, F = L-H, L-H-B, H-2*B
    z, n = Fr(0), Fr(0)
    for k2 in range(A+1):
        R = F-k2
        if R < 0:
            continue
        for k1 in range(B+1):
            if k1 == 0:
                mult = comb(A,k2) if R == 0 else 0
            elif k1 <= R:
                mult = comb(A,k2)*comb(B,k1)*comb(R-1,k1-1)
            else:
                mult = 0
            if mult:
                w = mult * a**k2 / (1-a)**(k1+k2)
                z += w
                n += (a*k1+k2)*w
    return z,n


def coeff(n, C, B, v):
    if n < 0:
        return Fr(0)
    return sum(comb(C,j)*v**j*comb(B+n-j-1,n-j)
               for j in range(min(C,n)+1))


def bulk(rho,beta,alpha):
    c = 1-rho
    f = rho-2*beta
    K = f+c*alpha+beta*(1-alpha)
    d = K*K-4*c*f*alpha
    t = 2*f*alpha/(K+sqrt(d))
    return rho-c*t


def main():
    checks=0
    for L in range(5,20):
        for H in range(1,L):
            for B in range(1,L):
                C,A,F = L-H,L-H-B,H-2*B
                if min(A,F) < 1:
                    continue
                for a in (Fr(1,4),Fr(1,2),Fr(2,3),Fr(3,4)):
                    v=a/(1-a)
                    z,n=original(H,B,L,a)
                    z2=coeff(F,C,B,v)
                    n2=C*v*coeff(F-1,C-1,B,v)
                    assert z==z2 and n==n2, (L,H,B,a)
                    assert 0 < n < H*z
                    checks+=2
    # Exact deterministic-limit and strict bulk monotonicity, across feasible interiors.
    for beta in (.02,.08,.13,.20):
        for rho in (.44,.53,.67,.75):
            if not (2*beta < rho < 1-beta):
                continue
            v=[bulk(rho,beta,a) for a in (.03,.25,.5,.8,.97,.9999)]
            assert all(v[i] > v[i+1] for i in range(len(v)-1))
            assert all(q>max(2*rho-1,2*beta) for q in v)
            assert abs(v[-1]-max(2*rho-1,2*beta)) < .02
            checks+=3
    # Exact critical-line expansion as epsilon -> 0: coefficient sqrt(c beta).
    beta=0.1
    rho=(1+2*beta)/2
    c=1-rho
    Q0=max(2*rho-1,2*beta)
    for eps in (1e-4,1e-6,1e-8):
        val=(bulk(rho,beta,1-eps)-Q0)/sqrt(eps)
        assert abs(val-sqrt(c*beta)) < .004
        checks+=1
    # Double-scaling boundary-layer profile along feasible sequences.
    beta0=.09
    c0=(1-2*beta0)/2
    for lam in (-.4,-.15,0,.2,.5):
        eps=1e-8
        rho=(1+2*beta0+lam*sqrt(eps))/2
        c=1-rho
        beta=beta0
        q0=max(2*rho-1,2*beta)
        limit=(sqrt(lam**2+4*c0*beta0)-abs(lam))/2
        val=(bulk(rho,beta,1-eps)-q0)/sqrt(eps)
        assert abs(val-limit)<.001,(lam,val,limit)
        checks+=1
    print('PASS:',checks,'finite exact coefficient, strict bulk ordering, and critical-scaling checks')


if __name__=='__main__':
    main()
