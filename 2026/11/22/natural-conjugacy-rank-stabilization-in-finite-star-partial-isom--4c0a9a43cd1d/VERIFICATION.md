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

Each of the two conjugation identities gives a rank inequality, hence the ranks agree. In b=g⁻¹ag the map g sends dom b into dom a and im b into im a and intertwines their arrows. By equal ranks both images are onto, so g restricts to an isometry of the spans. Conversely such a span isometry, on just that domain, satisfies both identities. In a star, a metric span involving the hub and at least two leaves has a distinguished hub and cannot be isometric to a leaf span; on a two-point span the hub–leaf and leaf–leaf metrics differ. A singleton span is the sole fusion of the ordinary leaf and hub-fixed types. A rank-two hub mover must use the hub on both the domain and image sides, yielding either a transposition or a leaf→hub→leaf path. At higher rank the two stars in the domain and image force the hub to be fixed. At rank one the two directions of the hub–leaf arrow are span-isometric. Thus all three hub-moving classes and sizes follow. The labeled cycle/path counts divide by cycle rotations and repeated components, not path reversals. Removing the empty hub-fixed copy subtracts z, which the rank-one hub mover restores, leaving +2z². At z=1 the formal convolution telescopes to p₂(m), and at rank r the unique leaf profile of support 2r consists of r disjoint arrows; hub-fixed profiles use at most 2r−2 leaves. For r=1 the one-leaf monoid has two rank-one classes (identity singleton and single arrow), versus three at two leaves, so the boundary comparison includes r=1. The independent direct equation census (`python3 -B /workspace/review-evidence/star_direct.py`) matches all rank/class-size multisets for m=1,2,3,4, with 7,22,83,442 elements respectively. Those checks corroborate but do not replace the uniform argument.

## originality

PASS

The star element decomposition, the ambient finite inverse-monoid cycle/chain classes, and the two-partition convolution are prior. The inspected sources do not classify the metric-restricted conjugators or give the full star class-rank and class-size distribution or the sharp stabilization. The prior decomposition is important input but contains no conclusion that all the necessary within-family span maps or between-family mergers are allowed.

## value

PASS

Domain-rank class counts and class sizes are natural intrinsic invariants for the star inverse monoids. The formula separates the inherited cycle/path combinatorics from every geometric exception and resolves exactly, rather than asymptotically, which number of leaves first realizes the stable set of classes. This complete classification with all sizes and a sharp uniform threshold is useful beyond a restatement of the monoid order or an ambient partition count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
