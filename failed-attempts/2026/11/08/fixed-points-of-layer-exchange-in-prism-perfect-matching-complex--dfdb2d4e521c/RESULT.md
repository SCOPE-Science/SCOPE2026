# Fixed points of layer exchange in prism perfect-matching complexes

## Finding

**Theorem.** Let \(H\) be any finite simple graph on \(n\geq1\) vertices, and let \(p(H)\) denote its number of perfect matchings. Form the Cartesian prism \(P=H\square K_2\). Let \(\mathcal M_p(P)\) be the simplicial complex whose simplices are edge sets extendible to perfect matchings of \(P\), and let \(\tau\) exchange the two copies of \(H\). The **geometric fixed-point space** \(|\mathcal M_p(P)|^\tau\) has integral homotopy type

\[
|\mathcal M_p(H\square K_2)|^\tau\simeq
\begin{cases}
\bigvee^{p(H)}S^{n/2-1},&n\text{ even},\\
\mathrm{pt},&n\text{ odd}.
\end{cases}
\]

Here an empty wedge is a point. For \(n=2\) the wedge of zero-spheres means \(p(H)+1\) discrete points. In particular, the reduced integral homology in even order is free of rank \(p(H)\), concentrated in degree \(n/2-1\); when \(p(H)=0\) the fixed space is contractible.

**Circular-ladder instance.** For each cycle \(H=C_n\) with \(n\geq3\), the fixed space is contractible for odd \(n\), and is \(S^{n/2-1}\vee S^{n/2-1}\) for even \(n\). The reduced Lefschetz number of layer interchange acting on the *entire* perfect-matching complex is \(0\) for odd \(n\) and \(2(-1)^{n/2-1}\) for even \(n\). More generally, for any \(H\) it equals \(p(H)(-1)^{n/2-1}\) when \(n\) is even and zero otherwise.

## Assumptions and scope

The graphs are finite, loopless and without multiple edges; they need not be connected and may have isolated vertices. The prism vertices are \((v,a)\), with \(v\in V(H)\) and \(a\in\{0,1\}\); its edges are the rungs \(r_v=\{(v,0),(v,1)\}\), and the horizontal pairs \(e_0=\{(u,0),(v,0)\}\), \(e_1=\{(u,1),(v,1)\}\) for every \(e=\{u,v\}\in E(H)\). The involution exchanges the horizontal edges in each pair and fixes each rung. The fixed-point space means pointwise fixed points of the geometric realization, not the subcomplex of individually fixed vertices (which would only involve rungs).

A matching in \(H\) is a set of vertex-disjoint edges. A perfect matching covers every vertex. For \(n\) odd there are none. Every prism possesses a perfect matching given by all rungs, so its perfect-matching complex is nonvoid even if \(H\) has none.

## Proof

**1. Fixed-point simplex identification.** For a simplicial automorphism \(\tau\), each point in its geometric fixed set lies in a unique minimal \(\tau\)-stable face. Within a stable face, barycentric coordinates are constant along each \(\tau\)-orbit of vertices. Therefore the geometric fixed set is canonically triangulated by taking as vertices the barycenters of those vertex-orbits whose unions are simplices and as faces the compatible collections of such orbits.

Here the orbits are singleton rungs \(\{r_v\}\) and pairs \(\{e_0,e_1\}\). Let \(T(H)\) have a vertex \(R_v\) for each \(v\in V(H)\), and a vertex \(D_e\) for each \(e\in E(H)\). A set of these tile vertices is a face when their underlying vertex supports in \(H\) are pairwise disjoint: support of \(R_v\) is \(\{v\}\), support of \(D_{\{u,v\}}\) is \(\{u,v\}\). A \(\tau\)-stable face of \(\mathcal M_p(P)\) cannot include a rung together with a horizontal edge at the same base vertex, nor two horizontal pairs sharing a base vertex, since it is a matching in \(P\). Conversely, every disjoint collection of tile supports determines an edge set in \(P\), extendible to a perfect matching by inserting all remaining rungs. Hence these are exactly the stable faces. The orbit-barycenter identification gives a **homeomorphism**

\[
|\mathcal M_p(H\square K_2)|^\tau\cong |T(H)|.
\]

**2. An acyclic matching.** Fix a total order on \(V(H)\). For a face \(F\in T(H)\), let \(D(F)\subseteq E(H)\) be its set of dimers, and let \(U(F)=V(H)\setminus\bigcup_{e\in D(F)}e\) be its free vertices before adding monomers. If \(U(F)\neq\varnothing\), put \(u(F)=\min U(F)\). Pair the two faces differing by toggling the monomer \(R_{u(F)}\), except that the empty face has no partner in the ordinary (nonaugmented) face poset. If \(U(F)=\varnothing\), do not pair \(F\). This is well defined: the lower and upper faces of every pair have identical dimer sets, and the same selected free vertex, so no face belongs to two pairs.

