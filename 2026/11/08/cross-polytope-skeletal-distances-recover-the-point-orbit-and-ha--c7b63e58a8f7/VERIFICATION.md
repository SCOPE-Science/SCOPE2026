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

# Reproduction and verification

Run `python verify.py` with Python 3 and NumPy. The package includes all formulas, the dependency description, and the complete standalone checker. This execution returned `CROSSPOLYTOPE_SKELETON_SIGNATURE_JOINT_GAMMA_LIMIT_OK 490 210000 15000`.

The checker compares exact squared distances with independent projections to every signed face of dimensions 2 through 5, reconstructs ordered absolute coordinates, samples volume-uniform interior points to check finite harmonic mean formulas, draws a gamma-Poisson arrival process to check limiting means, variances, and cross-rank covariance, and independently checks centering using 15,000 points in dimension 1200. All randomized tests have a fixed seed. A finite test cannot validate a general theorem for all dimensions or prove historical novelty.
