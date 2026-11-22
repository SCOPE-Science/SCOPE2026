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

The theorem was checked by an exact symbolic algebra and independent numerical script, `CHECKER.py`, using `sympy` and `mpmath`. Run `python CHECKER.py` from the directory containing the proof and code. A successful replay prints `PASS 137 checks` and the derived jump and onset locations. The source of the critical values is the exact resultant and the sign/concavity arguments in `RESULT.md`, not a numerical sweep.

The replay verifies the rational stationary heat response by symbolic differentiation, direct moment equations and time-domain integration. It checks the sextic polynomial, resultant identity, exact rational sign witnesses and representative global maximizers across the transition intervals. The code covers finitely many numerical parameters, so it does not independently establish the universal quantifiers.

The asserted observable is the *translational* heat flux into the thermal bath. The active angular drive has no assigned fuel-consumption/entropy cost here, and none is inferred. In the boundary regime, the optimum over strictly positive angular diffusion is not attained, only approached. Formal independent scientific validation and experimental validation have not been performed.
