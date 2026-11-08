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

Run `python check_cubic_caps.py` using dependencies in `requirements.txt`. The run returned `CUBIC_DOUBLE_CAP_CHECKS_PASS 147`.

The checker verifies, symbolically in the dimension parameter, the four spherical beta normalizers and five critical difference identities. It verifies symmetry-sector dimensions in multiple integers, compares eigenvalue integrals and crossing orders over a range of dimensions, independently integrates standard complex spherical harmonics on the ordinary two-sphere, and checks the sharp thin-cap coefficient numerically. The proof of statements for every integer dimension is the closed-form beta integration and the sign factorization, not the finite checks. The computations are reproducibility evidence and do not constitute independent mathematical validation.

Limits: global probability-normalized surface measure, pure degree three, equal antipodal caps, dimensions at least three, no finite-sampling or noise conclusions. The exact scientific comparison with earlier Slepian work is detailed in `RESULT.md` and `REVIEW.md`.
