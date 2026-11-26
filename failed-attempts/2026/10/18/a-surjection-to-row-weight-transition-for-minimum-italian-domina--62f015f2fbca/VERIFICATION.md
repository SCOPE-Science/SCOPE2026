---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At a zero cell, the open-neighborhood weight is exactly its row sum plus column sum. An empty column forces every row sum at least two; without an empty column the total is at least n. Both candidate weights are attainable: put one 1 per column covering every row, or put one 2 per row. For n<2m equality excludes empty columns and forces every column sum to be 1, with each row occupied. For n>2m equality forces an empty column and then every row sum must be 2. At n=2m the same alternatives are exhaustive and the two feasible families can coexist. Column assignments onto the m named rows count m! S(n,m); independent rows of weight two give (n+binom(n,2))^m. The boundary overlap assigns labeled columns in pairs to the named rows, giving (2m)!/(2!)^m. Independent adjacency enumeration gave no lower-weight examples at 2x4 or 3x6 and respectively counted (U,B,overlap,union)=(14,100,6,108) and (540,9261,90,9711). The frozen checker and recorded 19-profile output were inspected, not executed; the finite checks do not replace the equality proof.

## originality

FAIL

Two verified overlaps matter. Alizadeh et al., Theorem 3.4, already give the exact ordinary scalar formula for all rectangles, not just squares. More decisively, a distinct indexed Resultary record with the same displayed date states the identical labeled optimization problem and every optimizer family and count, including the boundary intersection, on the superset 1<=m<=n. This is demonstrated equivalent coverage of the entire mathematical contribution, not a title match or a comparison to perfect Italian domination. No distinct remainder within the frozen claim is established. The same displayed date and metadata do not establish who was first; this is a failure to substantiate distinct originality, not a finding of copying or a rejection based on an inaccessible paper. No repair is supported by narrowing the claim within the covered domain.

## value

PASS

As mathematics, the complete equality classification and labeled enumeration across the natural n=2m boundary give more useful information than the scalar minimum, including the first nonzero coefficient of the weight polynomial and the exact double-count correction. This evaluates the theorem's content, not its novelty: the separate exact coverage bars credit for an original contribution from this frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
