# Quadratic sphere wedges in one-tolerance complexes of squared cycles

## Finding
For every integer \(n\ge 9\), let \(G_n=C_n^2\) be the simple graph with vertex set \(\mathbb Z/n\mathbb Z\), in which two distinct vertices are adjacent precisely when their cyclic distance is one or two. Let \(K_n=\operatorname{Cl}(G_n)\) be the **filled clique complex** and let
\[
X_n=\mathcal T_1(K_n)=\{\sigma\subseteq\mathbb Z/n\mathbb Z: \text{there is }v\in\sigma\text{ with }\sigma\setminus\{v\}\in K_n\}\cup K_n.
\]
Then there is an integral homotopy equivalence
\[
\boxed{|X_n|\simeq\bigvee^{(n^2-7n-2)/2}S^2.}
\]
Equivalently, the reduced integral homology is free abelian of rank \((n^2-7n-2)/2\) in dimension two and vanishes in every other dimension. In particular, the ranks at \(n=9,10,11,12\) are \(8,14,21,29\).

## Assumptions and scope
All complexes are finite abstract simplicial complexes and all homotopy equivalences are ordinary (not equivariant). Edges at cyclic distance two are present in \(G_n\); all its graph triangles are **filled** in \(K_n\). A tolerance-one face is a face of \(K_n\) enlarged by at most one vertex; the empty face is included by downward closure. For \(n\ge9\), the only three-vertex cliques of \(G_n\) are the \(n\) consecutive triples
\[\tau_i=\{i,i+1,i+2\},\qquad i\in\mathbb Z/n\mathbb Z.\]
There are no four-vertex cliques. Thus \(X_n\) has dimension three, and its tetrahedra are precisely the sets \(F_{i,j}=\tau_i\cup\{j\}\) with \(j\notin\tau_i\); some admit two such descriptions. The graph \(G_n\) has an induced chordless cycle of length at least five (for instance the alternating cyclic vertices), so this family is not covered by hypotheses requiring chordality.

## Proof
**1. Cell counts.** The one-skeleton of \(X_n\) is complete, so \(f_0=n\) and \(f_1=\binom n2\). A three-element set is a face of \(X_n\) exactly when it contains a graph edge of \(G_n\). Since \(G_n\) is 4-regular, has \(2n\) edges and exactly \(n\) graph triangles, it has \(3n\) unordered triples containing exactly two graph edges (three length-two wedges at each vertex, after excluding wedges belonging to graph triangles). Inclusion-exclusion of graph-edge incidences gives
\[f_2=2n(n-2)-3n-2n=n(2n-9).\]
The \(n\) filled triangles have \(n-3\) possible fourth vertices each. A four-set contains two consecutive triples exactly when it is four consecutive cyclic vertices; there are precisely \(n\) such sets, and none contains three. Therefore
\[f_3=n(n-3)-n=n(n-4).\]

**2. An explicit three-stage collapse.** All subscripts below are modulo \(n\). A displayed pairing \((Q,F)\) means remove the tetrahedron \(Q\) together with its free triangular face \(F\), an ordinary elementary simplicial collapse. The following pairings are performed in the indicated stages, with arbitrary order within each stage.

*Stage I.* For each \(i\) and each \(j\notin\{i-2,i-1,i,i+1,i+2,i+3,i+4\}\), pair
\[
 (\{i,i+1,i+2,j\},\ \{i,i+2,j\}).
\]
The triangle on the right has precisely one graph edge, \(\{i,i+2\}\), and its isolated third vertex \(j\) cannot complete any other consecutive triple. Consequently it is contained in that tetrahedron alone. Distinct pairs are distinct; Stage I removes \(n(n-7)\) tetrahedra. Every remaining tetrahedron is one of the following \(3n\) distinct local four-sets:
\[
A_i=\{i-2,i,i+1,i+2\},\qquad
B_i=\{i,i+1,i+2,i+4\},\qquad
C_i=\{i,i+1,i+2,i+3\}.
\]
*Stage II.* Remove the \(2n\) local tetrahedra \(A_i\) and \(B_i\) with respective faces
\[
(A_i,\{i-2,i+1,i+2\}),\qquad(B_i,\{i,i+1,i+4\}).
\]
For \(A_i\), the only other initial tetrahedron using its chosen face is \(\{i-2,i+1,i+2,i+3\}\), already removed in Stage I. For \(B_i\), the only other initial tetrahedron using its chosen face is \(\{i-1,i,i+1,i+4\}\), likewise removed in Stage I. Thus these faces are free when used.

