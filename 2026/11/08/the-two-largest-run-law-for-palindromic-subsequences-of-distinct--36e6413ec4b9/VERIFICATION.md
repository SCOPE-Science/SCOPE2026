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

For an expanded common-subsequence alignment, normalize the match count in each same-letter block pair by the length of that letter's run. The resulting matrix has row and column sums at most one and no crossing positive pairs. The bipartite matching polytope on its support is integral: any fractional vertex would admit opposite alternating perturbations along a cycle of fractional edges, or along a path between fractional-degree-one vertices, which have slack. Integral matchings on this support are increasing. Thus the expanded optimum is bounded by the maximum weighted skeleton matching, and at equality all matchings in a convex decomposition are optimal. Greedily embedding the skeleton in the increasing and decreasing period powers uses one new copy per weak descent and weak ascent respectively. For skeleton length m and e adjacent ties this yields m+e<=2k-1, and each letter appears at most k times. These give the stated weighted bound including A=B, and an alternating two-letter skeleton with lengths A and B realizes it as a palindrome. When A>B, equality forces m=2k-1, e=0, all k top-letter blocks and one B-letter in each gap in every integral optimum. Averaging forces all top blocks to be fully selected and each expanded gap to have B letters chosen only from B-blocks. The actual palindromic gaps are reverse partners in the same distinct-run order, and hence must each be monochromatic, including a central gap. Conversely each mirror-paired choice embeds. The k-1 gaps have floor(k/2) reversal orbits, including none at k=1. Deletions follow by subtraction. The bounded DP and optimizer-enumeration code was inspected but not executed; the proof, not the finite profiles, supports the universal statement.

## originality

PASS

The arbitrary-run law and complete unique-top optimizer classification are distinct from the inspected unit-weight spectra, generic LCS algorithms and other periodic objectives. The unit-run result and length/deletion equivalence are not separate contributions.

## value

PASS

For a natural unbounded class of periodic strings, the invariant collapses to two order statistics despite arbitrary weights, alphabet size and cyclic order. The exact deleted length and the complete optimizer structure with a unique maximum are useful beyond generic instance-by-instance dynamic programming. No tied-maximum optimizer count or general run-repeat theorem is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
