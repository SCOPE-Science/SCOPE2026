# Independent audit — SCOPE-20260910-015

## Scope
Independent review of `2026/09/10/015` at Git tree `f7877db2115fcd667d4e99dab12f6ae71a68db6c` for task `20cb4fb0f42f361f7a14d25d084c5c02`. The current `main` tree matched the assigned source snapshot, so the scientific assessment used the assigned package without a stale-tree substitution.

## Correctness
**PASS**

Independent exhaustive enumeration of all 64 deterministic response triples reproduces the win-count spectrum {0:3,2:7,3:24,4:18,5:8,6:3,8:1} and the unique 8/8 strategy f=g=h≡1.

The analytic forcing is immediate and correct: diagonal questions identify the three answers at input 0 and input 1; off-diagonal questions 001 and 110 force both common bits to 1.

A perfect classical strategy embeds in every quantum/commuting strategy class, while all game values are <=1, so omega_c=omega_q=omega_qc=1 and the purported 23/24 upper bound is false.

## Originality
**FAIL**

The entire headline follows by evaluating the frozen predicate on the constant answer 111. The uniqueness proof needs only two further question triples. This is a truth-table consequence of the definition, not a new nonlocal-game phenomenon.

The literature's open search for an explicit synchronous Tsirelson-separation witness does not make an arbitrary failed candidate scientifically original; this candidate is excluded before any NPA, operator-algebra, or entanglement analysis.

## Scientific value
**FAIL**

The package is a useful sanity check for a malformed candidate game, but its central result is the existence of an obvious constant classical winner. It contributes no separation, bound, self-testing theorem, or nontrivial game-algebra analysis.

The NPA and GHZ observations are downstream consequences of classical value 1 and do not restore research-level value.

## Reproducibility
Status: **reproduced**.
- Independent 64-strategy enumeration reproduced the exact deterministic spectrum and unique optimum.
- Direct predicate evaluation confirms constant-1 wins all eight questions.
- Limitation: No high-level NPA computation is needed; the value-one conclusion is already exact at the classical level.

## Literature checked
- [Connes implies Tsirelson: a simple proof](https://arxiv.org/abs/2209.07940): Explains that the post-MIP*=RE quest is for an explicit synchronous game violating the synchronous Tsirelson conjecture; the record's game does not approach that frontier because it has a perfect classical strategy.
- [Nonlocal games, synchronous correlations, and Bell inequalities](https://arxiv.org/abs/1707.06200): Gives substantive small synchronous Bell-inequality phenomena; it highlights the contrast with a predicate trivialized by a constant strategy.
- [Robust self-testing for nonlocal games with robust game algebras](https://arxiv.org/abs/2411.03259): Provides general self-testing criteria for synchronous/XOR/BCS games; the record's claimed rigidity fallback is moot once multiple non-GHZ perfect realizations follow from the classical constant winner.

## Limitations
- The exact finite game diagnosis is correct and worth preserving as a failed-candidate record; failure concerns originality and scientific value.

## Conclusion
The package is scientifically **failed** under the three-axis audit because at least one required axis fails. Relocate the complete original package atomically to the assigned failed path, preserving all original evidence. The relocation is a publication-status decision, not a claim that every underlying computation is false.
