# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-95dbd4525738`

## Correctness — PASS

The formula and equality classification are correct. Mapping the record's four neighborhood classes to the earlier general two-vertex-extension theorem gives the polynomial exactly, and the equality cases map exactly as well. Independently, the assigned verifier was inspected in full: it computes Wiener and Szeged indices from graph distances for every admissible parameter quadruple through clique size twenty and reproduces the formula on 10,165 cases. That finite check is corroborative only; the infinite conclusion is supported by the symbolic case analysis in RESULT and by the earlier broader theorem.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_small_side.py
- earlier SCOPE theorem `szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8`
- Zhang–Li, arXiv:2609.20025

### Correctness risks

- The global Zhang–Li equality problem outside the near-complete regime remains open.

## Originality — FAIL

The record is a strict specialization of an earlier same-day published SCOPE theorem. That earlier theorem treats every 2-connected graph containing an \((n-2)\)-clique, gives the adjacent-outside-vertices four-cell formula, and classifies the same equality family plus the same order-ten exception. Interchanging the earlier theorem's labels for the common-neighbor and non-neighbor cells turns its formula into this record's formula term by term. The audited RESULT itself now acknowledges that earlier coverage.

### equivalent_formulations

Searches:
- Resultary semantic search for Szeged–Wiener equality with an \((n-2)\)-clique and a two-vertex co-bipartite side
- direct comparison with `szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8`

Evidence:
- The earlier theorem includes both adjacent and nonadjacent outside vertices; the audited class is exactly its adjacent case.

Reasoning:
The two statements differ only by restricting to the adjacent two-vertex side and swapping two cell names.

### broader_coverage

Searches:
- earlier SCOPE near-complete equality theorem
- Zhang–Li arXiv:2609.20025

Evidence:
- The earlier SCOPE theorem has strictly broader graph coverage and contains the complete audited equality classification.

Reasoning:
A theorem for every \((n-2)\)-clique graph dominates the co-bipartite two-vertex-side subclass.

### exact_database_or_table

Searches:
- Resultary published findings for exact Szeged–Wiener equality classifications

Evidence:
- The earlier near-complete record is an exact theorem-level covering result, so no numerical database is needed to establish coverage.

Reasoning:
This originality question is settled by theorem implication rather than a finite table.

### claim_vs_prior_implication

Searches:
- formula-by-formula comparison of the two SCOPE records

Evidence:
- After identifying earlier cell C with this record's D and earlier D with this record's C, the polynomials and equality tuples are identical.

Reasoning:
The final claim is mechanically implied by the earlier broader statement.

### source_inspections

- **Szeged–Wiener equality for graphs with an \((n-2)\)-clique** — 2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8. Trigger: Earlier same-day theorem named in the audited RESULT. Material read: Complete RESULT.md from the assigned repository snapshot. Method: Full statement, formula, and equality-case comparison. Assessment: DECISIVE COVERAGE. Evidence: Its adjacent-outside-vertices case is exactly the audited theorem after renaming two neighborhood cells.
- **Improved Bounds on the Szeged–Wiener Gap and the BKLPS Conjecture** — https://arxiv.org/abs/2609.20025. Trigger: Primary motivating equality problem. Material read: Authorized full text, pages 1–12, including definitions, intermediate bounds, and Theorem 6 proof setup. Method: Primary full-text inspection. Assessment: Background source posing the equality problem; not needed for the decisive same-day coverage. Evidence: It proves the \(2n\) lower bound and presents equality as a classification problem.

### checked_sources

- earlier SCOPE near-complete equality theorem
- Zhang–Li arXiv:2609.20025
- assigned RESULT.md and exact verifier
- Resultary semantic search

### residual_risks

- No residual novelty remains for the stated theorem because the earlier broader record is decisive.

## Scientific value — FAIL

As a focused derivation the record is reproducible and pedagogically tidy, but under the required value bar it is only a known specialization/corroboration of an already published broader theorem. It introduces no new boundary, invariant, or obstruction beyond that coverage.

### Value sources

- earlier SCOPE near-complete equality theorem
- assigned RESULT.md

### Value risks

- The rejection is scientific-value based for a duplicate specialization, not a correctness defect.

## Limitations

- Correctness passes; originality and scientific value fail because an earlier broader theorem already contains the result.
- The finite verifier is supporting evidence only.
- The global equality problem remains open outside the stated near-complete regime.

## Disposition

**FAILED**
