"""Exhaustive checks for the abstract automorphism groups of cyclic and wheel partial-isometry monoids.

A permutation is admitted precisely when it preserves equality of the positive
pair distances. The finite check tests the structural normalizer criterion,
not an independent exhaustive search over all monoid self-bijections.
"""
from itertools import permutations
from math import gcd, factorial


def cyclic_distance(n, a, b):
    s = (a-b) % n
    return min(s, n-s)


def distance_table_cycle(n):
    return [[cyclic_distance(n, a, b) for b in range(n)] for a in range(n)]


def distance_table_wheel(n):
    a = distance_table_cycle(n)
    return [[0 if i==j else (1 if a[i][j] == 1 else 2) for j in range(n)]+[1] for i in range(n)] + [[1]*n + [0]]


def is_color_normalizer(pi, dist):
    seen = {}
    for i in range(len(pi)):
        for j in range(i+1,len(pi)):
            before = dist[i][j]
            after = dist[pi[i]][pi[j]]
            if before in seen:
                if seen[before] != after:
                    return False
            else:
                seen[before] = after
    return len(set(seen.values())) == len(seen)


def affine_permutations(n):
    return {tuple((a+u*i) % n for i in range(n)) for a in range(n)
            for u in range(n) if gcd(u,n)==1}


def dihedral_wheel(n):
    return {tuple((a+s*i) % n for i in range(n))+(n,)
            for a in range(n) for s in (1,-1)}


def main():
    for n in range(3,9):
        actual={p for p in permutations(range(n)) if is_color_normalizer(p,distance_table_cycle(n))}
        expected=affine_permutations(n)
        assert actual==expected, ("cycle",n,len(actual),len(expected))
        print("cycle",n,"normalizers",len(actual))
    for n in range(5,8):
        D=distance_table_wheel(n)
        actual={p for p in permutations(range(n+1)) if is_color_normalizer(p,D)}
        expected=dihedral_wheel(n)
        assert actual==expected, ("wheel",n,len(actual),len(expected))
        print("wheel",n,"normalizers",len(actual))
    print('AFFINE_DIHEDRAL_METRIC_NORMALIZERS_VERIFIED')


if __name__ == "__main__":
    main()
