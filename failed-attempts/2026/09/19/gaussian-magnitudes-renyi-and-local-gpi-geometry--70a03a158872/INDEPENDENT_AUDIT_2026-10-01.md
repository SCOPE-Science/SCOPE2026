# Independent audit — SCOPE-20260919-70a03a158872

Audited: 2026-10-01 UTC.

Disposition: **failed**.

## Final claim

For fixed dimension and fixed positive exponents, the normalized Gaussian absolute product moment has quadratic doubled-edge coefficients and cubic signed-triangle coefficients near independence, yielding a local quadratic gap at independence.

## Correctness (C) — PASS

Expanding each normalized even function in probabilists’ Hermite polynomials gives a multigraph series. Parity eliminates odd vertex degrees; the only degree-two graph is a doubled edge and the only degree-three graph is a triangle. The identity \(h_2(\alpha)=\alpha\) therefore gives exactly the displayed coefficients. Analytic dependence on the correlation matrix in a positive-definite neighborhood makes the remaining terms \(O(\lVert E\rVert^4)\) in fixed dimension. The positive quadratic form then dominates the cubic and higher terms on a sufficiently small neighborhood, proving the stated local gap. The committed Wick and bivariate checks are consistent but are not used as proof.

**Sources checked.** assigned RESULT.md and verifier blobs at the audited tree; Ogasawara’s general Gaussian product absolute-moment series as a cross-check of the same moment object

**Risks / limits.** The constant in the local neighborhood is existential and dimension/exponent dependent, exactly as stated.

## Originality (O) — FAIL

Ogasawara’s pre-existing general \(n\)-variate series explicitly covers central untruncated Gaussian cross-product absolute moments of arbitrary real-valued orders as functions of the full correlation matrix. The audited formula is the degree-two and degree-three Taylor extraction from that broader series; the local lower bound is then the routine consequence of the positive quadratic leading term. Under implication-based originality, a coefficient extraction from an already published general series is covered even though the exact signed-triangle sentence is not separately highlighted.

**Sources checked.** H. Ogasawara, Series formulas for the untruncated Gaussian product moments, Behaviormetrika, DOI 10.1007/s41237-025-00277-2; full preprint text inspected; Resultary semantic search for the signed-triangle absolute-moment expansion; published SCOPE records on Gaussian-magnitude Rényi dependence for scope separation

**Risks / limits.** The recent strong-GPI preprint arXiv:2609.20234 was not available in full text through the lawful routes tried, but this does not affect the decisive broader-series coverage.

## Value (V) — FAIL

The signed-triangle interpretation is lucid, but after the general Gaussian absolute-moment series is credited, the surviving work is only the first two nonzero Taylor layers plus a standard small-neighborhood domination argument. That is a routine coefficient extraction rather than a separately motivated mathematical gap under the required value bar.

**Sources checked.** same Ogasawara series and the audited derivation

**Risks / limits.** None material beyond the stated scope.

## Originality comparison

**Equivalent formulations.** The Hermite multigraph expansion and Ogasawara’s general central GPAM series are two representations of the same normalized Gaussian absolute product moments near the identity correlation matrix.

**Broader coverage.** Ogasawara gives a general \(n\)-variate infinite-series formula for the whole moment as the correlation matrix varies; the audited quadratic and cubic terms are contained in that broader object.

**Exact database or table checks.**

- Resultary: Gaussian absolute product moments local Hermite expansion signed triangle correlation — The audited record ranked first; related SCOPE hits concerned Rényi magnitudes rather than a distinct prior signed-triangle theorem.

- primary-literature web search: Series formulas for the untruncated Gaussian product moments absolute moments — Located Ogasawara’s published article and author-posted full preprint covering general central n-variate GPAMs.

**Claim versus prior implication.** The general series determines every Taylor coefficient at independence. Extracting the doubled-edge and triangle coefficients, and then observing local positivity from the quadratic term, is logically implied by that prior formula plus elementary expansion.

## Source inspections

- Ogasawara full preprint text: abstract, general n-variate GPAM section, and central untruncated corollary inspected.

- Assigned RESULT.md, METADATA.json, AUDIT.json, VERIFICATION.md, verifier source and verifier output inspected from the frozen Git tree.

- Resultary semantic results and earlier Gaussian-magnitude SCOPE records inspected for overlapping formulations.

## Residual risks

- Full text of arXiv:2609.20234 was unavailable, but the originality rejection already follows from older broad GPAM coverage.

## Scope boundary

Scientific rejection is on originality and value, not correctness. The package evidence is retained; no claim is made that the local expansion is false.
