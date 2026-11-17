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

The proof identifies all irredundant facets using the standard bipartite matching formulation. All purported ridge pairs are witnessed by points satisfying exactly two facet equalities; all excluded pairs force an additional linearly independent facet equality. Normal products are calculated in the unscaled Frobenius inner product. The mean-angle sign and balanced asymptotic follow from the exact angle count.

To reproduce the additional finite exact checks, run `python3 geometry_checker.py` in the directory containing the standalone artifact. The checker requires only the Python standard library. It enumerates every \(0\)-\(1\) partial matching vertex for eight parameter pairs, forms all pairwise facet intersections, and computes modular face ranks, signed normal products and squared cosine values. Its expected concluding line is `MATCHING_RIDGE_EXACT_PASS cases=8`.

Modular ranks are sufficient for positive independence certificates on tested faces but are not themselves a substitute for the all-dimensional witness/obstruction proof. This verification does not assess independently conducted mathematical auditing or comprehensive priority.
