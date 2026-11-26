---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Reproduction and limits

Run `python3 checker.py` using only the standard library. The exact rational check enumerates both the strategic type and auxiliary action vectors and keeps the probability mass and integrated risk of each environment stratum separate. It tests the payoff components without counting contribution costs as saved endowment. The parity counterexample is outside the theorem's hypotheses and shows why independence of the entire type vector from risk matters even if each marginal type is independent of risk. The infinite-size and strict single-crossing assertions are proved in `RESULT.md` under the stated joint independence assumption.
