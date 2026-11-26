---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

PASS

The second-difference matrix B is surjective by recurrence, so B_A has full row rank for every active set. Prescribe curvature zero on A and one off A to get x; y=x−B_Aᵀ1 has projection x by the KKT conditions with strictly positive active multipliers. Strict primal slack and strict multipliers persist locally, and the projection there is H_A=I−B_Aᵀ(B_AB_Aᵀ)⁻¹B_A. The first-difference map D has right inverse J given by cumulative step columns. Since H_A fixes constants, the active-cell quotient norm is the largest absolute column sum of DH_AJ. Integrating on line segments and using continuity gives the upper bound globally; perturbing an open-cell point by a maximizing step attains it. Appending an inactive constraint gives H_A⊕[1]; extending the step by its tail keeps the input TV and preserves all old output edges, proving monotonicity. On the affine face the slope for step j is covariation divided by site variance, 6j(n−j)/[n(n²−1)], giving the stated TV norm and limit. A separate exact Fraction implementation enumerated all 127 faces for n=2–8 and obtained 1, 1, 6/5, 4/3, 7/5, 28/19, 11/7. It verified finite witnesses at ε=1/100 with strict slack, positive multipliers and the exact quotient in each size. The n=7 alternate maximizer has A={2,3,5}, step 4 and column (−4,6,6,6,3,3)/19; it is the reflected witness and does not conflict with the frozen one.

## originality

FAIL

The principal finite classification is already stated by the earlier distinct Resultary entry a125b58f7e4e: same Euclidean convex regression, two-input adjacent variation, first expansion at four, exact coefficients identical in all seven audited dimensions and finite attainment. That entry extends the table through ten. This is positive, specific coverage evidence, not a failure based on missing full text. The catalogue alone does not establish that the earlier record states the all-face formula or monotonicity. Those items are separate from the duplicated table and cutoff; the frozen finding as a whole cannot pass originality on that basis.

## value

FAIL

The exact first-expansion cutoff and finite classification would be useful if they were distinct, but repeating a table already reported through a larger size does not supply fresh scientific value. After setting those claims aside, the all-face formula is the induced ℓ¹ column norm of the standard affine pieces of a cone projector. Appending one coordinate with the new face constraint slack gives monotonicity directly from that identity. As submitted, that remainder does not resolve a further exact regime, limiting modulus, or structural obstruction beyond the routine face reduction and extension. No available remainder warrants a repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
