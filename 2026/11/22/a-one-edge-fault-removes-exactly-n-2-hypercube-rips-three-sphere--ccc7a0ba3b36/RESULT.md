# A one-edge fault removes exactly \(n-2\) hypercube Rips three-spheres

## Finding

Let \(Q_n\) be the graph on \(\{0,1\}^n\) with edges joining words that differ in one coordinate, and let \(e\) be any graph edge. Put \(G_n=Q_n-e\), with its **recomputed, unweighted shortest-path metric**. For each integer \(n\ge3\), define
\[
c_n=\sum_{0\le j<i<n}(j+1)\bigl(2^{n-2}-2^{i-1}\bigr).
\]
The inclusive radius-two Vietoris–Rips complex has the integral homotopy type
\[
\operatorname{VR}(G_n;2)\simeq\bigvee^{c_n-(n-2)}S^3.
\]
The wedge with zero summands is a point; thus the three-cube with one edge deleted is contractible at radius two.

More precisely, the filtration is unchanged from the intact cube at every radius at least three. At radius one, \(G_n\) is a wedge of \((n-2)2^{n-1}\) circles, one fewer than the intact cube. The integral persistent-homology barcode differs from that of \(Q_n\) by **exactly one fewer degree-one interval** \([1,2)\) and **exactly \(n-2\) fewer degree-three intervals** \([2,3)\); every other interval is unchanged. Intervals are half-open and include the lower endpoint. This comparison holds for all integer \(n\ge3\).

## Assumptions and scope

All complexes are finite abstract simplicial complexes: a subset is a face of \(\operatorname{VR}(G;r)\) if all its pairwise shortest-path distances in \(G\) are at most \(r\). All homotopy and homology assertions are integral. The vertex set of the faulted graph is unchanged. The deleted edge is not reintroduced as a length-one connection; distances are recomputed. By hypercube edge transitivity, set \(e=\{0,e_1\}\) without loss of generality, where \(e_i\) is the word with a one in coordinate \(i\).

The intact-cube theorem of Adamaszek–Adams, \(\operatorname{VR}(Q_n;2)\simeq\bigvee^{c_n}S^3\) for \(n\ge3\), is used as an established input [1]. The scale-inclusion nullhomotopy theorem of Adams–Virk [2] is used only to deduce the final barcode comparison, not the homotopy claim.

## Proof

**1. The only changed pairwise distance.** In \(Q_n-e\), the distance from \(0\) to \(e_1\) is exactly three: the four-cycle through any other coordinate supplies a three-edge path, whereas bipartiteness excludes a two-edge path. Any two words at Hamming distance at least two have multiple shortest coordinate-flip paths, and no single edge belongs to all of them: varying which required coordinate is flipped first or last supplies a geodesic avoiding the deleted edge. Any other adjacent pair retains its edge. Thus no other graph distance changes. Put \(X=\operatorname{VR}(Q_n;2)\) and \(Y=\operatorname{VR}(Q_n-e;2)\). The complex \(Y\) consists exactly of the faces of \(X\) **not containing both endpoints of** \(e\).

**2. The link of the lost edge.** Let \(L=\operatorname{lk}_{X}(e)\). Its vertices comprise
\[
a_i=e_i,\qquad b_i=e_1+e_i,\qquad 2\le i\le n,
\]
where the plus sign means disjoint coordinate support, not addition in an ambient metric. All \(a_i\) are pairwise adjacent, all \(b_i\) are pairwise adjacent, and the only edges between these two groups are \(a_i b_i\). Consequently \(L\) consists of two disjoint \((n-2)\)-simplices connected by \(n-1\) distinct rung edges. Collapsing each simplex to a point shows
\[
L\simeq\bigvee^{n-2}S^1.
\]
The cycles \(a_2a_ib_ib_2a_2\), with \(3\le i\le n\), form an **integral basis** of \(H_1(L;\mathbb Z)\). This follows by collapsing the two contractible cliques: the resulting multigraph has two vertices and \(n-1\) parallel edges, with the displayed cycles corresponding to differences from the rung indexed by \(2\).

**3. Excision and a primitive surjection.** The closed star \(\operatorname{st}_X(e)=e*L\) is contractible and
\[
X=Y\cup(e*L),\qquad Y\cap(e*L)=(\partial e)*L\simeq\Sigma L.
\]
Thus cellular excision (or the corresponding quotient of the star) gives
\[
H_k(X,Y;\mathbb Z)\cong\widetilde H_{k-2}(L;\mathbb Z).
\]
The only nonzero relative group is therefore \(H_3(X,Y;\mathbb Z)\cong\mathbb Z^{n-2}\).

