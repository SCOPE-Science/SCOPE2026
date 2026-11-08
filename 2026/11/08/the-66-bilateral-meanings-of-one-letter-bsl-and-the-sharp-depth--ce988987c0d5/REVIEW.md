# Mathematical review

**Scope.** Exactly one Boolean proposition \(p\), its two valuations, every one of the four teams, and the bilateral BSL grammar with internal \(\Diamond\), split disjunction, and \(\mathrm{NE}\). The final claim is the exact **paired** census \(66\), with depth-profile \(39,64,66\), sharp maximum depth two, and 11 support projections present already at depth zero.

## Correctness: PASS

The primary semantics gives an exact algebra of pairs of sets of four teams. Each operation is reconstructed from its support and antisupport clauses, especially the nonempty-subteam requirement for internal \(\Diamond\). By induction on syntax, the closure of the three atomic pairs is exactly the set of paired meanings. An explicit table has 66 pairs, contains the atoms, and is closed under each operation; an independently implemented set-family enumeration reaches all 66 elements. Repeating closure with a depth restriction gives 39, then 64, then 66, then unchanged 66. The depth-two formula \(\Diamond\neg\Diamond p\) supplies a profile absent from depth at most one. Two stand-alone Python implementations were run successfully on the four-team universe. Computation is finite and exhaustive; the inference to arbitrarily long formulas uses structural induction and the closed table, not extrapolation.

**Correctness risk:** The result depends on the particular bilateral BSL clauses of Aloni et al. Section 3.1; it should not be transferred to BSML or Kripke-external possibility by analogy. The codes are masks for sets of teams, not truth values at valuations.

## Originality: PASS within inspected evidence

The closest text is Aloni et al. (2026), *Teams, Truthmakers, Translations*, arXiv:2610.15680v1, Section 3.1 (full displayed semantic clauses) and Section 4 (paired translation). It defines the object but does not establish the 66-pair census or depth counts in the inspected text. Anttila and Knudstorp (2025), *Convex Team Logics*, arXiv:2503.21850, prove weak-ideal **support** expressivity, but a support-only coverage theorem does not determine which supports and antisupports occur together, nor when two-sided meanings first become expressible. The earlier state-based-modal treatment arXiv:2305.11777 has external modal operators, so its theorems do not entail the internal-subteam census. Targeted published-record searches for bilateral one-letter profiles, free finite algebras, and weak-ideal pairs found no equivalent or stronger result. This is not proof of global historical uniqueness.

**Originality risk:** A specialized earlier calculation or consequence of an uninspected theorem on free bilateral team algebras may cover the 66-pair statement. The relevant 2026 full text was inspected at its clauses and main translation rather than every conceivable implication of all cited literature.

## Value: PASS

The pair count and the exact sharp depth threshold solve an intrinsic finite semantic problem raised by a recent new translation linking bilateral team logic to classical semilattice-modal logic. It measures precisely the two-sided descriptive resources the translation must preserve. The dramatic contrast between support-only saturation at depth zero (11 possibilities) and full paired stabilization at depth two (66) shows why support expressivity cannot replace bilateral analysis. These are complete, natural classifications, not an arbitrary sample or a trivial rephrasing of the weak-ideal result.

**Value risk:** The domain is the smallest nontrivial propositional vocabulary. No asymptotic or complexity bound for a large variable set is derived; its value is as an exact baseline and a sharp polarity-sensitive counterpoint.

## Independence and limits

The included `checker.py` and `checker_direct.py` are finite reproducibility artifacts. They do not constitute outside verification, independent review, or a priority certificate. No exhaustive audit of older, unindexed literature was completed.

Self-review: passed. Independent audit: not yet performed.
