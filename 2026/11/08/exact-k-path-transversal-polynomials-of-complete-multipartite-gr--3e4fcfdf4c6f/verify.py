"""Direct finite checker for maximal induced P_k-free sets of complete multipartite graphs.

Requires Python 3.9+ standard library only.  Paths are ordinary (not induced) simple paths.
The implementation discovers paths from adjacency; it does not use the occupancy lemma
in its brute-force branch.
"""
from collections import Counter
from itertools import combinations_with_replacement
from math import comb


def compositions_of_order(N):
    for r in range(2, N + 1):
        for sizes in combinations_with_replacement(range(1, N), r):
            if sum(sizes) == N:
                yield sizes


def expected(parts, k):
    N = sum(parts)
    t = (k - 2) // 2
    C = k - 1 - t
    qfull = N - max(parts)
    maximal = Counter()
    if qfull <= t:
        maximal[N] = 1
    else:
        # Balanced (k-1)-vertex layer: at most C-1 from each part.
        p = [1]
        for n in parts:
            pnew = [0] * min(k, len(p) + min(n, C - 1))
            for s, coef in enumerate(p):
                for j in range(min(n, C - 1, k - 1 - s) + 1):
                    pnew[s + j] += coef * comb(n, j)
            p = pnew
        if len(p) > k - 1:
            maximal[k - 1] += p[k - 1]
        for n in parts:
            if n >= C and N - n >= t:
                maximal[n + t] += comb(N - n, t)
    allfree = Counter()
    for s in range(k):
        allfree[s] += comb(N, s)
    for n in parts:
        for b in range(min(t, N - n) + 1):
            for a in range(max(k - b, 0), n + 1):
                allfree[a + b] += comb(n, a) * comb(N - n, b)
    return +maximal, +allfree


def independent_brute(parts, k):
    vp = tuple(i for i, n in enumerate(parts) for _ in range(n))
    N = len(vp)
    adjacency = []
    for i in range(N):
        adj = sum(1 << j for j in range(N) if i != j and vp[i] != vp[j])
        adjacency.append(adj)

    def has_k_path(S):
        if S.bit_count() < k:
            return False
        def extend(endpoint, used, length):
            if length == k:
                return True
            avail = (adjacency[endpoint] & S) & ~used
            while avail:
                vbit = avail & -avail
                avail ^= vbit
                if extend(vbit.bit_length() - 1, used | vbit, length + 1):
                    return True
            return False
        starts = S
        while starts:
            vbit = starts & -starts
            starts ^= vbit
            if extend(vbit.bit_length() - 1, vbit, 1):
                return True
        return False

    feasible = [not has_k_path(S) for S in range(1 << N)]
    allfree = Counter(S.bit_count() for S, yes in enumerate(feasible) if yes)
    maximal = Counter()
    for S, yes in enumerate(feasible):
        if not yes:
            continue
        if all(not feasible[S | (1 << v)] for v in range(N) if not (S >> v) & 1):
            maximal[S.bit_count()] += 1
    return +maximal, +allfree


def main():
    cases = subsets = 0
    for N in range(4, 11):
        for parts in compositions_of_order(N):
            for k in range(4, min(N, 8) + 1):
                got = independent_brute(parts, k)
                want = expected(parts, k)
                assert got == want, (parts, k, got, want)
                cases += 1
                subsets += 1 << N
    for h in range(2, 9):
        for m in range(h + 1, 25):
            even, _ = expected((m, m), 2 * h)
            odd, _ = expected((m, m), 2 * h + 1)
            assert even == Counter({m + h - 1: 2 * comb(m, h - 1)})
            want = Counter({2 * h: comb(m, h) ** 2})
            want[m + h - 1] += 2 * comb(m, h - 1)
            assert odd == want, (h, m, odd, want)
    print(f'VERIFY_OK instances={cases} independently_tested_subsets={subsets} all_and_maximal_polynomials=PASS bipartite_parity_cases=PASS')


if __name__ == '__main__':
    main()
