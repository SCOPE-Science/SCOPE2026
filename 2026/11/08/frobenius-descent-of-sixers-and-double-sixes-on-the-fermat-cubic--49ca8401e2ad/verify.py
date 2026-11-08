"""Exact arithmetic and finite enumeration for the Fermat cubic marking scheme.

Run with Python 3.8 or later, no third-party dependencies.
"""
from itertools import permutations, combinations
from collections import Counter

PAIRINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
ZERO = (0, 0)
ONE = (1, 0)
OMEGA = ((1, 0), (0, 1), (-1, -1))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    a, b = x
    c, d = y
    return (a*c - b*d, a*d + b*c - b*d)


def norm(x):
    a, b = x
    return a*a - a*b + b*b


def determinant(rows):
    s = ZERO
    for perm in permutations(range(4)):
        v = ONE
        for i, j in enumerate(perm):
            v = mul(v, rows[i][j])
        if sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4)) % 2:
            v = neg(v)
        s = add(s, v)
    return s


def make_line(family, a, b):
    rows = []
    for (i, j), e in zip(PAIRINGS[family], (a, b)):
        r = [ZERO]*4
        r[i] = ONE
        r[j] = OMEGA[e]
        rows.append(tuple(r))
    return tuple(rows)


LINE_LABELS = [(f,a,b) for f in range(3) for a in range(3) for b in range(3)]
LINES = [make_line(*label) for label in LINE_LABELS]
assert len(LINE_LABELS)==27 and len(set(LINE_LABELS))==27
FROB = {i: LINE_LABELS.index((f,(-a)%3,(-b)%3))
        for i,(f,a,b) in enumerate(LINE_LABELS)}
assert all(FROB[FROB[i]]==i for i in range(27))


def frob(s):
    return tuple(sorted(FROB[i] for i in s))


def main():
    meet = [[False]*27 for _ in range(27)]
    norms = Counter()
    for i,j in combinations(range(27),2):
        det = determinant(LINES[i]+LINES[j])
        norms[norm(det)] += 1
        meet[i][j] = meet[j][i] = det == ZERO
    assert norms == {0:135, 3:162, 9:54}, norms
    assert all(sum(row)==10 for row in meet)
    # Every nonzero line-pair determinant has norm 3 or 9.
    # Therefore the incidence graph is unchanged in all characteristics != 3.
    skew = {s for s in combinations(range(27),6)
            if all(not meet[i][j] for i,j in combinations(s,2))}
    assert len(skew)==72, len(skew)
    partner={}
    for s in skew:
        t = tuple(i for i in range(27) if i not in s and
                  sum(meet[i][j] for j in s)==5)
        assert t in skew and len(t)==6
        assert sorted(next(j for j in s if not meet[i][j]) for i in t)==list(s)
        partner[s]=t
    assert all(partner[partner[s]]==s and partner[s]!=s for s in skew)
    double_sixes={frozenset((s,partner[s])) for s in skew}
    assert len(double_sixes)==36
    assert {frozenset((frob(s),frob(partner[s]))) for s in skew} == double_sixes
    invariant_sixers = sorted(s for s in skew if frob(s)==s)
    invariant_double = [d for d in double_sixes if
                        frozenset(frob(s) for s in d)==d]
    fixed_halves = [d for d in invariant_double if
                    all(frob(s)==s for s in d)]
    exchanged_halves=[d for d in invariant_double if d not in fixed_halves]
    assert (len(invariant_sixers),len(invariant_double),len(fixed_halves),
            len(exchanged_halves))==(2,4,1,3)
    assert set().union(*[set(d) for d in fixed_halves])==set(invariant_sixers)
    assert all(tuple(sum(LINE_LABELS[i][0]==f for i in s)
                     for f in range(3))==(2,2,2)
               for s in invariant_sixers)
    print('EXACT_DETERMINANT_NORMS',dict(sorted(norms.items())))
    print('FROBENIUS_FIXED_SIXERS',invariant_sixers)
    print('FROBENIUS_STABLE_DOUBLE_SIXES',len(invariant_double),
          'FIXED_HALVES',len(fixed_halves),
          'EXCHANGED_HALVES',len(exchanged_halves))
    print('VERIFY_FERMAT_DOUBLE_SIX_OK sixers=72 double_sixes=36 fixed_sixers=2 fixed_double_sixes=4')

if __name__=='__main__':
    main()
