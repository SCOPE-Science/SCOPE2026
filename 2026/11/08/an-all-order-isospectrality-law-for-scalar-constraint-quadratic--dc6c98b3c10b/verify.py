"""Exact arithmetic checks for fixed-order scalar-constraint ADMM spectra.

Run: python3 verify.py. Uses Python standard library only.
Finite checks corroborate but do not replace the all-n symbolic argument.
"""
from fractions import Fraction as F
from itertools import permutations


def sweep_matrix(cs):
    n = len(cs)
    rows = [[F(i == j) for j in range(n + 1)] for i in range(n + 1)]
    for i, c in enumerate(cs):
        rows[i] = [-c * (sum(rows[k][j] for k in range(n) if k != i) + rows[n][j])
                   for j in range(n + 1)]
    rows[n] = [rows[n][j] + sum(rows[i][j] for i in range(n)) for j in range(n + 1)]
    return rows


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def charpoly(a):
    # Faddeev-LeVerrier, coefficients from highest degree down.
    n = len(a)
    b = [[F(i == j) for j in range(n)] for i in range(n)]
    coefs = [F(1)]
    for k in range(1, n + 1):
        t = matmul(a, b)
        ck = -sum(t[i][i] for i in range(n)) / k
        coefs.append(ck)
        for i in range(n):
            t[i][i] += ck
        b = t
    return coefs


def predicted_coefficients(cs):
    # q has length n, degree n-1; characteristic lambda^2*q.
    n = len(cs)
    p = [F(1)]
    for c in cs:
        q = [F(0)]*(len(p)+1)
        for j, v in enumerate(p):
            q[j] -= c*v
            q[j+1] += v
        p = q
    z = F(1)
    for c in cs:
        z *= 1-c
    p[n-2] += z
    p[n-1] -= 2*z
    q = [F(0)]*n
    q[n-1] = p[n]
    for j in range(n-2,-1,-1):
        q[j] = p[j+1]+q[j+1]
    assert p[0]+q[0] == 0
    return list(reversed(q)) + [F(0),F(0)]


def apply_order(cs, order, state):
    y=list(state[:len(cs)])
    u=state[-1]
    for i in order:
        y[i]=-cs[i]*(sum(y[j] for j in range(len(cs)) if j!=i)+u)
    u=u+sum(y)
    return y+[u]


def main():
    counts={}
    cs = [F(1,5),F(2,5),F(3,5),F(4,5),F(1,7),F(3,7),F(2,9)]
    assertions=0
    for n in range(2,6):
        expected=predicted_coefficients(cs[:n])
        count=0
        for pp in permutations(cs[:n]):
            assert charpoly(sweep_matrix(pp))==expected
            assertions+=1
            count+=1
        counts[n]=count
    for n in [6,7]:
        expected=predicted_coefficients(cs[:n])
        choices=[cs[:n],list(reversed(cs[:n])), cs[1:n]+cs[:1],cs[n-1:n]+cs[:n-1]]
        for pp in choices:
            assert charpoly(sweep_matrix(pp))==expected
            assertions+=1
        counts[n]=len(choices)
    # Heterogeneous four-block example: all permutations share eigenvalues, transients differ.
    x=[F(1),F(-2),F(3),F(-1),F(1,3)]
    o1=(2,1,0,3)  # one-based (3,2,1,4)
    o2=(1,3,2,0)  # one-based (2,4,3,1)
    v1=apply_order(cs[:4],o1,x)
    v2=apply_order(cs[:4],o2,x)
    assert v1==[F(1,25),F(-8,15),F(1),F(-84,125),F(21,125)]
    assert v2==[F(49,125),F(-4,3),F(36,25),F(-12,5),F(-196,125)]
    assert sum(v*v for v in v1)==F(248323,140625)
    assert sum(v*v for v in v2)==F(1718953,140625)
    assertions+=4
    # Exactly check all positivity identities needed for the n=3 Schur test.
    for a in [F(1,7),F(1,2),F(6,7)]:
      for b in [F(1,3),F(4,5)]:
       for c in [F(1,4),F(8,9)]:
        B=a+b+c-1-2*(a*b+a*c+b*c)+2*a*b*c
        D=a*b*c
        assert 1+B+D == a*(1-b)*(1-c)+b*(1-a)*(1-c)+c*(1-a)*(1-b) > 0
        assert 1-B+D == 1+(1-a)*(1-b)*(1-c)+a*b+a*c+b*c > 0
        assert 1-D>0
        assertions+=3
    print('all checks passed')
    print('exact characteristic comparisons per n:',counts)
    print('exact arithmetic assertions:',assertions)
    print('transient squared norms:',sum(v*v for v in v1),sum(v*v for v in v2))
    print('finite checks are not a proof for all block counts or parameter values')


if __name__=='__main__':
    main()
