"""Independent reproducibility checks for a two-state, harmonic run-and-tumble cusp.

Requires Python 3, NumPy and SciPy. Numerical tests do not replace the proof.
"""
import warnings
import numpy as np
from scipy.special import roots_jacobi, hyp1f1
from scipy.integrate import quad
from scipy.optimize import brentq, root


def stationary_nodes(a, b, n=200):
    """Jacobi quadrature for (1-y)^(a-1)(1+y)^(b-1), -1<y<1."""
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', RuntimeWarning)
        return roots_jacobi(n, a-1, b-1)


def f_derivative_equations(x, s, a, b):
    y, w = stationary_nodes(a, b)
    z = y-x
    w = w*np.exp(-z*z/(2*s))
    return np.array([np.dot(w, z), np.dot(w, z*z-s)])


def critical_ell(ell):
    def eq(t):
        return hyp1f1(.5, ell+.5, -t) - t/(ell+.5)*hyp1f1(1.5, ell+1.5, -t)
    t = brentq(eq, .001, 100, xtol=1.e-13)
    s = 1/(2*t)
    y,w = stationary_nodes(ell,ell,300)
    w = w*np.exp(-t*y*y)
    w = w/sum(w)
    # Endpoint logarithmic singularity makes finite Jacobi summation slow;
    # resolve this separate coefficient by adaptive singular quadrature.
    def base(z):
        return np.exp(-t*z*z)*(1-z*z)**(ell-1)
    den = quad(base,0,1,epsabs=1e-10,epsrel=1e-10,limit=500)[0]
    num = quad(lambda z:z*np.arctanh(z)*base(z),0,1,
               epsabs=1e-10,epsrel=1e-10,limit=500)[0]
    H = num/den
    A = (3*s*H/(1-ell))**(1/3)
    return t,s,A,w,y


def check():
    count=0
    for ell in (.4,.5,.77):
        t,sc,A,w,y=critical_ell(ell)
        assert np.isfinite([t,sc,A]).all() and t>0 and sc>0 and A>0
        count+=3
        # Kummer-derived exact critical weighted moment identities.
        assert abs(np.dot(w,y*y)-sc)<1e-9
        assert abs(np.dot(w,y**4)-(2*ell+1)*sc**2)<1e-9
        count+=2
        for eps in (1e-3,-1e-3,1e-4,-1e-4):
            a,b=ell+eps,ell-eps
            direction=np.sign(eps)
            z0=direction*A*abs(eps)**(1/3)
            s0=sc-A*A*abs(eps)**(2/3)
            sol=root(lambda z:f_derivative_equations(z[0],z[1],a,b),[z0,s0],tol=1e-11)
            assert sol.success or np.linalg.norm(sol.fun)<2e-12, (ell,eps,sol.message)
            xx,ss=sol.x
            assert 0<ss<sc and np.sign(xx)==direction
            assert np.linalg.norm(f_derivative_equations(xx,ss,a,b))<2e-12
            assert abs(xx / (direction*A*abs(eps)**(1/3)) - 1)<.06
            assert abs((sc-ss)/(A*A*abs(eps)**(2/3)) - 1)<.07
            count+=5
            # Independently compare Jacobi-weight stationary beta moments with the generator equations.
            yn,wn=stationary_nodes(a,b)
            wn=wn/sum(wn)
            mu=np.dot(wn,yn)
            second=np.dot(wn,yn*yn)
            exact_mean=(b-a)/(a+b)
            exact_second=(1+(b-a)*exact_mean)/(1+a+b)
            assert abs(mu-exact_mean)<2e-9
            assert abs(second-exact_second)<2e-9
            count+=2
        print(f'ell={ell:.2f} critical variance={sc:.12f} cusp A={A:.12f}')
    t,s,A,_,_=critical_ell(.5)
    assert abs(s-.3164643403484473)<1e-11
    assert abs(A-1.0116863052989679)<2e-8
    count+=2
    print(f'PASS: {count} deterministic numerical checks; finite checks are not a theorem')

if __name__ == '__main__':
    check()
