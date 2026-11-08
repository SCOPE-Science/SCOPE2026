# Review of the three-plant pollination-reliability theorem

## Correctness — PASS

The event that all three plants retain at least one pollinator is evaluated by three-event inclusion–exclusion. With the union constrained to \(3d-2s\), the excess-incidence identity \(2t+\sum b_{ij}=2s\) is exact. For fixed triple intersection \(t\), strict convexity of exponential pair terms forces overlap concentration; strict convexity of the resulting one-variable envelope forces one of two endpoint designs. Both endpoints exist for \(d\ge2s\), and subtraction gives \(q^{2d-2s}(1-q^s)(1-2q^s)\). All equality cases are covered. The standard-library checker additionally enumerates 93,354 admissible labeled neighborhood triples across three finite parameter choices and passes 87 exact assertions. Numerical or finite enumeration evidence is corroborative and is not used to justify the infinite-parameter proof.

## Originality — PASS within the inspected evidence, with residual risk

Bascompte et al. (2003) study observed mutualistic nestedness rather than optimizing Bernoulli all-plant joint persistence over fixed-degree incidences. Memmott et al. (2004) introduce the relevant last-pollinator-loss ecological criterion and evaluate extinction sequences empirically; the inspected full paper does not state a sharp structural optimization for three identical plant degrees. Bane et al. (2018) study extinction-order robustness measures on empirical networks, not this joint endpoint. Fishburn et al. (1986) study a related biased-set event under pairwise-intersection family constraints, but the accessible abstract neither states nor implies the fixed-union three-set extremum with a disjoint module; full-text comparison remains a risk because the source was inaccessible. No matching direct statement appeared in searched literature or mathematical-result records. Absence of a match is not proof of novelty, and broader reliability/set-family coverage may remain.

## Value — PASS

Degree and pollinator-count controls leave every plant's support probability, expected supported species count, and probability of any support unchanged. Yet optimal joint persistence undergoes a unique, analytically sharp transition between disconnected paired modules and a connected common core. This isolates a high-order network effect of ecological relevance that ordinary species-richness summaries conceal. The theorem supplies a complete global optimizer classification for every \(d\ge2s\ge2\), not merely two hand-picked graphs. Its scope is a simplified instantaneous independent-loss model; connectivity or ecological dynamical constraints may alter the result.

## Residual limitations

The novelty assessment is provisional, especially for unavailable full-text extremal set-system literature. No independent theorem review has occurred. The paired-module solution is disconnected, the biological failure model is static and homogeneous, and the result is not a field recommendation.

Self-review: passed. Independent audit: not yet performed.
