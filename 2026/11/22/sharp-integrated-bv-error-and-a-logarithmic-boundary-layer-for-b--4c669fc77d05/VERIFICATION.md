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

Run `python check_baskakov.py` with Python 3, NumPy, and SciPy. The source file is included intact. In the current check the script reported 324 direct negative-binomial tail comparisons, 81 original integrated single-jump comparisons, and 81 convex cell endpoint comparisons, and passed its assertions. The tested degrees include 10, 30, 100, 300, 1000, 3000 and 10000 for the asymptotic diagnostics. The finite diagnostics are empirical support only and cannot certify all positive degrees or logarithmic limits; the proof in `RESULT.md` establishes those quantifiers.

The exact finite formula can independently be evaluated using regularized incomplete beta functions as specified in `RESULT.md`. The reported floating-point optimizer positions are approximations, not a certificate of a unique winning cell for any given degree. The self-review passed; there has been no independent audit, independent proof verification, or historical-priority certification.
