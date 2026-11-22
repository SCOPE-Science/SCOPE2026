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

# Verification record

The intrinsic Euclidean facet-area computations use three lower coordinate faces of area \((t+2)^2-1/2\), three upper coordinate faces of area \((t+1)^2-1/2\), three pair faces of area \(\sqrt2\,t\), and a regular-hexagonal top face of area \(3\sqrt3\). The volume is independently derived from support-plane heights and the divergence theorem.

The exact symbolic checker confirms the surface and volume polynomials, the cubic derivative factor and its coefficient signs, and rational brackets around the unique positive optimizer. Convex-hull diagnostics at nine nonnegative parameter values agree numerically with the formulas, including the degenerate endpoint. The equal-volume cube comparison follows from \(Q(t)=S(t)^3/V(t)^2\), with cube threshold \(216\). Test command: `python verification/verify.py`; third-party dependencies are listed in `verification/requirements.txt`.

The analytic proof applies to every real \(t\ge0\), while the hull enumerations are finite diagnostics. This record does not assert an independent mathematical audit, independent source-priority certification or an optimizer among arbitrary convex bodies.
