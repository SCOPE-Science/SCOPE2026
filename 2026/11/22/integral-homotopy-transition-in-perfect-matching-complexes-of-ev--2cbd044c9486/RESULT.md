# Integral homotopy transition in perfect-matching complexes of even bipyramids

## Finding
For \(m\in\{3,4,5\}\), let \(B_{2m}=C_{2m}*\overline{K}_2\) be the bipyramid graph on a cycle of \(2m\) rim vertices with two nonadjacent apices, each adjacent to every rim vertex. Let \(\mathcal P(B_{2m})\) be the simplicial complex on graph edges whose facets are the perfect matchings of \(B_{2m}\). Then, integrally,
\[
\begin{aligned}
|\mathcal P(B_6)|&\simeq\bigvee^{4}S^1,\\
|\mathcal P(B_8)|&\simeq\bigvee^{3}S^2,\\
|\mathcal P(B_{10})|&\simeq S^2\vee S^3\vee S^3.
\end{aligned}
\]
The decagonal bipyramid gives the first mixed-dimensional reduced homology among the consecutive even bipyramid sizes \(2m=4,6,8,10\); the four-rim octahedral case was previously determined and is not part of this new classification.

## Assumptions and scope
The rim is the simple graph \(C_{2m}\), without diagonals. The two apex vertices are **not** adjacent to each other. The join notation \(*\) here denotes the **graph join**, whereas the wedge symbol in the conclusion denotes a topological wedge. A face of \(\mathcal P(B_{2m})\) is any subset of a graph perfect matching, not an arbitrary graph matching. Geometric realization is the standard finite simplicial realization. No claim is made for \(m\ge6\).

## Proof
**Facet enumeration.** Label the rim \(0,\ldots,2m-1\) cyclically and the two apices \(u,v\). Every perfect matching contains exactly one edge \(u a\) and exactly one edge \(v b\), where \(a,b\) are distinct rim vertices. The rim vertices remaining after deleting \(a,b\) form the two interior paths between them. Both paths have an even number of vertices exactly when \(a\) and \(b\) have opposite parity. In that case each path has a unique perfect matching, because its endpoint edge is forced recursively. Thus the \(2m\) choices of \(a\) and \(m\) choices of \(b\) of opposite parity yield exactly \(2m^2\) distinct facets, each of \(m+1\) edges. The independent exhaustive graph-recursion routine in the verification program reconstructs precisely this set.

**Elementary collapses.** In `certificates/bipyramid-collapse.json`, the cases indexed `3`, `4`, `5` contain explicit ordered pairs of simplices \((\sigma,\tau)\), with \(\tau\) the unique immediate coface of \(\sigma\) at the moment of deletion. The checker independently builds the facet complex, checks every free-face assertion against the *current* full face set, deletes each pair, and verifies the complete final face set and its simplicial closure. Therefore these are homotopy-preserving elementary simplicial collapses, not merely chain cancellations. The verified numerical data, recording the number of nonempty simplices in each dimension, are

| \(m\) | Facets | Initial nonempty face counts in dimensions \(0,1,\ldots,m\) | Collapse pairs | Final face counts by dimension |
|---|---:|---|---:|---|
| 3 | 18 | \((18,75,72,18)\) | 83 | \((7,10)\) |
| 4 | 32 | \((24,148,256,160,32)\) | 288 | \((8,20,16)\) |
| 5 | 50 | \((30,245,610,645,300,50)\) | 904 | \((10,26,26,10)\) |

**The six-rim case.** The collapsed core is a connected graph with seven vertices and ten edges. The checker's graph traversal proves connectivity. Contracting a spanning tree proves that the graph has the homotopy type of a wedge of \(10-7+1=4\) circles.

**The eight-rim case.** The collapsed core is two-dimensional. The certificate supplies a spanning tree of its one-skeleton and an ordered list of triangles. Starting with the tree, each listed triangle has two already-known boundary edges and supplies the third; the checker verifies that *all* non-tree edges are obtained. In the standard spanning-tree presentation of the fundamental group, this is a sequence of eliminations of every generator, proving \(\pi_1=0\). The Euler characteristic is \(8-20+16=4\), so \(H_2\cong\mathbb Z^3\), since a connected simply connected two-complex has no \(H_1\), no homology above degree two, and its second homology is free. Maps of three two-spheres representing a basis of \(\pi_2\cong H_2\), followed by the homological Whitehead theorem, give \(\bigvee^3 S^2\).

