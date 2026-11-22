# Proper conflict-free coloring separates the Shrikhande and rook graphs

## Finding

Let \(S\) be the Shrikhande graph on \(\mathbb Z_4^2\) with Cayley steps \((\pm1,0)\), \((0,\pm1)\), \((1,1)\), \((-1,-1)\). Let \(R=K_4\square K_4\) be the four-by-four rook graph. Both are strongly regular with parameters \((16,6,2,2)\), yet their proper open-neighborhood conflict-free chromatic numbers differ:

\[
\boxed{\chi_{\mathrm{pcf}}(S)=5,\qquad\chi_{\mathrm{pcf}}(R)=6.}
\]

The exact value for \(R\) was reported previously in a general study of square rook graphs; the independently derived new part here is the sharp five-color result for \(S\) and its comparison with the cospectral graph \(R\).

## Assumptions and scope

Graphs are finite, simple, undirected, and have no isolated vertices. A proper coloring \(f:V(G)\to[k]\) is *open-neighborhood conflict-free* if every vertex \(v\) has a color occurring **exactly once** among \(\{f(u):u\in N(v)\}\). Here \(\chi_{\mathrm{pcf}}(G)\) is the smallest permitted palette size. This is not improper conflict-free coloring and not the closed-neighborhood condition.

Use coordinates \((i,j)\) with \(i,j\in\{0,1,2,3\}\). In \(R\), distinct cells are adjacent exactly when they share a row or column. In \(S\), distinct coordinates \((i,j),(p,q)\) are adjacent exactly when \((p-i,q-j)\bmod4\) belongs to the six-element step set given above. The sixteen vertices are fixed and named by their coordinates; color names may be permuted without changing feasibility.

## Proof

**1. The common strongly regular structure and independence bound.** In \(S\), the step set \(D\) has cardinality six. Its ordered difference multiset \(D-D\) contains \((0,0)\) six times and every other element of \(\mathbb Z_4^2\) exactly twice. Thus each vertex has degree six and any two distinct vertices have exactly two common neighbors. The same parameters hold for \(R\), directly from its row/column adjacency. In particular, if \(C\) is an independent set of cardinality \(t>0\) in either graph, put \(a_x=|N(x)\cap C|\) for \(x\notin C\). Counting incident pairs and shared neighbors gives

\[
\sum_{x\notin C}a_x=6t,\qquad
\sum_{x\notin C}\binom{a_x}{2}=2\binom{t}{2},
\qquad \sum_{x\notin C}a_x^2=2t(t+2).
\]

Cauchy--Schwarz implies \(36t^2\le(16-t)2t(t+2)\), or \(t^2+4t-32\le0\), hence \(t\le4\). If \(t=4\), the twelve values \(a_x\) have sum \(24\) and squared sum \(48\); their variance is zero, so every vertex outside \(C\) has **exactly two** neighbors in \(C\).

Consequently a proper coloring using at most four colors would have exactly four independent classes, each of size four. For every vertex, each of the other three colors occurs twice in its neighborhood, while its own color occurs zero times. This violates the conflict-free condition. Thus \(\chi_{\mathrm{pcf}}(S)\ge5\) (and also \(\chi_{\mathrm{pcf}}(R)\ge5\)).

**2. A five-color witness for the Shrikhande graph.** The following array gives \(f(i,j)\), with rows indexed by \(i\) and columns by \(j\):

\[
\begin{pmatrix}
0&4&0&2\\
1&3&2&4\\
2&0&1&0\\
3&1&3&4
\end{pmatrix}.
\]

Every one of the 48 edges has endpoints of different colors, and each of the sixteen open neighborhoods contains a color occurring once. Both conditions are verified by the included independently implemented certificate checkers, which construct the graph directly from the step set and evaluate all 16 neighborhoods. Since the lower bound was proved for all colorings, \(\chi_{\mathrm{pcf}}(S)=5\).

