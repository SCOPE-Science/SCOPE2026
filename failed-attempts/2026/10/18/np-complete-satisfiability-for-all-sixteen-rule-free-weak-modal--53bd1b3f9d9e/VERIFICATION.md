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

Independently verified locality for the fixed syntax. Let Q be the restricted saturation. If C is present, close Q under arbitrary binary conjunction trees. This intersects the support S exactly in Q: a constructed conjunction in S has both children in S, and induction on its construction followed by restricted C gives membership in Q. M on a new conjunction returns its children, and on an old one returns subformulas already in Q. An implication premise for K cannot be a newly constructed conjunction, so it is in Q; its antecedent and consequent are in S, so its antecedent in the tree closure must be in Q and K works within Q. N is accounted for at the seed, and with no C use Q itself. The result is closed and contains the generators, giving equality by leastness. This applies to primitive conjunction or Nishimura's usual non-implication-headed negation/implication abbreviation, and to formulas measured in the fixed syntax used for saturation. A one-world model with the least closure of guessed positive bodies realizes the guesses exactly when no guessed-negative body enters the saturation. Every existing model supplies such guesses since its closed H contains this least closure. N does not require necessitation. There are linearly many subformulas and bits, linearly many strict rounds, and each round can enumerate premises and compare ordinary syntax trees in polynomial time. Modal-free SAT and tautology are identity reductions, and negation interchanges invalidity and satisfiability. The same verifier works with four selection bits. The frozen checker was inspected, not executed; its bounded comparisons do not establish unrestricted locality.

## originality

FAIL

Nishimura does not label the rule-free problem NP/coNP-complete and explicitly mentions complexity as a direction. However, Corollary 3.14 already states the decisive exact finite-support membership computation and specifies the one-world candidate to which it applies, for the very same sixteen systems. Definitions 3.5 and 3.7 make the support linear and the restricted fixed-point computation polynomial by a direct count. Guess the subset in Corollary 3.14 rather than loop over it, and use the modal-free classical fragments for hardness. This yields the frozen classification without a new premise. It is verified implication by prior text, not a claim that the complexity labels appear there verbatim.

## value

FAIL

The decision-complexity question is natural and the proof exposition is useful, especially for readers wary of infinite conjunction closure. However, relative to the existing exact support recipe and already specified enumerable singleton candidates, the gain is the routine polynomial fixed-point count, guessing the explicitly described subset instead of enumerating it, and modal-free SAT/tautology hardness. The general intersection statement is already implicit per target in that recipe. The record does not supply a new structural ingredient or a distinct valuable complexity claim beyond that direct deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
