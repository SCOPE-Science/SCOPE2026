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

# Reproducibility

Run `python verify.py` using Python 3.8 or later; the script uses only the standard library. It implements the per-neighbor three-strategy payoff matrix with exact rational arithmetic, tests all possible unilateral action choices in every profile, and checks the analytic equilibrium sets for paths and cycles of the stated small orders. The original run produced:

`PASS: 85 graph/parameter exhaustive profile comparisons; all parameters rational; exact payoff arithmetic.`

The degree-two local response table and forced word structure in `RESULT.md` prove the all-size claim. Enumeration up to order ten does not prove a statement about arbitrarily many vertices. The 9,999- and 10,000-vertex checks inspect constructed prediction sets rather than exhaustively testing all their possible profiles. No finite-population stochastic conclusion or independent expert certification is asserted.
