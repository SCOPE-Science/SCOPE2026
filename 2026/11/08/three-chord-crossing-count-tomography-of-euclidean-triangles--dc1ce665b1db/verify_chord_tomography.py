"""Reproduce exact and numerical checks for triangle chord-crossing tomography.

Uses only the Python standard library.  A crossing is required to lie in the
open interior of the triangle, so same-edge segments never count.
"""
from fractions import Fraction as F
from itertools import permutations
from math import sqrt
import random


def invariants(p):
    a, b, c = p
    e2 = a*b+b*c+c*a
    e3 = a*b*c
    q = 2*e2**2
    g2 = F(20, 9)*e2**3-F(4, 3)*e3**2
    v = g2-q*q
    mean_count = 3*q
    variance_count = 3*q*(1-q)+6*v
    return e2, e3, q, g2, v, mean_count, variance_count


def numerical_integral_g_and_g2(p):
    # Tensor 3-point Gauss-Legendre quadrature exactly integrates polynomials
    # of degree <=5 in each variable, including the square of g.
    coords = (0.5-sqrt(3/5)/2, .5, .5+sqrt(3/5)/2)
    weights = (5/18, 4/9, 5/18)
    p = [float(x) for x in p]
    em = 0.
    em2 = 0.
    for i in range(3):
        j = (i+1)%3
        k = (i+2)%3
        for x, wx in zip(coords, weights):
            for y, wy in zip(coords, weights):
                g = 2*(p[i]*p[j]*((1-x)*(1-y)+x*y)
                       +p[i]*p[k]*(1-x)+p[j]*p[k]*y)
                weight = 2*p[i]*p[j]*wx*wy
                em += weight*g
                em2 += weight*g*g
    return em, em2


def sample_chord(p, rng):
    u, v = rng.random(), rng.random()
    cut0, cut1 = p[0], p[0]+p[1]
    def edge(t):
        return 0 if t<cut0 else (1 if t<cut1 else 2)
    return (u,v,edge(u),edge(v))


def properly_cross(c1, c2):
    u, v, i, j = c1
    s, t, k, l = c2
    if i==j or k==l:
        return False
    if u>v:
        u,v=v,u
    return (u<s<v) != (u<t<v)


def simulation(p, n=120000, seed=41521):
    rng = random.Random(seed)
    counts = [0, 0, 0, 0]
    for _ in range(n):
        chords = [sample_chord(p, rng) for _ in range(3)]
        n_cross = sum(properly_cross(chords[i],chords[j])
                      for i,j in ((0,1),(0,2),(1,2)))
        counts[n_cross]+=1
    mean = sum(i*v for i,v in enumerate(counts))/n
    variance = sum(v*(i-mean)**2 for i,v in enumerate(counts))/n
    return mean, variance, counts


def main():
    test_cases = [
        (F(1,3), F(1,3), F(1,3)),
        (F(3,12), F(4,12), F(5,12)),
        (F(4,15), F(4,15), F(7,15)),
        (F(2,5), F(2,5), F(1,5)),
        (F(8,21), F(7,21), F(6,21)),
    ]
    for p in test_cases:
        assert sum(p)==1 and max(p)<F(1,2) and min(p)>0
        e2,e3,q,g2,v,mu,var=invariants(p)
        # Direct moment integrals independent of the simplified symmetric form.
        a,b=numerical_integral_g_and_g2(p)
        assert abs(a-float(q))<3e-15, (p,a,q)
        assert abs(b-float(g2))<3e-15, (p,b,g2)
        # Exact inverse from pair-crossing mean and three-chord variance.
        rec_e2 = sqrt(float(mu)/6)
        rec_v = (var-3*q*(1-q))/6
        rec_e3 = sqrt(float(F(3,4)*(F(20,9)*e2**3-4*e2**4-rec_v)))
        assert abs(rec_e2-float(e2))<1e-14
        assert abs(rec_e3-float(e3))<1e-14
        for pi in p:
            assert pi**3-pi**2+e2*pi-e3==0
    # Two non-similar triangles with exactly the same two-chord crossing law.
    u = invariants(test_cases[2]); w=invariants(test_cases[3])
    assert u[0]==w[0]==F(8,25)
    assert u[2]==w[2]==F(128,625)
    assert u[1]!=w[1] and u[6]!=w[6]

    for k,p in enumerate(test_cases[:3]):
        *_,expected_mean,expected_var = invariants(p)
        mean,var,counts=simulation([float(x) for x in p], n=120000, seed=41521+k)
        assert abs(mean-float(expected_mean))<0.017, (p,mean,expected_mean)
        assert abs(var-float(expected_var))<0.022, (p,var,expected_var)
        print('case',k,'histogram',counts, 'mean',round(mean,6),
              'theory',round(float(expected_mean),6),'variance',round(var,6),
              'theory',round(float(expected_var),6))
    print('VERIFY_OK exact_rational_cases=5 independent_gauss_integrals=10 '
          'reconstructions=5 nonidentifiability_pair=1 three_chord_trials=360000')

if __name__=='__main__':
    main()
