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

# Verification notes

The proof in RESULT.md establishes the full parameter-domain claim. `checker.py` separately implements the Möbius flow maps, the critical duration, the positive fixed point and high-precision identities; it compares those formulas with independent numerical integration of each Riccati phase using `scipy.integrate.solve_ivp` and verifies threshold inequalities across multiple positive parameter choices. Run `python checker.py` with Python 3, mpmath and scipy; the local replay passed 802 assertions.

At the explicit \(p=q=L=1\), \(T=0.8\) example, the one-pair threshold is approximately \(0.65088016802300755\), the two-pair threshold is approximately \(0.86576948323965862\), and the two-pair periodic minimum is approximately \(0.08447452679426052\). The favorable average forcing is \((1-0.8)/(1+0.8)>0\), yet one coarse cycle has finite-time loss while two cycles have a positive attracting periodic solution.

Checks are not an infinite-domain numerical certificate. The continuum claims require the displayed Möbius-map fixed-point argument and strict-concavity proof; the quadratic marsh model is not empirically validated, and historical originality remains qualified by incomplete access to some general periodic Riccati literature.
