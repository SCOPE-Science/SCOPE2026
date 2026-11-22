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

# Reproducibility

Run `python3 verify.py` for the direct labelled three-point diagram enumeration compared against an independent matching-and-assignment construction. Run `python3 verify_general.py` to reproduce the enumerated small-arity packing polynomials and finite-extension counts. Their full actual output is saved in `verification_output.txt`.

`verify.py` checks the direct triple-subset enumeration through three old vertices and the exact matching construction through six old vertices. `verify_general.py` checks packing-polynomial coefficients through six new vertices and finite-extension counts for selected pairs of old/new sizes. These are finite examples only; the all-arity asymptotic statement is established by the involution factorial-moment and collision-negligibility argument in `RESULT.md`. No independent mathematical audit or external proof certification was performed.
