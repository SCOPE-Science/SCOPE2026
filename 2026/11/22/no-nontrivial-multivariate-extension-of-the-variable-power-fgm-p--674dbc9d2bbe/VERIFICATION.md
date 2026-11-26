---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Set P=∏u_i, Q=∏(1−u_i), and write G=P exp(aQ log P). For a nonempty face set S, let h_i=u_i−1 for i in S, keeping all remaining coordinates positive. The coefficient of ∏_{i∈S}h_i in the analytic expansion is the claimed mixed derivative on the face: the constant exponential term contributes P_{S^c}; the linear term contributes a(−1)^|S| P_{S^c}Q_{S^c}log P_{S^c}; every higher term contains h_i² for each i∈S and cannot contribute. When a(−1)^{n−1}>0, keep one free coordinate z: the derivative correction contains (1−2z)log z+1−z, diverging negatively. In the other sign case keep two free coordinates, one fixed at 1/4: the logarithmic term has coefficient (1−2x)/2, tending to 1/2, with all other terms bounded as x→0. Both face sets exist when n≥3. Choose the free coordinates strictly positive first and transfer the strict sign into the interior by smooth continuation across the upper face. Integration over a small interior box gives negative volume, regardless of what boundary values are assigned. For a=0 the product extends to independence. No assumption on |a| or on lower-face smoothness is required.

## originality

PASS

The checked source explicitly proposes the exact displayed formula and leaves its admissible range open. No distinct independent result resolving this formula for n≥3 surfaced. The pass is limited to the all-parameter exclusion in those dimensions, not to the bivariate range or other multivariate power constructions.

## value

PASS

This resolves a specific published proposed extension and rules out both signs for every higher dimension, despite all proper margins looking valid. The interior sign witnesses make the result stronger than a boundary failure, and the two-face method identifies why the natural bivariate extrapolation fails without excluding other models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
