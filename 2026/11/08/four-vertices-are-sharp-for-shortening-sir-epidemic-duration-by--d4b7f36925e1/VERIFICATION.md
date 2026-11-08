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

# Reproducible verification

Run `python verify.py` using Python 3 with SymPy installed. The code reconstructs the SIR transition rates from the stated graph edges and the declared seed. It symbolically enumerates the 38 labeled possible one-edge insertions across all graphs with two or three vertices and all initial seeds, checks coefficient positivity of exact rational differences, and confirms the four-node strict counterexample by two exact-rational algorithms.

The forward algorithm propagates probability mass through the finite acyclic state graph ordered by irreversible status rank, accumulating expected holding time and new infections, independently of the backward expectation recursion. It checks that terminal probability totals one. These calculations check the precise specified model, not its applicability to field data. The generic monotonicity question for all larger graphs, unique threshold location, and external historical priority are not proved.
