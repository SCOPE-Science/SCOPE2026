"""Exact rational checks for the two-patch selection--migration stability criterion.

Run: python3 verify.py. Only the Python standard library is required.
Finite tests corroborate the independently stated analytic proof; they are not substitutes for it.
"""
from fractions import Fraction as Q
from math import sqrt


def F(x, y, b, d, c):
    return (d*(y-x) + x*(1-x)*(b*(x-Q(1,2))+c),
            d*(x-y) + y*(1-y)*(b*(y-Q(1,2))-c))


def J(x, y, b, d, c):
    # Differentiate the polynomial vector field exactly.
    a = b*((1-2*x)*(x-Q(1,2))+x*(1-x))+c*(1-2*x)-d
    z = b*((1-2*y)*(y-Q(1,2))+y*(1-y))-c*(1-2*y)-d
    return ((a, d), (d, z))


def alpha(m, b, d):
    return b*(1-m*m)/4-4*d*m*m/(1-m*m)


def certify_witness():
    b, d, c = Q(3), Q(1), Q(23,12)
    x,y=Q(3,4),Q(1,4)
    m=Q(1,2)
    assert F(x,y,b,d,c)==(0,0)
    assert J(x,y,b,d,c)==((Q(-37,48)-d,d),(d,Q(-37,48)-d))
    assert alpha(m,b,d)==Q(-37,48)
    assert c>b/2 and c*c<b*b/4+b*d
    assert c*c+d*d<(b/2+d)**2
    for xx,yy in [(Q(0),Q(0)), (Q(1),Q(1))]:
        A=J(xx,yy,b,d,c)
        assert A[0][0]+A[1][1]==-b-2*d
        assert A[0][0]*A[1][1]-d*d==b*b/4+b*d-c*c>0
    assert F(Q(0),Q(1),b,d,c) == (d,-d)
    assert F(Q(1),Q(0),b,d,c) == (-d,d)
    print('exact witness and corner Jacobian: PASS')


def check_identity():
    # Dimensionless testing of exact closed-form parameter thresholds and
    # the stationary balance at the critical mixed-state Jacobian.
    for b,d in [(Q(1),Q(1)),(Q(1),Q(4)),(Q(3),Q(1)),
                (Q(9),Q(4)),(Q(20),Q(1)),(Q(1),Q(20))]:
        t=float(b/d)
        ms=(sqrt(4+t)-2)/sqrt(t)
        cm=0.5*sqrt(float(b*d))*(4-sqrt(4+t))
        cp=sqrt(float(b*b/4+b*d))
        assert 0<ms<1 and cm<cp
        assert abs(float(b)*(1-ms*ms)**2-16*float(d)*ms*ms)<1e-11
        assert abs(cm-(4*float(d)*ms/(1-ms*ms)-float(b)*ms/2))<1e-11
        lhs=cp*cp-cm*cm
        rhs=128*float(d*d)*ms**4/(1-ms*ms)**3
        assert abs(lhs-rhs)<1e-10*max(1,lhs)
        # Monomorphism and mixed-state strict sinks on the interior of wedge.
        lo=max(float(b)/2,cm)
        ci=(lo+cp)/2
        assert ci>float(b)/2 and ci<cp
        low=0.0; high=1.0
        for _ in range(70):
            mid=(low+high)/2
            h=(1-mid*mid)*(float(b)*mid+2*ci)-8*float(d)*mid
            if h>0: low=mid
            else: high=mid
        m=(low+high)/2
        assert alpha(m,float(b),float(d))<0
    print('transition algebra and representative wedge tests: PASS')

if __name__=='__main__':
    certify_witness()
    check_identity()
