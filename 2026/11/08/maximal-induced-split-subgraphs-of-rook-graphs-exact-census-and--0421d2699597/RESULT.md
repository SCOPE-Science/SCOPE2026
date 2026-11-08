# Maximal induced split subgraphs of rook graphs: exact census and square-root crossover

## Finding

For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\) be the rook graph on the \(m\)-by-\(n\) board: two cells are adjacent when they share a row or column. A set \(S\) is **split-admissible** when its induced graph admits a partition into a clique and an independent set. Define the inclusion-maximal split-set polynomial
\[
\mathcal M_{m,n}(z)=\sum_{S\text{ inclusion-maximal split-admissible}}z^{|S|}.
\]
Set \(F(q,k)=q!/(q-k)!\) for integers \(q\ge k\ge0\).

**Theorem.** The exact polynomial for every \(2\le m\le n\) is
\[
\mathcal M_{m,n}(z)=
\begin{cases}
4z^3,&m=n=2,\\
2mF(m,m-1)z^{2m-1},&m=n\ge3,\\
mF(n,m-1)z^{m+n-1}+nF(n-1,m)z^{2m},&n\ge m+1.
\end{cases}
\]
When \(n=m+1\), the two terms on the last line have the same exponent and their coefficients add. Every maximal set is obtained uniquely from one of the following line-and-rooks constructions, apart from the double representation when \(m=n=2\): (i) a full row and a nonattacking rook in each other row; (ii) a full column and a maximum nonattacking placement on the remaining \(m\)-by-\((n-1)\) board. For square boards of side at least three, the row and column classes have equal cardinality and equal numbers of realizations.

For \(n\ge m+2\), there are exactly two attained cardinalities, \(2m\) and \(m+n-1\); the intervening \(n-m-2\) integers are absent. Write \(d=n-m\ge2\). Choosing an inclusion-maximal split-admissible set uniformly, the probability of the larger cardinality is exactly
\[
\Pr(|S|=m+n-1)=\frac{m}{m+d(d+1)}.
\]
Consequently if \(m\to\infty\) and \(d/\sqrt m\to\lambda\ge0\) while \(d\ge2\), this probability tends to \(1/(1+\lambda^2)\). For fixed \(m\ge2\), it is \(m n^{-2}(1+O(n^{-1}))\) as \(n\to\infty\). Thus the short-cardinality class dominates at extreme aspect ratio despite the growing gap from the largest class.

## Assumptions and scope

All graphs are finite, simple and undirected. Rook-graph vertices are labeled board cells, so the polynomial counts labeled vertex subsets, not graph-isomorphism types. Inclusion-maximal means no *single vertex* can be added while preserving split-admissibility, which for a hereditary property is equivalent to inclusion-maximality among all vertex subsets. A split graph is a graph whose vertex set admits a disjoint clique/independent-set partition. Rook placements called nonattacking use distinct rows and distinct columns. Falling factorials above are always evaluated with \(q\ge k\); the first two cases handle the exceptional square parameters.

## Proof

**1. Complete lines and independent rooks.** Every clique of a rook graph containing at least two cells lies in a single row or column: two adjacent cells share one coordinate, and any cell adjacent to both has that coordinate, unless it is one of the two. The maximal cliques are therefore exactly the complete rows and complete columns. Let \(S\) be any inclusion-maximal split-admissible set, with split partition \(C\sqcup I\). If \(C\) is not yet a maximal clique of the ambient rook graph, then some \(v\notin C\) extends its clique. If \(v\notin S\), adjoining \(v\) to \(S\) with \(v\) placed in the clique contradicts maximality. Hence \(v\in I\); move \(v\) from \(I\) to \(C\). Since \(I\) is independent, after this move any possible further extension of the clique must be outside the selected set, and is impossible by maximality. This also works if the initial clique has zero or one vertex, by first extending it to an ambient maximal clique. Thus \(S=K\sqcup I'\), where \(K\) is one full row or column and \(I'\) is independent outside \(K\). If \(I'\) is not a maximal independent set in the subgraph outside \(K\), a vertex can be added to \(I'\) without spoiling the split partition, also a contradiction.

