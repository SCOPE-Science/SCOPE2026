# Review of the smallest leaf-optimal proper double star

## Correctness: PASS

The full PZF forcing rule is fixed explicitly. Conditioned on both hubs being blue, opposite-side leaf infection counts are independent binomials, yielding an exact two-index triangular first-step recurrence. With only one hub blue, the infect-opposite-hub Bernoulli and binomial new-leaf count give a second triangular recurrence; every nonterminal self-transition probability is below one. A pendant leaf performs one deterministic first round. These equations calculate all four source orbits exactly. The six possible proper double-star isomorphism types through nine vertices are enumerated exhaustively. The included Python checker uses exact rational arithmetic to verify all required strict comparisons and the \(D_{2,5}\) positive difference, and an independently written fully labeled infection-state solver reproduces all four rational values in five of the six graphs (including both nine-vertex graphs). The result makes no inference beyond the exhaustively classified range.

## Originality: PASS, qualified

Chan et al. (2019 preprint, 2020 journal), **Section 2.1** explicitly treats the symmetric \(D_{k,k}\) family and already reports the hub/leaf crossover at \(k=10\); that **previously known result is not part of the assessed new claim**. The assessed contribution is a different sharp cutoff: a leaf becomes uniquely optimal already at nine vertices within the full asymmetric proper double-star family, specifically \(D_{2,5}\). Their primary text supplies general Markov-chain machinery and balanced-double-star values but does not state or imply the six-type optimal-source comparison without additional exact computations. Geneson–Hogben's earlier path/cycle/star propagation work likewise does not imply this boundary. Published research-record searches for stochastic forcing on unbalanced double stars and equivalent optimal-source statements found deterministic-fort results but no exact nine-vertex PZF cutoff. Residual risk: independently checking all historical appendices or less visible graph-enumeration tables could reveal the same finite fact.

## Value: PASS

The ideal starting vertex for stochastic infection is a natural graph-probability invariant. Double stars are the complete diameter-three tree family, and the proper subclass excludes degenerate single-leaf arms. The result precisely locates the first failure of hub-only optimal seeding in that class and compares the two distinct nine-vertex types. Against the known balanced-double-star transition at 22 vertices, the sharp nine-vertex asymmetric obstruction explains a substantive source-placement effect of imbalance, not merely an arbitrary small parameter slice. No larger graph theorem is required for this natural complete first-failure classification to be useful.

## Closest sources and residual limits

- Geneson–Hogben, *Propagation time for probabilistic zero forcing*, arXiv:1812.10476 (December 24, 2018).
- Chan et al., *Using Markov Chains to Determine Expected Propagation Time for Probabilistic Zero Forcing*, arXiv:1906.11083 (June 25, 2019); published Electronic Journal of Linear Algebra 36 (2020), Section 2.1, https://emis.de/ft/34759 (balanced double stars covered).
- Deterministic and fractional zero-forcing classifications of double stars use non-equivalent dynamics.
- The result does not classify arbitrary trees or any proper double star of order greater than nine.

Self-review: passed. Independent audit: not yet performed.
