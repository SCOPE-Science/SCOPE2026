"""Independent checks for the two-sunfleck activation--damage timing theorem.

Run: python check_sunfleck.py. Uses only the Python standard library and scipy.
The proof, not these finite checks, establishes the all-parameter theorem.
"""
import math
import random
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar


def coeff(a, b, c, d, ell):
    C = -math.expm1(-c * ell)/c
    D = -math.expm1(-(a+c)*ell)/(a+c)
    X = -math.expm1(-a*ell)
    Y = -math.expm1(-c*ell)
    P = D*X
    Q = (C-D)*Y
    R = D*X*Y
    return C, D, X, Y, P, Q, R


def total(a, b, c, d, ell, gap):
    C,D,_,_,P,Q,R=coeff(a,b,c,d,ell)
    return 2*(C-D) + P*math.exp(-b*gap)-Q*math.exp(-d*gap)-R*math.exp(-(b+d)*gap)


def optimizer(a,b,c,d,ell,cap=float('inf')):
    assert min(a,b,c,d,ell)>0 and d>b and cap>=0
    C,D,X,Y,P,Q,R=coeff(a,b,c,d,ell)
    B0=-b*P+d*Q+(b+d)*R
    if B0 <= 0 or cap==0: return 0.0
    def B(g):
        return -b*P+d*Q*math.exp(-(d-b)*g)+(b+d)*R*math.exp(-d*g)
    hi=1.0
    while B(hi)>0: hi*=2
    return min(brentq(B,0,hi,xtol=1e-13),cap)


def direct_integral(a,b,c,d,ell,g):
    # Direct numerical integration of exact state trajectories on each light interval.
    def integrand(t, x0, y0):
        x=1-(1-x0)*math.exp(-a*t)
        y=1-(1-y0)*math.exp(-c*t)
        return x*(1-y)
    X=-math.expm1(-a*ell)
    Y=-math.expm1(-c*ell)
    return quad(lambda t:integrand(t,0,0),0,ell,epsabs=2e-13)[0]+quad(
        lambda t:integrand(t,X*math.exp(-b*g),Y*math.exp(-d*g)),0,ell,epsabs=2e-13)[0]


def exercise():
    rng=random.Random(103417)
    assertions=0
    # Analytic objective reconstructed from two independent light-pulse trajectories.
    for _ in range(120):
        a=10**rng.uniform(-1,1)
        b=10**rng.uniform(-1,.5)
        c=10**rng.uniform(-1,1)
        d=b*10**rng.uniform(.03,1)
        ell=10**rng.uniform(-2,.8)
        G=rng.uniform(.1,5)
        for g in (0,G/3,G,3*G):
            f=total(a,b,c,d,ell,g)
            direct=direct_integral(a,b,c,d,ell,g)
            assert math.isclose(f,direct,rel_tol=3e-11,abs_tol=1e-12),(f,direct,a,b,c,d,ell,g)
            assertions+=1
        gg=optimizer(a,b,c,d,ell,cap=G)
        for i in range(81):
            v=G*i/80
            assert total(a,b,c,d,ell,gg)>=total(a,b,c,d,ell,v)-1e-11
            assertions+=1
        # Unconstrained maximum also dominates a long window.
        h=optimizer(a,b,c,d,ell)
        assert total(a,b,c,d,ell,h)>=total(a,b,c,d,ell,0)-1e-12
        assertions+=1
        for k in range(11):
            v=k*(h+10)/10
            assert total(a,b,c,d,ell,h)>=total(a,b,c,d,ell,v)-1e-11
            assertions+=1
    # Exact special-case threshold and asymptotic log 3.
    ell_c=-math.log((math.sqrt(57)-3)/6)
    assert abs(ell_c-0.27666862477983234)<1e-13
    assertions+=1
    previous=0.0
    for i in range(1,201):
        ell=ell_c+i*.075
        g=optimizer(1,1,1,2,ell)
        assert g>previous
        assert g<math.log(3)
        previous=g
        assertions+=2
    for ell in (.001,.03,.1,.2,ell_c*.999999):
        assert optimizer(1,1,1,2,ell)==0
        assertions+=1
    assert abs(optimizer(1,1,1,2,24)-math.log(3))<3e-10
    assertions+=1
    gap=optimizer(1,1,1,2,1.0)
    gain=total(1,1,1,2,1,gap)-total(1,1,1,2,1,0)
    ratio=total(1,1,1,2,1,gap)/total(1,1,1,2,1,0)-1
    assert abs(gap-.6495460359695122)<1e-12
    assert abs(gain-.10942585787499198)<1e-12
    assert abs(ratio-.29272140461370633)<1e-12
    assertions+=3
    print('PASS',assertions,'deterministic numerical assertions')
    print('critical length',format(ell_c,'.15f'))
    print('example optimal gap',format(gap,'.15f'),'relative improvement',format(ratio,'.15f'))
    print('limiting gap',format(math.log(3),'.15f'))

if __name__=='__main__': exercise()
