# Independent mathematical audit

## correctness

PASS

On any strict fused-star proximal cell, soft-thresholding the leaves and solving the strictly monotone hub equation yields an attainable linear slope that averages the hub (mass a) and r fused leaves, while preserving other leaves. All r=0..k cell types occur with strict penalties, for arbitrary independently positive beta_i. Coarea reduces each block induced Gini seminorm to binary cuts. For a cut with fused hub flag c, fused-leaf count A and unfused-leaf count d, the claimed numerator p[d(1-m)+(t-d)m]+d(t-d) and denominator (c+A+d)(n-c-A-d) follow by level-counting, with m=(ac+A)/(a+r). Subtracting the candidate K times denominator is concave in d for K>=1, so d=0,t suffice; complement symmetry, then hub-in/out endpoint optimization give exactly B_r and C_r. The two mass regimes produce max{1,2(k-1)/(k(a+1)),max_r a(r+1)(k-r)/(k(a+r))}. Independent exact-rational cut enumeration matched this formula for 42 combinations of k=2..8 and a in {1/5,3/5,1,7/5,3,10}. The reciprocal interval and five-leaf crossover follow by elementary optimization. This validates the stated two-input real-data bound; numerical examples alone would not.

## originality

PASS

PASS (bounded best-of-knowledge). The local Jacobian is a weighted pooled-block projection; identical block slopes appear in weighted isotonic regression, but the global nonlinear star-fit and reachable subsets require separate analysis. The weighted-isotonic general finite formula does not assert which nonconsecutive fused subsets arise for star-graph edge penalties; that additional KKT and cut optimization is essential. Material full texts and relevant primary sections checked; remaining historical-equivalence risks retained.

## value

PASS

Star fused denoising is a natural branching proximal problem; the precise robust two-input complete-pair dispersion boundary in the fidelity mass is a practical and mathematical stability question. The invariant edge-penalty independence, reciprocal interval and change of dominant mechanism at five leaves are nontrivial structural results beyond merely computing an algorithm output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
