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

# Reproducibility and checks

The standalone `verify.py` checks the original reversal-payoff row difference against the three-state reduction using symbolic expressions, verifies \(F'w=q\), verifies strict positive curvature algebraically, and confirms the two asymptotic endpoint slopes. Its numerical integration with the original physical-time equations uses \((a,b,\theta,\delta,c)=(2,1,2,1/3,\log3)\), conserves the Hamiltonian to the stated tolerances, and reports period ratios for several energy levels. It prints `VERIFY_OK` when all assertions pass.

The limiting period theorem is **not** established by these finite integrations. It is established by the turning-point asymptotics, central-strip bounds and monotone-cap estimates in RESULT.md. All parameters and energy normalization are spelled out there. No external independent audit was carried out.
