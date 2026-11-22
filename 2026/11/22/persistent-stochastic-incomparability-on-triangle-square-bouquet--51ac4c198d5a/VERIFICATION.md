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

# Reproducibility and verification
The full finite-state checker is `CHECK.py`; run `python3 CHECK.py` without third-party packages. It builds the graph from its edges independently of the analytic proof, computes exact sequential random-availability dynamics using rational arithmetic, and directly enumerates all maximal independent sets. It checks the three-point laws for the three smallest parameter values and verifies crossover and total-variation identities for eighty finite parameters. The checker's finite coverage does not establish any limiting theorem. The all-parameter proof is the analytic argument and inequalities in `RESULT.md`.

The initial \(r=2\) example is published previously. Unindexed general formulas for cycle bouquets could still cover this theorem; no independent publication-priority or mathematical audit is claimed.
