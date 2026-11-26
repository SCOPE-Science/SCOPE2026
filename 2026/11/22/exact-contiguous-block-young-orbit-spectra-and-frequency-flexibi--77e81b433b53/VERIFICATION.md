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

A Young orbit is exactly a tuple of block one-counts, equivalent by differencing to the tuple of prefix one-counts. At starting phase x the i-th prefix count is floor(S_i alpha) plus the indicator of x >= 1-frac(S_i alpha) if the latter fraction is nonzero. These sorted half-open intervals give distinct tuples because a coordinate changes upwards at each distinct cut. At irrational slope, equidistribution gives every gap its length, and the positive prefix lengths yield r distinct nonzero cuts. At slope p/q, the phases modulo one form a size-q grid with one point per half-open mesh cell, even for boundary intercepts, giving both the length formula and the count by distinct prefix residues. For simplex density, pick strictly increasing prefix indices successively from dense tails of the irrational orbit, in disjoint neighborhoods of the desired cumulative masses. Entropy is positive because every gap is positive and there are at least two; equality at the maximum would require rational nonzero cuts. The read scripts and recorded outputs give finite corroboration, not the infinite proof. The exact checker uses selected cut sets (not exhaustive at all tested lengths as a script comment suggests); this does not affect the proof or the stated test count.

## originality

PASS

Best-of-knowledge pass on the combined arbitrary-contiguous-partition spectrum and statistical law, not on ordinary rotation coding or the known single-permuted-suffix count. The strongest mathematical and indexed overlap has different coverage: a special family of groups in one case, and a different quotient in the other. The arbitrary block-frequency law and flexibility are not statements of those inspected results.

## value

PASS

Contiguous position blocks are a natural class of subgroups in the prior group-complexity problem. The result gives a complete measured classification for that family, including the rational degeneration and the contrast that for fixed irrational slope the orbit count is locked while its actual probabilities approximate every positive distribution. The structural use is this joint count-versus-measure distinction, not merely applying an entropy inequality or restating equidistribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
