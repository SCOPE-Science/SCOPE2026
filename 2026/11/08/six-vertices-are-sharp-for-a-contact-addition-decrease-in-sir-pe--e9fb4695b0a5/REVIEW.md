# Scientific review

## Correctness — PASS

For disjoint susceptible and infectious sets, the exact first-event recurrence follows from independent exponential clocks and decreases the integer \(2|S|+|I|\) strictly. Complete simple-graph generation up to five vertices and permutation-based isomorphism canonicalization give connected graph class counts \(1,2,6,21\). All \(1738\) edge-addition/seed/peak-threshold comparisons were symbolically reduced; every nonzero difference has numerator and denominator with nonnegative coefficients and strictly positive values at \(\beta=1\), proving the sign for every \(\beta>0\). The exact six-site rational witness is reproduced by two different recursions. A finite enumeration is used only for the finite small-graph assertion, not extrapolated to larger graphs.

## Originality — PASS (subject to historical-priority risk)

Focused literature searches and four primary full-text comparisons revealed no dominating claim. Van Mieghem (2014) studies mean prevalence maxima; Economou et al. (2015) compute SIS maximum prevalence and discuss a possible SIR extension; Holme (2013) studies discrete-time extinction time; Holme (2017) works on expected final size, vaccination and sentinel timing for small graphs. These results share methods or model components but do not imply the all-positive-rate SIR peak-edge inequality or its six-vertex counterexample. Equivalence, broader coverage and exact table checks, with precise source reading and remaining risks, appear in `AUDIT.json`. Unindexed literature may affect priority.

## Value — PASS

The exact minimum network order is a natural structural invariant for a capacity-overload decision. The theorem separates pathwise concurrent infection risk from mean peak prevalence and final size; it gives an exact benchmark for stochastic network interventions. The witness decrease is small and at a particular rate, but the five-vertex theorem is uniform over all positive rates, all missing contacts and every peak target. No claim is made about empirical contact tracing or public-health recommendations.

## Scientific limitations

Only simple undirected connected unweighted graphs, one initial infectious site, homogeneous exponential infection/recovery, and one edge addition are covered. The exhaustive certification is limited to graph orders at most five, the counterexample to one six-vertex graph. All computations are reproducible from the accompanying source and do not constitute independent validation.

Self-review: passed. Independent audit: not yet performed.
