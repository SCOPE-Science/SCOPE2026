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

For m≥3 two vertices in one clique fiber have a third common neighbor. In neighboring fibers a mixed-label pair has a common Cartesian corner; a same-label pair does not. In fibers two steps apart the shared neighborhood is through an intervening fiber and requires matching labels. For n≥5 these cases exhaust common neighbors and give the exact cyclic-word characterization. No three successive fibers can be occupied, hence 3|S|≤2n. The directed two-symbol-state transfer uses exactly the allowed triples; its indexed closed walks correspond one-to-one to indexed packing words, with deficit 2n−3|S|. Splitting the color vector into constant and zero-sum parts, the off-diagonal color adjacency J−I acts by a and −1 respectively. The constant block has determinant (1−q²x)(1−a qx²−ax³)−m q³x³−m q²x⁴, which simplifies to the first factor of D_m; the zero-sum block gives 1+qx²+x³ with multiplicity a. The formal trace/logarithm identity then counts every size. Expanding through q² gives the three displayed coefficients at the least allowable deficits 0,1,2; each is positive for the stated k and a≥2, so the upper bound is sharp and the coefficients count precisely the maxima. An independently written subset- and series-check agreed in all sizes in three direct graph instances and with cyclic-word histograms for m=3, 5≤n≤12 and m=4, 5≤n≤10. Replay: python3 /workspace/branches/4b5697de-7e6a-4162-9e72-689c83c22fb0/independent_recheck_record3.py. These are finite corroboration. The frozen programs and logs were inspected, not executed.

## originality

PASS

Credit the known scalar maximum, the component-coloring construction, and the path transfer. The supported distinct contribution is the labeled cyclic all-cardinality determinant with its additional color factor and the resulting maximum census for every m≥3, n≥5. The strongest path and K₂-cycle comparisons do not supply that count.

## value

PASS

For a standard product graph, the labeled optimum multiplicity and all-cardinality distribution refine the known optimum size in a way that distinguishes cyclic closure and the clique color count. Resolving the color-sensitive cyclic spectrum yields both exact polynomials and short residue-specific counts, a reusable enumeration rather than a recomputation of the scalar packing bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
