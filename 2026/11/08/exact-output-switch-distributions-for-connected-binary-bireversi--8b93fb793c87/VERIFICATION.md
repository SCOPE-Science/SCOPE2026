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

# Verification

Run `python3 checker.py` with Python 3.9 or later. The code independently enumerates all invertible reversible binary Mealy transition/output tables on 1–5 labeled states and checks bireversibility directly from the defining inverse-output transition maps. For each valid table, it also classifies connectivity by reachability in the state-transition graph. These brute-force counts are compared coefficient-by-coefficient against the exact formulas and separately implemented component recurrence.

Observed complete successful replay: 470,322 tables examined; all switch-count coefficients match for state sizes 1–5, and the component recurrence produces nonnegative symmetric polynomials through state size 9. The checker contains no external dependencies. Direct enumeration ends at 5 states and does not prove the infinitely quantified theorem; see `RESULT.md` for the proof.

The proof assumes labeled state and alphabet sets, no distinguished start state, and complete invertible reversible Mealy tables. The relevant 2026 structural paper could not be fully inspected, leaving priority risk. Independent audit is unperformed.
