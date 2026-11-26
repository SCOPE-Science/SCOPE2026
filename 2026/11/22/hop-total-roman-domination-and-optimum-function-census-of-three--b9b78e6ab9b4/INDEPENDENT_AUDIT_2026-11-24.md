# Independent mathematical audit

## correctness

PASS

At n>=8, distinct intersecting triples have a common disjoint triple since their union has at most five elements; disjoint triples are adjacent, not at distance two. With m defenders and union U, every triple outside U is a mandatory 1 and all other nondefenders are allowed 0 by the hop condition. Thus the weight is at least 2m+C(n-|U|,3), in turn at least 2m+C(max(n-3m,0),3). With n=3r+s, the no-defender weight C(n,3) and m>=r+1 exceed 2r. For 1<=m<=r-2 the relaxed bound is decreasing as m increases and its endpoint is 2r-4+C(6+s,3)>2r; that range is empty for r=2. Comparing m=r-1 and r yields exactly 2r-1 for s=0 and 2r for s>0 as lower bounds. Equality at s=0 forces disjoint defenders with precisely one complementary triple carrying 1. For s>0 equality forces r defenders, no 1s, and at most two unused points. Thus the incidence excess 3r-|U| is zero or (only at s=1) one, the latter forcing exactly two triples to share one point. Ordinary disjointness gives no positive isolates: in that exceptional case r>=3, and another disjoint defender supplies neighbors. This includes n=8, where the two disjoint defenders suffice. Choosing distinguishable 1/2 blocks gives n!/[6^r(r-1)!] at s=0; disjoint 2-blocks give n!/[s!6^r r!] at s>0. The extra s=1 family divides n! by the 2! for unused points, the (2!)^2 for two unordered two-point branches, the 2! interchanging branches and 6^(r-2)(r-2)! for the other triples. An independent bounded check using computed shortest-path masks and exhaustive defender sets at the candidate weight or lower reproduces all minima for n=8,9,10, including 37800 overlapping and 2800 disjoint assignments at n=10. The structural proof handles all n, not just the replays.

## originality

PASS

The examined results on the same graphs concern other adjacency-based invariants; the exact hop-total results use different graphs. The rank-two intersection-graph enumerator gives a close support-counting analogue, not the rank-three residue law and full optimum census. This pass is for that precise census and theorem, not the underlying hop-total definition or the general method of using the union of defenders.

## value

PASS

The ordinary disjointness and hop intersection conditions coexist on a canonical infinite family. The result identifies exactly when as little as one unit of overlap in the defender family is possible at equality, counts all labeled optima in all residue classes, and yields explicit benchmarks beyond a scalar minimum. The extra overlapping census is not an artifact of enumeration at small n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
