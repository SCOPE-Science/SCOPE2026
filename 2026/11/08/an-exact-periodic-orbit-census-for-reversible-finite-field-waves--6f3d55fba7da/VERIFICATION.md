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

The proof is a complete algebraic reduction over a splitting field, not a numerical extrapolation. The critical local assertions checked in the proof are the polynomial factorization \((t-z)(t-z^{-1})=0\), the resonance identity \((t-\zeta)^2=\epsilon^2t/z\) at \(\zeta^2=1\), the resulting exact Jordan-block lengths, and the required prime-power valuations. Counting kernels across all cyclic characters establishes the finite-field formula.

Run `python3 verify_matrix.py` and `python3 verify_enumeration.py` from the package directory. Both require only the standard Python library. The first performs exact matrix-rank and global-order tests on 1,235 \((n,p,k)\) cases. The second enumerates 103,788 configurations and checks 36 independent fixed-point totals using direct state updates. The included stdout files give the outputs observed when the supplied programs were executed. Neither finite checker alone proves the universal assertion. Independent mathematical review is outstanding.
