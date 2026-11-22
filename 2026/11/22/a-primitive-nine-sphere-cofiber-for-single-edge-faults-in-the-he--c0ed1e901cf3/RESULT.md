# A primitive nine-sphere cofiber for single-edge faults in the Heawood perfect-matching complex

## Finding
Let \(H\) be the Heawood graph, regarded as the point–line incidence graph of the Fano plane. Let \(\mathcal P(G)\) be the simplicial complex on graph edges whose faces are edge sets contained in some perfect matching of \(G\). Put \(X=\mathcal P(H)\), and, for **every** edge \(e\in E(H)\), put \(X_e=\mathcal P(H-e)\subset X\). Then
\[
X\simeq\bigvee^{16} S^2,\qquad X_e\simeq\bigvee^{7} S^2,\qquad X/X_e\simeq\bigvee^{9} S^2.
\]
The first equivalence is an established result included as context; the latter two and the following natural-map statement are the finding. The inclusion \(X_e\hookrightarrow X\) induces an injective **primitive split** integral homology map
\[
0\longrightarrow\widetilde H_2(X_e;\mathbb Z)\cong\mathbb Z^7
\longrightarrow\widetilde H_2(X;\mathbb Z)\cong\mathbb Z^{16}
\longrightarrow\widetilde H_2(X,X_e;\mathbb Z)\cong\mathbb Z^9
\longrightarrow0.
\]
All other reduced integral homology groups of \(X\) and \(X_e\) vanish, and the relative homology is zero outside degree two. Hence each single graph-edge fault kills exactly nine primitive homology generators, irrespective of which edge is deleted.

## Assumptions and scope
Index the points and lines of the Fano plane by \(0,\ldots,6\). Line \(i\) contains points \(i,i+1,i+3\) modulo seven. A graph edge is an incidence \((i,j)\) with \(j\) on line \(i\). Label the 21 incidences lexicographically by line and then point, with labels \(0,\ldots,20\). A perfect matching is seven incidences with distinct point labels and distinct line labels; a nonempty simplicial face is any nonempty subset of a perfect matching. The empty face is implicit but is omitted in the nonempty Morse face-posets. The assertion is about the *extendible-to-perfect-matching* subcomplex, not the ordinary matching complex.

For each \(e\), the quotient \(X/X_e\) denotes the geometric realization of \(X\) with the entire nonempty subcomplex \(X_e\) identified to one basepoint. This is a based CW quotient. All homology groups use integral coefficients unless a verification explicitly says otherwise.

## Proof
**Finite enumeration and exhaustive coverage.** Enumerate the image line for each of seven points by a depth-seven recursion with no repeated line. Every point has exactly three incident lines, so this enumerates all perfect matchings, with no search-space omission. It finds exactly 24 perfect matchings. Their full downward closure \(X\) has 2,201 nonempty faces with counts in dimensions zero through six
\[
(21,168,560,756,504,168,24).
\]
For every one of the 21 choices of \(e\), exactly eight perfect matchings contain \(e\), leaving 16 perfect matchings of \(H-e\). Their downward closure \(X_e\) has 1,552 nonempty faces. Its complement \(R_e=X\setminus X_e\), interpreted as the relative face set, has 649 cells.

**Exact finite Morse certificate.** On each of the three finite face sets \(X\), \(X_e\), and \(R_e\), use the following fully specified pairing. Initially mark every nonempty face as unmatched. For graph-edge labels \(i=0,\ldots,20\) in order, scan unmatched face bitmasks in increasing numerical order. Whenever an unmatched face \(\sigma\) does not contain \(i\) and the larger face \(\sigma\cup\{i\}\) is also unmatched in the same face set, pair those faces and remove both from the unmatched set. All pairs differ by a single graph-edge vertex. For the relative face set, only pairs with **both** faces in \(R_e\) are permitted.

The supplied standard-library verifier regenerates every bitmask from the Fano incidences; checks each pair and all codimension-one incidences; and checks the entire directed Hasse graph, directing unmatched incidences downward and matched incidences upward, by a complete topological sort. It establishes the following exact counts:

| Face set | Cells | Morse pairs | Critical cells | Hasse incidences |
|---|---:|---:|---|---:|
| \(X\) | 2,201 | 1,092 | one 0-cell; sixteen 2-cells | 8,736 |
| \(X_e\), each of 21 choices | 1,552 | 772 | one 0-cell; seven 2-cells | 6,040 |
| \(R_e\), each of 21 choices | 649 | 320 | nine 2-cells | 2,144 |