**The ten-rim case.** The same tree-and-triangle certificate proves that the three-dimensional collapsed core is simply connected. Its cellular chain groups are free of ranks \((10,26,26,10)\) in degrees zero through three. Let \(\partial_3\) be the signed simplicial boundary map from ten tetrahedra to 26 triangles, in the lexicographically sorted oriented bases of the checker. The certificate identifies an eight-by-eight subdeterminant of \(-1\): row indices \((0,1,5,9,11,15,18,21)\) and column indices \((0,1,2,3,4,5,6,7)\), all zero-based. It also supplies two linearly independent integer kernel vectors
\[
(1,-1,1,-1,0,0,0,0,1,0),\qquad
(0,0,0,0,1,-1,1,-1,0,1).
\]
The checker verifies the minor and both kernel equations exactly over the integers. Consequently \(\operatorname{rank}\partial_3=8\). The unit minor also implies that the image is a primitive rank-eight subgroup of the free triangle chain group: all eight nonzero Smith invariants equal one. Thus \(H_3\cong\mathbb Z^2\) and \(H_2\) has no torsion. By Euler characteristic \(10-26+26-10=0\), and \(H_0\cong\mathbb Z\), \(H_1=0\), its free second homology has rank one.

To upgrade homology to homotopy, collapse the spanning tree of the simply connected three-complex. Its two-skeleton is a simply connected two-dimensional CW complex, hence is homotopy equivalent to a wedge of second-dimensional spheres. Under this identification, the attaching maps of the ten three-cells lie in \(\pi_2\), which the Hurewicz isomorphism identifies with free \(H_2\). Their cellular degrees are the columns of \(\partial_3\) after unimodular basis changes, and their image is primitive of rank eight. Integer row and column operations therefore cancel eight degree-one attaching pairs, leaving one \(S^2\) and two trivially attached \(S^3\)'s up to homotopy. Equivalently, a map from \(S^2\vee S^3\vee S^3\) realizing integral homology generators is a homology equivalence between simply connected CW complexes and hence a homotopy equivalence. This proves the assertion.

## Verification
The self-contained standard-library program `src/verify_bipyramid.py` reads `certificates/bipyramid-collapse.json` and can be run with `python3 src/verify_bipyramid.py`. It reconstructs all perfect matchings by two different methods, enumerates all simplices, verifies every collapse and final face, verifies the explicit graph or fundamental-group elimination, and checks the signed integral boundary witnesses. `verification_output.txt` records the actual complete run. The proof does not extrapolate from finite experiments: each of the three claimed graphs is exhaustively checked.

## Relationship to prior work
Chandrakar, Chau, Goyal, Karki and Subhash (first public 13 November 2026) determine perfect-matching complex homotopy for **open three-row rectangular grid graphs**, not for bipyramids. Bayer, Jelić Milutinović and Vega study honeycomb perfect-matching complexes; their graphs and classifications differ from the cycle-with-two-apices family here. Agarwal and Basak (first public 31 August 2026) classify **cubic** Möbius and circular ladders, again different graphs. The known octahedral four-rim perfect-matching complex, with five first-homology generators, is treated solely as a boundary comparison, not a new claim. Importantly, the previously studied **ordinary** matching complex of the octagonal bipyramid allows all partial matchings; it does not compute the *perfect-matching extendibility* subcomplex classified here. Searches and comparisons did not identify a covering published homotopy theorem for these three even bipyramids, but this is not a proof of publication priority.

## Limitations
The conclusions are topological homotopy equivalences over the integers, not canonical equivariant equivalences or PL-homeomorphism statements. No general recurrence or formula for even bipyramids beyond the ten-rim case is established. The proof uses exhaustive finite certificates and a standard exact-arithmetic checker, not independent mathematical validation. Unindexed or inaccessible equivalent literature may exist.

## References
1. H. Chandrakar, T. Chau, S. Goyal, R. Karki and B. Subhash, *Perfect Matching Complexes of \(3\times 2n\) Grid Graph*, arXiv:2611.18058 (first posted 2026-11-13), https://arxiv.org/abs/2611.18058.
2. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first posted 2026-08-31), https://arxiv.org/abs/2608.30601.
3. M. Bayer, S. Jelić Milutinović and L. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, 2023, https://doi.org/10.37236/11525.
