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
# Verification record

The proof's key invariant is the dimension of the solution space after each tridiagonal row. The packaged checker independently enumerates the unstructured free coefficients and calculates matrix ranks over finite fields, including nonprime \(\mathbb F_4\); a separate graph branch directly builds the alternating adjacency matrix. Exhaustive scopes and rank-cell comparisons appear in `checks/verification_output.txt` and finish with `LADDER_CHARACTER_RANK_TRANSFER_PASS`. The ranks are computed by finite-field Gaussian elimination, and this finite replay cannot establish an all-dimensional statement by itself.

The self-contained argument in `RESULT.md` supplies the all-dimensional boundary propagation and the odd-characteristic group-theoretic justification. The checker verifies the degree-square identity in its odd-field graph cases; it does not independently construct character tables. The nonsingular coefficient comparison uses the published two-term tridiagonal determinant recurrence, checked symbolically for prime-power samples. All additional potential higher-width patterns remain outside scope.
