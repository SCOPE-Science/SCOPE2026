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

Run `python3 check.py` with Python 3 and the standard library. The checker enumerates all labeled Cayley trees on 3–7 vertices by Prüfer codes. It checks 101 exact rational identities: mixed anchored factorial moments for one or two designated hubs, full fixed-hidden-count root deficit distributions, and the fixed-two-vertex graph-distance formula. Expected output: `PASS: 101 exact rational checks of anchored factorial moments, root deficits and two-vertex distances on all Cayley trees with 3<=n<=7`.

The check is finite. Infinite-n convergence is supplied by the algebraic factorial-moment limit, the exact root-component law and tightness, a hub-separation union bound, and truncation to a proper finite marked Poisson limit. Numerical/finite checks do not certify infinite claims or historical priority.
