"""Exact identities and finite diagnostics for an entrywise quaternionic row map."""
import numpy as np
from sympy import I as symI, Matrix, sqrt, eye, zeros

J = Matrix([[0, 1], [-1, 0]])
E = eye(2)
W = E.row_join(J).col_join(J.row_join(E))
Z = E.row_join(J).col_join((-J).row_join(E))
assert W * W.conjugate().T == 2 * eye(4)
assert Z * Z == 2 * Z
assert Z.conjugate().T == Z
assert (Z / sqrt(2)).eigenvals() == {0: 2, sqrt(2): 2}

rng = np.random.default_rng(220011)
count = 4
for k in (1, 2, 3, 4, 6):
    for _ in range(27):
        A, B, C, D = [rng.normal(size=(k,k)) + 1j*rng.normal(size=(k,k)) for i in range(4)]
        X = np.block([[A,B],[C,D]])
        Y = np.block([[A,B],[-B.conj(),A.conj()]])
        row = np.block([A,B])
        assert np.linalg.norm(Y,2) <= np.sqrt(2)*np.linalg.norm(X,2) + 1e-9
        assert np.linalg.norm(row,2) <= np.linalg.norm(X,2) + 1e-9
        if k == 1:
            assert np.linalg.norm(Y,2) <= np.linalg.norm(X,2) + 1e-9
        count += 2 + int(k == 1)
print(f'AMPLIFICATION_CHECK_OK {count}')
