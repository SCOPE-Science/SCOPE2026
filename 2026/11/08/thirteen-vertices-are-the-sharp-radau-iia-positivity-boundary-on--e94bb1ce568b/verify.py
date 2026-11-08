"""Exact-rational checks for Radau IIA positivity on conference graphs.
Standard-library only; run: python verify.py
Finite checks supplement the proof in RESULT.md; they do not certify all parameters.
"""
from fractions import Fraction as F


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def inv(A):
    n = len(A)
    M = [[F(z) for z in row] + [F(i == j) for j in range(n)] for i, row in enumerate(A)]
    for k in range(n):
        idx = next(i for i in range(k, n) if M[i][k])
        M[k], M[idx] = M[idx], M[k]
        z = M[k][k]
        M[k] = [x/z for x in M[k]]
        for i in range(n):
            if i != k and M[i][k]:
                z = M[i][k]
                M[i] = [M[i][j]-z*M[k][j] for j in range(2*n)]
    return [row[n:] for row in M]


def graph(q):
    if q == 9:  # the 3 by 3 rook graph, SRG(9,4,1,2)
        return [[F(i != j and (i//3 == j//3 or i%3 == j%3)) for j in range(q)] for i in range(q)]
    assert q in (5, 13, 17, 29)
    residues = {x*x % q for x in range(1, q)}
    return [[F(i != j and ((i-j) % q in residues)) for j in range(q)] for i in range(q)]


def polynomial(t, h):
    return (t*t*(4*t+1)*h**4-4*t*(t-1)*(4*t+1)*h**3 +
            (-8*t*t+40*t+6)*h*h+(24*t+24)*h+36)


def coefficients(t, h):
    d = 4*t+1
    p = t*d
    den = h**4*p*p + 4*h**3*p*d + h*h*(6*d*d+4*p) + 24*h*d + 36
    alpha = h*(h**3*p*d + h*h*(6*d*d-2*p) +24*h*d+36)/den
    beta = h*h*(h*h*p+6*h*d+18)/den
    return alpha, beta, den


def check_graph(q, h):
    t = (q-1)//4
    A = graph(q)
    k = 2*t
    L = [[F(k*(i == j)) - A[i][j] for j in range(q)] for i in range(q)]
    L2 = matmul(L, L)
    alpha,beta,den=coefficients(t,h)
    # A direct rational inversion, independent of the three-entry formula.
    D = [[h*h*L2[i][j]+4*h*L[i][j]+6*F(i==j) for j in range(q)] for i in range(q)]
    Numer = [[6*F(i==j)-2*h*L[i][j] for j in range(q)] for i in range(q)]
    T = matmul(Numer,inv(D))
    assert all(sum(row)==1 for row in T)
    for i in range(q):
        for j in range(q):
            assert L2[i][j] == (k*k+k if i==j else -3*t-1 if A[i][j] else t)
            val = F(i==j)-alpha*L[i][j]+beta*L2[i][j]
            assert T[i][j] == val
            if i == j:
                assert T[i][j] == polynomial(t,h)/den
            elif A[i][j]:
                Q=(36+(42*t+6)*h+4*t*(4*t+1)*h*h+t*t*(4*t+1)*h**3)
                assert T[i][j] == h*Q/den
                if h>0:
                    assert T[i][j]>0
            else:
                assert T[i][j] == t*beta
                if h>0:
                    assert T[i][j]>0
    return q*q


def main():
    cases = 0
    entries = 0
    hs = [F(0),F(1,8),F(1,2),F(1),F(2),F(3),F(4),F(6)]
    for q in (5,9,13,17,29):
        for h in hs:
            entries += check_graph(q,h)
            cases += 1
    # Exact finite witnesses and sign checks, not a proof of the infinite claim.
    assert all(polynomial(t,F(2))>0 for t in (1,2))
    assert all(polynomial(t,F(2))<0 for t in range(3,301))
    for t in range(1,101):
        for h in (F(0), F(1,20),F(1,4), F(1),F(2),F(5),F(20)):
            alpha,beta,D=coefficients(t,h)
            assert D>0
            assert polynomial(t,h)/D == 1-2*t*alpha+(4*t*t+2*t)*beta
            if t<=2:
                assert polynomial(t,h)>0
    print(f'PASS: {cases} exact matrix inversions, {entries} exact entry identities, 300 exact cutoff witnesses, 700 additional diagonal identities.')


if __name__=='__main__':
    main()
