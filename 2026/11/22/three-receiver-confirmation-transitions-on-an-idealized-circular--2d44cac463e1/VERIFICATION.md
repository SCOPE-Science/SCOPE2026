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

# Reproducible mathematical checks

The theorem is proved analytically in `RESULT.md`. The stand-alone `checker.py` independently obtains each arc multiplicity by endpoint partition, evaluates the Bernoulli event-success probabilities, and compares with the analytical bound. With the fixed random seed it passes 18,000 random placement tests and 14 exact-threshold cases. It checks the count identity, geometric constraint, three attaining placements, regime selection, and the concrete numerical example.

Run: `python3 checker.py` (Python standard library only).

The calculations cannot establish priority, field calibration, or infinite-domain correctness on their own. Infinite-domain correctness rests on the interval-geometric argument and affine maximization in `RESULT.md`. The independence assumption applies to separately constructed receivers, even at coincident sites, and may fail in deployment. No external independent audit has been performed.
