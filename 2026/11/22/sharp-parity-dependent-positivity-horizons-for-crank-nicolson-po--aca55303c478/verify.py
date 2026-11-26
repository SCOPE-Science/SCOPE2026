"""Finite exact-rational tests for the Crank--Nicolson star sign formulas."""
from fractions import Fraction as Q


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def crank_nicolson(n, edges, h):
    laplacian = [[0]*n for _ in range(n)]
    for i, j in edges:
        laplacian[i][i] += 1
        laplacian[j][j] += 1
        laplacian[i][j] -= 1
        laplacian[j][i] -= 1
    h = Q(h)
    eye = identity(n)
    work = [[eye[i][j] + h*laplacian[i][j]/2 for j in range(n)]
            + [eye[i][j] - h*laplacian[i][j]/2 for j in range(n)] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if work[i][j])
        work[j], work[p] = work[p], work[j]
        pivot = work[j][j]
        work[j] = [x/pivot for x in work[j]]
        for i in range(n):
            if i != j:
                v = work[i][j]
                work[i] = [x-v*y for x, y in zip(work[i], work[j])]
    assert [row[:n] for row in work] == eye
    return [row[n:] for row in work]


def star(m, h):
    return crank_nicolson(m+1, [(0, i) for i in range(1, m+1)], h)


def main():
    cases = 0
    for m in range(2, 9):
        for h in map(Q, ('1/100', '1/2', '2/3', '1', '2', '3', '4', '5', '6', '30', '100')):
            c = star(m, h)
            a, b = (2-h)/(2+h), (2-(m+1)*h)/(2+(m+1)*h)
            p = identity(m+1)
            for k in range(1, 10):
                p = multiply(p, c)
                hd, hl = (1+m*b**k)/(m+1), (1-b**k)/(m+1)
                ld = (m+(m*m-1)*a**k+b**k)/(m*(m+1))
                ll = (m-(m+1)*a**k+b**k)/(m*(m+1))
                assert all(sum(row) == 1 for row in p)
                for i, row in enumerate(p):
                    for j, value in enumerate(row):
                        want = (hd if i == j else hl) if min(i,j) == 0 else (ld if i == j else ll)
                        assert value == want
                        if i != j or k % 2 == 0:
                            assert value > 0
                if k % 2:
                    assert ld > hd
                cases += 1

    for m, k, h in ((2, 1, Q(2)), (8, 3, Q(2,3))):
        c = star(m, h)
        p = identity(m+1)
        for _ in range(k):
            p = multiply(p, c)
        assert p[0][0] == 0
        assert all(p[i][j] > 0 for i in range(m+1) for j in range(m+1) if i or j)
    for h in (4, 5):
        c = star(2, h)
        assert c[0][0] < 0
        assert c[1][1] == c[2][2] == Q(4+4*h-h*h, (2+h)*(2+3*h))
        assert (c[1][1] > 0) == (h == 4)
    c = star(2, 6)
    assert [c[i][i] for i in range(3)] == [Q(-1,5), Q(-1,20), Q(-1,20)]
    assert all(x > 0 for row in multiply(c, c) for x in row)
    c = crank_nicolson(4, [(0,1), (1,2), (2,3)], 30)
    assert multiply(c, c)[0][1] == Q(-5111040, 250937281)
    print('Exact star-power cases:', cases, '; both hub crossings, leaf bracket and path witness verified')


if __name__ == '__main__':
    main()
