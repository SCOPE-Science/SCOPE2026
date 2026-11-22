"""Independent finite arithmetic checks for the stated high-intensity Poisson fluctuation theorem.
These checks supplement, not replace, the analytic proof of process convergence.
Requires Python 3 and scipy (only for numerical integration).
"""
import math
from scipy.integrate import quad

checks=0
for r in (2.25, 2.5, 3, 4, 7):
    alpha=1/r
    for t in (0.01, 0.25, 1, 5):
        # Beta-prime (Lomax) mark moments and Poisson isometry.
        ew=1/(r-1)
        ew2=2/((r-1)*(r-2))
        mean=(r-1)*quad(lambda v:ew, 0, t**alpha)[0]
        sq=(r-1)**2*quad(lambda v:v*ew2, 0, t**alpha)[0]
        expected_sq=(r-1)/(r-2)*t**(2*alpha)
        assert math.isclose(mean,t**alpha,rel_tol=1e-11)
        assert math.isclose(sq,expected_sq,rel_tol=1e-11)
        checks+=2

# Exact critical truncated second moment (r=2), obtained by tail integration.
def truncated_second(u):
    return 2*(math.log1p(u)+1/(1+u)-1)-u*u/(1+u)**2
for u in (.1,.3,1,4,23,100):
    direct=quad(lambda w:2*w*w/(1+w)**3,0,u,epsabs=1e-10)[0]
    assert abs(direct-truncated_second(u))<1e-9
    checks+=1
for beta in (1e4,1e7,1e11):
    L=math.sqrt(beta*math.log(beta))
    for t in (0.1,1,3):
        qv=quad(lambda v: v*truncated_second(L/v) if v else 0.,0,math.sqrt(t),epsabs=1e-9)[0]/math.log(beta)
        assert 0.35*t <qv<0.9*t,(beta,t,qv)
        checks+=1

# Jacobian identity: the normalized candidate's physical-time jump density
# is y^(-r-1)*(1+t^alpha/(beta^(1/r)*y))^(-r-1).
for r in (1.2,1.5,1.75,1.95):
  alpha=1/r
  for beta in (1,37,100000):
    for t in (.07,.5,2):
      for y in (.03,1,7):
        direct=alpha*r*beta**(1+1/r)*t**(-1-alpha)*(1+beta**(1/r)*y/t**alpha)**(-r-1)
        simplified=y**(-r-1)*(1+t**alpha/(beta**(1/r)*y))**(-r-1)
        assert math.isclose(direct,simplified,rel_tol=5e-12),(r,beta,t,y)
        assert direct<=y**(-r-1)*(1+5e-13)
        checks+=2

print(f'PASS: {checks} numerical identity, moment, critical truncation and Levy-kernel checks.')
print('Limit proofs require the Poisson martingale and Levy-measure arguments in RESULT.md.')
