---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

All connected nonempty allocations on a star have one hub bundle with exactly r=k-n+1 chosen leaves and n-1 singleton leaf bundles. For a neighboring singleton j, its exact connected two-way share is max over isolating one leaf i of min(w_i,H+w_j-w_i). A strict improvement exists exactly when selected i and outside j satisfy w_i>w_j and H>w_i. This yields sorted-leaf choices or h=0 and at most one positive selected leaf. Counting tie classes gives Q_r; labels give n!Q_r. Any violating inversion permits a leximin-improving swap. Fair allocations share an identical sorted utility vector, establishing the converse, including r=0, r=k, zero weights and ties. Independently reconstructed 6,012 exact finite (k,weight,hub,r) settings, checking direct pair shares, leximin and Q_r.

## originality

PASS

Published Hummel–Igarashi Theorem 6.1 gives leximin => local PMMS under common utility, but not PMMS => leximin or the star-specific complete tie-and-zero classification. The other fully inspected Resultary star census concerns ordinary EF1, a different criterion, and does not imply this PMMS all-allocation count. Prior existence and algorithms are explicitly excluded from novelty. Priority remains qualified.

## value

PASS

Star-connected allocations are a canonical solvable boundary for graph-constrained fair division. The exact PMMS class, tie-sensitive probability Q_r/binom(k,r), equivalence with leximin, and discontinuous zero-center transition supply useful structure beyond a routine existence corollary. The precise fair-allocation count is a natural invariant, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
