# Independent mathematical audit

## correctness

PASS

Under the coherent Ewens cycle-partition coupling, the ranked paintbox gives iid labels conditional on the masses, so the statistic is exactly the longest constant-color interval in numerical label order. The largest atom exists and is below 1; a continuous GEM stick-breaking factor rules out equality with any earlier atom, simultaneously for all countably many pairs. With p the largest mass, the upper bound n*sum_j P_j^k <= n p^(k-1) controls the whole countable alphabet. Disjoint all-top-color windows give the complementary exponential lower-tail bound. Both are summable on dyadic n at thresholds (1 plus or minus epsilon) log n/(-log p); monotonicity interpolates. Top-color run starts count each maximal run once and have mean p^k+(n-k)(1-p)p^k. Their windows are independent beyond distance k and distinct starts within distance k are incompatible. The dependency-graph bound is therefore O((k+1)n p^(2k)), tending to zero at the stated critical thresholds. If q<p is the second-largest mass, all other colors contribute probability at most n q^(k-1)=o(1). The critical-limit conclusion is meaningful along suitable subsequences, as the finding qualifies: for a fixed p an all-n integer threshold with positive finite limiting intensity is impossible, since the ratios of successive intensities would force k_(n+1)-k_n=0 eventually. At theta=1, uniform stick breaking gives P_* =d max(U,(1-U)P_*') with independent U uniform and P_*' a copy. For R(u)=Pr(P_*<=1/u) this gives uR(u)=integral_(u-1)^u R(v)dv for u>1, with R=1 on [0,1], hence the Dickman equation. Substituting u=exp(1/t) verifies the CDF with the correct direction. The frozen checker was inspected, not executed; its finite color-equivalence checks do not verify these limits.

## originality

PASS

The classical fixed-probability longest-head-run law, the top-color Bernoulli approximation and the PD/Dickman identity are not separate originality credits. The distinct claim is their use for the maximum over all colors of the coherent Ewens partition, yielding a nondegenerate PD-dependent almost-sure scale and a linked quenched threshold law. The stronger checked run or cycle sources do not supply that combined asymptotic for this statistic.

## value

PASS

Cycle cohesion along consecutive labels probes spatial organization not identified by the cycle size counts alone. The all-color result shows a realization-dependent leading logarithmic scale, rules out a deterministic Bernoulli parameter for that scale, and connects the same dominant atom to the quenched lattice threshold. The Dickman transformation makes the scale explicit in the uniform case. The value is in that conclusion for a natural exchangeable cycle statistic, not in repeating a finite enumeration or a fixed-p run theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
