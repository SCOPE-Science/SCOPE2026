"""Independent algebraic and finite-sample checks for the lossy source--sink result.

Run: python CHECK.py
The exact theorem relies on the analytic proof in RESULT.md; finite checks are not its proof.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt, isclose


def eval_state(a,b,v,h,q,r):
    c=b+v*(1-h*q)
    w=b+v
    X=(a*h-c*r)/(h+r*r)
    Y=r*X
    u=(r*(w+r*X))/h
    T=X+Y
    return c,w,X,Y,u,T


def deriv_num(a,c,h,r):
    d=a*h-c
    return h*d-2*h*(a+c)*r-d*r*r


def det_mut(a,b,v,h,q,X,Y,u,mut):
    return (a-X-mut)*(-b-v-Y)-v*q*h*mut


def check():
    rng=Random(9215)
    checks=0
    cases=[(F(4),F(1,2),F(1),F(3,4),F(3,4)),
           (F(5,4),F(1,2),F(1),F(3,4),F(3,4)),
           (F(1),F(1),F(1),F(3,4),F(3,4))]
    for _ in range(200):
        a=F(rng.randint(1,30),rng.randint(1,8))
        b=F(rng.randint(1,20),rng.randint(1,8))
        v=F(rng.randint(1,20),rng.randint(1,8))
        h=F(rng.randint(1,9),10)
        q=F(rng.randint(1,9),10)
        cases.append((a,b,v,h,q))
    for a,b,v,h,q in cases:
        c=b+v*(1-h*q)
        w=b+v
        rc=a*h/c
        uc=a*w/c
        assert w>c>0
        checks+=1
        d=a*h-c
        for k in range(1,13):
            r=rc*F(k,13)
            c0,w0,X,Y,u,T=eval_state(a,b,v,h,q,r)
            assert c0==c and w0==w and 0<u<uc and X>0 and Y>0
            assert X*(a-X-u)+v*q*Y==0
            assert -Y*(b+Y)-v*Y+h*u*X==0
            checks+=4
            assert T-a==r*(d-(a+c)*r)/(h+r*r)
            checks+=1
            # Closed-form u' numerator and a strictly positive lower bound.
            unump=w*(h+r*r)**2+2*a*h*h*r-3*c*h*r*r-c*r**4
            assert unump>0
            assert unump > w*h*h+(2*w-c)*h*r*r+(w-c)*r**4
            checks+=2
            # derivative and sign of biomass validated by an exact finite difference.
            eps=rc*F(1,10**7)
            _,_,_,_,up,Tp=eval_state(a,b,v,h,q,r+eps)
            _,_,_,_,um,Tm=eval_state(a,b,v,h,q,r-eps)
            assert up>um
            num=deriv_num(a,c,h,r)
            if num!=0 and abs(float(num))>float(eps)*1000:
                assert (Tp>Tm)==(num>0)
                checks+=1
            for mut in [F(0),u/2,u,u+F(1,3),u+F(10)]:
                det=det_mut(a,b,v,h,q,X,Y,u,mut)
                assert det==(c+Y)*(mut-u)
                checks+=1
        # Biomass monotonicity and single peak through continuous r-grid.
        nlist=[deriv_num(a,c,h,rc*F(j,200)) for j in range(201)]
        if d<=0:
            assert all(z<=0 for z in nlist)
        else:
            assert nlist[0]>0 and nlist[-1]<0
            assert all(nlist[j+1]<nlist[j] for j in range(200))
            ropt=(h*d)/(sqrt(float(h*h*(a+c)**2+h*d*d))+float(h*(a+c)))
            assert 0<ropt<float(rc)
            assert isclose(float(deriv_num(a,c,h,F.from_float(ropt))),0,abs_tol=1e-8)
        checks+=4
        # Extremal bifurcation at u=uc and u=0.
        assert eval_state(a,b,v,h,q,F(0))[3:]==(F(0),F(0),a)
        assert eval_state(a,b,v,h,q,rc)[2:]==(F(0),F(0),uc,F(0))
        checks+=2
    # Rational cases on both sides and at the sharp threshold.
    a,b,v,h,q=cases[0]
    c=b+v*(1-h*q)
    assert c==F(15,16) and a*h-c==F(33,16)
    rstar=float((h*(a*h-c))/(sqrt(float(h*h*(a+c)**2+h*(a*h-c)**2))+float(h*(a+c))))
    _,_,X,Y,ustar,Tstar=eval_state(float(a),float(b),float(v),float(h),float(q),rstar)
    assert 0<ustar<float(a*(b+v)/c) and Tstar>float(a)
    checks+=3
    print(f'PASS {checks} exact-rational/analytic-identity and finite-grid checks')
    print(f'example r*={rstar:.15f}, u*={ustar:.15f}, T*={Tstar:.15f}')

if __name__=='__main__':
    check()
