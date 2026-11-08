"""Checks for the three-opinion persuasion--polarization relaxation theorem.

Run: python verify.py
Only finitely many examples and symbolic identities are checked; the proof is analytic.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log


def source_rhs(a,b,c,alpha):
    beta=1-alpha
    return (
        alpha*a*b + beta*c*b - alpha*a*(1-a),
        a*alpha*(b+c)+c*alpha*(a+b)-b*(1-b),
        alpha*c*b+beta*a*b-alpha*c*(1-c)
    )


def compact_rhs(a,b,c,alpha):
    beta=1-alpha
    return (c*(beta*b-alpha*a),2*alpha*a*c-beta*b*(a+c),a*(beta*b-alpha*c))


def centered_rhs(a,b,c,alpha):
    beta=1-alpha
    kappa=2-alpha
    star=alpha/kappa
    x=b-star
    d=c-a
    dx=-beta*x+kappa*x*x/2-alpha*d*d/2
    dd=-beta*(star+x)*d
    return dx,dd

checked=0
for den in (5,7,11,17):
    for nalpha in range(1,den):
        alpha=F(nalpha,den)
        for a_num in range(den+1):
            for b_num in range(den-a_num+1):
                a=F(a_num,den); b=F(b_num,den); c=1-a-b
                f=source_rhs(a,b,c,alpha)
                g=compact_rhs(a,b,c,alpha)
                assert f==g
                assert sum(f)==0
                dx,dd=centered_rhs(a,b,c,alpha)
                assert dx==f[1]
                assert dd==f[2]-f[0]
                beta=1-alpha
                star_a=beta/(2-alpha)
                star_b=alpha/(2-alpha)
                assert compact_rhs(star_a,star_b,star_a,alpha)==(0,0,0)
                checked += 1

# Cross-over algebraic identities, including the exact borderline.
for alpha in (F(1,5),F(1,2),F(2,3),F(7,8),F(9,10)):
    beta=1-alpha
    rate=alpha*beta/(2-alpha)
    assert beta-2*rate==beta*(2-3*alpha)/(2-alpha)
    assert (2*rate<beta)==(alpha<F(2,3))
    assert (2*rate==beta)==(alpha==F(2,3))

# Independent floating-point trajectory evidence: positivity and convergence.
from scipy.integrate import solve_ivp
for alpha in (0.3,0.5,2/3,0.85):
    beta=1-alpha
    st=alpha/(2-alpha)
    la=alpha*beta/(2-alpha)
    y0=(0.52,0.17,0.31)
    def func(t,y): return tuple(map(float,compact_rhs(*y,alpha)))
    sol=solve_ivp(func,(0,75),y0,method='DOP853',rtol=1e-12,atol=1e-14,dense_output=True)
    assert sol.success
    assert all(min(sol.sol(t))>-1e-9 for t in (0,3,10,25,50,75))
    for t in (30,55,75):
        a,b,c=sol.sol(t)
        assert abs(a+c+b-1)<1e-10
        assert abs(b-st)<0.1
        assert abs((c-a))<0.1
    # Direct check of Lyapunov identity, using the exact ODE at an interior point.
    a,b,c=y0
    sa=beta/(2-alpha); sb=st
    adot,bdot,cdot=func(0,y0)
    dotH=adot*log(a/sa)+bdot*log(b/sb)+cdot*log(c/sa)
    diss=-c*(alpha*a-beta*b)*log(alpha*a/(beta*b))-a*(alpha*c-beta*b)*log(alpha*c/(beta*b))
    assert abs(dotH-diss)<1e-12
    assert dotH<0
print(f'VERIFY_OK exact_rational_states={checked} analytical_boundaries=5 numeric_trajectories=4')
