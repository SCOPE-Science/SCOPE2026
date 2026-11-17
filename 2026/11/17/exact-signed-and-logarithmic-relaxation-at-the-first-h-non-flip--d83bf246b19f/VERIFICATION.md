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

The mathematical certificate is the exact polynomial coordinate change, center-graph invariance through fourth order, the resulting fifth-order one-step normal form, and the summable-remainder reciprocal-square proof in RESULT.md.

Run `python verify.py` with Python 3 and SymPy. The script performs exact symbolic checks and independently iterates representative Hénon trajectories. All finite numerical checks are diagnostics, not proof of an infinite-time limit. The constants in the leading asymptotic are derived algebraically; the orbit-dependent additive constant exists by an absolutely summable difference estimate, not by extrapolation from samples.

The proof relies on the standard local center-manifold and stable-foliation tracking theorem for a planar smooth map with one simple unit-modulus multiplier and one multiplier strictly inside the unit circle. It does not assert global attraction or any conclusion at the endpoint \(b=1\).
