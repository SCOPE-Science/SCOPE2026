#!/usr/bin/env python3
"""Independent numerical diagnostics for a binned exponentiated half-logistic model.
All theoretical claims require the analytic proof; these computations are not infinite certificates.
Requires only the Python 3 standard library.
"""
from decimal import Decimal, localcontext


def mass(j, alpha, theta):
    assert j >= 0 and alpha > 0 and theta > 0
    def Fpow(x):
        if x == 0:
            return Decimal(0)
        qx = (-theta*x).exp()
        a = (1-qx)/(1+qx)
        return (alpha*a.ln()).exp()
    return Fpow(j+1)-Fpow(j)


def g(k, alpha, theta):
    return mass(k+1,alpha,theta)-mass(k,alpha,theta)


def alpha_root(k, theta):
    lo,hi=Decimal(1),Decimal(2)
    while g(k,hi,theta)<=0:
        hi*=2
    for _ in range(240):
        mid=(lo+hi)/2
        if g(k,mid,theta)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def limiting_c(theta):
    q=(-theta).exp()
    d=1+1/q
    # r in (0,1) solves r^d-2r+1=0; choose left root using bracket
    rlo=Decimal('1e-40')
    rhi=Decimal('0.999')
    # for q close to 1, the root can be closer to 1 than 0.999
    while rhi**d-2*rhi+1>=0:
        rhi=(rhi+1)/2
    for _ in range(240):
        rmid=(rlo+rhi)/2
        if rmid**d-2*rmid+1>0:rlo=rmid
        else:rhi=rmid
    r=(rlo+rhi)/2
    return -r.ln()/(2*q*(1-q))


def test():
    assertions=0
    with localcontext() as ctx:
        ctx.prec=95
        for theta in [Decimal('.25'),Decimal('.5'),Decimal('1'),Decimal('2')]:
            roots=[alpha_root(k,theta) for k in range(12)]
            for k,a in enumerate(roots):
                assert a>1; assertions+=1
                assert abs(g(k,a,theta)) < Decimal('1e-55'); assertions+=1
                if k>0:
                    assert a>roots[k-1];assertions+=1
                assert g(k,a*Decimal('.99999'),theta)<0;assertions+=1
                assert g(k,a*Decimal('1.00001'),theta)>0;assertions+=1
                for j in range(max(1,k-3), min(k+3,13)):
                    m0,m1,m2=[mass(u,a,theta) for u in (j-1,j,j+1)]
                    assert m1*m1>m0*m2;assertions+=1
            c=limiting_c(theta)
            q=(-theta).exp()
            # Limiting asymptotic with loose tolerance at k=11 for the slower q=.7788
            ratio=roots[-1]*q**11/c
            assert abs(ratio-1)<Decimal('.03');assertions+=1
            print('theta=',theta,'alpha0=',str(roots[0])[:22],
                  'alpha1=',str(roots[1])[:22], 'c=',str(c)[:22],
                  'ratio11=',str(ratio)[:18])
        print('PASSED', assertions,'finite numerical diagnostics')
if __name__=='__main__':test()
