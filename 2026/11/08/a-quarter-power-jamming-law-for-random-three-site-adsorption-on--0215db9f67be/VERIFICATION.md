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

The `verify.py` program uses only the Python standard library. From this directory run `python3 verify.py`. It computes exact terminal distributions by two distinct constructions: (i) recursively evaluating all labeled occupancy bitmasks and distinct three-site paths, and (ii) recursively evaluating the pair of unoccupied part sizes. All 16 cases with both part sizes between one and four give exactly identical rational distributions. Across 9,798 admissible count states, the conditional drift and variance formulas are checked using rational arithmetic. The deterministic seeded simulations of three larger systems are exploratory diagnostics only.

The proof of the limiting distribution is in `RESULT.md`, including the deterministic drift normalizer, the martingale central limit theorem conditions, a negligible final stochastic increment, and the first-boundary-crossing argument. An analytic asymptotic claim cannot be certified by finite simulation alone. No independent scientific audit has been performed.
