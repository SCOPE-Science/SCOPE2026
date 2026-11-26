---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For a shortest run, its letter occupies precisely one cyclic interval of length m≤p/2. At its first position only shifts 1,…,m−1 can match; at its last only shifts p−m+1,…,p−1 can match. These disjoint ranges force the sorted proper shifts to be u and p−d with 1≤u,d<m, and exclude all proper shifts immediately when m=1. On that run their return traces on offsets are respectively the prefix [0,m−1−u] and suffix [d,m−1]. The cover is exact iff u+d≤m. On any run of length L≥m the same two directions suffice: if t+u≥L, then t−d≥L−u−d≥0. The condition implies u<p−d, and summing m−u over u=1,…,m−1 gives m(m−1)/2. Periodicity gives the residue corollary; the first/last-position obstruction also excludes any equal nonzero residue and proves primitivity. The recorded 19,525-profile run is correctly described and direct from the script, but was not independently rerun and is not the unbounded proof.

## originality

PASS

Known existential-shift pseudoperiodicity and the technique of testing run boundaries are prior. The bounded comparisons did not locate the full proper residue-pair classification and count for these periodic words.

## value

PASS

This is a complete invariant of a natural family for the smallest nontrivial number of shifts. It identifies an unexpectedly sufficient statistic—the shortest run, not the whole period profile—and gives all admissible pairs, count and nonexistence threshold, rather than a yes/no test of individual words. This is useful as an exact baseline for more general periodic-word classifications, despite the short proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
