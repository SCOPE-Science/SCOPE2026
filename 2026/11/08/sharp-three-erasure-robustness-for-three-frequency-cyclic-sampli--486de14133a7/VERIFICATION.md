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

The embedded `checker.py` uses Python 3 and NumPy, constructs the complex Fourier erasure matrices, and verifies exact analytic matrix-eigenvalue formulas against direct diagonalization for every cycle length from 6 to 40. It exhaustively checks all three-site masks and their precise equality class in those finite orders. It also checks the special six-node endpoint and sampled cosine/asymptotic comparisons. All uniform and asymptotic assertions rely on the analytic proof in RESULT.md; finite checks do not establish the infinite quantifier. Complete older prolate full texts were inaccessible, and independent audit has not been performed.
