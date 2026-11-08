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

The result was checked using two standalone exact-arithmetic implementations.

`verify_moran.py` uses SymPy on all transient mutant-subset states. It verifies the two- and three-vertex cases symbolically for arbitrary positive fitness, and confirms the four-vertex diamond rational witness at fitness \(r=5\). Run `python verify_moran.py` after installing SymPy.

`verify_doob.py` uses only Python standard-library rational arithmetic. It independently rebuilds the diamond transition system as frozensets, calculates fixation probabilities, forms the conditional Doob matrix, and solves for the conditional first and second moments. Run `python verify_doob.py`.

Both programs returned PASS when executed from these included files. The all-fitness assertion is confined to the three-vertex bound; only the exact positive-rate witness and a continuity consequence are proved on four vertices. No external independent audit has been performed.
