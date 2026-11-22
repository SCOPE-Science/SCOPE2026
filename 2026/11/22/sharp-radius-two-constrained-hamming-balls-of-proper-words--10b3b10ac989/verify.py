"""Independent finite checks of radius-two Hamming spheres in proper word spaces.
Uses no third-party modules. Run: python verify.py
"""
from itertools import product
from collections import Counter


def proper_words(q, n):
    for x in product(range(q), repeat=n):
        if all(x[i] != x[i+1] for i in range(n-1)):
            yield x


def direct_ball(q, x):
    """Independent changed-coordinate enumeration, counting outputs directly."""
    n = len(x)
    ys = {x}
    for i in range(n):
        for a in range(q):
            if a == x[i]:
                continue
            y = x[:i] + (a,) + x[i+1:]
            if all(y[t] != y[t+1] for t in range(n-1)):
                ys.add(y)
    for i in range(n):
        for j in range(i+1, n):
            for a in range(q):
                if a == x[i]:
                    continue
                for c in range(q):
                    if c == x[j]:
                        continue
                    y = list(x)
                    y[i], y[j] = a, c
                    if all(y[t] != y[t+1] for t in range(n-1)):
                        ys.add(tuple(y))
    return len(ys)


def local_formula(q, x):
    n = len(x)
    if n == 1:
        return q
    u = []
    for i in range(n):
        blocked = {x[i]}
        if i:
            blocked.add(x[i-1])
        if i+1 < n:
            blocked.add(x[i+1])
        u.append(q-len(blocked))
    adjacent = []
    for i in range(n-1):
        four = {x[i],x[i+1]}
        if i:
            four.add(x[i-1])
        if i+2<n:
            four.add(x[i+2])
        a = q-1-int(i>0)
        b = q-1-int(i+2<n)
        adjacent.append(a*b-q+len(four))
    return 1+sum(u)+sum(u[i]*u[j] for i in range(n) for j in range(i+2,n))+sum(adjacent)


def minimum(q,n):
    return (q-3)**2*n*(n-1)//2+(4*q-11)*n+14-3*q


def maximum(q,n):
    return (q-2)**2*n*(n-1)//2+3*q-5


def run():
    instances = 0
    summaries = []
    for q,nmax in [(3,9),(4,8),(5,7),(6,6)]:
        for n in range(2,nmax+1):
            histogram = Counter()
            minima = maxima = 0
            for x in proper_words(q,n):
                predicted = local_formula(q,x)
                actual = direct_ball(q,x)
                assert predicted == actual,(q,n,x,predicted,actual)
                histogram[actual] += 1
                instances += 1
                if n>=5:
                    if actual == minimum(q,n):
                        minima+=1
                        assert all(x[i]==x[i+3] for i in range(n-3))
                    if actual == maximum(q,n):
                        maxima+=1
                        assert all(x[i]==x[i+2] for i in range(n-2))
            assert sum(histogram.values()) == q*(q-1)**(n-1)
            if n>=5:
                assert min(histogram)==minimum(q,n)
                assert max(histogram)==maximum(q,n)
                assert minima==q*(q-1)*(q-2)
                assert maxima==q*(q-1)
            summaries.append((q,n,min(histogram),max(histogram)))
    print('VERIFIED',instances,'source words; local formula and, when n>=5, sharp bounds and rigid equality cases')
    print('SAMPLE_SUMMARIES',summaries)

if __name__=='__main__':
    run()
