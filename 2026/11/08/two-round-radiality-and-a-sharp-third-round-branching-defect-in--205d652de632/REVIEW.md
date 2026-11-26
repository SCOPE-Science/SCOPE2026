# Independent mathematical audit

## correctness

PASS

After one round an edge can only span original distance at most two. On a tree, at distance 2 the same initial witness guarantees both offers; at distance 3 exactly two independent first-round chords can make the pair eligible; at distance 4 exactly the midpoint can serve and both of its first-round chords are required. These cases give weights 1, 2p-p^2, 2p^2-p^3, p^3 and 0 beyond 4. In the two five-vertex trees, presample common pair coins. Unless both ac and bd fail twice, the third-round eligibility for absent ad is already guaranteed in both trees. On the joint failure event, of probability (1-p)^4, path x has no edge to d after round two, while branch x can serve precisely when ax succeeds by round two and the xc first-round and xd second-round coins succeed. The probabilities multiply and a further p is needed for ad. The exact path probability and difference (including 3/512 at p=1/2) were independently reconstructed by counting histories by successful/failed offer counts. Minimality follows since distances 1 and 2 are radial in every round and the only larger distance on at most four tree vertices is 3 on P4. For the sparse limit, the marked, induced original radius-four ball suffices for root degree after two rounds. Around one or two random distinct roots these fixed-radius neighborhoods converge to one or two independent PGW(c) trees, with fresh pair marks; for two roots this follows by truncating explorations to bounded size before taking n large. Truncation gives vanishing variance for the empirical mean of bounded degree observables. Breadth-first domination by four generations of Bin(n,c/n) offspring bounds the second moment of the original ball size uniformly, allowing removal of truncation. The expected depth-d population is c^d, giving the polynomial for 2|E|/n, the mean degree, not the unscaled edge fraction.

## originality

PASS

The model and local-limit transfer are prior. The retrieved comparisons do not cover the evaluated two-round radial kernel, the minimal exact third-round defect, or the polynomial value of the limiting mean degree. Credit the local-convergence mechanism separately from the new computation.

## value

PASS

The exact radial law explains when backbone distances alone suffice, while the minimal third-round example identifies exactly when this reduction fails and why branching matters. The evaluated two-round limit supplies a macroscopic benchmark not furnished by distributional local convergence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
