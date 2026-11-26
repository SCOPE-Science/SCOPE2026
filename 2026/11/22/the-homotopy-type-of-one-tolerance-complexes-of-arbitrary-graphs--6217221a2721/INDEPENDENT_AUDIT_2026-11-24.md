# Independent mathematical audit

## correctness

PASS

For the unfilled graph input every edge of the complete one-skeleton occurs, and a triple is present exactly when it spans at least one original edge. Inclusion-exclusion gives s; there are no larger faces. The forest Morse matching is injective and gradient paths decrease the maximal vertex (the vertex-level paths go toward a root and then r0). The attaching-map conclusion can also be checked without identifying attaching maps under the Morse equivalence: retain the complete one-skeleton and just the forest-matched triangles. In descending nonroot order, each edge uv with v currently maximal and u != p(v) is free in its own uvp(v); after those collapses the leaf v and its parent edge collapse. This leaves the complete root graph. The component-root map on the full complex is a retraction because every triangle projects to at most two roots. Consequently all discarded triangles have attaching loops trivial in the retained subcomplex, whose collapse to the roots induces the same fundamental-group isomorphism as the retraction. Reattaching them wedges on two-spheres; their number is s-[binom(n,2)-(n-c)-binom(c,2)], and the root graph gives binom(c-1,2) circles, including edgeless graphs and n=2. The independent bounded replay `python3 /workspace/checks/tolerance.py` checks the triangle formula and these actual elementary collapses for all 33,866 labelled graphs on 2–6 vertices; it is not the all-orders or attaching-map proof.

## originality

PASS

The supported distinct claim is the full integral homotopy classification at t=1 for arbitrary unfilled graph inputs. Neither the retrieved special-family statements nor the available evidence of general Leray and collapsibility results gives this classification. The disjoint-two-edge sphere and the disjoint-clique overlap in the shared domain are not new here. This is a bounded best-of-knowledge finding, not a claim of historical priority.

## value

PASS

At the first nontrivial tolerance parameter this determines the entire integral homotopy type of a natural two-complex on any graph, not just vanishing or field Betti numbers. The component-rank formula and the quadratic path–star contrast give useful structural information even for classically homotopy-equivalent graph inputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
