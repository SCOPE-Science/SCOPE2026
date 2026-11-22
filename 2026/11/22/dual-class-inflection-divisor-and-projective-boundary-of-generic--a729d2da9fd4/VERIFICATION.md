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

`checker.py` runs with Python 3 and SymPy and uses exact rational arithmetic to check the curvature determinant, degree and squarefreeness for ten coprime frequency pairs, the basepoint-free Gauss polynomial triple, arithmetic genus, and the full Wronskian-weight identity. Execute `python checker.py`; each tested pair prints its numerical invariants and the program terminates with `ALL 10 EXACT CHECKS PASSED`.

This finite computation is not an exhaustive proof for all coprime frequencies or all transcendental phase coefficients. The general proof uses a basepoint-free parametrization, explicit fiber coincidences, characteristic-zero duality, Puiseux expansions, and separability of a rational function. All mathematical assumptions and exclusions are in `RESULT.md`.

Self-review was passed; independent audit has not been performed. No external proof assistant or independent certification is claimed.
