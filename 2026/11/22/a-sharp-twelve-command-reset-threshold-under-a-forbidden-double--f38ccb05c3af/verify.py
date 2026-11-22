#!/usr/bin/env python3
"""Exhaustive four-state no-00 reset-word census. Python 3 standard library only."""
from collections import Counter, deque
from itertools import permutations, product

N = 4
MAPS = list(product(range(N), repeat=N))
REP = ((3, 2, 1, 2), (1, 3, 2, 0))
EXPECTED = {-1:19440,1:2032,2:17088,3:15456,4:4992,5:3696,
            6:1056,7:984,8:312,9:288,10:72,11:96,12:24}

def image_mask(mask, trans):
    result = 0
    for q in range(N):
        if mask & (1 << q):
            result |= 1 << trans[q]
    return result

def bfs(a, b, prohibit_00=True):
    """Shortest path on (nonempty image subset, previous symbol)."""
    queue = deque([(15, 2, 0)])
    seen = {(15, 2)}
    while queue:
        mask, previous, depth = queue.popleft()
        if mask.bit_count() == 1:
            return depth
        for c, action in enumerate((a, b)):
            if prohibit_00 and c == previous == 0:
                continue
            successor = (image_mask(mask, action), c)
            if successor not in seen:
                seen.add(successor)
                queue.append((*successor, depth + 1))
    return -1

def layer_census(a, b):
    """Independent method: reachable subsets by exact word length and last letter.

    This method uses no BFS queue or global visited set. If both last-letter
    reachable collections repeat as a pair, there is no reset word.
    """
    transitions = []
    for action in (a, b):
        transitions.append([image_mask(s, action) for s in range(16)])
    s0, s1 = {transitions[0][15]}, {transitions[1][15]}
    length = 1
    seen = set()
    while True:
        if any(s.bit_count() == 1 for s in s0 | s1):
            return length
        signature = (frozenset(s0), frozenset(s1))
        if signature in seen:
            return -1
        seen.add(signature)
        # '00' forbidden, so 0 may follow only 1; 1 may follow either.
        next0 = {transitions[0][s] for s in s1}
        next1 = {transitions[1][s] for s in (s0 | s1)}
        s0, s1 = next0, next1
        length += 1

def conjugates(a,b):
    ans = set()
    for perm in permutations(range(N)):
        inv = [0] * N
        for i, j in enumerate(perm):
            inv[j] = i
        aa = tuple(perm[a[inv[i]]] for i in range(N))
        bb = tuple(perm[b[inv[i]]] for i in range(N))
        ans.add((aa, bb))
    return ans

def witness_images(a, b, word):
    mask = 15
    route = [mask]
    for char in word:
        mask = image_mask(mask, (a, b)[int(char)])
        route.append(mask)
    return route

def main():
    hist = Counter()
    maximum_pairs = set()
    ordinary = 0
    compared = 0
    for a in MAPS:
        for b in MAPS:
            d1 = bfs(a, b)
            d2 = layer_census(a, b)
            assert d1 == d2, (a, b, d1, d2)
            hist[d1] += 1
            if d1 == 12:
                maximum_pairs.add((a,b))
            if bfs(a,b,False) != -1:
                ordinary += 1
            compared += 1
    assert compared == 65536
    assert dict(hist) == EXPECTED, (hist, EXPECTED)
    assert ordinary == 51520
    assert ordinary - (65536 - hist[-1]) == 5424
    assert maximum_pairs == conjugates(*REP)
    assert len(maximum_pairs) == 24
    assert bfs(*REP,False) == 6
    assert bfs(*REP,True) == 12
    word = '011101101110'
    assert '00' not in word and len(word) == 12
    route = witness_images(*REP, word)
    assert route[-1].bit_count() == 1
    print('VERIFY_OK')
    print('total=65536 ordinary=51520 no00=46096 ordinary_but_no00_impossible=5424')
    print('histogram=' + repr(dict(sorted(hist.items()))))
    print('extremizers=24 one_state_conjugacy_orbit=24')
    print('representative=' + repr(REP))
    print('ordinary_min=6 admissible_min=12 witness=' + word)
    print('witness_masks=' + repr(route))

if __name__ == '__main__':
    main()
