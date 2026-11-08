#!/usr/bin/env python3
"""Independent fixed-state and cut-quality census for matching-deleted bicliques.

Counts stable configurations by directly evaluating vertexwise cut inequalities,
not by exploring the update graph or using a graph library.
"""
from math import comb


def stable_and_cut(left, right, n, t):
    cut = 0
    for i in range(n):
        left_bit = (left >> i) & 1
        right_bit = (right >> i) & 1
        left_opposites = 0
        right_opposites = 0
        for j in range(n):
            if i == j and i < t:
                continue
            left_opposites += (left_bit != ((right >> j) & 1))
            right_opposites += (right_bit != ((left >> j) & 1))
            cut += (left_bit != ((right >> j) & 1))
        # Closed-neighborhood minority retains a state only when
        # it has at least as many opposite as same opinions in its
        # closed neighborhood (the vertex itself is counted as same).
        if 2*left_opposites < (n-(i<t)+1):
            return False, cut
        if 2*right_opposites < (n-(i<t)+1):
            return False, cut
    return True, cut


def run():
    total_states = total_graphs = 0
    for n in range(3, 9):
        for t in range(n+1):
            observed = []
            for left in range(1 << n):
                for right in range(1 << n):
                    stable, cut = stable_and_cut(left, right, n, t)
                    if stable:
                        observed.append((left, right, cut))
            expected = 2 + (comb(n, n//2) if n % 2 == 0 and t == n else 0)
            assert len(observed) == expected, (n,t,observed)
            if t==n and n%2==0:
                extra = [e for e in observed if e[0]==e[1]]
                assert len(extra)==comb(n,n//2)
                assert all(e[2]==n*n//2 for e in extra)
                assert all(e[0].bit_count()==n//2 for e in extra)
            maximum = n*n-t
            assert any(c==maximum for _,_,c in observed)
            total_states += 1 << (2*n)
            total_graphs += 1
        print(f'n={n}: all {n+1} deletion sizes checked')
    print(f'PASS: {total_graphs} graphs; {total_states} configurations checked')

if __name__ == '__main__':
    run()
