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

All band formulas and coordinate transformations are exact affine identities. The return-time bound uses \(s\le9/8\), \(m_s\le45/64\), \(a_s\ge4/9\), and \(s^2(m_s-a_s)\le1341/4096<4/9\). The limiting density is independently obtained from a two-cell transfer matrix and the Kac mean-return identity. The exact stationary-mean identity reduces the quadratic coefficient to the limiting rescaled first moment.

Run `python verify.py` using Python's standard library; it checks rational parameter instances, itinerary restrictions, the conjugacy, the limiting density equation, and the mean algebra. Finite tests are supplementary and cannot establish the quantified limiting law. The proof also invokes standard uniform expanding-map density stability. It neither asserts numerical experiments prove \(L^1\) convergence nor assesses independent validation.
