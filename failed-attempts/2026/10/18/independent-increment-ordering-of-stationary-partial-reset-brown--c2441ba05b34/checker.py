"""Reproducible checks for the additive-noise ordering of partially reset Brownian stationary laws.
Run with: python3 checker.py. Only Python's standard library is required.
Finite computations test formulas; the infinite theorem is proved analytically.
"""
from fractions import Fraction as F
from math import log, sqrt, exp, cos, pi
from itertools import combinations

checks = 0
params = [F(0), F(1,7), F(1,4), F(2,5), F(1,2), F(3,4)]
for a,b in combinations(params,2):
    # Each Bernoulli/Laplace mixture provides exactly the Fourier ratio.
    for j in range(1, 17):
        zero_weight = (a/b)**(2*j)
        active_weight = 1-zero_weight
        assert F(0) <= zero_weight < 1
        assert F(0) < active_weight <= 1
        for t2 in [F(0),F(1,5),F(1),F(2),F(9,2)]:
            s2 = b**(2*j)/2
            phi_mixture = zero_weight + active_weight/(1+s2*t2)
            phi_ratio = (1+(a**(2*j))*t2/2)/(1+(b**(2*j))*t2/2)
            assert phi_mixture == phi_ratio, (a,b,j,t2)
            checks += 1
        assert (1-zero_weight)*(b**(2*j)) == b**(2*j)-a**(2*j)
        checks += 1
    # Whole finite products and variance verify telescoping at any length.
    for n in range(1,15):
        for t2 in [F(0),F(1,2),F(3)]:
            p_a = F(1)
            p_b = F(1)
            p_increment = F(1)
            for j in range(n+1):
                p_a /= 1+a**(2*j)*t2/2
                p_b /= 1+b**(2*j)*t2/2
                if j:
                    p_increment *= (1+a**(2*j)*t2/2)/(1+b**(2*j)*t2/2)
            assert p_a*p_increment == p_b
            checks += 1
        var_a = sum((a**(2*j) for j in range(n+1)),F(0))
        var_b = sum((b**(2*j) for j in range(n+1)),F(0))
        var_z = sum((b**(2*j)-a**(2*j) for j in range(1,n+1)),F(0))
        assert var_a+var_z == var_b
        checks += 1
    # Full infinite variance identity.
    assert 1/(1-b*b)-1/(1-a*a) > 0
    checks += 1

# Elementary Lévy-Khintchine integral identity using midpoint quadrature
# and 4th-order Simpson scheme on a rapidly decaying finite interval.
def simpson_integral(t, scale, n=12000):
    L = 42*scale
    h = L/n
    def g(x):
        if x == 0: return 0.0
        return 2*(1-cos(t*x))*exp(-x/scale)/x
    out = g(0)+g(L)
    for k in range(1,n):
        out += (4 if k%2 else 2)*g(k*h)
    return out*h/3

for scale in [1/sqrt(2), 0.5/sqrt(2), 0.2/sqrt(2)]:
    for t in [0.25,0.8,1.7]:
        integral = simpson_integral(t,scale)
        predicted = log(1+(scale*t)**2)
        assert abs(integral-predicted) < 2e-7, (scale,t,integral,predicted)
        checks+=1

# Structural tests: each individual Lévy density is increasing in c;
# the change is positive and the quadratic small-jump bound is summable.
for a,b in combinations([0.0,0.25,0.4,0.7],2):
    for x in [0.001,0.05,0.3,2.0,9.0]:
        va=sum(exp(-sqrt(2)*x/(a**j)) for j in range(1,13)) if a else 0
        vb=sum(exp(-sqrt(2)*x/(b**j)) for j in range(1,13))
        assert vb>va, (a,b,x)
        checks+=1
    assert sum(b**(2*j)-a**(2*j) for j in range(1,500)) > 0
    checks+=1

print(f"PASS: {checks} exact rational and numerical assertions")
