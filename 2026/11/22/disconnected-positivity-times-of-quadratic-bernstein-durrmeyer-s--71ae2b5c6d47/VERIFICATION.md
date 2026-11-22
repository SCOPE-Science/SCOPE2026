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

# Verification

The accompanying `VERIFY.py` is an executable, standalone Python 3 standard-library checker. Run `python VERIFY.py` in the extracted directory. Its source constructs Bernstein–Durrmeyer polynomial kernels by exact rational integration, verifies the relevant orthonormal eigenpolynomials, checks powered spectral-kernel values and finite-grid minima, and brackets the two unique roots by numeric bisection. The observed execution completed with `VERIFIED 31260 checks; transitions tau-=0.891289809950934, tau+=1.130946264800073`.

The checker is supplementary evidence only. The continuum kernel lower bound is exact because equality occurs at a boundary point for every auxiliary variable. Strict concavity of the lower-exponent minimum and a one-turn derivative for the higher-exponent minimum establish the complete, all-real-time sign classification. Numerical root values are illustrative; the implicit root equations define the exact transition points. No independent validation has been performed.
