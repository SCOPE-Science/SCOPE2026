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

Run `python3 verify.py` using Python 3.10 or newer; no external packages are needed. The script enumerates every labeled tree on 2–8 vertices by Prüfer sequences (280,392 total), verifies the proposed path/star bounds and equality characterization, explicitly constructs positive-semidefinite Gram witnesses for 480 randomly sampled feasible tree-edge configurations, numerically integrates 18 beta functions by an independent composite Simpson rule, checks their recurrence, compares 30 star volumes with the previously published triangular-book beta formula, and checks the sharp ratio asymptotic.

Observed output: `TREE_ELLIPTOPE_DEGREE_VOLUME_PASS explicit_trees=280392 auxiliary_checks=566`.

The infinite-domain proof is the constructive tree Gram completion, conditional interval factorization and strict convexity/majorization argument in `RESULT.md`. The finite code verifies formulas and implementation conventions but does not certify historical novelty, prove theorems beyond the written arguments, or replace independent validation. Endpoint correlations are handled in the proof by continuity and measure-zero Fubini sections, not by a numerical boundary experiment.
