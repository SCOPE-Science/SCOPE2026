---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For a finite annotation beta, the least rule chooses exactly one gamma<beta and thus unfolds as finite additive sum of lower approximants, while the greatest rule demands all gamma<beta and thus finite additive conjunction. Stage zero uses 0/top. Recursion terminates in finite beta and formula nesting; capture-avoiding substitution and MALL duality preserve sequent rules. Finite cut-free MALL search decides the uniformly effectively translated sequent. The alpha=omega complexity claim is cited, not proved, as the alpha=omega instance of Das–Pshenitsyn Theorem 2.8. Independent check enumerates 21 finite rule-arity instances n<=5; proof is conceptual finite unfolding, not a computation certificate.

## originality

FAIL

FAIL due to decisive prior implication, not lack of search: the entire finite-stage assertion is the immediate finite-arity restatement/inlining of the explicitly published mu/nu ordinal introduction rules in Das–Pshenitsyn Definition 2.4 with MALL additive connectives, and the omega hardness clause is literally its Theorem 2.8 at alpha=omega. The paper need not spell the corollary in identical words for its proof-system definition and theorem to cover the claimed content. No additional nontrivial independent lemma, optimization, or new equivalence is established.

## value

FAIL

The finite-stage reduction merely expands a finite family of ordinal-indexed premises into MALL additive connectives exactly as their published rule definitions prescribe, with no structural obstacle, unexpected cutoff, sharp bound, or new invariant. The infinite-stage hardness is imported unaltered from the defining paper. Thus the conjunction is a useful pedagogical observation but a routine definitional consequence, not an independently motivated substantive research finding under the same value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
