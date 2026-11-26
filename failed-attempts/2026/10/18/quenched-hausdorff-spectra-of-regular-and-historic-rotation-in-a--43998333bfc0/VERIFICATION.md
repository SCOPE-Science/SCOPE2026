---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two lifts have the stated ternary slopes and integer-part rows (0,1,1) and (-1,-1,0), and the difference between lift displacement and the branch-sum is bounded by 1. Each nth full cylinder is a triadic interval of length 3^-n. Exponential counting gives the limsup cover bound for each prescribed endpoint, including extremal rotations by taking t to infinity with the appropriate sign. On the lower side, the endpoint-targeting exponential digit distributions (uniform on the optimizing support at extremal rotations) have the prescribed expected drift and Legendre entropy. For alternating blocks with N_(k+1)/N_k tending to infinity, accumulated discrepancies from every completed block are bounded by a constant times the sum of |e(N_j)| for e(n)=N_+(n)-pn=o(n); this is o(n) because the block endpoints grow at least geometrically eventually. The partial block error is at most a constant times |e(n)|+|e(N_k)|. Independent bounded-variable strong laws therefore give the required liminf and limsup and the minimum entropy lower bound. Vanishing Cesàro jumps fill the cluster interval. The cylinder information estimate yields a uniform mass bound after restricting to a positive-measure subset; an interval of the comparable Euclidean length meets at most three triadic cells, giving Frostman. Countable boundary codings have dimension zero, whereas all asserted spectra are positive for 0<p<1. The supporting finite itinerary checks were inspected, not executed, and do not prove the dimension formula.

## originality

FAIL

The full formula, not only its regular-level specialization, is covered by the weighted Birkhoff spectrum and prescribed-liminf/limsup results of Bárány–Rams–Shi after the known ternary coding and the elementary pressure upper bound. Thus narrowing to nondegenerate intervals would not uncover an original theorem.

## value

FAIL

The dimension question is natural and the direct product-measure proof is a readable illustration, but the frozen contribution is confined to a known three-branch coding and direct application of the existing weighted spectrum and gluing results. The explicit extremal and maximizing values are immediate substitutions in the same pressure; no distinct invariant, hypothesis extension or needed new cutoff survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
