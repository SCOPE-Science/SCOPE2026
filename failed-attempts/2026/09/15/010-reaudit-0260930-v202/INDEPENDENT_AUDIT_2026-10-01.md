---
audit_date_utc: 2026-10-01
status: failed
record_id: SCOPE-20260915-010
---

# Scientific audit

## Final claim

For the reciprocal fixed-field span \(X=\{1/(x-y):x\in F\}\), every subset of size at most \([F(y):F]\) is \(F\)-linearly independent; hence if \([F(y):F]\ge q=|F|\), then the \(F\)-span and prime-field span have exact coarse contributions \(mq/n\) and \(q/n\), and the weak condition \(m/n	o0\) does not imply the strong \(q/n	o0\) condition.

## Correctness — PASS

Clearing denominators in an \(N\)-term relation produces a nonzero polynomial over \(F\) of degree at most \(N-1\) vanishing at \(y\), proving independence for \(N\le [F(y):F]\). Under degree at least \(q\), all \(q\) reciprocal elements are independent, so the prime-field span has size \(p^q\) and the \(F\)-span has size \(q^q=p^{mq}\), giving coarse dimensions \(q/n\) and \(mq/n\). The sequences \(m=1,n=p^2\) and \(m=1,n=p\) give \(q/n	o0\) and \(q/n=1\), respectively, while both have \(m/n	o0\).

Checked sources: artifacts/span_delta.py; Hils--Hrushovski--Ye--Zou, arXiv:2406.00880, Example 7.12

Residual risk: The result is conditional on maximal enough extension degree and does not establish uniform cross-characteristic definability or positive transformal degree.

## Originality — FAIL

The primary source already uses this reciprocal-span construction, its linear-independence mechanism, and the strong hypothesis \(p^{m_i}/n_i	o0\). The finite-degree truncation is the standard minimal-polynomial version of that argument, and the weak/strong separation follows from substituting \(q=p^m\) and two elementary sequences. Thus the audited statement is mechanically implied by the published construction plus elementary finite-field arithmetic.

### Equivalent Formulations

Searches: fixed field reciprocal span pseudofinite difference fields coarse dimension; Example 7.12 reciprocal 1/(x-y)

Evidence: Example 7.12 uses the same reciprocal set and prime-field span.

Reasoning: The finite statement is the bounded-degree form of the source's independence argument.

### Broader Coverage

Searches: pseudofinite difference fields coarse dimension transformal transcendence

Evidence: The source already states the stronger size hypothesis needed for its coarse-dimension conclusion.

Reasoning: The new ratio comparison only diagnoses that the source hypothesis is stronger than \(m/n	o0\).

### Exact Database Or Table

Searches: q/n m/n pseudofinite difference fields

Evidence: No database is relevant; the distinction is an elementary asymptotic calculation.

Reasoning: No tabulation is needed.

### Claim Vs Prior Implication

Searches: arXiv 2406.00880 Example 7.12 fixed prime p

Evidence: The source's condition is \(p^{m_i}/n_i	o0\), exactly \(q_i/n_i	o0\).

Reasoning: Choosing varying primes immediately separates it from \(m_i/n_i	o0\).


### Source inspections

- **COVERING** — 2406.00880 (https://arxiv.org/pdf/2406.00880): Primary full-text Example 7.12 and adjacent coarse-dimension argument. Evidence: The same reciprocal set, linear independence, and strong \(p^{m_i}/n_i\) hypothesis are explicit.
- **CONTEXT** — 1806.10026 (https://arxiv.org/pdf/1806.10026): Background primary paper on pseudofinite difference fields and dimension context. Evidence: Provides ambient model-theoretic setting, not an independent source of the ratio observation.

Checked sources: https://arxiv.org/pdf/2406.00880; https://arxiv.org/pdf/1806.10026; artifacts/span_delta.py

Residual risks: No source was found spelling out the two example sequences, but they are immediate arithmetic consequences rather than a substantive independent theorem.

## Value — FAIL

The statement is a useful warning about a failed transfer route, but the mathematical content beyond the published example is a standard minimal-polynomial lemma and an elementary asymptotic hypothesis check. It does not settle the cross-characteristic definability or transformal-dimension issue that motivates the target, so it does not clear the value bar as a standalone result.

Checked sources: https://arxiv.org/pdf/2406.00880

Residual risk: A theorem resolving uniform definability or producing a genuine cross-characteristic counterexample would materially raise the value.

## Disposition

**FAILED**. Acceptance requires PASS on correctness, originality, and value.
