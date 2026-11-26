# Independent mathematical audit

## correctness

PASS

Remove right-shore vertices of degree at most one. The remaining graph is a forest on a+j vertices with at least 2j edges, so j≤a−1. For a chosen set of j right labels, their neighbor sets form an ordered tuple; adding each connector creates a cycle precisely when two of its neighbors were already in the same component. The other right labels have a+1 independent leaf-or-isolate choices each. This gives the stated binomial sum and counts unrooted edge sets once. An independent bounded replay confirmed all three coefficient lists, all strict signs for a≤b≤t_a, and the inequalities (a+1)b^a>a(b+1)^a at b=10,18,27. After these starts the right-hand side of the lower bound on R_a(b+1)/R_a(b) is strictly increasing in b and already exceeds one; the binomial polynomial in the proof is positive and nondecreasing there. Thus the infinite tails cannot recross or meet equality. For a+b≤17, widths 3–5 leave just (3,14). Widths 6–8 have b≤11≤2a, so the published strict minimum-degree theorem applies with δ=a≥(a+b)/3 and a+b≥12. Independently, choosing the tree component of a fixed left vertex yields F(a,b)=F(a−1,b)+sum over 1≤i≤a, 1≤j≤b of C(a−1,i−1)C(b,j)i^(j−1)j^(i−1)F(a−i,b−j), with F(0,b)=1. The bipartite spanning-tree factor follows by the matrix-tree theorem. Exact arithmetic using this recurrence gave negative F−D for all twelve remaining pairs at widths 6–8, corroborating the exclusion.

## originality

PASS

Credit prior exact count generation, the K_{3,14} witness, the minimum-degree sufficient inequality, and eventual existence of violations. The distinct claims supported by the comparison are the exact all-size signs for widths 3–5 and the unique first obstruction in the stated biclique class, not the individual counts or example graph.

## value

PASS

The sharp thresholds quantify when a natural degree-product bound first fails and prove failure persists thereafter in three thin-shore families. The connector expansion makes the infinite comparison transparent; the finite classification gives exact scope to an already known counterexample, previously not located within a biclique-wide first-failure statement in the inspected sources.

The dated certificate retains the supplied scientific assessment, sources and limitations.
