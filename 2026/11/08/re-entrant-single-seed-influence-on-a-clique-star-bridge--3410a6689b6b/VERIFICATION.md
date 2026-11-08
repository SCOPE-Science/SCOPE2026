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

## Reproducibility
The included `verify.py` uses only the Python 3 standard library and prints a PASS line after 68 exact checks. Run `python3 verify.py` from the extracted package directory. No external data or random seeds are needed.

The code derives clique two-terminal connection polynomials by exhaustive edge-state enumeration, derives expected reach polynomials for all nine possible seeds from the 11-edge graph, and checks them against the analytic bridge formulas. It independently computes clique-component expectations by a connected-subgraph recurrence at rational probabilities. It verifies the rational root brackets, transformed quintic, and three representative strict maxima by exact arithmetic.

## Boundaries of verification
Finite examples do not establish the statement for all clique sizes. That statement follows from the explicit independent two-hop lower bound and limiting comparison proved in `RESULT.md`. The uniqueness of the two nine-vertex switches follows from Descartes' rule and exact sign changes, not numerical root-finding. The program does not certify publication priority or independently validate its own proof.
