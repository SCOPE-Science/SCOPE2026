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

# Verification and limits

Run `python check_star.py` using SymPy and SciPy. The standalone program checks the exact Volterra-entropy dissipation, conserved initial ratio, full three-species Jacobian characteristic polynomial, and the rational invariant-ratio boundary. Three finite integrations test one node-selected trajectory, one focus-selected trajectory and one critical spectral case; those trajectories end near the predicted equilibrium compositions. The finite critical numerical frequency is a roundoff artifact, not a positive predicted frequency.

The infinite-time convergence is established by a proper Lyapunov function plus LaSalle invariance and a unique leaf intersection. The focus-level crossing frequency uses asymptotic polar angular dynamics; the distinct-node finite-crossing property uses the stable-node asymptotic-direction theorem and analytic isolation of finite-time zeros. These global and infinite-time conclusions cannot be certified by finite integrations. There is no claim of independent audit or exhaustive historical-priority certification.
