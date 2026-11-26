---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Equal-coloured leaves agree on atoms and on every diamond formula (false), hence on all terms. Conversely, for a vertex of remaining height d pick a leaf at distance d. With an exact-height test conjoined with the d-fold diamond of this leaf's colour minterm, any matching endpoint is a leaf, is the same leaf by injection, and determines a unique d-th ancestor. At d=h one can omit the exclusion of paths of length h+1, so all singleton formulas have depth at most h, including h=0. A monochromatic path's root and child agree on all formulas through depth h-1 by induction on depth. The count is injections on L labelled leaves times q^(n-L); q=1 works exactly for L=1. The logarithm of the collision product gives the finite positive birthday limit with O(L^3/q^2) error, the upper exponential bound gives the zero limit (including q<L), and the union bound gives the one limit.

## originality

PASS

The supported distinction is reduction of full generation to leaf injection on finite immediate-child outforests, with the resulting shape-free count and uniform depth bound. The general colouring theorem, modal witnesses, comparable catalogue censuses and the classical birthday calculation are not claimed as new.

## value

PASS

This reduces a whole-frame generation problem to a single leaf-injectivity test regardless of internal labels. It supplies a closed census, exact minimal rank and optimal worst-case formula depth for an entire natural class. The birthday law is a useful consequence, rather than a separate novelty claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
