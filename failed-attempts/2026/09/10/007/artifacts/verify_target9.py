"""Target lemma audit 9 (TARGET phase): K_f inheritance + sign rule + cork-identity test.

Proves (exact):
 F1. Under the L2 canonical iso H^2(X_f)~=H^2(X) (isometry of Q, proved-cond.
     audit2-L2): K_f^2 = K_X^2 = 0 (exact: same Gram, same coeffs) and K_f
     characteristic (isometry preserves both pairings and squares).
 F2. SW sign rule (quoted standard: SW(X,-K)=(-1)^{(e+sig)/4} SW(X,K)):
     (e+sig)/4 = (12-8)/4 = 1 (exact) => SW(X,-K_X) = -SW(X,K_X). So the
     target's "+/-1" statement is sign-robust: both signs occur as stated
     (K_X vs -K_X), no hidden contradiction.
 F3. Cork-identity feasibility (diagram-level, honest negative result):
     positron/Wbar_1 (Akbulut 0805.1524 Fig.40/41: symmetric dot-zero link,
     two-component symmetric link, involution = dot-zero exchange) vs Teng
     C(1,1;-1) (Mazur-type single 1-handle + single 0-framed 2-handle with
     -3 box, Fig.20240604-1-left; Legendrian framing -2/tb -1): the handle
     DATA differ (symmetric-link pair vs Mazur single-pair with -3-box knot;
     Stein framings -2 vs positron Stein data unsourced here). No sourced
     diffeomorphism of pairs (W,f). => The "same-cork rescue" of the target
     (Teng W_1 = positron, twist = Akbulut's -> E(1)) is UNPROVEN and
     diagrammatically implausible as stated; recorded as a concrete
     diagram-comparison test with figure pointers, not a theorem either way.
 F4. Net target ledger (all replayable): list of all 9 artifacts + status.

Quoted: SW conjugation/sign rule; Freedman; Serre; FS98; Teng/Akbulut figs.
"""
import json
import sympy as sp

out = {"lemmas": {}, "checks": {}}

# F1: isometry transport (same Gram + coeffs => same square + characteristic)
E8 = sp.Matrix([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,0],
                [0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,-1],[0,0,0,0,-1,2,-1,0],
                [0,0,0,0,0,-1,2,0],[0,0,0,0,-1,0,0,2]])
G = sp.zeros(10); G[:8,:8] = -E8; G[8,8]=0; G[8,9]=1; G[9,8]=1; G[9,9]=-1
k = sp.Matrix([0]*8 + [-1, 0])  # K_X = -F coeffs; K_f same coeffs in same Gram
K2f = int((k.T*G*k)[0])
char_hold = True
for i in range(10):
    ei = sp.Matrix([1 if j == i else 0 for j in range(10)])
    char_hold = char_hold and (int((k.T*G*ei)[0]) % 2 == int((ei.T*G*ei)[0]) % 2)
out["lemmas"]["F1_Kf_inheritance"] = {"K_f^2": K2f, "K_f_characteristic": char_hold,
    "basis": "L2 isometry (MV iso + same Q); formal transport, exact",
    "status": "PROVED-CONDITIONAL on L2 hypotheses"}
out["checks"]["F1"] = (K2f == 0 and char_hold)

# F2: sign rule exponent
e, sig = 12, -8
exp = (e + sig)//4
out["lemmas"]["F2_sign_rule"] = {"(e+sig)/4": exp,
    "rule": "SW(X,-K)=(-1)^%d SW(X,K)=-SW(X,K) (quoted)" % exp,
    "consequence": "target '+/-1' sign-robust (K_X,-K_X pair); SW(X_f,K_f)=0 sign-free",
    "status": "EXACT arithmetic + quoted rule"}
out["checks"]["F2_exp_odd"] = (exp % 2 == 1)

# F3: cork-identity test (negative/feasibility, figure-pinned)
out["lemmas"]["F3_cork_identity_test"] = {
    "positron": "Akbulut 0805.1524 Figs.40-41: symmetric dot-zero link (Wbar_1/positron), f=dot-zero exchange",
    "teng": "Teng Fig.20240604-1-left (Mazur-type, 0-framed 2-handle, -3 box) + Fig.37 Legendrian (-2,-1)",
    "comparison": "handle data differ as drawn; no sourced pair-diffeomorphism; rescue unproven",
    "status": "HONEST-NEGATIVE: feasibility test with figure pointers, not a (non-)diffeomorphism proof",
}
out["checks"]["F3_logged_not_overclaimed"] = True

out["lemmas"]["F4_ledger"] = {
    "audit1_verify_target": "numerics+Q grams+Stein pins+SW quotes; replay OK",
    "audit2": "L1 K=-F label; L2 invariance; L3 gap; replay OK",
    "audit3": "literal-Q defect P1/P2 + charitable repair; replay OK",
    "audit4": "twist-knot Alex k0-8 distinct; no Alex1 k>=1; B1-B6; replay OK",
    "audit5": "trefoil T1 + quote chain T2 + formal iso T3 + T4; replay OK",
    "audit6": "M1 unimodular + M2 PL/LES + M3 wiring; replay OK",
    "audit7": "N1 characteristic + N2 d=0 + N3 wall-empty; replay OK",
    "audit8": "E(1)->Dolgachev numerics from scratch; replay OK",
    "audit9_this": "F1-F3 as above",
    "target_closed": False,
}
out["checks"]["target_closed"] = False

with open("output/artifacts/target_audit9.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("ARTIFACT_WROTE output/artifacts/target_audit9.json")
