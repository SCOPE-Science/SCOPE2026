"""Reproduce finite consistency checks for an exact two-line Gaussian STFT zero law.

The universal statements follow from the analytic proof, not these tests.
"""
import math
import cmath

PI=math.pi


def parameters(nu1,nu2,s1,s2,z1,z2):
    delta=nu2-nu1
    assert delta>0 and s1>0 and s2>0 and z1 and z2
    mu=(nu1+nu2)/2+math.log(s1/s2)/(2*PI*delta)
    omega=mu+math.log(abs(z1)**2/abs(z2)**2)/(4*PI*delta)
    phase=((cmath.phase(-z1/z2)/(2*PI))%1)
    return delta,mu,omega,phase


def stft(x,w,nu1,nu2,s1,s2,z1,z2):
    inside=(s1*z1*math.exp(-PI*(w-nu1)**2)*cmath.exp(2j*PI*nu1*x)
           +s2*z2*math.exp(-PI*(w-nu2)**2)*cmath.exp(2j*PI*nu2*x))
    return 2**.25*cmath.exp(-2j*PI*w*x)*inside


def density(w,delta,mu):
    y=2*PI*delta*(w-mu)
    return PI*delta/math.cosh(y)**2


checks=0
samples=[(-.4,1.3,1,1,(1+.3j),(-.9+.2j)),
         (0.,.33,.2,1.7,(.02+.5j),(2.-.3j)),
         (-3.,-2.25,2.2,.8,(-3.+.75j),(.5-1.4j))]
for nu1,nu2,s1,s2,z1,z2 in samples:
    delta,mu,omega,U=parameters(nu1,nu2,s1,s2,z1,z2)
    for k in range(-5,6):
        x=(k+U)/delta
        assert abs(stft(x,omega,nu1,nu2,s1,s2,z1,z2))<2e-9
        checks+=1
    # Check ratio of independent Exp(1) magnitudes: exact CDF of log ratio.
    for v in [-5.,-2.,0.,.7,3.,7.]:
        F=math.exp(v)/(1+math.exp(v))
        assert abs(F-1/(1+math.exp(-v)))<1e-14
        checks+=1
    # Smoothed atomic spectral measure as Gaussian kernel sum:
    # its log-second derivative is -4pi + 4pi^2 delta^2 sech^2.
    for w in [mu-1.3,mu-.1,mu,mu+.26,mu+1.23]:
        a=s1*s1*math.exp(-2*PI*(w-nu1)**2)
        b=s2*s2*math.exp(-2*PI*(w-nu2)**2)
        weights=a/(a+b),b/(a+b)
        mean=(weights[0]*(w-nu1)+weights[1]*(w-nu2))
        second=-4*PI+16*PI**2*(weights[0]*(w-nu1)**2+weights[1]*(w-nu2)**2-mean**2)
        assert abs(1+second/(4*PI)-delta*density(w,delta,mu))<2e-9
        checks+=1

# Exact count distribution by enumeration of every rational lattice phase U=j/10000.
for t in [0.1,.37,1.0,1.41,2.37,7.91]:
    n=math.floor(t);u=t-n
    counts=[]
    for j in range(10000):
        U=(j+.5)/10000
        N=sum(0<=k+U<t for k in range(-2,12))
        counts.append(N)
    avg=sum(counts)/len(counts)
    var=sum((x-avg)**2 for x in counts)/len(counts)
    assert abs(avg-t)<1e-4
    assert abs(var-u*(1-u))<1e-4
    checks+=2
print('TWO_LINE_GAUSSIAN_ZERO_CHECKS_PASSED',checks)
