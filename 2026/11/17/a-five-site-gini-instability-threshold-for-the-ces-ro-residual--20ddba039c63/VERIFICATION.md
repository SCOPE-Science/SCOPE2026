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

# Reproduction

Run `python3 check_cesaro_residual.py` from this directory. The script uses only Python standard-library `fractions` and `random`; no numerical floating-point values are accepted as proof certificates.

The script exhausts every binary cut in dimensions two, three and four; checks the signed third-coordinate formula for dimensions five through one hundred; verifies the exact discrete difference identities and the finite stochastic-column examples. The unbounded-dimension threshold and logarithmic growth are established by the symbolic induction and column-mass inequalities in RESULT.md, not by the script's finite loops.

The full finite-dimensional operator norm for dimension five onward is not claimed. Independent verification is not performed.
