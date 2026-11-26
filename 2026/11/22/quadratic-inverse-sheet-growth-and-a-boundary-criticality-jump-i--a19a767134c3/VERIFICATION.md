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

The second coordinate uniquely imposes y=V−x. The phase bx cos(V−x) ranges over R and is analytic and nonconstant. Its derivative is b√(1+x²) cos(V−x−arctan x); the angle decreases at speed between 1 and 2, so there are O(R+1) monotonicity pieces. Counting distinct phase levels on each piece costs a bounded error including shared endpoints. There are two disjoint levels per 2π in the interior and one at either edge. The variation is b∫|x sin(V−x)|dx+O(bR)=2bR²/π+O(b(R+1)), using a bounded periodic primitive of |sin|−2/π separately on each half. This yields the stated coefficients and no solutions outside the strip. Each nonempty full fiber is infinite and its analytic zeros are locally finite. The determinant along the fiber is a cos(phase) times the phase derivative: every edge preimage is critical, and at most O(R+1) interior ones are. Removing only bounded-length end portions for the square window costs O(R+1) by the same count. O(R) is an assertion for R tending to infinity, not a bound down to zero. The frozen Python code uses floating-point sign changes and generic endpoints; its recorded finite samples do not certify exact tangencies or the square window. No frozen code was executed.

## originality

PASS

The known map and standard level counting are not credited as novel. The supported distinct claim is its exact global inverse growth with a boundary transition and a regular-sheet count. The closest same-day comparisons substantially overlap in method and transition but do not cover this map; their date is not taken as scientific priority evidence.

## value

PASS

For a natural published real-plane map, the result distinguishes infinite ambiguity from quantitative inverse multiplicity and shows that a boundary target has half as many ancestors to leading order yet no regular ancestor at all. The symmetric-window statement makes the comparison meaningful for bounded observations of both coordinates. The analytic proof is elementary, but the coefficient and the regular/critical contrast are global features not supplied by the forward dynamics or by computing the determinant alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
