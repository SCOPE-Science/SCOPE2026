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

The complex has as faces exactly edge matchings extendible to a perfect matching after deleting top seam edge T0 from C_n□K2 (n≥3). Every perfect matching using a rung has paired top/bottom horizontal edges, so is an open-ladder matching. For odd n no rungless perfect matching exists and the complex equals L_n≃point. For even n the deleted-top-edge graph has exactly one extra rungless perfect-matching facet F, and its exact simplicial intersection with L_n is Ind(P_{n−1}) via alternating ordered horizontal edges. Open ladder decomposes as a union of two cones with intersection L_{n−2}, so L_{2k}≃S^{k−1}. The attachment inclusion Ind(P_{2k−1})→S^{k−1} is null because the source is contractible or a lower-dimensional sphere (n=4 uses path connectivity), yielding S^{n/2−1}∨Σ Ind(P_{n−1}) and the displayed mod-6 cases. Independently enumerated every perfect matching for n=3..10, confirmed no extra face for odd n and one for even, inspected verify_horizontal_defect.py for reduced mod-two homology tests 3..10 and facet partition 11..14. Finite tests corroborate the analytic all-n decomposition, not prove infinity.

## originality

PASS

The new uniform one-horizontal-edge-deletion integral homotopy decomposition is not implied by known intact prism and open ladder theorems; the distinct n=6 one-edge-fault record is narrower and expressly credits the horizontal family. Best-of-knowledge judgment remains qualified by unavailable full Agarwal–Basak text and any unindexed seam-defect classification.

## value

PASS

Single-edge faults are a natural robustness question for an established family of perfect-matching complexes. The proof explains an unexpected infinite mod-six periodic classification and infinitely many mixed-dimensional sphere wedges, distinguishing a horizontal rim break from vertical-rung breaks. The exact decomposition is structurally reusable, not merely a small finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
