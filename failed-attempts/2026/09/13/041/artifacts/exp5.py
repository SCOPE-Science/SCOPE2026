"""Exp5: construct X_{sigma=1}/F13 candidate as Kummer sandwich via degree-2 isogeny.

Mechanism (Katsura-Kondo / Dolgachev-Keum, char p != 2): Km(A) has 16 nodes; take double cover
branched over an even set of 8 nodes (+/- tropes) -> new K3 with sigma dropped by 1.
Arithmetic question: can the 8-node set be F13-rational?

On Km(E_ss^2): 16 nodes = A[2] = V x V, V = E[2] = {0, a, b, c} with Frob: 0->0, a->a (rational
2-torsion), b<->c. So 16 nodes = pairs. Frob-fixed nodes: 2x2 = 4. Frob-orbits: 4 fixed + 6 pairs.
An 8-subset S with Frob(S)=S and even-set condition (sum zero in A[2]) gives rational branch locus.
Count such S; also target point count #X=456 as check later.
"""
import itertools
p = 13
# label V = {0,1,2,3}, Frob swaps 2<->3
V = [0, 1, 2, 3]
nodes = [(u, v) for u in V for v in V]
def frob(n):
    def f(x): return 3 if x == 2 else (2 if x == 3 else x)
    return (f(n[0]), f(n[1]))
# group law: V = F2^2: 0=00,1=10,2=01,3=11
rep = {0: (0,0), 1: (1,0), 2: (0,1), 3: (1,1)}
def add(n, m):
    for k, (rr, ss) in rep.items():
        pass
    r = (rep[n[0]][0]+rep[m[0]][0])%2, (rep[n[0]][1]+rep[m[0]][1])%2
    s = (rep[n[1]][0]+rep[m[1]][0])%2, (rep[n[1]][1]+rep[m[1]][1])%2
    inv = {v: k for k, v in rep.items()}
    return (inv[r], inv[s])
O = (0, 0)
def subset_sum(S):
    s = O
    for n in S:
        s = add(s, n)
    return s
fixed = [n for n in nodes if frob(n) == n]
pairs = []
seen = set()
for n in nodes:
    if frob(n) != n and n not in seen:
        pairs.append((n, frob(n)))
        seen.add(n); seen.add(frob(n))
print("#fixed:", len(fixed), "#pairs:", len(pairs))
# Frob-stable 8-sets: choose k fixed + (8-k)/2 pairs, 8-k even
count_even = 0
count_total = 0
examples = []
for k in [0, 2, 4, 6, 8]:
    if k > 4 or (8-k)//2 > 6: continue
    for F in itertools.combinations(fixed, k):
        for P in itertools.combinations(pairs, (8-k)//2):
            S = set(F)
            for pr in P:
                S.add(pr[0]); S.add(pr[1])
            count_total += 1
            if subset_sum(S) == O:
                count_even += 1
                if len(examples) < 5:
                    examples.append(sorted(S))
print("Frob-stable 8-sets:", count_total, " even (sum 0):", count_even)
for e in examples:
    print(e)
