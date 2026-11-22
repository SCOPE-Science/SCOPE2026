---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

Run `python3 VERIFY.py` with Python 3. The included standalone checker uses only the standard library and does not require external mathematical software. Its own deterministic random seed produces 3,840 rational test points over twelve positive rational triples. For every test point it compares direct perpendicular projection onto each lateral triangular face and each apex edge (and direct base-face tests) against the closed-form pair of inequalities. All 3,840 comparisons passed.

The verifier also computes the normalized area of the basal kernel independently, by exact rational halfplane clipping and polygon shoelace, for twelve parameter triples (including the rhombic and octagonal regimes). These exact areas match the analytic volume fraction. Sixteen further exact checks compare nonsquare rectangles with square bases at the same area and height, and all satisfy strict inequality. Expected terminal output: `PASS: 12 exact clipped-area identities; 3840 exact face-projection checks; 16 square-optimality instances`.

The proof itself provides exact facet projection, redundancy of the lower-dimensional face conditions, the area formula, and the rational derivative sign for all positive parameters. Finite tests alone do not establish the continuous family, the unique optimizer, or all asymptotic claims. Every published claim is scoped to right rectangular pyramids; no external audit has been performed.
