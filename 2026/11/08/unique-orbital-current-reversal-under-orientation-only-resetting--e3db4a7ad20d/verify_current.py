"""Independent finite diagnostics for orientation-only reset chirality reversal.
Only the standard Python library is required. Run: python verify_current.py
"""
import cmath
import math


def polynomial(a, t, q):
    return ((2*a-3)*q**4 + 2*(a*a-a-1)*q**3
            + (a*a-2*a+(1-6*a)*t*t)*q*q
            + (1-8*a-a*a)*t*t*q
            -2*(a+1)*(a+t*t)*t*t)


def rational_current(a, t, q):
    p=polynomial(a,t,q)
    return (-2*t**3*p /
            ((a+1)*(q*q+t*t)*(q*q+4*t*t)*
             ((a+q)**2+t*t)*((1+q)**2+t*t)))


def generator_current(a,t,q):
    # Units: k_y = v = 1. Stationary generator balance (not polynomial formula).
    m1=q/complex(q,-t)
    m2=q/complex(q,-2*t)
    ex=m1.real/a
    ey=m1.imag
    ax=((1+m2)/2+q*ex)/complex(a+q,-t)
    ay=((m2-1)/(2j)+q*ey)/complex(1+q,-t)
    return 2*(a*ax.imag-ay.real)/(a+1)


def quadrature_current(a,t,q,n=28000):
    # Independent age-at-observation representation: A~Exp(q), θ=tA.
    # Position is continuous at reset and the pre-reset mean equals its
    # stationary mean by Poisson-arrivals-see-time-averages (PASTA).
    m=q/complex(q,-t)
    ex=m.real/a
    ey=m.imag
    upper=38/q
    h=upper/n
    z1=z2=0.0
    for j in range(n+1):
        age=j*h
        co=math.cos(t*age); si=math.sin(t*age)
        cx=(a*co+t*si-a*math.exp(-a*age))/(a*a+t*t)
        cy=(si-t*co+t*math.exp(-age))/(1+t*t)
        wt=(1 if j==0 or j==n else (4 if j%2 else 2))*q*math.exp(-q*age)
        z1+=wt*(ex*math.exp(-a*age)+cx)*si
        z2+=wt*(ey*math.exp(-age)+cy)*co
    return 2*(a*z1-z2)*h/(3*(a+1))


def unique_positive_root(a,t):
    assert a>1.5 and t>0
    lo=0.0; hi=1.0
    while polynomial(a,t,hi)<=0:hi*=2
    for _ in range(110):
        m=(lo+hi)/2
        if polynomial(a,t,m)<0:lo=m
        else:hi=m
    return (lo+hi)/2


def main():
    count=0
    cases=[(2,1,.2),(2,1,1),(2,1,3),(2,1,4),(2,1,6),
           (1.51,.3,.25),(1.51,2,2),(1.7,.5,1.3),(3,2,3),
           (5,.7,.8),(2.6,4,1.2),(.8,1,3)]
    for a,t,q in cases:
        z=rational_current(a,t,q)
        w=generator_current(a,t,q)
        assert math.isclose(z,w,rel_tol=3e-11,abs_tol=2e-13),(a,t,q,z,w)
        count+=1
        zz=quadrature_current(a,t,q)
        assert math.isclose(z,zz,rel_tol=2e-6,abs_tol=2e-8),(a,t,q,z,zz)
        count+=1
    for a in [1.50001,1.51,1.6,1.6180339888,1.9,2,3,10,50]:
        for t in [.1,.5,1,4,10]:
            root=unique_positive_root(a,t)
            assert polynomial(a,t,root*.9)<0
            assert polynomial(a,t,root*1.1)>0
            assert rational_current(a,t,root*.9)>0
            assert rational_current(a,t,root*1.1)<0
            count+=4
    for t in [.1,1,10]:
        for q in [.01,.1,1,10,100]:
            assert polynomial(1.5,t,q)<0
            assert rational_current(1.5,t,q)>0
            count+=2
    root=unique_positive_root(2,1)
    assert abs(root-3.381098747)<2e-8
    assert abs(rational_current(2,1,1)-.06)<1e-12
    assert rational_current(2,1,4)<0
    count+=3
    print('PASS:',count,'deterministic assertions; sample root',format(root,'.12f'))

if __name__=='__main__':main()
