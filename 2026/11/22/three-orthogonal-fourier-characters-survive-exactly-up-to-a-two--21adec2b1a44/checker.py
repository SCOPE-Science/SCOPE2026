#!/usr/bin/env python3
"""Reproducible numerical diagnostics for the two-pair tetrahedral Fourier theorem.
This is not a substitute for the all-parameter mathematical proof.
"""
import cmath
import math


def triple_phases(a, b):
    assert a > 0 and b > 0 and abs(2*(a+b)-1) < 1e-12
    assert b <= 2*a + 1e-13 and a <= 2*b + 1e-13
    theta = math.acos(math.sqrt(b/(2*a)))
    phi = math.acos(-math.sqrt(a/(2*b)))
    return [cmath.exp(1j*theta), cmath.exp(-1j*theta),
            cmath.exp(1j*phi), cmath.exp(-1j*phi)]


def scalar_product(p, q, w):
    return sum(wj*p_j*q_j.conjugate() for wj,p_j,q_j in zip(w,p,q))


def run():
    checked=0
    for k in range(1001):
        ratio=0.5+1.5*k/1000
        b=1/(2*(1+ratio))
        a=ratio*b
        w=[a,a,b,b]
        z=triple_phases(a,b)
        moments=[sum(wj*(zj**m) for wj,zj in zip(w,z)) for m in (1,2)]
        assert max(map(abs,moments)) < 1e-12
        columns=[[zj**m for zj in z] for m in (0,1,2)]
        for i in range(3):
            for j in range(3):
                expected=1.0 if i==j else 0.0
                assert abs(scalar_product(columns[i],columns[j],w)-expected)<1e-12
        checked+=1
    # Equal weight gives the fourth column via four equally spaced phases.
    a=b=0.25
    z=triple_phases(a,b)
    w=[a,a,b,b]
    four=[[zj**m for zj in z] for m in range(4)]
    for i in range(4):
        for j in range(4):
            assert abs(scalar_product(four[i],four[j],w)-(i==j))<1e-12
    # Outside the threshold, 3*max(weight)>1, violating row leverage.
    for ratio in [0.01,0.1,0.3,0.49,2.01,3,100]:
        b=1/(2*(1+ratio));a=ratio*b
        assert 3*max(a,b)>1
    # One nonsymmetric tetrahedron: solve affine phase-realization equations.
    verts=[(0.2,0.4,-1.0),(1.2,0.9,0.1),(0.7,2.4,0.3),(-0.8,1.0,2.0)]
    ratio=1.7
    b=1/(2*(1+ratio)); a=ratio*b
    phases=triple_phases(a,b)
    mat=[[verts[j][c]-verts[0][c] for c in range(3)]
         + [cmath.phase(phases[j]/phases[0])/(2*math.pi)]
         for j in (1,2,3)]
    for c in range(3):
        r=max(range(c,3),key=lambda r:abs(mat[r][c]))
        mat[c],mat[r]=mat[r],mat[c]
        assert abs(mat[c][c])>1e-12
        pivot=mat[c][c]
        mat[c]=[v/pivot for v in mat[c]]
        for r in range(3):
            if r!=c:
                mult=mat[r][c]
                mat[r]=[mat[r][t]-mult*mat[c][t] for t in range(4)]
    xi=[mat[c][3] for c in range(3)]
    sitephases=[cmath.exp(2j*math.pi*sum(xi[c]*verts[j][c] for c in range(3)))
                for j in range(4)]
    for m in (1,2):
        assert abs(sum(wj*sitephases[j]**m
                       for j,wj in enumerate([a,a,b,b])))<1e-12
    # Two columns exist for every positive weight pair.
    for ratio in [0.01,0.1,0.5,1,2,10,100]:
        b=1/(2*(1+ratio));a=ratio*b
        assert abs(sum(wj*zj for wj,zj in zip([a,a,b,b],[1,-1,1,-1])))<1e-12
    print(f'PASS: {checked} exact-formula phase triples, equal-weight quartet, nonsymmetric tetrahedron, 7 exterior leverage tests, 7 two-character tests')

if __name__=='__main__':
    run()
