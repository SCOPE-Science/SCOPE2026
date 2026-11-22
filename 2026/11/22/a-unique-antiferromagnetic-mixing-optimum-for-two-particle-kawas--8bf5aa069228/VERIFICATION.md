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

The executable `verify_spectrum.py` directly enumerates every two-particle state and every eligible edge exchange, constructing the full negative Markov generator without relying on the proposed invariant-block matrices. It reports `EXACT_FULL_CHARACTERISTIC_POLYNOMIAL_CHECKS 9` for \(r=2,3,4\) and \(a=1/3,1/2,2/3\), and `TOTAL_SPECTRUM_CHECKS 21` after twelve more full-spectrum comparisons for \(r=5,6,7,8\) and \(a=1/4,1/2,3/4\).

The exact polynomial comparisons check **all** eigenvalues with multiplicity on the tested finite state spaces. The twelve floating-point comparisons use tolerance \(10^{-8}\). The general all-size statement instead follows from the dimension-complete invariant-space decomposition, the strict lower-root bound, and the analytic derivative argument in `RESULT.md`. The source code depends on SymPy, NumPy, and Python standard-library components. No Lean formalization, independent audit, or physical experimental verification is claimed.
