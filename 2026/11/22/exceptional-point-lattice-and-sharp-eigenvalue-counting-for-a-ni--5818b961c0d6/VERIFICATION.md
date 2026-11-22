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

# Finite checks and reproducibility

Run `python CHECK.py` with Python 3 and `mpmath`. The actual checked source printed `PASS: 186 finite diagnostic checks`; it tests exact reciprocal characteristic residuals, multiple Lambert branches, critical derivative zeros, positive-coupling real roots, the large-index logarithmic root asymptotics and splitting near double roots. These checks sample finitely many parameter values, not all roots or all couplings. The infinite-dimensional correctness rests on the analytical proof, including the complete-root localization and contour-integral multiplicity argument in `RESULT.md`.

The exact operator is specified via \(Se_n=e_{n+1}/(n+1)\), \(\varphi(e_0)=0\), and \(\varphi(e_n)=1/(n+1)\) for positive indices. These definitions, not finite sections, are the mathematical object. A full-independent audit has not been performed.
