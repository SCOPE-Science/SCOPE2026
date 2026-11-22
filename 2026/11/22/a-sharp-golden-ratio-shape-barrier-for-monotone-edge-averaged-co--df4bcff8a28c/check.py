"""Reproducible symbolic and finite checks for affine-quadrilateral edge weights.
This script supplements, but does not replace, the analytical proof.
Run: python check.py  (requires Python, NumPy and SymPy).
"""
import math
import random

import numpy as np
import sympy as sp


def bernoulli(t):
    return 1.0 if abs(t) < 1e-13 else t / math.expm1(t)


def weights(a, b, c):
    return np.array([a/3-b/6, b/3-a/6, b/3-a/6,
                     a/3-b/6, (a+b)/6+c/2, (a+b)/6-c/2])


def local_matrix_from_weights(w, v, alpha=1.0):
    pairs = [(0, 1), (0, 2), (1, 3), (2, 3), (0, 3), (1, 2)]
    out = np.zeros((4, 4))
    for z, (i, j) in enumerate(pairs):
        p = float(np.dot(v, np.array([j % 2 - i % 2, j // 2 - i // 2]))) / alpha
        left, right = bernoulli(p), bernoulli(-p)
        out[i, i] += alpha*w[z]*left
        out[i, j] -= alpha*w[z]*right
        out[j, i] -= alpha*w[z]*left
        out[j, j] += alpha*w[z]*right
    return out


def local_matrix_edgewise(w, alpha_values, peclet_values):
    pairs = [(0, 1), (0, 2), (1, 3), (2, 3), (0, 3), (1, 2)]
    out = np.zeros((4, 4))
    for z, (i, j) in enumerate(pairs):
        fac = float(w[z] * alpha_values[z])
        p = float(peclet_values[z])
        left, right = bernoulli(p), bernoulli(-p)
        out[i, i] += fac * left
        out[i, j] -= fac * right
        out[j, i] -= fac * left
        out[j, j] += fac * right
    return out


def main():
    x, y, a, b, c = sp.symbols('x y a b c', real=True)
    phi = [(1-x)*(1-y), x*(1-y), (1-x)*y, x*y]
    H = sp.Matrix([[a, c], [c, b]])
    gradients = [sp.Matrix([sp.diff(f, x), sp.diff(f, y)]) for f in phi]
    K = sp.Matrix(4, 4, lambda i,j: sp.integrate(sp.integrate(
        (gradients[i].T * H * gradients[j])[0], (x,0,1)), (y,0,1)))
    expected = sp.Matrix([
        [a/3+b/3+c/2, -a/3+b/6, a/6-b/3, -(a+b)/6-c/2],
        [-a/3+b/6, a/3+b/3-c/2, -(a+b)/6+c/2, a/6-b/3],
        [a/6-b/3, -(a+b)/6+c/2, a/3+b/3-c/2, -a/3+b/6],
        [-(a+b)/6-c/2, a/6-b/3, -a/3+b/6, a/3+b/3+c/2]
    ])
    assert K == expected
    assert K*sp.ones(4,1) == sp.zeros(4,1)
    count = 2

    # Exact rational boundary witnesses and a sharp Jacobian distortion.
    Kstar = K.subs({a:sp.Integer(2), b:sp.Integer(1), c:sp.Integer(1)})
    assert all(Kstar[i,j] <= 0 for i in range(4) for j in range(4) if i != j)
    cond_star = (3+sp.sqrt(5))/(3-sp.sqrt(5))
    assert sp.simplify(cond_star-(7+3*sp.sqrt(5))/2) == 0
    assert sp.simplify(sp.sqrt(cond_star)-(3+sp.sqrt(5))/2) == 0
    count += 3

    rng = random.Random(261101175)
    for _ in range(300):
        length_a = math.exp(rng.uniform(-1.5, 1.5))
        length_b = math.exp(rng.uniform(-1.5, 1.5))
        angle = rng.uniform(0.20, math.pi-0.20)
        J = np.array([[length_a, length_b*math.cos(angle)],
                      [0.0, length_b*math.sin(angle)]])
        metric = abs(np.linalg.det(J))*np.linalg.inv(J)@np.linalg.inv(J).T
        m11, m22, m12 = metric[0,0], metric[1,1], metric[0,1]
        w = weights(m11, m22, m12)
        g1 = length_a**2
        g2 = length_b**2
        dot = length_a*length_b*math.cos(angle)
        allowed = (g1 >= .5*g2-1e-10 and g1 <= 2*g2+1e-10
                   and abs(dot) <= (g1+g2)/3+1e-10)
        assert (min(w) >= -1e-10) == allowed
        count += 1
        drift = np.array([rng.uniform(-3,3),rng.uniform(-3,3)])
        mat = local_matrix_from_weights(w, J.T@drift)
        assert np.max(np.abs(mat.sum(axis=0))) < 1e-10
        assert (max(mat[i,j] for i in range(4) for j in range(4) if i != j) <= 1e-10) == allowed
        count += 2
        if allowed:
            assert np.linalg.cond(J,2) <= (3+math.sqrt(5))/2 + 1e-10
            count += 1

    # Check 3x3 affine periodic-type tiling with outer Dirichlet nodes.
    for aa,bb,cc in [(1,1,0),(2,1,1),(2,1,-1),(2.2,1,0),(1,1,.80),
                     (1,1,-.80),(1.5,1,.4),(.7,1,.1)]:
        assert aa*bb>cc**2
        w=weights(aa,bb,cc)
        for t in [np.array([0.0,0.0]),np.array([2.5,-1.0])]:
            A=np.zeros((16,16))
            for i in range(3):
                for j in range(3):
                    ids=[i+4*j,(i+1)+4*j,i+4*(j+1),(i+1)+4*(j+1)]
                    sub=local_matrix_from_weights(w,t)
                    for k in range(4):
                        for z in range(4):
                            A[ids[k],ids[z]]+=sub[k,z]
            interiors=[i+4*j for i in [1,2] for j in [1,2]]
            A=A[np.ix_(interiors,interiors)]
            isZ=max(A[i,j] for i in range(4) for j in range(4) if i!=j)<=1e-10
            assert isZ == (min(w)>=-1e-10)
            if isZ:
                assert np.min(np.linalg.inv(A)) >= -1e-9
            count+=2
    # No global flow potential is needed: every edge may have its own positive
    # diffusion parameter and real Péclet label.
    for aa,bb,cc in [(1,1,0),(2,1,1),(2,1,-1),(2.2,1,0),(1,1,.8),(1,1,-.8)]:
        w = weights(aa,bb,cc)
        for _ in range(20):
            A=np.zeros((16,16))
            for i in range(3):
                for j in range(3):
                    ids=[i+4*j,(i+1)+4*j,i+4*(j+1),(i+1)+4*(j+1)]
                    alphas=[math.exp(rng.uniform(-2,2)) for __ in range(6)]
                    peclets=[rng.uniform(-5,5) for __ in range(6)]
                    sub=local_matrix_edgewise(w,alphas,peclets)
                    assert np.max(np.abs(sub.sum(axis=0)))<1e-10
                    count+=1
                    for k in range(4):
                        for z in range(4):
                            A[ids[k],ids[z]]+=sub[k,z]
            interiors=[i+4*j for i in [1,2] for j in [1,2]]
            A=A[np.ix_(interiors,interiors)]
            isZ=max(A[i,j] for i in range(4) for j in range(4) if i!=j)<=1e-10
            assert isZ == (min(w)>=-1e-10)
            count+=1
            if isZ:
                assert np.min(np.linalg.inv(A)) >= -1e-9
                count+=1
    print(f'PASS: {count} assertions including exact stiffness matrix, boundary distortion, '
          'random affine shapes, arbitrary drifts, edgewise Péclet assignments, and three-by-three Dirichlet tilings')

if __name__ == '__main__':
    main()
