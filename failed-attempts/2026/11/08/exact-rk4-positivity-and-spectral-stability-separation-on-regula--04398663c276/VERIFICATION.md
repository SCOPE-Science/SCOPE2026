---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The graph is finite connected unweighted d-regular bipartite, endpoint classical RK4, with an explicitly bounded weighted regular extension. Writing q=dh, P=A/d, the Taylor coefficients of f(q(I-P)) are nonnegative for 0<=q<=1. Every noncomplete connected bipartite graph has a distance-three opposite-class nonedge, giving exact transition (q³/6)(1-q)(P³)_{uv}, permanently negative when q>1. Complete K_{d,d} spectral projectors give cross-class (1-f(2q))/(2d) and positive diagonal/same-part entries, hence cutoff q=1.3926467817..., which also equals the stability endpoint since L has maximum eigenvalue 2d. Verified C6 distance-three at h=3/5 exactly -9/625, with 2h=6/5<ρ; algebraic signs and extension normalization are consistent. The finite example is only corroborative.

## originality

FAIL

Prior Oct26 biregular theorem encompasses every unweighted d-regular bipartite case exactly; earlier weighted Taylor walk-gap theorem covers the submitted weighted noncomplete corollary. Originality fails for the entire stated final claim, including its sharp thresholds and negativity witness.

## value

FAIL

A correct but strictly weaker restatement of a published all-biregular sharp theorem and its previously covered weighted walk-gap corollary is not a separate useful mathematical invariant. The C6 example illustrates known general phenomenon and cannot supply independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
