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
# Verification of the finite and asymptotic calculations

The proof supplies exact mass formula (3), multinomial characteristic-function convergence (5), Fourier inversion (7), and the local limit (8). The standalone standard-library script `checker.py` exhaustively checks the leaf-valuation model through branching degree four against exact multinomial sums for several threshold and equality events, including a parity-gated formula. It also numerically computes the entire two-category difference distribution at branching degrees 100, 400, and 1600.

Run: `python checker.py`. Expected terminating output contains `EXACT_FINITE_CASES_OK` and `ALL_CHECKS_OK`. The asymptotic reference constants are approximately 0.315809388873 for \(n^{1/4}\) times the tie mass and 0.157904694437 for \(n^{1/4}\) times the weak-inequality excess above one half. The finite numeric convergence is not monotone-fast; the script uses an honest 0.02 tolerance at the largest degree. No finite calculation establishes the general limits, which depend on the separate proof.

No independent mathematical audit is represented by this file.
