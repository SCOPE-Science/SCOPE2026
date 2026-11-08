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

The accompanying `checker.py` uses the Python standard library only. Run `python3 checker.py` in a directory containing this file to evaluate 321 reproducible positive-parameter configurations using 10,914 assertions. It compares the two-geometric mass formula against direct iteration of the independently assembled killed Markov matrix, checks eigenvalue ordering and weight positivity, confirms the matrix determinant and the strict interlacing identity numerically, and compares the reset-count mean with the known first-hitting-time formula. The recorded run returned `PASS: 10914 deterministic diagnostics across 321 parameter configurations`.

A separate finite-difference solution of the coupled backward boundary-value problem at \(p=1/2\), \(r=c=D=a=1\) agreed with the analytical first-cycle absorption probabilities within \(6.3\times10^{-6}\). Direct symbolic simplification under \(z=A^{-2}\) gave exactly zero for the difference between \(\det(sI-K)\) and \(-pquv/(AB^2)\), and exactly zero for the difference between \(\det K\) and \(z(1-h_1)\).

The numerical checks are not exhaustive and are not the basis of the theorem's universal quantifiers. The analytical derivation and equality/strictness reasoning reside in RESULT.md. No numerical failure, finite search, or formal external certification is presented as evidence of novelty or universal correctness.
