---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The last deleted a can be no earlier than block k; the k deleted b's then require blocks k through 2k-1 at the earliest. In a feasible embedding each block contributes ab, b, a, or nothing. All b-singletons come before a-singletons, with at most one empty block, which selects j=k or j=k-1. Conversely a tuple constructs an embedding, inserting a fully deleted block in the central gap when j=k-1. The maximum of prefix (#b−#a) is j, distinguishing the families; before its first attainment greedy left parsing separates intact pairs from b-singletons, after its last attainment greedy right parsing separates pairs from a-singletons, and the interval between consists only of intact pairs. Thus there are exactly binom(r+j,2j) distinct words per family and the boundary m=2k-1 has one word. An independent prefix dynamic program checked exact distinct-output counts and their peak statistics for 77 parameter pairs (including infeasible cases and the k=1 control). A separate direct position-subset comparison checked literal equality with the normal-form sets for 77 pairs including infeasible cases in the intended k≥2 regime.

## originality

FAIL

The published split-invariant two-run result already covers the entire frozen scope upon setting alpha=beta=k, including the exact formula and the same two-block-type gap characterization. It additionally handles unbalanced runs and embedding multiplicities. Its catalog date follows the frozen one: the decision is based on verified equivalent/stronger coverage, with no inference about which proof was discovered first or about provenance. Adamson et al.'s general algorithm alone would not imply this closed form as a stated theorem, and the repeated alternating-pattern deletion formula concerns a different pattern.

## value

PASS

The block-gap normal form solves the collision problem for distinct outputs, not just the number of deletion embeddings, and gives a natural exact structural benchmark for complementary-subsequence algorithms. This intrinsic usefulness does not provide a scientifically distinct remainder after specializing the stronger published result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