Every one of these 43 gradient graphs is acyclic, certified by visiting every vertex in the topological sort. Forman's discrete Morse theorem therefore gives CW models for \(X\) and \(X_e\) having one 0-cell and, respectively, sixteen and seven 2-cells, without 1-cells or higher cells. Since all attaching circles map into a point, these are the displayed wedges of two-spheres.

**The relative calculation, inclusion, and cofiber.** The relative cellular chain groups \(C_*(X,X_e;\mathbb Z)\) have bases indexed by the cells of \(R_e\). The verified acyclic relative pairing has unit incidence coefficients \(\pm1\), so the standard algebraic discrete-Morse cancellation theorem gives a chain-homotopy-equivalent free complex with nine generators in degree two and none in other degrees. Thus \(H_2(X,X_e;\mathbb Z)\cong\mathbb Z^9\), and all other relative integral homology groups vanish. This integral conclusion is stronger than the independently checked mod-two Betti numbers.

The long exact sequence of the pair \((X,X_e)\), together with \(H_3(X,X_e)=0\) and \(H_1(X_e)=0\), yields precisely the short exact sequence in the Finding section. Since its quotient is free abelian of rank nine, the sequence splits over \(\mathbb Z\): the image of \(H_2(X_e)\) is a primitive rank-seven direct summand of \(H_2(X)\).

Finally, both absolute spaces are wedges of two-spheres. A map between such wedges is classified up to homotopy by its degree matrix on \(\pi_2\cong H_2\). Primitive rank seven means this integer matrix has Smith normal form with seven diagonal ones. Changes of integral bases on source and target are realized by homotopy self-equivalences of the corresponding wedges (the induced \(H_2\) isomorphisms are homotopy equivalences by the simply connected Whitehead theorem). Hence the original inclusion is homotopy equivalent **as a map** to the standard inclusion \(\bigvee^7S^2\hookrightarrow\bigvee^{16}S^2\). Its homotopy cofiber is \(\bigvee^9S^2\). As \(X_e\subset X\) is a simplicial cofibration, the ordinary quotient \(X/X_e\) represents that same homotopy cofiber. This proves the claimed quotient homotopy type without assuming that an algebraic relative Morse reduction alone determines attaching maps.

## Verification
Run `python3 verify.py` using the Python standard library. The script independently reconstructs the 21 Fano incidences, verifies the unique-line-through-two-points axiom, enumerates all 24 perfect matchings, forms every face of all 22 absolute complexes and 21 relative sets, constructs every Morse pair, checks all 43 complete directed Hasse graphs acyclic, and compares the resulting Morse profiles against direct mod-two simplicial boundary reductions. Its successful output is included as `verification_output.txt`, ending with `INTEGRAL_RESULT_OK`.

The exhaustive computation covers a fixed 14-vertex graph and all 21 possible single-edge deletions. The integral conclusion does **not** follow by extrapolation from sampled instances or by treating mod-two ranks as integral ranks; it follows from the checked unit-incidence acyclic Morse pairings and the relative long exact sequence.

## Relationship to prior work
The established Heawood perfect-matching calculation gives \(X\simeq\bigvee^{16}S^2\), but does not determine \(X_e\), the cofiber, or any induced deletion map. A subsequent established Heawood symmetry calculation determines rational group characters for the intact complex, which likewise does not determine the homotopy or integral inclusion for a missing graph edge. Bayer, Jelić Milutinović and Vega introduce perfect-matching complexes and classify honeycomb graph families, not the edge-deleted Fano incidence graph. The present claim is the uniform fault classification **and its primitive integral map**, not the intact sphere count. The comparison is against inspected sources and indexed records; no assertion of absolute bibliographic uniqueness is made.

## Limitations
This is an exhaustive finite-graph theorem. It does not classify two or more simultaneous edge deletions, arbitrary incidence graphs or graph families, nor does it give an equivariant splitting of integral homology. Although the quotient is a wedge of spheres, no canonical basis of the split summand is asserted. The finite computation is fully reproducible from the included code; the proof is an exhaustive certificate rather than a short symbolic all-graphs argument. Historical equivalence under unindexed terminology remains a possible bibliographic risk.

## References
1. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (first public 2022-09-06), especially Definition 1 and the discrete-Morse framework.
2. *Perfect Morse reduction of the Heawood perfect-matching complex*, public research record `0994476b8c0d` (2026), for the already-known intact integral sphere-wedge type.
3. *Fano duality twists Heawood perfect-matching homology*, public research record `170613b1af40` (2026), for existing rational symmetry information about the intact complex.
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
