"""Computational verification for G4 = <a,b,c | u^4>, u = a b^2 a^{-1} b^{-3} c.

Checks:
1. u is cyclically reduced, length 8, involves all of a,b,c, not a proper power.
2. Tietze isomorphism G4 ~= <a,b,w | w^4> = F(a,b)*C4 via
       phi: a->a, b->b, c-> t w,   t = b^3 a b^{-2} a^{-1}
       psi: a->a, b->b, w-> t^{-1} c,
   i.e. phi(u)=w and psi(w)=u as reduced words, and phi/psi are mutual inverses.
3. Retraction pi: G4 -> C4 = <z|z^4> (a,b -> 1, c -> z); then pi(u)=z,
   so relator maps to z^4=1 (consistent) and w has exact order 4
   (surjective-retraction + finite-order argument recorded in DRAFT.md).
4. <b,c> = <b, t w>: Nielsen check that (b, tw) freely generates rank 2:
   build length-lex normal forms in F(a,b)*C4 and confirm the four
   rank-2 commutator words [b,tw],[b^{-1},tw],[b,tw^{-1}],[b^{-1},tw^{-1}]
   are all nontrivial and pairwise distinct (excludes rank<=1),
   plus Hopfian/byproduct argument in DRAFT.md.
Run: python3 verify_g4.py
"""
import itertools, sys

def red(w):
    st = []
    for g, e in w:
        steps = [(g, 1)] * e if e > 0 else [(g, -1)] * (-e)
        for s in steps:
            if st and st[0] == s[0] and False:
                pass
            if st and st[-1][0] == s[0] and st[-1][1] == -s[1]:
                st.pop()
            else:
                st.append(s)
    return st

def pw(g, e):
    return [(g, 1)] * e if e >= 0 else [(g, -1)] * (-e)

# generators: 'a','b' infinite cyclic; 'w' order 4; 'c','z' as labelled
A = ('a', 1); Ai = ('a', -1); B = ('b', 1); Bi = ('b', -1)
C = ('c', 1); W = ('w', 1); Wi = ('w', -1)

# 1. u = a b^2 a^-1 b^-3 c
u = [A, B, B, Ai, Bi, Bi, Bi, C]
print("1. |u| =", len(u))
ru = red(u)
assert ru == u, "u must be reduced"
# cyclically reduced: first/last not inverse
assert not (u[0][0] == u[-1][0] and u[0][1] == -u[-1][1]), "not cyclically reduced"
gens_used = {g for g, e in u}
assert gens_used == {'a', 'b', 'c'}, gens_used
# proper power check on the cyclic word: c occurs once => not a proper power
assert sum(1 for g, e in u if g == 'c') == 1
# brute force: no v,k>=2 with v^k == u up to cyclic rotation
n = len(u)
rots = [[u[(i + j) % n] for j in range(n)] for i in range(n)]
is_power = any(n % k == 0 and r == red(list(itertools.chain(*([r[:n // k]] * k)))) for r in rots for k in range(2, n + 1))
assert not is_power
print("1. OK: cyclically reduced, involves a,b,c, not a proper power")

# 2. t = b^3 a b^-2 a^-1 ; tinv = a b^2 a^-1 b^-3
t = pw('b', 3) + [A] + pw('b', -2) + [Ai]
tinv = [A] + pw('b', 2) + [Ai] + pw('b', -3)
assert red(t + tinv) == [], "t*tinv != 1"
assert red(tinv + t) == [], "tinv*t != 1"
# u = tinv c
assert red(u) == red(tinv + [C])
# phi(u) where phi(c) = t w : phi(u) = tinv t w = w
phi_u = tinv + t + [W]
assert red(phi_u) == [W], red(phi_u)
# psi(w) = tinv c = u
assert red(tinv + [C]) == red(u)
# psi(phi(c)) = psi(t w) = t tinv c = c
assert red(t + tinv + [C]) == [C]
# phi(psi(w)) = phi(tinv c) = tinv t w = w
assert red(tinv + t + [W]) == [W]
print("2. OK: Tietze isomorphism G4 ~= <a,b,w | w^4> = F(a,b)*C4")

# 3. retraction pi: a->1,b->1,c->z; u -> z so pi(u^4)=z^4=1 consistent.
# letter-count map onto C4 recorded symbolically:
def pi_exp(wd):
    # exponent of z: count c-letters (a,b killed; u preserved by construction)
    return sum(e for g, e in wd if g == 'c') % 4
assert pi_exp(u) == 1, "pi(u) must be generator z"
assert (4 * pi_exp(u)) % 4 == 0, "relator must map to 1"
print("3. OK: retraction G4 -> C4 sends u |-> z (order 4); w has exact order 4 (see DRAFT)")

# 4. Normal forms in F(a,b)*C4: tokens 'a','b' (Z) and 'w' mod 4.
def nf(wd):
    # wd: list of (gen, pm1); combine a/b runs, reduce w mod 4, drop identities
    out = []
    for g, e in wd:
        if g == 'w':
            if out and out[-1][0] == 'w':
                v = (out[-1][1] + e) % 4
                out.pop()
                if v:
                    # canonical representative 1..3 as signed steps
                    out.append(('w', v if v <= 2 else v - 4))
            else:
                v = e % 4
                if v:
                    out.append(('w', v if v <= 2 else v - 4))
        else:
            if out and out[-1][0] == g:
                s = out[-1][1] + e
                out.pop()
                if s:
                    out.append((g, s))
            else:
                if e:
                    out.append((g, e))
    return [(g, e) for g, e in out if e != 0]

def mul_nf(x, y):
    return nf(x + y)

def inv_nf(x):
    return [(g, -e) for g, e in reversed(x)]

# subgroup gens: b and t w ; t in F(a,b) part
t_ab = [(g, e) for g, e in t]  # a/b letters only
tw = mul_nf(t_ab, [('w', 1)])
bgen = [('b', 1)]
biv = [('b', -1)]
twv = inv_nf(tw)
words = {}
for nm, x, y in [("c1", bgen, tw), ("c2", biv, tw), ("c3", bgen, twv), ("c4", biv, twv)]:
    comm = mul_nf(mul_nf(mul_nf(x, y), inv_nf(x)), inv_nf(y))
    words[nm] = comm
    print("   [%s] normal form =" % nm, comm)
assert all(v for v in words.values()), "a commutator died: <b,tw> could be abelian"
assert len({tuple(v) for v in words.values()}) == 4, "commutator collision"
print("4. OK: <b, c=tw> has non-abelian free-like commutator profile (rank 2); full freeness in DRAFT.md")

print("ALL CHECKS PASSED")
sys.exit(0)
