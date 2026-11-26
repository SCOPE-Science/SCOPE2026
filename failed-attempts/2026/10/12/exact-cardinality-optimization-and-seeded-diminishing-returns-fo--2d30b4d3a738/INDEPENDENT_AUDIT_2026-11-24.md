# Independent mathematical audit

## correctness

PASS

Independent reconstruction: for each edge e, two independently sampled weighted tips straddle its cut with probability 2m_e(1−m_e), where m_e is descendant mass. The Rao sum is therefore 2Σ_e ℓ_e[m_e−m_e²]=2H−2Σ_eℓ_e m_e² by equal tip depth. The latter energy is that of unit current; minimizing at each parallel split divides current in proportion to finite positive branch conductances, so the circuit optimizer is feasible and every selected leaf receives positive mass. Positive pendant lengths make the quadratic strictly convex, including on the simplex. For the discrete optimum, fixed child counts compress each subtree to its smallest feasible resistance, since parallel conductance is decreasing in either resistance including the missing-branch convention. Maximizing the resulting sum over splits gives the exact recursion and O(nk²) arithmetic bound; stored splits and current division recover the set and weights. For diminishing returns, the branch transform has increment δ/[(1+aC)(1+a(C+δ))], decreasing in baseline C and increasing in δ. Induction from pendant branch indicators yields monotone submodular root conductance, strictly increasing under any new tip. For nonempty A⊊B and added x, the reciprocal-resistance drop is δ/[C(C+δ)] with the same monotonicities, strictly decreasing in finite positive C for δ>0. The inequality is strict; two distinct singleton values of zero and their positive pair value refute submodularity at the empty seed.

## originality

FAIL

The substantive new-looking components are direct transfers of existing results once the standard tree-cut/energy identity is written down. Fixed-set full support is already stated for ultrametric Rao. The claimed count-split knapsack is the existing series–parallel resistance DP with zero-cost backbone edges and unit-cost terminal links. Even the strict seeded law is the leaf case of the existing grounded-resistance commute-time proof: explicit positive-probability excursions make both inequalities strict. This is not a claim that any one antecedent prints the full Rao formulation.

## value

FAIL

Optimized Rao conservation is a natural distinction from Faith diversity, and the circuit formulation can be useful pedagogically. The exact optimization and the marginal behavior here nevertheless come directly from a standard energy reduction to two available resistance results and immediate leaf-specific consequences of their proofs. The record does not identify an independently new quantitative subproblem or substantive optimized-Rao phenomenon beyond that transfer and the singleton boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
