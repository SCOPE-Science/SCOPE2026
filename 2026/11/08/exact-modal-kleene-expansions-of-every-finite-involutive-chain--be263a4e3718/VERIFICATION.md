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

# Reproducibility and scope

Run `python3 check_modal_kleene_chains.py` using Python 3 and its standard library. The program enumerates all nondecreasing unary operations on each chain with sizes 2 through 9, tests the three original modal Kleene equations (not just the simplified condition), and checks exact equality with the two-case normal form, every count and normality/center statistics.

The closed forms hold for every integer size at least two by the independent mathematical proof in `RESULT.md`. A successful finite run is a check of formulas and implementation, not an infinite proof. No theorem prover or external certification was used. Independent mathematical and historical-priority audit has not been performed.
