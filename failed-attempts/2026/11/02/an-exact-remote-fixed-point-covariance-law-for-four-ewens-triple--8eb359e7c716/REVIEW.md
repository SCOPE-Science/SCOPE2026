# Independent mathematical audit

## correctness

PASS

Contracting each open path and removing already closed cycles gives the stated weighted completion quotient. I checked the loop counts for increasing triples and the peak counts including the two allowable single transpositions, one three-cycle and one loop-plus-transposition possibility. These counts apply already at size 3, needed when n=4. Reversal conjugation preserves Ewens weights and exchanges peak with valley after relocating the window. Deletion of j leaves the same Ewens weight on n-1 indices up to a constant factor, preserves the order of images and leaves the window consecutive. This gives covariance as theta/(theta+n-1) times the size difference of the marginal. Independent symbolic factoring of those differences times the common denominator gave theta^2*(theta-1)*(n+2*theta-3), -theta^2*(n-5)*(theta-1), and -theta^2*(theta-1)*(theta+1) for U,D,P/V. The denominator is strictly positive, so the signs, zeros and large-size powers follow; n=5 is a zero covariance for D, not a general independence claim about the entire triple law. The frozen checker was read, not executed.

## originality

FAIL

An inspected distinct indexed record gives exactly the six adjacent triple marginals for the same n, theta and all sites, which is more detailed than the frozen four marginals. The covariances are mechanical corollaries: one sums pattern probabilities if needed and takes a size difference under fixed-point deletion. The cancellation at n=5, signs and asymptotic orders then have no separate nontrivial ingredient. This is a comparison of available results, not an assertion that an indexed catalog date determines priority.

## value

FAIL

The clean finite-size cancellation is interpretable, but all four formulas and the sign and scaling conclusions are immediate algebra on an exact available six-pattern table after a one-fixed-point deletion. No independent structural result or substantive remainder survives the coverage comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
