"""Independent numerical consistency checks for the half-rotation tongue theorem.
Run with Python 3 standard library: python3 check_tongue.py.
These finite tests corroborate, but do not prove, the analytic assertions.
"""
import math
PI = math.pi
TAU = 2 * PI

def F(x, a, b, omega):
    return x + a * (1 - (omega - b * math.sin(TAU * x))**2)

def R(x, a, b, omega):
    y = F(x, a, b, omega)
    return F(y, a, b, omega) - x - 1

def DF(x, a, b, omega):
    return 1 + 4 * PI * a * b * (omega - b * math.sin(TAU * x)) * math.cos(TAU * x)

def bisect(func, lo, hi, iters=60):
    vlo = func(lo)
    vhi = func(hi)
    assert vlo <= 0 <= vhi or vhi <= 0 <= vlo, (lo, hi, vlo, vhi)
    if vlo > 0:
        return bisect(lambda t: -func(t), lo, hi, iters)
    for _ in range(iters):
        mid = (lo + hi) / 2
        if func(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def A(x, b, omega):
    return bisect(lambda a: R(x, a, b, omega), 0, 1.5)

def golden_opt(fun, left, right, maximize=False):
    if maximize:
        return golden_opt(lambda x: -fun(x), left, right, False)
    k = (math.sqrt(5) - 1) / 2
    u = right - k * (right-left)
    v = left + k * (right-left)
    fu, fv = fun(u), fun(v)
    for _ in range(66):
        if fu > fv:
            left, u, fu = u, v, fv
            v = left + k * (right-left)
            fv = fun(v)
        else:
            right, v, fv = v, u, fu
            u = right - k * (right-left)
            fu = fun(u)
    return (left+right)/2

def critical_extrema(b, omega, N=160):
    vals = [A(i/N, b, omega) for i in range(N)]
    highs, lows = [], []
    for i in range(N):
        l, r = vals[(i-1)%N], vals[(i+1)%N]
        if vals[i] >= max(l, r):
            x = golden_opt(lambda z: A(z,b,omega), (i-1)/N, (i+1)/N, True)
            highs.append((x%1, A(x,b,omega)))
        if vals[i] <= min(l, r):
            x = golden_opt(lambda z: A(z,b,omega), (i-1)/N, (i+1)/N)
            lows.append((x%1, A(x,b,omega)))
    assert len(highs) == 2 and len(lows) == 2, (omega, b, highs, lows)
    assert abs(highs[0][1]-highs[1][1]) < 2e-10
    assert abs(lows[0][1]-lows[1][1]) < 2e-10
    return lows[0][1], highs[0][1]

def four_orbit_roots(a,b,omega):
    N=300
    roots=[]
    for i in range(N):
        x,y=i/N,(i+1)/N
        if R(x,a,b,omega)*R(y,a,b,omega)<0:
            roots.append(bisect(lambda z:R(z,a,b,omega),x,y))
    assert len(roots)==4, (a,b,omega,len(roots))
    stable=0;unstable=0
    for x in roots:
        y=F(x,a,b,omega)
        assert min(abs((y%1)-v) for v in roots)<5e-8 or min(abs((y%1)-v+1) for v in roots)<5e-8
        product=DF(x,a,b,omega)*DF(y,a,b,omega)
        assert product>0
        stable += (product<1)
        unstable += (product>1)
    assert stable==unstable==2,(stable,unstable)
    return True

def run():
    checks=0
    for omega in (0,0.2,0.45,0.65):
        d=1-omega*omega
        a0=1/(2*d)
        S=math.sqrt(1+4*PI*PI*omega**4/d**2)
        for b in (0.015,0.025,0.04):
            lo,hi=critical_extrema(b,omega)
            assert abs(lo-(a0+(1-S)*b*b/(4*d*d))) < 250*b**4
            assert abs(hi-(a0+(1+S)*b*b/(4*d*d))) < 250*b**4
            assert abs((hi-lo)/b**2-S/(2*d*d)) < 500*b*b
            if omega==0:
                assert abs(lo-0.5)<1e-12
                assert abs(hi-1/(2*(1-b*b)))<1e-12
            assert four_orbit_roots((lo+hi)/2,b,omega)
            checks+=7
    omega0=1/math.sqrt(2)
    K=(math.sqrt(1+4*PI*PI)-1)/(2*math.sqrt(2))
    for b in (0.015,0.025,0.04):
        star=bisect(lambda omega: critical_extrema(b,omega)[0]-1,0.69,0.72,34)
        assert abs(star-(omega0+K*b*b))<100*b**4
        below=star-2e-5
        above=star+2e-5
        assert critical_extrema(b,below)[0]<1<critical_extrema(b,above)[0]
        checks+=3
    print(f'PASS: {checks} finite boundary, profile, and stability consistency tests')
if __name__ == '__main__':run()
