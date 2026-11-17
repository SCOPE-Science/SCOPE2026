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

# Verification record

Run `python verify.py` with ordinary Python 3. It enumerates every Dyck word for semilengths 1 through 10, compares Narayana peak means, Catalan-convolution hill means, each vertical-facet adjacency count, the total cover-adjacency count and its horizontal/vertical split, and prints `GRID_SURFACE_EXACT_PASS paths 23713 gram_faces 414` on success.

To verify Euclidean normalization independently of a counting formula, semilengths 1 through 5 are checked by constructing all order-simplex vertex coordinate vectors, deleting the vertex opposite each actual boundary face, and evaluating the rational Gram determinants. All 414 tested boundary faces have the expected determinants 1 for coordinate facets or 2 for cover-equality facets.

These are finite checks, not an exhaustive verification in every dimension. The proof for every dimension is the analytic argument in RESULT.md: canonical simplex-face metric measure, Narayana symmetry, Catalan convolution, and Catalan asymptotic estimates. The source comparisons are documented in AUDIT.json and REVIEW.md. No independent mathematical audit was performed.
