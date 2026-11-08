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

# Verification and scope

The result is proved by exact group-theoretic orbit counting in `RESULT.md`; its quantifiers cover every prime power, without computational inference. The full action on the quadratic and cubic closed-point factors and the singular/nonsingular element cases have been checked against the proof. The separability of the twisted Frobenius equation follows from a nonzero determinant, also in characteristic two. The potential characteristic-three unipotent case is excluded because it has only one geometric fixed point, while the degree-two closed point contains two distinct fixed points.

Run `python3 verify_pentads.py` (stdlib Python). This performs independent explicit orbit and stabilizer enumeration for prime fields 2, 3, 5, 7, 11, and 13, and prints `VERIFY_OK`. Finite runs are not a proof over every finite field; the symbolic group theory is.

Limitations: This counts only the Frobenius degree partition (2)(3), not all reduced binary quintics, Artin–Schreier covers, or automorphism groups of branched curves. Priority against older differently worded finite-geometric classification has not been externally certified. No independent mathematical audit has been performed.
