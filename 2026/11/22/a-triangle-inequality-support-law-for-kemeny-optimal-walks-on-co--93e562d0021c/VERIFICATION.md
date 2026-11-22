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

# Verification notes

The submitted standalone `check.py` uses only standard-library `fractions.Fraction`. It independently computes exact symbolic rational derivatives of the three-orbit Kemeny formula, checks feasibility and stationarity multipliers for every integer triple with \(1\le a\le b\le c\le18\), and checks selected small cases against complete-matrix exact rational inverse traces. The replay yielded: `PASS: 7989 exact-rational checks; triangle, boundary, and asymmetric-size regimes`.

Universal validity relies on the analytical eigenvalue reduction and KKT inequalities in `RESULT.md`, not on finitely many calculations. No independent mathematical audit was performed.
