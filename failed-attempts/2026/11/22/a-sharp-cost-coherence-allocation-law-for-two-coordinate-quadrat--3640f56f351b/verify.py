"""Finite exact-rational and numerical checks of a two-coordinate cost design.

Run with `python3 verify.py`; only the standard library is required.
These checks supplement, but cannot replace, the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose

checks = 0

def ck(test, description):
    global checks
    if not test:
        raise AssertionError(description)
    checks += 1

def det2(a, b, d):
    return a*d-b*b

# Rational unit-vector pairs (1,0),(rho,s) from Pythagorean triples.
for rn, sn, den in ((0,1,1),(3,4,5),(5,12,13),(8,15,17),(20,21,29),(99,20,101)):
    rho, ss = F(rn,den), F(sn,den)
    ck(rho*rho+ss*ss==1, 'unit direction')
    for ca, cb in ((1,1),(9,1),(1,16),(100,9),(10000,1),(4,25)):
        ra, rb = int(sqrt(ca)), int(sqrt(cb))
        ck(ra*ra==ca and rb*rb==cb, 'perfect square prices')
        a, b, root = F(ca), F(cb), F(ra*rb)
        D=a+b+2*rho*root
        g=(1-rho*rho)/D
        p=(root+rho*b)/(2*root+rho*(a+b))
        C=p*a+(1-p)*b
        q1,q2=p/C,(1-p)/C
        ck(0<p<1 and a*q1+b*q2==1, 'feasible positive optimum')
        ck(q1==(1+rho*F(rb,ra))/D, 'q1 explicit')
        ck(q2==(1+rho*F(ra,rb))/D, 'q2 explicit')
        # Unit vectors u=(1,0), v=(rho,ss); M(q)=q1 uu^T+q2 vv^T.
        m00=q1+q2*rho*rho
        m01=q2*rho*ss
        m11=q2*ss*ss
        ck(det2(m00-g,m01,m11-g)==0, 'one eigenvalue is g')
        ck(m00+m11-2*g>=0, 'other eigenvalue >=g')
        if rho==0:
            ck(p==F(1,2), 'orthogonal optimum')
        if a==b:
            ck(p==F(1,2), 'equal prices')
        if rho>0 and a!=b:
            ck((p<F(1,2))==(a>b), 'expensive coordinate less frequent')
        # Direct rational comparison using 2x2 PSD test: for every grid law,
        # M(p)/C-gI cannot be positive definite, and its lower eigenvalue <=g.
        for i in range(1,151):
            pp=F(i,151)
            cost=pp*a+(1-pp)*b
            u00=pp+(1-pp)*rho*rho
            u01=(1-pp)*rho*ss
            u11=(1-pp)*ss*ss
            A=u00/cost-g; B=u01/cost; E=u11/cost-g
            ck(not (A>0 and det2(A,B,E)>0), 'cannot beat global upper bound')

rho=F(3,5);a=F(9);b=F(1)
pp=(F(3)+rho*b)/(F(6)+rho*(a+b))
g=(1-rho*rho)/(a+b+2*rho*F(3))
ck(pp==F(3,10) and g==F(4,85), 'rational benchmark')
ck(g / ((1-rho)/(a+b))==F(20,17), 'sharp benchmark gain')

for rho in (0.0,.2,.6,.9,.99,.999):
    for ca,cb in ((1.,1.),(4.,1.),(1.,9.),(1e6,1.),(7.,13.)):
        k=sqrt(ca*cb)
        p=(k+rho*cb)/(2*k+rho*(ca+cb))
        optimal=(1-rho*rho)/(ca+cb+2*rho*k)
        def decrease(x):
            # stable formula via determinant and largest eigenvalue
            q=x/(x*ca+(1-x)*cb)
            r=(1-x)/(x*ca+(1-x)*cb)
            tr=q+r
            discr=sqrt(max(0.,(q-r)**2+4*q*r*rho*rho))
            return 2*q*r*(1-rho*rho)/(tr+discr)
        ck(isclose(decrease(p),optimal,rel_tol=1e-10,abs_tol=1e-15),'formula matches eigenvalue')
        for j in range(1,1000):
            x=j/1000
            ck(decrease(x)<=optimal+3e-14, 'dense grid no improvement')

# Gain approaches the nonattained sharp factor two.
rho=.999999;ca=1e12;cb=1.
gain=(1+rho)*(ca+cb)/(ca+cb+2*rho*sqrt(ca*cb))
ck(1.999<gain<2, 'sharp twofold limit')
print('VERIFY_OK',checks, 'rational and numerical checks')
