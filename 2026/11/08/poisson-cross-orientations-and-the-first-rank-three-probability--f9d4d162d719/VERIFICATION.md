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

Execute `python checker.py` with Python 3 and no third-party dependencies. The exact finite conditional distribution and the first-order formula's semantics were tested on all fair tournament orientations of sizes two through six, for every fixed marked-set cardinality (up to relabeling). Observed exact rational frequencies were compared to the multinomial/binomial coefficients, not to floating-point approximations.

Expected outputs:

`MARKED_TOURNAMENT_EXACT_OK tournament_instances=168146 formula_checks=168146`

`RANK_TWO_COLORED_TOURNAMENT_EF_OK models=1098 signatures=59 representative_pair_games=6786`

The second check directly plays the two-round Ehrenfeucht–Fraïssé game against the asserted neighbor-profile criterion on representative colored tournaments through order four. Neither finite test replaces the exact conditional-independence argument, Poisson limit, or analytic gap inequalities in `RESULT.md`. Independent audit or certification has not been performed.
