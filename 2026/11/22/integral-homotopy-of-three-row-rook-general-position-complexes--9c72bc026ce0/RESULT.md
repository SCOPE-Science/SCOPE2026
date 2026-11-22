# Integral homotopy of three-row rook general-position complexes

## Finding

Let \(n\ge3\) be an integer and let \(R_n=K_3\square K_n\) be the rook graph on three rows and \(n\) columns. Define \(\operatorname{GP}(R_n)\) as the abstract simplicial complex of all vertex sets containing no three distinct vertices on a common shortest path. Then, as an integral homotopy equivalence of geometric realizations,
\[
\boxed{\operatorname{GP}(R_n)\simeq
\left(\bigvee^{2^n}S^{n-1}\right)\vee
\left(\bigvee^n S^2\right).}
\]
For \(n=3\), both dimensions coincide and the answer is \(\bigvee^{11}S^2\); for every \(n\ge4\) there are nonzero free integral reduced homology groups in precisely degrees \(2\) and \(n-1\), of respective ranks \(n\) and \(2^n\). Moreover, the natural subcomplex formed by choosing at most one cell in each column injects on every integral homology group, with a free degree-two quotient of rank \(n\) (this includes \(n=3\)). The calculation is of homotopy type, not merely Betti numbers.

## Assumptions and scope

The graphs are finite, simple, undirected, unweighted; shortest paths use ordinary graph distance. Rows are indexed by \(r\in\{0,1,2\}\), columns by \(j\in\{1,\ldots,n\}\), and a graph vertex is a cell \((r,j)\). Two distinct cells are adjacent exactly when they share a row or a column; otherwise they are at distance two. All vertex subsets, including the empty set, are faces when they satisfy the stated condition. The symbol \(\Delta(T)\) denotes the full simplex on vertex set \(T\), and \(*\) denotes simplicial join.

## Proof

**1. Complete face classification.** A forbidden geodesic triple consists of cells \((r,j),(s,j),(s,k)\), where \(r\ne s\) and \(j\ne k\), or the transpose of this pattern. Equivalently, identify cells with edges of \(K_{3,n}\); a selected set is valid exactly when its edges form a star forest. For a direct proof, if a column contains two selected cells in rows \(r,s\), no other selected cell may occur in rows \(r,s\) at any different column, since it would complete such a forbidden triple. Moreover, at most one column can contain two selected cells: two distinct subsets of two rows from a three-element row set intersect, and their shared row would create a forbidden triple. If a column contains all three selected cells, no other column can contain a selected cell.

Put \(C_j=\{(0,j),(1,j),(2,j)\}\), and let
\[
A_n=\{\sigma:|\sigma\cap C_j|\le1\text{ for every }j\}
      =D_3*D_3*\cdots*D_3,
\]
where \(D_3\) is the discrete three-point complex and the join has \(n\) factors. For every column \(j\), unordered row pair \(\{r,s\}\), and remaining row \(t\), let
\[
B_{j;rs}=\Delta\big(\{(r,j),(s,j)\}\cup
                \{(t,k):k\ne j\}\big).
\]
The complete classification just proved gives the **equality of abstract simplicial complexes**
\[
\operatorname{GP}(R_n)
=A_n\cup\bigcup_{j,\{r,s\}} B_{j;rs}
\cup\bigcup_{j=1}^n\Delta(C_j).
\]
The last displayed triangles are the only faces with three selected cells in a single column. This is an exact union: it is not an enumeration or a homological approximation.

**2. Contractible attachments of the thickening simplices.** Set \(X_n=A_n\cup\bigcup_{j,\{r,s\}}B_{j;rs}\), temporarily omitting the final column triangles. Each \(B_{j;rs}\) is an \(n\)-simplex, hence contractible. Its intersection with \(A_n\) is
\[
 B_{j;rs}\cap A_n
 =\partial\Delta(\{(r,j),(s,j)\})
   *\Delta(\{(t,k):k\ne j\}).
\]
The second join factor is a **nonempty full simplex** because \(n\ge3\). Thus this intersection is a nonempty contractible subcomplex. Distinct thickening simplices have intersections contained in \(A_n\): outside \(A_n\), a face has a unique repeated column and a unique selected row pair in that column. Therefore when adding any \(B_{j;rs}\) to \(A_n\) and the already attached thickening simplices, its intersection with the old union is exactly \(B_{j;rs}\cap A_n\). By the homotopy gluing lemma for inclusions of finite CW subcomplexes, attaching a contractible simplex along a nonempty contractible intersection is a homotopy equivalence. Inductively,
\[
A_n\hookrightarrow X_n\quad\text{is a homotopy equivalence.}
\]
This particular inclusion, not merely an unspecified equivalence of spaces, will also give the integral homology injection.

