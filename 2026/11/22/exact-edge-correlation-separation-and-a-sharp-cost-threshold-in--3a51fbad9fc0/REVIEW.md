# Independent mathematical audit

## correctness

PASS

The payoff subtracts two costs for a cooperative vertex and uses edge-dependent benefits received from neighbors. The transition law uses pre-replacement competitor fitness, which is strictly positive on 0<c<2 for the fixed positive-cost setting and at cost zero for all nonnegative benefits. A boundary can move through a connected graph with positive probability, giving almost-sure absorption on this finite state space and uniqueness of the harmonic solution. I reconstructed independently from a uniformly chosen singleton: the twelve reachable nonabsorbing masks have a cooperative cyclic arc, so only its growth/shrinkage by one boundary site is relevant. Cancelling self-loops, I solved the harmonic equations over exact rational-function fields without the frozen orbit quotient. The results verify both cost-free identities, the two positive-cost rational formulas, their difference, and the rational witness at c=1/100. For c=2t/(1+t) the independently expanded numerator has exactly one sign variation (negative constant, all later coefficients positive); the transformed denominator D_c is strictly negative and the transformed Q_c strictly positive. Endpoint signs and Descartes' rule give one crossing, and the remaining difference factors give strict clustered dominance everywhere in the interval. The alternating deviation is negative because its quadratic factor is positive and its three denominator factors are negative. An exact rational bracket [0.04927573663345605,0.04927573663345615] supports the stated rounded decimal; uniqueness and the algebraic definition are exact. Replay: python3 /workspace/branches/audit_exact_3.py.

## originality

PASS

The strongest related primary source includes an exact finite-selection checkerboard cycle formula, not only weak-selection analysis. Its donor-site game and the fixed symmetric edge-benefit game are distinct even on C4. The strongest distinct indexed four-cycle arrangement theorem uses mutant-only site fitness and birth–death updating. The supported increment is the exact cost-zero neutrality versus advantage for static symmetric edge layouts, and the unique all-interval positive-cost crossing and strict order for the stated parameters. Neither the chain method nor the general observation that some arrangements matter is new.

## value

PASS

This is a controlled regular-graph example showing that the same multiset of benefits does not determine exact fixation. It separates exact neutrality and strict advantage even away from weak selection, and shows the arrangement effect persists under a positive cost with a precisely identified neutral crossing. It supplies a test case for approximations using only a degree or global edge-benefit summary, not a theorem that the effect persists if all weighted degrees are also held fixed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
