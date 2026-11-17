# Independent mathematical audit

## correctness

PASS

In K_{a,b} with d>=2 i.i.d. uniform offers with replacement, each move deterministically changes part and new-target discovery probability is 1-(j/n)^d regardless of particular seen labels. A coupled greedy count chain proves optimality for every deadline against all adaptive randomized choices. The alternating independent offer streams yield C_A=max(2U_a,2U_b+1), C_B=max(2U_b,2U_a+1), where U_n starts with one coupon collected and equals sum_{r=1}^{n-1} Geom(1-(1-r/n)^d). Parity CDFs follow. Log-concavity of geometric masses, TP2 convolution and strict parameter monotonicity give likelihood-ratio order U_a>=lr U_b, hence strict even-time gap exactly k>=a-1 for a>b. Coupling maxima gives mean gap P(U_a>U_b)-P(U_a<U_b) in (0,1], equality 1 exactly b=1. Independent exact-rational labeled-mask process matched partwise collector CDFs for K_3,2 at d=2 and d=3 through nine traversals; at t=4 d2 larger-start CDF=10/27 and d3=1729/2916, versus 0 from smaller start. Finite checks are not proof of all sizes or MLR.

## originality

PASS

PASS with substantial prior coverage explicitly scoped: Nov 2 published theorem already establishes d=2 greedy all-deadline optimality, the same start-side ordering, parity laws and expected advantage, with extra logistic asymptotics. Nov 8 single-offer result covers d=1. The new claim extends all finite offer multiplicities d>=2 and proves the stronger likelihood-ratio ordering of individual multi-offer collector completion times; these are not statements of the earlier d=2 results. The d=2 special case is not original.

## value

PASS

PASS: the number of independent offers is a natural intrinsic choice parameter; all-d stochastic optimization and a monotone likelihood-ratio theorem control the entire completion-time distribution, not merely a new numerical example. Strict parity threshold and exact expectation bound for every d are useful for controlled coverage on complete bipartite graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
