#!/usr/bin/env python3
"""Independent finite-dimensional checks for wheel Laplacian simplex metric formulas.

Run: python3 verify.py
Requires numpy, sympy. Finite checks complement, and do not replace, the proof.
"""
import math
import numpy as np
import sympy as sp


def wheel_laplacian(m):
    n = m + 1
    L = sp.zeros(n)
    for j in range(1, n):
        L[0, j] = L[j, 0] = -1
        L[0, 0] += 1
        L[j, j] += 1
    for i in range(m):
        j, k = i + 1, (i + 1) % m + 1
        L[j, j] += 1
        L[k, k] += 1
        L[j, k] -= 1
        L[k, j] -= 1
    return L


def wheel_formula(m):
    n = m + 1
    a = math.sqrt(m / n**3)
    b2 = 1 / (m * n**3) + sum(
        1 / (3 - 2 * math.cos(2 * math.pi * k / m)) ** 2
        for k in range(1, m)) / m
    b = math.sqrt(b2)
    t_in = (a-b)/(a+m*b)
    r = 1/(a+m*b)
    t_out = (m*n - 12)/(2*n*n)
    R = math.sqrt(m*n)*(1-t_out)
    p = (1+m*t_out)/n
    return a,b,t_in,r,t_out,R,p


checks = 0
for m in range(3, 11):
    n = m+1
    L = wheel_laplacian(m)
    assert L.rank() == m
    assert L * sp.ones(n, 1) == sp.zeros(n, 1)
    v = [L[:, j] for j in range(n)]
    # Direct Gram determinants for the intrinsic Euclidean volumes of
    # full simplex and all opposite facets.
    B = sp.Matrix.hstack(*[v[j]-v[0] for j in range(1,n)])
    vol2 = sp.factor((B.T*B).det()) / sp.factorial(m)**2
    tau = (L[1:,1:]).det()
    assert sp.simplify(vol2 - sp.Rational(n**3)*tau**2/sp.factorial(m)**2) == 0
    V = math.sqrt(float(vol2))
    a,b,t_in,r,t_out,R,p = wheel_formula(m)
    areas = []
    for omitted in range(n):
        remaining=[v[j] for j in range(n) if j!=omitted]
        Bf=sp.Matrix.hstack(*[remaining[j]-remaining[0] for j in range(1,m)])
        area2=sp.factor((Bf.T*Bf).det())/sp.factorial(m-1)**2
        areas.append(math.sqrt(float(area2)))
    assert math.isclose(areas[0],m*V*a,rel_tol=2e-11)
    assert all(math.isclose(s,m*V*b,rel_tol=2e-11) for s in areas[1:])
    assert math.isclose(sum(areas)/V,m*(a+m*b),rel_tol=2e-11)
    # Independent pseudoinverse of the intrinsic linear map, to check
    # every facet distance at the computed incenter.
    Lnp=np.array(L,float)
    P=np.linalg.pinv(Lnp)
    hub=Lnp[:,0]
    cin=t_in*hub
    bary=np.ones(n)/n+P@cin
    clearances=bary/np.linalg.norm(P,axis=0)
    assert np.allclose(clearances,r,rtol=3e-12,atol=3e-12)
    assert abs(np.linalg.norm(cin-hub) - np.linalg.norm(cin-Lnp[:,1]))>1e-5 or m==3
    # The minimum enclosing ball has all vertices on the boundary;
    # its center is a *positive* convex combination of these vertices.
    cout=t_out*hub
    dist=np.linalg.norm(Lnp-cout[:,None],axis=0)
    assert np.allclose(dist,R,rtol=4e-12,atol=4e-12)
    weights=np.array([p]+[(1-p)/m]*m)
    assert np.all(weights>0)
    assert np.allclose(Lnp@weights,cout,rtol=5e-12,atol=5e-12)
    # Directly verify scalar minimax at perturbations of the center.
    for delta in [-1,-.1,-.001,.001,.1,1]:
        test=cout+delta*hub
        assert np.max(np.linalg.norm(Lnp-test[:,None],axis=0))>R
        checks+=1
    checks+=8

rho=(3-math.sqrt(5))/2
beta=math.sqrt(3/(5*math.sqrt(5)))
for m in [100,1000,5000,20000]:
    # Fast exact trigonometric expression, no large matrix construction.
    a,b,tc,r,td,R,p=wheel_formula(m)
    assert abs(b-beta)<1.1/m
    assert abs(m*r-1/beta)<6/m+0.05
    assert abs(m*m*a/(a+m*b)-1/beta)<10/m+0.08
    assert abs(2*R/m-1)<4/m
    assert abs(p-0.5)<1/m
    checks+=5

print(f"WHEEL_LAPLACIAN_METRIC_PASS checks={checks} m=3..10 and asymptotic m<=20000")
