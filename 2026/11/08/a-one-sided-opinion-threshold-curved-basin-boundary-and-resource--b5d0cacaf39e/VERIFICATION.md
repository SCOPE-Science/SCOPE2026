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

The accompanying `verify.py` rederives the exact rational Hawk–Dove payoffs and opinion-flux polynomial. It checks the degree-\((2,2)\) Bernstein certificate of \(1+h\ge0\), the upper clipping bound via \(h(x,1)\), the nullcline identity, the boundary signs, the saddle Jacobian, and the exact \(44/103\) stable-graph coefficient. Run `python verify.py` with Python 3, `sympy`, and `scipy`; successful output ends in `VERIFY_OK`.

The theorem's global assertion relies on the analytic planar-index/Poincaré–Bendixson argument, not on the numerical samples. The stable-graph calculation uses the negative-flux branch and checks the resulting sign locally. The environmental limit is obtained from a conserved logit balance, with absolute convergence only in the low-opinion regime. Example simulations test trajectories at and on either side of the one-way opinion threshold but cannot exhaust all initials or prove absence of other recurrent sets.

Scientific boundaries: the exact parameter instance and interior initial values only; the separating stable manifold is not globally expressed in elementary functions; the limiting environmental value is a convergent integral functional of the trajectory. No outside independent validation is asserted.
