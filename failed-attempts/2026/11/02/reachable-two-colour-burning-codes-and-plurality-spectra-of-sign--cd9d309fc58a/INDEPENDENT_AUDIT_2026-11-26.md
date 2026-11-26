# Independent mathematical audit

## correctness

PASS

Switching by the center-normalized sign vector multiplies the signed influence at each receiving vertex by its own switching sign. Zeros and ties are preserved, and legal ignitions correspond in both directions. On the positive star, center-first ignition produces a constant word. If a leaf burns first, the next spread colors the center from that single leaf; no other leaf can yet acquire a color at this same simultaneous spread. At most one of them can then be ignited before the next spread colors all remaining leaves. An exceptional leaf is realized by igniting another leaf first and the chosen leaf in the opposite color after the center burns. Thus there are exactly 2(n+1) distinct words, with the center sign and exceptional leaf recovering the word. Global negation reduces plurality to the maximum number of positive vertices, so the error count is the minimum distance of the switching vector to the positive-star code. For q negative leaves the two center choices cost max(0,q−1) and 1+max(0,n−q−1); grouping by q gives the signing polynomial. The distances at q=0,1 are zero and at q=n the distance is 1. On 2≤q≤n−1 the distance is min(q−1,n−q), whose maximizers are centered at (n+1)/2. Including q=n in the small tie cases gives q=2,3 for n=3 and q=2,3,4 for n=4; beyond them, the maximizing radius is floor((n−1)/2), with one central weight for odd n and two for even n. Binomial counting and the freely paired center signs give the claimed signing and full-code deep-hole counts.

## originality

FAIL

The reachable code, plurality function and covering-radius interpretation are already covered by star-specific catalog results and by the stronger complete-multipartite theorem. Its deep-hole characterization and counts specialize to the asserted star cases, and the proposed signing polynomial is a direct binomial aggregation of its per-signing formula. This is substantive prior coverage, irrespective of the notation used for the polynomial.

## value

FAIL

A complete signed-tree code and its plurality census would be a natural object of study, but this star case has already been settled, including the minimizing-signing count by specialization. The residual change of presentation to a signing polynomial collects known per-signing values with binomial weights and adds no independently unknown structural or exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