*Stage III.* Remove each remaining \(C_i\) with the face
\[
 (C_i,\{i,i+1,i+3\}).
\]
Among tetrahedra containing that face, the only other possible one is \(B_{i-1}\), already removed in Stage II. Thus these are elementary collapses as well. All congruence exclusions above are valid for every \(n\ge9\); none of the enumerated local tetrahedra collide. Exactly \(n(n-7)+2n+n=n(n-4)\) tetrahedra are removed. Consequently \(X_n\) collapses to a **two-dimensional** simplicial complex \(Z_n\) with \(f_2(Z_n)=f_2(X_n)-f_3(X_n)\).

**3. Simple connectivity.** Let \(T\) be any spanning tree of \(G_n\). The complex \(X_n\) has all possible one-simplices. For any graph edge \(\{u,v\}\) in the complete one-skeleton, the unique \(T\)-path from \(u\) to \(v\) has successive edges \(\{w_k,w_{k+1}\}\subseteq T\). Each triangle \(\{u,w_k,w_{k+1}\}\) whose vertices are distinct belongs to \(X_n\), since it contains the tree edge \(\{w_k,w_{k+1}\}\). Fan homotopies replace \(\{u,v\}\) by its tree path. Every edge loop is thereby homotopic to a loop in a tree and is nullhomotopic. Hence \(\pi_1(X_n)=0\), and collapses preserve this property, so \(\pi_1(Z_n)=0\).

**4. Integral homology and homotopy.** As \(Z_n\) is connected and simply connected, the degree-one boundary has rank \(n-1\) and the degree-two boundary has rank \(\binom{n}{2}-(n-1)=\binom{n-1}{2}\). The two-dimensional complex \(Z_n\) has no degree-three cellular boundary. Its second homology is therefore a subgroup of a free abelian group of rank
\[
\begin{aligned}
\beta_2&=n(2n-9)-n(n-4)-\binom{n-1}{2}\\
&=\frac{n^2-7n-2}{2}.
\end{aligned}
\]
It is free abelian with precisely this rank; all other reduced integral homology groups vanish. Choose a basis of \(H_2(Z_n;\mathbb Z)\). The Hurewicz isomorphism for the simply connected space \(Z_n\) represents these elements by maps of two-spheres. Their wedge induces an isomorphism on all integral homology, and the homological Whitehead theorem for simply connected CW-complexes yields the asserted homotopy equivalence. \(\square\)

## Verification
The standalone `verify.py` independently enumerates all faces of dimensions two and three directly from graph edges and consecutive triples; checks the exact face formulas; and **replays all three stages** of the collapse, testing at each individual pairing that the triangular face currently has exactly one incident tetrahedron. For every integer \(9\le n\le30\), all such exact combinatorial checks pass, including the final face counts and second Betti ranks. Independently, for \(9\le n\le16\), exact bitwise elimination over \(\mathbb F_2\) verifies the degree-three boundary has full column rank. `verification_output.txt` contains the recorded program output. These finite experiments corroborate but do not replace the unrestricted three-stage proof above. Reproduce with `python3 verify.py` (Python 3 standard library only).

## Relationship to prior work
Kim and Lew introduced tolerance complexes and proved general Leray bounds (arXiv:2109.03030, first publicly posted 7 September 2021). Selvaraja's arXiv:2611.14384v1, first publicly posted 10 November 2026, proves collapsibility results for tolerance complexes of **chordal** graph clique complexes and further general Leray bounds. The graphs \(C_n^2\) for \(n\ge9\) are nonchordal, and these bounding results give neither the number of integral two-spheres nor a homotopy classification for the present family. Related graph-power topology results for higher cut complexes, neighborhood complexes and two-independence complexes concern different simplicial constructions; even when the graph parameter is the same, their conclusions do not determine this tolerance complex's homotopy type.

## Limitations
The statement covers the **filled** clique complexes of squared cycles only at tolerance one and \(n\ge9\). It does not address other cycle powers, higher tolerances, or automorphism actions on integral homology. The proof concerns ordinary homotopy, not simple-homotopy classification of the final sphere wedge. 

## References
1. M. Kim and A. Lew, *Leray numbers of tolerance complexes*, arXiv:2109.03030 (first posted 7 September 2021), https://arxiv.org/abs/2109.03030.
2. S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384v1 (first posted 10 November 2026), https://arxiv.org/abs/2611.14384.
