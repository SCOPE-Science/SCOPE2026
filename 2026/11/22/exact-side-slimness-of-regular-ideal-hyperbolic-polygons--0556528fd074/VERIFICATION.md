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

# Verification steps and limits

The included `verify.py` evaluates the exact Poincaré-disk geodesic-line distance from the midpoint of a reference ideal regular polygon side to each other side; compares all values against the predicted analytic expressions; and scans 401 points per side in eleven polygon orders. The command `python3 verify.py` completed with `PASS`. This is a finite floating-point diagnostic, not a certificate of the all-integer theorem. The unrestricted proof is in `RESULT.md`, including the Lorentz-normal formula, nearest-side comparison, unique midpoint maximum and asymptotic. No independent audit has been performed.
