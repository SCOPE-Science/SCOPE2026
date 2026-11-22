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

## Exact checks

Run `python3 verify_quartic_reset.py` with Python 3 and SymPy. The checker evaluates Gaussian moments with exact rational arithmetic and reconstructs the original quartic-drift generator. It verifies the forced source normalization, factorized zero sets, stationary weak generator identity on every coordinate monomial of total degree at most six, and negative source density at one half of the sharp threshold, across seven parameter sets and dimensions 1 to 4. It reports 413 exact assertions passed.

## Scope and limits

The rate bound, uniqueness among Borel reset laws, three critical zero geometries, positivity for every radius, and large-dimension asymptotic are established analytically in `RESULT.md`, not inferred from tests. No claim of exhaustive computation over all dimensions, real parameters, or reset laws is made. A separate independent scientific audit has not been performed.
