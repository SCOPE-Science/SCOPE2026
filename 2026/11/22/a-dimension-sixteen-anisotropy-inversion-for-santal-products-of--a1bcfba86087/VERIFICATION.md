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

## Reproducible verification

Run `python3 check_anisotropy.py` from the unpacked directory with SymPy and mpmath installed. The checker verifies three exact coefficient identities, the sign classification over an extensive integer range including the sharp boundary, eight high-precision comparisons of the two extremal patterns in dimensions \(2,3,15,16\), and three independent direct-integral comparisons. The analytical proof in RESULT.md, not finite tests, proves all-dimensional strict Schur ordering locally.

The source domain is every integer \(n\ge2\), with \(|t_i|<1\); the optimization theorem applies only when \(\sum_i t_i^2\) is sufficiently small for that fixed dimension. The numerical checks use two small radii and do not produce a certified explicit radius in any dimension.

Self-review was conducted on correctness, overlap, value, and public-file integrity. Independent mathematical audit has not been performed.
