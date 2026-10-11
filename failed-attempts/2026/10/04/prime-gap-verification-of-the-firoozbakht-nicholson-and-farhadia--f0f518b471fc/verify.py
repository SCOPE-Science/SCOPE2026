#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80

data = [
    (81, 1552, 426181820436140029),
    (82, 1572, 428472240920394477),
    (83, 1676, 477141032543986017),
    (84, 1724, 1524717378371224128),
]

def ln(x):
    return Decimal(x).ln()

def f_nicholson(n):
    n = Decimal(n)
    L = (n * n.ln()).ln()
    return (L - 1) * L

def f_farhadian(n):
    n = Decimal(n)
    lnn = n.ln()
    A = (n * lnn).ln()                    # ln(n ln n)
    inner = n * (n * lnn).ln()            # n ln(n ln n)
    correction = lnn.ln() - inner.ln().ln()
    return (A - 1) * (A + correction)

for i, g, n in data:
    fn = f_nicholson(n)
    ff = f_farhadian(n)
    assert Decimal(g) < ff < fn, (i, g, ff, fn)

# Endpoint and record data used in the statement.
assert 18470057946260698231 < 18571673432051830099 < 20733746510561442863
assert 20733746510561442863 < 68068810283234182907 < 101412319996363309069

print("VERIFY_OK")
for i, g, n in data:
    print(i, g, f_nicholson(n), f_farhadian(n))
