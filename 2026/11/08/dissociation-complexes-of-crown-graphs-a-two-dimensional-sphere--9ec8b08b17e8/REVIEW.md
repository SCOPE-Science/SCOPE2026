# Scientific review: crown-graph dissociation complexes

## Correctness

**PASS.** Induced-degree identities \(d_S(a_i)=|J|-\mathbf1_{i\in J}\) and \(d_S(b_j)=|I|-\mathbf1_{j\in I}\) classify every mixed face. Counting these possibilities proves both polynomials and all facets without extrapolation. The critical topological step is an explicit simplicial retraction of the two-index complex onto the complete one-skeleton of one shore; contiguity gives a homotopy relative to that skeleton, so adjoining its simplex makes the intermediate complex contractible. Gluing the opposite-shore simplex along its complete one-skeleton yields the asserted suspension and integral homotopy wedge. Independent exhaustive testing agrees for \(n=3,\ldots,8\); mod-two boundary ranks agree for \(3\le n\le8\). The proof, not the finite test, establishes the unrestricted integral statement.

## Originality

**PASS, with residual publication-priority uncertainty.** The closest full-text results concern the ordinary independence complex of \(K_2\times K_n\) (Goyal–Shukla–Singh, arXiv:1905.06926, Proposition 3.2), the higher independence complexes of complete multipartite graphs (Deshpande–Singh, arXiv:2001.05448, Theorem 3.5), and universal maximal-dissociation bounds (Tu–Li–Du, arXiv:2103.01402, Theorems 1.1–1.2). The first changes the face condition; the second changes the edge set and predicts a wedge of circles for \(K_{n,n}\); the third has no exact crown-graph census or complex topology. None of the inspected statements logically contains the asserted \(\operatorname{Ind}_2(C_n)\) homotopy or complete face/facet classification. Published database claims on complete multipartite graphs, generalized windmills, and crown invariants were compared for implication, not just shared words. Searches cannot eliminate an unindexed equivalent treatment.

## Mathematical value

**PASS.** The higher-independence complex is a natural topological encoding of induced maximum-degree-one subsets, with established literature on its homotopy for other graph families. Deleting a *perfect matching* from \(K_{n,n}\) changes the known homotopy from \(\bigvee^{n^2-1}S^1\) to \(\bigvee^{\binom{n-1}{2}}S^2\), a dimension-changing structural effect rather than a small numerical improvement. The proof also gives an exact all-configuration census and a facet spectrum that is pure only at \(n=4\). These properties reveal the topology and nonpurity of an entire canonical regular bipartite family and provide concrete test cases for higher-independence-complex constructions.

## Limitations

No theorem on arbitrary graph products, unequal bipartite parts, or \(r\)-independence for \(r>2\) is asserted. The checker verifies only declared finite orders and mod-two homology; integral homotopy follows separately from the proof. Exact publication priority is not independently established, and independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
