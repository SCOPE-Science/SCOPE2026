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

# Verification and reproduction

The exact mathematical verification code is `verify.py`. Run with Python 3: `python3 verify.py`. The script uses only the standard library. It builds the actual tridiagonal matrix for three independent rational positive weight patterns and every path size from two through seven, uses exact Gaussian elimination to obtain its inverse, and independently verifies the left/right Green factorization, positive Wronskian, all-interval expansion, and the variance-excess identity. It enumerates all unlabeled set partitions and tests global optimality, unique periodic equality and the local defect lower bound.

Expected terminal result: `PASS: 14,337 exact assertions; n=2,...,7, three independent weight patterns each`.

The finite exact checks certify those finite sample inputs only; they do not replace the general inductive Green formula, interval telescoping identity, or universal integer balancing and window-propagation proof in `RESULT.md`. No independent mathematical audit has been performed.
