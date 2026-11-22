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

# Reproducibility and limits

The standalone `check_certificate.py` uses integer combinatorics, `fractions.Fraction`, and no external dependencies. Invoke `python3 check_certificate.py`. It checks 510 exact rational assertions, including the complete fourteen-case dual table, complete binary cube vertex checks, Fourier parity reconstruction, kernel entries and the \(-2/7\) deficit.

The globally quantified lower bound is proved in `RESULT.md` using compact-group Bochner theory and the explicit dual inequality; executing a finite checker cannot certify the functional analytic premise by itself. The function class consists of continuous real nonnegative positive-definite \(2\pi\)-periodic kernels, not all nonperiodic Fourier transforms on Euclidean space. The reported mathematical review was performed within the same review process; independent audit has not been performed.
