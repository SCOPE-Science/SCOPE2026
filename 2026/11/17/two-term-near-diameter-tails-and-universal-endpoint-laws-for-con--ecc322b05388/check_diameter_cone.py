#!/usr/bin/env python3
"""Independent numerical checks of near-diametral convex-polytope cone laws.
Requires numpy and scipy. Uses reproducible random generators."""
import math
import numpy as np
from scipy.integrate import quad


def box_coefficient(sides):
    x = np.asarray(sides, float)
    d = len(x)
    D2 = float(np.dot(x, x))
    V = float(np.prod(x))
    return (2.0**d * D2**d)/(math.factorial(2*d) * V**4)


def box_second_ratio(sides):
    sides=np.asarray(sides, float)
    d=len(sides)
    D=float(np.linalg.norm(sides))
    return 3*D/(2*d+1)*float(np.sum(sides**(-2))) - d/D


def rectangle_tail_exact(a, b, eps):
    D = math.hypot(a, b)
    rr = (D - eps)**2
    tmax = a - math.sqrt(rr - b*b)
    def integrand(t):
        h = math.sqrt(max(0, rr-(a-t)**2))
        zmax = b-h
        return 2*t*zmax*zmax/(a*a*b*b)
    return quad(integrand, 0.0, tmax, epsabs=2e-21, epsrel=5e-12)[0]


def box_importance_tail(sides, eps, count=400000, seed=59):
    sides = np.array(sides, float)
    d = len(sides)
    D = float(np.linalg.norm(sides))
    lam = sides/D
    factor = 1.0 + 8.0*eps / min(sides)
    rng = np.random.default_rng(seed)
    q = rng.dirichlet(np.ones(2*d+1), count)
    xdef = (eps*factor)*q[:, :d]/lam
    ydef = (eps*factor)*q[:, d:2*d]/lam
    # Near opposite corners: actual coordinate differences.
    dist = np.linalg.norm(sides[None,:] - xdef - ydef, axis=1)
    yes = dist > D - eps
    estimate = box_coefficient(sides) * (eps*factor)**(2*d) * np.mean(yes)
    r = np.sum(q[:,:2*d],axis=1) * factor
    conditional_mean = np.mean(r[yes])
    # Under the limiting Dirichlet law, E(sum of 2d parts)=2d/(2d+1).
    return estimate, conditional_mean, float(np.mean(yes)), factor


def triangle_coefficient(vertices):
    vv = np.array(vertices, float)
    A = abs(np.linalg.det(np.stack([vv[1]-vv[0],vv[2]-vv[0]],axis=1)))/2
    D = max(np.linalg.norm(vv[i]-vv[j]) for i in range(3) for j in range(i+1,3))
    ans=0.0
    for i in range(3):
      for j in range(3):
       if i==j or abs(np.linalg.norm(vv[j]-vv[i])-D)>1e-10:continue
       e=(vv[j]-vv[i])/D
       def corner(k, direction):
         edges=[vv[z]-vv[k] for z in range(3) if z!=k]
         J=abs(np.linalg.det(np.stack(edges,axis=1)))
         w=np.dot(edges, direction)
         assert np.all(w>0), (k, direction, w)
         return J/(w[0]*w[1])
       ans += corner(i,e)*corner(j,-e)/(24*A*A)
    return ans


def run():
    for a,b in [(1,1),(1,1.5),(0.7,1.4)]:
        c = box_coefficient([a,b])
        for eps in [0.025,0.0125,0.003125]:
            exact=rectangle_tail_exact(a,b,eps)
            ratio=exact/(c*eps**4)
            assert 0.999 < ratio < 1.20, (a,b,eps,ratio)
            print('quadrature',a,b,eps,'normalized_ratio',round(ratio,9))
            if eps==0.003125:
                measured=(ratio-1)/eps
                target=box_second_ratio([a,b])
                assert abs(measured/target-1)<0.015,(measured,target)
                print('second_coefficient',a,b,measured,target)
    # Cross-check a 2D rectangle with an independent importance sampler.
    p, mu, acc, _ = box_importance_tail([1,1.5],0.035,350000,71)
    exact=rectangle_tail_exact(1,1.5,0.035)
    assert abs(p/exact-1) < 0.018,(p,exact)
    print('rect-importance','relative_error',round(p/exact-1,6),'mean_deficit_fraction',round(mu,6),'acceptance',round(acc,6))
    # Higher-dimensional counterpart; inspect the asymptotic ratios directly.
    for d in [3,4]:
        sides=[1.0]*d
        c=box_coefficient(sides)
        p,mu,acc,_=box_importance_tail(sides,0.028,500000,81+d)
        expected_mu=2*d/(2*d+1)
        assert c>0 and 0.98 < p/(c*0.028**(2*d)) < 1.20,(d,p,c)
        assert abs(mu-expected_mu)<0.045,(d,mu,expected_mu)
        b=box_second_ratio(sides)
        assert b>0
        print('hypercube',d,'coefficient',c,'second_relative',b,'tail_ratio',round(p/(c*0.028**(2*d)),6),'mean_deficit_fraction',round(mu,6))
    # Exactly identifiable equilateral multiplicity and unique-longest isosceles cases.
    s=1.0
    eq=[[0,0],[1,0],[0.5,math.sqrt(3)/2]]
    iso=[[0,0],[1,0],[0.5,0.65]]
    assert abs(triangle_coefficient(eq)-4.0)<1e-12
    assert abs(triangle_coefficient(iso)-4.0/3)<1e-12
    print('triangle_coefficients',triangle_coefficient(eq),triangle_coefficient(iso))
    print('POLYTOPE_DIAMETRAL_CONE_TWO_TERM_DIRICHLET_CHECKS_OK')

if __name__ == '__main__':run()
