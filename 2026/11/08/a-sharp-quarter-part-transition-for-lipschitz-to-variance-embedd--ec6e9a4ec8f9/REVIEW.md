# Independent mathematical audit

## correctness

PASS

For r>=2, all n_i>=1, N=sum n_i>=2, unit cross edges, and uniform vertex masses, the squared operator norm of T_G is maximum centered variance. Anchoring at one vertex makes the feasible Lipschitz ball compact, and variance is strictly convex on that anchored affine space, so every maximizer must be a polytope vertex. At a vertex tight-edge incidence rank N-1 forces a spanning tight tree; summing +/-1 along its edges proves integrality. Since complete multipartite graph diameter is <=2, normalized extremal values are binary {0,1} or {-1,0,1}. The latter requires both signs within a single part, every outside vertex at zero, and no same-part zeros (they would be isolated in the tight-edge graph). Exact variance numerator equals t(N-t) for binary with t ones, or N*a-(2k-a)^2 for a +/-1 part with k positive signs. The former maximizes at floor(N²/4), the latter at N*m-(m mod2), monotone in a. All maximizing equality classes follow from these sharp cases. Singleton m=1 has no three-level type, including harmless N=2,3 algebraic ties. Writing N=4q+r and evaluating m=q and q+1 in residues r=0,1,2,3 establishes baseline iff m<=floor(N/4) for N>=4, and true coexistence exactly when N divisible by 8 and m=N/4. I independently enumerated all 58 unordered connected multipartite profiles N=2..8, 13800 feasible anchored integer assignments, all 968 maximizers and the classification; repeated exact threshold arithmetic for every N=4..1500 and m<N. Rebuilt both source and checks Git trees from all seven file and directory SHA identities: root ab29f40ac8925d33336695e4808476daa75792ac. These finite checks corroborate but do not replace the all-N proof.

## originality

PASS

Best-of-knowledge: the exact uniform scalar spread, all maximizing assignments, and quarter-size plateau for arbitrary complete multipartite graphs were not found as a pre-existing full theorem in the inspected primary literature or nearby published findings. The original source itself occurs in the Resultary index and is not counted as independent prior coverage. Strong 2018 facet results already classify potential shapes; novelty is the explicit centered quadratic optimization, integer parity boundary, and equality selection, not new polytope vertices. A separate published two-distance bipartite theorem covers the two-part t=2 special case while explicitly crediting an earlier multipartite scalar endpoint; its dated same-day occurrence cannot prove earlier priority for the all-part claim.

## value

PASS

Graph spread is a natural sharp scalar Lipschitz-to-centered-L2 concentration/embedding constant. Within an infinite, symmetric but parametrically nontrivial family the result gives an exact all-size operator norm, all norming functions and an exact quarter-largest-part stability plateau under extensive edge deletion. The parity-only coexistence at N divisible by 8 and balanced K_{s,s,s,s} exhibiting unchanged spread after deletion of asymptotically one quarter of clique edges are mathematically motivated non-strictness/phase phenomena. Although the candidate facet geometries are known, their exact centered quadratic optimization and global transition are not merely renaming the known facet count. The proof is elementary once the prior structural theorem is recognized, and its scope/value are stated accordingly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
