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

# Verification

From the directory containing `verify.py`, execute `python verify.py` with Python 3.9 or later. The script uses only the Python standard library. In the performed run it reported:

- PASS: exact symbolic identities and inequality boundaries for integers 3 through 399;
- PASS: 196 independent full symmetric Jacobi-spectrum comparisons;
- PASS: 21,000 numerical invariant-design comparisons;
- PASS: constructed optimal kernels feasible and attaining the claimed SLEM for integers 3 through 399.

These reproducible finite checks support the identities and detect errors in the matrix decomposition. They do not prove all integers, scientific novelty or unique global optimization; those are addressed, with explicit scope, by the analytical proof in `RESULT.md`. The SLEM objective is the spectral norm on the orthogonal complement of the constant vector. Matrix comparisons include both positive and negative eigenmodes. Holding probabilities are residual diagonal entries, not preassigned uniform values.

The infinite-family correctness argument is the two-block spectral decomposition, the small-size norm lower bound and a convex subgradient lower certificate in the large-size branch. No external independent validation has been undertaken.
