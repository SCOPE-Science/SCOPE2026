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

# Exact computation and analytical limits

The supplied `check_priority.py` has no external dependencies. Execute `python3 check_priority.py` from the extracted files. It evaluates unilateral service-rank payoff gains independently of the coefficient formulas, computes exact rational Walsh spectra, projects onto gradients by an orthonormal-basis identity, and verifies both stated energies and the potential-share formula for all integer \(N\) from two to nine. It additionally reconstructs the comparison quadratic forms for all \(2\le N\le6\) and checks exact positive pivots on the orthogonal complement of affine increments, and verifies the previously published seven-agent witness probability-free energy ratio exactly.

The infinite-family proof is the explicit algebra in `RESULT.md`: a finite-degree Walsh decomposition and polynomial identities for sums over arbitrary integer \(N\). Finite checks are consistency tests only; none establishes an unbounded quantifier by enumeration. The signed gap has a proved factorization. No claim is made about optimal nonlinear payoffs for larger populations, and the earlier seven-agent and small-population results are attributed to their publication.
