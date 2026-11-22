"""Reproduce exact three-patch invasion signs and resistance coefficients.

Requires Python 3 standard library only. This checks a finite example; it is
not a substitute for the general graph perturbation proof.
"""
from fractions import Fraction as F

B = (F(3), F(2), F(1))
N = 3
A = F(2)
F_RATE = F(10)
H = F(49, 50)


def det2(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def det3(mat):
    return sum(((-1) ** j) * mat[0][j] * det2([[mat[r][c] for c in range(3) if c != j] for r in (1, 2)]) for j in range(3))


def laplacian(edges):
    l = [[F(0) for _ in range(N)] for _ in range(N)]
    for u, v in edges:
        l[u][u] += 1
        l[v][v] += 1
        l[u][v] -= 1
        l[v][u] -= 1
    return l


def invasion_minors(l):
    t = [[A * (i == j) + F_RATE * l[i][j] - (H * B[i] if i == j else 0) for j in range(N)] for i in range(N)]
    return t[0][0], det2([row[:2] for row in t[:2]]), det3(t)


def laplace_energy(l):
    # Solve L phi=(1,0,-1), phi[2]=-phi[0] for these symmetric examples.
    # In a general connected graph the unique mean-zero potential exists.
    potential = (F(1) / (l[0][0] + l[0][2] * (-1)), F(0), F(-1) / (l[0][0] + l[0][2] * (-1)))
    target = [B[i] - F(2) for i in range(3)]
    assert all(sum(l[i][j] * potential[j] for j in range(3)) == target[i] for i in range(3))
    return sum(target[i] * potential[i] for i in range(3))


def main():
    p = laplacian([(0, 1), (1, 2)])
    t = laplacian([(0, 1), (1, 2), (0, 2)])
    p_minors, t_minors = invasion_minors(p), invasion_minors(t)
    assert p_minors == (F(453, 50), F(101953, 1250), F(-448897, 62500))
    assert t_minors == (F(953, 50), F(352453, 1250), F(1053103, 62500))
    assert p_minors[0] > 0 and p_minors[1] > 0 and p_minors[2] < 0
    assert all(x > 0 for x in t_minors)
    e_p, e_t = laplace_energy(p), laplace_energy(t)
    assert e_p == F(2) and e_t == F(2, 3)
    s = sum(B)
    q_p = N * A * e_p / (s * s)
    q_t = N * A * e_t / (s * s)
    eta = F(1, 5)
    assert q_p == F(1, 3) and q_t == F(1, 9)
    assert q_t < eta < q_p
    print('Path Sylvester minors:', p_minors, '=> invasion eigenvalue > 1')
    print('Triangle Sylvester minors:', t_minors, '=> invasion eigenvalue < 1')
    print('Laplacian energies:', e_p, e_t)
    print('Critical-window coefficients:', q_p, q_t, '; eta=', eta)
    print('All exact-rational checks passed.')


if __name__ == '__main__':
    main()
