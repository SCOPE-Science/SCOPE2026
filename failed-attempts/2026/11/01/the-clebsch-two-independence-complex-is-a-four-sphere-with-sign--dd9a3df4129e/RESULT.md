# The Clebsch two-independence complex is a four-sphere with sign orientation

## Finding
Let \(C\) be the 16-vertex 5-regular Clebsch graph, equivalently the folded five-cube. Its two-independence complex \(X=\operatorname{Ind}_2(C)\) is the simplicial complex of vertex sets whose induced graph components each have at most two vertices. Then
\[
X\simeq S^4,\qquad \widetilde H_i(X;\mathbb Z)=\begin{cases}\mathbb Z&i=4,\\0&i\ne4.\end{cases}
\]
Under the canonical full graph automorphism group \(G\cong (\mathbb Z/2)^4\rtimes S_5\), every translation acts as \(+1\) on \(\widetilde H_4(X;\mathbb Z)\), whereas a permutation of the five folded-cube edge directions acts by its sign. Thus the complete **integral orientation character** is
\[
\chi_X(t,\sigma)=\operatorname{sgn}(\sigma)\quad(t\in(\mathbb Z/2)^4,\ \sigma\in S_5).
\]
In particular \(X/G\) is rationally acyclic: \(\widetilde H_i(X/G;\mathbb Q)=0\) for all \(i\).

## Assumptions and scope
Represent vertices by the integers \(0,1,\ldots,15\), interpreted as 4-bit words. Vertices \(a\ne b\) are adjacent if and only if \(\operatorname{wt}(a\mathbin{\mathrm{xor}}b)\in\{1,4\}\). This realizes the 5-regular Clebsch graph, not its 10-regular complement. A vertex subset \(F\) is a face of \(X\) exactly when every vertex of the induced subgraph \(C[F]\) has degree at most one, equivalently when \(F\) contains no three-vertex wedge (a center with two selected neighbors). Throughout, simplices carry the increasing numerical vertex order for their integral orientations.

The group description can be seen without relying on a graph-library convention. Put \(V=\{y\in\mathbb F_2^5:\sum_i y_i=0\}\). Write \(v_i=\mathbf 1+e_i\) for \(i=0,\ldots,4\); the five weight-four vectors satisfy \(\sum_i v_i=0\), and any four form a basis for \(V\). Two vertices \(y,z\in V\) are adjacent exactly when \(y+z\in\{v_0,\ldots,v_4\}\). Translations by \(V\) and permutations of the five coordinates supply \(16\cdot120=1920\) distinct graph automorphisms. There can be no others: an automorphism fixing a vertex permutes its five neighbors, and the ten other vertices are each uniquely identified by the corresponding two neighbors of that vertex. Hence the vertex stabilizer injects into \(S_5\) and \(G=V\rtimes S_5\).

## Proof
**Finite face poset and a complete acyclic matching.** Exhaust over all \(2^{16}\) subsets with the induced-degree test. The resulting nonempty face vector, in dimensions \(0\) through \(7\), is
\[
(16,120,400,660,576,280,80,10),
\]
with 2,142 nonempty simplices. An independent description forbids the 160 distinct wedges obtained by choosing two neighbors of each of 16 centers; enumerating subsets that contain none of these wedges gives exactly the same face family.

Start with all nonempty faces unmatched. For vertices \(j=0,1,\ldots,15\), in that order, match every still-unmatched face \(F\) lacking \(j\) with \(F\cup\{j\}\) whenever both remain unmatched. This is a fixed sequence of element matchings; the bundled program also verifies acyclicity directly. Specifically, orient each unmatched covering relation from a higher-dimensional face to its codimension-one face and reverse each matched relation. The resulting directed Hasse graph has 9,280 arrows, and a topological sort visits every one of the 2,142 nonempty faces. Exactly 1,065 pairs are matched. The critical faces consist of one vertex, five 3-faces and six 4-faces, with no others. In increasing integer-bitmask order their masks are
\[
(556,16428,16652,32812,33292)
\]
and
\[
(17044,18724,24856,33128,34328,37412),
\]
respectively. Thus ordinary discrete Morse theory gives a CW complex with one 0-cell, five 3-cells and six 4-cells.

