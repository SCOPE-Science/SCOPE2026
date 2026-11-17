# Independent mathematical audit

## correctness

PASS

Identify R_{m,n}=L(K_{m,n}), m,n>=1. An induced maximum-degree-one vertex set becomes a vertex-disjoint bipartite edge component packing of K_{1,1}, K_{1,2}, K_{2,1}. The unique triple (a,b,c) uses r=a+b+2c rows, s=a+2b+c columns, and k=a+2b+2c selected vertices. Insertion of a missing edge proves the exact maximality condition (r=m and s=n) OR (a=0 and (r=m or s=n)); in particular the a=0 condition when only one shore is covered is necessary. Counting labeled star slots gives m!n!/[a!b!c!2^(b+c)(m-r)!(n-s)!]. For 1<=m<=n, n>=2m, coverage forces all rows and a=0, b=m-2c, giving all even sizes 2ceil(m/2)..2m. Independently tested all subsets for boards (1,1),(2,2),(3,3),(3,5): polynomials z,6z²,6z³+9z⁴,90z⁴+90z⁵. Includes clique K_n and n=2m boundaries.

## originality

PASS

Earlier same-day complete rook-graph dissociation polynomial counts ALL feasible sets and gives component decomposition, but explicitly does NOT count inclusion-maximal sets. The new saturation test, irredundant maximal-set factorial summation, and gapped rectangular facet spectrum are not stated in that prior all-set polynomial. Results on ordinary grid P_m square P_n and general maximal-dissociation bounds do not settle these facets. Best of knowledge with same-day coverage attributed.

## value

PASS

The inclusion-maximal dissociation complex and its cardinality gap/purity behavior are natural invariants beyond the all-set dissociation polynomial. The exact criterion and arbitrary-rectangle labeled maximal-set count determine irredundant configurations and an unbounded gap in valid facet sizes; useful independently of a broader graph-theoretic downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
