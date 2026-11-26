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

The frozen Finding is correct, but its proof line 23 incorrectly prints binomial(a+1,2)+binomial(b+1,2): at a=b=1 that line would give 9 instead of 7. The corrected complete RESULT.md at /workspace/repairs/2/RESULT.md uses binomial(a,2)+binomial(b,2). Both bounds nonempty force both onto one chain of length m, with 1≤p≤q≤m−1; the one-sided types number 2(a+1)(b+1)−1. For the pair count, homogeneity means each consistent finite induced diagram gives exactly one complete type. Downsets, upsets and lower-to-upper comparisons characterize the single-point diagrams. For x<y, lower sets must nest forward and upper sets backward; these inclusions already close paths through x<y. For incomparable x,y, the two lower/successor intersections must be empty, preventing any newly forced x–y comparison via the base. With either relation all other paths close using those conditions and the unary ones. Independently compressed each chain's four cuts to endpoint flags and k used interior ranks, each contributing binomial(m−1,k). Combined the two chains by excluding opposite nonempty lower/upper flags between them for each variable. The resulting two Newton-basis coefficient arrays agree exactly with the Finding's polynomials; checked each single-chain axis and the empty base separately (62 equalities in all; symmetry gives the second axis). This certifies the identity for all lengths, not just samples. Finally H−N is strictly positive and O((a+b+1)^3), whereas N² grows quartically, giving the claimed fraction and uniform limit. The corrected unary line changes neither the Finding nor the pair proof or certificate inputs.

## originality

PASS

Best of the inspected evidence: only the independent two-length pair spectrum and its incomparable-count factorization and uniform-in-balance comparison survive as the contribution. Unary counts, single-chain counts, generic extension machinery and the qualitative comparable-fraction phenomenon on a different parameter family are not new. The repaired prose now explicitly identifies the strongest same-date comparison.

## value

PASS

The marked disjoint-two-chain class is distinguished by a pre-existing extremal unary equality. The new structural fact is that the incomparable pair channel over this entire class reduces to its unary count, although full pair counts require more information. It also supplies an exact comparable comparison and a limit without balance assumptions. These are useful checks for type-spectrum and order-diagram work, not arbitrary small poset counts. Correcting the unary derivation preserves that contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
