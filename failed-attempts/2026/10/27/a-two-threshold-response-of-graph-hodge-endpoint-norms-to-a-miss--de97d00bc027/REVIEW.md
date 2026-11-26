# Independent mathematical audit

## correctness

PASS

On the zero-sum vertex space, the Laplacian is N I−ddᵀ for d=e₀−e₁. Its inverse there is I/N+ddᵀ/[N(N−2)] since dᵀd=2. For an incident edge 0x the potential has values (N−1)/[N(N−2)], −1/[N(N−2)], −1/N at 0,1,x respectively, and zero elsewhere. Summing the absolute differences along surviving edges gives q_A=2−1/(N−2) with diagonal r_A=(2N−3)/[N(N−2)]. For a remote edge, the rank-one term vanishes and the omitted edge would have had zero drop; q_B=2−2/N and r_B=2/N. Since 0≤r_e≤1 for an orthogonal projector, complementary absolute column sums are 1+q_e−2r_e. The two orbit differences are therefore (N−4)/[N(N−2)] and (N−6)/[N(N−2)]. Both orbits exist only for N≥4; their maxima give the signs and ties stated. For N=3 the surviving graph is a tree with Q=I and P=0. For the full clique, every cut column has diagonal 2/N and 2(N−2) entries of magnitude 1/N, so the full clique values are 2−2/N and 3−6/N. Symmetry of the projections identifies the two endpoint norms, and orientation only changes row and column signs.

## originality

FAIL

The inspected complete multipartite theorem (Resultary 745e7b0c399e) gives the same cut and complementary cycle projections, the exact absolute column sums for each pair of part sizes, and the maxima. Both the intact clique and the once-deleted clique lie in that class. Substituting their part sizes gives all displayed norms, thresholds and extremizers, including the N=3 star. This is positive statement-level subsumption by a stronger result, not a decision based on matching titles, scope words or an unavailable source.

## value

FAIL

The deletion thresholds are informative as examples of a broader phenomenon, but the precise values, sharp ties, and boundary case are already mechanically determined by the two known multipartite score functions. The frozen record supplies no independent new example outside that theorem, new invariant, or nonmechanical consequence beyond ordering these two scores.

The dated certificate retains the supplied scientific assessment, sources and limitations.
