"""Numerical replay of exact Schur norms for signed prism-graph Cayley matrices.
Uses only the Python standard library; finite checks do not replace proof.
"""
from math import cos, sin, pi, sqrt


def exact_sum(m):
    assert m >= 3
    return 1 - 6/m + 2/m * sum(max(1, 2*abs(cos(2*pi*j/m))) for j in range(m))


def closed_form(m):
    n = m // (2 if m % 2 == 0 else 1)
    q = n // 3
    h = pi/(2*n)
    return 3 - 6/m - 2*(2*q+1)/n + 4/n*sin((2*q+1)*h)/sin(h)


def eigenvalue(m, k, t):
    if k == 0 and t == 0:
        return 2*m - 6
    return -2*(2*cos(2*pi*k/m) + (-1)**t)


def matrix_and_witness(m):
    n = 2*m
    verts = [(i, a) for a in range(2) for i in range(m)]
    mu = {(k,t): eigenvalue(m,k,t) for k in range(m) for t in range(2)}
    M, W = [], []
    for i, a in verts:
        row_m, row_w = [], []
        for j, b in verts:
            edge = (a == b and (i-j)%m in (1,m-1)) or (a != b and i == j)
            row_m.append(-1 if edge else 1)
            row_w.append(sum((1 if mu[k,t] >= -1e-10 else -1) * cos(2*pi*k*(i-j)/m)*(-1)**(t*(a-b)) for k in range(m) for t in range(2))/n)
        M.append(row_m)
        W.append(row_w)
    return M,W


def run():
    count = 0
    largest = 0
    for m in range(3,21):
        M,W = matrix_and_witness(m)
        n = 2*m
        got = sum(M[i][j]*W[i][j] for i in range(n) for j in range(n))/n
        for expect in (exact_sum(m), closed_form(m)):
            assert abs(got-expect)<1e-9, (m, got, expect)
        for i in range(n):
            for j in range(n):
                v = sum(W[i][k]*W[k][j] for k in range(n))
                e = abs(v-(1 if i==j else 0))
                largest=max(largest,e)
                assert e<1e-9, (m,i,j,e)
                count+=1
    L = 5/3+4*sqrt(3)/pi
    for m in range(301, 307):
        coeff = {0:-4/3,1:1/9,2:4/9,3:-1/3,4:4/9,5:1/9}[m%6]*pi*sqrt(3)
        error=abs(exact_sum(m)-(L-6/m+coeff/m**2))
        assert error < 1e-7, (m,error)
    print('DIEHEDRAL_SCHUR_REPLAY_OK', 'dimensions_m=3..20', 'orthogonality_entries', count, 'max_err', f'{largest:.2e}', 'six_phase_checked_m=301..306')

if __name__=='__main__':run()
