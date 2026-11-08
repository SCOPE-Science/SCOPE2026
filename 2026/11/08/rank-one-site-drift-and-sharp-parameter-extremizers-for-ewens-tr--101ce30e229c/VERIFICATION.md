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

# Reproducibility and mathematical checks

The accompanying `verify.py` needs only Python 3 and its standard library. Run `python verify.py`. The completed execution reported `PASS 1270 exact assertions`.

It independently enumerates complete permutations through size eight, groups them by their number of cycles, and checks Ewens-weighted local probabilities for six patterns at all internal sites and four positive rational parameters. It also enumerates three-source partial injections through size twelve, checks their directed-cycle coefficients and verifies the exact total-variation formula. Exact integer positivity checks corroborate the sharp finite-size witness for sizes five through one hundred.

The all-size assertions are established by the proof in `RESULT.md`: contraction of forced permutation paths, an eight-type elementary cycle count, algebraic normalization, the one-root quartic sign argument, and the explicit positive polynomial witness. No bounded numerical experiment constitutes a proof of the infinite parameter or size ranges. The independent audit channel remains unperformed.
