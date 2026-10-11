---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The restriction is mathematically correct. Independent formula-by-formula inspection of the primary PDF confirms the fixed vocabulary, depth at most two for Good and membership, depth one for successor/addition/multiplication, and no extra temporal operators in the arithmetic translation or injectivizing padding. Restricting the published injective upper reduction preserves injectivity, so Myhill applies.

## originality

FAIL

The final claim is implication-covered by the very primary paper it audits. Pshenitsyn fixes exactly the five agents and five propositions before the lower reduction, explicitly explains that numbers are encoded after one move and sets after two moves, and the displayed formulas use only \(X\) and \(XX\). The same paper supplies the injective upper reduction and the Myhill step. Reading off a temporal-depth-two bound and freezing the already fixed vocabulary is therefore a direct corollary of the published construction, even though the theorem statement does not spell out those two adjectives.

## value

FAIL

The restriction is conceptually neat, but as a scientific contribution it is a routine proof-range observation: the source explicitly fixes the vocabulary and encodes first- and second-order objects at one and two moves. No new lower-bound gadget, structural lemma, counterexample, classification, or nontrivial boundary argument is added. The package itself disclaims optimality at depth one and at smaller vocabularies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
