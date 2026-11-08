"""Exact finite-state checks for a two-class copy/oppose voter chain.

Standard-library only. The analytic all-size and weak-limit proofs are in RESULT.md;
finite computations below are cross-checks, not substitutes for those proofs.
"""
from fractions import Fraction as F
from itertools import product


def rates(m, r, a, b):
    return [(1, 0, (m-a)*(a+b)), (-1, 0, a*(m-a+r-b)),
            (0, 1, (r-b)*(m-a+b)), (0, -1, b*(a+r-b))]


def stationary(m, r):
    states = list(product(range(m+1), range(r+1)))
    ix = {s: i for i, s in enumerate(states)}
    n = len(states)
    q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, (a, b) in enumerate(states):
        for da, db, rate in rates(m, r, a, b):
            if rate == 0:
                continue
            j = ix[(a+da, b+db)]
            q[i][j] += rate
            q[i][i] -= rate
    # Solve Q^T pi=0 with normalization sum(pi)=1.
    mat = [[q[j][i] for j in range(n)]+[F(0)] for i in range(n-1)]
    mat.append([F(1)]*n+[F(1)])
    for col in range(n):
        pivot = next((i for i in range(col, n) if mat[i][col]), None)
        assert pivot is not None, (m, r, col)
        mat[col], mat[pivot] = mat[pivot], mat[col]
        v = mat[col][col]
        mat[col] = [z/v for z in mat[col]]
        for i in range(n):
            if i == col:
                continue
            coeff = mat[i][col]
            if coeff:
                mat[i] = [a-coeff*b for a, b in zip(mat[i], mat[col])]
    pi = [row[-1] for row in mat]
    assert all(z>0 for z in pi)
    assert sum(pi)==1
    assert all(sum(pi[j]*q[j][i] for j in range(n))==0 for i in range(n))
    return states, pi


def check(m, r):
    states, pi = stationary(m, r)
    center_a = F(m, 2)
    center_b = F(r, 2)
    moment = lambda f: sum(w*f(a,b) for (a,b),w in zip(states,pi))
    ex, ey = moment(lambda a,b:F(a)-center_a),moment(lambda a,b:F(b)-center_b)
    xx = moment(lambda a,b:(F(a)-center_a)**2)
    xy = moment(lambda a,b:(F(a)-center_a)*(F(b)-center_b))
    yy = moment(lambda a,b:(F(b)-center_b)**2)
    den = 4*(2*m*r+m+r)
    assert (ex,ey)==(0,0), (m,r,ex,ey)
    assert xx==F(m*m*(m+3*r),den), (m,r,xx)
    assert xy==F(m*r*(r-m),den), (m,r,xy)
    assert yy==F(r*r*(3*m+r),den), (m,r,yy)
    # Three exact generator moment identities at stationarity.
    assert F(m*m+m*r,2)-2*(r+1)*xx+2*(m-1)*xy==0
    assert -r*xx-(m+r)*xy+m*yy==0
    assert F(m*r+r*r,2)-2*(r-1)*xy-2*(m+1)*yy==0
    return len(states)


def main():
    count=0
    states=0
    for m in range(1,7):
        for r in range(1,5):
            states += check(m,r)
            count += 1
    # All-source algebraic consequences and limit of exact moments.
    for r in range(1,6):
        assert F(1,4*(2*r+1))==F(r,4*(2*r*r+r))
    print(f"PASS: {count} finite irreducible chains, {states} aggregate states; exact stationary means, covariance matrices, and generator identities")
    print("PASS: fixed-contrarian limiting variance formula; full weak-limit proof is analytic")


if __name__ == '__main__':
    main()
