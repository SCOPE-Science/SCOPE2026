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

# Reproducibility and proof boundaries

The attached `checker.py` is a self-contained Python 3 program. Execute `python3 checker.py`; a successful run ends with `DYNAMIC_ALEXANDROV_NECKLACE_ALGEBRA_OK`. It enumerates all valuations and pointed worlds at eleven finite \((k,m)\) settings, computes the modal bisimulation-refinement partition using next successors and spatial successor-class sets, checks agreement with the necklace formula, and explicitly evaluates the characteristic formulas in eight settings. These are 2022 pointed valuations in total. Its extra composite-formula checks include eventuality.

The all-parameter formula algebra is justified separately by the normal-form/characteristic-formula proof in `RESULT.md`, not by extrapolation from a finite run. The crucial cases are the root's fixed temporal orbit, leaf rotation orbits, and the unique constant-color root/leaf identification. The checker does not provide an independent human audit or a certificate for infinite parameter ranges. Any claims beyond cyclic dynamics on rooted Alexandrov stars remain unproved here.
