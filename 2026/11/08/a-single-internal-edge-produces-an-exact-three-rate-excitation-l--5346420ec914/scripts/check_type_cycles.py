"""Finite type-graph proof checker for 3-color successor-contact dynamics.

Usage: python check_type_cycles.py
No third-party dependencies.
"""
from itertools import combinations, product
from fractions import Fraction

def subsets(include_empty=True):
    cs = (0, 1, 2)
    return [frozenset(s) for k in range(0 if include_empty else 1, 4)
            for s in combinations(cs, k)]

def cycle_max(colors, edges):
    n = len(colors)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    best = Fraction(0)
    cycles = 0
    def walk(start, u, visited, weight):
        nonlocal best, cycles
        for v in adj[u]:
            d = (colors[v]-colors[u]) % 3
            delta = 0 if d == 0 else (1 if d == 1 else -1)
            if v == start and len(visited) >= 3:
                cycles += 1
                best = max(best, Fraction(weight+delta, len(visited)))
            elif v > start and v not in visited:
                walk(start,v,visited | {v},weight+delta)
    for start in range(n):
        walk(start,start,{start},0)
    return best, cycles

def test():
    cases = 0
    by_rate = {Fraction(0):0,Fraction(3,4):0,Fraction(1):0}
    max_cycles = 0
    for a,b in product(range(3),repeat=2):
        for ordinary in subsets():
            for shore in subsets(include_empty=False):
                colors = [a,b]+list(sorted(ordinary))+list(sorted(shore))
                n_A = 2+len(ordinary)
                edges = [(0,1)]+[(u,v) for u in range(n_A)
                                           for v in range(n_A,len(colors))]
                rate,cycle_count = cycle_max(colors,edges)
                max_cycles = max(max_cycles,cycle_count)
                A = ordinary | {a,b}
                triangle = (a != b and (set(range(3))-{a,b}).pop() in shore)
                six = (len(A) == 3 and len(shore) == 3)
                four = (len(A) >= 2 and len(shore) >= 2 and len(A | shore)==3)
                expected = Fraction(1) if triangle or six else Fraction(3,4) if four else Fraction(0)
                if rate != expected:
                    raise AssertionError((a,b,ordinary,shore,rate,expected))
                by_rate[rate] += 1
                cases += 1
    assert cases == 504
    print('All 504 canonical color-support type graphs exhaustively passed.')
    print('Activity class counts over type patterns:',[(str(k),by_rate[k]) for k in sorted(by_rate)])
    print('Maximum oriented simple cycles examined for one type graph:',max_cycles)

if __name__=='__main__':test()
