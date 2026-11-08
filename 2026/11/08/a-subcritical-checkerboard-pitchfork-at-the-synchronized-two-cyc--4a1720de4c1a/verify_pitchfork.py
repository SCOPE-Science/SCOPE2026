#!/usr/bin/env python3
"""Numerical and exact-algebra checks for the checkerboard pitchfork theorem.
Run: python3 verify_pitchfork.py. Requires Python 3 and NumPy.
The analytic proof, not these finite checks, establishes the theorem.
"""
import math
import numpy as np

checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1

def maps(v, a):
    x, y = v
    return np.array([(1-a)*(2*x*x-1)+a*y,
                     (1-a)*(2*y*y-1)+a*x])

def jac2(v, a):
    return np.array([[4*(1-a)*v[0], a], [a, 4*(1-a)*v[1]]])

def sync(a):
    discriminant = math.sqrt(9*a*a-18*a+5)
    return ((-1-a+discriminant)/(4*(1-a)),
            (-1-a-discriminant)/(4*(1-a)))

def newton_two_step(a, guess):
    z = np.array(guess, dtype=float)
    for _ in range(40):
        z1 = maps(z, a)
        residual = maps(z1, a)-z
        jac = jac2(z1, a) @ jac2(z, a)-np.eye(2)
        delta = np.linalg.solve(jac, residual)
        z -= delta
        if np.max(abs(delta)) < 1e-13:
            break
    assert np.max(abs(maps(maps(z, a), a)-z)) < 2e-12
    return z

def jac_ring(z, a):
    n = len(z)
    mat = np.diag(4*(1-a)*np.array(z))
    for i in range(n):
        mat[i, (i+1) % n] += a/2
        mat[i, (i-1) % n] += a/2
    return mat

a_star = (11-4*math.sqrt(6))/5
u = 1-a_star
p, q = sync(a_star)
alpha0, alpha1 = 4*u*p+a_star, 4*u*q+a_star
beta0, beta1 = 4*u*p-a_star, 4*u*q-a_star
m0coef = 2*u*(alpha1+beta0**2)/(1-alpha0*alpha1)
m1coef = alpha0*m0coef+2*u
B = 4*u*(beta1*m0coef+beta0*m1coef)
K = 8*math.sqrt(6)/B
check(0.2404 < a_star < 0.2405, 'critical coupling enclosure')
check(17.8 < B < 17.81, 'positive cubic coefficient')
check(1.1007 < K < 1.1009, 'squared amplitude coefficient')
check(abs(beta0*beta1-1) < 1e-13, 'critical unit multiplier')
check(-1 < alpha0*alpha1 < 1, 'synchronized stable companion multiplier')
for c in [-1, -0.75, -0.5, 0, 0.5, 0.75, 1]:
    multiplier = (4*u*p+a_star*c)*(4*u*q+a_star*c)
    formula = a_star*a_star*c*c-2*a_star*(1+a_star)*c-4+20*a_star-8*a_star*a_star
    check(abs(multiplier-formula)<1e-12, 'Fourier multiplier identity')
    check(-1 < multiplier <= 1+1e-12, 'critical Fourier bound')
for eps in [1e-3, 1e-4, 1e-5]:
    a = a_star-eps
    p_a, _ = sync(a)
    d0 = math.sqrt(K*eps)
    z = newton_two_step(a, [p_a+d0, p_a-d0])
    z1 = maps(z, a)
    d = (z[0]-z[1])/2
    check(abs(d*d/eps-K)<3, 'amplitude approach')
    check(abs(d*d/eps-K)<3*math.sqrt(eps), 'quantitative amplitude rate')
    check(np.max(abs(maps(maps(z[::-1], a),a)-z[::-1]))<1e-11,
          'swapped companion orbit')
    eigen = np.linalg.eigvals(jac2(z1,a)@jac2(z,a))
    check(sum(abs(x)>1 for x in eigen)==1, 'one unstable 2-colour multiplier')
    check(abs((max(eigen.real)-1)/eps-16*math.sqrt(6))<150*math.sqrt(eps),
          'unstable multiplier linear coefficient')
    for n in [4,6,8,10,12,16]:
        zring = np.array([z[i%2] for i in range(n)])
        zring1 = np.array([z1[i%2] for i in range(n)])
        next_ring = lambda r: (1-a)*(2*r*r-1)+a/2*(np.roll(r,1)+np.roll(r,-1))
        check(np.max(abs(next_ring(zring)-zring1))<1e-13, 'ring first step')
        check(np.max(abs(next_ring(zring1)-zring))<2e-12, 'ring return')
        eig_ring = np.linalg.eigvals(jac_ring(zring1,a)@jac_ring(zring,a))
        check(sum(abs(ev)>1+1e-7 for ev in eig_ring)==1,
              'exactly one ring unstable multiplier')
        check(sum(abs(ev)<1-1e-7 for ev in eig_ring)==n-1,
              'all remaining ring multipliers stable')
        check(max(abs(zring))<1 and max(abs(zring1))<1, 'physical phase cube')
print(f'PASS {checks} checks; a*={a_star:.15f}, B={B:.12f}, K={K:.12f}')
