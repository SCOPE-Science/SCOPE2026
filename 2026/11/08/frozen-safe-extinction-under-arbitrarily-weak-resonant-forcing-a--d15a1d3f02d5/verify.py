"""Standalone corroborative checks of small-amplitude threshold separation."""
import math
import numpy as np
from scipy.integrate import solve_ivp

r, K, a, b, m = 1.2, 6.0, 1.1, 0.32, 0.45
s, u, v = 0.3, 1.0, 1.0
n = m/(a*b)
p = r*(1-n/K)/a
alpha = r*n/K
beta = a*n
gamma = a*b*p
d = beta*gamma
q = math.sqrt(d-alpha**2/4)
c = n*(1-n/K)
kap = (1-n/K)/a
H = kap/math.tanh(math.pi*alpha/(4*q))
w = math.sqrt(d)
assert 0 < alpha**2 < 4*d
assert (2/math.e)*s*c/alpha < u < s*c/alpha
assert v > s*H

checks = 0
# Independent integration of the exact first-order perturbation equations.
from scipy.linalg import expm
J = np.array([[-alpha,-beta],[gamma,0.0]])
for t in np.linspace(.01,25,79):
    x=(expm(J*t)@np.array([0.,-1./beta]))[0] # not needed for step
    step_N = c*math.exp(-alpha*t/2)*math.sin(q*t)/q
    B=np.array([c,0.0])
    step=np.linalg.solve(J,(expm(J*t)-np.eye(2))@B)
    assert abs(step[0]-step_N)<2e-12
    checks += 1


def integrate_case(eps, frozen=None):
    A=eps*s; na=n-eps*u; pa=p-eps*v
    def rhs(t,z):
        N,P=z
        rr=r+(A*math.sin(w*t) if frozen is None else A*frozen)
        return (rr*N*(1-N/K)-a*N*P,(a*b*N-m)*P)
    sol=solve_ivp(rhs,(0,120),(n,p),rtol=2e-10,atol=2e-12,max_step=.09,dense_output=True)
    assert sol.success
    grid=np.linspace(0,120,6001)
    Z=sol.sol(grid)
    assert min(Z[1])>pa
    if frozen is None:
        good=np.where(Z[0]<na)[0]
        assert good.size > 0
        tc=grid[good[0]]
        # A genuine down-crossing at this grid resolution.
        assert Z[0,good[0]-1]>=na
        assert rhs(tc,Z[:,good[0]])[0]<0
        return tc
    else:
        assert min(Z[0])>na
        return float(min(Z[0]-na))

for eps in (.02,.008,.002):
    tc=integrate_case(eps)
    for h in np.linspace(-1,1,13):
        margin=integrate_case(eps,h)
        checks+=1
    checks+=1
print('VERIFY_OK', 'linear_step_checks=79', 'frozen_profiles=39', 'forced_crossings=3', 'verified_total=',checks,
      'analytic_coth_bound=',round(H,10), 'last_crossing_t=',round(tc,5))
