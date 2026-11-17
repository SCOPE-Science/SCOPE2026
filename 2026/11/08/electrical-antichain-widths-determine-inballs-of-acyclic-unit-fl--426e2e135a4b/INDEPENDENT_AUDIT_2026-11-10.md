# Independent mathematical audit

## correctness

PASS

On the affine unit flow space Bx=e_s−e_t with positive diagonal metric Q, the norm squared of coordinate e restricted to ker B is [Q⁻¹−Q⁻¹Bᵀ(BQ⁻¹Bᵀ)^+BQ⁻¹]_{ee}=q_e⁻¹−q_e⁻²R_e. Thus a Q-ball of radius r fits exactly when a unit flow satisfies x_e≥r α_e for all edges, including α_e=0 inactive constraints. Every unit DAG flow is a convex combination of s–t route incidence vectors. Each reachability-poset antichain meets any route at most once, so r≤1/max_AΣ_{e∈A}α_e. The weighted Dilworth lemma supplies a distribution of maximal chains with inclusion probabilities at least α_e/W: for integer weights, replace each poset element by that many incomparable clones, partition into W chains by ordinary Dilworth, project and extend; rational scaling and simplex compactness give arbitrary real weights. This proves the bound attained and the entire incenter locus; equality gives maximum-antichain tangencies. A pair of internally disjoint paths of lengths a,b gives r=sqrt(a+b)/2 under the inherited Euclidean metric. I examined the exact grounded-Laplacian plus independent path-mixture LP checker; no claim that its 96 numerical examples alone prove the general theorem.

## originality

PASS

Best-of-knowledge PASS: classical source–sink flow polytopes and their route decompositions, electrical coordinate projections, and weighted Dilworth are known; however, the inspected prior flow-polytope triangulation/volume results and unrelated geometric inradius results do not give the present exact weighted electrical-antichain formula and full incenter locus for arbitrary acyclic source–sink networks. A 2026 same-week complete-network inball result has stricter graph and netflow restrictions and does not dominate all positive diagonally weighted DAGs.

## value

PASS

This is a natural complete metric-geometric characterization of a broad class of network flow polytopes: electrical resistances determine facet speeds, poset antichains give tight inball certificates and an explicit finite convex locus of all incenters. It unifies electrical network geometry and weighted Dilworth, with useful path-length examples. It makes no unfounded claim about all netflows or arbitrary affine metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
