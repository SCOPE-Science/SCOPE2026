"""Exact checks for lag-one reconstruction under vertex-clock updates."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import prod


def observed_stars(edges, n):
    return Counter(frozenset(i for i, edge in enumerate(edges) if v in edge)
                   for v in range(n))


def reconstruct(m, n, get_stat, r, omega):
    # Use inclusion-exclusion on lag-one statistics to count common endpoints.
    def hits(S):
        return n / (omega * (r-1)**len(S)) * sum(
            (-1)**(len(S)-a) * (get_stat(T)-1)
            for a in range(len(S)+1) for T in combinations(S,a))

    neighbors = [set() for _ in range(m)]
    for i,j in combinations(range(m),2):
        if hits((i,j)):
            neighbors[i].add(j)
            neighbors[j].add(i)
    stars = set()
    for i, adj in enumerate(neighbors):
        for j in adj:
            stars.add(frozenset({i,j} | {k for k in adj-{j} if hits((i,j,k))}))
    answer = Counter(stars)
    for i in range(m):
        missing = 2 - sum(i in S for S in stars)
        assert 0 <= missing <= 2
        if missing:
            answer[frozenset({i})] = missing
    return answer


def projected_kernel(edges,n,S,p,q,omega):
    states = tuple(product((0,1), repeat=len(S)))
    K = ((1-p,p),(q,1-q))
    return tuple(tuple((1-omega)*(a==b) + omega/n * sum(
        prod(K[x][y] if v in edges[j] else x==y for j,x,y in zip(S,a,b))
        for v in range(n)) for b in states) for a in states)


def from_kernel(kernel,k,p,q):
    states = tuple(product((0,1), repeat=k))
    pi = p/(p+q)
    masses = [prod(pi if x else 1-pi for x in a) for a in states]
    h = [prod(x-pi for x in a) for a in states]
    assert all(sum(row)==1 for row in kernel)
    assert all(sum(masses[i]*kernel[i][j] for i in range(len(states)))==masses[j]
               for j in range(len(states)))
    return sum(masses[i]*kernel[i][j]*h[i]*h[j]
               for i,j in product(range(len(states)),repeat=2))/(pi*(1-pi))**k


def formula(edges,n,S,r,omega):
    return 1-omega+omega/n*sum(r**sum(v in edges[i] for i in S) for v in range(n))


def check_witness(a,b,n,gap):
    p,q,omega = F(1,2),F(1,4),F(2,3)
    r = 1-p-q
    aa,bb = {},{}
    for k in range(4):
        for S in combinations(range(len(a)),k):
            ka,kb = [projected_kernel(e,n,S,p,q,omega) for e in (a,b)]
            if k<=2:
                assert ka==kb
            aa[S],bb[S] = (from_kernel(kernel,k,p,q) for kernel in (ka,kb))
            assert aa[S]==formula(a,n,S,r,omega) and bb[S]==formula(b,n,S,r,omega)
    assert bb[(0,1,2)]-aa[(0,1,2)] == gap
    assert observed_stars(a,n) != observed_stars(b,n)
    for edges, values in [(a,aa),(b,bb)]:
        assert reconstruct(len(edges),n,lambda S: values[tuple(sorted(S))],r,omega) == observed_stars(edges,n)
    print(f'N={n}: labelled order-two kernels coincide; the order-three gap is {gap}')


def main():
    check_witness([(0,1),(0,2),(0,3),(2,3),(1,3),(1,2)],
                  [(2,3),(1,3),(1,2),(0,1),(0,2),(0,3)],4,F(9,128))
    check_witness([(0,1),(0,2),(0,3),(4,5),(5,6),(6,4)],
                  [(0,1),(1,2),(2,0),(3,4),(3,5),(3,6)],7,F(9,224))
    count = 0
    for n in range(2,6):
        pairs = list(combinations(range(n),2))
        for choice in product((0,1),repeat=len(pairs)):
            edges = [e for e, present in zip(pairs,choice) if present]
            truth = observed_stars(edges,n)
            if frozenset() in truth:
                continue
            r,omega = F(-1,5),F(3,5)
            f = lambda S: formula(edges,n,S,r,omega)
            assert reconstruct(len(edges),n,f,r,omega)==truth
            count += 1
    print(f'PASS: {count} additional simple graphs on at most five vertices without isolates')


if __name__ == '__main__':
    main()
