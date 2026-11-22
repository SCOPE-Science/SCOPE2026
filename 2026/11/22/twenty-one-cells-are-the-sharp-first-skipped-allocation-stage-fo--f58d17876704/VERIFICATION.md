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

## Exact checks and limits
Run `python3 checker.py` with `witnesses.json` in the same directory. The script relies only on Python 3 standard-library exact `fractions.Fraction` arithmetic, integer binomial coefficients and finite enumeration; decimal printing is not a logical premise.

- All 63 canonical profiles with 3 through 20 cells have explicit strict rational global-optimality witnesses, checked against every unordered feasible positive triple.
- The proposed missing 21-cell profile is dominated everywhere on the open physical risk interval by at least one of two explicit competitors; two polynomial signs at an exact rational threshold certify it.
- All 70 additional global-competitor comparisons on the two stated rational intervals are certified using strictly positive exact Bernstein coefficients; no interval is sampled.
- An explicit quartic polynomial gives the unique crossing and exact radical expression.

Scientific limits: no general envelope classification beyond the stated 21-cell window; no extension to other wildfire spread distributions or landscape geometries. Self-review only; independent audit not performed.
