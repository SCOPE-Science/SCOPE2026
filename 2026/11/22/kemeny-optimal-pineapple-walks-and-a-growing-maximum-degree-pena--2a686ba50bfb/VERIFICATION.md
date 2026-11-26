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

Symmetry fixes uniform stationary mass but leaves the edge probabilities adjustable. For connected support, L+Q is positive definite with Q the stationary projection. The trace of its inverse has strictly positive second directional derivative on every nonzero symmetric direction (write it in an eigenbasis, where it is a sum of positive multiples of squared entries). The feasible connected class is convex; its compact closure and divergence of the inverse trace at a disconnected support give existence and strict convexity gives uniqueness. Averaging or uniqueness under permutations then justifies the orbit reduction even for arbitrary competitors. In addition to the leaf and ordinary-clique contrasts, use the block-constant Laplacian on the ordinary clique, gateway and leaves. Its diagonal entries are a,(n-1)a+rb,b; the sum of its principal two-minors is Nab, so its two nonzero eigenvalues contribute ((r+1)b+na)/(Nab). Adding the contrast inverses gives precisely the three-term formula. At fixed a it strictly decreases in b and c, so saturating the two independent row bounds is valid. The reduced objective is strictly convex with endpoint barriers; its derivative gives the stated equation and the root forces all allowed nonloop weights positive, no holds except at leaves, and positive holds even for r=1. For fixed r, the third term differs from n-3 by O(1/n) uniformly in z since (n-2)^2=(n-1)(n-3)+1; the other two positive terms keep minimizers away from the endpoints. Compact uniform convergence therefore gives the stated z-limit, b-limit and additive asymptotic cost. Substituting equal maximum-degree weights produces the stated finite benchmark and fixed-r ratio. The bounded independent `python3 -B /workspace/review_evidence/kemeny_checks.py` probe compared 36 exact rational inverse traces including connected examples with c=0; the frozen script was inspected, not executed. No joint-growth limit is inferred.

## originality

PASS

The supported distinct claim is exact one-gateway Kemeny optimization with unrestricted symmetric competitors, including support, holds and the fixed-r benchmark limit. Generic fixed-stationary design, the maximum-degree walk, and SLEM solutions of the same graph are antecedents. A same-day corona result even shares a limiting leaf probability on clique cores, so that limit alone is not the distinction; its assignment is to every core vertex and its cost and penalty are different.

## value

PASS

A one-vertex cut concentrates competing demands for transition mass at a single row. The exact classification establishes how that bottleneck should be weighted and which permitted edges can be dropped (none at the optimum), not simply that an SDP could solve the problem. The fixed-r clique limit isolates an arbitrarily large penalty across the family for the standard maximum-degree heuristic, even though each n-limit keeps r fixed. This is informative for comparing designs on networks with a large tightly connected core and a localized peripheral star.

The dated certificate retains the supplied scientific assessment, sources and limitations.
