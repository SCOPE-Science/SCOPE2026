---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Complete-pair Gini of a real vector is exactly reducible to binary cuts for a constant-preserving linear Markov operator. Under K_{m,m} half-lazy transition, a cut with r sites in the first part, s in the second, k=r+s and d=|r-s| has exact output Gini mk-r²-s²+d[rs+(m-r)(m-s)]/(2m), obtained by counting within- and between-class output levels. The normalized expression R=1/2+d[m²+(m-k)²-2md-d²]/[4mk(2m-k)] is maximized by a singleton (or complement), using complement symmetry, d<=k, d>=1 and convex endpoint comparison in t=m-k, yielding 3(m-1)/[2(2m-1)]. At m=1 the walk is uniform averaging and norm zero. Strict equality in the cuts plus nesting of level sets proves only one-exception-coordinate real extremizers for m>=3, and rational comparison proves monotone rise to unattained 3/4.

## originality

PASS

The related exact lazy biclique edge-variation theorem concerns cross-part graph edges, not all vertex pairs. Continuous-time normalized heat on K_{a,b} has a different spectral family and does not determine this discrete half-lazy one-step coefficient/equality classification. No checked primary or published record implies the exact claimed global constant.

## value

PASS

The natural balanced complete-bipartite lazy walk has a fully classified sharp all-pairs dispersion contraction and singleton equality mechanism, with exact finite-size-to-thermodynamic 3/4 gap; useful in stochastic smoothing versus other norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
