# Independent mathematical audit

## correctness

PASS

Verified for the stipulated stationary, integer-spaced adjacent-pair readout. Write k=s/(1+3s); then π_i c_i=k, balancing flux and giving J=k(p−q). Each state has exactly one opposite-label neighbor. Thus the two routes for 0101 have weights kspq² and kp²q, and those for 1010 have ksp²q and kpq², giving δ=kpq(p−q)(1−s). Stationary balance at the three-bit marginals 000,111 gives the two zero pairs; balance at 010 and 101 gives discrepancies δ for 0010/0100 and 1011/1101, and balance at 001 and 100 gives −δ for 0011/1100. TV is 4|δ|; in particular p=3/8,q=1/8,s=1/3 yields 1/192. On the full-path zero surfaces, p=q gives detailed balance; s=1 identifies the reversed chain by i↦1−i preserving labels; at pq=0 the binary runs are independent sums of the two geometric holds belonging to their class. Stationary alternating renewal reversal follows by length-biasing the origin run, placing the origin uniformly in it and then using the independent alternating lengths on either side; reversal reflects that uniform offset. For any irreducible chain on at most three hidden states a nonconstant binary labeling has a singleton. At its entry successive visits regenerate, and the geometric holding length is independent of exit destination and excursion duration, yielding the same stationary renewal representation. Shorter stationary binary words have equal forward/reverse frequencies by marginal balance. With d=|p−q|, optimize [s(1−s)/(1+3s)] [(u²−d²)d]: the signs of 1−2s−3s² and u²−3d² give unique maxima 1/9 and 2u³/(3√3), attained as stated. Inspected submitted check.py and VERIFICATION.md without running uploaded code; a separate symbolic expansion agreed with the analytic calculation. Neither finite word expansion nor rational tests alone prove full-process reversibility.

## originality

PASS

The substantiated distinct contribution is the exact one-defect adjacent-pair ring TV, its full-path zero set, and the sharp fixed-activity optimizer; distinguish the general frame and hidden-state cutoffs shared with other sources.

## value

PASS

At the smallest nontrivial hidden-state size, this concrete occupancy measurement can hide even maximal directionality, yet detects a precise combination of positive two-way motion, bias and heterogeneity in the shortest possible stationary binary block. The population-TV optimum is a meaningful quantitative benchmark for this particular coarse sensor at fixed activity, not a statement about estimation power, generic network structure or hidden entropy production.

The dated certificate retains the supplied scientific assessment, sources and limitations.
