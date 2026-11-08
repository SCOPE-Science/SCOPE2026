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

# Computational verification and boundaries
The finite certificate consists of `verify.py` and `CERTIFICATE.json`. Execute `python verify.py CERTIFICATE.json` in one directory, using Python 3.9+ and no third-party package. The script enumerates all exponent vectors of total weights 16, 32, and 48, checks the 37/630/6885 semigroup counts, verifies explicit equations for the quadratic normalization hole, constructs the 22 cubic holes, and checks an exact integer separating hyperplane for every other admissible lattice vector. It reports `VERIFY_OK` if every integer assertion passes.

The 37+170 integer cuts are a compact finite certificate. For each cut the script recalculates its maximum on all 37 columns, so these bounds are not trusted as hard-coded values. The proof of completeness is the fully exhaustive integer domain and the strict separation inequalities. It does not rely on a timeout, floating-point feasibility result, or a comparison against a sampled subset.

This establishes the stated low-degree normalization counts, not higher-degree normalization or the conductor. No independent mathematical audit was performed.
