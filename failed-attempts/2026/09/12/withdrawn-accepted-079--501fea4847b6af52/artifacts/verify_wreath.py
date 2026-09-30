"""Verify wreath class recursion for H_n = Aut(rooted binary tree height n).

H_0 = 1; H_{n+1} = (H_n x H_n) semi S2.
Represent H_n as permutations of 2^n leaves (faithful action).
Compute conjugacy-class counts for n<=3 by brute force and check
c_0=1, c_{n+1} = c_n(c_n+1)/2 + c_n.
"""
import itertools

def wreath_gens(n):
    # leaves labelled 0..2^n - 1; binary splitting: left half / right half
    # generators: swaps at each internal node. Build permutation list.
    N = 2 ** n
    gens = []
    # for each level k=1..n, each block: swap the two halves of each block of size 2^k
    for k in range(1, n + 1):
        block = 2 ** k
        half = block // 2
        for start in range(0, N, block):
            p = list(range(N))
            for j in range(half):
                a = start + j
                b = start + half + j
                p[a], p[b] = p[b], p[a]
            gens.append(tuple(p))
    return N, gens

def compose(p, q):
    # apply q then p? consistent convention; conjugacy count independent
    return tuple(p[q[i]] for i in range(len(p)))

def group_closure(N, gens):
    ident = tuple(range(N))
    G = {ident}
    stack = [ident]
    while stack:
        g = stack.pop()
        for s in gens:
            for h in (compose(s, g), compose(g, s)):
                if h not in G:
                    G.add(h)
                    stack.append(h)
    return G

def class_count(G):
    # brute-force conjugacy: x ~ y iff exists g: g x g^{-1} = y
    # permutations: inverse + compose
    def inv(p):
        q = [0]*len(p)
        for i, v in enumerate(p):
            q[v] = i
        return tuple(q)
    Glist = list(G)
    seen = set()
    ncl = 0
    for x in Glist:
        if x in seen:
            continue
        ncl += 1
        orb = set()
        for g in Glist:
            orb.add(compose(compose(g, x), inv(g)))
        seen |= orb
    return ncl

def main():
    counts = {}
    for n in range(0, 4):
        N, gens = wreath_gens(n)
        G = group_closure(N, gens)
        c = class_count(G)
        counts[n] = (len(G), c)
        print(f"n={n} leaves={N} |H_n|={len(G)} classes={c}")
    # check recursion
    c = {n: counts[n][1] for n in counts}
    for n in range(0, 3):
        pred = c[n]*(c[n]+1)//2 + c[n]
        print(f"recursion n={n}: predicted c_{n+1}={pred}, actual={c[n+1]}, "
              f"match={pred==c[n+1]}")
    # orders: |H_{n+1}| = 2|H_n|^2
    for n in range(0, 3):
        print(f"order check n={n}: 2*{counts[n][0]}^2={2*counts[n][0]**2} "
              f"vs {counts[n+1][0]}")

if __name__ == "__main__":
    main()
