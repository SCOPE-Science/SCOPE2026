# The two-color gap in proper conflict-free colorings of square rook graphs

## Finding

**Theorem.** For integers \(1\le m\le n\), put \(R_{m,n}=K_m\square K_n\), the graph of cells in an \(m\)-by-\(n\) array, where cells are adjacent precisely if they have the same row or the same column. With the standard *open-neighborhood* proper conflict-free coloring convention,

\[
\chi_{\mathrm{pcf}}(R_{m,n})=\begin{cases}
1,&m=n=1,\\
n,&m<n,\\
n+2,&m=n\ge2.
\end{cases}
\]

There is a stronger structural characterization. For a proper coloring \(c\), write \(S_i\) for the set of colors used in row \(i\) and \(T_j\) for the set of colors used in column \(j\). If \(mn>1\), then \(c\) is proper conflict-free exactly when

\[
S_i\ne T_j\quad\text{for every cell }(i,j).
\]

In particular, *every* proper coloring of a nonsquare rook graph satisfies the conflict-free condition, while every square rook graph of side at least two requires exactly two more colors than its ordinary chromatic number. Equivalently, the theorem determines the proper conflict-free chromatic number of the line graph \(L(K_{m,n})\).

## Assumptions and scope

All graphs are finite and simple. A proper coloring assigns colors to every vertex and gives distinct colors to adjacent vertices. It is *proper conflict-free* when every nonisolated vertex \(v\) has a color occurring exactly once among the vertices of its open neighborhood \(N(v)\). Isolated vertices impose no condition. A palette of \(q\) colors need not use every color. The parameter \(\chi_{\mathrm{pcf}}\) is the least palette cardinality for such a coloring. The index range is exactly all positive integral \(m,n\) with \(m\le n\); exchanging the coordinates covers all rectangular dimensions. No list-coloring or nonproper conflict-free conclusion is asserted.

## Proof

**Neighborhood-signature lemma.** In any proper rook coloring, the colors of the other vertices in row \(i\) are pairwise distinct, and likewise for the other vertices in column \(j\). The center color \(c(i,j)\) occurs in neither part of the open neighborhood. For each other color \(t\), its multiplicity in \(N(i,j)\) is the sum of the indicators that \(t\) occurs in row \(i\) and in column \(j\). Hence its multiplicity is one precisely if \(t\in S_i\triangle T_j\). As \(c(i,j)\) belongs to both sets and never to the symmetric difference, a uniquely occurring neighbor color exists exactly when \(S_i\ne T_j\). This proves the structural characterization for every nonisolated cell.

**Rectangular case.** A row contains a clique of size \(n\), so at least \(n\) colors are required by any proper coloring. Suppose \(m<n\). Each \(S_i\) has size \(n\), whereas each \(T_j\) has size \(m\). The two sets are therefore unequal at every cell, regardless of palette cardinality, and the lemma shows that every proper coloring is proper conflict-free. A proper \(n\)-coloring is given by \(c(i,j)=i+j\pmod n\) with row indices \(0,\ldots,m-1\) and column indices \(0,\ldots,n-1\): each row uses each residue once, and each column uses distinct residues because \(m\le n\). Thus \(\chi_{\mathrm{pcf}}=n\).

**Square lower bound.** Fix \(n\ge2\). A row clique forces at least \(n\) colors. With a palette of exactly \(n\) colors, every row and column uses the whole palette, so the lemma rules out a proper conflict-free coloring. Now suppose the palette has \(n+1\) colors and \(c\) is proper. Each row, being a clique of order \(n\), omits exactly one palette color, as does each column. For any palette color \(t\), let \(r(t)\) count rows omitting \(t\) and let \(s(t)\) count columns omitting \(t\). Each occurrence of \(t\) occupies one row and one column; by properness, no row or column contains two occurrences of \(t\). Consequently, the number of rows containing \(t\) equals the number of columns containing it, and \(r(t)=s(t)\). Since every row omits some color, at least one \(t\) has \(r(t)>0\). For that color there exist a row \(i\) and a column \(j\) both omitting \(t\); their color sets are both the full palette minus \(t\). Hence \(S_i=T_j\), contrary to the lemma. Therefore \(\chi_{\mathrm{pcf}}(R_{n,n})\ge n+2\).

