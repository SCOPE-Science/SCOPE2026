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

# Verification and reproducibility

`check_power.py` independently enumerates all elements and repeated semidirect-product multiplication in 22 parameter-depth configurations. It computes the complete output histogram and compares each target multiplicity with the Jordan-filtration prediction; all cases returned PASS. `check_power.out` records each group size, image size and the sum of all multiplicities. Run with `python3 check_power.py`; Python 3 standard library suffices.

Finite exhaustive checks cannot validate universal quantifiers by themselves; the detailed cyclic-module argument and image-fiber proof in `RESULT.md` establish the infinite family. The 2014 upper-central-series full text was unavailable. No independent mathematical audit was performed.
