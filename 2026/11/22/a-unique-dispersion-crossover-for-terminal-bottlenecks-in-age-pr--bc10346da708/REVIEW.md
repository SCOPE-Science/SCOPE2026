# Scientific review: terminal-bottleneck count dispersion

## Correctness — PASS

The statement specifies the full infinite-horizon cut event, the independent truncated-geometric parent law, fixed \(m\) and \(q\) for the Gaussian limit, and a separate large-\(m\) root expansion. The one-cut and two-cut probabilities follow from finite products and conditional restarting. The two-sided geometric-lag coupling has finite second-moment total mismatch; its stationary cut-indicator process is exponentially strongly mixing because a future edge returning across a distant boundary has geometrically small probability. The standard bounded-variable strong-mixing CLT therefore applies. The absolutely convergent two-cut covariance sum gives the variance constant. Monotonicity of the infinite product and series proves a single dispersion crossing, and uniform small-\(q\), large-\(m\) expansions yield the second-order root location. The standalone exact checker returned 598 passing rational assertions; those computations are auxiliary rather than an infinite proof.

## Originality — PASS with priority limitations

The motivating 2026 manuscript defines the multi-parent age-preferential graph, its terminal bottlenecks and the renewal mechanism. An accessible previously published mathematical finding determines the bottleneck one-point probabilities and finite-window two-point probabilities, and establishes a fixed-parent weak-bias Poisson point-process limit. These exact identities are incorporated as prior inputs, not presented as new. The classic renewal/strong-mixing CLT also supplies standard asymptotic-normal machinery. The new assessed conclusion is the explicitly classified fixed-bias count dispersion, the **unique** frontier and the two-term large-parent frontier asymptotic. These results are not the fixed-parent rare-bias Poisson statement; no searched record directly stated the same dispersion phase diagram. Because exact prior pair identities supply most of the algebraic inputs, unindexed pre-existing deductions remain a material priority risk.

## Value — PASS

The mean count alone cannot tell whether terminal bottlenecks are more or less variable than a Poisson count with the same mean. The classification identifies when the count changes from under- to over-dispersion in a graph with strongly dependent local cuts, and exactly how increasing parallel parent multiplicity moves the boundary. This is a natural quantitative statistic for the regenerative bottlenecks used in recurrence analysis, not an arbitrarily selected graph slice. The second-order large-parent expansion resolves the transition in a regime not addressed by the fixed-parent weak-bias Poisson limit.

## Closest work and limits

1. Tang, Wang and Wu, *Random Walk on age-preferential random growth processes*, arXiv:2611.02329 (2026): construction, renewal and recurrence, rather than the fixed-bias dispersion frontier.
2. *Poisson activation of terminal bottlenecks in weakly age-biased recursive trees* (public mathematical result): exact finite-start cut probability and truncated pair identity, plus Poisson activation as bias vanishes for fixed parent multiplicity. Closest computational and conceptual precursor; the new variance coefficient follows by summation of its known pair identities, whereas the sharp sign classification and large-parent expansion are further calculations.
3. Aguech et al., *Exponentially preferential trees* (2025): vertex-degree laws for the single-parent model; no terminal cut-dispersion statement located in the inspected article.

The claims do not cover variable bias with growing sample size, simultaneous parent/sample-size CLTs, or online cut detection. Independent mathematical review has not been performed. Unindexed relevant literature could change the originality assessment.

Self-review: passed. Independent audit: not yet performed.
