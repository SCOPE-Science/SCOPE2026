"""Exact tests for the singular strata of hollow symmetric determinant hypersurfaces.
No floating-point arithmetic; this is a finite consistency check, not the proof."""
from itertools import combinations
from random import Random
from sympy import Matrix, I, symbols, expand

rng = Random(271828)
checked_derivative = checked_schur = checked_rank = checked_normals = 0
for n in range(5, 9):
    r = n - 2
    # An explicit family of full-rank matrices with zero diagonal and nullity two.
    rows = []
    rows.append([1, I] + [0]*(r-2))
    rows.append([1, -I] + [0]*(r-2))
    for j in range(2, r):
        v = [0]*r
        v[0], v[j] = 1, I
        rows.append(v)
    rows += [list(rows[0]), list(rows[2])]
    W = Matrix(rows)
    M0 = W * W.T
    assert W.rank() == r and M0.rank() == r
    assert all(M0[j,j] == 0 for j in range(n))
    ker = [Matrix([(-1 if k == 0 else 1 if k == r else 0) for k in range(n)]),
           Matrix([(-1 if k == 2 else 1 if k == r+1 else 0) for k in range(n)])]
    assert all(M0*u == Matrix.zeros(n,1) for u in ker)
    # Three independent infinitesimal normal directions on the hollow subspace.
    choices = [(0, r), (2, r+1), (r, r+1)]
    data = []
    for i,j in choices:
        E = Matrix.zeros(n,n); E[i,j] = E[j,i] = 1
        data.append([(ker[0].T*E*ker[0])[0], (ker[0].T*E*ker[1])[0], (ker[1].T*E*ker[1])[0]])
    assert Matrix(data).det() != 0
    checked_normals += 1
    checked_rank += 1
    # Verify exact Schur complement near a rank-(n-1) point with its first row zero.
    B = Matrix(n-1,n-1, lambda i,j: 0 if i==j else 1)
    assert B.det() == (-1)**(n-2)*(n-2)
    t = symbols('t'); v = Matrix([k+1 for k in range(n-1)])
    A = Matrix.vstack(Matrix.hstack(Matrix([[0]]), (t*v).T),Matrix.hstack(t*v,B))
    assert expand(A.det() + B.det()*t*t*(v.T*B.inv()*v)[0]) == 0
    checked_schur += 1
    # Differentiate determinant with respect to one off-diagonal variable exactly.
    for trial in range(9):
        E = Matrix.zeros(n,n)
        for i,j in combinations(range(n),2):
            z = rng.randint(-4,4)
            E[i,j] = E[j,i] = z
        i,j = tuple(rng.sample(range(n),2))
        adj = E.adjugate()
        delta = Matrix.zeros(n,n); delta[i,j] = delta[j,i] = 1
        polynomial = (E+t*delta).det()
        assert expand(polynomial.diff(t).subs(t,0) - 2*adj[i,j]) == 0
        checked_derivative += 1
print('CHECK_OK')
print('matrix_sizes=5,6,7,8')
print(f'full_rank_isotropic_gram={checked_rank}')
print(f'independent_conormal_witnesses={checked_normals}')
print(f'exact_schur_identities={checked_schur}')
print(f'cofactor_jacobian_specializations={checked_derivative}')
