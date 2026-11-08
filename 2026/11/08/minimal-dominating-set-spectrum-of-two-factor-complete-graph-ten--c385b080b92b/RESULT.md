# Minimal dominating-set spectrum of two-factor complete-graph tensor products

## Finding

For integers \(m,n\ge 2\), write \(G_{m,n}=K_m\times K_n\) for the categorical (tensor/direct) product, in which cells \((i,j)\) and \((k,\ell)\) are adjacent exactly when \(i\ne k\) and \(j\ne\ell\). An *inclusion-minimal dominating set* is a dominating vertex set with no smaller dominating subset. Its cardinality enumerator is

\[
\begin{aligned}
\mathcal D_{m,n}(z)={}&n z^m+m z^n
+4\mathbf 1_{\{m,n\ge3\}}\binom m2\binom n2z^3\\
&+6\binom m3\binom n3z^3
+6\left(\binom m2\binom n4+\binom n2\binom m4\right)z^4.
\end{aligned}
\]

Here \(\binom ab=0\) if \(b>a\). All inclusion-minimal dominating sets have one of the following five forms, and each form listed is inclusion-minimal within its stated range: (I) one entire row; (II) one entire column; (III) three corners of a \(2\)-by-\(2\) coordinate rectangle, only when \(m,n\ge3\); (IV) three cells in pairwise distinct rows and columns; (V) exactly four cells in two rows, two in each, with four distinct columns, or its transposed two-column form. These forms are disjoint as vertex sets.

In particular, for every \(n\ge6\), the possible cardinalities of inclusion-minimal dominating sets of \(K_3\times K_n\) are exactly \(\{3,4,n\}\). Therefore \(5,6,\ldots,n-1\) are missing: the length of the cardinality gap is \(n-5\), unbounded with \(n\).

## Assumptions and scope

Both complete factors are finite simple graphs with at least two vertices. Rows are indexed by the first factor and columns by the second. Ordinary domination is used: a vertex already selected dominates itself. This is distinct from *total* domination, which requires each vertex to have a selected adjacent vertex. All statements are for every labeled pair of factor orders \(m,n\ge2\), including the disconnected boundary \(K_2\times K_2\). No divisibility, balance, primality, or connectedness assumption is made.

For a set \(S\) of cells, form the bipartite *incidence graph* \(B(S)\) having one vertex for each row and one for each column; its edges are precisely the selected cells. A graph-theoretic matching is a family of edges with no common endpoint, and a vertex cover meets each edge.

## Proof

**Domination criterion.** For any unselected cell \((i,j)\), the selected set dominates that cell precisely when it contains some \((k,\ell)\) with \(k\ne i\) and \(\ell\ne j\). Equivalently, \(S\) fails to dominate precisely when there exists an unselected cell \((i,j)\) such that every edge of \(B(S)\) is incident to row \(i\) or column \(j\).

**Matching case.** If \(B(S)\) has three disjoint edges, their three corresponding cells already dominate: any cell shares its row with at most one and its column with at most one of the three, so at least one selected cell is adjacent unless it is already selected. If \(S\) is inclusion-minimal, it therefore consists of exactly those three disjoint edges. Conversely, any three such cells dominate; removing one leaves two distinct-row, distinct-column cells, and an unselected opposite corner of their \(2\)-by-\(2\) rectangle is not dominated. Thus exactly the sets in (IV) arise in this case.

**Small-matching case.** Suppose the matching number of \(B(S)\) is at most two. By the bipartite matching-cover theorem (Kőnig's theorem), its edges admit a vertex cover of size at most two. Analyze a fixed such cover.

If one row (or one column) covers all edges, then all selected cells lie in that row (column). The domination criterion forces every cell of this row (column) to be selected, giving (I) or (II). Such a full line is minimal: deleting one cell makes that cell itself undominated.

Suppose a row \(r\) and a column \(c\) cover all selected edges. The crossing cell \((r,c)\) must be selected; otherwise it is an undominated cell. If both the row and column contain a selected edge outside their intersection, the selected set contains a three-corner rectangle. This triple dominates by the criterion. Under inclusion-minimality there are no other selected cells. The triple is inclusion-minimal when \(m,n\ge3\): a selected two-cell subset lying in one row or one column fails to dominate a third cell of that line; a diagonal two-cell subset fails at an opposite corner. If \(m=2\), the triple contains an entire two-cell column; if \(n=2\), it contains an entire two-cell row. Both are smaller dominating sets. If one arm is empty, the cover collapses to the one-line case.

Finally suppose two distinct rows \(r,s\) cover every selected edge; the two-column case is symmetric. If only one row contains selected cells, we have (I). If one row, say \(r\), has only the selected cell \((r,c)\), then \((s,c)\) must be selected: otherwise the cell \((s,c)\) has no selected neighbor outside row \(s\) and column \(c\). If \(m=2\), these two cells make an entire column and domination-minimality excludes extras. If \(m\ge3\), domination requires a second column \(c'\ne c\) in row \(s\) (otherwise an unselected cell in a third row and column \(c\) is undominated). Together \((r,c),(s,c),(s,c')\) are the dominating three-corner rectangle; minimality excludes extras. If both rows contain at least two selected cells, the selected set dominates automatically: each row has two selected distinct columns to cover all unselected cells in the other selected row, and at least two different columns together cover cells outside those rows. Minimality forces **exactly two** selected cells in each row, since any excess can be removed while both rows retain at least two cells. Their column sets must be disjoint: a shared column produces a dominating three-corner subset when \(m\ge3\), or a complete two-cell column subset when \(m=2\). Conversely, with four distinct columns, deleting any selected cell leaves its unique same-row partner \((r,c)\) and two selected cells of the opposite row in columns distinct from \(c\); then the unselected opposite-row cell in column \(c\) has no selected neighbor. Hence the four-cell set is minimal. This is precisely (V). Transposition covers two selected columns. Exhaustiveness follows from the cover cases.

