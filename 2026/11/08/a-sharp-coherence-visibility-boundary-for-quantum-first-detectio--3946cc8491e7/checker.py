"""Independent numerical checks of a two-level first-detection survival-order theorem.

Run: python checker.py
Requires numpy, scipy. Results are diagnostic; proof is analytic in RESULT.md.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.signal import residue
from scipy.linalg import expm


def threshold():
    root = brentq(lambda x: math.tan(x)-x, 4.4, 4.6, xtol=1e-14)
    return root, 1/(1-math.sin(root)/root)


def survival_gap_laplace(s, a, omega, rate):
    q = s + rate
    return rate*(q*q+(1-a)*omega*omega)/(q*(s*(q*q+omega*omega)+rate*a*omega*omega/2))


def survival_gap(t, a, omega, rate):
    # Inverse Laplace transform using poles and residues of the exact rational function.
    num = rate*np.array([1, 2*rate, rate*rate+(1-a)*omega*omega])
    den = np.polymul([1, rate], [1, 2*rate, rate*rate+omega*omega, rate*a*omega*omega/2])
    residues, poles, direct = residue(num, den)
    assert not len(direct)
    return float(np.real(np.sum(residues*np.exp(poles*t))))


def double_laplace_via_integral(s,a,omega,r):
    # Construct from independent exponential no-detection/success kernels.
    L = quad(lambda t: r*math.exp(-(r+s)*t)*(1-a*math.sin(omega*t/2)**2),0,np.inf,epsabs=1e-12)[0]
    K = quad(lambda t: r*math.exp(-(r+s)*t)*a*math.sin(omega*t/2)**2,0,np.inf,epsabs=1e-12)[0]
    return (L-K)/((s+r)*(1-L))


def main():
    count=0
    x0, ac=threshold()
    assert 4.49<x0<4.50
    assert abs(ac-0.8215349763788107)<1e-12
    count+=2
    # A general Hermitian two-state Hamiltonian gives exactly the claimed visibility parameter.
    for delta,g in [(0,1),(.6,1),(2,1),(3,.5)]:
        H=np.array([[delta/2,g],[g,-delta/2]],dtype=complex)
        omega=math.sqrt(delta*delta+4*g*g)
        a=4*g*g/(omega*omega)
        for t in [.03,.4,2.1]:
            p=abs(expm(-1j*H*t)[1,0])**2
            assert abs(p-a*math.sin(omega*t/2)**2)<3e-13
            count+=1
    for rate in [.07,.4,1.,3.]:
        for a in [.15,.65,.8,.95,1.]:
            for s in [.1,.55,2.3]:
                lhs=survival_gap_laplace(s,a,1.,rate)
                rhs=double_laplace_via_integral(s,a,1.,rate)
                assert math.isclose(lhs,rhs,rel_tol=1e-9,abs_tol=1e-10), (rate,a,s,lhs,rhs)
                assert lhs>0
                count+=2
    # For subcritical visibility the analytic convolution density is nonnegative.
    for a in [.1,.5,.8,ac]:
        for x in np.linspace(.0001,35,300):
            kernel=(1-a)*x+a*math.sin(x)
            assert kernel>-2e-12, (a,x,kernel)
            count+=1
    # Direct rational inverse: positive survival-order gap throughout various finite rates.
    for a in [.45,.77,ac]:
        for r in [.05,.3,2.,7.]:
            for t in np.linspace(.05,15,160):
                val=survival_gap(t,a,1.,r)
                assert val>-2e-9, (a,r,t,val)
                count+=1
    # Strong coherent mixing and weak Poisson probing yield survival crossing.
    for r in [.1,.05,.025,.0125]:
        delta=survival_gap(x0,1.,1.,r)
        assert delta<0, (r,delta)
        # Sharp small-r coefficient is sin(x0) (omega=1).
        assert abs(delta/r-math.sin(x0)) < 5.0*r, (r,delta/r)
        assert survival_gap(.03,1.,1.,r)>0
        count+=3
    # The moment ordering survives where pointwise survival ordering fails.
    for a in [.2,.7,.99,1.]:
        for r in [.1,.4,2.]:
            ET=2*(r*r+1)/(a*r)
            ER=2/r
            assert ET>ER
            count+=1
    print(f"PASS {count} deterministic assertions; root={x0:.14f}; threshold={ac:.14f}")
    for a in [.8,1.]:
        print(f"a={a:.2f}: survival difference at r=0.1,t={x0:.5f} is {survival_gap(x0,a,1.,.1):+.8f}")

if __name__=='__main__': main()
