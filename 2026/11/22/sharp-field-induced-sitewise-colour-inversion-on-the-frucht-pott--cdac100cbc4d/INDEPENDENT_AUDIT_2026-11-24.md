# Independent mathematical audit

## correctness

PASS

The specified edge list is the standard labelled Frucht graph. Three disjoint triangles and the residual three-vertex path bound the independent set size by five; equality forces the two path endpoints and then fixes one vertex of each triangle, giving only A. Its complement B induces a three-edge matching and one isolate. For a favoured set S of size k, m>=e(S)>=3(k−6) by cubic degree counting. At k=6, e(S)<=1 would allow deletion of a vertex to leave A, but every vertex of B has at least two neighbours in A, so m>=2 instead. These bounds exclude every population other than 5 before h=3/2, 7 between 3/2 and 3, and exactly 5 and 7 at their first crossing. At k=5 equality forces A and gives 2^4 labelled completions; at k=7 equality in the degree bound forces the complement to be A and gives 2^5 completions. For h>3 only k=12 can attain the linear lower bound. At h=3, for T=V\S the energy is −18+e(T)+m_T, where m_T counts monochromatic edges inside T. Equality is equivalent to independence of T, with two freely chosen colours at its vertices. Independently enumerating all 4096 subsets gives coefficient vector (1,12,48,73,34,1) and I_G(2)=1377. A separate exhaustive base-three enumeration of all 531441 spin assignments gives population minima (3,2,1,0,0,0,2,3,6,9,12,15,18) and corresponding degeneracies (2,12,24,16,112,16,544,32,544,584,192,24,1). It finds all 16 k=5 minimizers supported on A and all 32 k=7 minimizers supported on B. There are 48 at the first crossing; every site switches between the adjoining strict intervals, not at a unique ground configuration at the crossing itself.

## originality

PASS

The supported distinction is the exact positive-field envelope and complete strict-side inversion for this graph. Prior formalism includes the Hamiltonian, and other records specialize the same model to other graphs, but the inspected sources do not establish this ground-state support or these counts for Frucht.

## value

PASS

This gives a small, natural finite-graph witness that a positive uniform field can increase total occupation of the favoured colour while switching its site indicator at every vertex. The uniqueness of each strict-side favoured set makes the phenomenon stronger than a change in mean occupation or a choice of representatives from degenerate sectors. The exact envelope and multiplicities make the example usable as a reproducible benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
