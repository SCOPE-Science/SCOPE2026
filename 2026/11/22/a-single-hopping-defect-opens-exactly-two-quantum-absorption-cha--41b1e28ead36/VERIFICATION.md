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

The finding is established algebraically for all integers \(m,n\ge3\) and all positive \(J,w,\kappa\). The proof uses a five-vector invariant orbit-sum decomposition, a nonvanishing singular-value determinant for \(w\ne1\), and positivity of the off-diagonal Gram entry. At \(w=1\) the rank-one biadjacency gives precisely three visible modes.

Run `python3 verify.py` in a Python 3 standard-library environment. It constructs rational Hamiltonians, Krylov spans, and orthogonal projectors without floating-point arithmetic and compares the theorem against \(64\) parameter instances. The expected output is `EXACT_BRIGHT_PROJECTOR_CHECKS_PASSED 64`. This is a supplementary finite consistency check, not a substitute for the all-parameter proof. Published models and historical priority were compared only as described in the accompanying review; independent scientific audit has not been performed.
