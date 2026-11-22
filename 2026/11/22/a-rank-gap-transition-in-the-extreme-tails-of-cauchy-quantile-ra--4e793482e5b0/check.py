"""Supplementary finite calculations for Cauchy rank-spacing endpoint constants.

Requires numpy and scipy. This is not a substitute for the analytical proof.
"""
from math import factorial, pi
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc, t as student_t

checks = 0

def require(cond, label):
    global checks
    if not cond:
        raise AssertionError(label)
    checks += 1


def adjacent_density(m, j):
    c = factorial(m) / (factorial(j - 1) * factorial(m - j - 1)) / pi
    q, error = quad(lambda u: (u ** (j - 1)) * ((1-u) ** (m-j-1)) * np.sin(pi*u)**2,
                    0., 1., epsabs=1e-12)
    require(error < 1e-10, f'quadrature error {m},{j}')
    return c*q

for m in range(3, 9):
    for j in range(1, m):
        d = adjacent_density(m, j)
        require(d > 0, 'positive density')
        require(abs(d - adjacent_density(m, m-j)) < 1e-11, 'reflection symmetry')

require(abs(adjacent_density(3, 1) - 3/(2*pi)) < 1e-12, 'left adjacent density')
require(abs(adjacent_density(3, 2) - 3/(2*pi)) < 1e-12, 'right adjacent density')
A4=4/pi*(adjacent_density(3, 1)+adjacent_density(3, 2))
require(abs(A4-12/pi**2)<1e-12,'four-rank logarithmic coefficient')

# Exact Cauchy-squared integrals (also direct numerical verification).
f=lambda x:1/(pi*(1+x*x))
a=quad(lambda x:f(x)**2,-np.inf,np.inf,epsabs=1e-12)[0]
b=quad(lambda x:x*x*f(x)**2,-np.inf,np.inf,epsabs=1e-12)[0]
require(abs(a-1/(2*pi))<1e-11, 'squared density integral')
require(abs(b-1/(2*pi))<1e-11, 'weighted squared density integral')
Cright=12*a*b
require(abs(Cright-3/pi**2)<1e-11, 'four-rank right-tail coefficient')

# Reproducible numerical integral comparisons: no claim these are limits/proofs.
# For the right endpoint, squared-Cauchy importance distribution is t_3/sqrt(3).
u=qmc.Sobol(d=4,scramble=True,seed=789001).random_base2(16)
y=student_t.ppf(u[:,0],3)/np.sqrt(3)
z=student_t.ppf(u[:,1],3)/np.sqrt(3)
low=np.minimum(y,z); high=np.maximum(y,z); length=high-low
q=np.sqrt(u[:,2]); aa=1-q; bb=q*u[:,3]
for eps in [0.02,0.01]:
    ratio=((1+low**2)/(1+(low+eps*length*aa)**2)
           *(1+high**2)/(1+(high-eps*length*bb)**2))
    estimate=(3/pi**2)*np.mean((length**2/2)*ratio)
    require(abs(estimate-3/pi**2)<0.025, 'right endpoint quadrature')

# Separated ranks: finite reciprocal span of two nonadjacent order statistics.
u=qmc.Sobol(d=4,scramble=True,seed=2026).random_base2(17)
sample=np.tan(pi*(u-0.5));sample.sort(axis=1)
inverse_mean=np.mean(1/(sample[:,3]-sample[:,1]))
require(0.58 < inverse_mean < 0.76, 'four-sample reciprocal two-rank span')

print(f'{checks} supplementary checks passed')
print(f'four-rank left coefficient: {A4:.14f}')
print(f'four-rank right coefficient: {Cright:.14f}')
print(f'five-sample separated-rank linear coefficient estimate: {10/pi*inverse_mean:.7f}')
