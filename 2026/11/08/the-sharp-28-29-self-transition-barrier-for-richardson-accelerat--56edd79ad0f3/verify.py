"""Standalone exact checks for a graph-heat Richardson extrapolation theorem.

Run with Python 3: python verify.py. No third-party packages are required.
Finite matrix tests supplement, but do not establish, the universal theorem.
"""
from fractions import Fraction as Q


def polyadd(*args):
    n = max(map(len, args))
    return tuple(sum((a[i] if i < len(a) else 0) for a in args) for i in range(n))


def polymul(a, b):
    p = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            p[i + j] += x * y
    return tuple(p)


def polydiff(a):
    return tuple(i * a[i] for i in range(1, len(a)))


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def inverse(A):
    n = len(A)
    aug = [[Q(x) for x in A[i]] + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        p = next(j for j in range(i, n) if aug[j][i])
        aug[i], aug[p] = aug[p], aug[i]
        t = aug[i][i]
        aug[i] = [x / t for x in aug[i]]
        for j in range(n):
            if j == i:
                continue
            t = aug[j][i]
            aug[j] = [x - t * y for x, y in zip(aug[j], aug[i])]
    return [row[n:] for row in aug]


# R(z)=-(z^2-4z-4)/((z+1)(z+2)^2).
D = polymul((1, 1), polymul((2, 1), (2, 1)))
N = (4, 4, -1)
assert D == (4, 8, 5, 1)
# 27*N+D = z(z-12)^2 +2(z-7)^2 +14, hence R(z)>-1/27 for z>=0.
left = polyadd(D, tuple(27*x for x in N))
right = polyadd(polymul((0, 1), polymul((-12, 1), (-12, 1))),
                tuple(2*x for x in polymul((-7, 1), (-7, 1))), (14,))
assert left == right == (112, 116, -22, 1)
# Derivative's numerator D*N' - N*D', all terms checked exactly.
deriv_num = polyadd(polymul(polydiff(N), D),
                    tuple(-x for x in polymul(N, polydiff(D))))
assert deriv_num == polymul((2, 1), ( -8, -20, -10, 1))
assert Q(-23, 637) == -Q(12*12-4*12-4, (12+1)*(12+2)**2)
assert Q(-23, 637) < -Q(1, 28)

checks = 6
# For any network with a uniform-weight universal hub, all its other edges
# are irrelevant to that hub's exact scalar spectral profile.
for n in range(2, 9):
    for a in (1, 2, 5):
        W = [[Q(0) for _ in range(n)] for _ in range(n)]
        for j in range(1, n):
            W[0][j] = W[j][0] = Q(a)
        for j in range(1, n):
            for k in range(j+1, n):
                if (2*j + k) % 3 == 0:
                    W[j][k] = W[k][j] = Q(j+k, 7)
        L = [[(sum(W[i]) if i == j else 0) - W[i][j]
              for j in range(n)] for i in range(n)]
        # L(e_hub - 1/n*1) = n*a*(e_hub - 1/n*1)
        v = [Q(int(i == 0)) - Q(1, n) for i in range(n)]
        assert [sum(L[i][j]*v[j] for j in range(n)) for i in range(n)] == [n*a*x for x in v]
        h = Q(12, n*a)
        M1 = [[Q(int(i==j))+h*L[i][j] for j in range(n)] for i in range(n)]
        Mh = [[Q(int(i==j))+h*L[i][j]/2 for j in range(n)] for i in range(n)]
        A = inverse(M1)
        B = inverse(Mh)
        BB = matmul(B, B)
        T00 = 2*BB[0][0] - A[0][0]
        assert T00 == Q(660-23*n, 637*n)
        checks += 2

# The first dimension to give a negative hub diagonal at z=12 is n=29.
assert all(Q(660-23*n, 637*n)>0 for n in range(2, 29))
assert Q(660-23*29, 637*29) == Q(-7, 18473)
assert all(Q(660-23*n, 637*n)<0 for n in range(29, 100))
checks += 3
print(f"EXACT_VERIFICATION_OK {checks} algebraic/matrix/threshold checks")