**3. Five colors fail for the rook graph.** Suppose a proper coloring of \(R\) uses a palette of at most five colors. Each row and each column induces a \(K_4\), so all four entries in every row and column have distinct colors. With at most four colors, every row and column sees the same four-color palette, and every cell has each of the three other colors twice in its open neighborhood. Now assume a five-color palette. Let \(A_i\) be the four-color set used in row \(i\) and \(B_j\) that used in column \(j\). Because \(A_i\setminus\{f(i,j)\}\) and \(B_j\setminus\{f(i,j)\}\) each have three distinct colors, the coloring is conflict-free at cell \((i,j)\) exactly when \(A_i\ne B_j\).

For each palette color \(c\), its number of missing rows equals its number of missing columns, because its occurrences occupy distinct rows and distinct columns. Each of the four rows misses one color; choose a row missing \(c\). Some column also misses \(c\). Their palettes both equal the five-color palette minus \(\{c\}\), so the cell at their intersection fails. Hence \(\chi_{\mathrm{pcf}}(R)\ge6\).

**4. A six-color witness for the rook graph.** The array

\[
\begin{pmatrix}
0&1&2&4\\
1&4&3&2\\
2&3&0&5\\
5&0&1&3
\end{pmatrix}
\]

is proper along every row and column and has a uniquely occurring neighbor color at every cell. The included checkers verify every edge and open neighborhood, yielding \(\chi_{\mathrm{pcf}}(R)\le6\). Combining both bounds proves the finding.

## Verification

Run `python3 check_coloring.py`, and separately compile `check_independent.cpp` with `c++ -O2 -std=c++17 check_independent.cpp -o check_independent` and run `./check_independent`. Both reconstruct the two sixteen-vertex graphs from their definitions and verify degree six, the common-neighbor count two for every pair, properness and a singleton neighbor color at each vertex for the displayed certificates. The Python implementation also checks all fifteen nonzero differences in \(D-D\) and the distinct local-neighborhood component profiles (one six-cycle against two triangles). Neither finite checker is used to claim an unbounded graph-family theorem; all lower bounds here are deductive.

## Relationship to prior work

The open-neighborhood proper conflict-free invariant is defined and studied in Liu (2022) and Jiménez et al. (2023), including general structural bounds. In the 2023 paper the claw-free and quasi-line bounds do not determine either exact value; moreover, \(S\) is not claw-free, since the neighborhood of a vertex is an induced six-cycle containing an independent triple. A prior online result titled *A two-color gap for proper conflict-free coloring of square rook graphs* already reports \(\chi_{\mathrm{pcf}}(K_4\square K_4)=6\), and its complete square-rook formula is fully credited. No exact \(\chi_{\mathrm{pcf}}(S)\) result was identified in the targeted sources or searched mathematical research records. The novelty claim is restricted to the Shrikhande value and the resulting separation, not to the rook value, the general definitions, or the strongly regular parameters.

## Limitations

This is an exact comparison of two specific graphs, not a general formula for strongly regular graphs. In particular the shared parameter array \((16,6,2,2)\) does not determine this coloring invariant. A targeted literature search is not a proof of historical uniqueness; unindexed earlier work could cover the Shrikhande case. No independent mathematical audit is claimed.

## References

1. Chun-Hung Liu, *Proper conflict-free list-coloring, odd minors, subdivisions, and layered treewidth*, arXiv:2203.12248 (first public 23 March 2022), https://arxiv.org/html/2203.12248v3.
2. A. Jiménez et al., *Boundedness for proper conflict-free and odd colorings*, arXiv:2308.00170 (first public 31 July 2023), https://arxiv.org/html/2308.00170v4.
3. *A two-color gap for proper conflict-free coloring of square rook graphs*, online research record dated 18 October 2026, public record suffix `fb9f4a963e44` (relevant previously reported square-rook formula; full proof was not obtained during the comparison).
