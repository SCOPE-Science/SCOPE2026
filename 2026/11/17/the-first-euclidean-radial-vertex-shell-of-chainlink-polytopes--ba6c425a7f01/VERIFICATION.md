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

The analytical proof establishes all real parameter values \(s\geq2\), \(\ell>0\), \(a_i\geq2\ell\). The independent finite checker `verify.py` uses exact rational Gaussian elimination, enumerates feasible vertices as intersections of supporting hyperplanes, and checks the complete second-shell equality set and count in 237 integer parameter profiles. Run it with `python3 verify.py` using the standard Python 3 library only. Expected output: `CHAINLINK_EXACT_INTERSECTION_PASS profiles=237`. Finite checks are corroboration, not a proof for all real parameters. The earlier external numerical halfspace comparison covered 1,016 additional integer parameter profiles through six dimensions, with no conflicting case. Historical novelty is provisional; independent audit is not performed.
