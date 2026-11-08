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

# Reproducibility checks

The companion `verify.py` is standalone and needs only the Python standard library. Running `python3 verify.py` enumerates all 20 possible two-sentinel placements on paths of two through five vertices. It compares exact rational Laplace transforms from independent first-event SI Markov recursions with the closed-form Erlang expressions at four positive rational transform arguments per placement, totaling 80 fraction equalities. It also checks the rational mean table and the lower-order sharpness classification. On the reviewed package the program printed: `PASS 80 independent rational Laplace comparisons; all exact mean classes and sharp minima`.

The root uniqueness and all-positive-time optimizer phase diagram are established in the proof using derivative signs. Four transform evaluations are finite corroboration, not an infinite-time symbolic identity certificate. No independent outside audit was performed.
