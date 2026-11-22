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

# Reproducibility of the star-heat Nyström claim

Run `python3 CHECK.py` using Python 3.10+ (standard library only). The checker constructs the exact spectral projectors with rational arithmetic, verifies that the spectral formula composes at twice the time, and evaluates both landmark trace gains, the sign factor and the diagonal inequality. It evaluates six independent rational decay parameters for each star size \(2\le m\le14\) and spot-checks the positive threshold by bisection for ten sizes. The actual checked output was `PASS: 15458 exact-rational and numerical assertions`, with sample thresholds \(\tau_2=0.545424232976\), \(\tau_3=0.495053264332\), \(\tau_{10}=0.312228575934\), and \(\tau_{100}=0.071469250542\).

A separate numerical test formed the full Laplacian and compared the closed-form gains to a matrix exponential for several star sizes, including near the crossing. Finite computational checks are illustrations only; the all-dimension and asymptotic assertions require the projector identity, exact difference factorization, monotone crossing equation and asymptotic argument given in `RESULT.md`.
