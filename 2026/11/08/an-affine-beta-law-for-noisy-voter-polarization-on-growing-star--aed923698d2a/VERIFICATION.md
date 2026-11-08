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

# Reproducibility

From the extracted directory, execute `python verify_noisy_star.py` with NumPy, SciPy and SymPy. The checker uses independent stationary finite-state matrices for six sizes and three rate pairs, tests the rational pair-correlation formula, and algebraically verifies the PDMP stationary density equation.

Observed output includes `Symbolic identities: PASS` and `Exact Markov generator checks: PASS`. The checker verifies the critical algebraic identities and finite instances; the infinite limit and invariant-law uniqueness are proved analytically in RESULT.md, not inferred from numerical calculations. No independent review or audit has been performed.
