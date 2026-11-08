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

The standalone `verify.py` is included. Execute with `python3 verify.py` (standard library only). It independently implements the Borda scores, simultaneous-lowest-elimination winner, strict pairwise margins, and two proposed necessary-and-sufficient tests. It checks 605,682 exact profile-plus-vote combinations through 17 original voters and verifies six first-boundary events are the full candidate-relabeling orbit of a canonical witness. It checks a second-type witness at 12 original voters. The all-electorate theorem is based on a separate exact case proof; finite checking is not treated as its proof. The known lower bound previously appeared in Brandt et al. (2022). Independent scientific auditing has not occurred.