For acyclicity orient every unmatched Hasse cover from its larger face to its smaller face, and every matched cover upward. An upward arrow adds only a monomer. Hence the number of dimers never increases along a directed path. In any directed cycle it is constant. With the dimer set fixed, the selected free vertex \(u\) is fixed; the only upward arrows add \(R_u\). The matched cover involving \(R_u\) is never directed downward, and all other covers remove monomers. Thus a cycle is impossible. This proves global acyclicity, not just acyclicity in each dimer fiber.

**3. Critical cells and attaching maps.** The exceptional unpaired singleton \(\{R_{\min V(H)}\}\) is one critical zero-cell. Every other critical simplex has \(U(F)=\varnothing\), i.e. its dimers constitute a perfect matching of \(H\), and it has no monomers. Conversely every perfect matching of \(H\) gives exactly one critical simplex containing \(n/2\) dimer vertices, hence of dimension \(n/2-1\). When \(n\) is odd, there are no such simplices. Discrete Morse theory therefore produces a CW complex with one vertex and precisely \(p(H)\) cells of dimension \(n/2-1\), and no other cells. If this dimension is positive all attaching maps are constant since the lower skeleton consists only of a point; if the dimension is zero we obtain exactly \(p(H)+1\) points. The asserted integral homotopy equivalence follows in all cases.

**4. Lefschetz formula.** For a finite simplicial automorphism, the Lefschetz number of its action on rational homology equals the Euler characteristic of its geometric fixed set (e.g. by the orbit subdivision and cellular fixed-point formula). Subtracting the degree-zero contribution yields the reduced Lefschetz number, equal here to \(p(H)(-1)^{n/2-1}\) in even order and \(0\) in odd order. For a cycle, the number of perfect matchings is exactly two if the length is even and zero if odd.

## Verification

The accompanying standalone `verify.py` uses **two independent constructions**: it enumerates perfect matchings of \(H\square K_2\) and tests invariant subsets of those matchings; it separately enumerates disjoint monomer-dimer tiles on \(H\). Exact equality of these face sets is checked. It then verifies every matched cover and performs a complete topological sort of the directed Hasse graph. It also compares the reduced Euler and Lefschetz quantities. All cycle base graphs with \(3\leq n\leq10\) and nine additional graphs (including \(K_4\), \(K_{3,3}\), disjoint edges, and edgeless graphs) passed. For \(K_{3,3}\), the fixed complex has \(286\) faces and exactly six critical two-cells. The script concludes with `ALL_VERIFY_OK` and `ALL_GRAPH_FAMILY_VERIFY_OK`. Those experiments check the construction on finite inputs; the argument above proves the assertion uniformly.

Run the bundled code with `python3 verify.py`. No external Python packages are required. The associated `verify_output.txt` is its recorded output.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega (2023) define perfect-matching complexes and classify several honeycomb examples by discrete Morse methods. The primary paper's definition, introductory examples and the honeycomb theorems were inspected. Its results concern the ordinary homotopy types of honeycomb perfect-matching complexes, not the layer-exchange fixed set of arbitrary Cartesian prisms.

Agarwal and Basak's 2026 article studies the ordinary independence and perfect-matching complexes of Möbius and circular ladders, providing the direct recent motivation. Its indexed 2026-09-14 expanded version describes the nonequivariant homotopy type of the circular-ladder perfect-matching complex. The present theorem concerns **pointwise fixed spaces of the layer-exchange involution**, and applies to arbitrary graphs \(H\), not only cycles. The complete manuscript of that expanded version was not accessible for a page-by-page comparison. Searches for monomer-dimer tile complexes, prism layer-swap fixed-point topology, alternate formulations as independence complexes of tile-conflict graphs, and broader covering theorems did not identify a result implying the theorem. Such absence of results is not proof of novelty.

## Limitations

The theorem does not classify the nonequivariant homotopy type of \(\mathcal M_p(H\square K_2)\), all its homology representations, or fixed spaces of other graph automorphisms. The result requires an actual layer-exchange involution and the indicated perfect-matching-complex definition. A closely relevant expanded 2026 preprint was available through its public abstract/metadata but not full-text inspection; a previously unindexed or inaccessible stronger theorem could overlap. The discrete-Morse proof establishes homotopy equivalence, not a natural equivariant deformation retraction of the full perfect-matching complex.

## References

1. Margaret Bayer, Marija Jelić Milutinović, and Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics 30(2), P2.45 (2023). https://doi.org/10.37236/11525 .
2. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (2026; initial posting 2026-08-31, expanded version 2026-09-14). https://arxiv.org/abs/2608.30601v2 .
3. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete-Morse background).
