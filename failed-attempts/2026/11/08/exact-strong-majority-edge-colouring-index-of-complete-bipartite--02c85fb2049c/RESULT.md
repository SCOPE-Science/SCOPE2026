# Exact strong-majority edge-colouring index of complete bipartite graphs

## Finding

For a finite simple graph, an edge-colouring is *strong-majority* if, for each edge and each colour, that colour appears on at most half the other edges sharing an endpoint with the edge. Write \(\operatorname{Maj}'(G)\) for the least number of named colours required (unused colours do not count).

**Theorem.** For every pair of integers \(2\le m\le n\),
\[
\operatorname{Maj}'(K_{m,n})=
\begin{cases}
2,&m=2\text{ and }n\equiv0\pmod 2,\\
4,&(m,n)\in\{(3,4),(4,5)\},\\
3,&\text{otherwise}.
\end{cases}
\]
The vertices and edges are labelled. There are exactly \(\binom{n}{n/2}\) named two-colour optimal edge assignments when \(m=2<n\) is even, and exactly four on \(K_{2,2}\). Every optimum in the first case colours both edges incident with each vertex of the larger part identically, with half these vertices assigned each colour. On \(K_{2,2}\), stripes may follow either bipartition.

## Assumptions and scope

All graphs are simple complete bipartite graphs with both shore sizes at least two. A colour class need not be a matching. When an edge \(e=uv\) is incident with vertices of degrees \(m\) and \(n\), its edge-neighbourhood contains \(m+n-2\) edges. For a colour \(c\) write \(r_i(c)\) for the number of edges of that colour in row \(i\), and \(s_j(c)\) for the number in column \(j\). If edge \((i,j)\) has colour \(c_0\), the number of adjacent edges of colour \(c\) equals
\[
r_i(c)+s_j(c)-2\mathbf1_{c=c_0}.
\]
Thus the condition is the integral inequality \(r_i(c)+s_j(c)-2\mathbf1_{c=c_0}\le\lfloor(m+n-2)/2\rfloor\) for every row, column and colour.

## Proof

**One and two colours.** One colour cannot work since each edge has at least two adjacent edges. For two colours, the neighbour counts of the two colours must each equal exactly \(h=(m+n-2)/2\); in particular \(m+n\) is even. Encode the first colour by \(x_{ij}\in\{0,1\}\), and let \(r_i=\sum_jx_{ij}\), \(s_j=\sum_ix_{ij}\). Equality of the adjacent first-colour count gives \(r_i+s_j-2x_{ij}=h\). Consequently all \(2\)-by-\(2\) additive minors vanish:
\[
x_{ij}+x_{k\ell}=x_{i\ell}+x_{kj}.
\]
For binary matrices, this forces either all rows to be identical (hence every column is monochromatic) or every row to be monochromatic. Indeed, the difference between any two rows is constant across all columns. If it is nonzero, those two rows are respectively all ones and all zeroes, and comparison with either forces every other row to be constant. If all row differences vanish, the rows are identical.

Suppose every row is monochromatic, and exactly \(s\) of the \(m\) rows have the first colour. For first-colour edges the neighbour count of that colour is \(n+s-2\); for other-colour edges it is \(s\). Both must equal \(h\), so \(n=2\) and \(s=m/2\). The column-monochromatic case is symmetric and requires \(m=2\), with exactly \(n/2\) first-colour columns. These constructions meet both-colour constraints, giving the stated classification and binomial counts; when both shores have size two the two stripe directions are disjoint and contribute two choices each.

**Three colours in the generic regime.** For \(m,n\ge3\), colour the edge at row \(i\), column \(j\) by \(i+j\pmod3\), with indices starting at zero. Every colour occurs at most \(\lceil n/3\rceil\) times in a row and \(\lceil m/3\rceil\) times in a column, so at most their sum can occur adjacent to an edge. The sufficient inequality is
\[
\lceil m/3\rceil+\lceil n/3\rceil\le\lfloor(m+n-2)/2\rfloor.
\]
It always holds when \(m+n\ge17\), since its left side is at most \((m+n+4)/3\) and its right side is at least \((m+n-3)/2\). Exact inspection of all integer pairs \(3\le m\le n\), \(m+n\le16\), leaves precisely the four exceptions \((3,4),(4,4),(4,5),(4,7)\). For the latter two non-obstructive exceptions, explicit valid three-colour matrices, with digits \(0,1,2\) read as colours, are

```text
(4,4): 0202 / 1021 / 0101 / 2211
(4,7): 0010212 / 1202011 / 0020121 / 2121200
```

When \(m=2\), three colours suffice for each odd \(n=2k+1\ge3\): colour both edges of \(k\) columns with colour zero, both edges of another \(k\) columns with colour one, and both edges of the remaining column with colour two. For any edge, the adjacent colour counts are exactly \(k,k,1\) (in some order), and the allowed maximum is \(\lfloor n/2\rfloor=k\). The even case already has a two-colouring.

**Sharp four-colour exceptions.** Two explicit valid four-colour matrices are

```text
(3,4): 0220 / 1313 / 1223
(4,5): 01202 / 32130 / 01121 / 33202
```

To exclude three colours, use a complete finite search. Each \(m\)-by-\(n\) matrix over \(\{0,1,2\}\) is equivalent under permuting its columns to one in which, whenever two adjacent columns have identical prefixes in the rows already assigned, their entries in the next row are nondecreasing. This is simply lexicographic sorting of the full column strings and loses no orbit. The standalone verifier enumerates every such canonical next-row assignment and rejects it only when an already-assigned edge already exceeds the final colour-count bound using adjacent edges in the assigned rows. Future rows can only increase these counts, so the rejection is sound. The complete enumeration returns no full assignments for either \((3,4)\) or \((4,5)\); it examines respectively \((15,270,2754)\) and \((21,954,55917,175554)\) canonical partial row assignments at successive depths. Hence both graphs need at least four colours, attained by the displayed matrices.

Together, these mutually exhaustive cases establish the theorem for every permitted \(m,n\).

## Verification

Run `python3 artifacts/verify.py` using Python 3 with no third-party dependencies. The script checks the four displayed matrices directly by edge-neighbourhood sums; independently exhausts all lexicographically column-canonical three-colourings for both exceptional graphs using monotone partial pruning; checks all finite inequalities needed in the generic proof; and directly enumerates every named two-colouring for small shore sizes against the formula. All integer operations are exact. The exhaustive search over the two fixed exceptional graphs is a complete finite proof certificate; the small-parameter colour enumeration does not establish the infinite theorem, which follows from the algebraic argument and constructions above.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak and Woźniak introduced strong-majority edge-colouring and proved general upper bounds (arXiv:2605.23828v1, §3); their treatment covers the definition, de Werra's balanced-colouring tool, and broad sufficient conditions, not this full biclique classification. Antoniuk, Prorok and Salia subsequently improved the general bound to five (arXiv:2607.00212v1); the accessible full HTML exposition treats general bounds and different four-colour obstructions. Pękała and Przybyło (arXiv:2608.04122v1, Observation 9) **already proved** that \(K_{3,4}\) cannot receive three colours, and proved the minimum-degree-five three-colour sufficiency theorem. The public September 2026 published-finding corpus biclique-threshold record separately establishes the \(K_{4,5}\) obstruction. **Both individual four-colour obstructions are known prior facts and are not claimed as original here.** The present contribution is a complete exact index formula for every pair of shore sizes, including all positive lower-degree cases, combined with the characterization and binomial count of every optimal two-colouring. The full readable August 2026 paper, including its conjectures on degree-four graphs, was inspected: it does not prove this complete biclique phase diagram. An equivalent independently recorded classification remains a historical-priority risk.

## Limitations

The result concerns complete bipartite graphs with both shore sizes at least two and the strong edge-neighbourhood definition. It is not about ordinary majority edge-colouring at vertices, proper edge-colouring, or arbitrary bipartite graphs. Only the optimal two-colour assignments are enumerated; the numbers of optimal three- and four-colour assignments are not determined. Independent scientific validation has not been performed.

## References

1. R. Kalinowski, M. Kamyczura, M. Pilśniak and M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1, first posted 2026-05-22, https://arxiv.org/abs/2605.23828.
2. S. Antoniuk, M. Prorok and N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212v1, first posted 2026-06-30, https://arxiv.org/abs/2607.00212.
3. P. Pękała and J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122v1, first posted 2026-08-04, https://arxiv.org/abs/2608.04122.
4. *Exact bipartite threshold for generalized strong-majority edge colouring*, publicly available published-finding corpus research record (2026-09-17), https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE005.
