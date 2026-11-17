"""Exact exhaustive test for four-or-more-state GHM on labelled double stars."""
from itertools import product

def formula(q, a, b):
    A = lambda k: q**k - (q-1)**k
    B = lambda k: (q-1)**k - (q-4)**k + q**k - (q-3)**k
    return A(a)*B(b) + A(b)*B(a)

def check(q, a, b):
    n = a+b+2
    adj = [[1]+list(range(2, 2+a)), [0]+list(range(2+a, n))]
    adj.extend([[0] for _ in range(a)])
    adj.extend([[1] for _ in range(b)])
    terminal = 0
    max_time = 0
    for x in product(range(q), repeat=n):
        t = 0
        while any(x):
            old = x
            x = tuple((s+1) % q if s else int(any(old[j] == 1 for j in adj[i]))
                      for i, s in enumerate(old))
            t += 1
            if t > q+2:
                raise AssertionError((q,a,b,old,'failed cutoff'))
        max_time = max(max_time,t)
        terminal += t == q+2
    assert max_time == q+2
    assert terminal == formula(q,a,b), (q,a,b,terminal,formula(q,a,b))
    return f'q={q} a={a} b={b} states={q**n} max={max_time} terminal={terminal}'

if __name__ == '__main__':
    cases = [(4,1,1),(4,1,2),(4,2,2),(4,2,3),(4,3,3),
             (5,1,1),(5,1,2),(5,2,2),(5,2,3),
             (6,1,1),(6,1,2),(6,2,2),(7,1,1),(7,1,2)]
    for p in cases:
        print(check(*p))
    print('PASS all exhaustive instances')
