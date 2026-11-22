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

# Verification record

Run `python3 verify.py` in the same directory as this file. The checker reconstructs all pairings of 4, 6, 8, 10 and 12 ordered endpoints (corresponding to two through six intervals), independently computes graph degrees and disjoint-endpoint-tail counts, and checks the known exact baseline probability of no universal vertex. It also tests the deterministic degree-probability lower bound and the two-sided Poisson intensity formula, then performs a seeded, explicitly nonproof numerical comparison of the smallest-degree mean.

The checker has been executed successfully with `PASS: exact pairings and endpoint identity, localization inequality, intensity, seeded sanity; checks >= 11491`.

The infinite-dimensional Poisson limit, its joint coupling, conditional Poisson law and strict positive limiting covariance are justified by the proof in `RESULT.md`; finite checker output is not an asymptotic certificate. The supporting published literature was compared for model identity and statement implication; incompletely accessible sources and possible broader implicit priority are listed in `REVIEW.md` and `AUDIT.json`. No independent audit has been performed.
