# Independent mathematical audit

## correctness

PASS

PASS. All allowed edge vectors e_u+e_v have squared norm 2, so the minimal enclosing center equals the unique minimum-norm point p in their convex hull: the projection inequality gives upper radius 2-||p||² and barycentric averaging gives universal lower bound with equality only at p. Class mass variables t_j in [0,1], sum=2 form the rank-two hypersimplex, and uniform per-class coordinates minimize squared norm for fixed masses; strict convexity/KKT yields t_j=min(1,λ a_j). For 2A≤N, p=2/N*1 and R²=2-4/N with all vertices contacting. If 2A>N, only unique largest class saturates, p=1/A on it, 1/B outside, R²=2-1/A-1/B, exactly the AB largest-class meeting edges contact; others' squared clearance 2(1/B-1/A), if present. For missing internal edge z=e_u+e_v in class a, t_class≤1 gives squared distance ≥(2-t)²(1/2+1/(N-a)) with equality at t=1 and projection .5(eu+ev)+1/(N-a)*1_complement, explicitly an average of allowed cross-edges. Distance-to-convex-set convexity bounds all Δ2,N points by max vertex distance, and strict triangle equality plus distinct residuals identifies only missing edges within largest classes as farthest; all-singleton case gives distance zero. Independent rational checks tested 58 profiles n≤8; unrestricted proof is convexity/KKT/equality, not enumeration.

## originality

PASS

PASS under bounded priority. Higashitani–Matsushita treat the *same complete multipartite edge polytope* but their theorems concern edge rings, Gorenstein/levelness; Tran–Ziegler study general edge-polytope combinatorics and face counts. Related published PQ adjacency polytope has ordered tensor/product coordinates and a distinct underlying polytope despite similar nearest-point language. Known minimum inradii of matroid polytopes are different optimization. No checked source implies the exact two-regime enclosing sphere and continuous Hausdorff farthest-set classification.

## value

PASS

PASS. The edge polytope of complete multipartite graphs is a natural rank-two partition-matroid family. Its threshold 2A=N separates all-sphere-contact from strict interior vertices, while the exact Hausdorff gap remains positive even when circumspheres coincide. Exact metric and equality-locus formulas furnish concrete invariants of a central polytope family, not an arbitrary table lookup or recomputation of vertex counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
