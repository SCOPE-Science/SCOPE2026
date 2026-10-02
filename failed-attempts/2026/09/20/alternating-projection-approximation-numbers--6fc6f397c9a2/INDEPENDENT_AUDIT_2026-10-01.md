# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-6fc6f397c9a2`

## Correctness — PASS

The identity is correct. On Halmos' generic two-subspace block, \(PQ\) has row operator \((C^2,CS)\), so \((PQ)^n\) has row \((C^{2n},C^{2n-1}S)\) and modulus \(C^{2n-1}\). The intersection and the three other reducing summands vanish after subtracting \(R\). For a positive operator, approximation numbers transform monotonically under the power functional calculus, so \(a_k(C^{2n-1})=a_k(C)^{2n-1}\). Essential norm, compactness, finite rank, compact singular-value, and Schatten consequences follow exactly.

### Correctness sources

- assigned RESULT.md
- Halmos two-subspace canonical representation
- Andruchow–Corach 2017 singular-value geometry
- Kayalar–Weinert norm law

### Correctness risks

- The statement is specific to two orthogonal projections.

## Originality — FAIL

Under the required implication standard, the all-\(k\) law is covered as a routine corollary of the classical two-subspace canonical form and standard Hilbert-space \(s\)-number calculus. The canonical block explicitly identifies the one-step singular profile with the positive angle operator \(C\); powering the same block replaces it by \(C^{2n-1}\). No additional nonstandard lemma is needed. The 2017 primary product-of-projections paper independently documents the established singular-value geometry of \(PQ\). The fact that a source may not print the exact equation \(a_k(E_n)=a_k(E_1)^{2n-1}\) verbatim does not preserve originality when the equation is mechanically implied.

### equivalent_formulations

Searches:
- Resultary: two orthogonal projections approximation numbers powers Schatten
- classical two-projection canonical-angle/singular-value literature
- exact approximation-number power-law searches

Evidence:
- Only the audited record states the formula verbatim in the current corpus, but the canonical representation already determines the entire singular profile of every iterate.

Reasoning:
Equivalent formulations via principal-angle operators, singular values, approximation numbers, and Schatten exponents were compared.

### broader_coverage

Searches:
- Halmos two-subspace theorem
- Andruchow–Corach 2017 Schmidt-decomposable products
- Böttcher–Spitkovsky survey

Evidence:
- The established theory expresses \(PQ\) through the same angle operator and relates singular values directly to that operator.

Reasoning:
The audited formula is not stronger than the canonical decomposition plus monotone functional calculus; it is an immediate derived identity.

### exact_database_or_table

Searches:
- current Resultary projection-product records
- Schatten/essential-norm consequences

Evidence:
- No database lookup is needed because the all-scale profile is already fixed by the canonical operator representation.

Reasoning:
The corollaries are standard consequences of the same power identity.

### claim_vs_prior_implication

Searches:
- claim-to-canonical-form implication comparison

Evidence:
- On the generic block, the modulus of the nth error is exactly \(C^{2n-1}\), while the modulus of the first error is \(C\).

Reasoning:
The claimed approximation-number, essential-norm, compactness, rank, and Schatten laws all follow mechanically.

### source_inspections

- **Schmidt decomposable products of projections** — https://arxiv.org/abs/1706.05022. Trigger: Primary source on established singular-value geometry of products of two projections. Material read: Primary full PDF text around Theorems 2.2 and 2.4 and the singular-value/eigenvalue correspondence; screenshot retrieval was attempted but the remote PDF timed out. Method: Primary theorem comparison. Assessment: Supports prior canonical singular-value coverage. Evidence: The paper explicitly derives the singular values of \(PQ\) from the two-projection spectral data and treats compact/S-decomposable cases as established geometry.
- **A gentle guide to the basics of two projections theory** — https://doi.org/10.1016/j.laa.2009.11.002. Trigger: Broad canonical two-projection survey and principal residual coverage risk. Material read: Open-access retrieval was attempted but the available route failed; an authorized institutional request was then attempted and stopped when human verification was required. Method: Access attempt recorded without bypass. Assessment: Not relied upon for the originality failure; canonical coverage is already established by Halmos and accessible projection-product sources. Evidence: No whole-document NOT_COVERING inference was made.
- **Assigned alternating-projection proof** — assigned RESULT.md. Trigger: Exact all-k identity. Material read: Complete file. Method: Independent line-by-line proof reconstruction. Assessment: Correct but mechanically implied by the canonical block. Evidence: No step beyond the standard two-subspace block and positive-operator min-max calculus is needed.

### checked_sources

- Halmos 1969 two-subspace theorem
- Andruchow–Corach 2017 primary PDF
- Kayalar–Weinert 1988 norm law
- current Resultary exact search
- assigned RESULT.md

### residual_risks

- The broad Böttcher–Spitkovsky survey could not be fully retrieved because the authorized route required human verification; it was not retried or bypassed. This access issue does not affect the implication-based coverage finding.

## Scientific value — FAIL

The full approximation profile is a useful way to package the classical two-subspace calculus, but it is a textbook-level functional-calculus consequence of the canonical angle operator. The compactness, rank, essential-norm, and Schatten statements are likewise immediate once the modulus is \(C^{2n-1}\). Under the required value standard this does not constitute a new structural boundary or independently motivated invariant.

### Value sources

- Halmos canonical two-subspace representation
- standard Hilbert approximation-number calculus

### Value risks

- The result can still be pedagogically useful despite failing the new-finding value bar.

## Limitations

- Correctness passes.
- Originality and scientific value fail because the complete theorem is mechanically implied by classical canonical two-projection theory.
- The institutional full-text attempt for one broad survey required human verification and was not retried.

## Disposition

**FAILED**
