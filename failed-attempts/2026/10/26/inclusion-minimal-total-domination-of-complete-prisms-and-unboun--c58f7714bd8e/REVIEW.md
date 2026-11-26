# Independent mathematical audit

## correctness

PASS

At uᵢ the selected-neighbor count is |A|−1_{i∈A}+1_{i∈B}, and the dual count holds at vᵢ. With one layer empty the other must be full, and each of its vertices is essential to the corresponding unmatched-by-others vertex. A singleton in a nonempty layer forces its matching index into the other layer, yielding a smaller dominating pair unless the set is that pair. When both layers contain at least two selected vertices, minimality forces exactly two per layer; an index in common would again give a properly contained matched pair. For disjoint indices every deletion leaves a singleton with no selected neighbor. Thus the only possibilities are the n matched pairs, two full layers, and the 6 binomial(n,4) ordered two-and-two choices on disjoint indices. At n=2 one obtains the four edges of C₄, all of size two, and at n=4 the four-vertex contributions add. For n≥6 the gap is exactly the n−5 integers from 5 through n−1. The degree, diameter and vertex transitivity follow from the two cliques, the cross-matching, and layer swap together with simultaneous index permutations. The exact proof is unrestricted; inspected the frozen subset checker and recorded output, not rerun.

## originality

FAIL

The earlier indexed crown-graph result 798a85759c22 covers the full nontrivial family under an exact neighborhood equivalence. Let H be the crown graph on the same U,V with edges uᵢvⱼ exactly when i≠j. Then N_G(uᵢ)=N_H[vᵢ] and N_G(vᵢ)=N_H[uᵢ]. Thus the hypergraphs of open neighborhoods in the prism and closed neighborhoods in the crown are identical, with the vertex-indexed edges simply permuted. Ordinary domination of H and total domination of G therefore have exactly the same feasible sets and exactly the same inclusion-minimal sets. The earlier classification for n≥3 gives all three families and the identical polynomial. Its support yields precisely the asserted gap; the symmetry and diameter facts for G are immediate from its definition. The n=2 boundary is an elementary C₄ case, not a substantive new remainder. The failure is from verified equivalent coverage, not lack of access to a Cartesian-product paper.

## value

FAIL

Unbounded gaps within a symmetric regular family are a motivated phenomenon, but the submitted result adds only the immediate same-neighborhood reinterpretation of an already classified complete profile and the trivial order-four boundary. The long gap follows directly from the old polynomial, and the graph-side properties require no additional scientific result. No distinct valuable remainder is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
