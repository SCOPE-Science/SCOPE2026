"""Finite consistency checks for the Gaussian map's positive-detuning escape clock.

Use the Python 3 standard library only. Tests are not substitutes for the proof.
"""
import math


def outer_root(a, eps):
    assert 0 < 2*eps < a*math.exp(-2)
    lo, hi = 2.0, 4.0
    while a*(hi-1)*math.exp(-hi) > 2*eps:
        hi *= 2
    for _ in range(90):
        mid = (lo+hi)/2
        if a*(mid-1)*math.exp(-mid) > 2*eps:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def forward_u(u,a,eps):
    h = 2*eps+a*(u-1)*math.exp(-u)
    return u*(1+h)**2


def passage(a, eps, r0, targets):
    U=outer_root(a,eps)
    goals=[U+t for t in targets]
    u=r0*r0
    n=0
    outcomes=[]
    for goal in goals:
        while u<goal:
            u=forward_u(u,a,eps)
            n+=1
            assert n<5_000_000
        outcomes.append((n,4*eps*U*n))
    return U,outcomes


def main():
    for a in (0.8,1.0,2.0):
        for eps in (1e-3,1e-5,1e-7):
            U=outer_root(a,eps)
            assert abs(a*(U-1)*math.exp(-U)/(2*eps)-1)<1e-12
            for w in (-2.,-0.5,0.,1.,2.):
                u=U+w
                if u<=2:continue
                h=2*eps+a*(u-1)*math.exp(-u)
                direct=(forward_u(u,a,eps)-u)/(4*eps*U)
                symbolic=(u/U)*(1+(u-1)/(U-1)*math.exp(-w))+(u/U)*h*h/(4*eps)
                assert abs(direct-symbolic)<3e-8
            for x in (2.1, -2.1, 3.0):
                y=-x;b=.5+eps
                fa=lambda z:a*z*(1-z*z)*math.exp(-z*z)
                xp=fa(x)+b*(y-x)
                yp=fa(y)+b*(x-y)
                assert abs(xp+yp)<1e-13
                assert math.isclose(xp*xp,forward_u(x*x,a,eps),rel_tol=1e-12)
    # At the smallest epsilon the five fixed offsets reproduce the predicted
    # softplus times with the expected slow finite-U corrections.
    U,outcomes=passage(1.,1e-7,2.,[-2.,-1.,0.,1.,2.])
    for t,(n,scaled) in zip((-2.,-1.,0.,1.,2.),outcomes):
        expected=math.log1p(math.exp(t))
        assert abs(scaled-expected)<0.15,(t,scaled,expected)
    # A direct trend test checks errors get smaller as the detuning shrinks.
    for t in (-1.,0.,1.):
        err=[]
        for eps in (1e-4,1e-5,1e-6,1e-7):
            _,vals=passage(1.,eps,2.,[t])
            err.append(abs(vals[0][1]-math.log1p(math.exp(t))))
        assert all(err[i+1]<err[i] for i in range(len(err)-1)),(t,err)
    print('PASS: exact reductions, root checks, five-offset near-critical profile and monotone convergence diagnostics')


if __name__=='__main__':
    main()
