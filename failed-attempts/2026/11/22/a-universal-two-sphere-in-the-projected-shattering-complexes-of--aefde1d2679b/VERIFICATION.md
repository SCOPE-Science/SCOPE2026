---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For one fixed target per selected vertex, a queried four-vertex path is impossible: all-positive forces neighbouring targets to differ, each 1-0-1 triple forces its end targets to coincide, and the resulting alternating targets make 1-0-0-1 impossible. Conversely, in a double star without such a path, target all selected leaves with colour 1; when zero or one hub is marked the hubs can take colours 2 and 3 in the required order. When both are marked, any selected leaves are on one side and the listed four hub pairs leave that hub outside colour 1. This yields the four maximal supports; the sum by number of hubs gives the stated polynomial, and at most one query per vertex makes the maximum support size the VC dimension. The triple intersections A, B, {u}, {v} are nonempty, the fourfold intersection is empty, and the simplicial nerve lemma gives S². Independently, replacing each bank's leaves by one representative is a simplicial retraction onto the four-vertex boundary and is contiguous to the identity after inclusion. Purity and unbounded facet gaps follow from the facet sizes. The proof is for a,b≥1 and exactly three named colours; it does not classify marked targets or arbitrary trees. Replay is algebraic from RESULT.md lines 29–52; the supplied scripts and VERIFICATION.md were inspected as finite corroboration, not executed.

## originality

FAIL

The older finite tree note does not cover all double stars. However, a separate indexed same-day record explicitly classifies every feasible marked query profile on the identical graph and hypothesis class. Its feasibility lemma and exhaustive centre profiles decide existential projection face by face. Consequently the projected support classification, face polynomial, facets, scalar VC dimension and routine tetrahedral nerve are already determined at statement level. This is a coverage finding, not a finding that the same-day record was published first or that the frozen authors copied it; the marked record itself credits an earlier projected result without settling exact public release order.

## value

FAIL

The contrast of nonpurity and fixed homotopy is naturally motivated, and the classification is a useful exposition. Relative to the exact marked-profile coverage, however, the invariant submitted as the distinct contribution is mechanically determined: existentially forget colours, take four obvious maximal sets, and apply the tetrahedral nerve lemma. The record does not establish a surviving distinct exact invariant or nonroutine mathematical remainder. This finding is about the claimed incremental contribution, not the general value of projected complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
