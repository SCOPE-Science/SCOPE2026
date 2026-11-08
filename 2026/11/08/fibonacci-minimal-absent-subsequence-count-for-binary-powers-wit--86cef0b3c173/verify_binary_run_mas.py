#!/usr/bin/env python3
"""Reproducible independent finite checks of a binary scattered-subsequence formula.

Two independent constructions are used: direct subword enumeration, and a
position-by-position bridge enumerator. Only the algebraic proof establishes
validity for unbounded positive parameters.
"""
from itertools import product
from functools import lru_cache


def embeds(s, w):
    pos = 0
    for symbol in w:
        if pos < len(s) and symbol == s[pos]:
            pos += 1
    return pos == len(s)


def direct_minimal_absent(w):
    n = len(w)
    subseqs = {''}
    for symbol in w:
        subseqs |= {u + symbol for u in tuple(subseqs)}
    answer = set()
    # Every minimal absent word is one letter longer than an embedded prefix.
    for size in range(1, n + 2):
        for chars in product('01', repeat=size):
            u = ''.join(chars)
            if u in subseqs:
                continue
            if all(u[:j] + u[j+1:] in subseqs for j in range(size)):
                answer.add(u)
    return answer


def bridge_minimal_absent(w):
    n = len(w)
    answers = set()
    # i is matched greedy position (1-based), j the preceding position.
    def visit(u, j, i):
        bridge = w[j:i]
        for c in '01':
            if c not in bridge:
                continue
            q = w.find(c, i)
            if q < 0:
                answers.add(u + c)
            else:
                visit(u + c, i, q + 1)
    for c in '01':
        first = w.find(c)
        if first >= 0:
            visit(c, 0, first + 1)
    return answers


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def run_graph_count(a, b, k):
    n = 2*k
    @lru_cache(None)
    def f(j):
        if j >= n:
            return 1
        same = f(j+2)
        opposite = f(j+1) if (a if j % 2 == 0 else b) >= 2 else f(j+3)
        return same + opposite
    return f(1) + f(2)


def main():
    tested = 0
    positions = 0
    for a in range(2, 5):
        for b in range(2, 5):
            for k in range(1, 5):
                n = k*(a+b)
                if n > 18:
                    continue
                w = ('0'*a + '1'*b)*k
                direct = direct_minimal_absent(w)
                bridge = bridge_minimal_absent(w)
                assert direct == bridge, (a, b, k, direct ^ bridge)
                expect = fibonacci(2*k+2)
                assert len(direct) == expect == run_graph_count(a,b,k), (a,b,k,len(direct),expect)
                positions += sum(map(len, direct))
                tested += 1
    # Test arbitrary weights and large repetition counts by the graph count
    for a in range(2, 15):
        for b in range(2, 15):
            for k in range(1, 25):
                assert run_graph_count(a,b,k) == fibonacci(2*k+2)
    print('VERIFY_OK', 'direct_vs_bridge_cases', tested,
          'total_minimal_absent_symbol_positions', positions,
          'graph_cases', 13*13*24,
          'first_six_counts', [fibonacci(2*k+2) for k in range(1,7)])

if __name__ == '__main__':
    main()
