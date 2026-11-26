# Independent mathematical audit

## correctness

PASS

The common return cancels in the payoff comparison; a defector copying cooperator j uses p_j, while cooperator i copying a defector uses q_i. A reset contributes u to any specified flip. This gives the stated hypercube kernel; every flip and self-loop has positive probability. On the square missing only i and j at its bottom, the common first addition, the removals from the full set, and common factors cancel to give the stated ratio. Its two factors have the same strict comparison sign because q=1-p, so Kolmogorov's criterion rules out reversibility for any unequal pair. For equal p, the reciprocal edge weights depend only on level and the stated product recursion satisfies detailed balance on every edge. At fixed mutation rate with N=2, influx to each singleton equals u times the mass of the two consensus states and outflux is (2u+v) times the singleton mass, whence the common singleton probability u/(4u+v). The two consensus balances give the displayed probabilities and J=uv(p_1-p_2)/(2(4u+v)). Conservation fixes the same signed flux on all four edges; the stationary probabilities cancel around the cycle in the log ratio for entropy production. The homogeneous model at the mean p is admissible and has that same snapshot law with zero current. An independent exact solve that builds transitions directly from focal and model payoff comparisons tested 12 kernels for N=2,3,4, including the stated pair of examples; see /workspace/reproductions/frozen-check-3.txt and replay with python3 /workspace/reproductions/frozen_checks.py 3.

## originality

PASS

The linear public-goods instance is already in Foster–Knight–Krapohl with the same Fermi-plus-fair-reset probability law, not merely an absorbing imitation antecedent. The source gives the transition formula, payoff domination and a bound on mean cooperation. The checked results do not establish the exact reversibility threshold or the equality of the full labeled stationary distribution across models with different time reversal. Neither the standard finite-chain cycle criterion nor the prior mean bound substitutes for the chosen square and the two-player contrast calculation.

## value

PASS

An exact necessary-and-sufficient criterion over all finite population sizes is stronger than inferring reversibility from a stationary average. The two-player formula supplies an explicit identifiability obstruction even when snapshots resolve every labeled state: matching the acceptance sum hides heterogeneity, but the signed trajectory current exposes it. The example is structural across the admissible two-player parameters, not a lone numerical coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
