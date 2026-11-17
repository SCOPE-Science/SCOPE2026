---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Proof reconstructed from frozen RESULT.md: for r!=s the shorter source is an actual contiguous factor of the longer. In equal powers, U and V are contiguous overlaps in both; a common subsequence not embedding in U must use initial A of X and final A of Y, so it embeds in X with final B removed, namely V. Multiplicity of letters in each disjoint alphabet proves U and V incomparable. Exact lengths and all-positive-integer boundaries follow. Independently implemented scattered subsequence generation and one-character insertion maximality for 108 small disjoint-block/r/s cases, all matching. Tests are diagnostic; proof is general.

## originality

PASS

Best-of-knowledge new exact structural language classification, in contrast to general MCS DAG algorithms or reversed permutation-block results; searches and materially read theorems did not imply it. No global novelty guarantee.

## value

PASS

Maximal common subsequences differ materially from longest ones. This natural periodic-string family has a complete two-generator downward-language description and unbounded exact maximal-versus-longest gap; it is a useful algorithmic benchmark, not merely a filename or parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
