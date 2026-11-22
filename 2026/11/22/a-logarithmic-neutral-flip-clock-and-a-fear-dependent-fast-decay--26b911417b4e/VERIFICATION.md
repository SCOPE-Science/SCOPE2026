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

# Verification scope

Reproduce the symbolic and finite numerical diagnostics by running `python verify.py` with Python 3 and SymPy installed. A successful run prints `VERIFY_OK` after checking the exact Taylor coefficients and graph-invariance equations. The finite trajectory diagnostics include two nonzero predator starts on opposite sides of the fast-decay curve, as well as the quadratic graph's small-argument residual.

The infinite-time theorem is supported by the mathematical proof in `RESULT.md`: small-data trapping, summable forcing, exponential inverse shadowing, the standard local strong-stable theorem and the convergent reciprocal-square clock. Numerical runs do not certify the infinite tail, exact universal quantifiers or novelty relative to all mathematical literature.

The cited original map is Eq. (1.2) in Du–Han–Lei (2023), https://doi.org/10.3934/math.20231221. The parameter regime \(\alpha=d\) and global initial states are not covered. Independent audit has not been performed.
