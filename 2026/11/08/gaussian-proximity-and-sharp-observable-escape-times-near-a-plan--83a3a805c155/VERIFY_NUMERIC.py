"""Numerical checks of a planar observable first-exit asymptotic.

Requires Python 3, scipy, and NumPy. These finite tests supplement,
not replace, the analytic proof of the asymptotic theorem.
"""
from math import exp, log, sqrt
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq


def direct_exit(log_inv_epsilon, eta, threshold):
    epsilon = exp(-log_inv_epsilon)
    assert epsilon * abs(eta) < threshold
    energy = epsilon + log_inv_epsilon + eta * eta / 2

    def energy_at_exit(z):
        return z*z/2 + log(z/threshold) + threshold/z - energy

    # The relevant large root has x=threshold/z well below 1.
    z = brentq(energy_at_exit, sqrt(energy), 3*sqrt(energy)+4)

    def flow(_, state):
        logx, y = state
        return (-y, exp(logx)-1)

    def event(_, state):
        return -exp(state[0])*state[1]-threshold
    event.terminal = True
    event.direction = 1
    sol = solve_ivp(flow, (0, 4*sqrt(energy)+abs(eta)+10),
                    (-log_inv_epsilon, eta), events=event,
                    atol=2e-14, rtol=2e-12, max_step=0.045)
    assert sol.success and len(sol.t_events[0]) == 1
    tau = float(sol.t_events[0][0])
    logx_end,y_end = sol.y_events[0][0]
    x_end = exp(logx_end)
    assert y_end < 0 and x_end < 0.4
    assert abs(x_end*abs(y_end)-threshold) < 1e-9
    assert abs(-y_end-z) < 2e-7
    return z, tau


def predicted(log_inv_epsilon, eta, threshold):
    L=log_inv_epsilon
    R=sqrt(2*L)
    return eta+R+(eta*eta+2*log(threshold)-log(2*L))/(2*R)


def verify():
    cases = 0
    for eta in (-1.0, 0.0, 2.0):
        for threshold in (0.25,1.0):
            prior_error = None
            for L in (15.0,30.0,60.0,100.0):
                z,tau=direct_exit(L,eta,threshold)
                assert abs(tau-predicted(L,eta,threshold)) < 0.012
                assert abs((tau-eta-z)-threshold/(z*z)) < 0.0016
                # Check the Gaussian inverted relationship in log form.
                Q=tau-eta
                reconstructed=Q*Q/2+log(Q)-eta*eta/2-log(threshold)
                assert abs(L-reconstructed) < 0.018
                cases+=1
    # Independent quadrature in the y-coordinate for a representative case.
    L, eta, threshold = 30.0, 1.0, 0.7
    z,tau=direct_exit(L,eta,threshold)
    energy=exp(-L)+L+eta*eta/2
    def x_from_y(y):
        a=exp(-energy+y*y/2)
        return brentq(lambda x:x*exp(-x)-a,1e-16,0.5,xtol=5e-17)
    quadrature,_=quad(lambda y:1/(1-x_from_y(y)), -z,eta, epsabs=1e-10)
    assert abs(tau-quadrature)<3e-7
    print(f'VERIFY_OK ODE_first_exits={cases} root_conditions={cases} '
          f'Gaussian_log_inverse={cases} independent_time_quadrature=1')

if __name__=='__main__':
    verify()
