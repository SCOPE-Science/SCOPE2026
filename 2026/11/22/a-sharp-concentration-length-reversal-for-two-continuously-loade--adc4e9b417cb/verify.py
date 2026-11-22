"""Finite diagnostic checks for two serial saturating nutrient-removal reaches.

Run: python verify.py (Python 3 standard library). The analytic theorem is in RESULT.md.
"""
import math
import random


def phi(c, H, s, k):
    assert c >= 0 and H > 0 and s > k > 0
    w = s-k
    return c/w-k*H/(w*w)*math.log1p(w*c/(s*H))


def flow(c, H, s, k, t):
    """Monotone inversion of the exact scalar flow primitive."""
    assert t >= 0
    if t == 0:
        return c
    target = phi(c,H,s,k)+t
    lo,hi = c,c+s*t+1.
    for _ in range(85):
        mid=(lo+hi)/2
        if phi(mid,H,s,k) < target: lo=mid
        else: hi=mid
    return (lo+hi)/2


def order_difference(x, K, L, s, k, a, b):
    """Outlet (L then K) minus outlet (K then L)."""
    LK=flow(flow(x,L,s,k,b),K,s,k,a)
    KL=flow(flow(x,K,s,k,a),L,s,k,b)
    return LK-KL


def deltadiff(b,z,K,L,s,k,a):
    x=flow(0.,L,s,k,z)
    xb=flow(x,L,s,k,b)
    return (phi(flow(xb,K,s,k,a),L,s,k)-(z+b))-(phi(flow(x,K,s,k,a),L,s,k)-z)


def bisection(f,lo,hi,steps=75):
    f0=f(lo);f1=f(hi)
    if f0*f1 >= 0: raise ValueError((f0,f1))
    for _ in range(steps):
        mid=(lo+hi)/2
        fm=f(mid)
        if (fm>0)==(f0>0):lo=mid;f0=fm
        else:hi=mid
    return (lo+hi)/2


def turning_z(K,L,s,k,a):
    q=s*K*L/(s-k)
    f=lambda z: flow(0,L,s,k,z)*flow(flow(0,L,s,k,z),K,s,k,a)-q
    hi=1.
    while f(hi)<0:hi*=2
    return bisection(f,0.,hi)


def critical_b(K,L,s,k,a):
    z0=turning_z(K,L,s,k,a)
    f=lambda b:deltadiff(b,0.,K,L,s,k,a)
    hi=max(1.,z0*2)
    while f(hi)>0:hi*=2
    return z0,bisection(f,z0,hi)


def crossing_x(K,L,s,k,a,b,z0):
    f=lambda z:deltadiff(b,z,K,L,s,k,a)
    zz=bisection(f,0.,z0)
    return flow(0.,L,s,k,zz)


def check():
    tests=0
    s,k,K,L,a=2.,1.,4.,1.,1.
    z0,bc=critical_b(K,L,s,k,a)
    assert abs(z0-1.418006394027433)<1e-9
    assert abs(bc-8.185090434901728)<1e-8
    tests+=2
    for b in (0.1,0.5,1.,3.,5.,7.,8.):
        xc=crossing_x(K,L,s,k,a,b,z0)
        for xx in (0.,xc/2,xc+0.1,xc+1.,xc+10.):
            v=order_difference(xx,K,L,s,k,a,b)
            expected=1 if xx<xc else -1
            assert expected*v > 2e-12,(b,xx,xc,v)
            tests+=1
    xc=crossing_x(K,L,s,k,a,1.,z0)
    assert abs(xc-1.562116337663599)<1e-8
    tests+=1
    for b in (bc+0.1,bc+1,bc+10):
        for xx in (0.,0.01,0.1,1.,5.,100.):
            assert order_difference(xx,K,L,s,k,a,b)<-1e-10
            tests+=1
    for bb in (0.1,0.5,1.,3.,8.):
        for xx in (0.1,0.5,1.,2.,10.):
            # Exact transform identity sign. Both outlet coordinates are strictly increasing transforms.
            z=phi(xx,L,s,k)
            dz=deltadiff(bb,z,K,L,s,k,a)
            d=order_difference(xx,K,L,s,k,a,bb)
            assert (dz>0)==(d>0),(bb,xx,dz,d)
            tests+=1
    rng=random.Random(450531)
    for j in range(450):
        s=rng.uniform(1.,3.);k=s*rng.uniform(.15,.85)
        L=rng.uniform(.2,2.)
        K=L+rng.uniform(.15,4.)
        a=rng.uniform(.1,2.)
        z0,bc=critical_b(K,L,s,k,a)
        assert 0<z0<bc
        tests+=1
        b=bc*rng.uniform(.1,.9)
        xc=crossing_x(K,L,s,k,a,b,z0)
        assert xc>0
        tests+=1
        for xx in (0.,xc/2,xc+max(.02,xc*.1)):
            d=order_difference(xx,K,L,s,k,a,b)
            if xx<xc:assert d>1e-12,(j,xx,xc,d)
            else:assert d< -1e-12,(j,xx,xc,d)
            tests+=1
    print('VERIFY_OK assertions=',tests)
    print('example: z0=',1.418006394027433,'b_crit=',8.185090434901728)
    print('example: at b=1, inlet switch=',1.562116337663599)

if __name__=='__main__':check()
