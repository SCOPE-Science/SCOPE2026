---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The compact-range Weyl coefficient, trace limits, bounded critical essential norm and unbounded regime are correct. Normalized monomial integration gives both squared norms in RESULT.md, and the shift by a is injective; the weighted orthogonal images give the displayed diagonal weights. The square-root factors from each coordinate converge uniformly after scaling (sqrt(x+l/n) converges uniformly to sqrt(x)); gamma ratios then give uniform degree control, including coordinate faces. Scaled lattice counts squeeze to the bounded radial region whose volume is the Dirichlet integral with simplex-coordinate Jacobian r^(d-1). For d=1 the angular region is a point; for d=2, alpha=0, a=(1,1) the formula reduces to 1/15. Counting-function inversion and uniform tail comparison with zeta(p/rho) prove the ordered law and the displayed real-axis residue; the latter is not itself a proof of meromorphic continuation. At alpha=1 the tail supremum of the weights yields the essential norm; at alpha>1 a fixed positive angular proportion on the support of a yields divergent weights. However, the unqualified complete singular-value multiset and nonincreasing-arrangement assertions (RESULT.md lines 8, 35, 43) fail at the noncompact endpoint under their stated convention. For d=1, alpha=1, b=z^2, the squared diagonal weights are 2(n+1)/(n+2), strictly increasing to 2 without a largest entry. They cannot be arranged in nonincreasing order, and if singular values are interpreted as approximation numbers, all are sqrt(2), since the essential norm and operator norm coincide. The formula is valid there as an unordered list of diagonal weights, not as the claimed ordered singular multiset, and for alpha>1 one should likewise speak of weights of the polynomial-defined operator rather than bounded-operator singular values. Replay: RESULT.md Steps 1–4 and this one-dimensional substitution; the frozen finite gamma checker was read, not run. No repaired finding is claimed.

## originality

FAIL

Verified broader generalized Toeplitz Weyl theory gives the exact compact coefficient via a direct Hardy-space reduction, not merely a rate or ideal criterion. The log-trace and real zeta residue are immediate consequences of that law, and at the boundary the exact norm is the usual multiplication-operator essential norm modulo a compact radial factor. The known boundedness and Schatten criteria are not the basis of this rejection, and inaccessible near-source papers are not used as negative evidence.

## value

FAIL

A sharp angular Weyl coefficient is a natural invariant, but here it is a direct symbol-volume evaluation of an existing law; its log sums and real zeta residue do not supply a new invariant beyond that evaluation. The endpoint adds a standard multiplier norm and weighted AM–GM. The elementary explicit monomial weights provide an illustration, but no scientifically valuable unknown exact remainder is demonstrated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
