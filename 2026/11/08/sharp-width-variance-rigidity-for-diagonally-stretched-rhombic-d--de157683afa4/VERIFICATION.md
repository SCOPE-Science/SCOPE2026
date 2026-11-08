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

# Reproduction and scope

From a directory containing the supplied verifier, execute `python3 verify_rhombic_width.py`. The program uses only Python 3 standard-library `math`, `random`, and `itertools`, with fixed random seed 20261103. Its observed final output is `RHOMBIC_WIDTH_OK exact_vertices=14 support_consistency=9000 cases=3 stability_samples=30000`.

The verifier checks the zonotope endpoint set, direct-vertex and generator width formulas, moments for three positive axial triples, 30,000 random checks of the quantitative lower bound and strict upper bound, and the exact regular-cell normalization. The proof in `RESULT.md` supplies the all-real-parameter argument: convexity, pair-Gaussian integration, and sharp boundary analysis. No numerical test is treated as an infinite certificate; no independent audit has been performed.
