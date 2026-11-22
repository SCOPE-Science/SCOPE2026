# Independent mathematical audit

## correctness

PASS

In each strict coordinate ordering of u, the unique maximizing simplex vertex for each I is highest-ranked e_i, giving orbit coordinates a_i(k)=Σ_{j=1}^k binom(i−1,j−1), strictly increasing for k≥2. The difference body is centrally symmetric orbit polytope with d_i=a_i−a_(n+1−i), all proper subset-sum facets. Its largest centered Euclidean insphere is tangent to a minimizing facet, so minimizing support directions are precisely facet unit normals ν_S, not sums of multiple gap normals. For S of size s each Δ_I width is 1 in the unnormalized indicator precisely when I intersects both sides; crossing count C=Σ_{j=2}^k[binom(n,j)−binom(s,j)−binom(n−s,j)], yielding cut widths. For k=n, C=(2^s−1)(2^(n−s)−1), minimize over s. Independently enumerated all 36 finite strict integer comparisons for n=3..14. For n≥15 derivative h’(t)>0 for t≥5 forces f_n(s) decreasing on s∈[5,⌊n/2⌋]; s=2,3,4 handled by separate exact inequalities; direct comparison at n=15 and monotone even/odd upper bounds for n≥16 select balanced uniquely. Independent numeric ratio f_14(7)/f_14(1)=1.01425, f_15(7)/f_15(1)=0.988372, f_16(8)/f_16(1)=0.960725 (diagnostic only). Distinguishes ambient Euclidean width induced on sum x_i=constant; no arbitrary simplex weights.

## originality

PASS

Pešović–Stojadinović define precisely Q_{Γ,m}; Postnikov supplies orbit/simplex-sum framework, but neither derives min Euclidean width or n=15 minimizer classification. Closely related published Resultary 2026 claims for complete-bipartite K_pq and split K_c∨independent_m (c,m≥2) share n=15 threshold but have different tube sets; crucially split theorem EXCLUDES complete graphs (m=1). Thus same numeric threshold does not establish direct implication.

## value

PASS

Minimum Euclidean thickness and the complete set of optimal orientations are natural exact metric invariants of the canonical unweighted graph-associahedron and its intermediate graph-polytopes, not ordinary face counts. The first dimension exhibiting a change in width bottlenecks is a meaningful sharp geometric cutoff even though similar thresholds occur in other tube families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
