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

Run `python3 check.py` using Python 3 with NumPy and SciPy. The script performs 62 finite tests: 48 independent Fourier-versus-Hankel integral comparisons, four exact constant-normalization checks to machine precision, four critical-cutoff slope checks, and six critical-window spot checks. The run produced `PASS 62 independent radial integration, normalization, critical slope, and window checks`.

The verified analytic steps are the Sonine transform identity, the fixed-order Bessel error estimate in NIST DLMF 10.17, the bounded-primitive integration-by-parts estimate uniform in phase and nearby parameters, the exact limiting gamma coefficient, and Fourier uniqueness for finite measures followed by Cauchy–Schwarz. Finite numerical tests do not certify these infinite statements and do not establish publication priority.

The most relevant recent paper's abstract was accessible but its complete manuscript was not. No independent mathematical audit has been performed.
