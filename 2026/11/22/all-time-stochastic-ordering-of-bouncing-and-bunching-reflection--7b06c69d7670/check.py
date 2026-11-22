"""Independent exact finite-state checks for the reflection-protocol CDF ordering.

Run with `python3 check.py`. Python standard library only.
The finite calculations supplement, and do not replace, the general proof.
"""
from fractions import Fraction as F


def chain(n, f, b, mode):
    c = 1 - f - b
    assert n >= 2 and min(f, b, c) >= 0 and f*b > 0
    states = [(x, h) for x in range(1, n) for h in (1, -1)]
    idx = {s: i for i, s in enumerate(states)}
    m = len(states)
    Q = [[F(0) for _ in states] for _ in states]
    absorb = [F(0) for _ in states]
    for i, (x, h) in enumerate(states):
        Q[i][i] += c
        for weight, step in ((f, h), (b, -h)):
            y = x + step
            if y == n:
                absorb[i] += weight
            elif y < 1:
                new_h = 1 if mode == 'bounce' else h
                Q[i][idx[(1, new_h)]] += weight
            else:
                Q[i][idx[(y, step)]] += weight
        assert sum(Q[i]) + absorb[i] == 1
    return states, idx, Q, absorb


def row_history(Q, initial, horizon):
    v = [F(int(k == initial)) for k in range(len(Q))]
    rows = []
    for t in range(horizon + 1):
        rows.append(v[:])
        v = [sum(v[i]*Q[i][j] for i in range(len(Q))) for j in range(len(Q))]
    return rows


def cdf(rows):
    return [1-sum(r) for r in rows]


def coefficients_conv(a, b, horizon):
    return [sum(a[j]*b[t-j] for j in range(t+1)) for t in range(horizon+1)]


def verify(n, f, b, horizon):
    states, idx, B, absorb_B = chain(n, f, b, 'bounce')
    states2, idx2, U, absorb_U = chain(n, f, b, 'bunch')
    assert states == states2 and absorb_B == absorb_U
    m = len(states)
    w = idx[(1, -1)]
    # Rank-one change at the reflecting wall only.
    for i in range(m):
        for j in range(m):
            expected = f*(int(j == idx[(1, 1)])-int(j == w)) if i == w else 0
            assert B[i][j]-U[i][j] == expected
    if n == 2:
        f_U2 = [F(1)] + [F(0)]*horizon
    else:
        rows_U2 = row_history(U, idx[(2, 1)], horizon)
        s = [sum(row) for row in rows_U2]
        f_U2 = [F(0)] + [s[t-1]-s[t] for t in range(1, horizon+1)]
    a, d = b+(1-f-b), f+(1-f-b)
    geom = [sum(a**j*d**(t-j) for j in range(t+1)) for t in range(horizon+1)]
    kernel = coefficients_conv(f_U2, geom, horizon)
    checks = 0
    strict_seen = 0
    for init in range(m):
        rows_B = row_history(B, init, horizon)
        rows_U = row_history(U, init, horizon)
        left = [cdf(rows_B)[t]-cdf(rows_U)[t] for t in range(horizon+1)]
        r = [row[w] for row in rows_B]
        rhs_inner = coefficients_conv(r, kernel, horizon)
        rhs = [F(0), F(0)] + [(f-b)*f*rhs_inner[t-2] for t in range(2,horizon+1)]
        for t in range(horizon+1):
            assert left[t] == rhs[t], (n, f, b, t, states[init], left[t], rhs[t])
            assert left[t]*(f-b) >= 0, (n, f, b, t)
            checks += 2
        if f != b and any(x != 0 for x in left):
            strict_seen += 1
    assert strict_seen == (m if n >= 3 and f != b else (1 if n == 2 and f != b else 0))
    return checks


def main():
    total = 0
    combinations = [
      (F(3,4),F(1,4)), (F(1,4),F(3,4)), (F(1,2),F(1,2)),
      (F(1,2),F(1,4)), (F(1,4),F(1,2)), (F(1,3),F(1,3)),
      (F(2,5),F(1,5)), (F(1,5),F(2,5))]
    for n in (2,3,4,5,6):
      for f, b in combinations:
        total += verify(n,f,b,36)
    print(f'PASS {total} exact rational temporal identities and sign checks across 40 finite systems')
    print('Covered both reflection protocols, lazy and non-lazy dynamics, and N=2 boundary degeneracy.')

if __name__ == '__main__':
    main()
