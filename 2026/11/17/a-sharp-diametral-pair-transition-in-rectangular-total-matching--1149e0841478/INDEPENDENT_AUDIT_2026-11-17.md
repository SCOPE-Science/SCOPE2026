# Independent mathematical audit

## correctness

PASS

All 0/1 total-matching incidence vectors are polytope vertices; pairwise squared distance equals symmetric-difference cardinality, and any shared element can be removed to increase extremal distance, hence diametral T1,T2 are disjoint. Because selected graph vertices within a matching occupy one shore, mixed-shore pairs have at most p+q items and both-left at most 2p, strictly below target since q>p. Both-right has at most q+2p (q right vertices and max 2p edges), and independently 2q by at most two objects per right vertex. Witnesses cover R if q<2p and use disjoint full p-matchings if q>=2p. Saturating either bound forces stated right-vertex assignments; the overlapping-edge ban is enforced. For q>=2p choose two ordered injections on 2p distinct right endpoints, 2^(q-2p) spare assignments, divide by 2. For q<2p choose ordered right endpoint sets with union R and sizes a,b, and use inclusion-exclusion over t=a+b-q shared right endpoints to forbid common edges. Nonvertex points cannot realize the farthest distance by strict convexity of squared norm.

## originality

PASS

The reported diameter is Euclidean in the natural vertex-edge incidence coordinates, not the graph-theoretic/1-skeleton diameter. Ferrarini and Faenza/Ferrarini treat facets and extended formulations for exactly these polytopes, but inspected relevant primary results do not classify the Euclidean farthest pairs or their sharp q=2p count transition. Resultary semantic matches were the same self-record and different polytopes or matching-flip graphs, not a dominating theorem. Possible equivalent formulation via independent sets of total graph remains historical risk.

## value

PASS

A sharp two-parameter Euclidean diameter, complete farthest-pair classification, and a closed count with a q=2p phase transition are meaningful metric invariants for a well-defined established polytope family. The count is not a routine recasting of facet descriptions or the elementary upper bound 2q; it gives a reusable diameter graph characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
