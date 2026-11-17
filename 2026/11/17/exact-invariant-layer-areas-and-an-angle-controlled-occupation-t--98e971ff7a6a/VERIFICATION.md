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

# Reproducibility
Execute `python3 CHECK_AREA.py` with Python 3. No third-party packages are required.

Recorded actual output:
`TCE_LAYER_AREA_CHECK_OK exact_shoelace_cases=66 sampled_invariant_images=12977 angle_and_limit_checks=OK`

The checker reconstructs the ordered polygon vertices for 66 parameter cases with rational cosine, sine and translation, comparing the signed shoelace area **exactly** as rational numbers to the derived quadratic expression. It samples 12,977 planar points inside example polygons and checks that their translated-cone images stay inside the same polygon, and verifies the finite-layer monotonicity and asymptotic distribution at sampled parameters. The code is included in full.

These finite checks are not a proof of invariance or convergence for arbitrary real parameters. The existence, nestedness, and almost-everywhere invariance of the polygonal regions are established by Cockram, Ashwin and Rodrigues (arXiv:2312.17412, Theorem 4.2 and Corollary 4.4). The exact area identity and the limiting law are proved analytically in `RESULT.md`. No external independent mathematical audit has been performed.
