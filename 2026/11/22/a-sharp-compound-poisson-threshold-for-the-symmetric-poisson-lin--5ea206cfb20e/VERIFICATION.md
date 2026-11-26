---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification notes

Exact symbolic checks in `check_spl_divisibility.py` verify normalization, Poisson-kernel differentiation, numerator and boundary factorizations, and the exact fourth-Fourier-harmonic obstruction at \(\theta=13/27\). For each boundary polynomial the script checks opposite signs at consecutive multiples of \(10^{-20}\), which certify the printed decimal prefixes given uniqueness of the positive roots. It also checks the decimal prefixes after transforming those brackets by \(r\mapsto 1/r-1\), without converting the bracket or root to floating point. Finite numerical characteristic-function sums independently corroborate the closed expression at several parameter values and angles.

The complete infinite-divisibility equivalence uses a mathematical proof from the absolutely convergent cosine logarithm and the classical lattice compound-Poisson characterization; checking a finite number of harmonics alone would not prove the theorem.