For every \(i\in\{3,\ldots,n\}\), restrict to the eight vertices of the coordinate three-subcube supported on \(\{1,2,i\}\). Their radius-two Rips complex is the boundary of a four-dimensional cross-polytope, hence an oriented \(S^3\). Under the relative map
\[
H_3(X;\mathbb Z)\longrightarrow H_3(X,Y;\mathbb Z)\cong H_1(L;\mathbb Z),
\]
its fundamental class maps, up to sign, to the four-cycle \(a_2a_ib_ib_2a_2\). Indeed, the relative part of the oriented cross-polytope boundary consists of the tetrahedra containing \(e\), and deleting \(e\) from their oriented faces leaves exactly the signed edge-cycle of the link square. The \(n-2\) images form the integral basis from step 2. **Hence the map is surjective over \(\mathbb Z\)**, not merely over a field.

**4. Homology and homotopy.** The intact complex \(X\) is a wedge of \(c_n\) three-spheres by [1]. The long exact sequence of \((X,Y)\), together with step 3, yields
\[
\widetilde H_k(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{c_n-(n-2)},&k=3,\\
0,&k\ne3.
\end{cases}
\]
As \(L\) is connected, \((\partial e)*L\simeq\Sigma L\) is simply connected. The star is contractible, and \(X\) is simply connected. Van Kampen applied to the above cover implies \(\pi_1(Y)=0\). Since \(H_2(Y)=0\), the degree-two Hurewicz theorem also gives \(\pi_2(Y)=0\). Choose based three-sphere maps representing a basis of \(H_3(Y;\mathbb Z)\) via Hurewicz. Their wedge induces an integral homology isomorphism; the simply-connected homology Whitehead theorem makes it a homotopy equivalence. This establishes the asserted integral three-sphere wedge, including the contractible case.

**5. All scales and persistence.** At radius one, the complex is the connected graph \(Q_n-e\), with \(n2^{n-1}-1\) edges and \(2^n\) vertices. Its first Betti number is \((n-2)2^{n-1}\). At any radius \(r\ge3\), the only changed vertex distance, from one to three, is again admissible, so the two Rips complexes are literally equal. The degree-one classes die at radius two because \(H_1(Y)=0\); the degree-three classes die at radius three because the inclusion from the faulted radius-two complex to radius three factors through the intact radius-two complex, and the intact scale-two-to-three inclusion is nullhomotopic by [2, Proposition 3.3]. All scale complexes and connecting maps from radius three onward are unchanged, giving the stated exact barcode difference. The degree-zero part is unaffected.

## Verification

The standalone standard-library script `verify_hypercube_fault.py` independently reconstructs the graph distances with breadth-first search, checks that precisely the endpoint distance changes, enumerates every clique face at radius two, computes all boundary ranks over \(\mathbb F_2\), and checks the explicit two-clique-plus-rungs edge-link structure for \(n=3,4,5,6\). The accompanying `verification_output.txt` is its recorded execution output. Its original/faulted third Betti ranks are respectively \((1,0)\), \((9,7)\), \((49,46)\), and \((209,205)\). These finite experiments support the calculations but are not the infinite proof, which is the integral argument above.

## Relationship to prior work

Adamaszek–Adams [1] classify the intact hypercube's scale-two Rips homotopy and give the formula for \(c_n\). Adams–Virk [2] discuss independent cross-polytopal classes and nullhomotopy of inclusions between consecutive Rips scales, again with the intact Hamming metric. These known theorems provide inputs; neither states the homotopy or barcode response under a **deleted graph edge with recomputed distances**. The distinction matters: merely deleting a vertex, changing the radius, or passing to a quotient is not equivalent to the present edge fault. The structural step specific to this result is the primitive surjection from coordinate three-cube sphere classes onto the edge-link cycle lattice.

## Limitations

The argument treats exactly one missing edge and unweighted shortest-path distance for binary cubes of dimension at least three. It does not classify arbitrary simultaneous edge failures, weighted faults, or the individual homotopy types at radii at least three beyond their identity with those of the intact hypercube. The novelty comparison cannot exclude unindexed or inaccessible equivalent literature, and the computational checks are finite only.

## References

[1] M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first submitted 2021-03-01), Theorem 1 and its proof. https://arxiv.org/abs/2103.01040

[2] H. Adams and Ž. Virk, *Lower bounds on the homology of Vietoris–Rips complexes of hypercube graphs*, arXiv:2309.06222 (first submitted 2023-09-12), Proposition 3.3, Theorem 2.4 and Section 4. https://arxiv.org/abs/2309.06222

[3] S. Shukla, *On Vietoris–Rips complexes (with scale 3) of hypercube graphs*, arXiv:2202.02756 (first submitted 2022-02-06). https://arxiv.org/abs/2202.02756
