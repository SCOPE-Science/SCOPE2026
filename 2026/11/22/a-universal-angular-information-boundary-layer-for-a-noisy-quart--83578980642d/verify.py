"""Reproducible mathematical checks for angular information of trapped telegraph motion.

Requires Python 3, NumPy, and SciPy. Uses deterministic quadrature and exact
rational moments. The continuum theorem is analytic; finite checks are diagnostics.
"""
from fractions import Fraction as Q
import math
import numpy as np
from scipy import integrate, special

count = 0


def close(got, expected, tol=1e-8, label=''):
    global count
    assert math.isfinite(got), (label, got)
    assert abs(got - expected) <= tol, (label, got, expected, tol)
    count += 1


def require(condition, label=''):
    global count
    assert condition, label
    count += 1


def phi(z):
    return np.exp(-0.5*np.asarray(z)**2) / math.sqrt(2*math.pi)


def Phi(z):
    return special.ndtr(z)


def integral(fun, lo, hi, points=None):
    return integrate.quad(fun, lo, hi, epsabs=2e-11, epsrel=2e-11,
                          limit=350, points=points)[0]


def H0_angle(theta):
    return math.tan(theta) + 2*math.log(math.cos(theta))


def trapezoid_pdf(x, a, theta):
    A = a*math.cos(theta)
    B = a*math.sin(theta)
    w = abs(x)
    if B == 0:
        return 1/(2*A) if w < A else 0.
    if w <= A-B:
        return 1/(2*A)
    if w < A+B:
        return (A+B-w)/(4*A*B)
    return 0.


def density_entropy(p, a, b, pts=None):
    def term(x):
        z = p(x)
        return -z*math.log(z) if z > 0 else 0.
    return integral(term,a,b,points=pts)


def gaussian_uniform_pdf(x, a, h):
    s=math.sqrt(h)
    return max(0.,float((Phi((x+a)/s)-Phi((x-a)/s))/(2*a)))


def gaussian_uniform_derivative(x,a,h):
    s=math.sqrt(h)
    return float((phi((x+a)/s)-phi((x-a)/s))/(2*a*s))


def J(a,h):
    s=math.sqrt(h)
    def value(x):
        f=gaussian_uniform_pdf(x,a,h)
        if f <= 1e-290:
            return 0.
        d=gaussian_uniform_derivative(x,a,h)
        return d*d/f
    L=a+12*s
    return integral(value,-L,L,[-a,a])


def primitive(z):
    return z*Phi(z)+phi(z)


def gaussian_trapezoid_pdf(x,A,B,h):
    if B < 1e-12:
        return gaussian_uniform_pdf(x,A,h)
    s=math.sqrt(h)
    # A and B are the half-widths of two independent uniforms.
    d=(primitive((x+A+B)/s)-primitive((x+A-B)/s)
      -primitive((x-A+B)/s)+primitive((x-A-B)/s))
    return max(0.,float(s*d/(4*A*B)))


def H_gauss_sum(a,h,theta):
    A=a*math.cos(theta)
    B=a*math.sin(theta)
    s=math.sqrt(h)
    L=A+B+11*s
    pdf=lambda x: gaussian_trapezoid_pdf(x,A,B,h)
    return density_entropy(pdf,-L,L, [-A-B,-A+B,A-B,A+B])


def MI(a,h,theta):
    Hu=H_gauss_sum(a,h,0.)
    Hw=H_gauss_sum(a,h,theta)
    return 2*(Hw-Hu)


def G(t,z):
    if t==0:
        return float(Phi(-z))
    return float(np.clip((primitive(t-z)-primitive(-t-z))/(2*t),0,1))


def H_layer(t):
    def val(z):
        q=G(t,z)
        return -q*math.log(q) if q>0 else 0.
    return integral(val,-t-12,t+12,points=[-t,t] if t else None)


def K_constant():
    def val(z):
        g=Phi(-z)
        return float(phi(z)**2/g) if g > 0 else 0.
    return integral(val,-12,12)


