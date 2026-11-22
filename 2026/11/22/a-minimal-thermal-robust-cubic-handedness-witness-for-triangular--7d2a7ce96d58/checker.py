"""Reproducible checks of the triangular active-swimmer stationary moment identity.
Only standard Python packages numpy and sympy are needed. Standalone.
"""
import math
import numpy as np
import sympy as sp


def exact_prediction(k,v,u,d):
    s=u+d
    delta=u-d
    real=(k+sp.Rational(3,2)*s)*(2*k+sp.Rational(3,2)*s)+sp.Rational(3,4)*delta**2
    imag=sp.sqrt(3)*k*delta/2
    return sp.simplify(2*v**3/(k*(real+sp.I*imag)))


def matrix_prediction(k,v,u,d):
    w=sp.Rational(-1,2)+sp.I*sp.sqrt(3)/2
    Q=sp.zeros(3)
    for j in range(3):
        Q[j,j]=-u-d
        Q[j,(j+1)%3]=u
        Q[j,(j-1)%3]=d
    P=sp.diag(1,w,w*w)
    m=sp.Matrix([sp.Rational(1,3)]*3)
    for n in (1,2,3):
        m=(n*k*sp.eye(3)-Q.T).inv()*n*v*P*m
    return sp.simplify(sum(m))


def check():
    choices=[(sp.Rational(5,4),sp.Rational(7,5),sp.Rational(3,4),sp.Rational(1,6)),
             (sp.Integer(1),sp.Integer(1),sp.Rational(1,4),sp.Rational(2,3)),
             (sp.Rational(9,10),sp.Rational(11,10),sp.Rational(3,5),sp.Rational(3,5)),
             (sp.Rational(3,2),sp.Rational(4,5),sp.Integer(2),sp.Integer(0))]
    for x in choices:
        assert sp.simplify(exact_prediction(*x)-matrix_prediction(*x))==0,x
    rng=np.random.default_rng(20261118)
    for i in range(80):
        k=float(rng.uniform(0.25,3)); v=float(rng.uniform(.2,3))
        u=float(rng.uniform(.04,3)); d=float(rng.uniform(.04,3))
        arr=np.array([[ -u-d,u,d],[d,-u-d,u],[u,d,-u-d]],dtype=complex)
        omega=np.exp(2j*np.pi/3)
        T=np.ones(3,dtype=complex)/3
        for n in (1,2,3):
            T=np.linalg.solve(n*k*np.eye(3)-arr.T,n*v*np.array([1,omega,omega**2])*T)
        expected=complex(exact_prediction(k,v,u,d))
        assert abs(T.sum()-expected)<1e-10*max(1,abs(expected)),i
        assert abs(T.sum().imag)<1e-9 or np.sign(T.sum().imag)==-np.sign(u-d)
    # Separate backward renewal simulation from first principles, no moment matrix.
    k,v,u,d=1.3,1.2,.9,.2
    n=180000
    heading=rng.integers(0,3,size=n)
    total=np.zeros(n)
    Z=np.zeros(n,dtype=complex)
    s=u+d
    for step in range(150):
        run=rng.exponential(1/s,size=n)
        attenuation=np.exp(-k*total)
        Z+=v/k*attenuation*(-np.expm1(-k*run))*np.exp(2j*np.pi*heading/3)
        total+=run
        step_chance=rng.random(n)<u/s
        heading=(heading+np.where(step_chance,-1,1))%3
        if np.max(np.exp(-k*total))<1e-13: break
    estimated=np.mean(Z**3)
    predicted=complex(exact_prediction(k,v,u,d))
    assert abs(estimated-predicted)<.025*max(1.,abs(predicted)),(estimated,predicted)
    assert np.sign(estimated.imag)==np.sign(predicted.imag)
    # Gaussian-convolution invariance of complex cubic moment via independent noise.
    thermal_D=0.12
    G=np.sqrt(thermal_D/k)*(rng.normal(size=n)+1j*rng.normal(size=n))
    therm=np.mean((Z+G)**3)
    # Absolute Monte Carlo error scales with noise; use conservative sampling interval.
    assert abs(therm-predicted)<.035,(therm,predicted)
    print('PASS: four exact symbolic 3-state matrix cases; 80 independent numeric matrix cases;')
    print('PASS: 180000-cycle backward renewal simulation and independent isotropic-noise check')
    print('sample third moment:', estimated, 'predicted:', predicted, 'thermal sample:',therm)

if __name__=='__main__':
    check()
