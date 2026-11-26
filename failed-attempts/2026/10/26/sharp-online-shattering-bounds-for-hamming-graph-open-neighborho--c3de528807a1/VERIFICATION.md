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

After a first positive query v, a distinct second positive query w leaves q−2 centers on one coordinate line at distance one, exactly two intermediate centers at distance two, and none beyond that. On a coordinate line a query on the line excludes at most one center; a query off the line includes at most one. Thus every genuine second split has a branch of Littlestone dimension ≤1, the first-positive space has dimension ≤2, and the full dimension is ≤3. In dimension one a negative answer identifies the center; H(2,2) has only two distinct concepts, and in H(3,2) the first-positive space has only three centers and hence cannot realize depth two. The independent replay `python3 /workspace/review-evidence/independent_finite_checks.py 5` verified every frozen certificate path under distance-one labels, giving depths 3,3,2 in H(2,3), H(4,2), H(3,2), respectively. Fixing extra coordinates and restricting symbols preserves all these labels, giving the lower bounds for larger graphs. Independently, no triple in H(2,3) can be VC-shattered: a distance-one pair has only one common neighbor, and a triple of pairwise distance-two points can be relabeled as the diagonal, which has no common neighbor. Two points are shattered. Standard version-space prediction and the shattered-tree adversary identify the dimension with the deterministic realizable mistake bound.

## originality

FAIL

A distinct Resultary record gives the exact all-parameter formula on the identical query domain and open-neighborhood class, with the H(2,3) adaptive/static separation, and additionally addresses induced subgraphs and the uniqueness of the full-graph gap. A second distinct record gives the open table in a broader mixed-alphabet theorem. The asserted mistake bound is an immediate translation of the Littlestone formula, not a surviving independent claim. This is a finding of verified exact coverage, not a conclusion about who obtained or published the theorem first; the catalog-path dates do not settle priority.

## value

FAIL

The dimension and VC gap are useful facts about an elementary learning class, but the record supplies no additional invariant, parameter regime, stronger bound, or distinct technical ingredient beyond the verified overlapping proof and results. The implementation and particular leaf choices are corroboration, not an independent mathematical advance. There is no separately valuable narrower remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
