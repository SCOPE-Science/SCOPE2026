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

# Verification scope

`python3 verify.py` compiles and replays both C++17 complete enumerators against all 100 rows of `AVALANCHE_COUNTS.csv`. The first implementation directly applies Dhar's legal-burning deletion test to all 48,828,125 stable states, then topples lowest-index unstable sites. The second independently constructs the graph from two pentagonal rings and poles, checks recurrence with the burn-addition replay criterion, and topples highest-index unstable sites. No seeded sampling or Monte Carlo approximations are used.

The outputs must agree on exactly 5,184,000 recurrent configurations, 100 nonzero joint coefficients, normalization and the support endpoints 11, 28 and 29. Auxiliary exact reduced-Laplacian determinant and automorphism orbit computation justify the recurrent count and the three source-distance representative classes. The output `VERIFY_OK` is a reproducible check of the finite enumeration; it is not independent expert review. This calculation does not certify an asymptotic statistical-mechanical scaling law.
