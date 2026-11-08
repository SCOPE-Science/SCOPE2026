"""Independent graph-level exhaustive check of synchronous majority on a clique corona.
Run: python3 verify_exhaustive.py
"""
from collections import Counter
from math import comb


def graph(n):
    adj = [[] for _ in range(2*n)]
    for i in range(n):
        for j in range(i+1,n):
            adj[i].append(j)
            adj[j].append(i)
        adj[i].append(n+i)
        adj[n+i].append(i)
    return adj


def iterate(s, adj):
    nxt = 0
    for i, neighbors in enumerate(adj):
        ones = sum((s >> j) & 1 for j in neighbors)
        old = (s >> i) & 1
        if 2*ones > len(neighbors) or (2*ones == len(neighbors) and old):
            nxt |= 1 << i
    return nxt


def target(n):
    if n % 2 == 0:
        b = comb(n,n//2)
        return 2+b, b*(b-1)
    r = (n-1)//2
    return 2, 2*n*comb(n-1,r)+2*comb(n,r)


def main():
    processed = 0
    details = []
    for n in range(2,8):
        adj = graph(n)
        count = Counter()
        max_t = 0
        for x in range(1 << (2*n)):
            processed += 1
            y = iterate(x,adj)
            if y == x:
                count[1] += 1
            elif iterate(y,adj) == x:
                count[2] += 1
            cur = x
            for t in range(10):
                if iterate(iterate(cur,adj),adj) == cur:
                    max_t = max(max_t,t)
                    break
                cur = iterate(cur,adj)
            else:
                raise AssertionError(('unexpected transient',n,x))
        assert (count[1], count[2]) == target(n), (n,count,target(n))
        details.append((n,count[1],count[2],max_t))
    assert processed == sum(1 << (2*n) for n in range(2,8))
    for n,p1,p2,t in details:
        print('n=%d fixed=%d primitive2=%d max_transient=%d' % (n,p1,p2,t))
    print('EXHAUSTIVE_OK %d initial configurations' % processed)

if __name__ == '__main__':
    main()
