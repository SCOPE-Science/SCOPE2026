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

# Reproduction

Run `python3 verify.py certificate.json` (standard Python 3 only). Expected exact line: `S4_SUBGROUP_CONJUGACY_QUOTIENT_SEVEN_CYCLE_OK 30 [9, 15, 6]`. The program exhaustively rebuilds 24 permutations, all 30 subgroups, conjugation orbits of 115 strict chains, 9/15/6 orbit cells, incidence maps, two-step integral cellular boundary composition, eight individually valid free-face pairs and the final connected seven-cycle. No numerical approximation or sampling is used.

# Limits

This verifies the finite claim, not publication priority, mathematical independence, or a general formula for other finite groups.
