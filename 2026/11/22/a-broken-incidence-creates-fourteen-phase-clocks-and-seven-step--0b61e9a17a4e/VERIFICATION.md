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

Run `python3 check_matrix.py` and `python3 check_states.py` in a standard Python 3 installation without dependencies. The first independently reconstructs the edited undirected adjacency and checks ranks of powers and periodic fixed spaces for every order from 3 through 34. The second independently builds neighbor lists and follows all binary states on orders 3, 4 and 5, comparing entry/period counts and distinct temporal orbits with the claimed formulas.

Actual outputs are in `matrix_checks.txt` and `state_checks.txt` and end with `ALL_MATRIX_CHECKS_PASS` and `ALL_STATE_CHECKS_PASS`, respectively. The mathematical proof, not exhaustive checks of finitely many graph sizes, establishes every quantified result. No external independent audit was performed. Historical-priority risk remains for inaccessible or unindexed literature.
