"""Exact rational checks for the gauge-regularized weighted proximal objective bound.
No external libraries. The universal proof is in RESULT.md; this is a finite test.
"""
from fractions import Fraction as F
from itertools import product

def soft(t, a):
    return max(t-a, F(0)) if t >= 0 else min(t+a, F(0))

def f(x, b, lam, r):
    return sum(((xi-bi)**2 + r*xi**2)/2 + li*abs(xi)
               for xi, bi, li in zip(x, b, lam))

def run():
    checks = 0
    for k, r, c in product((F(1,4),F(1,2),F(3,4)),
                            (F(1,10),F(1),F(4)),
                            (F(1,3),F(1),F(3))):
        lam = (F(1),c)
        vals = (F(-3)/k, -c/k, -c, F(0), c/2, c, c/k,
                F(3)/k)
        for b in product(vals,repeat=2):
            u = tuple(soft(bi,li)/(1+r) for bi,li in zip(b,lam))
            v = tuple(soft(k*bi,li)/(k+r) for bi,li in zip(b,lam))
            p = tuple(max(-li,min(li,k*bi)) for bi,li in zip(b,lam))
            q = tuple(k*bi-pi for bi,pi in zip(b,p))
            P = sum(z*z for z in p)
            Q = sum(z*z for z in q)
            T = sum(pi*qi for pi,qi in zip(p,q))
            A,B,D = 1+r,k+r,r+k*(2-k)
            low = (D*P+2*B*T+r*Q)/(2*A*k*k)
            dualopt = sum(bi*bi for bi in b)/2 - sum((bi-max(-li,min(li,bi)))**2
                    for bi,li in zip(b,lam))/(2*A)
            fv, fu = f(v,b,lam,r),f(u,b,lam,r)
            model = P/(2*k*k)+(r+k*k)*T/(k*k*B)+r*(r+k*k)*Q/(2*k*k*B*B)
            gap = (1-k)**2*(B*T+r*Q/2)/(D*B*B)
            assert T >= 0
            assert fv == model
            assert fu == dualopt and low <= fu
            assert A*low/D-fv == gap
            assert fv <= A*fu/D
            # The worst case has all nonzero components at the weighted threshold.
            if b == (lam[0]/k, F(0)):
                assert fv == A*fu/D
            checks += 6
    print(f'PASS: {checks} exact rational assertions over {3*3*3*8*8} two-coordinate parameter cases')

if __name__ == '__main__':
    run()
