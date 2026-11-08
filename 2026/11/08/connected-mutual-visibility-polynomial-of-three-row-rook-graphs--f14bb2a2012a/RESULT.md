# Connected mutual-visibility polynomial of three-row rook graphs

## Finding

Let \(G_n=K_3\square K_n\) for every integer \(n\ge3\). Write \(C_n(z)\) for the sum of \(z^{|S|}\) over **nonempty** connected mutual-visibility vertex sets \(S\) in \(G_n\). Then

\[
\begin{aligned}
C_n(z)={}&3((1+z)^n-1)+3nz^2(1+2z)^{n-1}\\
&+nz^3(1+3z)^{n-1}\\
&+3n(n-1)z^4(1+3z)^{n-2}\\
&+n(n-1)(n-2)z^6(1+3z)^{n-3}.
\end{aligned}
\]

Every counted set has an explicit five-family row-column classification given below. In particular,

\[
\mu_c(K_3\square K_n)=n+3,
\qquad [z^{n+3}]C_n(z)=n(n-1)(n-2)3^{n-3}.
\]

The count distinguishes all named vertices (not just automorphism classes). For example,

\[
C_3(z)=9z+18z^2+42z^3+72z^4+81z^5+6z^6.
\]

## Assumptions and scope

Graphs are finite, simple, undirected. The graph \(G_n\) has vertices \( (i,j)\) where \(i\in\{1,2,3\}\) denotes a row and \(j\in\{1,\ldots,n\}\) denotes a column; distinct cells are adjacent precisely when they share a row or column. A set \(S\ne\varnothing\) is **connected mutual-visible** when \(G_n[S]\) is connected and for every two distinct cells \(u,v\in S\), some shortest \(u,v\)-path in \(G_n\) has all internal cells outside \(S\). The polynomial excludes the empty set. The claimed formula and maximum are for every integer \(n\ge3\), without a hidden asymptotic restriction.

## Proof

**Visibility and the incidence graph.** Any two cells in a shared row or column are adjacent and hence automatically mutually visible. Two cells in distinct rows and columns have distance exactly two and precisely two common neighbors: the opposite corners of their rectangle. They fail to be mutually visible precisely when **both** other corners are selected. Therefore mutual visibility is equivalent to forbidding any completely selected \(2\times2\) subrectangle. In particular, each unordered pair of rows occurs together in at most one column.

Construct the bipartite incidence graph \(B_S\) with three row vertices, \(n\) column vertices, and an edge \(ij\) for each selected cell \((i,j)\). The line graph of \(B_S\), restricted to its edges, is exactly \(G_n[S]\). Thus \(G_n[S]\) is connected exactly when all selected edges of \(B_S\) belong to a single edge-containing component. We now enumerate the mutually exclusive possibilities by the number of selected cells in each column.

**No multirow column.** If every occupied column contains only one cell, selections in distinct rows have no induced edges between them. Connectivity forces the selected cells to occupy one row. Choose one of three rows and a nonempty subset of the \(n\) columns: contribution \(3((1+z)^n-1)\).

**A three-row column.** If some column has all three cells selected, every row-pair is already used together, so each other column has at most one selected cell. Conversely the complete column connects all three rows, so every such singleton joins the same component. Choose the special column in \(n\) ways, and choose absence or any of three rows in each remaining column: \(nz^3(1+3z)^{n-1}\).

**No three-row column but one two-row column.** Choose the pair of rows in \(3\) ways and the column in \(n\) ways. Every other column is empty or a singleton because a second column of that pair would create a selected rectangle. Connectivity rules out singleton cells in the unused third row, and allows both used rows. This yields \(3nz^2(1+2z)^{n-1}\).

**Exactly two two-row columns.** Their unordered row pairs must be distinct to avoid a rectangle, and hence on three rows share one row and collectively span all rows. Choose the two row-pair types in \(3\) ways, then inject them into two distinct columns in \(n(n-1)\) ways. Any remaining column may be empty or contain one of the three singleton rows. The induced set is connected because the two multirow columns intersect in a row, and every extra singleton attaches to this component. The contribution is \(3n(n-1)z^4(1+3z)^{n-2}\).

