"""Self-contained finite-graph tests for the two-chord cycle theorem.
Run with Python 3: python verify.py. No third-party dependencies.
"""
import math


def bisect(fn, left, right, iterations=100):
    fl, fr = fn(left), fn(right)
    assert fl * fr < 0, (fl, fr)
    for _ in range(iterations):
        mid = (left + right) / 2
        if fn(mid) * fl > 0:
            left, fl = mid, fn(mid)
        else:
            right = mid
    return (left + right) / 2


def F(q):
    return q * (1 + q*q) / (1 - q*q)


def root(L, sign):
    return bisect(lambda q: F(q)*(1+sign*q**(L-2))/(1-sign*q**L)-1,
                  0.000001, 0.999999)


def green(k, L, q):
    N = 2*L
    k %= N
    return (q**k + q**(N-k)) / ((1/q-q)*(1-q**N))


def adjacency(L, chords=2):
    N = 2*L
    A = [[0.0]*N for _ in range(N)]
    for i in range(N):
        j = (i+1)%N
        A[i][j] = A[j][i] = 1.0
    for u, v in [(0,2),(L,L+2)][:chords]:
        A[u][v] = A[v][u] = 1.0
    return A


def jacobi_eigenvalues(matrix):
    """Independent real-symmetric Jacobi diagonalizer (finite tests only)."""
    a = [row[:] for row in matrix]
    n = len(a)
    for iteration in range(75*n*n):
        p, q, largest = 0, 1, 0.0
        for i in range(n):
            for j in range(i+1,n):
                v = abs(a[i][j])
                if v > largest: p, q, largest = i, j, v
        if largest < 1e-12:
            return sorted((a[i][i] for i in range(n)), reverse=True)
        theta = 0.5*math.atan2(2*a[p][q], a[q][q]-a[p][p])
        c, s = math.cos(theta), math.sin(theta)
        # Rotation [[c,s],[-s,c]] in the (p,q) coordinate plane.
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = c*c*app - 2*c*s*apq + s*s*aqq
        a[q][q] = s*s*app + 2*c*s*apq + c*c*aqq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k == p or k == q: continue
            akp, akq = a[k][p], a[k][q]
            a[k][p] = a[p][k] = c*akp - s*akq
            a[k][q] = a[q][k] = s*akp + c*akq
    raise AssertionError('Jacobi diagonalization did not converge')


def check():
    tests = 0
    q0 = bisect(lambda x: x**3+x*x+x-1, .1, .9)
    lam0 = q0 + 1/q0
    C = (2*(1+q0*q0)*(1-q0*q0)**3 /
         (q0**4*(1+4*q0*q0-q0**4)))
    assert abs(q0-0.5436890126920753) < 1e-13; tests += 1
    assert abs(lam0-2.38297576790624) < 1e-12; tests += 1
    assert abs(C-4.94735937855521) < 1e-11; tests += 1

    for L in range(5, 15):
        qplus, qminus = root(L, 1), root(L, -1)
        lp, lm = qplus + 1/qplus, qminus + 1/qminus
        assert lp > lm > 2; tests += 1
        assert qplus < q0 < qminus; tests += 1
        assert abs(F(qplus)*(1+qplus**(L-2))/(1-qplus**L)-1) < 1e-12; tests += 1
        assert abs(F(qminus)*(1-qminus**(L-2))/(1+qminus**L)-1) < 1e-12; tests += 1
        A = adjacency(L)
        vals = jacobi_eigenvalues(A)
        assert abs(vals[0]-lp) < 1e-9; tests += 1
        assert abs(vals[1]-lm) < 1e-9; tests += 1
        assert vals[2] <= 2 + 1e-9; tests += 1
        for sign, q in [(1, qplus), (-1, qminus)]:
            vec = [green(i,L,q)+green(i-2,L,q)+
                   sign*(green(i-L,L,q)+green(i-L-2,L,q))
                   for i in range(2*L)]
            norm = math.sqrt(sum(v*v for v in vec))
            vec = [v/norm for v in vec]
            lam = q + 1/q
            assert max(abs(sum(a*v for a,v in zip(row,vec))-lam*vec[i])
                       for i,row in enumerate(A)) < 1e-9; tests += 1
            if sign == 1:
                assert min(vec) > 0; tests += 1
        # One-chord comparison, including the rank-one upper bound on lambda_2.
        single = jacobi_eigenvalues(adjacency(L,1))
        assert single[0] > 2 and single[1] <= 2+1e-9; tests += 1
        assert single[1] >= 2*math.cos(2*math.pi/(2*L))-1e-9; tests += 1

    ratios = []
    for L in [10,12,14,16,18,20]:
        qp,qm = root(L,1),root(L,-1)
        gap = (1/qp+qp)-(1/qm+qm)
        ratios.append(gap/q0**L)
    assert abs(ratios[-1]-C)/C < 1e-6; tests += 1
    assert abs(ratios[-2]-C)/C < 1e-5; tests += 1
    for a,b in zip(ratios,ratios[1:]):
        assert abs(b-C) < abs(a-C); tests += 1
    assert abs(lam0/C-0.4816661951495721) < 1e-12; tests += 1
    print('VERIFY_OK', tests, 'assertions; q0=',repr(q0),
          'lambda0=',repr(lam0), 'C=',repr(C))

if __name__ == '__main__':
    check()
