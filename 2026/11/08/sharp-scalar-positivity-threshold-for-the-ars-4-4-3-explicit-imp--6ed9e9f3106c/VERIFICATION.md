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

The polynomial derivation and sign classification are given in `RESULT.md`. Run `python verify.py` with Python 3.10+ and SymPy 1.12+ from the extracted package; its expected terminal output begins with `VERIFY_OK`. The checker uses exact rational arithmetic and symbolic polynomial identities, not a fitted numerical formula. It reconstructs the stage tableau from independent rational constants, checks the five Bernstein coefficients, the cubic isolation, the entire sign certificate for the quartic at \(t=4\), and 77 additional rational consistency cases.

These finite checks reproduce algebraic identities; the universal quantifiers in the theorem are justified by the sign proofs, not by a finite parameter sweep. The scalar classification does not provide matrix-valued or nonlinear spatial positivity. No independent mathematical audit has been performed.
