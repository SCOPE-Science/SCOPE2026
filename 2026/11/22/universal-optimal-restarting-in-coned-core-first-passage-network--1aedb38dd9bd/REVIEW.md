# Scientific review: coned-core optimal resetting

## Correctness — PASS

The full hitting-time-law invariance follows from strong lumpability: every nongateway core vertex escapes to the gateway at unit rate, irrespective of its internal edges. The four backward equations are explicitly given in `RESULT.md`. The symbolic derivative reduces to a quartic with one positive root by Descartes' rule, and its simple limiting root gives the sharp optimizer and mean expansions. The independent full-generator checker passed 96 exact-rational comparisons, including nonzero Laplace transforms. This checks finite instances without mistaking finite tests for the infinite proof.

## Originality — PASS on examined evidence

Full publicly available source text of Evans–Majumdar (2011), Reuveni (2015/2016), Pal–Reuveni (2016) and Riascos et al. (2019/2020) was compared. Their general renewal and network spectral frameworks can reproduce model-specific calculations after specialization, but none states a coned-core hitting-law invariance plus the unique universal reset optimizer and its first-size corrections. Related published index records concern resets at a different vertex (clique gateway), initial leaf on two-hub trees, or an apex with competing targets. These differing initial/reset locations change the model. Repository full texts for the closest indexed records could not be inspected, so undetected stronger results remain a residual historical-priority risk. Detailed comparisons and searches appear in `AUDIT.json`.

## Mathematical value — PASS

The finding resolves a natural random-search design problem for an infinite graph family whose internal edge density ranges from zero to complete. The entire absorption-time law is invariant under arbitrary internal rewiring, while one optimized resetting rate bounds the mean despite a linearly increasing unrestarted mean. The limiting rate \(\sqrt2\), minimum \(4+2\sqrt2\), and finite-size corrections quantify a structural transport effect not supplied by generic restart identities alone. The graph geometry and observable are motivated by the contrast between long excursions into an increasingly large trap and a fixed-distance absorbing target; these are not arbitrary numerical slices.

## Scope and limitations

Unit rate per edge, fixed universal gateway, three-edge tail, one absorbing endpoint, instantaneous reset to the tail's first vertex, \(m\ge3\). This is not the degree-normalized random-walk model and does not optimize over all restart distributions. Historical priority is provisional and independent external scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
