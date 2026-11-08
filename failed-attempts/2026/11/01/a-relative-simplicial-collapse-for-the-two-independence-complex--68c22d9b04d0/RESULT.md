# A relative simplicial collapse for the two-independence complex of the Grötzsch graph

## Finding

For the eleven-vertex Grötzsch graph \(G=\mu(C_5)\), let \(K_r=\operatorname{Ind}_r(G)\) be the complex of vertex subsets all of whose induced connected components have at most \(r\) vertices. The natural inclusion \(K_1\hookrightarrow K_2\) is a simple-homotopy equivalence realized by explicit elementary collapses:

\[
\boxed{K_2\searrow K_1\simeq S^2.}
\]

The collapse from \(K_2\) to \(K_1\) removes exactly 105 free-face pairs. In particular, the first higher-independence cutoff adds 210 nonempty faces but preserves the integral homotopy type and all inclusion-induced homology classes. This is a statement about this graph and these two cutoffs, not an assertion about all Mycielski graphs.

## Assumptions and scope

Let the five original vertices be \(0,1,2,3,4\), their clones be \(5,6,7,8,9\), and the apex be \(10\). All cycle indices in the following edge description are taken modulo five. The graph has precisely the following 20 undirected edges: five edges \(\{i,i+1\}\), ten edges \(\{5+i,i-1\},\{5+i,i+1\}\), and five edges \(\{5+i,10\}\), for \(0\le i<5\). The graph is the standard Mycielskian of the five-cycle.

For a nonempty vertex subset \(U\), let \(c(U)\) be the largest order of a connected component of the induced graph \(G[U]\). A simplex belongs to \(K_r\) exactly when \(c(U)\le r\). In particular \(K_1\) is the ordinary independence complex, while \(K_2\) is also called the dissociation complex, because the induced maximum vertex degree is at most one. The empty simplex is included in both complexes, but is not listed in the finite certificates. Each vertex subset \(U\) is encoded by the integer bitmask \(\sum_{u\in U}2^u\); the numerical encoding is machine data, not an additional mathematical hypothesis.

## Proof

**1. Exhaustive face construction.** Enumerate all 2,047 nonempty subsets of the eleven vertices and compute connected components of their induced graphs by ordinary depth-first search. This produces 102 nonempty faces of \(K_1\), with face vector by dimension \((11,35,40,15,1)\), and 312 nonempty faces of \(K_2\), with face vector \((11,55,110,95,36,5)\). The included verifier checks the defining component condition for every subset and verifies downward closure for each complex.

**2. A relative elementary collapse.** The file `proof/relative_collapse.json` lists 105 successive ordered pairs of integer-encoded faces \((\sigma,\tau)\). Replay them in that order, starting with the complete face set of \(K_2\). At each step the independent verifier checks that both faces are present, neither belongs to \(K_1\), that \(\tau\) has exactly one more vertex than \(\sigma\), and that **the only strict coface of \(\sigma\) remaining in the current complex is \(\tau\)**. Thus \(\sigma\) is a free codimension-one face and deleting the two faces is an elementary simplicial collapse. All 105 pairs are distinct. The checker verifies that the remaining faces after the final step are exactly all faces of \(K_1\). Consequently \(K_2\searrow K_1\), proving the actual inclusion is a simple-homotopy equivalence, rather than merely that both spaces have identical Betti numbers.

**3. The retained sphere.** The independent certificate `proof/morse_pairs.json` gives 50 disjoint Hasse-edge pairs in the nonempty face poset of \(K_1\). The verifier reverses the matched edge directions and directs every other Hasse edge downward, then checks all 255 oriented incidences by a topological sort; no directed cycle remains. Exactly two cells are unmatched: the vertex mask `1024`, of dimension zero, and the triangle mask `133`, of dimension two. The acyclic-matching theorem gives a CW complex with one zero-cell and one two-cell and no other cells. Since the two-cell attaches to a point, this CW complex is \(S^2\). Therefore \(K_1\simeq S^2\). Combining with Step 2 yields the claimed exact integral homotopy classification.

All enumerations are finite and exhaustive: the graph has eleven vertices, the checker visits every subset, and the two certificates contain all claimed pairings. No random sample is used in the proof.

## Verification

Run `python3 proof/verify_groetzsch.py` from an extraction of the included research files, preserving the relative names of the two JSON certificate files. The script uses only the Python standard library, constructs the graph and face sets anew, independently checks all elementary-collapse free faces and Morse acyclicity, and independently computes mod-two simplicial boundary ranks. The full recorded output is in `proof/verification_output.txt`.

The boundary ranks over \(\mathbb F_2\) for \(K_1\), in degrees one through four, are \((10,25,14,1)\). The corresponding ranks for \(K_2\), in degrees one through five, are \((10,45,64,31,5)\). Both give ordinary Betti ranks \((1,0,1,0,\ldots)\). These checks are corroboration; the integral homotopy conclusion follows from the verified collapse and acyclic-matching certificates, not from field homology.

## Relationship to prior work

Deshpande and Singh introduced and computed higher-independence homotopy types for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees [1]. Deshpande, Shukla, and Singh proved bounds and a sphere-wedge theorem for chordal graphs [2]. The Grötzsch graph contains an induced five-cycle, hence is nonchordal, and is not any of the listed families.

Goyal, Shukla, and Singh treated ordinary independence complexes of generalized Mycielskians of complete graphs [3]. Later, Carnero Bravo determined ordinary independence-complex homotopy types for generalized Mycielskians of arbitrary graphs, including cycles [5]. Those results account for the sphere homotopy type of \(K_1\), but do not imply that the natural inclusion into \(K_2\) is an elementary collapse. In particular the present new statement is the **105-pair relative simple-homotopy equivalence**; the ordinary independence-complex sphere identification is independently verified here and is not claimed as a previously unknown standalone fact.

## Limitations

The result is restricted to the eleven-vertex standard Grötzsch graph and the first two component-size cutoffs. It does not establish an all-order theorem for Mycielskians, a general stability rule for higher-independence complexes, or the homotopy types at cutoffs three and above. A complete bibliographic guarantee of novelty is not asserted; unindexed equivalent calculations remain possible. The finite proof has been checked with a reproducible verifier, but no independent mathematical audit has been performed.

## References

[1] P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first public version January 15, 2020), https://arxiv.org/abs/2001.05448.

[2] P. Deshpande, S. Shukla, and A. Singh, *Distance \(r\)-Domination Number and \(r\)-Independence Complexes of Graphs*, arXiv:2001.06775 (January 19, 2020), https://arxiv.org/abs/2001.06775.

[3] S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (May 16, 2019), https://arxiv.org/abs/1905.06926.

[4] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (June 21, 2021), https://arxiv.org/abs/2106.10863.

[5] A. Carnero Bravo, *Independence Complexes of Generalized Mycielskian Graphs*, arXiv:2601.13432 (January 19, 2026), https://arxiv.org/abs/2601.13432.
