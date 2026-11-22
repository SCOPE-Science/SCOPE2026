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

## Reproducible checks

Run `python3 verify.py` and `python3 check_surj.py` from this directory. The exact rational linear systems independently enumerate 174 number-conserving ordered pairs. The second script performs full finite-subset reachability, yielding 16 globally onto pairs and 4, 84, 70 minimal forbidden two-site-word counts at lengths 1, 2, 3. The first verifies 166 periodic collision witnesses and eight coordinate permutations. All integer calculations are exact. This proves an all-length result, rather than extrapolating finite enumerations.

## Limits

A historical-priority comparison is necessarily provisional, especially with respect to the 2026 barriers-and-blocks paper whose full text was not accessible. External independent mathematical validation has not been performed.
