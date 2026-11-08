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
# Computational verification

Both included scripts were executed with Python 3 and outputs saved in companion `.out` files. `verify_exhaustive.py` generates each feasible state from all subsets, explicitly constructs the state graph and obtains all-pairs shortest distances by breadth-first search, then tests them against the explicit four-lift formula. `verify_constructive.py` separately generates valid sets, verifies every coordinatewise meet and performs the single-coordinate decrement construction to its completion, checking the exact move total. The checks cover 48 and 54 parameter cases respectively; the latter visits 17,467 unordered state pairs. Program termination with successful exit status and printed `PASS` is the finite-evidence criterion.

The proof is independent of any finite computational coverage. For reproducibility, run `python3 verify_exhaustive.py` and `python3 verify_constructive.py`.
