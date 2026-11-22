"""Exact finite tests for nonstandard digit carry synchronization."""
from collections import deque
from itertools import product


def represented_runs(base, exponent):
    level = 2*exponent-1
    top = base**level
    digits = list(range(base-1)) + [base**exponent-1]
    values = {0}
    for j in range(level):
        power = base**j
        values = {x+digit*power for x in values for digit in digits if x+digit*power < top}
    runs = []
    start = last = None
    for x in sorted(values):
        if start is None:
            start = last = x
        elif x == last+1:
            last = x
        else:
            runs.append((start, last))
            start = last = x
    if start is not None:
        runs.append((start,last))
    return runs


def formula(base, exponent):
    k = exponent
    B = base**k
    M = (B-1)//(base-1)
    H = (base**(k-1)-1)//(base-1)
    allowed = []
    for ds in product(range(1,base-1), repeat=k-1):
        V = sum(v*base**i for i,v in enumerate(ds))
        allowed.append((B*V-H+M, B*V+(base-2)*M))
    expected = (base-2)**(k-1)*((base-1)*base**(k-1)-M)
    return allowed, M, expected


def transitions(base, exponent):
    B = base**exponent
    M = (B-1)//(base-1)
    digs = tuple(range(base-1))+(B-1,)
    return [tuple((a+c-digs[(a+c)%base])//base for c in range(-M,1)) for a in range(base)]


def shortest_bfs(base, exponent):
    M = (base**exponent-1)//(base-1)
    maps = transitions(base, exponent)
    start = tuple(range(-M,1))
    layers = {start}
    for length in range(1,2*exponent+2):
        new = set()
        for subset in layers:
            for a in range(base):
                nxt = tuple(sorted({maps[a][c+M] for c in subset}))
                if nxt == (0,):
                    return length
                new.add(nxt)
        layers = new
    raise AssertionError('no reset detected')


def run():
    cases = [(b,k) for b in range(3,9) for k in (2,3)] + [(b,4) for b in (3,4,5,6)]
    count=0
    for b,k in cases:
        bands,M,expected = formula(b,k)
        runs = represented_runs(b,k)
        # Only values in 0..b^(2k-1)-1 can be legal input words.
        actual = set()
        for lo,hi in runs:
            if hi-lo+1 >= M+1:
                actual.update(range(lo+M,hi+1))
        predicted = {A for lo,hi in bands for A in range(lo,hi+1)}
        assert len(predicted) == expected, (b,k,'predicted count')
        assert actual == predicted, (b,k,len(actual),len(predicted))
        assert all(0 <= A < b**(2*k-1) for A in actual)
        count += 1
    for b,k in [(b,k) for b in range(3,9) for k in (1,2)] + [(3,3),(3,4),(4,3),(5,3)]:
        assert shortest_bfs(b,k) == 2*k-1, (b,k,'shortest')
        count += 1
    print('PASS:',count,'exact run and independent carry-subset BFS cases')

if __name__ == '__main__':
    run()
