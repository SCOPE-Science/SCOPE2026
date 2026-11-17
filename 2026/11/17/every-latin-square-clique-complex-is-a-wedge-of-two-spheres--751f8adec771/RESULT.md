# Every Latin-square clique complex is a wedge of two-spheres

## Finding
Let \(M=(M(r,c))\) be **any** Latin square of order \(n\ge2\), with row, column, and symbol sets each of cardinality \(n\). Define its Latin-square graph \(G(M)\) on the \(n^2\) cells, joining distinct cells precisely when they share a row, column, or symbol. Let \(I(M)\) denote the number of unordered \(2\times2\) intercalates: choices of two rows and two columns whose four entries have pattern \(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\), with \(a\ne b\).

Then the **full flag/clique complex**, not merely its two-skeleton, has integral homotopy type
\[
\boxed{\operatorname{Cl}(G(M))\simeq\bigvee^{(n-1)^3-I(M)}S^2.}
\]
The empty wedge is a point. In particular the complex is simply connected, has free second integral homology of the indicated rank, and has no other reduced homology. The statement is uniform over every Latin square, without group, parity, or associativity assumptions. It includes intercalate-bearing even-order squares and the exceptional small orders \(2,3,4\).

## Assumptions and scope
A Latin square has each of its \(n\) symbols once in each row and column. The three families of *line cliques* are all rows, columns and symbol classes. Distinct points share at most one of these line types. The clique complex contains one simplex for **every** graph clique, with all its faces. Homotopy equivalence is ordinary nonequivariant homotopy equivalence of geometric realizations. The formula does not assert a canonical decomposition or equivariant splitting.

## Proof
**1. Classify every nonline simplex.** Each graph edge belongs to exactly one of three line cliques. In any three-clique, if two incident edges share one line type then all three vertices lie in that line. Otherwise the edges have the three different types, and we call the triangle *rainbow*. For each triple of line labels \((r,c,s)\) for which \(M(r,c)\ne s\), there is exactly one rainbow triangle. Its vertices are the three distinct cells
\[
x=(r,c),\qquad y=(r,c_s),\qquad z=(r_s,c),
\]
where \(M(r,c_s)=s=M(r_s,c)\). They share, respectively, the row between \(x,y\), the symbol between \(y,z\), and the column between \(z,x\). Conversely a rainbow triangle determines uniquely its row, column and symbol edge labels, so there are exactly \(n^3-n^2=n^2(n-1)\) rainbow triangles.

Every fourth vertex adjacent to all vertices of such a triangle must be the cell \((r_s,c_s)\), and this is possible precisely when its symbol is \(M(r,c)\). To check uniqueness, a candidate in the row of \(x,y\), the column of \(x,z\), or the symbol class of \(y,z\) cannot join all three without repeating a triangle vertex; thus it must join \(x\) by the latter's symbol, \(y\) by its column, and \(z\) by its row, determining the fourth cell. This condition says exactly that the four cells form a \(2\times2\) intercalate. Furthermore any clique of at least four vertices not wholly in a line contains a rainbow triangle: three vertices in one line cannot have an adjacent fourth outside that line, because a fourth cell can share at most one column and at most one symbol with those three distinct cells. Hence the only nonline cliques of dimension at least three are the \(I(M)\) intercalate tetrahedra, with no higher nonline cliques. Every rainbow triangular facet belongs to **at most one** intercalate tetrahedron.

**2. Identify the complex before the tetrahedra.** Let \(A\) be the union of the \(3n\) full line simplices, and let \(Z\) be \(A\) with all rainbow two-simplices added. Every nonempty intersection of line simplices is a vertex or a full simplex, hence contractible. The nerve of this cover of \(A\) is a subcomplex \(L\) of the join
\[
J=D_n*D_n*D_n,
\]
where each \(D_n\) is a discrete set of \(n\) line labels in one direction. The nerve contains all edges between unlike directions and exactly the \(n^2\) triangles \((r,c,M(r,c))\); no triple of two lines of the same type intersects. The simplicial nerve theorem gives \(A\simeq L\).

For a missing triple \((r,c,s)\), the corresponding rainbow triangle is attached along the cycle \(x\mathrel{-}y\mathrel{-}z\mathrel{-}x\) in \(A\). Under the standard carrier realization of the nerve equivalence, this loop is homotopic to the boundary of the **missing** triangle with vertices the line labels \((r,c,s)\): the edge \(xy\) travels inside the row simplex, \(yz\) inside the symbol simplex, and \(zx\) inside the column simplex. More explicitly, replace each of those three paths within its contractible line simplex by two paths through its nerve vertex; their endpoints lie in the corresponding pairwise line intersections, whose nerve edges make the required three-sided loop. The composite nerve map carries those three edges, up to endpoint-preserving homotopies, to the three edges of the absent line-label triangle. This is the cellular form of the nerve theorem, and the replacements may be made simultaneously for all rainbow triangles.

