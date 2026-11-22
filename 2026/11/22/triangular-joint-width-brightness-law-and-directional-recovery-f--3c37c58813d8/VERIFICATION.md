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

# Verification evidence

The elementary proof calculates the normal-projection determinant using complementary minors, maps independent normal-square coordinates through a nonsingular affine transform, and evaluates covariance using exact fourth spherical moments. The companion `check.py` performs deterministic tests of the affine-inversion accuracy, independent Gaussian-direction sampling, covariance identity, and symbolic Vandermonde and sum-of-squares polynomial identities. It is supporting evidence, not a replacement for the all-parameter proof.

The density is with respect to two-dimensional Lebesgue measure only for pairwise distinct semiaxes. The spheroidal and spherical cases are lower-dimensional measures. All conclusions concern geometric projection area, not a scattering-law brightness model.

Independent audit: not performed.
