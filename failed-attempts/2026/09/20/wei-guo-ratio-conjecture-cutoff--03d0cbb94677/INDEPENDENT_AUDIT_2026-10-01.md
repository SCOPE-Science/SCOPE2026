# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-03d0cbb94677`

## Correctness — PASS

The Eulerian-polynomial reduction is correct. For \(i\ge1\), the ratio is \(A_{i+1}(e^{-t})/((1-e^{-t})A_i(e^{-t}))\). Eulerian polynomials have simple negative roots; monicity and constant term one force at least one root in \((-1,0)\) for every degree at least two, and the recurrence prevents cancellation with the numerator. Exponential substitution sends that root to a genuine pole in the open right half-plane. A completely monotone function is a Laplace transform and therefore holomorphic there, giving the contradiction for every \(i\ge3\). The cases \(0,1,2\) have explicit positive discrete Laplace expansions.

### Correctness sources

- assigned RESULT.md
- Wei–Guo 2014 full accessible article
- current published complete-monotonicity classification

### Correctness risks

- The theorem does not identify the first real derivative-sign violation for each failed index.

## Originality — FAIL

Current published coverage is exact and decisive. A 2026-09-21 published finding gives the same complete-monotonicity cutoff \(i\in\{0,1,2\}\), the same Eulerian-polynomial right-half-plane pole mechanism for all \(i\ge3\), and the same explicit first obstruction. It additionally proves the logarithmic-complete-monotonicity boundary. The audited theorem is therefore fully covered under the required current-implication standard. The later date does not determine historical first-discovery priority.

### equivalent_formulations

Searches:
- Resultary: Wei Guo Conjecture 12 complete monotonicity polylogarithm Eulerian cutoff
- direct comparison with 2026/9/21/SCOPE-polylog-ratio-complete-monotonicity-classification--efe7f86dd392

Evidence:
- The later theorem states the identical cutoff and identical pole proof.

Reasoning:
The ratio notation, negative-integer polylogarithm form, and Eulerian rational-function form are mathematically equivalent.

### broader_coverage

Searches:
- https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-polylog-ratio-complete-monotonicity-classification--efe7f86dd392
- Wei–Guo 2014

Evidence:
- The later theorem strictly contains the audited result by adding the logarithmic-complete-monotonicity classification.

Reasoning:
A stronger current theorem covers every originality-bearing assertion of the audited final claim.

### exact_database_or_table

Searches:
- current Resultary special-function findings

Evidence:
- No database comparison is needed because exact theorem-level coverage exists.

Reasoning:
Coverage is direct, not table-based.

### claim_vs_prior_implication

Searches:
- statement-by-statement implication comparison

Evidence:
- Both results prove positivity for indices zero through two and use a denominator Eulerian root in \((-1,0)\) to obstruct all higher indices.

Reasoning:
The current theorem reproduces the full scientific claim, not merely its title or a special case.

### source_inspections

- **Complete-monotonicity classification for consecutive exponential-derivative ratios** — https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-polylog-ratio-complete-monotonicity-classification--efe7f86dd392. Trigger: Exact current semantic match. Material read: Complete published RESULT.md. Method: Full theorem-and-proof comparison. Assessment: DECISIVE CURRENT COVERAGE. Evidence: The cutoff and Eulerian-pole mechanism coincide; the current result is stronger because it also classifies logarithmic complete monotonicity.
- **Complete Monotonicity of Functions Connected with the Exponential Function and Derivatives** — https://doi.org/10.1155/2014/851213. Trigger: Primary conjecture source. Material read: Complete accessible article text including Theorem 3 and Conjecture 12. Method: Primary full-text statement comparison. Assessment: Background source posing the conjecture. Evidence: The paper proves the ratios decreasing and explicitly conjectures complete monotonicity for all indices.

### checked_sources

- https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-polylog-ratio-complete-monotonicity-classification--efe7f86dd392
- https://doi.org/10.1155/2014/851213
- current Resultary search
- assigned RESULT.md

### residual_risks

- The covering theorem postdates the audited record by one day; current coverage does not adjudicate historical priority.

## Scientific value — FAIL

Settling the Wei–Guo conjecture is mathematically worthwhile, but the unchanged finding is now duplicated by a stronger current theorem with the same mechanism. Under the required value bar, republishing that covered result as a separate finding adds no surviving mathematical contribution.

### Value sources

- current stronger classification
- Wei–Guo conjecture source

### Value risks

- Failure is due to current duplication, not incorrect mathematics.

## Limitations

- Correctness passes.
- Originality and scientific value fail under exact current coverage.
- The later covering result postdates this record, so historical priority is not adjudicated.

## Disposition

**FAILED**
