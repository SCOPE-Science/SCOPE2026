---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For fixed finite n with epsilon=1/n and the depth-limit epsilon=0, the exact local expansion at u=1 is -z+(epsilon-2)z²+(epsilon²/3-2epsilon+8/3)z³+O(z⁴), so the second iterate is z-kappa z³+O(z⁴) with kappa=(4/3)(2-epsilon)(5-2epsilon)>0. The two-step contraction and reciprocal-square telescoping yield k(u_k-1)²→kappa^-1 in the original single-step clock. For the infinite-depth f(u)=u exp(2u(1-u)), every orbit enters a compact invariant interval, and a hypothetical prime 2-cycle u<1<v would require s=u+v in (1,2), delta=v-u, delta²=s(2-s), and log(v/u)=(s-1)delta; the strict logarithmic-mean inequality instead gives log(v/u)>2delta/s>(s-1)delta. Coppel's no-2-cycle interval theorem then gives convergence; positive trajectories cannot tend to the repelling boundary zero. Thus all positive initial states converge to one; nonfinite-hits have k^-1/2 coefficient sqrt(3/40). This makes no global finite-depth claim.

## originality

PASS

Best-of-knowledge PASS but with a material primary-text access warning. Hofmann 2026 introduces the exact depth-indexed quotient and limiting quadratic-exponent map, and identifies the first flip, all treated as prior. The accessible source summaries do not provide the explicit fixed-depth critical k^-1/2 constant or a global all-positive critical-limit theorem. The full Hofmann preprint could not be read via available open routes and authorized institutional access reported disconnected, so priority is not certified; this access problem alone does not refute the proved, motivated new consequences.

## value

PASS

A closed depth-dependent physical-iteration critical relaxation constant precisely at the first gradient-descent flip boundary is a natural optimization dynamics invariant. The additional global critical convergence theorem for the nonstandard quadratic-exponent limiting map resolves an actual basin question, not implied by local post-edge bifurcation plots. Its domain and finite-hit exceptions are exact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
