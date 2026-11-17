#!/usr/bin/env python3
"""Standalone algebra and sign consistency checks for the cyclic population model."""
import math
import cmath


def vector_original(m, alpha, beta, mu):
    return [m[i] * (1-m[i]-alpha*m[(i+1)%3]-beta*m[(i+2)%3])
            + mu*(m[(i+1)%3]+m[(i+2)%3]-2*m[i]) for i in range(3)]


def vector_reduced(x, y, z, alpha, beta, mu):
    sig = 1+alpha+beta
    lam = (alpha+beta-2)/2
    w = math.sqrt(3)*(beta-alpha)/2
    omega = w/sig
    delta = lam/(3*sig)-mu
    c = (sig+3)/2
    U = complex(x, y)
    dU = complex(3*delta, omega)*U + complex(lam,-w)*U.conjugate()**2 + complex(-c,w)*U*z
    dz = -z-sig*z*z+2*lam*abs(U)**2
    return dU.real, dU.imag, dz


def period_slope(lam, w):
    sig = 2*lam+3
    return 2*sig/(lam*(sig+3))*(3-lam+sig*lam*lam/(w*w))


def close(a,b, tol=3e-10):
    assert abs(a-b) <= tol*max(1.0,abs(a),abs(b)), (a,b)


for alpha,beta,mu,x,y,z in [
    (1.2,2.4,.013,.011,-.021,.002),
    (11-16/math.sqrt(3),11+16/math.sqrt(3),.14,.002,.003,-.001),
    (11-18.5/math.sqrt(3),11+18.5/math.sqrt(3),.14,-.001,.002,.0003),
    (.5,2.9,.02,.021,.013,.008)]:
    sig=1+alpha+beta
    m=[1/sig+2*x+z,1/sig-x-math.sqrt(3)*y+z,1/sig-x+math.sqrt(3)*y+z]
    assert min(m)>0
    a=vector_original(m,alpha,beta,mu)
    derived=((2*a[0]-a[1]-a[2])/6,(a[2]-a[1])/(2*math.sqrt(3)),sum(a)/3)
    expected=vector_reduced(x,y,z,alpha,beta,mu)
    for got,want in zip(derived,expected):close(got,want)

for lam,w in [(.6,1.0),(10,16),(10,18.5),(20,30),(20,36)]:
    sig=2*lam+3;c=(sig+3)/2;omega=w/sig
    A=1j*complex(lam,-w)/(3*omega)
    B=2*complex(lam,-w)*A.conjugate()+2*lam*complex(-c,w)
    close(B.real,-2*lam*c)
    close(B.imag,2*lam*w-2*(lam*lam+w*w)/(3*omega))
    rho_to_r2=3/(2*lam*c)
    direct=-(B.imag/omega)*rho_to_r2
    close(direct,period_slope(lam,w))

root_low=8.0123;root_high=8.0124
f=lambda u:u**3-6*u*u-15*u-9
assert f(root_low)<0<f(root_high)
for lam,w in [(10,16),(10,18.5)]:
    assert abs(w)<math.sqrt(3)*(lam+1)
assert period_slope(10,16)>0>period_slope(10,18.5)
assert period_slope(8,math.sqrt(3)*9*.999)>0
assert period_slope(20,30)>0>period_slope(20,36)
print('MAY_LEONARD_HOPF_PERIOD_SIGN_OK')
