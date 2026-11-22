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

Run `python3 verify.py` using only the Python 3 standard library. The program constructs all assignments directly for wheel rim sizes 3 through 10, checks the two-color neighborhood rule, then independently enumerates cyclic rim words by finite-state recurrence for sizes 3 through 50. All counts are integer-exact. The target theorem covers the infinite range \(n\ge9\); finite computations are corroboration only. A successful execution prints `INDEPENDENT_DIRECT_LABELING_CENSUS_3_TO_10_PASS` and `FINITE_STATE_CHECK_3_TO_50_PASS`.

The proof for all sizes is combinatorial. For a colored hub, selected rim vertices dominate the cycle, so \(k\ge\lceil n/3\rceil\). For a zero hub, at least half the rim is selected and the only possible tie at \(n=10\) is forbidden by an odd cyclic inequality. The equality-case neighborhood-incidence bound forces all but at most one selected rim vertex to carry the opposite hub color. Circular gap compositions count the all-opposite-color cases, while exactly \(n\) exceptional placements occur only when \(n\equiv1\pmod3\).

No proof was derived from sampled numerical values. Full access to a relevant 2026 introductory dual-server journal paper was not established, so historical priority remains an independently assessable risk. No independent audit or external certification is claimed.
