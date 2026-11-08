"""Exact rational verification of the star Haken--Strobl lifetime identities.
All parameters in this checker are rational; no numerical integration is used.
"""
from fractions import Fraction as F


def solve(a, b):
    a = [[F(x) for x in row] + [F(y)] for row, y in zip(a, b)]
    n = len(b)
    for i in range(n):
        p = next(j for j in range(i, n) if a[j][i])
        a[i], a[p] = a[p], a[i]
        pivot = a[i][i]
        a[i] = [x / pivot for x in a[i]]
        for j in range(n):
            if j != i:
                t = a[j][i]
                a[j] = [x - t*y for x, y in zip(a[j], a[i])]
    return [a[i][-1] for i in range(n)]


def lifetime(m, j, gamma, kappa, hub=False):
    """Integrate p,a,b,y ODE exactly: -generator * integrated = initial."""
    a = [
        [kappa, F(0), F(0), 2*m*j],
        [F(0), F(0), F(0), -2*j],
        [F(0), F(0), gamma, -2*j],
        [-j, j, (m-1)*j, gamma + kappa/2],
    ]
    start = [F(int(hub)), F(0) if hub else F(1,m), F(0), F(0)]
    p, x, b, y = solve(a, start)
    return p + m*x, (p, x, b, y)


def main():
    nchecked = 0
    for m in range(2, 20):
        for j, gamma, kappa in [(F(1),F(1),F(1)),(F(7,3),F(2,5),F(11,6)),(F(-3,5),F(7,4),F(2,3))]:
            leaf, ints = lifetime(m,j,gamma,kappa)
            formula = F(m+1)/kappa + F(m-1)/gamma + (gamma+kappa/2)/(2*j*j)
            assert leaf == formula, (m,j,gamma,kappa,leaf,formula)
            hub, ints_h = lifetime(m,j,gamma,kappa,hub=True)
            assert hub == F(m+1)/kappa
            assert ints[0]==F(1)/kappa and ints_h[0]==F(1)/kappa
            nchecked += 2
    print('EXACT_REDUCED_OK', nchecked, 'initial-state/parameter cases')

if __name__=='__main__':
    main()
