# Independent audit — 2026-10-01

**Record:** `SCOPE-20260911-039`

## Correctness — PASS

Fresh exact matrix arithmetic verifies the counterexample. With the standard two-by-two representation, the half-twist image squares to minus the identity, gamma=sigma1 sigma2^{-1} has trace 3 and determinant 1, and beta*=gamma Delta^2 has trace -3 and determinant 1. Thus both have spectral radius (3+sqrt(5))/2. Abelianization gives exponent sum 0 for every power of gamma and 6 for beta*, proving the required non-conjugacy. Exact rational evaluation gives f(3)=-1, f(3.1)=16691/10000, and f(2.747)=-5549417340919/10^12; the derivative identity makes the largest root exceed 3.

## Originality — FAIL

The scientific implication is already mechanically forced by standard published structure: the full twist generates the center of B3 and disappears in the modular-group quotient, while the classical minimum-dilatation result identifies gamma=sigma1 sigma2^{-1}. Multiplying gamma by any nonzero central power therefore preserves the projective mapping class and dilatation while changing abelianization, producing non-conjugate central translates immediately. The displayed beta* is the first such translate, not a new mathematical phenomenon under the audit rule that counts direct corollaries as covered.

### Structured originality checks

- **equivalent_formulations:** Searches: B3 center Delta squared quotient PSL(2,Z); 3-braid minimum dilatation sigma1 sigma2 inverse. Evidence: Published sources identify Delta^2 as the central full twist and B3 modulo its center with PSL(2,Z). Lanneau-Thiffeault gives the n=3 minimum with polynomial X^2-3X+1 and braid sigma1 sigma2^{-1}. Reasoning: The counterexample is equivalently the observation that central translates represent the same projective modular element but distinct braid conjugacy classes detectable by exponent sum.
- **broader_coverage:** Searches: 3-braid center modular quotient; minimum dilatation 3-braids. Evidence: The prior results cover all central powers, not merely the single beta* used here. Reasoning: The standard center quotient plus the published minimizer strictly dominates the one-example statement.
- **exact_database_or_table:** Searches: published-result semantic search for central-twist counterexample; web search exact beta* central twist. Evidence: No separate exact beta* table row was needed because the broader structural implication is decisive. Reasoning: Absence of a verbatim record cannot restore originality when a general theorem immediately supplies an infinite family of the same counterexamples.
- **claim_vs_prior_implication:** Searches: full twist center B3; Lanneau Thiffeault Theorem 1.1 n=3. Evidence: Center quotient preserves the underlying punctured-disk mapping class; the minimizer is published. Reasoning: Taking one central translate and using abelianization to separate conjugacy is a short direct corollary of these standard facts.

## Scientific value — PASS

As a diagnosis of a malformed universal gap claim, the counterexample is useful: it identifies the missing need to control the central power or refine the invariant. That structural correction is mathematically motivated even though the result fails originality.

## Source inspections

- **Lanneau, Thiffeault, On the minimum dilatation of braids on punctured discs** (arXiv:1004.5344). Full HTML theorem statement and surrounding definitions. Assessment: COVERING_COMPONENT. The n=3 minimum is (3+sqrt(5))/2, with polynomial X^2-3X+1 and braid sigma1 sigma2^{-1}.
- **Tuba, Wenzl, Representations of the braid group B3 and of SL(2,Z)** (Pacific J. Math. 197 (2001)). Indexed article excerpt containing the central element and B3/Z identification. Assessment: COVERING_COMPONENT. States that the square of the half twist is central and identifies the modular quotient; combined with the minimum theorem, central translates yield the same projective class.

## Residual risks

- The scientific rejection is an originality rejection, not a correctness or access failure.
- The explicit beta* remains a useful diagnostic example even though the phenomenon is covered by standard center structure.

## Disposition

**FAILED**. The mathematical claim is retained as evidence, but it does not pass the originality requirement and is not validated as a publishable independent finding.
