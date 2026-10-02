# Independent scientific audit — SCOPE-20260918-307617ad8c19

Audited at: 2026-10-01T07:11:57.147372Z

Disposition: **failed**

## Correctness — PASS

For any selected \(r\times r\) minor, the clustered exponential determinant has leading term \((i\varepsilon)^{r(r-1)/2}V(a)V(b)/\prod_{q=0}^{r-1}q!\), which is nonzero for distinct real nodes. Hence the minor is a nontrivial real-analytic function of either the selected delays or the selected angles. The zero set of its squared modulus has Lebesgue measure zero, and rank deficiency is contained in that zero set. Nonvanishing of a maximal minor is open, while a nontrivial analytic zero set has empty interior, giving density. A separate numerical expansion check reproduced the predicted leading coefficient in a four-by-four example, but the proof is analytic.

## Originality — FAIL

The source-specific conjecture is correct, but its probability-one rank conclusion is mechanically implied by classical analytic-function results. For distinct frequencies the exponentials are linearly independent analytic functions; Bostan–Dumas give the classical nonzero-Wronskian criterion for such a family. A nonzero Wronskian yields a nontrivial clustered evaluation determinant, and Mityagin's standard zero-set theorem then makes the singular evaluation tuples measure zero. The record's Cauchy–Binet computation is an explicit proof of this known implication rather than an original theorem.

### Equivalent formulations

The audited clustered determinant is the standard bridge from nonzero Wronskian/analytic independence to generic invertibility of an evaluation matrix.

### Broader coverage

Together these classical results cover the essential implication for arbitrary finite rank, more generally than the Takens application.

### Exact database or table

Absence of the source-specific wording does not restore originality when the statement is a direct corollary of standard analytic-function theory.

### Claim versus prior implication

This is exactly the fixed-frequency and fixed-delay generic-rank conclusion claimed by the record.

## Value — FAIL

Removing an explicit assumption from a recent embedding paper is useful, but the mathematical step is a short application of classical analytic linear independence, a confluent Vandermonde expansion, and the standard zero-set theorem. Under the stated value bar, this is a routine textbook-level deduction rather than a new substantive structural result.

## Sources inspected

- Stable Takens' Embedding Theorem for Non-Uniformly-Sampled Linear Systems — https://arxiv.org/abs/2608.14001. TARGET_OPEN_STATEMENT: The paper explicitly poses full rank as Conjecture 1 and conditions its embedding theorem on it.
- Wronskians and Linear Independence — https://arxiv.org/abs/1301.6598. COVERING_GENERAL_THEOREM: Distinct exponential functions are linearly independent analytic functions, so the theorem gives a nonzero Wronskian.
- The Zero Set of a Real Analytic Function — https://doi.org/10.1134/S0001434620030189. COVERING_GENERAL_THEOREM: Applied to the squared modulus of a maximal minor, it gives the measure-zero singular set.

## Checked sources

- https://arxiv.org/abs/2608.14001
- https://arxiv.org/abs/1301.6598
- https://doi.org/10.1134/S0001434620030189
- https://arxiv.org/abs/2609.03325
- Resultary semantic search

## Residual risks

- The Ng–Kutz paper genuinely left the statement as a conjecture; the failure is therefore coverage by older general mathematics, not a claim that the source itself solved it.
- The explicit clustered determinant remains a useful self-contained exposition of the classical implication.

## Limitations

- The generic-rank statement is mathematically correct, but it is rejected as a new finding because it is a direct application of classical analytic-function theory. It also gives no quantitative conditioning bound and requires distinct nodes and absolutely continuous random parameters.