**3. Homotopy type of the one-per-column core.** The join of two three-point discrete complexes is the complete bipartite graph \(K_{3,3}\), with first Betti number \(9-6+1=4\); hence it is \(\bigvee^4 S^1\). Joining any connected based complex \(Y\) with three discrete points is homotopy equivalent to \(\Sigma Y\vee\Sigma Y\): the three cones on \(Y\) glue along their common base, and one cone can be contracted before the other two become suspensions. Apply this with \(Y\) the preceding joins. Induction yields
\[
 A_n\simeq\bigvee^{2^n}S^{n-1},\qquad n\ge2.
\]
In particular \(X_n\) is simply connected for every \(n\ge3\).

**4. Exactly one new two-sphere per column.** For every column \(j\), the boundary of \(\Delta(C_j)\) is already in \(X_n\): its three edges are contained in the three thickening simplices with row pairs \(\{0,1\},\{0,2\},\{1,2\}\). None of the two-simplices \(\Delta(C_j)\) itself belongs to \(X_n\), and the triangles have pairwise disjoint vertex sets. Therefore \(\operatorname{GP}(R_n)\) is obtained from \(X_n\) by attaching **exactly \(n\) two-cells** along maps \(S^1\to X_n\), one per column. All those maps are nullhomotopic, because \(X_n\) is simply connected. Replacing each attaching map by a nullhomotopic map in the homotopy pushout gives
\[
 \operatorname{GP}(R_n)\simeq X_n\vee\bigvee^nS^2
 \simeq\bigvee^{2^n}S^{n-1}\vee\bigvee^nS^2.
\]
Since these null attachments also leave the integral homology of \(X_n\) primitively embedded as a direct summand, the inclusion of \(A_n\) has the claimed homology splitting. The argument applies uniformly at \(n=3\), where the two types of sphere both have dimension two. This proves every assertion.

## Verification

The independent standard-library Python program `verify.py` reconstructs the face complex in two ways: from the displayed join/thickening/triangle decomposition and by directly evaluating graph shortest-path geodesic triples on every vertex subset. For each \(3\le n\le6\), it checks equality of the complete face sets, computes all reduced mod-two homology groups from explicit simplicial boundary matrices, and tests the claim that pairwise thickening-simplex intersections lie in \(A_n\). The exact output is in `expected.txt`; run `python verify.py` from the directory holding both files. The checks use \(103,356,1269,4678\) total faces, including the empty face, for respective column counts \(3,4,5,6\). These computations corroborate but do not replace the all-parameter integral proof above.

## Relationship to prior work

A recent complete polynomial enumeration of general-position sets in rectangular rook graphs, *General-position polynomials of rectangular rook graphs via bipartite star forests*, supplies the exact geodesic-to-star-forest correspondence and a generating function for face numbers. That combinatorial characterization is taken as prior work here. Its stated results do not classify the homotopy type of the star-forest complex, identify a simply connected core, or establish the new two-cell null attachments. Another published analysis, *Complete general-position enumerators and gapped maximal spectra of rook graphs*, determines maximality and extremal sizes but not homotopy. Cody and Detore (2026) place geodesic-avoidance sets within a general \((k,d)\)-framework; Rather (2026) studies counting polynomials on other graph families. Earlier work of Klavžar and collaborators studies the general-position number in Cartesian products. None of these inspected statements gives an all-\(n\) homotopy classification of \(\operatorname{GP}(K_3\square K_n)\). The new content is the homotopy-pushout decomposition with explicit contractible attachments and nullhomotopic column boundaries, not the previously known face enumeration or extremal number.

## Limitations

Only three-row rook graphs with \(n\ge3\) are classified. No result is claimed for arbitrary row counts or for the two-column boundary case, where the core is not simply connected and the null-attachment step does not apply. The homotopy equivalence is nonequivariant; no action of the full rook-graph automorphism group is classified. Computations cover finite instances only, while the proof covers all stated parameters. The literature comparison was broad but cannot exclude a differently named or unindexed equivalent result; independent mathematical validation has not been performed.

## References

1. B. Cody and R. Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351, first public 2026-01-07, https://arxiv.org/abs/2601.04351 .
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930, first public 2026-03-06, https://arxiv.org/abs/2603.06930 .
3. S. Klavžar, B. Patkós, G. Rus and I. G. Yero, *On General Position Sets in Cartesian Products*, Results in Mathematics 76 (2021), https://doi.org/10.1007/s00025-021-01438-x .
4. *General-position polynomials of rectangular rook graphs via bipartite star forests*, public full text and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-general-position-polynomials-of-rectangular-rook-graphs-via-bipa--fc2af413d7b2 .
5. *Complete general-position enumerators and gapped maximal spectra of rook graphs*, public full text and proof, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-general-position-enumerators-and-gapped-maximal-spectra--809e96679882 .
6. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), https://doi.org/10.1007/s00025-024-02133-3 .
