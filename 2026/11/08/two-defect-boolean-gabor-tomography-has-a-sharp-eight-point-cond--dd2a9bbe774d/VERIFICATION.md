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

The source file `CHECK.py` uses only Python's standard library. Run `python3 CHECK.py` from the same directory to perform exact Gaussian-integer calculations of all \(N^2\) Weyl ambiguities in \(N=8,16,32\), with ten window parameter pairs for each order. For \(N=8\), it additionally forms every rank-one orbit projector explicitly and performs modular Gaussian elimination on the vectorized projectors for five Gaussian-integer windows, giving a second type of rank check. The coefficient embedding in the prime field is used only for these finite consistency tests; the all-parameter complex theorem comes from the exact algebraic identities in `RESULT.md`. It also tests all eight proposed optimizers for each of \(N=8,16,32,64\).

Actual completed execution returned `TWO_DEFECT_BOOLEAN_GABOR_EXACT_CHECKS_PASS 30 spectral enumerations, 5 exact modular projector ranks, 32 sharp optimizers`.

The universal proof checks separately the sign classes at shifts outside the two-point subgroup, the two special shifts, the spectral diagonalization, both ranges of the optimization variable, and the complete equality case. No statistical Monte Carlo or finite-only extrapolation is used. The C/O/V review in `REVIEW.md` is a bounded self-review; independent external validation has not been performed.
