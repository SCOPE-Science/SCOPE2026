# General-position enumerators and re-entrant unimodality in \(K_m\times K_n\)

## Finding
For integers \(m,n\ge3\), let \(G_{m,n}=K_m\times K_n\) be the **direct (categorical) product**, not the Cartesian product. Write \(\Psi_{m,n}(z)=\sum_{S\text{ in general position}}z^{|S|}\), and let \(\mathcal M_{m,n}(z)\) count inclusion-maximal general-position vertex sets by cardinality. Then
\[
\boxed{\begin{aligned}
\Psi_{m,n}(z)={}&m(1+z)^n+n(1+z)^m-(m+n-1)-mnz\\
&+\sum_{k=2}^{\min\{m,n\}}\binom mk\binom nk k!z^k
+\binom m2\binom n2(4z^3+z^4),\\
\mathcal M_{m,n}(z)={}&mz^n+nz^m
+\frac{\max\{m,n\}!}{(\max\{m,n\}-\min\{m,n\})!}z^{\min\{m,n\}}
+\binom m2\binom n2z^4.
\end{aligned}}
\]
Every inclusion-maximal general-position set is precisely a full row, a full column, a maximum-cardinality partial permutation, or the four corners of a two-by-two subrectangle. In particular the maximal cardinality spectrum is exactly \(\{4,m,n\}\), so the general-position simplicial complex is pure exactly for \(m=n=4\). In the family \(G_{3,n}\), \(n\ge6\), there are no inclusion-maximal sets of any cardinality \(5,\ldots,n-1\), giving \(n-5\) consecutive gaps.

There is also a sharp, **re-entrant unimodality transition** for the complete general-position polynomial:
\[
\boxed{\Psi_{3,n}(z)\text{ has unimodal coefficients}
\quad\Longleftrightarrow\quad 3\le n\le10\ \text{or}\ n\ge18.}
\]
Thus the coefficient sequence is nonunimodal for *exactly* \(11\le n\le17\), and becomes unimodal again for all larger \(n\). For instance, the coefficients of \(z^3,z^4,z^5\) in \(\Psi_{3,11}\) are respectively \(2156,1155,1386\).

## Assumptions and scope
The graph has vertex set \([m]\times[n]\), with distinct vertices \((i,j)\) and \((i',j')\) adjacent exactly when \(i\ne i'\) **and** \(j\ne j'\). A set \(S\) is in general position when no three of its vertices lie on any graph geodesic. The empty set is included in \(\Psi\); maximality refers to inclusion, not merely maximum size. Binomial coefficients outside their natural range are zero. All results require \(m,n\ge3\). The separate coefficient-shape theorem fixes the first factor at three, with \(n\ge3\).

## Proof
**1. Local criterion.** The graph has diameter two: nonadjacent distinct cells share a row or column, and a common neighbor exists by choosing a different row and a different column (using \(m,n\ge3\)). Three selected vertices occur together on a shortest path exactly when they induce a path on three vertices, \(P_3\). Consequently a subset is in general position if and only if its induced subgraph is a disjoint union of cliques.

**2. Exhaustive classification.** Suppose a selected row contains at least two different cells \((i,c_1),(i,c_2)\). An off-row selected cell \((j,d)\) with \(j\ne i\) must have \(d\in\{c_1,c_2\}\), because otherwise these three cells induce \(P_3\) with \((j,d)\) in the middle. If the row contained a third selected column, no off-row selected cell would be possible: that cell would be adjacent to two other selected row cells. Hence any set extending outside this row uses exactly those two columns. At most one selected cell can occur in each column outside the first row: two such cells together with the *opposite* first-row corner induce \(P_3\). If there are off-row cells in both columns, they must belong to the same second row; otherwise one off-row cell, the other, and an appropriate first-row corner induce \(P_3\). Thus the set is confined to a two-by-two rectangle and contains three or four of its corners. Interchanging rows and columns covers the symmetric case.

If no selected row and no selected column contain two cells, the set is a partial permutation (cells in pairwise distinct rows and columns). The remaining sets lie in a single row or column. Conversely, every row/column subset, partial permutation, and three- or four-corner rectangle induces a disjoint union of cliques, so all are in general position. For cardinality at least two, these classes are disjoint, except that a row or column subset must be counted using its own orientation; the empty set and singletons need the usual overlap correction.

**3. All-set enumeration.** Row-contained and column-contained sets contribute \(m(1+z)^n+n(1+z)^m\). The empty set is overcounted \(m+n-1\) times and each singleton once, giving the corrections \(-(m+n-1)-mnz\). A partial permutation on \(k\ge2\) cells has \(\binom mk\binom nk k!\) choices. Each choice of two rows and two columns yields four distinct three-corner sets and one four-corner set. Adding these contributions gives the first boxed identity.

