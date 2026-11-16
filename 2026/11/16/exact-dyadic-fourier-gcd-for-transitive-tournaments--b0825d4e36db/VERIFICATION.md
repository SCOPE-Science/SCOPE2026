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

# Verification of the dyadic transitive-tournament Fourier gcd

The stand-alone integer program `checker.py` enumerates all labeled total orders, records their complete edge-inversion vectors, and performs an integer Walsh–Hadamard transform at all frequencies for \(1\le n\le6\). It independently recomputes selected coefficients directly as signs over all permutations. It checks the predicted gcd, the exact divisor, and vanishing at every odd-weight frequency. Deterministic additional sign evaluations are run at \(n=7,8\), 300 frequencies each. The program completed with the exact marker `TRANSITIVE_TOURNAMENT_FOURIER_GCD_PASS`.

The proof handles all positive \(n\) independently of exhaustive finite computation. These tests do not establish novelty, independence or untested all-length conclusions.
