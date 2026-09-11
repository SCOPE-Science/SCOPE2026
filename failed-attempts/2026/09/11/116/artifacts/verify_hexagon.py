"""Machine-checked Yang-Baxter hexagon ledger for Gray interchangers.

Setting: monoid of 2-cell pastings = words over {A,B,C}; 3-cells compose
vertically (diagrammatic order, denoted by lists) and whisker by words.
Interchanger family chi_{X,Y} : X+Y => Y+X (whiskered: L+chi+R).

Axioms used (standard Gray-category laws, valid in the free Gray-category):
  (H1) chi_{AB,C} = (A*chi_{B,C}) . (chi_{A,C}*B)      [compatibility]
  (H2) chi_{BA,C} = (B*chi_{A,C}) . (chi_{B,C}*A)      [compatibility]
  (N)  (chi_{A,B}*C) . chi_{BA,C} = chi_{AB,C} . (C*chi_{A,B})  [naturality
        of chi_{-,C} at the 3-cell chi_{A,B}]

Theorem: P = Q where
  P = (chi_AB*C).(B*chi_AC).(chi_BC*A)   (clockwise, s1 s2 s1)
  Q = (A*chi_BC).(chi_AC*B).(C*chi_AB)   (counterclockwise, s2 s1 s2)

This script checks: every step is well-typed, consecutive boundaries match,
both sides of each axiom share source/target, P and Q are parallel 3-cells
ABC=>CBA, and substitution of (H1),(H2) into (N) yields P=Q syntactically.
"""
from __future__ import annotations

Word = tuple  # tuple of str

def cat(*ws):
    out = []
    for w in ws:
        out.extend(w)
    return tuple(out)

def whisk_source(L, X, Y, R):
    return cat(L, X, Y, R)

def whisk_target(L, X, Y, R):
    return cat(L, Y, X, R)

class Step:
    def __init__(self, L, X, Y, R, tag=""):
        self.L, self.X, self.Y, self.R = tuple(L), tuple(X), tuple(Y), tuple(R)
        self.tag = tag
    @property
    def src(self):
        return whisk_source(self.L, self.X, self.Y, self.R)
    @property
    def tgt(self):
        return whisk_target(self.L, self.X, self.Y, self.R)
    def key(self):
        return (self.L, self.X, self.Y, self.R)
    def __repr__(self):
        w = lambda t: "".join(t) if t else "I"
        return f"{w(self.L)}*chi_{w(self.X)},{w(self.Y)}*{w(self.R)} [{w(self.src)}=>{w(self.tgt)}]"

def check_chain(steps, name):
    for i in range(len(steps) - 1):
        assert steps[i].tgt == steps[i + 1].src, (
            f"{name}: boundary mismatch between step {i} {steps[i]} "
            f"and step {i+1} {steps[i+1]}")
    return (steps[0].src, steps[-1].tgt)

A, B, C = ("A",), ("B",), ("C",)
AB, BA = ("A", "B"), ("B", "A")
I = ()

# Atomic whiskered steps (the six hexagon edges)
s_AB_C = Step(I, A, B, C, "chi_AB*C")      # ABC=>BAC
s_B_AC = Step(B, A, C, I, "B*chi_AC")      # BAC=>BCA
s_BC_A = Step(I, B, C, A, "chi_BC*A")      # BCA=>CBA
s_A_BC = Step(A, B, C, I, "A*chi_BC")      # ABC=>ACB
s_AC_B = Step(I, A, C, B, "chi_AC*B")      # ACB=>CAB
s_C_AB = Step(C, A, B, I, "C*chi_AB")      # CAB=>CBA

# Composite-argument interchangers in axioms
chi_AB_C = Step(I, AB, C, I, "chi_AB,C")   # ABC=>CAB
chi_BA_C = Step(I, BA, C, I, "chi_BA,C")   # BAC=>CBA

P = [s_AB_C, s_B_AC, s_BC_A]
Q = [s_A_BC, s_AC_B, s_C_AB]

p_src, p_tgt = check_chain(P, "P")
q_src, q_tgt = check_chain(Q, "Q")
assert p_src == q_src == ("A", "B", "C"), (p_src, q_src)
assert p_tgt == q_tgt == ("C", "B", "A"), (p_tgt, q_tgt)

# Axiom boundary checks
assert (chi_AB_C.src, chi_AB_C.tgt) == (("A", "B", "C"), ("C", "A", "B"))
assert (chi_BA_C.src, chi_BA_C.tgt) == (("B", "A", "C"), ("C", "B", "A"))
n_lhs = [s_AB_C, chi_BA_C]
n_rhs = [chi_AB_C, s_C_AB]
check_chain(n_lhs, "N-lhs")
check_chain(n_rhs, "N-rhs")
assert n_lhs[0].src == n_rhs[0].src == ("A", "B", "C")
assert n_lhs[-1].tgt == n_rhs[-1].tgt == ("C", "B", "A")
h1_rhs = [s_A_BC, s_AC_B]
check_chain(h1_rhs, "H1-rhs")
assert h1_rhs[0].src == chi_AB_C.src and h1_rhs[-1].tgt == chi_AB_C.tgt
h2_rhs = [s_B_AC, s_BC_A]
check_chain(h2_rhs, "H2-rhs")
assert h2_rhs[0].src == chi_BA_C.src and h2_rhs[-1].tgt == chi_BA_C.tgt

# Substitution: (N) with (H1),(H2) gives P=Q syntactically.
lhs_expanded = [s_AB_C] + h2_rhs          # = P
rhs_expanded = h1_rhs + [s_C_AB]          # = Q
assert [s.key() for s in lhs_expanded] == [s.key() for s in P]
assert [s.key() for s in rhs_expanded] == [s.key() for s in Q]

print("P source/target:", "".join(p_src), "=>", "".join(p_tgt))
print("Q source/target:", "".join(q_src), "=>", "".join(q_tgt))
print("P =", " . ".join(s.tag for s in P))
print("Q =", " . ".join(s.tag for s in Q))
print("(N): (chi_AB*C).chi_BA,C = chi_AB,C.(C*chi_AB)  [parallel ABC=>CBA]")
print("(H1): chi_AB,C = (A*chi_BC).(chi_AC*B)")
print("(H2): chi_BA,C = (B*chi_AC).(chi_BC*A)")
print("Substituting (H1),(H2) into (N): P = Q.")
print("VERIFY_OK")
