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

# Reproducibility and limits

The core argument is analytical, with definitions and all boundary cases in `RESULT.md`. Run `python verify.py` in the directory containing these files, with a normal Python standard-library installation. The checker was extracted from the prospective complete package and returned `PASS 21494 assertions`, together with the sample activation threshold `1.033440586918726` and limiting second gap `0.514564753997183`.

Checks cover the positive Poisson-tail series, representative monotonic elasticity inequalities, the three-stage example, active-set Karush–Kuhn–Tucker equations, 100 randomized heterogeneous configurations checked against 150 competing allocations each, and long-range asymptotic numerical behavior when two stages tie for minimum effective decay. These numerical checks are finite; they neither exhaust all parameters nor prove the infinite result. Strict concavity, global optimality, and exact exponential asymptotics are proved independently in `RESULT.md`. No external computation service or formal proof assistant was used. Independent validation has not been performed.
