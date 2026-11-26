# Independent mathematical audit

## correctness

PASS

Fix the walk horizon k and a test on the finite score lattice. Write the signed-graph conditional expectation as the ratio of root averages of the tilted test expectation and the tilt weight. Conditional on the unsigned graph, only O(n) ordered pairs of radius-(k+1) root neighborhoods share signs, so the conditional variance of each bounded root average is O(1/n). The conditional numerator mean agrees with the tree mean up to a constant times the fraction of roots without a tree neighborhood, which tends to zero in probability by fixed-radius local convergence; the denominator mean is exactly [p exp(−β)+(1−p)exp(β)]^d and positive. Thus the ratio converges in probability, not only after averaging over graphs. On the tree the tilt changes precisely the d root-incident signs independently to parameter q. At distances zero, one and at least two the score laws are A0, A1 and A∞. The odd-time mass at distance one is d times the following even-time return mass u_m; no other tilted component is possible at either parity. The mean identity follows by counting tilted signs in expectation. For a convex test let h(j) be its expected value with j of d signs tilted. Two replacements give Δ²h(j)=(p−q)² times the expectation of the second difference of the test at W−2,W,W+2, where W uses the remaining j tilted signs. The even-minus-odd expectation is u_m[h(d)+(d−1)h(0)−dh(1)], nonnegative and strictly positive for a strictly convex test; neither direction of first-order dominance is possible at equal means with distinct laws. For the quadratic test the second difference is 8, giving gap 4d(d−1)u_m(p−q)². The Catalan first-return counts, divided by d^(2j), give the asserted renewal generating function. At ρ=d²/[4(d−1)] its square-root coefficient is −2d(d−1)/(d−2)²; on the principal branch the denominator does not vanish and transfer yields the stated positive m^(-3/2) prefactor. The example at d=3 and m=1 matches exactly; when β=0 or p is deterministic the mixtures coincide. The large-time asymptotic is subsequent to the fixed-time graph limit.

## originality

PASS

The same marked tree and exponential sampling tilt, and the exact return-count component, are prior mathematics. The new claim is the realized-score marginal law and strict spread comparison between paired adjacent times, not the stochastic comparison to time zero, the law of a root-wise mean bias, or the walk return law alone. The closest inspected results do not cover that combined claim; priority remains bounded.

## value

PASS

A start-versus-future sampling theorem leaves open what happens between successive positive times. This result shows a systematic, not exceptional, distinction: the odd and following even limiting scores share a mean but are stochastically incomparable, with the even score strictly more dispersed in convex order. The exact mixture laws and return-controlled spread quantify that phenomenon for all nondegenerate parameters in the model. It is not a finite-graph coupling or a joint time-and-size limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
