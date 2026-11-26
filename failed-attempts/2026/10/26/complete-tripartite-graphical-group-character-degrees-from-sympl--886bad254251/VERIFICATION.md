---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

FAIL

The claimed explicit formula is not defined under its stated domains. For (a,b,c)=(2,2,4), r=2,s=0,t=1 requires H_q(2,4;1); its u=2 term requires N_q(0,1), outside 0≤t≤v. In the proof an isotropic radical of dimension u leaves a 2(v−u)-dimensional symplectic quotient, so a nondegenerate 2t-plane requires u≤v−t. Replacing the upper bound by min(v−t,h−2t), or explicitly defining N outside its range to be zero, would fix this. The supplied artifacts/verify_tripartite.py (lines 27–33, inspected but not executed) in fact uses this zero extension, unlike the frozen formula. The remainder of the derivation supports the corrected expression: elimination of the X hyperbolic block leaves C and PᵀJP, elimination of the s paired C coordinates leaves the restriction on ker C (the inverse pairing block has lower-right block zero), and a specified P|ker C has q^(2rs) extensions. The symplectic basis and surjection counts hold in characteristic two as well. For odd q the edge center and commutator coincide and a central additive character, written using a fixed nontrivial additive character of F_q and an F_q-linear edge functional, yields a radical of size q^(n−2j); induction from a maximal isotropic subgroup gives degree q^j and that many representations. Independent exact evaluation with the corrected range gave the five stated K₃,₃,₃/F₃ coefficients and multiplicities, with totals 3²⁷ and 3³⁶; replay: /workspace/branches/1bc60fc1-44fc-4adf-9cfe-9ef24f191274/k333_recompute.py. This is evaluation of the finite sum, not brute force. VERIFICATION.md documents the finite checks, not a proof or formal certificate.

## originality

FAIL

Resultary c071440590d6 already gives the same rank distribution via the same reductions and pullback formula for all three part sizes at least two and all finite fields, with the same odd-q character consequence. Resultary 732adc755a75 already gives an explicit all-field formula for the remaining singleton-part case. Consolidation into one generating polynomial, including an evaluation at (3,3,3,3), is not a distinct invariant or theorem. The domain defect does not create novelty.

## value

FAIL

Tripartite rank and character enumeration is a natural and valuable problem, but the frozen record's remainder after prior coverage is coefficient bookkeeping and an immediate evaluation for one example. Neither fixing the domain nor listing those coefficients supplies an independently useful unknown mathematical fact. No substantive repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
