"""Numerical verification of the stated pure-gas location-score theorem.

Dependencies: Python 3, scipy, numpy.  All checks are finite tests; the
all-parameter and singular-limit statements are established analytically.
"""
import math
from scipy.integrate import quad
from scipy.special import lambertw


def u_profile(x, chi, u0):
    z = -u0 * math.exp(-u0-chi*abs(x))
    return -lambertw(z).real


def params(m, M, chi):
    delta = 1.0-2*M*chi/m
    if not (m > 4 and 0 <= delta < 1):
        raise ValueError('outside declared parameter regime')
    return delta, 1-math.sqrt(delta)


def p(x,m,M,chi):
    delta,u0=params(m,M,chi)
    return m/(2*M)*u_profile(x,chi,u0)

checks=0
for m,M,chi in [(6.,6.,.4),(9.,5.,.6),(10.,3.,.8),(6.,6.,.5)]:
    delta,u0=params(m,M,chi)
    integral=2*quad(lambda x:p(x,m,M,chi),0,120/chi,epsabs=1e-10,limit=300)[0]
    assert abs(integral-1)<2e-8,(m,M,chi,integral)
    checks+=1
    for x in [.08,.31,.9,2.7,5.2]:
        ux=u_profile(x,chi,u0)
        # Source equation: d[u-u^2/2]/dx=-chi*u.
        eps=1e-5
        fplus=u_profile(x+eps,chi,u0)
        fminus=u_profile(x-eps,chi,u0)
        residual=(fplus-fminus)/(2*eps)*(1-ux)+chi*ux
        assert abs(residual)<2e-7,(m,M,chi,x,residual)
        checks+=1
    if delta>0:
        lo,hi=chi,chi/math.sqrt(delta)
        norm=quad(lambda w:m*chi/(M*w**3),lo,hi)[0]
        assert abs(norm-1)<1e-10
        checks+=1
        for q in [0.5,1.,1.4,2.,3.]:
            measured=quad(lambda w:w**q*m*chi/(M*w**3),lo,hi)[0]
            if q==2:
                formula=m*chi/(2*M)*math.log(1/delta)
            else:
                formula=m*chi**(q-1)/M*(1-delta**((2-q)/2))/(2-q)
            assert abs(measured-formula)<1e-9*max(1,abs(formula)),(q,measured,formula)
            checks+=1

# Nonregular critical-location Hellinger asymptotic, direct quadrature.
m=M=6.
chi=m/(2*M)
def rootp(x): return math.sqrt(p(x,m,M,chi))
ratios=[]
for h in [0.025,0.008,0.0025,0.0008]:
    h2=.5*quad(lambda x:(rootp(x-h)-rootp(x))**2,-100,100,points=[0,h],epsabs=1e-13,limit=450)[0]
    lead=chi**2/8*h*h*math.log(1/(chi*h))
    ratios.append(h2/lead)
    assert 1<ratios[-1]<1.20,(h,ratios[-1])
    checks+=1
assert all(ratios[j+1]<ratios[j] for j in range(len(ratios)-1)),ratios
checks+=1
print(f'{checks} tests passed. Hellinger leading-term ratios:',[round(x,8) for x in ratios])
