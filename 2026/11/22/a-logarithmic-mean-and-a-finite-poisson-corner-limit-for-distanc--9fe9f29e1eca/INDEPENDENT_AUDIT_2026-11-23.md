# Independent mathematical audit

## correctness

PASS

Pass for the repaired files, not the original slogan. The slogan assigned the displayed additive mean constant to pairs at graph distance exactly three, whereas the computed mean is for disjoint pairs with no common neighbor, including disconnected pairs. This is not an editorial distinction: if N_n counts isolated intervals with right endpoint below 1/n, then at least (n-1)N_n/2 obstruction pairs cannot be at distance three. The expectation of N_n is at least n^(-1)(1-2/n)^(n-1) since the short interval has probability 1/n^2 and each other interval can intersect it only if its left endpoint is below 1/n. Thus liminf of the mean discrepancy is at least exp(-2)/2. The corrected statement transfers only the weak limit to true distance-three pairs. The checked finite mean integral uses the two oriented beta densities and third-interval bridging probability 2rs; its one-dimensional reduction, scaled by x=nr at the left edge and dominated by an exponential envelope for the comparison, gives log(2n)+gamma-1+o(1). Independent compact-window rare-cell limits give all three corner processes; for fixed positive lower cutoff alpha, the upper-coordinate omission is bounded by the integral of 4rs exp(-rs) on r,s>=alpha and max(r,s)>K. It vanishes with K, then the probability of a lower-cutoff omission is at most 2 alpha^2. This proves weak convergence and almost-sure finiteness (the limiting minima are positive), whereas the untruncated Campbell mean diverges as the integral of dr/r. The repaired zero-event argument uses existence of a void rectangle, not that all rectangles are void when the minimum is void. The minimum-exponential integral equals 1/3 for a positive count. Two overlapping middle-anchored intervals give the high-probability distance interpretation, including the case they coincide. A common continuous CDF preserves the sampled endpoint order almost surely. The exact finite enumeration was read, not executed, and does not prove the weak limit. Corrected complete affected files are RESULT.md and SLOGAN.txt under repairs/4; other frozen files remain evidence.

## originality

PASS

For the repaired claim, the classic zero probability, the high-probability diameter bound and the compact corner processes are not new. The all-pair count over the full rectangle family, tightness despite the divergent mean, and the exact finite mean and its additive term are not supplied by the materially inspected work. The inaccessible historical paper remains a source of priority uncertainty.

## value

PASS

The repaired statistic resolves how many vertex pairs fail to have a path of length at most two, rather than merely detecting the event. The exact additive mean term and an unscaled finite yet infinite-mean limit identify non-uniform integrability in a natural graph model. Distinguishing genuine distance-three pairs from obstructions also shows concretely why a high-probability graph property cannot be used to transfer this precision in expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
