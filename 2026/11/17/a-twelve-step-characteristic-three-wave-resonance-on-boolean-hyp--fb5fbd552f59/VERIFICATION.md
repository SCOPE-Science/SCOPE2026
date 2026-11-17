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

All calculations are exact in \(\mathbb F_3\). Run the included Python 3 scripts from the package root:

`python3 proof/verify_matrix.py`

`python3 proof/verify_enumeration.py`

The matrix program constructs the ordinary Boolean-cube adjacency and the reversible two-row update with no use of the Walsh eigenvalue formula, checks six fixed nullities and exact global order in dimensions zero through five. The second program independently evolves all labelled initial states in dimensions zero through two and counts every primitive temporal period; it does not use matrix ranks. Captured outputs in `proof/verify_matrix.out` and `proof/verify_enumeration.out` were produced by running the included scripts and correspond to those scripts.

The complete proof covers all nonnegative cube dimensions and all extension fields \(\mathbb F_{3^f}\). The finite tests do not prove the infinite parameter claim, do not establish historical priority, and are not independent review. The validation status is therefore self-review only; an independent audit has not been performed.
