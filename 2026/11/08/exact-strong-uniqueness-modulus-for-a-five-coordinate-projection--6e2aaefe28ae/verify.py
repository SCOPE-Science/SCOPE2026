"""Exact rational certificate for a five-coordinate minimal-projection stability inequality.

Requires Python 3 and SymPy. Run: python verify.py
"""
import sympy as S

R = S.Rational
U = S.Matrix([
    [1, 0], [R(13, 20), R(3, 5)], [0, 1],
    [-R(1, 2), 1], [-R(19, 20), R(3, 5)]
])
F0 = S.Matrix([
    [R(520, 659), R(105, 1318), R(110, 659), -R(110, 659), -R(105, 1318)],
    [R(130, 659), R(665, 5272), R(315, 659), R(260, 659), R(455, 5272)]
])
P0 = U * F0
radius = R(845, 659)
K = R(493257, 1508)
assert F0 * U == S.eye(2)
assert [sum(abs(P0[i, j]) for j in range(5)) for i in range(5)] == [radius]*5

def opnorm(A):
    return max(sum(abs(A[i, j]) for j in range(A.cols)) for i in range(A.rows))

x = S.symbols('h0:10')
H = S.Matrix([list(x[:5]), list(x[5:])])
Q = U * H
HU = H * U
constraint = list(HU)
forms = []
for i in range(5):
    signs = [S.sign(P0[i, j]) for j in range(5)]
    if i in (1, 4):
        zero = 4 if i == 1 else 1
        for choice in (1, -1):
            z = signs.copy()
            z[zero] = choice
            forms.append(S.expand(sum(z[j] * Q[i, j] for j in range(5))))
    else:
        forms.append(S.expand(sum(signs[j] * Q[i, j] for j in range(5))))
weights = [R(104, 659), R(29, 1318), R(143, 659), R(120, 659),
           R(120, 659), R(29, 1318), R(143, 659)]
assert sum(weights) == 1 and all(z > 0 for z in weights)
# Barycentric identity: the weighted supporting-form sum vanishes whenever HU = 0.
identity = sum(w*L for w, L in zip(weights, forms))
assert S.expand(identity - (R(416,659)*HU[0,0] - R(13,2636)*HU[0,1] + R(429,659)*HU[1,1])) == 0
assert S.linear_eq_to_matrix(constraint, x)[0].rank() == 4
assert S.linear_eq_to_matrix(constraint + forms, x)[0].rank() == 10
expected = [R(1013,104), K, R(9739,572), R(2909,104),
            R(2909,104), K, R(9739,572)]
vertices = []
for omitted in range(7):
    system = constraint + [forms[j]-1 for j in range(7) if j != omitted]
    A, b = S.linear_eq_to_matrix(system, x)
    assert A.det() != 0
    solution = A.inv() * b
    Hvertex = S.Matrix([list(solution[:5]), list(solution[5:])])
    assert Hvertex * U == S.zeros(2, 2)
    evaluations = [S.expand(L.subs(dict(zip(x, solution)))) for L in forms]
    assert all(evaluations[j] == 1 for j in range(7) if j != omitted)
    assert evaluations[omitted] == 1 - 1/weights[omitted]
    assert opnorm(U*Hvertex) == expected[omitted]
    vertices.append(Hvertex)
assert max(expected) == K
# A concrete rational small perturbation attains the exact slope K.
epsilon = R(1, 100000)
Hext = vertices[1]
assert opnorm(U*Hext) == K
assert opnorm(P0 + epsilon*U*Hext) == radius + epsilon
print('PASS: exact reproduction of 7 simplex vertices, all norms and sharpness')
print('minimum projection norm =', radius)
print('sharp error-bound constant =', K)
print('directional equality at epsilon =', epsilon)
