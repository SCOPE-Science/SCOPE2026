---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With unit total continuous-time jump rate per walker, the vacant-hub holding time is 1/k in expectation and its next state is A_(k-1). From A_k the three rates are k to A_(k-1), k/m to B_k, and (m-k)/m to B_(k+1); at k=m the last term is absent and at k=1 both one-walker states are absorbing. These give a_1=(3m-1)/(2(m+1)) and a_k-a_(k-1)=(2m+1)/((m+1)k)-1/(k+1), reproducing the formula, the gap, and the saturation equality of means. Clique thinning gives merger rates j(j-1)/m and the telescoping sum m²/(m+1). Comparison follows from H_m≤1+(m-2)/2+1/m for m≥2, strictly below m-1+1/m for m>2; m=1 is checked directly. The harmonic asymptotic has the stated constant and error. A newly written Fraction test checked all 144 reduced classes for 1≤m≤12 as well as the clique sum; the frozen source's separate full-state test is recorded evidence, not a replay or attestation.

## originality

FAIL

A distinct indexed result contains the identical full-start mean and a level-by-level distributional construction that mechanically yields both initial-configuration formulas. The occupancy gap and exact constant then follow by subtraction or specialization, and the clique comparison adds only the standard death-rate sum and an elementary harmonic-number bound. This is a finding of extant equivalent coverage and implication, not a claim about which record has priority.

## value

FAIL

An exact initial-configuration mean on a canonical graph and a rate-matched comparison are well motivated, but the stronger indexed stage formula already yields the exact quantities by summation. After crediting that coverage, the remaining star–clique comparison is an elementary death-process sum and harmonic bound, not a standalone valuable repaired result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
