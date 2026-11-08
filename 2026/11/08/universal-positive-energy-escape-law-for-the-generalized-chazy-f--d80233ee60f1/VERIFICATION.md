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

The conservation law is checked by direct differentiation on each sign component. In the positive sign component the exact identities are \(w=z+x^qy\), \(\dot w=-x^{q-1}y^2\), \(xw-y^2/2=H\). They imply global continuation. The crucial moving-barrier check is the derivative \(\mp\varepsilon H/x+(q+3/2)(1\pm\varepsilon)^2H^2/x^{2q+3}\), with the appropriate inward signs at large \(x\). A bounded axial derivative forces \(\int^\infty dt/x(t)=\infty\), completing entrance into the strip.

For numerical corroboration, a direct ODE solver checked integer exponents 1, 2, 3, positive energies 1/2 and 2, with stop time 2000. No claim of infinite verification is made. Direct proof, not sampled computations, covers all admissible parameters. A separate independent audit has not been performed.
