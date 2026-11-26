---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Use the left plot point as anchor and keep h,k positive fixed integers with signed vertical gap. Prescribing an injective assignment on v positions has probability 1/(n)_v. For any fixed ordered factorial-moment tuple with graph type (v,c), horizontal constraints leave at most one free base index per component, and consistent signed vertical constraints leave at most one free base value. Thus the total contribution is O(n^(2c−v)). For mixed counts take disjoint rectangles within each mark; a duplicated horizontal edge would have conflicting gaps or would be the same event, excluded by disjointness or the falling factorial. Any nonmatching contributing type has v>=2c+1 and vanishes. For t vertex-disjoint edges the anchor grid contributes n^(2t) times the product of region areas, up to o(n^(2t)); fixed boundary shifts and each forbidden endpoint-index or endpoint-value equality cost O(n^(2t−1)). Dividing by (n)_(2t) gives independent Poisson rectangle factorial moments. All orders are controlled by the same calculation; higher bounded moments justify identification of subsequential count laws. Tightness of counts and compactness of the square give tightness of point measures, and rectangle counts determine the limiting processes. General boundary-null marked regions follow by continuity, not by asserting independence of overlapping counts of the same mark. The integer triangle/square union gives the asserted joint void exponent (e.g. d=3,r=2 gives −12). For the conditional shell statement, voidness of smaller shells and nonemptiness of shell m has positive limiting probability; if the latter count is positive, dividing the shell integral of a bounded continuous test by that count implements uniform tie selection. In the limit the equal-intensity independent clouds yield an independent uniform pooled mark and anchor. Inspected the supplied exact enumerator and verification note without executing the uploaded script. It checks finite counts and some second moments, not the process limit. No growing-mark, growing-threshold or quantitative assertion is supported.

## originality

PASS

Pass for the joint planar fields for arbitrary fixed signed numerical offsets and the resulting nonredundant geometric and conditional location laws. The aggregate Manhattan close-pair limit, Manhattan minimum marginal, the Chebyshev r=1 marginal, and the succession index law are covered and receive no novelty credit.

## value

PASS

Fixed signed displacements measure local collisions in a natural spatial matching model. The joint marked law captures anisotropy and localization that are invisible in the aggregate close-pair count, provides joint calibration for distinct geometric norms, and identifies the conditional distribution when a nearest pair is sampled uniformly. The complete finite-mark theorem is more than a fresh scalar count or a reinterpretation of the known Manhattan marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
