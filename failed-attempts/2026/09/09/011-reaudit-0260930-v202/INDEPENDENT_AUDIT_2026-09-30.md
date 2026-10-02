# Independent mathematical audit — 2026-09-30

## Outcome

**FAILED** for the final finding as stated.

## Correctness — PASS

The recurrence is reconstructed directly from the move rule. Strong induction gives \(L(n)=\lfloor n/2\rfloor\): every split satisfies \(\lfloor a/2\rfloor+\lfloor b/2\rfloor\le\lfloor(n-2)/2\rfloor\), with equality at \((0,n-2)\). For \(S(n)\), the residue-class inequality \(\lfloor(a+1)/3\rfloor+\lfloor(b+1)/3\rfloor\ge\lfloor(a+b)/3\rfloor\) and the stated witness split give \(S(n)=\lfloor(n+1)/3\rfloor\). The committed DP verifier and an independent recurrence replay agree for every \(0\le n\le120\), including the extremal/distribution claims.

Checked sources:
- actual committed `artifacts/verify.py` and `artifacts/dawson_durations_0_120.csv`; independent recurrence replay

Residual risks:
- The name “birthday/remoteness” is broader terminology than needed; the audited invariants are explicitly defined shortest and longest play lengths.

## Originality — PASS

No inspected publication or database entry was found stating these two closed forms for Dawson’s Kayles game length. The standard OEIS entry records Sprague–Grundy values instead. This is best-of-knowledge originality only.

### equivalent_formulations

Searches: Resultary semantic search for Dawson’s Kayles shortest/longest game length; OEIS searches for Dawson remoteness/birthday; arXiv search for Dawson game length

Evidence: The only exact published-result hit was the audited record; OEIS A002187 concerns Grundy values.

Reasoning: Shortest/longest play, birthday and remoteness aliases were checked; no exact prior formula was located.

### broader_coverage

Searches: Plambeck, Taming the wild in impartial combinatorial games, arXiv:math/0501315; OEIS A002187

Evidence: These sources treat impartial-game structure/Grundy data rather than the audited duration recurrence.

Reasoning: No inspected broader theorem was found that states the same length formulas for this octal game.

### exact_database_or_table

Searches: OEIS A002187 and its b-file; Resultary exact formula search

Evidence: The standard table is Grundy-valued; it does not tabulate \(S(n)\) or \(L(n)\).

Reasoning: The 0..120 duration CSV was not found as a known table.

### claim_vs_prior_implication

Searches: Comparison of the move recurrence with general combinatorial-game definitions

Evidence: The closed forms follow from elementary induction once this move recurrence is written down.

Reasoning: Mechanical derivability from the definition is a value concern, not evidence that a prior publication already stated the formulas.

### source_inspections

- **OEIS A002187 — Dawson’s Chess/Dawson’s Kayles Grundy values** (https://oeis.org/A002187): trigger=Canonical databased information for the same game.; material read=Sequence definition and cited role as the standard Grundy table.; method=Database comparison.; assessment=NOT COVERING THE AUDITED INVARIANT.; evidence=It tabulates nim-values, not shortest/longest total play lengths.
- **Taming the wild in impartial combinatorial games** (https://arxiv.org/abs/math/0501315): trigger=Standard modern Dawson/octal-game literature cited by the record.; material read=Accessible abstract/scope material.; method=Primary-source inspection.; assessment=RELATED, NOT FOUND TO STATE THE TWO LENGTH FORMULAS.; evidence=The work concerns impartial game structure and quotients rather than this elementary duration recurrence.
- **Committed duration verifier** (artifacts/verify.py): trigger=Finite dataset and recurrence certificate.; material read=Complete source and complete CSV.; method=Source inspection and independent recurrence replay.; assessment=Supports correctness.; evidence=All 121 rows satisfy the two closed forms and witness recurrences.

### checked_sources

- OEIS A002187
- arXiv:math/0501315
- Resultary semantic search
- committed verifier/CSV

### residual_risks

- An older combinatorial-games text may mention these elementary duration formulas without being indexed by the searches.

## Scientific value — FAIL

The headline formulas are immediate elementary consequences of the one-line recurrence and two floor inequalities; the 0..120 extremal/distribution table is then automatic arithmetic from those formulas. The cutoff 120 is not mathematically intrinsic. Under the required value standard this is a routine deduction plus an arbitrary finite slice, not a structural gap needing a new research record.

Checked sources:
- audited recurrence proof; standard Dawson/CGT sources

Residual risks:
- A pedagogical or benchmarking use is plausible, but that is not enough to meet the stated research-value bar.

## Limitations

- The mathematical formulas are correct, but the scientific rejection is on value rather than truth.
- No claim is made about novelty of Sprague–Grundy periodicity or outcome classes.
- The 0..120 cutoff is not intrinsic to the uniform proof.
