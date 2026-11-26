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

The imported classification and Proposition 4.2 apply at n≥5. In a permissible pair, t restricts to an involution on its image and all off-image vertices are leaves. Each e-fibre has one distinguished root star, arbitrary other root stars, and arbitrary two-cycles decorated by an unordered pair of leaf counts; the latter give floor(j/2) types at size j. This gives APQ, with AP exactly the no-two-cycle case, and taking multisets of fibres implements simultaneous relabelling. A rank-three square root of t must transpose two non-distinguished t-roots in an e-fibre. Conversely choose such a transposition on the roots, fixing the others, and compose it with t to obtain u. The multiplication table shows that a product of image-rank≥3 maps becomes rank two only by replacing a rank-three parameter u by u², up to relabelling: odd-type factors preserve the right parameter, even-type factors square it, and singular t collapses the image to rank one. Iterating the table cannot undo a rank drop. A double transposition fixing one point, with e constant there, supplies the even-type factor at every n≥5. Thus essential rank-two fibres have at most one additional root star; exactly the partition subfamily t=e must be removed. Independently multiplied truncated geometric factors through degree 12; reproduced all eight displayed ranks, beginning with orbit counts 15 and 17 at n=5. Inspected checker.py and its recorded output without executing them; neither finite computation establishes the quantified theorem. The original classification is due to Schein–Teclezghi, as cited by Gould–Grau–Johnson, Theorem 2.1.

## originality

FAIL

Direct equivalent coverage by a distinct indexed Resultary record: both Euler orbit counts, the all-n rank formula, initial ranks, and the essential square-root criterion agree. This is scientific duplication, not a claim about external historical priority or chronology inferred solely from path dates.

## value

PASS

The all-size minimal generating-set rank is a natural invariant queried explicitly in the structural literature. The fibre and square-root characterization makes the difficult orbit split enumerable for every size. That mathematical value does not provide new value beyond the exact matching indexed finding and cannot cure the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
