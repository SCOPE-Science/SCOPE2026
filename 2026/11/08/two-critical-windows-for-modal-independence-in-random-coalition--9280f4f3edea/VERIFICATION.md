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

# Verification details

The direct finite-game checker enumerates the 3, 81, and 19,683 possible labelled ternary action tables for one, two, and three actions per player, respectively. For each table it checks the semantic value of all disjoint-coalition independence-axiom instances against the pure-line characterization, and tests implication from action independence to modal validity. It additionally enumerates the exact action-independence probability at rational cell probability 2/5 and compares it to the closed rectangular-support sum. The program's success marker is `COALITION_IA_FINITE_CHECKS_OK`. The infinite upper-window theorem is justified by a direct factorial-moment argument, not by numerical simulation. No independent mathematical audit has been performed.