**4. Inclusion-maximal sets.** A proper row/column subset extends within that row/column, while a full row or column cannot extend: any cell outside is adjacent to at least two nonadjacent cells inside (there are at least three selected cells). A partial permutation of size less than \(\min\{m,n\}\) extends using an unused row and column. A partial permutation of size \(\min\{m,n\}\ge3\) is maximal: any added cell shares a row or column with an existing cell; among at least three matching cells one can find another cell adjacent to both of these nonadjacent cells, producing \(P_3\). Any three-corner rectangle extends by its missing corner. A full four-corner rectangle is maximal, since every outside cell is adjacent to two nonadjacent corners. These and only these are maximal. Full rows and columns contribute \(mz^n+nz^m\); maximum partial permutations contribute the falling factorial \(\max\{m,n\}!/(\max\{m,n\}-\min\{m,n\})!\), and full rectangles contribute \(\binom m2\binom n2\). This proves the second boxed identity.

Each of the four types occurs for all \(m,n\ge3\), so the size support is \(\{m,n,\min(m,n),4\}=\{m,n,4\}\). It has one element exactly when \(m=n=4\). For \(m=3\), \(n\ge6\), the support is \(\{3,4,n\}\), giving precisely \(n-5\) missing intermediate sizes. In particular \(\mathcal M_{4,4}(z)=68z^4\).

**5. Sharp unimodality window.** Write \(\Psi_{3,n}(z)=\sum_{k\ge0}a_kz^k\). The first coefficients and the tail are
\[
\begin{gathered}
a_0=1,\quad a_1=3n,\quad a_2=\binom{3n}{2},\\
a_3=9\binom n3+12\binom n2+n,\quad
a_4=3\binom n4+3\binom n2,\quad
a_k=3\binom nk\ \ (k\ge5).
\end{gathered}
\]
For every \(n\ge3\), \(a_0<a_1<a_2<a_3\); the last inequality follows from \(a_3-a_2=\tfrac n2(3n^2-6n-1)>0\). The critical differences are
\[
\begin{aligned}
a_3-a_4&=\frac n8\bigl(-n^3+18n^2-11n+2\bigr),\\
a_4-a_5&=3\binom n2\left(1-\frac{(n-9)(n-2)(n-3)}{60}\right).
\end{aligned}
\]
The first difference is positive for \(3\le n\le17\) and negative for \(n\ge18\): write its cubic factor as \(n^2(18-n)-11n+2\), which is positive on \(3\le n\le10\) using \(18-n\ge8\), positive on \(11\le n\le17\) using \(18-n\ge1\), and negative on \(n\ge18\). The second difference is positive for \(3\le n\le10\) and negative for \(n\ge11\), since the integer product \((n-9)(n-2)(n-3)\) crosses 60 strictly between 10 and 11 and then increases.

For \(n\le10\), coefficients increase to \(a_3\), then decrease through \(a_4,a_5\); the remaining binomial tail \(3\binom nk\) is nonincreasing for \(k\ge5\). For \(11\le n\le17\) the strict valley \(a_3>a_4<a_5\) forbids unimodality. For \(n\ge18\) they increase through \(a_5\), after which the binomial coefficients form a unimodal tail. These three cases exhaust all \(n\ge3\), proving the third boxed statement.

## Verification
A standalone standard-library Python program, `verify.py`, builds graph adjacency directly and enumerates every subset for factor orders \((3,3),(3,4),(3,5),(4,4),(4,5)\): **1,151,488 subsets**. It checks the induced-\(P_3\) condition and all one-vertex extensions, then compares both complete counting polynomials to the formulas, without relying on the structural case classification for its acceptance decisions. Exact arithmetic additionally checks 276 parameter profiles with \(3\le m\le n\le25\) for the predicted maximal-size spectrum and checks the three-by-\(n\) unimodality criterion for \(3\le n\le300\). See `verification_output.txt` for the reproducible stdout. None of the finite checks substitutes for the preceding all-parameter proof.

## Relationship to prior work
Di Stefano, Klavžar, Krishnakumar, Tuite and Yero [1, Theorem 5.4] prove the **known scalar** identity \(\operatorname{gp}^{-}(K_m\times K_n)=\min\{m,n,4\}\), and exhibit maximum cliques, full layers, and four-corner rectangles. The scalar identity and these examples are not claimed as new. The contribution here is the *exhaustive all-set and all-maximal-set enumeration*, together with the proved re-entrant unimodality window, pure-complex classification, and explicit unbounded facet-size gaps; none of these statements follows numerically from the scalar minimum alone. Iršič, Klavžar, Rus and Tuite [2] introduce and study general-position polynomials, including product-related questions and unimodality, but their treated product is the Cartesian product, not the present direct product. The general structural characterization of general-position sets by Anand and collaborators [3] provides background, not these two-parameter coefficients.

## Limitations
Only direct products of **two** complete graphs with both orders at least three are covered; the two-vertex-factor and higher-factor cases are not settled by these formulas. The computational tests are finite. The first-public dates and source comparison have been checked against the cited accessible records, but unindexed equivalent enumerations under cluster-subgraph terminology may exist. Independent scientific audit and comprehensive bibliographic priority verification have not been performed.

## References
[1] G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965, first posted 2023-06-16, Theorem 5.4. https://arxiv.org/abs/2306.09965 ; accessible full text: https://ar5iv.labs.arxiv.org/html/2306.09965

[2] V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, Results in Mathematics (2024), doi:10.1007/s00025-024-02133-3. https://link.springer.com/article/10.1007/s00025-024-02133-3

[3] B. S. Anand, U. S. V. Chandran, M. Changat, S. Klavžar and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460 (2018). https://arxiv.org/abs/1812.08460
