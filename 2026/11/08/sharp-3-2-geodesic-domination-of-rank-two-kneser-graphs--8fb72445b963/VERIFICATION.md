---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For all n>=5, KG(n,2) has distance one for disjoint pairs and distance two for intersecting pairs. Reconstructing the selected-geodesic condition rules out all two-set selections; any selected triple with two intersecting ground edges has an outside witness lacking an admissible 2-geodesic. Three pairwise disjoint edges work precisely when only zero or one ground vertex is unused, i.e. n=6,7, with counts 15 and 105. The universal four-set {12,13,23,45} works for every n>=5 by the cases on an outside pair's ground support. The reported lower and upper bounds and extremizer classification follow for arbitrary n, not from finite checking. Independent direct graph-geodesic enumeration for n=5,6,7,8 found respectively 0,15,105,0 dominating triples and checked the four-set at n=5,8. Reviewed exact RESULT.md and verify.py from the pinned Git commit; no all-four-minimizer claim.

## originality

PASS

Best-of-knowledge original within the precise domain and invariant, based on actual relevant mathematical comparisons; source access limitations and priority risks are retained.

## value

PASS

It answers the specific Kneser-graph instance of an explicitly posed (3,2)-geodesic domination problem, establishes a sharp two-order exception, and gives a structural characterization and labelled count of all optimal triples. This is a meaningful natural graph-invariant classification rather than a parameter substitution or textbook deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
