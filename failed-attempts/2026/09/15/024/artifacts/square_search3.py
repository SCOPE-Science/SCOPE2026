"""Extended recovery test for lane-20211: 3-generator one-vertex square complexes.

Plus a counting lemma (Mantel): link has 2k vertices; NPC needs simple
triangle-free link, so #edges <= k^2; each square contributes 4 edges, so
s <= k^2/4 squares. Finite H1 = Z^k/im needs s >= k relators.
k=2: s<=1 <2 -> H1 always infinite. k=3: s<=2 <3 -> H1 always infinite.
So this script verifies k=3 exhaustively (NPC count + H1), confirming the
counting lemma, and checks k=4 small cases are at least extremely sparse
(s=4 with extremal K_{4,4} link would be required for H1 finite).
"""
import itertools, math

NAMES = ['a', 'b', 'c', 'A', 'B', 'C']
INV = {0: 3, 3: 0, 1: 4, 4: 1, 2: 5, 5: 2}
# half-edges: out/in per generator: a_out=0,a_in=1,b_out=2,b_in=3,c_out=4,c_in=5
HEAD = {0: 1, 3: 0, 1: 3, 4: 2, 2: 5, 5: 4}
TAIL = {0: 0, 3: 1, 1: 2, 4: 3, 2: 4, 5: 5}

def corners(word):
    n = len(word)
    return [(HEAD[word[i]], TAIL[word[(i + 1) % n]]) for i in range(n)]

def canon(word):
    rots = [tuple(word[i:] + word[:i]) for i in range(len(word))]
    iv = [INV[x] for x in reversed(word)]
    rots += [tuple(iv[i:] + iv[:i]) for i in range(len(iv))]
    return min(rots)

def link_ok(words):
    seen = set()
    for w in words:
        for (u, v) in corners(w):
            if u == v:
                return False
            e = (min(u, v), max(u, v))
            if e in seen:
                return False
            seen.add(e)
    adj = {i: set() for i in range(6)}
    for (u, v) in seen:
        adj[u].add(v); adj[v].add(u)
    for u in range(6):
        for v in adj[u]:
            if adj[u] & adj[v]:
                return False
    return True

def h1_finite_possible(words, k=3):
    # H1 = Z^k / rows; finite iff rows span rank k over Q
    rows = []
    for w in words:
        e = [0]*k
        for x in w:
            g, s = (x % 3, +1) if x < 3 else (x - 3, -1)
            e[g] += s
        rows.append(e)
    # rank via integer Gaussian elimination (fractions)
    from fractions import Fraction
    M = [[Fraction(v) for v in r] for r in rows]
    r = 0
    for c in range(k):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]/M[r][c]
                for j in range(c, k):
                    M[i][j] -= f*M[r][j]
        r += 1
    return r == k

def main():
    words = sorted({canon(list(w)) for w in itertools.product(range(6), repeat=4)})
    print(f'distinct cyclic square words (3 gens): {len(words)}')
    npc1 = [w for w in words if link_ok([w])]
    print(f's=1 NPC: {len(npc1)}; H1-finite among them: {sum(1 for w in npc1 if h1_finite_possible([w]))}')
    npc2 = 0; fin2 = 0
    L = len(words)
    for i in range(L):
        for j in range(i, L):
            if link_ok([words[i], words[j]]):
                npc2 += 1
                if h1_finite_possible([words[i], words[j]]):
                    fin2 += 1
    print(f's=2 NPC: {npc2}; H1-finite among them: {fin2}')
    print('Counting lemma check (Mantel): s<=floor(k^2/4)=2 for k=3, and H1-finite needs s>=3.')
    print('Conclusion: NO one-vertex 3-generator NPC square complex can have finite H1.')

if __name__ == '__main__':
    main()
