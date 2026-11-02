---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

On xi<0, setting phi=1−exp(c xi) gives exact polynomial residual −(exp(c xi)−1)(2c²−kc−1)exp(c xi); choosing c=(k+sqrt(k²+8))/4 makes residual zero. On xi>=0 all terms vanish; phi continuous and phi phi′→0 at the interface, so no distributional Dirac mass. c>0 for every real k. Independent SymPy factorization confirmed this substitution and zero interface-flux limit. Correct existence but no stability/uniqueness/minimality is claimed.

## originality

FAIL

Decisive prior coverage: Gilding & Kersner (2005), Theorem 1(a), already gives the exact sharp-front profile and speed for the more general equation u_t+b u^κ u_x=(a u^κ u_x)_x+c u(1−u^κ), including all real convection b; substituting κ=1, a=c=1 and b=k yields precisely the submitted PDE, speed (k+sqrt(k²+8))/4, and profile max{1−exp(c xi),0}. This is not merely a similar equation or uninspected abstract: the full primary 2005 paper was materially read (Theorem 1(a), its normalization and boundary). An earlier 2004 Gilding–Kersner monograph also treats explicit diffusion-convection-reaction waves. The complete claim is an immediate specialization of a prior theorem.

## value

FAIL

The precise explicit sharp wave, speed and weak interface are direct algebraic specializations of the 2005 general theorem; an elementary rederivation of known closed form has no independently motivated new mathematical content. Correctness and a new verification do not rescue the covered original; no repaired narrower original valuable claim was supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
