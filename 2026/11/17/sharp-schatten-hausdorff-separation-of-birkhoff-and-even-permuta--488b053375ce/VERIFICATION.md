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

For every n>=4 and odd permutation Q, even vertices P have tr(Q^T P)<=n-2, with equality exactly when Q^T P is one transposition; this extends to the even-permutation convex hull. Because Q-X has zero row/column sums, Schatten duality against Q-J (orthogonal rank n-1 projector) gives dist_Sp(Q,E_n)>=2(n-1)^(1/p-1), including endpoints. The mean of all transpositions is ((n-3)/(n-1))I+2J/(n-1), so Q times that mean lies in the even hull and attains bound with n-1 identical singular values. Every full Birkhoff point is a convex mixture of even/odd vertices, which bounds the Hausdorff maximum by the same distance. The trace-contact transposition matrices have distinct off-diagonal entries, so define an exposed simplex; strict convexity of Schatten p for 1<p<infinity proves unique closest and no additional farthest nonvertex points. Independently enumerated permutation parity and transposition faces for n=4..7, yielding squared Frobenius gaps 4/(n-1), consistent with the formula, with no finite-to-infinite inference.

## originality

PASS

The classical alternating-permutation polytope papers emphasize combinatorial facets and even doubly stochastic membership, while modern Schatten geometry analyzes the full Birkhoff polytope; none of the materially inspected passages states a sharp all-p Hausdorff distance between B_n and the parity subpolytope, its exposed contact simplex, or strict-norm farthest-point rigidity. Best-of-knowledge PASS with explicit priority risk from inaccessible complete 1991/2004 primary papers.

## value

PASS

Deleting half of the vertices of the Birkhoff polytope while measuring precise Schatten geometry is a natural extremal convex-polytope question. Exact norm-by-norm Hausdorff gap, unique 1<p<infinity closest point, and exposed transposition simplex are independently informative, including nuclear norm persistence despite p>1 decay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
