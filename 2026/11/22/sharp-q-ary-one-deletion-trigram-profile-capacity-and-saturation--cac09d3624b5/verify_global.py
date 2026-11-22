"""Independent direct deletion-histogram witness checks; Python 3 stdlib only."""
from collections import Counter
from itertools import product


def debruijn(k, n=5):
    # FKM construction, returned as cyclic list of length k**n.
    a = [0] * (k*n + 1)
    seq = []
    def db(t, p):
        if t > n:
            if n % p == 0:
                seq.extend(a[1:p+1])
        else:
            a[t] = a[t-p]
            db(t+1, p)
            for j in range(a[t-p]+1, k):
                a[t] = j
                db(t+1, t)
    db(1, 1)
    assert len(seq) == k**n
    return seq


def hist3(word):
    return Counter(tuple(word[i:i+3]) for i in range(len(word)-2))


def word(q):
    p = [0,1,0,0]
    s = [0,1,0,1] if q==2 else [0,0,1,2]
    b = debruijn(q)
    return p+b+b[:4]+s


def capacity(q):
    return q**5-2*q**4+2*q**3-3*q**2+3*q+4

for q in (2,3,4,5):
    w = word(q)
    assert len(w) == q**5 + 12
    covered = {tuple(w[i:i+5]) for i in range(len(w)-4)}
    assert len(covered) == q**5
    # Independently recompute all full trigram histograms after deletion.
    outcomes = set()
    for j in range(len(w)):
        x = w[:j] + w[j+1:]
        h = hist3(x)
        outcomes.add(tuple(sorted(h.items())))
    assert len(outcomes) == capacity(q), (q,len(outcomes),capacity(q))
    print(f'q={q} length={len(w)} unique_output_profiles={len(outcomes)} capacity={capacity(q)}')
print('ALL_GLOBAL_CHECKS_PASS')
