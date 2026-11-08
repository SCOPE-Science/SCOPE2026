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

# Reproducible verification

Run `python3 verify.py` using Python 3 with no third-party dependencies. The checker constructs, rather than hardcodes, the candidate single-atom-deviation rankings for all \(3\le n\le100\) (binary) and \(4\le n\le100\) (ternary), then tests their cardinalities and distinctness from one another and from the identity. It also enumerates all 27 three-label three-atom outcomes for a separately chosen support word and computes an exact rational nonzero 5-by-5 Jacobian minor.

Observed output: `PASS: binary and ternary distinct-permutation witnesses, n<=100; 30465 scalar witness conditions; exact 3-variable Jacobian minor=-2/2187`.

A finite verification run is not an infinite mathematical certificate. The general statement for every integer \(n\ge4\) is proved in `RESULT.md` by an all-size list of distinct single-label relocations and preservation of the nonzero Jacobian minor on a positive-mass neighborhood. The three-variable determinant is an auxiliary check, not a claim of new three-variable priority. No independent validation has been performed.
