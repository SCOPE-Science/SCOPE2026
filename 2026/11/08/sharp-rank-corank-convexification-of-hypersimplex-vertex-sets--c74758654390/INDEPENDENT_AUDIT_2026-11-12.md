# Independent mathematical audit

## correctness

PASS

For each 0-1 hypersimplex vertex 1_I and lambda>0, the equation (1+lambda)y=1_I+lambda z is equivalent to y_i>=1/(1+lambda) for selected i and y_i<=lambda/(1+lambda) for unselected i, with sum(z)=k automatic. When lambda>=1 the nested cutoffs reduce exactly to y_(k)>=1/(1+lambda) and y_(k+1)<=lambda/(1+lambda), including ties. Every y in P_{n,k} satisfies y_(k)>=1/(n-k+1), y_(k+1)<=k/(k+1); sharp witnesses are k-1 ones plus n-k+1 equal small coordinates, and k+1 coordinates each k/(k+1) plus zeros. The first witness forbids any lambda<n-k, and the second any lambda<k, including lambda<1; their simultaneous satisfaction gives c(V)=max(k,n-k) for all lambda>0 and eta=1/(1+c). For lambda>=1 the two failure regions are disjoint because sorted y_(k)>=y_(k+1). Independent exact rational brute-force membership on finite hypersimplex grids through n=6 matched this criterion; universal proof uses inequalities, not finite enumeration.

## originality

PASS

The Schneider index and the vertex-generation normalization are classical; simplex endpoints and general face obstructions from Artstein-Avidan et al. are prior. The all-rank uniform-matroid base-polytope index and exact pointwise rank/corank membership phase diagram were not found in examined primary AFS full text or indexed related matroid findings. Meyer 2026 theorem plausibly gives a general criterion, but its full text could not be obtained, leaving a meaningful historical implication risk; accessible abstract alone is not used to claim it excludes the result.

## value

PASS

Uniform-matroid base polytopes are a natural canonical family across all n,k, and the exact rank/corank index plus complete two-threshold pointwise covering criterion upgrades generic existence/face bounds into an all-rank extremal classification. The original obstruction and sufficiency proofs remain meaningful beyond the known simplex endpoints; a natural exact invariant needs no unrelated general theorem to be worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
