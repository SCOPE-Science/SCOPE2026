"""Deterministic checks for the Euclidean circular-sector distance-tail theorem.
No external modules are required. Finite quadratures check, but do not prove, the limits.
"""
from math import acos, cos, log, pi, sin, sqrt, tan, isclose

def theory_tip(theta):
    return -8.0*log(cos(theta))/(3.0*theta**2)

def theory_rim(theta):
    return 4.0/(3.0*theta**2*sin(theta)**2)

def diameter(theta):
    return max(1.0,2*sin(theta/2.0))

def exact_angular_survival(theta,q,r,s):
    if q <= abs(r-s):
        return 1.0
    if q >= r+s:
        return 0.0
    h=(r*r+s*s-q*q)/(2.0*r*s)
    a=acos(max(-1.0,min(1.0,h)))
    return max(0.0,1.0-a/theta)**2

def localized_probability(theta,epsilon,kind,n=620):
    q=diameter(theta)-epsilon
    if kind=='tip':
        # One small-radius and one near-rim point; count the two ordered cases.
        # Applicable only in the narrow regime or at the transition.
        ar=min(1., 3.0*epsilon/cos(theta))
        bs=min(1., 2.4*epsilon)
        factor=2.0
        def radius_a(i):return ar*(i+.5)/n
        def radius_b(j):return 1.0-bs*(j+.5)/n
    else:
        ar=min(1., 2.5*epsilon/sin(theta/2.0))
        bs=ar
        factor=1.0
        def radius_a(i):return 1.0-ar*(i+.5)/n
        def radius_b(j):return 1.0-bs*(j+.5)/n
    total=0.0
    for i in range(n):
        r=radius_a(i)
        for j in range(n):
            s=radius_b(j)
            total+=4*r*s*exact_angular_survival(theta,q,r,s)
    return factor*total*ar*bs/(n*n)

def run():
    checks=0
    for th in (.4,.8,pi/3):
        target=theory_tip(th)
        for eps in (.03,.015):
            measured=localized_probability(th,eps,'tip')/eps**3
            assert abs(measured/target-1)<.035, (th,eps,measured,target)
            checks+=1
    for th in (1.4,2.0,2.6):
        target=theory_rim(th)
        for eps in (.02,.008):
            measured=localized_probability(th,eps,'rim')/eps**4
            assert abs(measured/target-1)<.09, (th,eps,measured,target)
            checks+=1
    # Exact angular-survival disintegration, evaluated at some boundary cases.
    assert exact_angular_survival(1.0,.2,.9,.6) == 1.0; checks+=1
    assert exact_angular_survival(1.0,1.7,.9,.6) == 0.0; checks+=1
    assert abs(exact_angular_survival(2.0,sqrt(2),1.,1.)-(1-pi/4)**2)<1e-13; checks+=1
    # Strictly increasing narrow coefficient and single wide minimum.
    for j in range(1,65):
        t1=(pi/3)*j/66
        t2=(pi/3)*(j+1)/66
        assert theory_tip(t2)>theory_tip(t1);checks+=1
    lo=2.028757838110434
    assert abs(tan(lo)+lo)<1e-12;checks+=1
    for t in (pi/3+0.02,1.6,1.9,2.2,2.7,3.05):
        assert theory_rim(t)>=theory_rim(lo)-1e-12;checks+=1
    assert isclose(theory_tip(pi/3),24*log(2)/pi**2,rel_tol=1e-12);checks+=1
    assert isclose(theory_rim(pi/3),16/pi**2,rel_tol=1e-12);checks+=1
    print('SECTOR_CHECKS_OK',checks)

if __name__=='__main__':run()
