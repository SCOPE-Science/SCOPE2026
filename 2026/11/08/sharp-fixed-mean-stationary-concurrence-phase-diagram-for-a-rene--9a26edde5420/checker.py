"""Reproduce finite checks for a renewal-reset two-qubit concurrence envelope.

Requires Python 3, numpy and scipy. These finite tests supplement, but do
not replace, the analytic proof of the unrestricted probability-law result.
"""
import math
import numpy as np
from scipy.optimize import brentq, linprog

TOL = 3e-9
checks = 0

def check(cond, detail):
    global checks
    if not cond:
        raise AssertionError(detail)
    checks += 1

x0 = brentq(lambda z: math.tan(z / 2) - z, 2, 3)
q0 = (1 - math.cos(x0)) / x0
check(abs(x0 - 2.33112237041442) < 1e-11, 'critical tangency')
check(abs(q0 - math.sin(x0)) < 1e-12, 'tangent slope')

def ceiling(m):
    return q0 if m <= x0 else ((1-math.cos(m))/m if m <= math.pi else 2/m)

def concurrence_of_law(times, weights, omega=1.):
    times = np.asarray(times, dtype=float)
    weights = np.asarray(weights, dtype=float)
    assert len(times) == len(weights)
    assert np.all(times > 0) and np.all(weights >= 0)
    check(abs(sum(weights)-1) < 1e-10, 'probability normalization')
    mean = float(weights @ times)
    f = 1 - np.cos(omega*times)
    C = float(weights @ f) / (omega*mean)
    # Independent stationary density calculation from average of unitary paths.
    c = float(weights @ np.sin(omega*times)) / (omega*mean)
    rho = np.zeros((4,4), dtype=complex)
    rho[0,0] = (1+c)/2
    rho[3,3] = (1-c)/2
    rho[0,3] = 1j*C/2
    rho[3,0] = -1j*C/2
    sy = np.array([[0,-1j],[1j,0]])
    spinflip = np.kron(sy,sy)
    rr = rho @ spinflip @ rho.conj() @ spinflip
    eig = np.sort(np.sqrt(np.clip(np.linalg.eigvals(rr).real,0,None)))[::-1]
    wootters = max(0,float(eig[0]-sum(eig[1:])))
    check(abs(wootters-C) < 1e-7, 'Wootters-concurrence calculation')
    check(C >= -TOL and C <= 1+TOL, 'physical range')
    check(C <= ceiling(omega*mean)+TOL, 'universal envelope')
    return C

rng = np.random.default_rng(104718)
for _ in range(300):
    scale = 10**rng.uniform(-1.8,1.8)
    size = int(rng.integers(1,9))
    times = scale*np.exp(rng.normal(size=size))
    weights = rng.dirichlet(np.ones(size))
    concurrence_of_law(times,weights,omega=10**rng.uniform(-1,1))

for m in [0.01,0.2,0.5,1,2,x0,2.5,3,math.pi,3.5,5,2*math.pi,10,20,45]:
    c = concurrence_of_law([m],[1.])
    if x0-1e-9 <= m <= math.pi+1e-9:
        check(abs(c-ceiling(m)) < TOL, 'deterministic optimal region')
    if m > math.pi:
        k = int(math.floor((m/math.pi-1)/2))
        x1 = (2*k+1)*math.pi
        x2 = x1+2*math.pi
        p = (x2-m)/(x2-x1)
        p = min(1,max(0,p))
        c2 = concurrence_of_law([x1,x2],[p,1-p])
        check(abs(c2-ceiling(m)) < TOL, 'odd-half-period optimizer')
    if m >= 2*math.pi:
        k = int(math.floor(m/(2*math.pi)))
        t1,t2=2*math.pi*k,2*math.pi*(k+1)
        p=(t2-m)/(t2-t1)
        c0=concurrence_of_law([t1,t2],[p,1-p])
        check(abs(c0) < TOL, 'full-period zero concurrence')

for m in [0.1,0.4,1.,2.,x0-.0001]:
    errors=[]
    for epsilon in [0.02,0.002,0.00002]:
        p=(x0-m)/(x0-epsilon)
        c=concurrence_of_law([epsilon,x0],[p,1-p])
        errors.append(ceiling(m)-c)
    check(errors[2]<errors[1]<errors[0], 'strict fast-reset supremum approach')
    check(errors[-1]<2e-4, 'fast-reset limiting supremum')

for m in [0.1,1,3,6]:
    cseq=[]
    for k in [10,100,1000]:
        eps=1e-5
        hi=2*math.pi*k
        p=(hi-m)/(hi-eps)
        cseq.append(concurrence_of_law([eps,hi],[p,1-p]))
    check(max(cseq)<3e-5, 'approachable zero lower endpoint')

# Grid-based primal LP independent of the supporting-line derivation.
xs=np.unique(np.r_[1e-8,np.linspace(0.004,75,4001),x0,math.pi,3*math.pi,5*math.pi,7*math.pi,9*math.pi,11*math.pi])
for m in [0.2,0.7,1,2,2.4,2.9,math.pi,4,6,10,20]:
    res=linprog(-(1-np.cos(xs)), A_eq=np.vstack((np.ones(len(xs)),xs)), b_eq=[1,m], bounds=(0,None),method='highs')
    check(res.success, 'LP solver success')
    check(-1e-9 <= ceiling(m)-(-res.fun/m) < 0.00002, 'LP match analytic supremum')

# Poisson resetting at rate 1/mean: dimensionless concurrence m/(1+m^2).
for m in [0.1,0.3,1,2,5,10]:
    check(m/(1+m*m)<=ceiling(m)+1e-12, 'exponential-clock benchmark')

print('PASS:',checks,'finite assertions; x0=',format(x0,'.15g'),'peak=',format(q0,'.15g'))
