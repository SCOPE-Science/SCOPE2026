"""Target lemma audit 7 (TARGET phase): null-class chamber rigidity + K characteristic.

Proves (reproducibly):
 N1. K_X = -F is CHARACTERISTIC (exact integer check on basis generators;
     extends by (x+y)^2 = x^2+y^2+2(x.y)): K.e_i=0=e_i^2 mod2 (E8 roots,
     sq -2); K.F=0=F^2 mod 2; K.S=-1=S^2=-1 mod 2. Exact sympy below.
 N2. Formal SW dimension d(K_X) = (K^2-2e-3sig)/4 = 0 (exact) => SW is a
     zero-dimensional count; no.:. moduli correction.
 N3. CHAMBER RIGIDITY for null K (PROVED from quoted standard Lorentz facts
     + Serre classification quoted in audit1):
     walls in the forward positive cone C_+ = {x : x^2>0} are K^perp;
     for null K != 0, x^2>0 & x.K=0 is impossible: move (over R) to the
     odd diagonal basis (Serre, quoted), Lorentz-rotate (O(1,9) transitive
     on null cone, quoted) to K=(1,1,0,...,0); then x.K = x0-x1 = 0 gives
     x^2 = -(x2^2+...+x9^2) <= 0, contradiction. Hence the wall W_{K_X} is
     EMPTY, SW(X,K_X) is chamber-independent, and likewise for K_f (K_f^2=0
     since Q preserved by L2). => B4 chamber caveat from audit4 is
     DISCHARGED for this class (was flagged; now proved a non-issue).
     Certified computation: the diagonal-basis implication
     (x0=x1 => x^2<=0) checked symbolically below.
 N4. Consequence: remaining target blockers are exactly B1 (embedding),
     B2 (X_f identification), B5 (knot-surgery mechanism cannot vanish),
     B6 (literal Q clause defective; charitable form certified).
     The X-side SW=+/-1 quote is now chamber-clean; the failure is purely
     on the twist side + embedding premise.

Quoted: Serre odd-indefinite classification; O(1,n) null-cone transitivity;
Freedman; FS98; Teng Aux lemma; Mazur-type contractibility lemma.
"""
import json
import sympy as sp

out = {"lemmas": {}, "checks": {}}

# ---- N1: characteristic check in -E8 (+) N basis ----
E8 = sp.Matrix([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,0],
                [0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,-1],[0,0,0,0,-1,2,-1,0],
                [0,0,0,0,0,-1,2,0],[0,0,0,0,-1,0,0,2]])
G = sp.zeros(10); G[:8,:8] = -E8; G[8,8]=0; G[8,9]=1; G[9,8]=1; G[9,9]=-1
K = sp.Matrix([0]*8 + [-1, 0])
rows = []
ok = True
for i in range(10):
    ei = sp.Matrix([1 if j == i else 0 for j in range(10)])
    lhs = int((K.T*G*ei)[0]) % 2
    rhs = int((ei.T*G*ei)[0]) % 2
    rows.append({"i": i, "K.e": lhs, "e^2": rhs, "match": lhs == rhs})
    ok = ok and (lhs == rhs)
out["lemmas"]["N1_characteristic"] = {"basis_rows": rows,
    "extension_rule": "(x+y)^2=x^2+y^2+2(x.y) so basis check suffices",
    "status": "PROVED (exact)"}
out["checks"]["N1"] = ok

# ---- N2: formal dimension ----
e, sig, K2 = 12, -8, int((K.T*G*K)[0])
d = sp.Rational(K2 - 2*e - 3*sig, 4)
out["lemmas"]["N2_formal_dim"] = {"K^2": K2, "e": e, "sig": sig,
    "d=(K^2-2e-3s)/4": str(d), "status": "EXACT: d=0, zero-dimensional count"}
out["checks"]["N2_d0"] = (d == 0 and K2 == 0)

# ---- N3: chamber rigidity (symbolic diagonal-basis step) ----
x = sp.symbols('x0:10')
x0, x1 = x[0], x[1]
rest = sum(xi**2 for xi in x[2:])
xsq_given = sp.expand(x0**2 - (x1**2 + rest))
consequence = sp.expand(xsq_given.subs(x0, x1))  # x0=x1 (i.e. x.K=0 for K=(1,1,0..))
out["lemmas"]["N3_chamber_rigidity"] = {
    "diagonal_step": "x.K=x0-x1=0 => x^2=-(x2^2+...+x9^2)<=0, computed: %s" % str(consequence),
    "conclusion": "no x with x^2>0 and x.K=0 => wall W_K empty => SW(-,K) chamber-independent",
    "applies_to": "K_X=-F (K^2=0) and K_f (K_f^2=0, Q preserved by L2)",
    "dependence": "Serre odd-diagonal basis + O(1,9) null transitivity (quoted standard)",
    "status": "PROVED-CONDITIONAL on quoted standard facts; B4 discharged for this class",
}
out["checks"]["N3_symbolic"] = (consequence == -rest)

out["lemmas"]["N4_remaining_blockers"] = {
    "B1_embedding": "OPEN: Teng E(n)n>=2 vs E(1)_{2,3} nucleus (no source)",
    "B2_X_f": "OPEN: no Teng-twist identification (sourced vanishing = positron->E(1), wrong cork)",
    "B5_mechanism": "PROVED-OBSTRUCTION: knot-surgery/Alexander preserves nonvanishing (audit4)",
    "B6_clause": "literal Q clause defective; charitable -E8(+)N certified (audit3)",
    "X_side": "chamber-clean quoted SW=+/-1 (T1-T2 audit5 + N1-N3 here)",
    "homeomorphism_side": "proved-conditional (L2+M1-M3)",
}
out["checks"]["target_closed"] = False

with open("output/artifacts/target_audit7.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("ARTIFACT_WROTE output/artifacts/target_audit7.json")
