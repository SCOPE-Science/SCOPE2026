"""Exhaustive ordinary zero-forcing and minimum-set mobility for K_n square K_n, n=2,3,4."""
from collections import Counter, deque
from itertools import combinations

def analyse(n):
    N = n*n
    all_mask = (1 << N)-1
    adjacency = []
    for a in range(N):
        adjacency.append(sum(1 << b for b in range(N)
                             if a != b and (a//n == b//n or a%n == b%n)))

    def forcing(blue):
        while True:
            added = 0
            for v in range(N):
                if (blue >> v) & 1:
                    whites = adjacency[v] & (~blue)
                    if whites and not (whites & (whites-1)):
                        added |= whites
            if not (added & ~blue):
                return blue == all_mask
            blue |= added

    first_size = None
    minima = []
    for k in range(N+1):
        for vertices in combinations(range(N),k):
            blue = sum(1 << v for v in vertices)
            if forcing(blue):
                minima.append(blue)
        if minima:
            first_size = k
            break
    assert first_size == N-2*n+2
    expected = 2*n*(n-1)**(n-1)*n**(n-2)
    assert len(minima) == expected
    index = {s:i for i,s in enumerate(minima)}
    result = {}
    for slide in (True, False):
        neighbors = [set() for _ in minima]
        for i,s in enumerate(minima):
            for old in range(N):
                if not (s >> old) & 1: continue
                for new in range(N):
                    if ((s >> new) & 1) or (slide and not ((adjacency[old] >> new) & 1)):
                        continue
                    j = index.get(s ^ (1 << old) ^ (1 << new))
                    if j is not None:
                        neighbors[i].add(j)
        seen = set()
        sizes = []
        for v in range(len(minima)):
            if v in seen: continue
            seen.add(v); queue = deque([v]); size = 0
            while queue:
                x = queue.popleft(); size+=1
                for y in neighbors[x]:
                    if y not in seen: seen.add(y); queue.append(y)
            sizes.append(size)
        expected_parts = sorted(([1]*4 if n==2 else [expected//2,expected//2]) if slide else [expected])
        assert sorted(sizes) == expected_parts
        edges = sum(len(x) for x in neighbors)//2
        result['TS' if slide else 'TJ'] = (edges, sorted(sizes))
    print('n=%d, min_size=%d, count=%d, TS=%s, TJ=%s' %
          (n,first_size,len(minima),result['TS'],result['TJ']))

if __name__ == '__main__':
    for n in (2,3,4): analyse(n)
    print('Independent direct forcing and mobility checks passed.')
