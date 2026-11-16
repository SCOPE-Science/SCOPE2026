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

# Verification notes

The frame/no-frame assertion was checked from the exact Zak criterion and a complete elliptic zero-count argument; no sampled grid is used to infer nonvanishing everywhere. The theta entire function has one simple zero per fundamental cell, the meromorphic log-derivative difference has exactly two zeros, and both correspond only to zero constant perturbation. The lower-bound expansion uses a unique isolated nondegenerate minimum, the analytic implicit-function theorem, reflection parity, and exact Gaussian moment sums.

For numerical reproducibility, run `python CHECK.py` in a clean Python 3 environment; no third-party modules are needed. The checker executes 162 finite numerical assertions with tolerances, prints the exact-series coefficient approximations, and exits nonzero on failure. It does not provide a formal certificate of the infinite zero count, nor an independent review. The two asymptotic coefficients in the result are determined by convergent exact series, not by numeric minimization.
