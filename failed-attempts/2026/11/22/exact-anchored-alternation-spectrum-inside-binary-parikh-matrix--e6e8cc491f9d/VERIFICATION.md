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

Reconstructed RESULT.md lines 51–69. Each b is labeled by its number i of preceding a's; these labels are weakly increasing and their multiplicities uniquely specify the word. Their sum is C. A set of occupied interior gaps uniquely determines the maximum possible number of alternating b selections: each gap supplies at most one, and taking one from each leaves an a on either end and between consecutive choices. Independent gap multiplicities yield (1), and setting z=1 gives [u^(B-j)](1-u)^(-j-2) times binomial(A-1,j), including B<j, A=1 and C=0. In the stable regime C<A, B>=C, the positive labels give unrestricted partitions, so J is their number of distinct sizes. The minimum area for j sizes is triangular, and any excess may be added to the largest distinct part. For fixed r>=2 the avoidance numerator lies between 1 and a polynomial in C; Hardy–Ramanujan then gives the logarithmic estimate. Removing one part of size k gives the exact mean. For k<=C^(3/5), the partition ratio is exp(-pi k/sqrt(6C))(1+o(1)) uniformly by Taylor expansion; monotonicity bounds the remaining sum by C times an exponentially small ratio in C^(1/10). This gives the asserted mean constant. Independently, at C=10 the four one-size partitions correspond to divisors of 10; two sizes give 22 by positive multiplicity counts, and four sizes force 1,2,3,4, leaving 15 three-size partitions. Both supplied checkers and their stored outputs were inspected, not executed; their bounded tests are supplementary.

## originality

FAIL

Distinct Resultary record 045006e3e432 defines precisely the same H=J in the same binary Parikh fibres, and gives precisely the same joint enumerator and fixed-composition totals as well as stronger factored factorial moments. Its additional asymptotic is in a different regime, but the frozen low-area assertions are direct specializations using Richomme's bounded partition bijection and standard partition asymptotics. No priority is inferred from a same-day date; the issue is verified coverage.

## value

FAIL

The conditional alternation law is a natural reconstruction invariant, but the exact law and stronger moment information for it are already available. The stable-chamber material is the same law with vacuous partition restrictions; its remaining estimates use standard partition counting directly. The frozen contribution does not supply an independent unknown fact of that type after this coverage is accounted for.

The dated certificate retains the supplied scientific assessment, sources and limitations.
