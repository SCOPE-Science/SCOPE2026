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

# Verification details

The proof has been checked by directly differentiating the three rational export fractions and factoring all derivative coefficients; the positive-parameter regimes follow from the strict order of three critical middle-loss thresholds. The exact rational example is independently reconstructed by matrix inversion. The checker program is self-contained and uses rational Gaussian elimination rather than floating-point solvers.

Execute `python3 checker.py` with Python 3. The packaged check passed 25,248 exact-arithmetic assertions. Finite parameter testing is supplemental only: it cannot prove the parameter-uniform classification, which is established symbolically in `RESULT.md`.

Primary material reviewed included the open 1995 Westerschelde full manuscript sections on advective-dispersive equations and conclusions, the freely accessible 2002 Waikato full-text model discussion, and the 2007 open lake-phosphorus article including its mixing appendix. The 1984 and 2009 papers were accessible only in part, and historical priority remains provisional. No external or independent scientific validation has been performed.
