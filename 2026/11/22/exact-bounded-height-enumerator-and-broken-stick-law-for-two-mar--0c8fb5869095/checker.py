#!/usr/bin/env python3
"""Independent subsequence-witness and polynomial checks; Python 3 standard library only."""
from collections import deque
from itertools import product


def shortest_distinguishing_subsequence(longer, shorter):
    """BFS in the two greedy matching automata, no gap/height formula used."""
    def next_pos(word, start, symbol):
        p = word.find(symbol, start)
        return None if p < 0 else p + 1

    pending = deque([(0, 0, 0)])
    visited = {(0, 0)}
    while pending:
        p, q, depth = pending.popleft()
        for symbol in '01':
            np = next_pos(longer, p, symbol)
            if np is None:
                continue
            nq = next_pos(shorter, q, symbol)
            if nq is None:
                return depth + 1
            state = (np, nq)
            if state not in visited:
                visited.add(state)
                pending.append((np, nq, depth + 1))
    raise AssertionError('The longer word should have a distinguishing subsequence')


def height_via_insertions(word):
    """Compute h using the published insertion characterization, not our formula."""
    return max(shortest_distinguishing_subsequence(word[:i]+s+word[i:], word)
               for i in range(len(word)+1) for s in '01')


def predicted_height(a, b, c):
    zeros = a+b+c
    candidates = [2]  # deletion of either one-marker
    if a:
        candidates.append(min(zeros, a + (1 if b == 0 else 2)))
    if b:
        candidates.append(min(zeros, b + (1 if a == 0 or c == 0 else 2)))
    if c:
        candidates.append(min(zeros, c + (1 if b == 0 else 2)))
    return max(candidates) + 1


def S(m):
    return {j: 1 for j in range(1, m+1)}


def add(a, b, factor=1):
    for k, v in b.items():
        a[k] = a.get(k, 0) + factor*v
    return a


def mul(a, b):
    out = {}
    for x, cx in a.items():
        for y, cy in b.items():
            out[x+y] = out.get(x+y, 0) + cx*cy
    return out


def height_at_most_poly(H):
    assert H >= 3
    s1, s2, s3 = S(H-1), S(H-2), S(H-3)
    out = {0: 1}
    add(out, s1, 3)
    add(out, mul(s2,s2))
    add(out, mul({1:1},s2), 2)
    add(out, mul({x:1 for x in range(2,H-1)},s3),2)
    add(out, mul(mul(s3,s3),s3))
    return out


def run_checks():
    pairs = 0
    for zeros in range(0, 13):
        for a in range(zeros+1):
            for b in range(zeros-a+1):
                c = zeros-a-b
                word = '0'*a+'1'+'0'*b+'1'+'0'*c
                observed = height_via_insertions(word)
                expected = predicted_height(a,b,c)
                assert observed == expected, (a,b,c,observed,expected)
                pairs += 1
    polynomial_cases = 0
    for H in range(3,19):
        pol = height_at_most_poly(H)
        for zeros in range(0,23):
            direct = sum(predicted_height(a,b,zeros-a-b)<=H
                         for a in range(zeros+1)
                         for b in range(zeros-a+1))
            assert pol.get(zeros,0) == direct, (H,zeros,direct,pol.get(zeros,0))
            polynomial_cases += 1
    print(f'PASS exact_generic_insertion={pairs} polynomial_coefficients={polynomial_cases}')

if __name__ == '__main__':
    run_checks()
