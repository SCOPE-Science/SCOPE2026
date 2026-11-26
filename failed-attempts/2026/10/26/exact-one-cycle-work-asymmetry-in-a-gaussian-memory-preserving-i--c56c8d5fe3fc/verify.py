"""Finite numerical checks for one-cycle work statistics in a harmonically trapped Gaussian feedback engine.

Requires numpy and scipy. The analytic proof is independent of these checks.
"""
import math
import numpy as np
from scipy import integrate, linalg, special


def closed_covariance(kappa, tau_r, tau_c, tau, gain, sigma2, thermal_var, force_var):
    damping = kappa * tau_r
    rho = math.exp(-tau/tau_r)
    nu = math.exp(-tau/tau_c)
    h = 1-gain
    cross_inf = force_var / (damping * (1/tau_r + 1/tau_c))
    v_inf = thermal_var + cross_inf/kappa
    cross_minus = cross_inf*(1-rho*nu)/(1-h*rho*nu)
    if math.isclose(tau_r, tau_c, rel_tol=1e-12):
        integral_ratio = (tau/tau_r)*rho*rho
    else:
        integral_ratio = (rho*nu-rho*rho)/(1-tau_r/tau_c)
    v_minus = (rho*rho*gain*gain*sigma2 + v_inf*(1-rho*rho)
               -(2*gain*cross_inf/kappa)*integral_ratio/(1-h*rho*nu))/(1-h*h*rho*rho)
    return v_minus, cross_minus


def independent_covariance(kappa,tau_r,tau_c,tau,gain,sigma2,thermal_var,force_var):
    damping = kappa*tau_r
    drift = np.array([[-1/tau_r,1/damping],[0,-1/tau_c]],dtype=float)
    forcing = np.diag([2*thermal_var/tau_r,2*force_var/tau_c])
    free_cov = linalg.solve_continuous_lyapunov(drift,-forcing)
    evolution = linalg.expm(drift*tau)
    added_noise = free_cov-evolution@free_cov@evolution.T
    feedback = np.diag([1-gain,1])
    measurement = np.diag([gain*gain*sigma2,0.])
    periodic = linalg.solve_discrete_lyapunov(evolution@feedback,evolution@measurement@evolution.T+added_noise)
    return periodic[0,0],periodic[0,1]


def work_parameters(kappa,gain,var,sigma2):
    m = kappa*gain*((2-gain)*var-gain*sigma2)/2
    d = (kappa*gain)**2*var*sigma2
    return m,d


def density(w,m,d):
    rad = math.hypot(m,math.sqrt(d))
    return math.exp((m*w-rad*abs(w))/d)*special.k0e(rad*abs(w)/d)/(math.pi*math.sqrt(d))


def check():
    cases = [(1.4,1.1,1.7,0.65,0.65,0.4,0.8,0.9),
             (2,1,2,0.7,1.0,0.5,1,1.3),
             (1,2,2,1.2,0.35,2,0.7,0.1),
             (1,0.8,0.8,0.4,1.8,0.2,2,1),
             (3,0.5,0.9,1.5,0.9,3,0.25,6),
             (0.8,1.1,4.2,0.9,0.1,0.6,0.3,2),
             (1,1,1,1,1,1,1,0.5)]
    checks=0
    for args in cases:
        kappa,tau_r,tau_c,tau,gain,sigma2,thermal_var,force_var=args
        v,c=closed_covariance(*args)
        vn,cn=independent_covariance(*args)
        assert v>0 and np.allclose((v,c),(vn,cn),rtol=1e-11,atol=1e-11), (args,v,c,vn,cn)
        checks+=2
        m,d=work_parameters(kappa,gain,v,sigma2)
        assert d>0
        checks+=1
        term=kappa/2*np.array([[gain*(2-gain)*v,gain*(1-gain)*math.sqrt(v*sigma2)],
                                  [gain*(1-gain)*math.sqrt(v*sigma2),-gain*gain*sigma2]])
        ev=np.linalg.eigvalsh(term)
        assert ev[0]<0<ev[1] and abs(ev.sum()-m)<1e-11 and abs(-4*ev.prod()-d)<1e-11
        checks+=3
        for t in [-0.05,-0.02,0.02,0.05]:
            lhs=(1-2*m*t-d*t*t)**(-0.5)
            rhs=np.prod(1-2*ev*t)**(-0.5)
            assert np.isclose(lhs,rhs,rtol=1e-12,atol=1e-12)
            checks+=1
        norm=integrate.quad(lambda w:density(w,m,d)+density(-w,m,d),0,np.inf,epsabs=1e-10,limit=200)[0]
        assert abs(norm-1)<1e-8,(args,norm)
        checks+=1
        p=0.5+math.atan(m/math.sqrt(d))/math.pi
        pi=integrate.quad(lambda w:density(w,m,d),0,np.inf,epsabs=1e-10,limit=200)[0]
        assert abs(p-pi)<1e-8,(args,p,pi)
        checks+=1
        for w in [.1,.4,1]:
            ratio=density(w,m,d)/density(-w,m,d)
            assert abs(math.log(ratio)-2*m*w/d)<1e-10
            checks+=1
        var_work=2*m*m+d
        moments=(3*(ev[0]**2+ev[1]**2)+2*ev[0]*ev[1])-(ev[0]+ev[1])**2
        assert abs(var_work-moments)<1e-10,(var_work,moments)
        checks+=1
    # symmetric case has exact zero mean and the density is even
    v=1.7
    sigma2=0.3
    g=2*v/(v+sigma2)
    m,d=work_parameters(1,g,v,sigma2)
    assert abs(m)<1e-14 and abs(density(0.5,m,d)-density(-0.5,m,d))<1e-13
    checks+=2
    print('PASS',checks,'deterministic numerical and algebraic comparisons')

if __name__=='__main__':
    check()
