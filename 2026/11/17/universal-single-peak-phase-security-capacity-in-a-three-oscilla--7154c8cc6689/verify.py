"""Reproducibility checks of phase-constrained three-node locking (not an infinite proof)."""
from math import sin, cos, asin, atan2, sqrt, pi, isclose

def phases(delta,b):
    phi=atan2(sin(delta),b+cos(delta))
    return phi,delta-phi

def power(delta,b):
    phi,psi=phases(delta,b)
    return sin(delta)+b*sin(phi)

def bstar(gamma,eta):
    return sin(eta)/sin(gamma-eta)

def boundary(b,gamma,eta):
    star=bstar(gamma,eta)
    if b<=star:
        return sin(gamma)*(1+b/sqrt(1+b*b+2*b*cos(gamma)))
    return sin(eta)+sin(eta+asin(sin(eta)/b))

cases=0
for gamma,eta in [(pi/3,pi/6),(.9,.2),(.55,.23), (1.35,.75), (1.2,.9)]:
    star=bstar(gamma,eta)
    assert 0<eta<gamma<pi/2 and star>0
    assert isclose(boundary(star,gamma,eta),sin(gamma)+sin(eta),rel_tol=1e-13)
    left=[boundary(star*i/10,gamma,eta) for i in range(1,11)]
    right=[boundary(star*i/10,gamma,eta) for i in range(10,81)]
    assert all(x<y for x,y in zip(left,left[1:]))
    assert all(x>y for x,y in zip(right,right[1:]))
    for b in [star/10,star/2,star,star*1.25,star*3,star*10]:
        dmax=gamma if b<=star else eta+asin(sin(eta)/b)
        phi,psi=phases(dmax,b)
        assert isclose(b*sin(phi),sin(psi),rel_tol=1e-12,abs_tol=1e-12)
        assert isclose(power(dmax,b),boundary(b,gamma,eta),rel_tol=1e-12,abs_tol=1e-12)
        assert dmax<=gamma+1e-13 and psi<=eta+1e-13
        for i in range(1,101):
            delta=dmax*i/101
            ph,ps=phases(delta,b)
            assert 0<ph<delta and 0<ps<delta
            assert isclose(b*sin(ph),sin(ps),abs_tol=1e-12)
            assert power(delta,b)<boundary(b,gamma,eta)
            cases+=1
    P=(max(sin(gamma),2*sin(eta))+sin(gamma)+sin(eta))/2
    assert max(sin(gamma),2*sin(eta))<P<sin(gamma)+sin(eta)
    b=1e9
    assert boundary(b,gamma,eta)<P
    lo,hi=0,pi/2
    for i in range(75):
        mid=(lo+hi)/2
        if power(mid,b)<P: lo=mid
        else: hi=mid
    phi,psi=phases((lo+hi)/2,b)
    assert phi>0 and psi>0 and phi+psi<pi/2
    assert psi>eta  # safe cap fails while an unconstrained stable state exists
    cases+=1
assert isclose(boundary(1,pi/3,pi/6),(1+sqrt(3))/2)
print('VERIFY_OK exact_boundaries=5 monotone_branch_tests=5 phase_balance_cases=%d stable_beyond_security=5'%cases)
