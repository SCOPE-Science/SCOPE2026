# Mathematical audit — 2026-10-01

## Final claim assessed

Critical algebraic decay and logarithmic correction at the Ricker flip threshold

## Correctness — PASS

PASS. The endpoint global convergence is correct and is independently documented in the one-dimensional Ricker literature via Coppel's theorem. Direct series composition gives \(G(u)=u-\frac43u^3+\frac{8}{15}u^5+\frac49u^6+O(u^7)\). Expanding reciprocal square yields the two-step increment \(\frac83+\frac{64}{15}u^2-\frac89u^3+O(u^4)\); summation gives the \(\frac85\log n\) term and the leading \(\sqrt3/2\) amplitude. The finite-hit exceptional set statement is also correct.

## Originality — FAIL

FAIL. The global basin statement at \(r=2\) is established prior Ricker theory. The remaining local asymptotic is a direct specialization of classical parabolic-germ/Fatou-coordinate theory: a codimension-\(k\) tangent-to-identity germ has a rectifying coordinate with a leading inverse \(k\)-th power and a logarithmic term whose coefficient is the iterative residue. The Ricker second iterate is a codimension-two parabolic germ; substituting its printed Taylor coefficients into that standard normal form yields the same inverse-square plus logarithmic expansion. Under the required implication standard, the model-specific constants do not create an original theorem merely because they were not located verbatim in Ricker papers.

### equivalent_formulations

Searches: Resultary: Ricker map r=2 critical algebraic decay logarithmic correction reciprocal square; Cambridge primary source on parabolic germs, rectifying/Fatou coordinate and iterative residue

Evidence: Classical parabolic normal form expresses the rectifying coordinate as an inverse-power term plus an iterative-residue multiple of \(\log z\).

Reasoning: The reciprocal-square Ricker asymptotic is the real attracting-petal form of this standard codimension-two Fatou-coordinate expansion.

### broader_coverage

Searches: Analytic classification of germs of parabolic antiholomorphic diffeomorphisms of codimension k, Section 4; Ricker global stability at r=2 via Coppel

Evidence: The parabolic source states the general normal form and time coordinate \(-1/(kz^k)+b\log z+\text{constant}\); the Ricker source states global convergence through the endpoint.

Reasoning: Together these cover the two ingredients of the package: basin-wide convergence and the local inverse-power/logarithmic iteration law.

### exact_database_or_table

Searches: Resultary semantic search for the exact Ricker coefficient

Evidence: The assigned record is the exact textual hit, but exact textual absence is not novelty when a general theorem mechanically yields the coefficient after substitution.

Reasoning: No database is relevant; implication from a stronger general theorem is decisive.

### claim_vs_prior_implication

Searches: general codimension-two parabolic Fatou coordinate versus Ricker second-iterate Taylor series; 2017 Ricker global-stability statement

Evidence: The package's own second-iterate coefficients determine the standard parabolic iterative residue, while global attraction is prior work.

Reasoning: No independent structural ingredient remains after applying established general parabolic iteration theory.

## Scientific value — FAIL

FAIL. Once the known global convergence at \(r=2\) is combined with standard parabolic iteration theory, the advertised critical decay and logarithmic correction reduce to evaluating the generic formal invariant for one explicit map. The computation is clean and reproducible but is a routine specialization rather than a separately motivated mathematical gap under the stated value bar.

## Source inspections

- **Analytic classification of germs of parabolic antiholomorphic diffeomorphisms of codimension k** — https://doi.org/10.1017/etds.2020.105. Material read: Primary full HTML around the formal normal form and Section 4. The time coordinate is displayed as \(-1/(kz^k)+b\log z+\text{constant}\), with \(b\) identified as the formal iterative residue. Assessment: DECISIVE_GENERAL_PRIOR_THEORY. Evidence: It gives the inverse-power plus logarithmic rectifying coordinate for arbitrary parabolic codimension, of which the Ricker second iterate is a codimension-two specialization.
- **Local Stability in 3D Discrete Dynamical Systems: Application to a Ricker Competition Model** — https://doi.org/10.1155/2017/6186354. Material read: Primary full-text section stating that for the one-dimensional Ricker equation the positive fixed point is globally stable for \(0<r\le2\), using Coppel's theorem. Assessment: DIRECT_PRIOR_GLOBAL_BASIN_COVERAGE. Evidence: The package's global convergence at \(r=2\) is prior work.

## Checked sources

- Complete assigned Git package and exact symbolic expansion artifacts.
- Independent series/recriprocal-square coefficient reconstruction.
- Primary full-text parabolic normal-form source and Ricker global-stability source.
- Resultary exact search.

## Limitations and residual risks

The calculation is correct for the deterministic one-dimensional Ricker map at \(r=2\), but it is preserved as a failed novelty/value attempt rather than a validated new finding.

- No bibliographic risk changes the failure: the rejection rests on a general classical mechanism plus prior global stability, not on failure to find the exact constants in model-specific literature.

## Disposition

**failed**
