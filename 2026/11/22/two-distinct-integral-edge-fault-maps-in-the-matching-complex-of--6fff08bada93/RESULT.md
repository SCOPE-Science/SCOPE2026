# Two distinct integral edge-fault maps in the matching complex of \(C_3\square C_4\)

## Finding
Let \(G=C_3\square C_4\) be the Cartesian product of a triangle and a four-cycle. For any finite simple graph \(H\), the *ordinary matching complex* \(\mathcal M(H)\) has the edges of \(H\) as its simplicial vertices and the pairwise vertex-disjoint collections of those edges as its faces. For a graph edge \(e=\{u,v\}\) define
\[
X=\mathcal M(G),\qquad Y_e=\mathcal M(G-e),\qquad L_e=\mathcal M(G-\{u,v\}).
\]
There are two edge orbits under \(\operatorname{Aut}(G)\): edges parallel to the triangle \(C_3\), and edges parallel to the square \(C_4\). The complete nonequivariant integral homotopy profiles are
\[
\begin{array}{c|cc}
&Y_e&L_e\\\hline
 e\parallel C_3&\bigvee^{36}S^3&\bigvee^{8}S^2\\
 e\parallel C_4&\bigvee^{44}S^3&(\bigvee^{2}S^2)\vee(\bigvee^{2}S^3).
\end{array}
\]
The intact reference complex has the previously established homotopy type \(X\simeq\bigvee^{44}S^3\); the new findings concern the faulted complexes, their links, and their **natural inclusion maps** \(i_e:Y_e\hookrightarrow X\).

For a \(C_3\)-parallel edge, \(i_e\) induces a primitive split injection
\[
0\longrightarrow\mathbb Z^{36}\xrightarrow{(i_e)_*}\mathbb Z^{44}
\longrightarrow\mathbb Z^8\longrightarrow0,
\qquad X/Y_e\simeq\bigvee^{8}S^3.
\]
For a \(C_4\)-parallel edge, the homology groups of source and target have *equal rank* forty-four, yet \((i_e)_*:H_3(Y_e;\mathbb Z)\to H_3(X;\mathbb Z)\) has rank forty-two, primitive rank-two kernel and free rank-two cokernel. Its integer Smith normal form has forty-two diagonal ones and two zeros, and
\[
X/Y_e\simeq(\bigvee^2S^3)\vee(\bigvee^2S^4).
\]
All other reduced integral homology groups of \(X\) and \(Y_e\) vanish. Thus the square-direction edge fault is invisible to the Betti numbers of the two spaces but not to the natural persistence map.

## Assumptions and scope
The graph has twelve vertices \((r,c)\) with \(r\in\mathbb Z/3\) and \(c\in\mathbb Z/4\); two vertices are adjacent when exactly one coordinate changes by an edge of its respective cycle. It is a simple four-regular graph with twenty-four edges. The representative \(C_3\)-edge joins \((0,0)\) and \((1,0)\); the representative \(C_4\)-edge joins \((0,0)\) and \((0,1)\). All graph deletions retain the unchanged endpoints unless both endpoints are explicitly deleted in the definition of \(L_e\). The result concerns exactly one deleted edge and ordinary, not perfect-matching, complexes. All homotopy and homology assertions are integral and nonequivariant.

## Proof
**Finite complexes and all edge orbits.** Number graph vertices by \(4r+c\) and graph edges lexicographically by their sorted endpoint labels. A simplex is an increasing index tuple of pairwise disjoint graph edges. Exhaustive recursive enumeration, independently testable by `verify_torus_fault.py`, yields \(2764\) faces for \(X\), \(2344\) for the triangle-direction deletion, and \(2308\) for the square-direction deletion, all counting the empty face. The two links have \(420\) and \(456\) faces, respectively. The action of \(S_3\times D_4\), permuting triangle vertices arbitrarily and acting dihedrally on the square, preserves \(G\) and is transitive on the twelve edges of each direction. Hence checking one representative from each orbit is exhaustive.

**Integral discrete-Morse certificates.** For each of the five complexes, the included program constructs its full face poset. Repeatedly it (i) removes a face \(\sigma\) and its unique immediate coface \(\tau\), provided \(\tau\) is maximal among the remaining faces, or (ii) removes one maximal cell as a critical cell. Condition (i) is precisely an elementary free-face collapse in the current face poset. The program also independently orients every original Hasse cover downward except the matched ones, which it orients upward, and proves acyclicity by a complete topological sort. An augmented matching pairs the empty face; releasing that pair gives one ordinary critical vertex.

