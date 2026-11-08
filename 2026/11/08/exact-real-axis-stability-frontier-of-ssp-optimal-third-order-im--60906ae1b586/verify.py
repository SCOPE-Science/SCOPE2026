"""Finite, independent numerical checks for the optimal SSP-SDIRK3 real-axis theorem.

Run: python verify.py
Universal assertions are proved algebraically in RESULT.md, not by this finite test.
"""
from mpmath import mp

mp.dps = 90
count = 0

def assert_close(a, b, label, tol=mp.mpf('1e-65')):
    global count
    if abs(a - b) > tol * (1 + abs(a) + abs(b)):
        raise AssertionError((label, mp.nstr(a, 30), mp.nstr(b, 30)))
    count += 1

def params(s):
    s = int(s)
    gamma = (1-mp.sqrt(mp.mpf(s-1)/(s+1)))/2
    delta = 1/mp.sqrt(s*s-1)
    c = mp.sqrt(1-mp.mpf(1)/(s*s))
    q = mp.sqrt(mp.mpf(s+1)/(s-1))
    u = mp.root(2/c-1, s)
    crit = (2/(delta-2*gamma) if s % 2 == 0 else
            (1+u)/(delta-gamma*(1+u)))
    return gamma,delta,c,q,u,crit

def rational_stability(s, x):
    g, d, c, q, u, _ = params(s)
    t=(1-(d-g)*x)/(1+g*x)
    return 1-c+c*t**s

def direct_stability(s, x):
    g,d,_,_,_,_=params(s)
    ysum=mp.mpf(0)
    for _ in range(s):
        stage=(1-x*d*ysum)/(1+x*g)
        ysum+=stage
    return 1-x*ysum/s

for s in range(2,36):
    g,d,c,q,u,xcrit=params(s)
    assert_close(c,1/(s*d),('prefactor',s))
    assert_close(d/g,1+q,('ratio',s))
    assert_close((1-(d-g)*xcrit)/(1+g*xcrit),
                 -1 if s%2==0 else -u,('critical t',s))
    assert_close(rational_stability(s,xcrit),
                 1 if s%2==0 else -1,('critical R',s))
    for scale in [mp.mpf('1e-10'),mp.mpf('0.01'),mp.mpf('0.2'),
                  mp.mpf('0.75'),mp.mpf('0.9999'),mp.mpf('1'),
                  mp.mpf('1.0001'),mp.mpf('1.3'),mp.mpf('5'),mp.mpf('100')]:
        x = xcrit*scale
        R=rational_stability(s,x)
        assert_close(R,direct_stability(s,x),('direct vs closed',s,scale))
        if scale < 1 and not abs(R)<1:
            raise AssertionError(('stable interior',s,scale,R))
        if scale > 1 and not abs(R)>1:
            raise AssertionError(('unstable exterior',s,scale,R))
        count+=1
    lim=1-c+(-1)**s*c*q**s
    if not ((lim>1) if s%2==0 else (lim< -1)):
        raise AssertionError(('stiff limit sign',s))
    count+=1

for s in [10,20,50,100,200,500,1000]:
    g,d,c,q,u,xcrit=params(s)
    asymp=4*s*s+(-3 if s%2==0 else 1)
    if abs(xcrit-asymp)>mp.mpf(10)/s**2:
        raise AssertionError(('critical asymptotic',s,xcrit,asymp))
    lim=1-c+(-1)**s*c*q**s
    if abs(lim-(-1)**s*mp.e)>mp.mpf(10)/s**2:
        raise AssertionError(('limit asymptotic',s,lim))
    count+=2
print('VERIFY_OK',count)
