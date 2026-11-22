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

# Reproducibility and verification

The independent of external dependencies script `check.py` runs under Python 3.10+ and was executed on the actual delivered package source. It verifies the exact algebraic square identity in the proof over rational \(n,t,s\) grids, positivity boundary inequalities, the two signed endpoint specializations, and numerical matrix spectra using a separately written real Jacobi eigenvalue routine. The observed run passed 22,110 assertions. To reproduce: `python check.py`.

The proof of the universal statement is mathematical: Schur norm/dual trace norm minimax, concave symmetry reduction, a complete invariant-subspace eigenvalue decomposition, an exact nonnegative squared gap, and finite-corner passage to infinity. Finite tests neither prove the optimization for every real \(t\) nor certify infinite-dimensional conclusions; those depend on the stated proof and cited norm theorem. The novelty comparison is literature-limited, and independent auditing has not occurred.
