# Independent mathematical audit

## correctness

PASS

For each cut, thresholding the median is majority, and the two cuts reconstruct exactly the ternary state. For binary walls d_i and activity a_i=d_(i−1)d_i, the cited wall update implies a'_i=a_(i−1)a_i a_(i+1): both adjacent new walls can be one only if the four old consecutive walls are one. Thus ordinary active runs lose their two ends at each step, and cease after ceil(r/2) steps. An all-active threshold is an even checkerboard and already periodic; the wall update cannot create a wall where there was none, so no other trajectory enters a checkerboard. The maximum is attained by taking one zero wall on an odd ring or two adjacent zero walls on an even ring, with all other walls one; parity of the number of walls makes each example realizable, and the active-run upper bound gives the asserted floor. The max of the two binary clocks is exact; inclusion–exclusion on their checkerboards (intersection the two 0/2 alternations) gives the basin. For L=2t+3=2s+1 the bad event is precisely a length-L alternating block following its first bit repeated; for a full checkerboard there is no such start. Cyclic reading remains valid for L≥n by wall-run length. The trace counts indexed words, not necklaces; given a labelled word the cyclic history at each location is forced, also for n<L. In the rare window the start probability is (5/9)(2/9)^s at each cut. Same-cut starts a positive distance <L apart are incompatible; a sole overlap at the precursor/end is bounded by a constant times (2/9)^(2s). For mixed cuts sharing L−d alternating sites, at least two shared sites force the shared word to alternate 0/2. The common portion costs O(3^{−(L−d)}), with the one-site case absorbed by a uniform factor, and each extension costs O((2/9)^(d/2)); ignoring precursor constraints only enlarges the upper bound. A geometric sum with ratio 2/3 gives O(n3^(−L)); the disjoint-window dependencies vanish and the local-dependence Poisson error tends to zero. The one-cut variance bound and the union upper tail are summable around floor(log_(9/2)n), proving the mean estimate and tightness. The supplied verification script's stale comment about excluding checkerboards is contrary to its actual edge test and trace assertion: checkerboards are included when all cuts have settled or are periodic. Independently replayed /workspace/reviews/evidence/4-ring-check.py: first-repeat periods and transients for all 29,511 words on n=3–9, and sparse adjacency powers at t=0,1,2 for n=3–7, including histories longer than the ring. All basin, sharp-time and trace checks passed; none is used as the asymptotic proof.

## originality

PASS

Qualified to the ordered ternary clock and basin. The binary periodicity/erosion mechanism, single-layer transfer and the existence of a binary Poisson window are precedents. The work needed for the ternary extreme law is not merely summing two binary means: correlations could change the limit, and the simultaneous 0/2 overlap suppression resolves that comparison.

## value

PASS

The ordered uniform three-level ring is the minimal setting where two threshold clocks are coupled and censoring oscillators matters. The finite trace, exact oscillator basin and sharp lattice window distinguish several natural notions of filter stopping; in particular the overlap control makes the useful global-time constant rigorous. The mean estimate is for first periodic entry, not time to a fixed point or a claim of a continuous limiting law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
