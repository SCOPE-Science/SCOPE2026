# Independent mathematical audit

## correctness

PASS

Under the stated Steiner normalization the generator-wedge sum gives V_3. By Cauchy–Binet, each forest component contributes its vertex count to the Gram determinant, since every maximal incidence minor obtained by deleting a row has determinant ±1. The only triple determinants are 4,6,8. Counting disjoint edge-pairs inside triples gives (m−2)M_2=P_4+2b+3M_3, where b counts triples with two components. Any nonstar has a three-edge path; taking its end edges and an edge outside that path gives a disconnected triple and hence strict star minimality. Leaf deletion bounds the three-matching count by the path value, and the strict path advantage in D=(m−2)M_2−P_4 is (m−2)(Σ_v binom(deg(v)−1,2)−1)+P_4(T)>0 for nonpaths (separate star case). The positive coefficients, path run counts, gap, ratio and two spider counts all check. `python3 /workspace/reviews/evidence/reproduce.py 4` independently enumerated 1,296 and 16,807 labeled trees of orders 6 and 7 by Prüfer codes, checked the determinant counts and detected exactly the labeled stars and paths at equality. This finite replay supplements the proof; the supplied checker was read, not run.

## originality

PASS

Supported for the matching/path reduction together with the sharp strict third-intrinsic-volume tree comparison and the resulting degree-sequence separation, not for the classical zonotope wedge formula or incidence-minor method. The strongest indexed neighbors treat different invariants or dense graphs, and the general zonotope theorem does not yield the strict tree comparisons without the additional structural argument.

## value

PASS

The third intrinsic volume is a natural Euclidean invariant. Three familiar graph counts replace an exponential-search-style pattern description by a short exact formula, yield sharp extremizers with a strict equality criterion, and show degree data alone do not determine it. The structural maximum, rather than the finite spider computation alone, gives the main value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
