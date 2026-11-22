"""Independent finite diagnostics for the circular Gaussian Fourier frontier.
Only finite numerical checks; the uniform theorem is analytic.
Requires Python and mpmath.
"""
import mpmath as mp
mp.mp.dps = 90
pi = mp.pi

def j(t, q):
    t, q = mp.mpf(t), mp.mpf(q)
    return mp.quad(lambda v: mp.exp(-2*pi*v-v*v/t)*mp.cos(q*v), [0,1,2,4,8,16,mp.inf])

def scaled_coefficient(t, n):
    t=mp.mpf(t)
    n=int(n)
    gauss=mp.exp(pi*pi*t-n*n/(4*t))/(2*mp.sqrt(pi*t))
    return gauss-(-1)**n*j(t,n/t)/(pi*t)

def center(t):
    t=mp.mpf(t)
    return 2*pi*t+mp.log(t)/(2*pi)+mp.log(2*pi**mp.mpf('1.5'))/pi

checks=0
for t in (1,2,5,10,20):
    v=center(t)
    n=2*int(mp.floor(v/2))
    lo=scaled_coefficient(t,n)
    hi=scaled_coefficient(t,n+2)
    assert lo>0 and hi<0, (t,n,lo,hi)
    checks+=2
    print('transition',t,'center',mp.nstr(v,16),'positive_even',n,'negative_even',n+2)
for t in (mp.mpf('0.25'),1,2,5,10):
    for n in (1,3,5,9,15):
        assert j(t,mp.mpf(n)/t)>0
        assert scaled_coefficient(t,n)>0
        checks+=2
for t in (20,40,80):
    for q in (0,mp.mpf('1'),2*pi,4*pi):
        rr=j(t,q)/(2*pi/(4*pi*pi+q*q))
        assert abs(rr-1)<mp.mpf('0.2')
        checks+=1
# Identity checked at moderate bandwidths to avoid catastrophic cancellation.
for t in (mp.mpf('0.5'),1,2):
    for n in (2,5,8):
        direct=mp.quad(lambda x: mp.exp(-t*x*x)*mp.cos(n*x), [0,pi/4,pi/2,3*pi/4,pi])/pi
        transformed=mp.exp(-pi*pi*t)*scaled_coefficient(t,n)
        assert abs(direct-transformed)<mp.mpf('1e-65')
        checks+=1
print('PASS:',checks,'finite diagnostics (not an infinite proof)')
