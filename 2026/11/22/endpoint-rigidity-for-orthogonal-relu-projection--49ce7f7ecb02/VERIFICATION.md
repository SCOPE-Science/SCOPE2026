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

The four proof steps in `RESULT.md` provide the complete analytic certificate. Every strict sign mask is realizable by an input to the invertible orthogonal transform. Its Jacobian is a coordinate-subspace orthogonal projector, whose maximum-row-sum norm is exactly the chamber sensitivity. Testing singleton and complementary masks forces flat row supports of size at most two; orthogonality then fixes the blocks. Conversely every permissible block projector has norm at most one.

The separately embedded `checker.py` can be executed with `python checker.py` in a Python environment with NumPy. It checks every mask for block constructions through dimension eight and for 540 random orthogonal matrices up to dimension seven, including the exact rational form of the three-coordinate complementary projector. These finite checks supplement, rather than replace, the universal analytic proof. No claim about a global exact constant for expansive cases, rectangular matrices, or general multi-layer networks is tested or made.
