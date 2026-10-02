# Fresh audit — SCOPE-20260910-045

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For the equation \(y\"\"-(z+1/z)y=0\) over \(\mathbb{C}(z)\), the Picard–Vessiot differential Galois group is \(\mathrm{SL}_2(\mathbb{C})\). The point \(z=0\) is regular singular, not irregular, so there are no Stokes matrices there.

## Correctness

**PASS** — The singularity analysis and Kovacic exclusions were reconstructed. At zero, \(z^2(z+1/z)=z^3+z\) is analytic and the Frobenius exponents are 0 and 1, with the exponent-0 recursion obstructed, giving a logarithmic second solution. At infinity the transformed coefficient has pole order 5, so the point is irregular. A rational Riccati solution is excluded by the valuation at infinity, a rational symmetric-square solution is excluded because its leading coefficient is proportional to \(2e+1\) for integral valuation exponent \(e\), and finite primitive Galois group is excluded by irregularity. These checks support \(G=\mathrm{SL}_2\).

Residual risk: The conclusion relies on the standard Kovacic classification and finite-group regular-singularity criterion; exact Stokes multipliers are not checked.

## Originality

**PASS** — Semantic search of published SCOPE/Resultary material returned this record as the exact operator match; nearby differential-Galois records concern different operators. General Kovacic references provide the decision framework but do not state this operator-specific singularity correction or group calculation. No stronger source found was seen to imply the exact statement without carrying out the operator calculation.

Residual risk: Best-of-knowledge originality only; an unindexed operator table could exist.

### Originality checks

**equivalent_formulations**

Searches: Resultary semantic query: deformed Airy z+1/z differential Galois SL2 regular singular zero; operator-specific web/literature search around Kovacic and deformed Airy.

Evidence: Resultary exact match: https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE045; M. F. Singer, Introduction to the Galois Theory of Linear Differential Equations, https://arxiv.org/abs/0712.4124.

Reasoning: The general theory explains how to decide the group but does not furnish this exact operator-specific conclusion.

**broader_coverage**

Searches: Kovacic classification and differential-Galois background; nearby SCOPE SL2 operator results.

Evidence: https://arxiv.org/abs/0712.4124.

Reasoning: The broad theory supplies a method, not an automatic theorem covering this coefficient without the displayed valuation and singularity computation.

**exact_database_or_table**

Searches: Resultary operator query; deformed Airy z+1/z exact group search.

Evidence: No independent exact operator table was located..

Reasoning: No exact external table for this coefficient was found in the sources inspected.

**claim_vs_prior_implication**

Searches: Kovacic framework and regular/irregular singularity criteria.

Evidence: The standard framework reduces the question to explicit cases but still requires the record-specific calculation..

Reasoning: Prior general theory does not alone state the operator result; the final calculation appears operator-specific.

### Source inspections

- **Assigned RESULT.md** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/045/RESULT.md. Trigger: Exact assigned claim and proof. Material read: Full theorem, local singularity argument, Kovacic eliminations, limitations. Method: direct file inspection. Assessment: SUPPORTS. Evidence: The displayed valuation and Frobenius arguments are internally coherent.
- **verify_kovacic.py** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/045/artifacts/verify_kovacic.py. Trigger: Critical finite checks. Material read: Full verifier source at the actual package path. Method: direct source inspection plus independent hand/Python reconstruction. Assessment: SUPPORTS. Evidence: The verifier encodes the stated Frobenius and valuation checks; its former output-prefixed path in prose is stale.
- **Introduction to the Galois Theory of Linear Differential Equations** — https://arxiv.org/abs/0712.4124. Trigger: General differential-Galois/Kovacic context. Material read: Relevant differential-Galois classification background. Method: primary-source inspection/search. Assessment: NOT_COVERING_EXACTLY. Evidence: Provides framework rather than this operator-specific result.
- **Resultary SCOPE045** — https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE045. Trigger: Exact-match novelty search. Material read: Title and summary returned by semantic search. Method: Resultary semantic search. Assessment: SELF_MATCH. Evidence: Exact published match is the assigned record itself.

## Value

**FAIL** — Although correct and apparently not duplicated verbatim, the final result is a routine application of standard singularity tests and the Kovacic decision framework to one ad hoc second-order operator. The correction that zero is regular singular is a local normalization/type check, and the record supplies neither exact Stokes data nor a motivated family theorem or reusable structural lemma. Under the shared value bar, correctness and novelty of this isolated calculation do not by themselves make it a worthwhile mathematical gap.

Residual risk: A future application that specifically requires this operator could change the value assessment, but none is established in the package or inspected literature.

## Overall disposition

**FAILED**
