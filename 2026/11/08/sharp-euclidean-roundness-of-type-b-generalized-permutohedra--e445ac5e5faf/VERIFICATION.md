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
# Reproducibility and scope

Run the standalone Python 3 program with `python verify_roundness.py`. The program uses only the Python standard library. It enumerates all signed-permutation vertices and every nonzero ternary signed-subset normal for dimensions 2–5, verifies all support numbers and each facet's codimension one, and counts 356 facets in total. It also tests the optimized inradius-to-circumradius bound against representative nonoptimal profiles in dimensions 2–127.

Observed successful replay: `TYPE_B_SHARP_ROUNDNESS_CHECKS_PASSED facet_checks= 356 dimensions_checked= 126`, preceded by counts 8, 26, 80, 242. Comparisons involving square roots use numerical tolerances of order \(10^{-9}\) to \(10^{-11}\). They are reproducibility checks, not all-dimensional certificates. The complete proof is mathematical and appears in RESULT.md; no code is needed to prove its summation-by-parts step or the Minkowski symmetrization inequality.

Independent mathematical audit has not been performed.