**Square construction.** Write \(q=n+2\ge4\) and use the additive cyclic group \(\mathbb Z_q\) as palette. Index the \(n\) rows by

\[
A=\mathbb Z_q\setminus\{0,1\}
\]

and the \(n\) columns by

\[
B=\mathbb Z_q\setminus\{0,2\}.
\]

Color cell \((a,b)\in A\times B\) with \(c(a,b)=a+b\pmod q\). Each row and each column has distinct colors by cancellation, so the coloring is proper. The row palette \(a+B\) omits exactly the two colors \(a\) and \(a+2\), while the column palette \(b+A\) omits exactly \(b\) and \(b+1\). If these omitted pairs were equal, their differences would give \(2\equiv1\pmod q\) or \(2\equiv-1\pmod q\), both impossible for \(q\ge4\). Thus every row palette differs from every column palette, and the lemma proves this \((n+2)\)-coloring is proper conflict-free. The row clique and the lower-bound argument make it optimal.

**Singleton case.** The graph \(R_{1,1}\) has one isolated vertex, which receives any one color. This proves the remaining case and the theorem. \(\square\)

## Verification

The accompanying pure-Python program `verify_pcf_rook.py` has no external dependencies. Run `python3 verify_pcf_rook.py` from the directory containing the file. It directly constructs and checks proper conflict-free colorings for every \(1\le m\le n\le13\), i.e. 91 dimension pairs. Independently, for 16 small dimension/palette cases, it enumerates *all* proper color arrays on the named palette, compares the original open-neighborhood definition against the row/column palette criterion, and checks palette feasibility at the claimed lower and upper thresholds. It checks 156,563 proper arrays in total, of which 129,519 satisfy the PCF condition. All these tests passed. They illustrate and independently stress-test the definitions; the proof above, not the finite computations, establishes the infinite-domain theorem.

## Relationship to prior work

The parameter and its open-neighborhood convention are standard. The motivating 2026 paper by Pradhan and Sharma treats PCF complexity and algorithms, reporting tractable families including block, proper interval, chain, and pseudo-split graphs. The accessible abstract does not state this two-parameter rook-graph formula. The fuller 2022 study by Caro, Petruševski, and Škrekovski gives exact values for trees, cycles, hypercubes and subdivisions of complete graphs; it already includes the four-cycle value, which corresponds to the \(2\)-by-\(2\) instance here. Jiménez and collaborators prove broad quasi-line and claw-free graph bounds, including a \(\Delta+4\) upper bound for quasi-line graphs; this does not yield the exact rook formula, and does not classify optimal square constructions. The structural statement here uses the rook graph's two transverse clique systems, so it differs from complete multipartite graph formulas and from nonproper conflict-free line-graph colorings.

## Limitations

The statement concerns finite rook graphs and proper *open*-neighborhood conflict-free vertex colorings, not list coloring, edge-neighborhood conflict-free coloring, or arbitrary Cartesian products. The case \(R_{2,2}\cong C_4\) is a known special case; no novelty is claimed for that numerical value. Literature-priority conclusions remain provisional: the full text of the 2026 motivating preprint and a related 2026 proceedings article could not be fully inspected, so unrecognized prior coverage cannot be excluded. Independent mathematical assessment has not been performed.

## References

- D. Pradhan and V. Sharma, *Complexity and algorithms for proper conflict-free coloring in graphs*, arXiv:2608.10874, first posted 2026-08-11. https://arxiv.org/abs/2608.10874
- Y. Caro, M. Petruševski, and R. Škrekovski, *Remarks on proper conflict-free colorings of graphs*, arXiv:2203.01088, first posted 2022-03-02. https://arxiv.org/abs/2203.01088
- A. Jiménez et al., *Boundedness for proper conflict-free and odd colorings*, arXiv:2308.00170, first posted 2023-07-31. https://arxiv.org/abs/2308.00170
- I. Fabrici et al., *Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods*, arXiv:2202.02570, first posted 2022-02-05. https://arxiv.org/abs/2202.02570
- V. Sharma et al., *Improved Bounds on Proper Conflict-Free Coloring of Graphs*, IWOCA 2026 proceedings, DOI:10.1007/978-3-032-27732-9_35 (abstract and bibliographic metadata consulted).