**The integral attaching degrees.** To determine more than field homology, orient a face \(F=\{a_0<\cdots<a_q\}\) by this ordered list, so \(\partial F=\sum_j(-1)^j(F\setminus\{a_j\})\). For every oriented 3-simplex \(f\), define its projection \(P(f)\) to the free abelian group on critical 3-simplices by the following recursion: it is the corresponding basis vector if critical; zero if paired downward with a 2-simplex; and, if matched upward to a 4-simplex \(U\), use
\[
P(f)=-[U:f]\sum_{\substack{h\subset U,\ |h|=4\\h\ne f}}[U:h]P(h),
\]
where incidence coefficients \([U:h]\) are \(\pm1\). Acyclicity makes the recursion finite. The signed Morse differential is \(D_{ij}=\sum_{f\subset U_j}[U_j:f]P_i(f)\), with the critical cells ordered as above. Exact integer evaluation gives
\[
D=\begin{pmatrix}
-1&0&0&0&0&-1\\
1&1&0&0&0&0\\
0&-1&1&0&0&0\\
0&0&0&1&0&1\\
0&0&0&0&1&-1
\end{pmatrix}.
\]
Its first five columns form a square matrix of determinant \(-1\). Therefore the sub-CW-complex formed using these five 4-cells is simply connected, integrally acyclic and hence contractible (the 3-skeleton is a wedge of five 3-spheres, and a unimodular degree map kills its whole third homotopy group). The remaining 4-cell attaches along a map to that contractible subcomplex; it contributes one 4-sphere. This proves \(X\simeq S^4\). The argument proves an **integral homotopy type**, not only a mod-two rank computation.

**Full orientation character.** For any simplicial automorphism \(g\), the reduced Lefschetz trace is computed exactly on the face chains:
\[
\operatorname{tr}(g\mid\widetilde H_4(X;\mathbb Q))=-1+\sum_{q=0}^7(-1)^q\sum_{\substack{F\in X,\ |F|=q+1\\gF=F}}\operatorname{sgn}(g\mid_F).
\]
The \(-1\) accounts for the empty simplex. The sum is an integer, and because \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z\), it is precisely the integral orientation sign. For translation by the generator \(v_0\), the signed simplex traces in degrees 0 through 7 are \((0,-8,0,12,0,-8,0,2)\), giving reduced Lefschetz trace \(+1\). For the coordinate transposition \((0\ 1)\), the traces are \((8,24,8,-46,-32,24,24,6)\), giving \(-1\). Symmetry of the five coordinate directions implies that every generating translation and every adjacent transposition have the corresponding sign. These generate \(V\rtimes S_5\), proving \(\chi_X(t,\sigma)=\operatorname{sgn}(\sigma)\). As an independent finite confirmation, the bundled verifier constructs all 1,920 automorphisms and checks this exact trace formula separately for each; 960 have trace \(+1\) and 960 trace \(-1\).

For a finite simplicial group action, after barycentric subdivision the rational homology of the quotient identifies with the invariant rational homology. Here the only nonzero reduced rational homology is a nontrivial sign line, which has no \(G\)-invariants. Therefore the full symmetry quotient is rationally acyclic.

## Verification
Run `python3 verify_clebsch.py` with Python 3 and its standard library only. It exhaustively tests both face-membership formulations, constructs the stated matching, topologically sorts every reversed covering arrow, calculates the signed integer Morse differential and its unimodular minor, independently computes all original simplicial boundary ranks over \(\mathbb F_2\), identifies the full graph automorphism group, and checks every integral orientation trace. The exact output is included as `verify_output.txt`. The program terminates with `ALL_CHECKS_PASS`.

The independent simplicial mod-two boundary ranks in degrees 0 to 7 are \((1,15,105,295,365,210,70,10)\), with reduced Betti number 1 only in degree 4. These are corroboration; the integer Morse determinant is the step proving the stronger integral homotopy statement. The enumeration is exhaustive because the vertex set has exactly 16 elements and the group has exactly 1,920 proven elements.

## Relationship to prior work
Conant and Thistlethwaite's archive-era hypergraph independence framework defines forbidding specified hyperedges, including the natural forbidden wedges used here; their reported cubical theta-complex examples are different constructions [1]. The later higher-independence treatment of Deshpande and Singh defines the precise component-size condition, and its classification covers complete multipartite, fully whiskered, path, cycle and perfect-ary-tree families, not the folded five-cube [2]. The Clebsch graph itself and its full group are standard [3]. Other available Clebsch computations concern the ordinary independence complex, the Lovász neighborhood complex or the ordinary edge-matching complex, each with different defining faces. None of those statements determines the present two-independence complex or its orientation character. No general claim about all folded cubes is made.

## Limitations
This is the exact result for the 5-regular 16-vertex Clebsch graph and component-size parameter two; it is not a classification for higher folded hypercubes or for other independence parameters. The quotient result is rational, and gives neither integral quotient torsion nor a quotient homotopy equivalence. The group action is classified on integral top homology, not up to equivariant homotopy. The finite computations are backed by exhaustive reproducible code; this report has not undergone independent mathematical audit. Literature searches cannot exclude every unindexed equivalent computation.

## References
[1] J. Conant and O. Thistlethwaite, “Boolean formulae, hypergraphs and combinatorial topology,” first arXiv submission 2008-08-05, arXiv:0808.0739, https://arxiv.org/abs/0808.0739.

[2] P. Deshpande and A. Singh, “Higher Independence Complexes of graphs and their homotopy types,” first arXiv submission 2020-01-15, arXiv:2001.05448, https://arxiv.org/pdf/2001.05448.

[3] DistanceRegular.org, “Clebsch graph, Folded 5-cube,” https://www.math.mun.ca/distanceregular/graphs/clebsch.html (graph model and full automorphism group).
