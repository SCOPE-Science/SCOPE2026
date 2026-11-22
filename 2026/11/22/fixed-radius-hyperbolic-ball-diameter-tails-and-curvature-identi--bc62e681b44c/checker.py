"""Independent quadrature checks for a fixed-radius hyperbolic ball two-point distance law.
No external data needed; numerical checks do not replace the proof.
"""
from math import sinh, cosh, tanh, gamma, sqrt, pi
from scipy.integrate import quad
from scipy.special import betainc
from numpy.polynomial.legendre import leggauss
import numpy as np

def radial_integral(n,k,T):
    q=n-1
    return quad(lambda x:(sinh(k*x)/k if k else x)**q,0,T,epsabs=1e-12)[0]

def boundary_density(n,k,T):
    return (sinh(k*T)/k if k else T)**(n-1)/radial_integral(n,k,T)

def coefficient(n,k,T):
    p=(n-1)/2
    c=(tanh(k*T)/k if k else T)/4
    return boundary_density(n,k,T)**2*gamma(n/2)/(2*sqrt(pi)*gamma(p+3))*c**(-p)

def exact_tail(n,k,T,eps,order=42):
    p=(n-1)/2
    xx,ww=leggauss(order)
    xx=(xx+1)/2; ww=ww/2
    I=radial_integral(n,k,T)
    target=2*T-eps
    z=0.0
    for x,wx in zip(xx,ww):
        a=eps*x
        s=T-a
        fs=(sinh(k*s)/k if k else s)**(n-1)/I
        for v,wv in zip(xx,ww):
            b=eps*(1-x)*v
            t=T-b
            ft=(sinh(k*t)/k if k else t)**(n-1)/I
            if k:
                # Avoid subtractive cancellation in cosh of nearby arguments.
                d=s+t-target
                numerator=2*sinh(k*(s+t+target)/2)*sinh(k*d/2)
                den=2*sinh(k*s)*sinh(k*t)
            else:
                numerator=(s+t)**2-target**2
                den=4*s*t
            Q=max(0,min(1,numerator/den))
            z+=wx*wv*eps**2*(1-x)*fs*ft*betainc(p,p,Q)
    return z

def exact_n3_tail_one_dim(k,T,eps):
    # Valid for threshold L=2T-eps >= T, and k>0.
    L=2*T-eps
    I=radial_integral(3,k,T)
    def integrand(u):
        return (cosh(k*u)-cosh(k*L))*((2*T-u)*cosh(k*u)-sinh(k*(2*T-u))/k)
    return quad(integrand,L,2*T,epsabs=1e-14,epsrel=1e-12)[0]/(4*I**2*k**4)

if __name__=='__main__':
    count=0
    for n,k,T in [(2,1,1),(3,1,1),(4,1.7,0.8),(3,0.7,1.5),(5,0.7,1.5),(3,0,1)]:
        C=coefficient(n,k,T)
        errors=[]
        for eps in [0.22,0.11,0.055]:
            value=exact_tail(n,k,T,eps)
            relative=value/(C*eps**((n+3)/2))-1
            errors.append(abs(relative))
            assert 0<value<1
            count+=1
            if n==3 and k>0:
                ref=exact_n3_tail_one_dim(k,T,eps)
                assert abs(value-ref) < 5e-9*max(1,ref), (value,ref)
                count+=1
        assert errors[-1]<errors[0],(n,k,T,errors)
        count+=1
        print('n,k,T:',n,k,T, 'coefficient:',C,'relative errors:',errors)
    for n in range(2,8):
        vals=[coefficient(n,k,1.3) for k in [0,0.2,0.8,2.0]]
        assert all(a<b for a,b in zip(vals,vals[1:]))
        count+=1
    print('HYPERBOLIC_BALL_FIXED_RADIUS_CHECKS_OK',count)