def check():
    # Exact uniform-trapezoid entropy, independent of any approximation.
    for a in [0.7,1.,2.5]:
        for theta in [0.025,0.1,0.2,0.4,math.pi/6,math.pi/4]:
            A=a*math.cos(theta); B=a*math.sin(theta)
            p=lambda x: trapezoid_pdf(x,a,theta)
            H=density_entropy(p,-A-B,A+B,[-A+B,A-B])
            close(2*(H-math.log(2*a)),H0_angle(theta),2e-9,
                  f'trapezoid a={a}, theta={theta}')
            require(H0_angle(theta)>0,'athermal positive info')
        close(H0_angle(math.pi/4),1-math.log(2),2e-14,'maximum')
    for theta in np.linspace(.01,.78,30):
        der=((1-math.tan(theta))**2)
        d=.000001
        measured=(H0_angle(theta+d)-H0_angle(theta-d))/(2*d)
        close(measured,der,2e-9,'athermal derivative')
    for delta in [.025,.0125,.00625]:
        slope=(H0_angle(math.pi/4)-H0_angle(math.pi/4-delta))/delta**3
        require(abs(slope-4/3)<4*delta,'cubic maximum')
    # An exact fourth-cumulant, fully evaluated in rational arithmetic.
    for a in [Q(1),Q(3,2),Q(5,2)]:
        for h in [Q(0),Q(1,7),Q(2)]:
            m2=a*a/Q(3)+h
            m4=a**4/Q(5)+2*a*a*h+3*h*h
            for c,s in [(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(1),Q(0))]:
                xy2=2*c*c*s*s*m4+(c**4+s**4-4*c*c*s*s)*m2*m2
                cum=xy2-m2*m2
                close(float(cum),float(-4*a**4*c*c*s*s/15),1e-13,
                      'exact mixed cumulant')
    # Gaussian-blurred one-particle density and its variance.
    for a,h in [(1.,.05),(1.,.2),(1.,1.),(1.75,.3)]:
        s=math.sqrt(h); L=a+12*s
        pdf=lambda x:gaussian_uniform_pdf(x,a,h)
        close(integral(pdf,-L,L,[-a,a]),1,2e-10,'density normalized')
        close(integral(lambda x:x*x*pdf(x),-L,L,[-a,a]),a*a/3+h,
              3e-9,'variance')
        j=J(a,h)
        require(j*(a*a/3+h)>1,'strict information inequality')
        for theta in [.012,.025,.04]:
            val=MI(a,h,theta)
            require(val>0,'thermal MI strictly positive')
            coeff=(a*a/3+h)*j-1
            close(val/theta**2,coeff,max(.025*coeff,.00008),
                  'quadratic small-angle scale')
    # Fisher constant and the two limits of the universal layer.
    K=K_constant()
    close(K,.9031972855686,5e-11,'universal K')
    H0=H_layer(0.)
    close(H0,K,2e-8,'H(0)=K integration by parts')
    for t in [.05,.1,.3,.5,1.,2.,5.,10.]:
        require(H_layer(t)>H0,'strictly positive information layer')
    for t in [.03,.05,.075]:
        F=2*(H_layer(t)-H0)
        close(F/t**2,K/3,max(.0004, t*t/5),'quadratic layer endpoint')
    for t in [20.,40.]:
        F=2*(H_layer(t)-H0)
        require(abs(F/t-1)<.12,'linear layer endpoint')
    for h in [.001,.003,.01]:
        close(math.sqrt(h)*J(1.,h),K,5e-6,
              'Fisher singular coefficient')
    # Finite-noise crossover approaches the universal function as epsilon shrinks.
    for t in [.5,1.,2.]:
        F=2*(H_layer(t)-H0)
        for eps in [.1,.06,.04]:
            actual=MI(1.,eps*eps,eps*t)/eps
            require(abs(actual-F)<4*eps*t*t+.016,
                    'finite-noise crossover to universal limit')
    # Heat/noise lowers information at a fixed nonaxis angle.
    for theta in [.1,.2,.4,math.pi/4]:
        vals=[MI(1.,h,theta) for h in [.02,.05,.2,1.]]
        require(all(u>v>0 for u,v in zip(vals,vals[1:])),
                'strict information loss from independent Gaussian noise')
    print(f'PASS: {count} deterministic exact-rational / quadrature assertions')
    print(f'K={K:.14f}; I0(pi/4)={1-math.log(2):.14f}')


if __name__=='__main__':
    check()
