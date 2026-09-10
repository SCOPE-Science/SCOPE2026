"""L-legality check for target formulas in L={<,+,P}.
phi1(x;y1) := (y1 < x) — uses {<} only. L-legal.
phi2(x;y2) := P(x - y2), i.e. exists z (P(z) /\ x = y2 + z) — uses {+,P,=} only. L-legal.
Verifies: no symbol outside L; phi2's existential expansion is an L-formula.
"""
import re

L = {"<", "+", "P", "=", "exists", "forall", "and", "or", "not", "->", "x", "y", "z"}

phi1 = "y1 < x"
phi2_expansion = "exists z (P(z) and x = y2 + z)"

# tokenize: identifiers and symbols
def tokens(s):
    return re.findall(r"[A-Za-z_][A-Za-z0-9_]*|[<+=()]", s)

allowed_ids = {"x", "y1", "y2", "z", "P", "exists", "and"}
allowed_syms = {"<", "+", "=", "(", ")"}

ok = True
for name, s in [("phi1", phi1), ("phi2_expansion", phi2_expansion)]:
    toks = tokens(s)
    bad = [t for t in toks if t not in allowed_ids and t not in allowed_syms]
    print(f"{name}: tokens={toks} bad={bad}")
    if bad:
        ok = False

# check phi2 uses + legally (in L) and P applied to a term
assert "+" in tokens(phi2_expansion), "phi2 must use +"
assert "P" in tokens(phi2_expansion), "phi2 must use P"
# check phi1 uses only < (no +, no P)
assert "+" not in tokens(phi1) and "P" not in tokens(phi1)
print("L_LEGALITY_OK" if ok else "L_LEGALITY_FAIL")
