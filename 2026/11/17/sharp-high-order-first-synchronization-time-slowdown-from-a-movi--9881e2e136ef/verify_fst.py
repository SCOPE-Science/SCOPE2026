#!/usr/bin/env python3
"""Independent finite numerical checks of the displayed scalar ODE theorem.
Only Python's standard library is required. Numerical samples are not proofs.
"""
from math import sqrt, log, isfinite


def simpson(f, a, b, tolerance=1e-23):
    def S(a, b, fa, fm, fb):
        return (b-a)*(fa+4*fm+fb)/6
    def recurse(a, b, fa, fm, fb, whole, eps, depth):
        m=(a+b)/2; l=(a+m)/2; r=(m+b)/2
        fl=f(l); fr=f(r)
        L=S(a,m,fa,fl,fm); R=S(m,b,fm,fr,fb)
        if depth==0 or abs(L+R-whole)<15*eps:
            return L+R+(L+R-whole)/15
        return recurse(a,m,fa,fl,fm,L,eps/2,depth-1)+recurse(m,b,fm,fr,fb,R,eps/2,depth-1)
    m=(a+b)/2; fa=f(a); fm=f(m); fb=f(b)
    return recurse(a,b,fa,fm,fb,S(a,b,fa,fm,fb),tolerance,22)


def check(P, Delta, H, delta, r0):
    s=1-2*Delta/P
    u0=r0*r0
    target=(sqrt(s)-delta)**2
    assert 0<H<P and 0<u0<target<s<1
    C=H*(1-s)*(1-delta/sqrt(s))/(P*P*target*(s-target))
    D=H*(1-target)/(P*P*(s-target)**2)
    def pair(t):
        return log(t*(s-u0)/(u0*(s-t)))/(P*s)
    def equilibrium(d):
        def g(u):
            return P*(s-u)+H*u**(d-1)*(1-u)
        lo,hi=s,1.0
        assert g(lo)>0 and g(hi)<0
        for _ in range(70):
            mid=(lo+hi)/2
            if g(mid)>0:lo=mid
            else:hi=mid
        return (lo+hi)/2
    def correction(d,t):
        def f(u):
            numerator=H*u**(d-2)*(1-u)
            denominator=P*(s-u)
            return numerator/(denominator*(denominator+H*u**(d-1)*(1-u)))
        return simpson(f,u0,t)
    moving, fixed =[],[]
    for d in (4, 6, 8, 12, 16, 20, 26, 32):
        ud=equilibrium(d)
        td=(sqrt(ud)-delta)**2
        moving_diff=(pair(td)-pair(target))-correction(d,td)
        fixed_diff=correction(d,target)
        assert ud>s and td>target
        assert fixed_diff>0 and isfinite(moving_diff)
        moving.append((d,moving_diff/(C*s**(d-1))))
        fixed.append((d,fixed_diff*(d-1)/(D*target**(d-1))))
    # The model's two different first-arrival definitions have opposite signs eventually.
    assert all(z>0 for d,z in moving if d>=12)
    assert abs(moving[-1][1]-1)<.003
    assert .6<fixed[-1][1]<1
    print('case', (P,Delta,H,delta,r0),'s=',round(s,6),'t=',round(target,6))
    print('moving_ratios',[(d,round(v,7)) for d,v in moving])
    print('fixed_ratios',[(d,round(v,7)) for d,v in fixed])
    return len(moving)

if __name__=='__main__':
    n=0
    n+=check(6.0,1.0,5.0,.15,.01)
    n+=check(8.0,2.0,3.0,.12,.015)
    n+=check(5.0,1.0,2.0,.1,.005)
    print('VERIFY_OK configurations=3 interaction_orders=',n, 'integral_and_equilibrium_checks=',2*n)