**Exactly three two-row columns.** The three row pairs must occur once each: select an injection of these three named pairs into three columns, in \(n(n-1)(n-2)\) ways. The three multirow columns form a connected triangle on the row vertices. All other columns may be empty or singleton in any row, producing \(n(n-1)(n-2)z^6(1+3z)^{n-3}\).

There cannot be a fourth two-row column, because the three row-pairs are exhausted. The cases are disjoint and exhaustive and all constructions meet both conditions. Their generating functions sum to the displayed formula, completing the all-coefficients proof.

**Extremal size and multiplicity.** The maximum sizes of these five families, respectively, are \(n\), \(n+1\), \(n+2\), \(n+2\), and \(n+3\). For \(n\ge3\), only the fifth family reaches \(n+3\), and this occurs exactly when every remaining column is a singleton. Its top coefficient is \(n(n-1)(n-2)3^{n-3}\), as claimed.

## Verification

The standalone Python 3 script `verify.py` independently constructs adjacency in \(K_3\square K_n\), checks induced connectivity by graph search, and checks every required distance-two geodesic. It exhaustively enumerates all nonempty vertex subsets for \(1\le n\le5\) (including boundary controls outside the theorem), compares every polynomial coefficient with an independently implemented five-family formula, and checks the asserted top coefficient through \(n=30\). Actual replay ended in `VERIFY_OK`. These finite tests are corroboration; the preceding case analysis proves all integers \(n\ge3\).

## Relationship to prior work

The connected mutual-visibility notion is due to Tonny and Shikhi [1]. The older ordinary mutual-visibility theory for rook graphs [2] shows that its visibility condition is a rectangle prohibition, a characterization explicitly restated in [3, Lemma 4.1]. This existing lemma is acknowledged, not claimed as new. Our claimed new contribution is the additional induced-*connectivity* classification, the full connected-set cardinality polynomial, and exact multiplicities of the maximum sets. The ordinary visibility polynomial formulas for wheels, friendship graphs, shell graphs, and bow graphs in [4] concern other graph families and do not impose connectedness. Total mutual visibility [5] requires a different, stronger condition quantifying over all graph vertices, so its Cartesian-product results are not the present connected-set enumerator. A related published result for Cartesian products of two high-girth graphs does not apply when a factor is the triangle \(K_3\).

## Limitations

The proof is specialized to exactly three rows; it does not assert a comparable five-type formula for arbitrary \(K_m\square K_n\) with \(m\ge4\). It counts nonempty connected mutual-visibility sets, not ordinary, total, outer, or dual sets. The initiating 2026 manuscript's full text could not be obtained in the available research session; its public abstract was inspected. Therefore historical priority remains provisional even though the mathematical claim and its proof are self-contained. No independent mathematical audit has been performed.

## References

1. Tonny K B and Shikhi M, Connected Mutual-Visibility in Graphs, arXiv:2609.18877 (first public 2026-09-16), https://arxiv.org/abs/2609.18877.
2. S. Cicerone, G. Di Stefano and S. Klavžar, On the mutual visibility in Cartesian products and in triangle-free graphs, Applied Mathematics and Computation 438 (2023), article 127619; arXiv:2112.13024, https://arxiv.org/abs/2112.13024.
3. V. Iršič Chenoweth, S. Klavžar, G. Rus, E. Tan and J. Tian, Builder-Blocker Mutual-Visibility Game, Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 89, https://doi.org/10.1007/s40840-026-02083-9.
4. K. B. Tonny and M. Shikhi, Visibility Polynomial of Some Graph Classes, Advances and Applications in Discrete Mathematics 43(2) (2026), 213–225, https://doi.org/10.17654/0974165826015.
5. D. Kuziak and J. A. Rodríguez-Velázquez, Total Mutual-Visibility in Graphs with Emphasis on Lexicographic and Cartesian Products, Bulletin of the Malaysian Mathematical Sciences Society 46 (2023), article 197, https://doi.org/10.1007/s40840-023-01590-3.
