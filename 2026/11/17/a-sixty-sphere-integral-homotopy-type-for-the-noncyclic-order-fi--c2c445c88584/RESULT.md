# A sixty-sphere integral homotopy type for the noncyclic order-five Latin-square clique complex

## Finding
Let \(L\) be the following Latin square of order five, with symbols numbered \(0,1,2,3,4\):

\[
L=\begin{pmatrix}
0&1&2&3&4\\
1&0&3&4&2\\
2&3&4&0&1\\
3&4&1&2&0\\
4&2&0&1&3
\end{pmatrix}.
\]

Let \(G(L)\) be its Latin-square graph, on the 25 cells \((i,j)\), with distinct cells adjacent exactly when they share a row, a column, or a symbol. Let \(X=\operatorname{Cl}(G(L))\) be its flag (clique) complex. Then, **over the integers and at the level of homotopy**,

\[
|X|\simeq\bigvee^{60}S^2.
\]

The same conclusion holds for every Latin square isotopic to \(L\), in particular the noncyclic isotopy class of Latin squares of order five.

## Assumptions and scope
The assertion concerns the finite simple undirected Latin-square graph defined by the explicit table above, not the partial-transversal (independence) complex and not the cyclic-group table. Isotopy allows independent relabelings of rows, columns, and symbols. Such relabelings induce graph isomorphisms, hence preserve its clique complex. The theorem is a nonequivariant integral homotopy statement; no claim is made for higher-order Latin squares or arbitrary quasigroups.

## Proof
Enumerate each nonempty subset \(F\) of the 25 cells, retaining it exactly if each pair of its cells shares a row, column, or symbol. The finite enumerator in `verify.py` gives the exhaustive face vector by cardinality

\[
(f_0,f_1,f_2,f_3,f_4)=(25,150,250,79,15).
\]

The file `verify.py` specifies a deterministic sequence of elementary collapses. At each step, take the lexicographically first available maximal face of the current cardinality (starting at five), and its first lexicographically available codimension-one face contained in exactly that maximal face. Delete this free face and the unique coface. The explicit search succeeds at every step, with 79 free-face pairs; at termination no simplex of dimension greater than two remains. Every step verifies the unique coface and preservation of downward closure, so these are simplicial elementary collapses, not homology-only reductions. The residual two-dimensional complex \(Y\) has

\[
(f_0(Y),f_1(Y),f_2(Y))=(25,150,186).
\]

The 1-skeleton is connected: lexicographic Kruskal spanning-tree selection reaches every vertex and gives 24 tree edges. Collapse the spanning tree in the standard cellular presentation of \(\pi_1(Y)\). For each retained triangular 2-face, the edge-loop boundary is a relator; when two of its three edges are already trivial as loops, its third edge becomes trivial. Starting from the 24 tree edges, the deterministic triangle-relator propagation in `verify.py` eliminates **all 126 remaining edges**, each by a specified retained triangle. Thus every generator of \(\pi_1(Y)\) is trivial, and van Kampen implies \(\pi_1(Y)=1\).

Since \(Y\) is a finite connected two-dimensional CW complex, \(H_2(Y;\mathbb Z)\) is free abelian, \(H_1(Y;\mathbb Z)=0\), and higher homology vanishes. Its Euler characteristic is

\[
\chi(Y)=25-150+186=61,
\]

so \(H_2(Y;\mathbb Z)\cong\mathbb Z^{60}\). By Hurewicz, the basis classes lift to maps of 2-spheres; their wedge induces an integral homology equivalence from \(\bigvee^{60}S^2\) to \(Y\). Both spaces are simply connected CW complexes, so the homological Whitehead theorem gives a homotopy equivalence. The elementary collapses give \(X\simeq Y\). Finally, row/column/symbol relabelings preserve adjacency, proving the isotopy clause.

## Verification
`verify.py` uses Python's standard library and reconstructs the table, all 519 nonempty faces, all 79 elementary collapse pairs, the two-dimensional spine, its spanning tree, and all 126 triangular relator eliminations. Every purported free face is checked against all currently remaining cofaces. It prints `LATIN5_NONCYCLIC_CLIQUE_PASS` only after all exact assertions succeed. See `verify_output.txt` for recorded output.

An independent second program, `crosscheck.py`, builds the full clique complex directly from an adjacency matrix and computes simplicial boundary ranks over the fields of orders two, three, five, and seven. In each characteristic it obtains Betti numbers \((0,60,0,0)\) in degrees one through four. These modular calculations corroborate, but do not substitute for, the integral homotopy proof. Run with `python3 verify.py` and `python3 crosscheck.py`; there are no third-party dependencies.

## Relationship to prior work
Cioabă and Mim (arXiv:2606.27328, first submitted 2026-06-25) determine the homology of Latin-square graph clique complexes over all fields. Their published abstract gives \(\dim H_2=(n-1)^3-I(L)\) for Latin squares of order \(n\ge5\), where \(I(L)\) counts intercalates. For this table an exhaustive test finds exactly four intercalates, yielding the already implied dimension \(60\). **That Betti number is not a new finding.** The new assertion is the actual integral homotopy equivalence and the explicit certificate that \(\pi_1(X)=1\), which cannot be inferred from vanishing first homology.

A published result entitled *Integral homotopy type of cyclic Latin-square clique complexes of odd order* covers cyclic group tables of odd order, including the distinct cyclic isotopy class at order five. Another result on the noncyclic order-five *partial-transversal complex* concerns a different simplicial complex. No previously identified published statement establishes the displayed noncyclic **clique-complex** homotopy equivalence, although inaccessible or implicit prior arguments remain possible.

## Limitations
This is a finite exact classification for a specified isotopy class, not a universal statement about Latin squares. No integral automorphism-homology module or equivariant homotopy type is determined. The most relevant 2026 source's abstract and published mathematical claims were accessible, but its full text could not be inspected during preparation, leaving a genuine risk of an implicit earlier simple-connectivity argument. There has been no independent mathematical audit.

## References
1. Sebastian M. Cioabă and Mutasim Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328, first submitted 2026-06-25. https://arxiv.org/abs/2606.27328
2. *Integral homotopy type of cyclic Latin-square clique complexes of odd order*, published-finding corpus record `2026/10/25/SCOPE-integral-homotopy-type-of-cyclic-latin-square-clique-complexes-o--290c2b5f7f37` (cyclic class, different graph).
3. *The noncyclic order-five Latin-square partial-transversal complex is a wedge of 48 two-spheres*, published-finding corpus record `2026/10/25/SCOPE-the-noncyclic-order-five-latin-square-partial-transversal-comple--db7fb57dc046` (independence complex, different object).
