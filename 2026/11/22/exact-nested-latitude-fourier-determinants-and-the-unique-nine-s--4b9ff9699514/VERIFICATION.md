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

# Verification details

Run `python3 verify.py` with Python 3.10 or newer. No nonstandard Python dependencies are required.

The checker builds real Legendre derivatives by their explicit finite coefficient sum; then constructs the complex normalized spherical harmonic evaluation matrix independently of the factorized formula. A pivoted complex Gaussian eliminator calculates its determinant modulus, which is compared with the predicted product for randomly selected noncolliding latitudes in both ordering chambers and for independently varied ring-longitude offsets. Exact rational-pair arithmetic in \(\mathbb Q(\sqrt{2305})\) checks both critical-point polynomial systems and the positive rational difference of the two chamber maxima. Output states the number of assertions and the optimal nine-sample coordinates and equiangular determinant ratio.

This is a reproducibility test, not an exhaustive test over all bandwidths or a replacement for the proof of block triangularization, strict concavity, or uniqueness. The analytic argument in `RESULT.md` proves those claims. Uncertainty outside the described structured designs and independent mathematical audit are not resolved.
