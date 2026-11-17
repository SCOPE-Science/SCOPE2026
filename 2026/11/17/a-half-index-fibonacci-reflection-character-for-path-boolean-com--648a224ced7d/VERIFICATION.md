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

# Reproducible checks

Run `python verify_boolean_path.py`; standard-library Python suffices. The attached `verify_output.txt` is the actual output of a separate execution and ends in `VERIFY_OK`.

The program enumerates supports and acyclic orientations (no exhaustive-word enumeration assumption), computes the correct oriented cell boundaries, tests boundary squared zero and reflection commutation for every cell at sizes two through eight, then tests finite-field ranks of boundary maps. It separately enumerates all fixed cells for the augmented Lefschetz trace through size twelve. The verifier has a finite scope; the all-parameter theorem rests on the explicit weighted-subset recurrence in `RESULT.md` and the referenced nonequivariant homotopy result. Finite-field ranks are corroboration rather than proof of integral torsion claims; no such claim is made. Independent audit has not been conducted.
