from fractions import Fraction as F


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def mv(A, x):
    return [sum((A[i][j]*x[j] for j in range(len(x))), F(0)) for i in range(len(A))]


def mm(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def inv(A):
    n = len(A)
    M = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(i for i in range(c, n) if M[i][c])
        M[c], M[p] = M[p], M[c]
        q = M[c][c]
        M[c] = [v/q for v in M[c]]
        for i in range(n):
            if i == c:
                continue
            q = M[i][c]
            if q:
                M[i] = [M[i][j] - q*M[c][j] for j in range(2*n)]
    return [r[n:] for r in M]


def sd_step(A, b, x):
    Ax = mv(A, x)
    r = [b[i] - Ax[i] for i in range(len(b))]
    if all(v == 0 for v in r):
        return x, r, None
    Ar = mv(A, r)
    alpha = dot(r, r) / dot(r, Ar)
    return [x[i] + alpha*r[i] for i in range(len(x))], r, alpha

# Exact three-dimensional witness.
A = [[F(2), F(-2), F(0)],
     [F(-2), F(3), F(-1)],
     [F(0), F(-1), F(7)]]
b = [F(3), F(0), F(1)]
# Sylvester minors: 2, 2, 12.
assert A[0][0] == 2
assert A[0][0]*A[1][1] - A[0][1]*A[1][0] == 2
assert (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
        - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
        + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])) == 12
Ainv = inv(A)
assert mm(A, Ainv) == eye(3)
sol = mv(Ainv, b)
assert sol == [F(31, 6), F(11, 3), F(2, 3)]
assert all(v > 0 for v in sol)

x0 = [F(0), F(0), F(0)]
x1, r0, a0 = sd_step(A, b, x0)
x2, r1, a1 = sd_step(A, b, x1)
assert a0 == F(2, 5)
assert x1 == [F(6, 5), F(0), F(2, 5)]
assert r1 == [F(3, 5), F(14, 5), F(-9, 5)]
assert dot(r0, r1) == 0
assert a1 == F(286, 1257)
assert x2 == [F(560, 419), F(4004, 6285), F(-4, 419)]
assert x2[2] < 0

# Supplementary exact checks of the two-dimensional recurrence on a family
# of rational SPD Stieltjes matrices and nonnegative right-hand sides.
examples = [
    ([[F(3), F(-1)], [F(-1), F(2)]], [F(2), F(1)]),
    ([[F(5), F(-2)], [F(-2), F(4)]], [F(0), F(3)]),
    ([[F(7,2), F(-1,2)], [F(-1,2), F(5,2)]], [F(1), F(4)]),
]
for B, c in examples:
    assert B[0][0] > 0 and B[1][1] > 0 and B[0][1] <= 0 and B[1][0] <= 0
    det = B[0][0]*B[1][1] - B[0][1]*B[1][0]
    assert det > 0
    Binv = inv(B)
    assert all(v >= 0 for row in Binv for v in row)
    x = [F(0), F(0)]
    xs = [x]
    alphas = []
    residuals = []
    for _ in range(10):
        xnew, r, a = sd_step(B, c, x)
        residuals.append(r)
        if a is None:
            x = xnew
            xs.append(x)
            break
        alphas.append(a)
        x = xnew
        xs.append(x)
        assert all(v >= 0 for v in x)
    if len(alphas) >= 2:
        a0e, a1e = alphas[0], alphas[1]
        tr = B[0][0] + B[1][1]
        assert a0e + a1e == a0e*a1e*tr
        r2 = residuals[2] if len(residuals) > 2 else [c[i] - mv(B, xs[2])[i] for i in range(2)]
        rho = F(1) - a0e*a1e*det
        calc_r2 = [c[i] - mv(B, xs[2])[i] for i in range(2)]
        assert calc_r2 == [rho*v for v in c]
        assert F(0) <= rho < 1

print('VERIFY_OK')
