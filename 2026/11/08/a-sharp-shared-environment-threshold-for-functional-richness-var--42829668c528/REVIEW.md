# Scientific review

## Correctness — PASS

The theorem is exactly quantified for \(g\ge2\), \(p\in(0,1)\), and \(\theta>0\). The conditional Beta moment calculation gives equation (1), algebraic differentiation gives equation (2), and the coefficient-sign proof in RESULT.md shows at most one positive zero using concavity of specific quadratics and Descartes' rule; the endpoint signs give exactly one when \(p<(g+5)/(12g)\). The proof handles equality at the phase boundary. The included exact checker separately enumerates survival configurations using Beta-binomial probabilities, verifies the symbolic differentiation identity, and checks the rational example. The checker is corroboration, not a substitute for the uniform analytic proof.

## Originality — PASS within inspected evidence, provisional

The closely related ecological mechanisms—functional redundancy under random extinctions, beta-distributed environmental survival and correlated food-web responses—are all established in primary sources. Fonseca and Ganade's full readable article develops fixed-count random extinction and a rarefaction variance, not a shared-Beta parameter phase diagram. Kaneryd and collaborators' full readable article employs correlated stochastic environmental growth in dynamical food webs and reports simulation responses, not the present closed-form one-peak law. Kendall's readable article abstract and source details establish use of Beta survival heterogeneity but concern likelihood-based estimation rather than guild-count uncertainty; the full mathematical text was not established as accessible and is a residual risk. Own earlier ecology records address either independently surviving species or fixed-budget random survivors; a separate earlier group-testing record uses a Beta latent variable for a different statistic. Semantic record searches returned no direct theorem, but indexing cannot certify uniqueness. An uninspected broader theorem for a general infinitely exchangeable binary model could, in principle, subsume the result. Priority remains provisional pending an independent literature review.

## Value — PASS

The result resolves a substantive exact risk-order question: whether more synchrony in species survival necessarily increases uncertainty in ecosystem functional richness. A whole infinite class of ecologically interpretable two-partner redundancies exhibits an exact, group-number-dependent threshold, and for rare mean survival there is exactly one interior worst-correlation regime. It separates correlated environmental stochasticity from independent demographic survival and gives a simple quantitative parameter boundary usable as a benchmark for simulation and interpretation. This is more than a numerical example or a routine end-point comparison.

## Sources and limitations

Kendall (1998), https://doi.org/10.1890/1051-0761(1998)008[0184:ETMOES]2.0.CO;2; Fonseca and Ganade (2001), https://doi.org/10.1046/j.1365-2745.2001.00528.x; Kaneryd et al. (2012), https://doi.org/10.1002/ece3.218. Model limitations and the historical priority risk are explained in RESULT.md. No independent scientific validation is claimed.

Self-review: passed. Independent audit: not yet performed.
