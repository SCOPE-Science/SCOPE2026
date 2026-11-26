from functools import cache
from itertools import permutations
from pathlib import Path
import re
import sys
from time import perf_counter

def literal_overlap(x, y):
    return next((d for d in range(min(len(x), len(y)), 0, -1)
                 if x.endswith(y[:d])), 0)

def replay(witnesses):
    words = [f'{i:04b}' for i in range(16)]
    lengths = set()
    for line in Path(witnesses).read_text().splitlines()[1:]:
        target, expected, moves = re.fullmatch(r'L=(\d+) word_order=[\d,]+ result=([01]+) merges=([\d,;]+)', line).groups()
        live = {(i,i): word for i,word in enumerate(words)}
        for move in moves.strip(';').split(';'):
            a,b,c,d,h = map(int, move.split(','))
            u,v = (a,b),(c,d)
            x,y = live[u],live[v]
            assert u != v and literal_overlap(x,y) == h
            assert max(literal_overlap(p,q) for p,q in permutations(live.values(),2)) == h
            for w in (u,v): del live[w]
            live[a,d] = x + y[h:]
        assert list(live.values()) == [expected] and int(target) == len(expected)
        assert set(words) <= {expected[i:i+4] for i in range(len(expected)-3)}
        lengths.add(len(expected))
    assert lengths == set(range(19,28))
    print('Literal witnesses OK:', sorted(lengths), flush=True)

def census(n):
    # The state is indexed by head label; a value 16 marks an absent head.
    s0 = bytes(range(n))
    O = tuple(tuple(max([d for d in range(1,4) if (u % (1<<d)) == (v // (1<<(4-d)))] + [0])
                    for v in range(n)) for u in range(n))
    @cache
    def path(s):
        active = [(h,t) for h,t in enumerate(s) if t != 16]
        if len(active)==1:
            return 1
        best, pairs = -1, []
        for h,t in active:
            for j,u in active:
                if h==j: continue
                d = O[t][j]
                if d < best: continue
                if d > best: best, pairs = d, []
                pairs.append((h,j,u))
        bits = 0
        next_state = bytearray(s)
        for h,j,u in pairs:
            next_state[h],next_state[j] = u,16
            bits |= path(bytes(next_state))
            next_state[h],next_state[j] = s[h],s[j]
        return bits << best
    bitset = path(s0)
    lengths = [4*n-i for i in range(4*n) if bitset>>i&1]
    if n == 16:
        assert lengths == list(range(27,18,-1))
    print(n, path.cache_info(), lengths, bitset, flush=True)
    path.cache_clear()

if __name__ == '__main__':
    if len(sys.argv) == 3: replay(sys.argv[2])
    start = perf_counter()
    census(int(sys.argv[1]))
    print('elapsed seconds:', round(perf_counter()-start,3), flush=True)
