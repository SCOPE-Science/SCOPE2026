# Self-review

## Correctness — PASS

The model and quantifiers are explicit: every integer \(m\ge1\), every infection rate \(\lambda>0\), one initially infectious shared hub, unit recovery. The proof conditions on the hub's exponential infectious lifetime, derives the one-triangle probabilities including post-hub-recovery secondary transmission, then integrates an independent conditional product law. Conditional laws of large numbers and central limit theorems justify the limit. Rational moment expansions prove finite variances and the crossover polynomial. Descartes' rule and strict \(m\)-monotonicity prove uniqueness and the decreasing threshold sequence. An independent fully labeled finite-state Markov-chain calculation agrees with the formula in 12 exact parameter instances. Finite checks are supporting evidence, not the infinite proof.

## Originality — PASS (with explicit priority risk)

Closest sources: Fransson–Trapman (2018 arXiv/2019 journal) analyze clustered configuration-model random graphs via branching processes; their bounded-degree-regime final-size theorem does not imply the continuous limit on the deterministic, diverging-degree shared-hub graph. McCulloch–Roberts–Laing (2019) compute final-size distributions along a *line* of triangles, not the friendship graph's shared-hub variance comparison. Their 2016 paper already treats the single triangle; that particular calculation is not claimed as new. A full-text inspection of the 2019 line-of-triangles paper was unavailable, so stronger implicit coverage remains a residual risk. Searches of mathematical research records, general literature, and accessible own claims found no matching all-size variance threshold or implication that directly covers it. Search absence alone is not a novelty proof.

## Value — PASS

This compares the same vertex set before and after a canonical clustering operation (closing disjoint leaf pairs into triangles) in a stochastic epidemic with dependent transmissions. The **mean gain always has one sign**, whereas the **risk measured by final-size variance changes sign exactly once**, with a sharp threshold for *every* finite graph and a strictly decreasing sequence of thresholds. Exact finite distributions and the non-self-averaging infinite-size law explain the mechanism and provide reproducible benchmarks beyond a small numerical example.

## Scope and remaining limitations

The theorem does not handle nonexponential lifetimes, multiple initial infectives, varying rates, or general graph motifs. Independence of a human or external mathematical audit has not been established. The 2019 full text could not be inspected; the priority comparison is qualified accordingly.

Self-review: passed. Independent audit: not yet performed.
