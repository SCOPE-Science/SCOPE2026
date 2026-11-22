# Self-review

## Correctness — PASS

The selected first-hit positions stabilize almost surely and leave at most two exceptional indices. The stationary Markov ergodic theorem then computes the pathwise limit; the strong Markov property proves independence of the two next-symbol reference states. All four probabilities and the displayed moments were derived independently and checked with exact fractions on 81 positive rational transition pairs. Sixteen length-100000 generated trajectories matched the calculated random limit within 0.012. No simulation is treated as an infinite proof.

## Originality — PASS within inspected sources

The full relevant portions of Śpiewak (2026), particularly Definitions 1.1 and Theorems 1.2–1.3, concern generic smooth observables; the tie-dependent binary Markov limit is not asserted there. The previous Bernoulli four-value special case corresponds to \(a+b=1\) and does not imply the two-parameter dependent process or the first-hit strong Markov identity. Kennel–Buhl's 2003 *symbolic FNN* addresses a distinct partition diagnostic (verified from its original abstract). Targeted searches of relevant published scientific records and literature did not find this Markov law. The possibility of a differently named historical result remains.

## Mathematical value — PASS

The complete two-parameter classification isolates precisely how serial correlation changes the empirical FNN diagnostic, not just an algebraic substitution: \(a=b=s\) holds the stationary one-symbol law fixed while its FNN mean becomes \(2s(1-s)\), and the limit remains random except at \(s=1/2\). The independence of successors at the *two stopping-time first hits*, despite serial dependence in the source, is the structural reason for the finite-atom law. This gives a natural complete classification of the simplest genuinely correlated finite-memory source under a common practical tie convention.

## Scope and residual risks

The result is restricted to one-delay binary quantization, positive transitions and earliest-index ties. The generic smooth-observable results of the source and the different symbolic partition diagnostic cannot replace this statement. Incompletely indexed older terminology remains a priority risk, and other tie conventions can have different limiting laws.

Self-review: passed. Independent audit: not yet performed.
