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

PASS

In the specified arc convention the support is the opposite-side component K_{q,q}, q=mn. On an orientation sector, a double step reflects independently at the two endpoints of this component, so the fourth power is identity. In particle-arc coordinates the off-diagonal block at step one is a signed rectangular reshaping of a reflected column, G/sqrt(2), up to row/column permutations and transposition; the inverse step has the same singular values. At step two the block is G ⊗ G^T/sqrt(2). Exchange symmetry gives a second copy of its squared singular values. The norm of G is 1 in Frobenius norm, and the sum of squares of its two-by-two minors is 4(m-1)(n-1)/q^2, giving the squared singular values in the finding even when one vanishes. Product probability entropy then gives the three time classes, the sharp log(8) ceiling, and the saturation cases by rank. The determinant at fixed q increases as m+n falls. When both sizes diverge the smaller weight is (4/q)(1+o(1)); the stated entropy asymptotic is valid at its stated o(log(q)/q) precision. An independent finite reproduction used the explicit degree-product scattering rule, repeatedly formed the arc coefficient matrix and computed its squared singular values for both signs at t=0,...,4. For K_{2,3} it recovered (1/2 twice), (1/3 twice, 1/6 twice), and (2/9 twice, 1/9 four times, 1/18 twice) in the three time classes; K_{1,3} gave 1/2 twice at every tested step. The unrestricted check is the reflection and block calculation, not that finite test.

## originality

FAIL

A distinct indexed result explicitly proves the same all-m,n, both-sign, all-time Schmidt spectra and the same rank-eight/log-eight ceiling for the same product-graph walk and initial state. The frozen fixed-q optimizer and diverging-parts estimate are immediate consequences of that formula, not a surviving distinct invariant. This is a coverage determination, not a claim about priority or provenance.

## value

FAIL

An unknown full entanglement spectrum for this irregular family would be a motivated invariant, but it is already available. The only additional formulas here are monotonicity in a single determinant parameter and the first small-weight binary-entropy estimate. Neither addresses a remaining scientific gap or extends that known invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