The complete matching counts and remaining positive-dimensional critical cells are
\[
\begin{array}{c|r|r|l}
&\text{faces including empty}&\text{pairs}&\text{critical cells}\\\hline
X&2764&1360&44\text{ in dimension }3\\
Y_{C_3}&2344&1154&36\text{ in dimension }3\\
Y_{C_4}&2308&1132&44\text{ in dimension }3\\
L_{C_3}&420&206&8\text{ in dimension }2\\
L_{C_4}&456&226&2\text{ in dimension }2,\ 2\text{ in dimension }3.
\end{array}
\]
These counts are exhaustive, not sample observations. All four pure-dimensional Morse CW models are wedges of spheres, since they have one vertex and no intervening positive-dimensional cells. For the mixed link \(L_{C_4}\), the program computes the signed integer Morse boundary through unit pivots \(\pm1\) along the full matching, using the exact Schur-complement cancellation formula. Its two-by-two boundary from degree three to two is **zero over the integers**, not merely modulo two. The Morse two-skeleton is \(S^2\vee S^2\); by \(\pi_2(S^2\vee S^2)\cong\mathbb Z^2\), a degree-zero attaching map of each three-cell is nullhomotopic. Therefore the mixed link also has precisely the displayed wedge type. Independent mod-two simplicial boundary calculations agree with all five integral models.

**Relative maps.** Every matching in \(G\) either avoids \(e\) or contains it with the remainder belonging to \(L_e\). Hence \(X=Y_e\cup(e*L_e)\), with intersection exactly \(L_e\). Since \(Y_e\subseteq X\) is a simplicial cofibration,
\[
X/Y_e\simeq\Sigma L_e.
\]
Substituting the two computed link types gives the cofibers above. In the triangle direction, the integral long exact sequence reduces to \(0\to\mathbb Z^{36}\to\mathbb Z^{44}\to\mathbb Z^8\to0\). In the square direction, it reduces to
\[
0\to\mathbb Z^2\to\mathbb Z^{44}\xrightarrow{(i_e)_*}\mathbb Z^{44}\to\mathbb Z^2\to0.
\]
The kernels and cokernels are free, establishing primitiveness and the asserted Smith normal forms without assuming a nullhomotopic link inclusion. This completes both edge orbits.

## Verification
Run `python3 verify_torus_fault.py` with Python 3.10 or newer and the standard library only. The program rebuilds all five face sets, validates every elementary collapse or critical maximal removal, independently detects absence of cycles in every complete reversed-cover Hasse graph, performs exact signed integral chain cancellations, verifies the final Morse differential vanishes, independently recomputes reduced mod-two Betti numbers from the original simplicial boundaries, and exhaustively checks the two graph-edge orbits. `verification_output.txt` records a successful execution; its concluding line is `TWO_EDGE_ORBITS_INTEGRAL_RELATIVE_HOMOTOPY_PASS`. The finite enumeration is exhaustive for the stated twelve-vertex graph; no inference for larger tori is made.

## Relationship to prior work
Matsushita's 2018–2019 small-grid matching-complex theorem concerns nonperiodic two-row grids and general line-graph constructions, not this doubly periodic graph or its one-edge faults. Goyal, Shukla and Singh's 2021 manuscript concerns rectangular \(P_3\square P_n\) grids and likewise does not determine the present periodic pair. A previously published exact computation of \(\mathcal M(C_3\square C_4)\) establishes the intact \(44\)-sphere wedge and its symmetry character; that baseline is credited here and is not new. A separately published six-orbit edge-fault result concerns the different rectangular graph \(P_3\square P_4\), for which all six natural deletion maps are split injective; it neither covers nor implies the noninjective square-direction map above. The general deletion–link cofibration is standard but does not supply these two link homotopy types or the actual integral map ranks. The closest indexed statements and accessible full texts were compared by graph identity, boundary conditions, link types, and implications, rather than by titles alone.

## Limitations
This is an exact finite calculation, not a classification of all toroidal dimensions, simultaneous edge faults, equivariant maps, or canonical bases for the free homology groups. The baseline previously published intact-complex calculation and the abstract deletion–link cofibration are not novel. Though the cited accessible texts and indexed records do not imply the edge-fault dichotomy, an unpublished or unindexed equivalent calculation cannot be excluded. No independent external mathematical audit is asserted.

## References
1. T. Matsushita, *Matching complexes of small grids*, arXiv:1812.11000v1 (first public 2018-12-28), full HTML at https://arxiv.org/html/1812.11000v2 .
2. S. Goyal, S. Shukla, A. Singh, *Matching complexes of 3 × n grid graphs*, arXiv:2106.09915v1 (first public 2021-06-18), https://arxiv.org/abs/2106.09915 .
3. *The matching complex of \(C_3\square C_4\): forty-four three-spheres and its full row-column character*, public mathematical record, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-the-matching-complex-of-c-3-square-c-4-forty-four-three-spheres--fb0b9d6e31bd .
4. *Six edge-orbit homotopy responses of the \(3\times4\) grid matching complex*, public mathematical record, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-six-edge-orbit-homotopy-responses-of-the-3-times4-grid-matching--374b91241af5 .
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
