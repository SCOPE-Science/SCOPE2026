"""Standalone finite verification for a sharp sorting-supersequence theorem.

Python 3 standard library only. All source words and target orders use distinct
integer labels. Exhaustion checks small finite cases; the general result is
proved symbolically in RESULT.md.
"""
from functools import lru_cache
from itertools import product
from collections import deque


@lru_cache(None)
def path_orders(n):
    if n == 0:
        return ((),)
    if n == 1:
        return ((1,),)
    return tuple(p + (n,) for p in path_orders(n-1)) + tuple(
        p + (n, n-1) for p in path_orders(n-2))


def witness(n):
    if n == 0:
        return ()
    if n == 1:
        return (1,)
    return witness(n - 1) + (n, n - 1)


def contains(word, target):
    j = 0
    for a in word:
        if j < len(target) and a == target[j]:
            j += 1
    return j == len(target)


def fibonacci(k):
    a,b=0,1
    for _ in range(k):
        a,b=b,a+b
    return a


def min_length_bfs(n):
    """Exact breadth-first search of the coverage-progress automaton."""
    orders = path_orders(n)
    start = (0,) * len(orders)
    frontier = deque([(start,0)])
    seen = {start}
    while frontier:
        prog, dep = frontier.popleft()
        if all(prog[t] == len(orders[t]) for t in range(len(orders))):
            return dep,len(seen)
        for a in range(1,n+1):
            nxt = tuple((j + (j < n and orders[i][j] == a)) for i,j in enumerate(prog))
            if nxt not in seen:
                seen.add(nxt)
                frontier.append((nxt,dep+1))
    raise RuntimeError('Unreachable')


def components(n, pattern):
    """Consecutive-path components from overlapping-adjacency mask."""
    out=[]
    begin=1
    for i in range(1,n):
        if not (pattern >> (i-1)) & 1:
            out.append(tuple(range(begin,i+1)))
            begin=i+1
    out.append(tuple(range(begin,n+1)))
    return out


def composed_orders(comps):
    all_parts=[]
    for comp in comps:
        all_parts.append([tuple(comp[i-1] for i in p) for p in path_orders(len(comp))])
    return [sum(parts,()) for parts in product(*all_parts)]


def composed_witness(comps):
    return sum((tuple(comp[i-1] for i in witness(len(comp))) for comp in comps),())


def verify():
    count_target=0
    for n in range(1,12):
        target = path_orders(n)
        w = witness(n)
        assert len(target) == fibonacci(n+1)
        assert len(w) == 2*n-1
        assert len(set(target)) == len(target)
        assert all(contains(w,t) for t in target)
        count_target += len(target)
    exact=[]
    for n in range(1,7):
        m,states=min_length_bfs(n)
        assert m == 2*n-1, (n,m,states)
        exact.append((n,m,states))
    patterns=0
    words=0
    for n in range(1,9):
        for pattern in range(1 << (n-1)):
            comps=components(n,pattern)
            w = composed_witness(comps)
            assert len(w) == 2*n-len(comps)
            target = composed_orders(comps)
            assert len(target) == __import__('math').prod(fibonacci(len(c)+1) for c in comps)
            assert all(contains(w,t) for t in target)
            assert len(set(target)) == len(target)
            patterns+=1
            words+=len(target)
    print('VERIFY_OK')
    print('path tests n=1..11, target orders checked:',count_target)
    print('exact BFS n=1..6 (n,minimum,visited states):',exact)
    print('overlap patterns checked:',patterns,'total realizable orders checked:',words)

if __name__ == '__main__':
    verify()
