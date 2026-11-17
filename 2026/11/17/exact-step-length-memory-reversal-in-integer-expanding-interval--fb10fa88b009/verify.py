"""Exact-rational checks for the expansion-map step-length covariance theorem.

Standard library only. Finite checks corroborate, but do not prove,
identities for all integer slopes or asymptotic limit laws.
"""
from fractions import Fraction as F

def step(x, b):
    return abs((b*x) % 1 - x)

def covariance_direct(b, lag):
    # All possible breakpoints of both piecewise affine factors.
    knots = {F(0), F(1)}
    knots.update(F(j,b) for j in range(b+1))
    knots.update(F(j,b-1) for j in range(b))
    seeds = tuple(knots)
    for r in range(b**lag):
        knots.update((r+c)/b**lag for c in seeds)
    knots = sorted(knots)
    integral = F(0)
    for a, z in zip(knots, knots[1:]):
        length = z-a
        x = a+length/3
        y = a+2*length/3
        f1, f2 = step(x,b), step(y,b)
        for _ in range(lag):
            x, y = (b*x)%1, (b*y)%1
        g1, g2 = step(x,b), step(y,b)
        # Integrate the product of two affine functions exactly.
        A, B = 2*f1-f2, 3*(f2-f1)
        C, D = 2*g1-g2, 3*(g2-g1)
        integral += length*(A*C+(A*D+B*C)/2+B*D/3)
    mean = F(2*b-1,6*b)
    return integral-mean**2

def predicted(b, lag):
    return F((b-4)*(b-2)*(b*b-b-1), 180*b**4*b**(2*(lag-1)))

def check_transfer_eigen(b, x):
    mu=F(2*b-1, 6*b)
    v=lambda t: sum((abs((b-1)*t-j) for j in range(b)), F(0))/b**2
    Pv=sum((v((x+j)/b) for j in range(b)), F(0))/b
    return Pv == mu + (v(x)-mu)/b**2

def main():
    eigen_cases=0
    for b in range(2,10):
        for k in range(1,13):
            assert check_transfer_eigen(b,F(k,13))
            eigen_cases+=1
    cases=0
    for b in range(2,8):
        for lag in (1,2,3):
            lhs = covariance_direct(b,lag)
            rhs = predicted(b,lag)
            assert lhs==rhs,(b,lag,lhs,rhs)
            cases+=1
    # Sign transition and the nonzero asymptotic-variance coefficient.
    for b in range(2,16):
        c1=predicted(b,1)
        assert (c1==0)==(b in (2,4))
        if b==3: assert c1<0
        if b>=5: assert c1>0
        v=F(2*b*b-2*b-1,36*b*b)
        diffusion=v+2*c1/(1-F(1,b*b))
        formula=F(12*b**4-24*b**3+11*b*b+6*b-11,180*b*b*(b*b-1))
        assert diffusion==formula and diffusion>0
    print(f'VERIFY_OK transfer_eigen_checks={eigen_cases} exact_piecewise_integrals={cases} covariance_lags=1..3 slopes=2..7 sign_and_variance_cases=14')
if __name__=='__main__': main()
