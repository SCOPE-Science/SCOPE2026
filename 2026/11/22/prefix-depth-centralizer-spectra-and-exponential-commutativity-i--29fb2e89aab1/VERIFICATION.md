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

# Verification scope
The standard polycyclic product, centralizer formulas, multiplicity census and commuting pair formulas were checked against exhaustive direct word-pair multiplication using `check.py` and captured in `check-output.txt`. Tested parameters were \((r,N)=(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2)\); the exact asymptotic coefficient was compared to calculated finite-cutoff deficits for \(r=2,3,5\). No random sampling is substituted for the exhaustive finite cases.

All unbounded assertions rest on the prefix-case proof and convergent geometric series given in `RESULT.md`, not finite enumeration. Direct checks do not certify novelty, independence or statements outside the specified family. Independent audit has not been performed.