**Counting and disjointness.** Entire rows and columns contribute \(m z^n+n z^m\). There are \(4\binom m2\binom n2\) three-corner rectangles when both factor orders are at least three. Three-edge matchings contribute \(3!\binom m3\binom n3\). For two-row four-cell sets, choose the rows, four columns, and the two columns assigned to the first row, giving \(6\binom m2\binom n4\); the transposed family gives \(6\binom n2\binom m4\). The families cannot coincide: complete lines have one occupied row or column; rectangle triples have repeated row and column; matching triples repeat neither; two-row four-cell sets use four different columns, and two-column four-cell sets use four different rows. Thus the displayed polynomial follows.

For \(m=3\), \(n\ge6\), every displayed term has exponent \(3\), \(4\), or \(n\). All three coefficients are positive (the rectangle term gives \(3\); the two-row four-cell term gives \(4\); the full-row term gives \(n\)). The gap statement follows.

## Verification

The accompanying standalone Python checker independently implements adjacency and closed-neighborhood domination on each cell graph. It exhaustively enumerates all nonempty candidate subsets for eleven parameter pairs up to \((4,5)\), testing deletion of each selected vertex rather than merely comparing generated counts. It constructs the five predicted families separately and compares the **actual families**, not just total counts. An additional five larger pairs are checked by construction, cardinality coefficients, and direct maximality tests; these are not represented as exhaustive subset searches. The recorded run returned:

`VERIFY_OK exhaustive_instances=11 candidate_subsets=1419077 dominating_sets=1412493 minimal_sets=2231 generated_instances=5 families=PASS coefficients=PASS gap_spectrum=PASS`

Reproduce with `python verify_minimal_dom_tensor.py` using Python 3; no external packages are needed. Finite checks do not replace the general proof.

## Relationship to prior work

Defant and Iyer (first public preprint August 3, 2017) study domination and upper domination of direct products of complete graphs. Their Theorem 2.1 records the minimum domination numbers of two factors, while their Proposition 4.5 establishes the relevant upper-domination bound using a four-vertex reduction. Those results do not enumerate all inclusion-minimal sets or specify all intermediate achievable cardinalities. Anderson, Kuenzel and Rall (2019) characterize well-dominated direct products under stated hypotheses, including the \(K_3\times K_3\) case; this does not determine the exact polynomial at arbitrary unequal factor orders. Burcroff and O'Brien (2021) prove unimodality of the ordinary domination polynomial of direct products of complete graphs, an all-dominating-set generating function distinct from the present **minimal-set** polynomial. There is also a separate total-domination problem for the same products, with open neighborhoods rather than closed neighborhoods. The present classification is not obtained by substituting total for ordinary domination.

The well-dominated characterization, already known upper bound, and known minimum values are not claimed as discoveries. The asserted new object is the exact five-family census together with its complete minimal-set cardinality spectrum and gap statement.

## Limitations

The result is specific to exactly two complete factors, and applies to ordinary minimal domination only. It does not give a minimal-set polynomial for three or more factors or for arbitrary product graphs. Prior-publication exclusion is provisional: alternate terminology, unpublished work, and tables not indexed by the searches may contain equivalent results. The evidence establishes a proof and reproducible finite checks, not independent external mathematical validation.

## References

- Colin Defant and Sumun Iyer, *Domination and Upper Domination of Direct Product Graphs*, arXiv:1708.01305, publicly posted 2017-08-03; especially Theorem 2.1 and Proposition 4.5. https://arxiv.org/abs/1708.01305
- Sarah E. Anderson, Kirsti Kuenzel, and Douglas F. Rall, *On Well-Dominated Graphs*, arXiv:1909.09955, publicly posted 2019-09-22; especially Theorem 3. https://arxiv.org/abs/1909.09955
- Amanda Burcroff and Grace O'Brien, *Unimodality and Monotonic Portions of Certain Domination Polynomials*, arXiv:2110.00709, publicly posted 2021-10-02; especially Section 5.1. https://arxiv.org/abs/2110.00709
