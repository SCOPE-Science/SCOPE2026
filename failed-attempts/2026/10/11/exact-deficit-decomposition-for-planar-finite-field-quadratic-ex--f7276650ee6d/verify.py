from fractions import Fraction
import math

PRIMES=[3,5,7,11,13,17,19,23,29,31]

def legendre(a,p):
    a%=p
    if a==0:
        return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def nonsquare(p):
    for d in range(2,p):
        if legendre(d,p)==-1:
            return d
    raise AssertionError("no nonsquare")

def gadd(z,w):
    return (z[0]+w[0],z[1]+w[1])

def gmul(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])

def gnorm(z):
    return z[0]*z[0]+z[1]*z[1]

def check(p,kind):
    if kind=="split":
        pts=[(x,y) for x in range(p) for y in range(p) if x*y%p==1]
        expected=p-1
    else:
        d=nonsquare(p)
        pts=[(x,y) for x in range(p) for y in range(p) if (x*x-d*y*y)%p==1]
        expected=p+1
    assert len(pts)==expected
    pset=set(pts)
    fibers={}
    for a in pts:
        for b in pts:
            s=((a[0]+b[0])%p,(a[1]+b[1])%p)
            fibers.setdefault(s,[]).append((a,b))
    assert len(fibers[(0,0)])==expected
    for s,ls in fibers.items():
        if s==(0,0):
            continue
        assert len(ls)<=2
        if len(ls)==2:
            assert ls[0][0]==ls[1][1] and ls[0][1]==ls[1][0]
    seen=set()
    reps=[]
    for a in sorted(pts):
        if a in seen:
            continue
        na=((-a[0])%p,(-a[1])%p)
        assert na in pset and na!=a
        reps.append(a)
        seen.add(a)
        seen.add(na)
    m=len(reps)
    assert 2*m==expected
    units=[(1,0),(0,1),(-1,0),(0,-1)]
    f={}
    for idx,a in enumerate(sorted(pts)):
        amp=1+(idx%4)
        unit=units[(3*idx+1)%4]
        f[a]=(amp*unit[0],amp*unit[1])
    W=0
    for ls in fibers.values():
        z=(0,0)
        for a,b in ls:
            z=gadd(z,gmul(f[a],f[b]))
        W+=gnorm(z)
    T=sum(gnorm(f[a]) for a in pts)
    us=[]; vs=[]; ts=[]; rs=[]; zs=[]
    for a in reps:
        b=((-a[0])%p,(-a[1])%p)
        u=gnorm(f[a]); v=gnorm(f[b])
        r=math.isqrt(u*v)
        assert r*r==u*v
        us.append(u); vs.append(v); ts.append(u+v); rs.append(r); zs.append(gmul(f[a],f[b]))
    P=(sum(z[0] for z in zs),sum(z[1] for z in zs))
    R=sum(rs)
    delta=Fraction(3*expected-3,expected)*T*T-W
    d1=Fraction(3,2)*(sum(t*t for t in ts)-Fraction(T*T,m))
    d2=Fraction(1,2)*sum((u-v)**2 for u,v in zip(us,vs))
    d3=2*sum(ts[i]*ts[k]-4*rs[i]*rs[k] for i in range(m) for k in range(i+1,m))
    d4=4*(R*R-gnorm(P))
    assert delta==d1+d2+d3+d4
    assert d1>=0 and d2>=0 and d3>=0 and d4>=0
    uniform_W=3*expected*expected-3*expected
    assert Fraction(uniform_W,expected*expected)==Fraction(3*expected-3,expected)
    return len(fibers)

def main():
    total_fibers=0
    checks=0
    for p in PRIMES:
        for kind in ("split","anisotropic"):
            total_fibers+=check(p,kind)
            checks+=1
    print(f"VERIFY_OK primes={len(PRIMES)} conics={checks} pair_fibers={total_fibers} energy_checks={checks}")

if __name__=="__main__":
    main()