Homotopy invariance of CW-cell attachment therefore gives
\[
Z\simeq L\cup_{(r,c,s):\,M(r,c)\ne s}\!\triangle^2_{r,c,s}=J.
\]
The join of three nonempty \(n\)-point discrete spaces is simply connected and has the homotopy type of a wedge of \((n-1)^3\) two-spheres (the join Künneth formula, or repeated suspension/distributivity of joins). In particular \(\pi_1(Z)=0\).

**3. Attach and remove the intercalate tetrahedra.** The full complex \(X=\operatorname{Cl}(G(M))\) is obtained from \(Z\) by attaching exactly \(I(M)\) three-simplices along their entire boundaries. Thus \(\pi_1(X)=\pi_1(Z)=0\). A facet of each of these tetrahedra is rainbow, and Step 1 shows it is contained in no other three-simplex or higher face. Collapsing each tetrahedron together with one of its free rainbow facets produces a subcomplex \(X'\) homotopy equivalent to \(X\), consisting of the line core \(A\) with only two-simplices attached along loops. Since \(A\simeq L\) and \(L\) is two-dimensional, \(X'\), and hence \(X\), has a two-dimensional CW model. These collapses do not require any assumption on \(n\) or on the intercalate overlap pattern at lower-dimensional faces.

**4. Compute the Euler characteristic and conclude.** Inclusion-exclusion for the line simplices gives
\[
\chi(A)=3n-3n^2+n^2=3n-2n^2.
\]
There are \(n^2(n-1)\) additional rainbow triangles, each with its boundary already in \(A\). The \(I(M)\) intercalate tetrahedra likewise attach along existing boundaries. Consequently
\[
\chi(X)=3n-2n^2+n^2(n-1)-I(M)=1+(n-1)^3-I(M).
\]
Because \(X\) is simply connected and has a two-dimensional CW model, \(H_2(X;\mathbb Z)\) is a subgroup of a free cellular \(C_2\), hence is free; all other positive-degree homology vanishes. Its rank is \(\chi(X)-1=(n-1)^3-I(M)\). Integral Hurewicz represents a basis by maps from two-spheres; their wedge induces an isomorphism on all homology groups. Both domain and target are simply connected CW spaces, so homological Whitehead gives the stated homotopy equivalence.

## Verification
The standalone standard-library program `verify_latin_homotopy.py` directly builds Latin-square graphs, enumerates maximal cliques independently of the line/rainbow/intercalate model, and checks all faces, the formula for the Euler characteristic, and the property that no rainbow triangle is a facet of two intercalates. It also computes all mod-two simplicial Betti numbers by exact XOR Gaussian elimination. The supplied `verify_latin_homotopy_output.txt` records tests for the cyclic group tables of orders \(2,3,4,5,6\), the Klein-four table, and a non-group order-five Latin square. For example the two order-four group tables yield \(23\) and \(15\) two-spheres, while the non-group order-five example gives \(60\). These are finite stress tests, not the proof of the universal result. Replay with `python3 verify_latin_homotopy.py`.

## Relationship to prior work
Cioabă and Mim (arXiv:2606.27328, first public June 25, 2026; Theorems 3.8 and 3.12) give the **field homology** formula \(\dim H_2=(n-1)^3-I(M)\) and higher-field-homology vanishing for \(n\ge5\). That numerical result is not new here. Previously published calculations establish the full homotopy type for *odd cyclic* Latin squares and for a particular non-group order-five Latin square, and an integral even-order abelian-group **homology module** exact sequence is also known. None of these narrower statements gives the arbitrary-Latin-square integral homotopy type or a universal simply connected two-dimensional model. The new step is the uniform full-join comparison for the rainbow-triangle stage together with free-facet removal of every intercalate tetrahedron. Prior homology computations alone cannot determine the fundamental group or homotopy type.

## Limitations
No equivariant homotopy equivalence, integral automorphism module or canonical sphere basis is claimed. The homotopy classification is for the graph clique complex, not the partial-transversal complex. The relevant sections of the closest 2026 primary paper were inspected from its accessible full text, including the Latin-square clique classification, homology theorems, and higher-homology argument. They establish homology but do not state a fundamental-group or universal homotopy classification. Unindexed work remains a priority risk; no independent mathematical audit is claimed.

## References
1. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328, first public June 25, 2026, https://arxiv.org/abs/2606.27328 .
2. *Integral homotopy type of cyclic Latin-square clique complexes of odd order*, public result of October 25, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-integral-homotopy-type-of-cyclic-latin-square-clique-complexes-o--290c2b5f7f37/RESULT.md .
3. *Intercalate correction modules in even-order Latin-square clique homology*, public result of November 1, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-intercalate-correction-modules-in-even-order-latin-square-clique--f1a50eb000f9/RESULT.md .
4. Standard simplicial nerve theorem, homotopy invariance of CW attachments, join homology, Hurewicz theorem and homological Whitehead theorem, e.g. A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.
