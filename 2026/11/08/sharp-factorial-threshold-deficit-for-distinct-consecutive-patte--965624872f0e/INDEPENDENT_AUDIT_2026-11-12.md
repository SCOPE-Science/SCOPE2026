# Independent mathematical audit

## correctness

PASS

Let D_n=n(n+1)/2-E X_n where X_n sums distinct consecutive relative-order patterns over all lengths. For k <=(1-eps)log n/loglog n deterministic U_(n,k)<=k! yields D_n>= (1-eps-o(1))nlog n/loglog n. For two length-k windows overlapping at shift d<k, edges (j,j+d) on 1..k+d form disjoint paths; alternate-edge matching of size >= floor(k/2) gives disjoint value sets whose restricted order types are independent, so collision prob <=1/floor(k/2)!. Disjoint windows collide with probability 1/k!. Number of duplicate appearances <= number colliding pairs; summing for k>=(1+eps)log n/loglog n has tails O(n^2/b! +nb/floor(b/2)!)=o(nlog n/loglog n). Taking eps down to zero proves sharp coefficient one. Independent permutation counts n=3..8 and matched-forest checks corroborate.

## originality

PASS

Prior Allen et al. gives only E X_n=(1/2)n^2(1-o(1)) and a cruder overlap bound; Godbole–Swickheimer improves error to O(nlog n) and explicitly asks for better error. Their inspected exact statements do not give the first-order deficit coefficient at log n/loglog n. Best-of-knowledge PASS for sharp expectation correction, not for known factorial crossover scale.

## value

PASS

Natural quantitative refinement of a well-studied random-permutation statistic: identifies exactly how many potential consecutive windows are lost to duplicate order patterns, with coefficient 1 rather than a crude order bound. The overlap matching proof separates dependent from independent windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
