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

The mathematical argument is contained in `RESULT.md`; no external or inaccessible program is needed for its proof.

Run `python verify.py` under Python 3. The checker enumerates every labeled triangle-free simple graph on at most six vertices, confirms the \(3a(G)\le4e(G)\) inequality for 6,228 graphs, tests equality at a four-vertex path and the two-edge path boundary, and performs seeded construction-invariant and approximate survival-profile tests at \(n=2000\) with 420 trials.

Actual recorded execution: `ALL CHECKS PASSED`, including checks for the 6,228 graphs. At normalized horizons 0.5, 1.0, and 1.5, respectively, the observed survival fractions were 0.8547619, 0.5333333 and 0.2452381, against normalized theoretical approximations 0.8510084, 0.5244877 and 0.2239498. Simulations are not proof of the asymptotic cdf; the analytic proof uses conditional hazard comparison and a bounded collision-budget expectation.

Limits: Full second-endpoint choice only, bounded rescaled time horizons, no claim of finite-size exact optimality, no independent audit.
