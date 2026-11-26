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

I derived the difference transfers by differentiating the Newton interpolation basis, substituting y_{n-j}=y_n−∑_{i<j}d_{n-i}, and taking the chronological two-step product. Its BDF4 characteristic cubic P_r/A agrees identically. For a monic cubic with coefficients a,b,c, the Schur reduction has quadratic coefficients 1−c²,a−bc,b−ac; positivity at ±1 and the upper bound on its constant coefficient are exactly the displayed conditions after dividing by positive factors. Exact expansion gives positive coefficients in each of the five proof numerators. Absolute summability of the differences then gives bounded nodal values and convergence for each fixed ratio. Reciprocity is exact; at t=1/r=0 the normalized cubic has a simple root −1 and a double root 0. Substitution of z=−1+ut into t⁴P_{1/t}(z) gives t(24u−128)+O(t²), so the |z| at the simple branch is 1−16t/3+O(t²). Strictness plus continuity on compact positive r intervals confines approach to the supremum to the extremes. Independent order-five differentiation at steps 1,10 gives det(I+T)=−8874496/44681585, so the monic quartic has a real root strictly below −1 by its sign at −1 and at negative infinity.

## originality

FAIL

The Oct. 12 indexed claim covers exactly the all-ratio interpolatory BDF4 assertion, even using the identical cubic and Schur polynomials. Its cubic supplies the endpoint expansion by the derivative of a simple root. Its BDF5 threshold classification strictly dominates the witness at r=10. The evidence is substantive prior coverage in the indexed record, irrespective of external publication priority.

## value

FAIL

The question itself is natural: extreme alternation tests the gap between arbitrary-ratio sufficient conditions and a fixed Floquet product. But the frozen record does not close a remaining gap: its complete Schur calculation was given for this family already, the BDF5 witness specializes an existing full classification, and the added sharp coefficient is a routine first derivative of the known exact cubic. Rechecking the known table does not constitute a separate worthwhile finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
