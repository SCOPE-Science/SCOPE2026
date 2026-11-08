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

Run `python verify.py` in an environment with the single dependency in `requirements.txt` installed. The script checks exact fifth-order Padé matching; the cubic pole isolating interval and positive derivative; the polynomial-remainder residue domination identity; the exact pole-distance equality; exact three-state rational entries and their sign windows; and a finite pure-birth counterexample at timestep two obtained independently through Taylor-coefficient recurrence and rational matrix inversion.

The observed result was:

```text
VERIFY_OK 22 first_negative_coefficient_at_h2 11 negative_entry -5772440991/3213750657762304
```

These tests verify specified finite algebraic identities and examples. The unrestricted-generator universal quantifiers, and the existence of a finite violating dimension for **every** supercritical timestep, are justified by the mathematical proof in `RESULT.md`, not by finite enumeration or runtime logs. The complete claim has not received independent external mathematical validation.
