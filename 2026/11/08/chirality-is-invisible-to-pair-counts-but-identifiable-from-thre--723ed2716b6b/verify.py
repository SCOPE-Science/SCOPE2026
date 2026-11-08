"""Deterministic consistency checks for exact chiral count-cumulant identities.

Requires mpmath. This checks formulas numerically; it is not a proof of
all-parameter statements. Run: python verify.py
"""
import mpmath as mp

mp.mp.dps = 55


def signed_area_closed(v, d, w, t, s):
    lam = mp.mpc(d, -w)
    if lam == 0:
        return mp.mpf('0')
    return v*v*mp.im((1-mp.exp(-lam*t))*(1-mp.exp(-lam*s))/lam**2)


def signed_area_quadrature(v, d, w, t, s):
    return v*v*mp.quad(lambda a: mp.quad(
        lambda b: mp.exp(-d*(b-a))*mp.sin(w*(b-a)), [t, t+s]),
        [0,t])


def msd_closed(v, Dt, d, w, t):
    lam = mp.mpc(d, -w)
    if lam == 0:
        return 4*Dt*t+v*v*t*t
    return 4*Dt*t + 2*v*v*mp.re(t/lam-(1-mp.exp(-lam*t))/lam**2)


def msd_quadrature(v, Dt, d, w, t):
    return 4*Dt*t+2*v*v*mp.quad(
        lambda u: (t-u)*mp.exp(-d*u)*mp.cos(w*u), [0,t])


def close(a,b,tol=mp.mpf('1e-35')):
    assert abs(a-b) <= tol*(1+max(abs(a),abs(b))), (a,b)


checks=0
for d,w in [('0','0'),('0','2'),('0.75','-1.2'),('1.6','0'),('2.25','3.5')]:
    d,w=mp.mpf(d),mp.mpf(w)
    v,Dt=mp.mpf('1.7'),mp.mpf('0.38')
    for t,s in [('0.13','0.27'),('0.6','0.8'),('1.4','0.25')]:
        t,s=mp.mpf(t),mp.mpf(s)
        close(signed_area_closed(v,d,w,t,s),signed_area_quadrature(v,d,w,t,s))
        checks+=1
        close(msd_closed(v,Dt,d,w,t),msd_quadrature(v,Dt,d,w,t))
        checks+=1
        close(signed_area_closed(v,d,w,t,s),-signed_area_closed(v,d,-w,t,s))
        checks+=1
        close(msd_closed(v,Dt,d,w,t),msd_closed(v,Dt,d,-w,t))
        checks+=1

# Test the leading and subleading short-lag asymptotics in several regimes.
for d,w in [('0.5','0.75'),('1.2','-2.5'),('0','3.25')]:
    d,w=mp.mpf(d),mp.mpf(w)
    v=mp.mpf('2.3')
    for j in [3,4,5,6]:
        h=mp.power(10,-j)
        a=signed_area_closed(v,d,w,h,h)
        approximation=v*v*w*h**3*(1-mp.mpf(7)*d*h/6)
        assert abs(a-approximation)<(10*abs(v*v*w)*h**5*(1+d+abs(w))**2)
        checks+=1
    h=mp.mpf('1e-9')
    a=signed_area_closed(v,d,w,h,h)
    w_recovered=a/(v*v*h**3)
    assert abs(w_recovered-w) < mp.mpf('1e-7')
    checks+=1

# The one-lag displacement variance gives the four derivative identities.
for d,w in [('0','0'),('0.25','-4'),('2.2','1.1')]:
    v,Dt=mp.mpf('1.9'),mp.mpf('0.12')
    d,w=mp.mpf(d),mp.mpf(w)
    f=lambda t: msd_closed(v,Dt,d,w,t)
    for order, expected in [
        (1,4*Dt),(2,2*v*v),(3,-2*v*v*d),
        (4,2*v*v*(d*d-w*w))]:
        close(mp.diff(f,0,order),expected,mp.mpf('1e-25'))
        checks+=1

# A marked-Poisson three-count cumulant is intensity times a one-mark
# triple product, as follows by differentiating the log-Laplace functional.
for p1,p2,p3 in [('0.2','0.3','0.9'),('1','0.4','0.7')]:
    p1,p2,p3=map(mp.mpf,(p1,p2,p3))
    intensity=mp.mpf('3.2')
    # A two-state trajectory mark with probability p1 has simultaneous
    # indicators (1,1,1); with complementary probability it has (0,0,0).
    g=lambda a,b,c: intensity*(p1*mp.exp(a+b+c)+(1-p1)-1)
    calc=mp.diff(lambda a: mp.diff(lambda b: mp.diff(
        lambda c: g(a,b,c),0),0),0)
    close(calc,intensity*p1)
    checks+=1

print(f'PASS: {checks} independent quadrature, symmetry, asymptotic and derivative checks')
