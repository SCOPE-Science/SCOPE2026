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

# Reproducibility

Run `python check_counts.py` to compare the formula with all weighted occupancy states for \(729\) ordered tripartite shore triples, each shore size \(1\) through \(9\). Run `python check_direct.py` for direct bit-level iteration of \(646680\) labelled initial configurations over \(80\) unordered tripartite profiles. Both were run from extracted final embedded sources and yielded the exact captured outputs at `checks/counts.out` and `checks/direct.out`.

The unrestricted theorem is proved by the two-time structural classification in `RESULT.md`. Neither finite verification alone nor any search-result absence certifies its infinite validity or priority. No independent audit has been performed.
