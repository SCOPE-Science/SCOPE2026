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

# Reproducibility checks

The proof in `RESULT.md` is symbolic and holds for all permitted dimensions, including zero generators by continuity or the separate zero-weight case. Its only external mathematical input is the established sum-of-wedge-norms formula for zonotope intrinsic volumes.

Run `python verify.py` with Python 3 and no external packages. The verifier performs an exact-fraction, nonregular configuration check, exact regular-simplex Gram/equality checks through dimension twelve, and 900 seeded floating-point checks across dimensions two through ten. It directly compares the weighted trace identity, the two nonnegative defects, and the full quantitative identity. Successful output begins `PASS:`.

Finite checks do not prove uniqueness or universal validity. The theorem's equality proof relies on a rank-one orthogonal-complement Gram matrix, not numerical extrapolation. No independent audit is claimed.
