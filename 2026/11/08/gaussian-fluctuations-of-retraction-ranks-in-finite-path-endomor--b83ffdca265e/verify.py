"""Independent small-case checks for path-graph retraction rank counts.

Run: python3 verify.py (Python 3 standard library only).
This does not prove the asymptotic limit.
"""
from itertools import product
from math import pi, log

def direct(n):
    result = {}
    for origin in range(n):
        for increments in product((-1, 1), repeat=n-1):
            f = [origin]
            for step in increments:
                f.append(f[-1] + step)
            if min(f) < 0 or max(f) >= n:
                continue
            if all(f[f[i]] == f[i] for i in range(n)):
                r = len(set(f))
                result[r] = result.get(r, 0) + 1
    return result

def formula(n):
    hist = {}
    for r in range(2, n+1):
        m = n - r
        vec = [1] * r
        w = [1]
        for _ in range(m):
            vec = [(vec[j-1] if j>0 else 0) +
                   (vec[j+1] if j+1<r else 0) for j in range(r)]
            w.append(vec[0])
        hist[r] = sum(w[l] * w[m-l] for l in range(m+1))
    return hist

for n in range(2, 12):
    observed = direct(n)
    predicted = formula(n)
    assert observed == predicted, (n, observed, predicted)
    print('n=%2d: %s' % (n, observed))

c = (pi*pi/log(2))**(1/3)
for n in (30,100,300):
    hist = formula(n)
    total = sum(hist.values())
    mean = sum(r*count for r,count in hist.items())/total
    mode = max(hist, key=hist.get)
    print('n=%3d mode=%d mean=%.5f, n^(1/3) scale=%.5f' %
          (n,mode,mean,c*n**(1/3)))
print('VERIFY_OK')
