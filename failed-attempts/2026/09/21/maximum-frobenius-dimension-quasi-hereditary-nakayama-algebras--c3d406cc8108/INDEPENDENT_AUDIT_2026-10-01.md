---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For split basic quasi-hereditary Nakayama algebras with \(n\ge2\) simple modules, the Frobenius dimension is at most \(n^2+1\), sharply attained; in the cyclic case at most one injective-projective Hom space has dimension two and all others have dimension at most one.

## Correctness — PASS

The uniserial Hom formula counts eligible occurrences of the source top in the terminal part of the target. Quasi-heredity in the cyclic case supplies a projective-dimension-two simple, forcing a plateau in lifted Kupisch endpoints; periodicity bounds projective and injective lengths by \(2n-1\), all long injectives share one top, and only one target can then support two eligible occurrences. Hence at most one of the \(n^2\) Hom spaces has dimension two. The displayed Kupisch family realizes every Hom nontrivially and one doubly. The inspected finite verifier confirms maxima \(n^2+1\) for \(2\le n\le6\) but is only corroborative.

**Checked sources.** assigned RESULT.md and artifacts/verify_small.py at tree 4d8f45c5a54cb031e54109838a24822e13cc5259; Uematsu--Yamagata/Marczinzik--Sen quasi-hereditary Nakayama criterion; published 2026-09-20 SCOPE theorem on the same Frobenius-dimension maximum

**Residual risks.** No correctness defect was found.

## Originality — FAIL

A published SCOPE record dated 2026-09-20 already proves the same \(n^2+1\) maximum with the same plateau/unique-double-Hom mechanism. The current changes from algebraically closed connected basic algebras to split basic algebras and adds disconnected bookkeeping, but those are routine proof-level extensions and do not create an uncovered mathematical claim under implication-level comparison.

### Equivalent formulations

The current statement is the same invariant and extremal theorem; its alternate sharp Kupisch representative does not change the implication.

### Broader coverage

The earlier SCOPE theorem already dominates the substantive content; the split-field wording is a routine generality because the proof uses only split uniserial combinatorics.

### Exact database or table

This is a decisive exact prior result, not an unsuccessful novelty search.

### Claim versus prior implication

The disconnected extension follows by additivity and a convexity inequality; the field generalization follows because the proof is split-uniserial. Neither avoids prior coverage of the main claim.

**Checked sources.** published SCOPE 2026-09-20 record 972984d0bf0d; https://arxiv.org/abs/2109.03441; MathOverflow question 351323

**Residual risks.** No residual search uncertainty can overcome the exact prior SCOPE coverage.

## Value — FAIL

The extremal theorem is valuable in itself, but this record is a next-day duplicate/routine generality extension of an already published theorem with the same mechanism. Under the shared value bar, alternate witnesses and split-field/disconnected bookkeeping do not constitute a separate motivated gap.

**Checked sources.** published SCOPE 2026-09-20 exact theorem; current proof

**Residual risks.** The statement remains useful as an alternate exposition.

## Limitations

- The theorem is for split basic finite-dimensional Nakayama algebras.
- The rejection is prior-coverage/value failure, not a correctness or access failure.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
