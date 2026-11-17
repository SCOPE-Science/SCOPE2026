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

# Reproducible checks and limits

Run `python3 verify_persistence.py` with standard Python 3 (no third-party dependencies). The program independently determines the birth stage of every admissible simplex directly from induced graph degrees in the matching-deleted complete bipartite graphs. It then reduces the full filtered simplicial boundary matrices over \(\mathbb F_2\) for six parameter profiles \(3\le a\le b\le5\). Its printed intervals reproduce `verification_output.txt`, culminating in `MATCHING_DELETION_INTEGRAL_STRUCTURE_MOD2_PERSISTENCE_PASS profiles=6 faces=477`.

The checks distinguish the birth and death parameter for each interval, not merely stagewise Betti numbers. They do not certify arbitrary sizes or integer maps. Those statements are justified in RESULT.md using natural two-pole quotient complexes, explicit CW square models, and primitive fundamental graph cycles; they have not received independent mathematical review.
