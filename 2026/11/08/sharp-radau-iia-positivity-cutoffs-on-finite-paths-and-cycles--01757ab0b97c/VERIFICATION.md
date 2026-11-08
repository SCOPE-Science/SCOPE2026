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

# Exact reproducibility

Execute `python VERIFY.py` from the directory containing `CERTIFICATE.json`. It requires a current standard installation of SymPy, and uses only exact integer/rational symbolic arithmetic, not floating-point approximate matrices. The expected final line is `VERIFY_OK: 11 graph orders; 60 rational entry certificates; fifth-order witnesses checked.`

The source code directly creates the combinatorial path/cycle Laplacians, calculates `Q.inv(method='DM')*A` in the exact rational-function field, cancels and normalizes each fraction, and checks that the resulting numerator and denominator coefficient arrays match the certificate. The checked rows span every path upper triangle and every cyclic distance. It verifies the coefficient of \(x^5\) of the Radau filter is \(1/108\), and the distance-five powers in \(P_6\) and \(C_{10}\) equal \(-1\) and \(-2\), respectively.

The uniform all-size negative conclusion is the short-walk proof in `RESULT.md`, not an extrapolation from the two boundary tests. Polynomial coefficient sign checks prove positivity at all real positive step sizes for the finite listed graphs. The verifier is same-package reproducibility evidence, not an independent external mathematical audit. It does not test weighted graphs or nonlinear systems.
