# Independent mathematical audit — 2026-10-01

## Final claim assessed

Exact ideal profile for differences of bounded graph projections

## Correctness — PASS

PASS. The canonical graph and graph-complement isometries give the stated cross operators, and \((P_A-P_B)^2\) is block diagonal relative to the graph and its orthogonal complement. Positive functional calculus yields the modulus decomposition. A fresh finite-dimensional reconstruction for rectangular graph maps reproduced the complete singular-value multiset. The rank, Schatten, essential-norm, and compact-Fredholm consequences then follow.

## Originality — FAIL

FAIL. The result is mechanically implied by standard two-projection theory plus the standard bounded graph map. Classical principal-angle theory already gives the singular-value profile of \(P-Q\), including doubled nontrivial sine angles, while Andruchow's graph-map framework supplies the normalized graph coordinates and Schatten setting. The key formula is the elementary universal block identity for \((P-Q)^2\) followed by a one-line graph-coordinate calculation. Under the required implication standard this is a routine specialization, not an original theorem.

### equivalent_formulations

Searches: difference of two orthogonal projections singular values principal angles graph subspaces; Andruchow 2015 graph map Schatten projections

Evidence: The known principal-angle theorem gives the singular values of \(P-Q\) with doubled nontrivial sine values; Andruchow supplies the graph map.

Reasoning: The audited modulus formula is the graph-coordinate form of standard two-subspace geometry.

### broader_coverage

Searches: DOI 10.1016/j.laa.2009.11.002; DOI 10.1016/j.laa.2014.10.029; Kaur--Lui 2023 Theorem 2.2

Evidence: Two-projection theory already organizes the difference by principal angles; the graph map is classical.

Reasoning: These ingredients mechanically dominate the claimed ideal profile.

### exact_database_or_table

Searches: Published-record query for graph-projection Schatten profile

Evidence: No exact wording match was found, but exact wording is immaterial against decisive implication from standard theory.

Reasoning: Failed exact search is not used as novelty evidence.

### claim_vs_prior_implication

Searches: Andruchow graph-map Section 4; principal-angle theorem for two projections

Evidence: The standard diagonal compressions of \((P-Q)^2\) become exactly the two normalized graph-difference squares.

Reasoning: No nonstandard lemma remains after substitution.

## Scientific value — FAIL

FAIL. Once the standard two-projection decomposition and graph coordinates are recognized, the rank, singular-value, Schatten, and essential-norm statements are direct bookkeeping consequences. They are convenient formulas but do not clear the bar against textbook deductions and routine substitutions.

## Source inspections

- **Parametrizing projections with selfadjoint operators** — https://doi.org/10.1016/j.laa.2014.10.029. Material read: Primary full-text HTML, including the graph-map section. Assessment: DECISIVE_PRIOR_INGREDIENT. Evidence: It provides the standard graph projection coordinates and Schatten restricted setting.
- **New lower bounds on the minimum singular value of a matrix** — https://doi.org/10.1016/j.laa.2023.02.013. Material read: Relevant PDF text in Section 2.4, Theorem 2.2. Assessment: KNOWN_TWO_PROJECTION_SINGULAR_VALUE_PROFILE. Evidence: Theorem 2.2 restates the known singular values of \(P-Q\) through principal angles.
- **A gentle guide to the basics of two projections theory** — https://doi.org/10.1016/j.laa.2009.11.002. Material read: Bibliographic and scope material; full-text retrieval timed out. Assessment: BACKGROUND_WITH_ACCESS_LIMITATION. Evidence: The originality failure does not rely on a whole-document noncoverage claim.

## Limitations and residual risks

The formulas are correct for bounded operators, but the package is rejected as a routine specialization of established two-projection geometry. No claim is made for arbitrary unbounded graph operators.

- No access risk changes the failure because the implication can be reconstructed from standard formulas.
- The package remains potentially useful exposition despite failing originality/value.

## Disposition

**failed**
