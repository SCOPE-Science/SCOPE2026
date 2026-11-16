"""Finite tests for a five-node circle Bernstein covariance calculation.
Only standard Python 3 is needed. Finite checks do not replace the proof.
"""
from math import pi, cos, comb, factorial

def polynomial(nodes, m):
    coeff = [0.0] * 5
    for j, node in enumerate(nodes):
        y = cos(m * node)
        for r in range(5 - j):
            coeff[j+r] += comb(4,j)*comb(4-j,r)*(-1)**r*y
    return coeff

def direct_coefficient(coeff,k):
    if k == 0:
        return 2*sum(coeff[j]/(j+1) for j in range(5))
    der1_0=coeff[1]
    der1_1=sum(j*coeff[j] for j in range(1,5))
    der3_0=6*coeff[3]
    der3_1=6*coeff[3]+24*coeff[4]
    z=pi*k
    return 2*(((-1)**k*der1_1-der1_0)/z**2-(((-1)**k*der3_1-der3_0))/z**4)

def predicted_coefficient(a,m,k):
    s=cos(m*a)
    if k == 0:
        if m%2: return 0.0
        return 2*(2+2*s+(-1)**(m//2))/5
    if (k-m)%2: return 0.0
    z=pi*k
    if m%2: return 16*((1-s)*z*z+12*s-6)/z**4
    e=(-1)**(m//2)
    return 16*((1-s)*z*z+24*s-18*e-6)/z**4

checks=0
for a in [pi/4,pi/3]:
    nodes=[0,a,pi/2,pi-a,pi]
    for m in range(0,65):
        coeff=polynomial(nodes,m)
        for k in range(0,48):
            actual=direct_coefficient(coeff,k)
            predicted=predicted_coefficient(a,m,k)
            assert abs(actual-predicted)<3e-10, (a,m,k,actual,predicted)
            assert actual > -3e-10, (a,m,k,actual)
            checks+=1
bad=direct_coefficient(polynomial([0,pi/6,pi/2,5*pi/6,pi],6),0)
assert abs(bad+0.4)<1e-12, bad
print(f'CHECK_OK coefficient_comparisons={checks} forbidden_node_zero_mode={bad:.12g}')
