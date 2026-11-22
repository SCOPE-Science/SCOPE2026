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

# Verification of the mathematical claim

Execute `python3 verify.py` from the directory containing the files. This script uses only Python's standard library, `fractions.Fraction` and exhaustive pairing enumeration. It was executed on the delivered source and returned `PASS` with **142 exact assertions**. The calculations check rational values of the central cross-projection integral, the Hoeffding first-projection moments, exact crossing-count and degree joint moments for all perfect matchings of up to six chords, and the exact finite mixed-moment polynomial at a range of sizes.

This is not a machine proof for all integers or a numerical certification of the limiting distribution. The argument for infinite weak convergence is the analytic conditional i.i.d. central limit theorem plus a variance-bounded degenerate U-statistic remainder, stated in `RESULT.md`. There is no independent review or external validation.
