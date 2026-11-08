# Scientific review of the coexistence transport theorem

## Correctness

PASS. The stationary source model establishes the two coexisting normalized spatial densities and the common flux equation. In the proposed proof, the spatial flux \(R(x)/v_0\) equals \(h\) times the radial survival probability; inverse flux gives explicit upper-tail quantile radii on the two branches. Their difference is a positive integral, exactly constant on the shared far-gas interval, which proves stochastic ordering and the sharp \(W_\infty\) result. An additional integration gives the stated \(W_1\) formula. Strict negativity of the second derivative of the endpoint integral reduces uniqueness of the maximal contrast to one scalar sign, and the endpoint sign has one rigorous zero. The high-crowding limit follows from trapping the unique critical point near the root of \(1-\log h\). A standalone standard-library verifier passed 1,070 numerical consistency checks, including checks that start from the source's density rather than the quantile formula.

## Originality

PASS, qualified. The directly relevant October 19, 2026 source of Grange provides the full single-branch profiles, gas/droplet coexistence region and nonmonotone *droplet width*. These are explicitly attributed. The new statement compares the two coexisting laws in the stochastic order and \(W_\infty\) sense, identifies an exact outer-tail translation and proves a distinct crowding threshold for *transport gap optimization*. A literature and indexed-finding search found no statement of this exact paired-branch transport theorem. Ordinary monotone rearrangement is classical; it does not alone establish the model-specific profile comparison or threshold. Since the primary paper gives strong raw formulas from which the conclusion can be derived, publication priority remains qualified and independent literature review is still needed.

## Value

PASS. The supersaturated gas and dense-droplet states are two physically motivated competing steady descriptions at the same resetting rate. A direct, sharp measure of their complete spatial difference is valuable for assessing how large a single-particle displacement is needed to couple their profiles. Stochastic order guarantees the sign of every increasing radial observable, while the exact \(W_\infty\) gap measures a worst-case displacement across all quantiles. The threshold \(m_*=7.322227\ldots\) distinguishes when the strongest contrast occurs at the terminal coexistence boundary versus a strictly interior reset rate, which is not predictable from the known nonmonotonic droplet radius. The parameter is the original physical density-slowdown scale, not an arbitrary numerical slice.

## Closest literature and residual limits

Grange, arXiv:2610.26149v2, Sections 2–5 and Appendix B, is the closest scientific source. De Pascale–Louet, arXiv:1704.02730, provides general one-dimensional \(L^\infty\) transport context; Evans–Majumdar, arXiv:1808.06450, concerns noninteracting reset run-and-tumble motion; Cates–Tailleur, arXiv:1406.3533, gives general MIPS context. The proof assumes the published piecewise kinetic continuum model, symmetric stationary states, and \(1<h<m/4\). It does not imply simultaneous long-lived dynamical stability of both stationary solutions. The source's exact steady profiles constitute substantial prior coverage, and unindexed literature remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
