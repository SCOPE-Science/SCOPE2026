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

# Verification and reproducibility

Run `python3 verify.py` with the Python 3 standard library from this package directory. The observed run printed `PASS: 182 exact phase-integral identities; 14 numerical coupling checks; positive low-coupling minimum, convexity kernel and zeta-asymptotic checks.`

The exact-rational tests integrate the phase identity by branch partition for gains \(2\) through \(8\) and a grid of rational shifts. The numerical tests integrate the periodic Bernoulli function for fourteen coupling values, including \(400\), and compare with the analytical low-coupling polynomial and leading large-coupling constant. The full theorem relies on the analytically reconstructed first-period, convexity, and Fourier/Gamma arguments in `RESULT.md`. Finite numerical tests alone cannot certify positivity for every real parameter or the asymptotic at infinity.

No independent validation or external mathematical audit is represented by these checks.
