# Independent mathematical audit

## correctness

PASS

For each selected induced complete multipartite subgraph with selected size s and largest part occupancy L, longest ordinary path length is min(s,2(s-L)+1). A P_k-free set therefore has size <=k-1 or outside-dominant count q<=floor((k-2)/2). Count all sets by unique dominant part for s>=k; inclusion maximality forces either (k-1)-sets with each part <=ceil(k/2)-1 or an entire dominant part plus exactly t outside vertices, with V(G) alone in the no-k-path case. Derivation covers k=4, k=N, small parts, ties and even/odd bipartite k; the complement gives minimal covers. Inspected original verify.py adjacency DFS. Fresh direct ordinary-path search and maximal-set extraction agreed with every coefficient across 207 multipartite size/k instances on total order 4..8.

## originality

PASS

Prior minimum k-path vertex-cover formulas yield only extremal cardinality, not the complete polynomial of all feasible sets or inclusion-maximal sets. General dissociation polynomial handles k=3 and does not imply the new k>=4 classifications; prior longest-path occupancy lemma is explicitly credited. No prior all-complete-multipartite k-path transversal-size polynomial found in the checked primary survey and published records.

## value

PASS

Path-transversal sets are natural graph deletion/hitting structures; knowing every inclusion-minimal solution and its cardinality distribution is a stronger mathematically motivated invariant than a minimum cover number. The sharp bipartite even/odd collapse, large gaps and asymptotic rarity of large maximal sets clarify a genuine structural phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
