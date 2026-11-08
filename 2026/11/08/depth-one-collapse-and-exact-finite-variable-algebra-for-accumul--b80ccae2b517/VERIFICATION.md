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

Run `python3 checker.py` with the Python standard library. The test builds random modal formulas over zero through three atoms, evaluates them independently at finite-periodic isolated points and at their unique accumulation point, and compares with the explicit semantic coordinates. It performed 1,680 seeded formula/periodic-tail trials; the output was `OMEGA_PLUS_ONE_MODAL_NORMAL_FORM_CHECKS_OK 1680 RANDOM_FORMULAS_AND_PERIODIC_MODELS ONE_VARIABLE_SEPARATION 8 ONE_VARIABLE_CLASSES 256`.

The code also checks distinct signatures for all eight semantic coordinates for one variable, establishing that four explicit modal-depth-one generators distinguish them. Generality over all formulas, all \(k\), and all valuations is established by the proof in `RESULT.md`, not by this finite check. No independent external validation is represented.
