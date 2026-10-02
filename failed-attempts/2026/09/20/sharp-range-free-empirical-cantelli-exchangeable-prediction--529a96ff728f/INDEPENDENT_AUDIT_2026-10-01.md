# Independent mathematical audit — Sharp range-free empirical Cantelli bounds for exchangeable prediction

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **failed**.

## Correctness

**PASS** — The leave-one-out algebra exactly transforms the externally studentized residual into a monotone threshold on the full-sample standardized coordinate. Conditional on an exchangeable orbit, the held-out coordinate is uniform among all coordinates. The finite-vector one-sided Cantelli count therefore gives the stated integer staircase, and two-level vectors realize the inclusive and strict integer bounds. The zero-variance convention correctly handles the single-high-coordinate endpoint.

## Originality

**FAIL** — The final tail theorem is already a direct corollary of published ingredients in Troffaes–Basu 2019. Their Lemma 5 gives the exact identities relating the training mean/variance residual to the full-sample standardized coordinate, and their Lemma 7 gives the needed one-sided finite-vector Cantelli count. Solving the Lemma 5 identity for the residual threshold and inserting it into Lemma 7 yields the audited staircase formula. The fact that the paper's main theorem instead introduces a range offset does not undo this implication under the audit rule that unstated corollaries are covered.

### Equivalent formulations

Searches/sources: Troffaes–Basu 2019 full PDF, Lemma 5 equations (57)–(58) and Lemma 7; Saw–Yang–Mo 1984 empirical Chebyshev result; Resultary semantic query: exchangeable externally studentized prediction residual exact Cantelli staircase.

Evidence: Troffaes–Basu Lemma 5 gives the exact leave-one-out/full-sample mean-variance identities used by the audited proof. Their Lemma 7 is the same one-sided count inequality on zero-sum, fixed-square-sum standardized coordinates. The current Resultary record is the exact published finding, but the mathematical implication predates it.

The audited deterministic reduction does not add a new theorem-level ingredient beyond combining these published lemmas and simplifying the threshold.

### Broader coverage

Searches/sources: Troffaes–Basu 2019 Sections 3–5; Saw–Yang–Mo 1984 exchangeable empirical Chebyshev theorem.

Evidence: Troffaes–Basu's paper is broader in presenting the exact algebra and both one- and two-sided counting machinery, although its stated Cantelli theorem uses an additional range offset.

Published lemmas already contain the exact data needed to derive the range-free external-residual statement.

### Exact database or table

Searches/sources: Resultary exact/semantic search for the staircase formula; Konijn 1987 distribution-free prediction interval source.

Evidence: No earlier exact Resultary title was found. Konijn full text remained unavailable despite authorized retrieval attempts; this uncertainty is not needed for the failure because Troffaes–Basu is decisive.

The absence of an exact-title match does not establish originality when a prior paper already implies the claim.

### Claim versus prior implication

Searches/sources: Substitute Troffaes–Basu Lemma 5 into Lemma 7; derive the current threshold from equations (57)–(58).

Evidence: Equations (57)–(58) give the full-sample standardized coordinate as an exact monotone function of the external residual. Lemma 7 supplies the sharp integer one-sided count at any fixed standardized threshold. Two-level equality vectors are the standard equality construction for this finite Cantelli count.

The final probability bound is mechanically implied. The strict/inclusive staircase distinction and finite-orbit witnesses are routine integer/equality refinements of the same implication.

### Source inspections

- **A Cantelli-Type Inequality for Constructing Non-Parametric P-Boxes Based on Exchangeability** — DECISIVE_IMPLICATION_COVERAGE.
  Identifier: https://proceedings.mlr.press/v103/troffaes19a.html
  Trigger: same exchangeable sample mean/standard deviation and one-sided p-box problem
  Material read: complete eight-page PMLR PDF, including Lemma 5, Lemma 7, Theorem 6 and discussion
  Method: lawful open-access full text
  Evidence: The published identities and one-sided count lemma mechanically yield the audited range-free external-residual staircase, even though the authors' stated theorem adds an offset.
- **Chebyshev Inequality with Estimated Mean and Variance** — FOUNDATIONAL_PRIOR.
  Identifier: https://doi.org/10.1080/00031305.1984.10483182
  Trigger: foundational exchangeable empirical studentization result
  Material read: abstract and the formulas as reproduced in Troffaes–Basu
  Method: lawful public material plus later full-text reproduction
  Evidence: Troffaes–Basu states that equations (57)–(58) are also in Saw et al.
- **Distribution-Free and Other Prediction Intervals** — ACCESS_RISK.
  Identifier: https://doi.org/10.1080/00031305.1987.10475433
  Trigger: plausible older prediction-interval source
  Material read: bibliographic material; open access failed and authorized retrieval remained queued without verified text
  Method: open web plus authorized institutional attempt
  Evidence: No conclusion about its full contents is used in the rejection.

Residual originality risks:
- None identified.

## Scientific value

**FAIL** — Once the published leave-one-out identities and one-sided count lemma are treated as prior, the remaining work is threshold algebra, integer rounding, and the standard two-level equality construction. Under the stated value bar that residual is a routine corollary rather than a distinct motivated mathematical contribution.

## Final assessment

The package is scientifically rejected because the final claim does not pass all three C/O/V axes. Correct mathematical material is retained as failed evidence; no disclaimer can convert implication-covered work into a passing claim.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
