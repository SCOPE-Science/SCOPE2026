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

# Reproducibility and limits

Run `python3 verify.py` with the Python standard library. The checker reconstructs all eight polynomial branch expansions using exact rational coefficients and checks each coefficient valuation. It enumerates complete least periods and compares every output fiber with the theorem for levels \(1\le k\le12\), as well as initial lower-index comparisons. It checks representative shift-period identities and explicit half-period witnesses.

Expected line: `VERIFY_OK rational_branch_table=8; modulo_power_levels=1..12; period_and_half_period=1..12; lower_columns=1..4; exact_arithmetic=True`.

The program is a finite check only. Universal correctness follows separately from the period identity, the eight exact 2-adic branch decompositions, and bijective lifting on each branch. Historical originality remains subject to unindexed prior literature.
