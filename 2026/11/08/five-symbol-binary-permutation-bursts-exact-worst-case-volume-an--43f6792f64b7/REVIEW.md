# Independent mathematical audit

## correctness

PASS

For binary one-length-five contiguous-block arbitrary permutation, uniquely classified every nonidentity descendant by first and last changed sites. For a changed segment v length 2..5, both endpoints flip and the new interior must have r+2a-2 ones, yielding exactly binomial(length-2,r+2a-2); summing is the distinct-sphere size. Reconstructed 16-state weighted max-plus DP tracking last four bits and tie counts; checked exact shift V_19(s)=(h_16(s)+16,c_16(s)) simultaneously for all 16 states, which propagates by max-plus translation equivariance to all lengths. Independent direct output-set enumeration for all binary words lengths 5..10 verified M_n and A_n (10/20,16/8,22/2,26/14,32/4,38/2). The statewise finite identity, not an extrapolation from n<=10, completes the proof all n>=5.

## originality

PASS

Chen–Milenkovic give the same channel and a per-word sphere formula, already explicitly credited. The published general sharp-sphere theorem gives universal bound attaining for q>=k and exact binary k=3 only. The binary k=5 case has q<k and is not implied; published binary k=4 and ternary k=4 maxima are other parameters. Neither the verified prior statements nor Resultary results give this exact all-n k=5 maximum and all maximizing counts. Closest 2026 primary paper was inaccessible in full, an explicit priority risk.

## value

PASS

Worst-case cardinality and exact maximizing-center counts for q=2<k=5 arise from a natural burst error channel where the known universal q>=k optimum is unattainable. The 16-state recurrence and eventual three-periodic extremal census settle a meaningful missing alphabet-deficient boundary, relevant to finite-length channel sphere estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
