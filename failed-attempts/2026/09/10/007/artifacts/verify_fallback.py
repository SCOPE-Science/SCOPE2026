"""Fallback audit (PRESET_FALLBACK route): Gompf d3 pair for Teng W_1 boundary.

Fixes the ONE diagram: Teng Fig.37 = Fig.20240420-23 (Legendrian C(1,1;-1),
2-handle framing -2, tb -1), i.e. W_1 := C(1,1;-1) Mazur-type contractible
Stein cork. Computes the XI side EXACTLY and tests the F_*XI side honestly.

XI SIDE (PROVED exact):
 H1. Handle count: one 0-h, one 1-h, one 2-h => e(W_1) = 1-1+1 = 1 (exact).
 H2. Contractible (Teng Aux lemma quoted + audit6-M1/M2) => sig(W_1) = 0,
     H2(W_1) = 0 => c1(W_1,J) = 0 in H^2 = 0 => c1^2 = 0 (no rot needed).
 H3. dW_1 homology sphere (audit6-M2 proved) => c1(xi) torsion (=0) =>
     Gompf d3 formula applies (quoted AY Lemma/contact refs).
 H4. d3(xi) = (0 - 2*1 - 3*0)/4 = -1/2 EXACT (matches fallback's first value).
     Rotation-number independence: ANY rot gives same answer since c1=0.

F_*XI SIDE (honest test of fallback's second value +1/2):
 G1. f is the infinite-order cork twist (torus/Dehn twist g x id, Teng Sec.2
     neck N = I x dSigma x S1), a SMOOTH boundary diffeomorphism; Teng's
     paper contains NO second Stein handlebody, NO rot data for f_*xi, and
     its closing Question asks whether f is even a contactomorphism.
 G2. d3(f_*xi) = +1/2 would require a Stein filling (W',J') of (Y,f_*xi)
     with c1^2 - 2e' - 3sig' = 2. No such filling sourced anywhere.
 G3. Brute-force search over small fillings (exact loop below): contractible
     Mazur-type (e=1,sig=0,c1^2=0) gives -1/2 only; Stein X' with b2>=1
     carrying c1^2=4+2(e'-1)+3sig' needs sourced Legendrian data (absent).
 G4. CONTACTOMORPHISM route (the only honest path to f_*xi d3): needs either
     (a) proof f is contactomorphism (then f_*xi ~= xi, d3 EQUAL, so pair
         would be (-1/2,-1/2), CONTRADICTING +1/2), or (b) explicit
         contact-surgery tracking of xi under f (absent). Either way the
         claimed (+/-) pair (+1/2 second value) is UNSUPPORTED and route (a)
         actively contradicts DISTINCTNESS. Teng's open Question confirms
         neither route is available.
 VERDICT on fallback second value: FAIL — d3(f_*xi)=+1/2 not computable from
 the fixed diagram; no archived log can produce it; claiming it would be
 fabrication. The fallback's binary criterion (PASS iff values differ AS
 STATED) is therefore NOT met.

Fallback salvage assessment: the XI side alone (d3(xi)=-1/2 exact) is a new
exact invariant value (no source logs it) but is NOT the admitted fallback
claim (which requires the PAIR differing as stated). Per instructions a
PRESET_FALLBACK claim must meet the EXACT success criterion, not approach it.
=> No PRESET_FALLBACK claim. Route decision must be TARGET / EMERGENT / NO_RESULT.
"""
import json
from fractions import Fraction

out = {"lemmas": {}, "checks": {}}

# H1-H4: xi side exact
eW, sW = 1 - 1 + 1, 0
c1sq = 0  # H^2(W_1)=0
d3_xi = Fraction(c1sq - 2*eW - 3*sW, 4)
out["lemmas"]["xi_side"] = {
    "handle_count": "0-h:1, 1-h:1, 2-h:1",
    "e(W_1)": eW, "sig(W_1)": sW, "H2(W_1)": 0, "c1": 0, "c1^2": c1sq,
    "d3(xi)": str(d3_xi),
    "formula": "Gompf d3 = (c1^2-2e-3sig)/4 (quoted AY Sec.4/Gompf-Stipsicz)",
    "applicability": "dW_1 homology sphere (audit6-M2) => c1(xi) torsion",
    "rot_independence": "c1=0 regardless of rot => tb/rot disambiguation irrelevant here",
    "status": "PROVED-EXACT from handle count + contractibility",
}
out["checks"]["d3_xi_minus_half"] = (d3_xi == Fraction(-1, 2))

# G3: small-filling scan (exact): which (e',sig',c1^2) give +1/2?
cands = []
for ee in range(0, 5):
    for ss in range(-4, 5):
        need = 2 + 2*ee + 3*ss  # c1^2 needed for d3=+1/2
        cands.append({"e": ee, "sig": ss, "need_c1^2": need})
contractible_gives = Fraction(0 - 2*1 - 0, 4)
out["lemmas"]["f_side"] = {
    "f_type": "smooth infinite-order torus twist g x id_S1 (Teng Sec.2); no Stein/contact data",
    "teng_question": "contactomorphism status OPEN (Teng Question, p.190-193)",
    "no_second_filling": "no sourced (W',J') with c1^2-2e'-3sig'=2",
    "contractible_Mazur_gives": str(contractible_gives),
    "small_filling_needs": [c for c in cands if c["e"] in (1, 2) and c["sig"] in (0, -1)],
    "contactomorphism_route": "(a) f contact => d3 equal (-1/2,-1/2), contradicts +1/2; (b) surgery tracking absent",
    "status": "d3(f_*xi)=+1/2 UNSUPPORTED (would be fabrication to claim)",
}
out["checks"]["f_side_computable"] = False
out["checks"]["fallback_pair_criterion_met"] = False
out["fallback_verdict"] = ("FAIL: xi side d3=-1/2 exact (new value, logged), but f_*xi side "
    "+1/2 has no route from the fixed diagram; binary pair criterion NOT met; "
    "no PRESET_FALLBACK claim permitted.")

with open("output/artifacts/fallback_audit.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("ARTIFACT_WROTE output/artifacts/fallback_audit.json")
