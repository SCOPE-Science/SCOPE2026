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

# Reproduction and limits

Run `python3 check_temporal_efx.py` from the same directory as this file. Only the Python standard library is required. The verifier computes cumulative values from individual item allocations directly, then takes the minimum of the exact EFX ratios over every prefix. It iterates all \(4^3=64\) three-day schedules at each of 21 rational ratios, for 1,344 schedules in total. A separate set-based dynamic check tests reachability of exact EFX over nine days for those ratios. Additional rational tests cover the branch values and crossover polynomial. The verifier exits nonzero on any failed assertion and prints three PASS lines otherwise.

Verification status: finite exact enumeration passed, analytic continuum proof reviewed in `RESULT.md`. The finite instances do not provide exhaustive evidence over real \(H/L\), arbitrary later horizons, or unconsidered fairness definitions. The theorem's real-parameter and all-horizon components depend on the written proof. Independent external audit not performed.
