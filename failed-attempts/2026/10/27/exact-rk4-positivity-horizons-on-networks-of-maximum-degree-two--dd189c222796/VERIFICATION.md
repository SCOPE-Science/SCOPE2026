---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently multiplied integer generator powers through order four on P2–P10 and C3–C10 and extracted the coefficient vectors (Q^k)uv/k!. This reproduces all controlling cubics, distance-two quadratics, and distance-three factors, including C6's two geodesics and C7's additional four-edge walk. For unbounded paths, an interior four-vertex path exists already on P6 and its only four-step contribution inserts a stay with total degree weight −8; for cycles of length at least eight, the alternative arc cannot contribute within four steps. These entries remain negative above 1/2; up to 1/2 the convex-Euler identity gives a nonnegative operator. The small cases are exact from the local coefficient lists: diagonal entries are positive by the spectral sum of squares, distance-two quadratic discriminants are negative, and the edge cubics are strictly decreasing with positive values at the relevant distance-three cutoffs. The other cases have an edge-cubic first zero and negative edge entries above it. Structural zeros and disconnected components obey the minimum rule (P1 gives no restriction). This proves the full interval rather than inferring it from the finite comparison. Read frozen VERIFICATION.md and verify.py; its 740 pair comparisons are recorded evidence, not this independent run.

## originality

FAIL

A distinct indexed Resultary record gives the identical classification, not just the same RK method or the same family. Its actual Finding and proof cover the exceptional cutoffs, all roots, permanent negativity above the cutoff, the explanation for C7 and the disconnected component rule. No provenance relationship between the two distinct catalogue records is inferred; substantive coverage is established directly.

## value

FAIL

The precise graph-dependent thresholds would be useful in the absence of the existing result, especially the nonmonotone cycle exception. In this submission every threshold, its sharpness and the C7 mechanism are already present in a distinct exact source. The different verification route and elementary sign certificates do not furnish an independently useful new endpoint, invariant or extension. No genuine surviving remainder warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