**2. Saturated placements.** On a \(p\)-by-\(q\) board, a nonattacking placement is maximal exactly when it meets every row or every column: otherwise an unused row and unused column intersect in a cell that may be added. Its size is \(\min(p,q)\). For a complete row \(K\), the remaining board has \(m-1\) rows and \(n\) columns, so \(I'\) has exactly one cell in each of its \(m-1\) rows, with columns all distinct. For a complete column \(K\), the remaining board has \(m\) rows and \(n-1\) columns. If \(n=m\), each of its \(m-1\) columns contains one selected cell in a different row. If \(n\ge m+1\), each of the \(m\) rows contains one selected cell in a different noncentral column.

**3. Sufficiency of the constructions.** A complete line plus a nonattacking placement is split-admissible, with that line as clique and those rooks as independent set. Suppose the line has at least three cells. In any split partition of an attempted one-vertex extension, at least two vertices of the complete line must lie in the clique, since the independent part can contain at most one. Every vertex outside the line is adjacent to at most one of its vertices, so the clique cannot contain any outside-line vertex. But maximality of the nonattacking placement on the remaining rectangle makes every omitted outside-line cell adjacent to some selected outside-line cell. Appending it violates independence, so no extension exists.

Only a full column of size two requires a separate argument (a full row of size two occurs only for the \(2\)-by-\(2\) square). For a \(2\)-by-\(n\) board with \(n\ge3\), such a column is accompanied by two cells in distinct other columns, one in each row. Adding a cell in the other row's selected column creates an induced \(C_4\), while adding a cell in a previously unused column creates an induced \(2K_2\) using the two cells of its row and the existing two cells in the opposite row at different columns. Neither forbidden graph is split. The \(2\)-by-\(2\) case has exactly four maximal three-cell paths, and adding the fourth cell gives an induced \(C_4\). This proves that each displayed construction is inclusion-maximal.

**4. Uniqueness and counting.** The number of complete-row constructions is \(mF(n,m-1)\), each of cardinality \(m+n-1\). The number of complete-column constructions is \(nF(m,m-1)\) of cardinality \(2m-1\) if \(n=m\), and \(nF(n-1,m)\) of cardinality \(2m\) if \(n\ge m+1\). For \(m\ge3\), a row construction cannot contain a full column because its \(m-1\ge2\) outside-row cells are in distinct columns. If \(m=2<n\), a set containing both a full row and full column has at least two outside-column cells in the full row and so cannot be of the column construction type. The only overlap occurs for \(m=n=2\), when every three-cell set is represented both ways. All representations within the same orientation are unique. Summing yields the stated three-case polynomial.

**5. Gaps and crossover.** For \(n\ge m+2\), the two cardinalities differ by \(n-m-1\), leaving \(n-m-2\) missing integers. By cancelling falling factorials, the ratio of the number of short sets to long sets is
\[
\frac{nF(n-1,m)}{mF(n,m-1)}=\frac{(n-m)(n-m+1)}m=\frac{d(d+1)}m.
\]
Normalizing yields the exact probability. The limits follow by dividing numerator and denominator by \(m\), or, for fixed \(m\), expanding \(d(d+1)=n^2+O(n)\). Every rook graph in the family is connected and vertex-transitive, so the gaps occur within that restricted graph class.

## Verification

The standalone `verify_rook_split.py` generates rook-graph adjacency independently, tests the classical forbidden induced subgraphs \(2K_2\), \(C_4\), \(C_5\), and enumerates all inclusion-maximal split vertex subsets. Fourteen board sizes, from \(2\)-by-\(2\) through \(4\)-by-\(5\) and including \(2\)-by-\(9\) and \(3\)-by-\(6\), yielded exact agreement for every coefficient. The total inspected candidate-subset count was \(1{,}763{,}152\). Run with `python3 verify_rook_split.py`; it requires only the Python standard library and ends with `VERIFY_OK instances=14 candidate_subsets=1763152 forbidden_induced_tests=2K2_C4_C5`. These finite checks do not constitute the unrestricted proof, which is the argument above.

## Relationship to prior work

Cao's 2020 paper proves polynomial-delay enumeration for maximal induced split subgraphs of arbitrary graphs, not a rook-family cardinality polynomial. Brosse and coauthors' 2020 preprint principally treats edge-subgraph split enumeration, distinguishing it from Cao's induced-vertex version. Brosse's 2023 thesis, Theorem 3.13, contains the stronger general **necessary** clique-plus-maximal-stable-set representation that supports the first reduction above; this general representation is credited. Neither inspected work supplies the rook-board completeness of the converse, the overlap exception, the falling-factorial enumerator or the exact square-root crossover. The present result is a family-specific refinement, not a new general enumeration algorithm. Rook graphs are also line graphs of complete bipartite graphs; this is merely an equivalent description.

## Limitations

Publication priority is provisional: a differently titled rook-graph or lattice-graph vertex-deletion study may exist outside the inspected literature. The general clique/stable-set theorem already explains why the counting problem is tractable; the independent contribution claimed here is the complete family-specific labeled classification and sharp asymptotic cardinality distribution. No assertion about arbitrary Cartesian products, higher-dimensional rook graphs, or independent validation is made.

## References

1. Yixin Cao, *Enumerating Maximal Induced Subgraphs*, arXiv:2004.09885 (first posted April 21, 2020), https://arxiv.org/abs/2004.09885.
2. Caroline Brosse, Aurélie Lagoutte, Vincent Limouzy, Arnaud Mary, and Lucas Pastor, *Efficient enumeration of maximal split subgraphs and induced sub-cographs and related classes*, arXiv:2007.01031 (first posted July 2, 2020), https://arxiv.org/abs/2007.01031.
3. Caroline Brosse, *Efficient enumeration algorithms for minimal graph completions and deletions*, doctoral thesis (2023), Section 3.2, Theorem 3.13, https://www-sop.inria.fr/members/Caroline.Brosse/149582_BROSSE_2023_archivage.pdf.
4. Stéphane Földes and Peter L. Hammer, *Split graphs*, Congressus Numerantium XIX (1977), 311–315.
