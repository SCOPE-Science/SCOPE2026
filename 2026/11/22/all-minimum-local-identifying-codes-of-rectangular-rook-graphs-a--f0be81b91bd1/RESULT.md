# All minimum local identifying codes of rectangular rook graphs and their ordinary-identification transition

## Finding

For integers \(3\le s\le l\), let \(R_{s,l}=K_s\square K_l\), with cells \((i,j)\) for rows \(i\in[s]\) and columns \(j\in[l]\). A *local identifying code* is a vertex subset whose closed-neighborhood traces are nonempty at every vertex and pairwise distinct for every adjacent pair of vertices. Its minimum cardinality is
\[
\gamma_{\mathrm{LID}}(R_{s,l})=2l-s.
\]
Every minimum code consists of \(s\) singleton columns occupied in distinct rows (exactly one in each row), plus exactly two selected cells in each of the \(l-s\) remaining columns. Conversely, every such selection is a minimum local identifying code. The exact number of labeled minimum codes is
\[
A_{s,l}=\frac{l!}{(l-s)!}\binom{s}{2}^{l-s}.
\]
Write \(q=l-s\) and
\[
T(a,q)=\sum_{j=0}^a(-1)^j\binom aj\binom{a-j}{2}^{q},
\]
using the combinatorial convention \(0^0=1\). Exactly
\[
B_{s,l}=\frac{l!}{(l-s)!}\bigl(T(s,q)+sT(s-1,q)\bigr)
\]
of these optimal local codes also identify *all* distinct vertices, including nonadjacent vertices. Hence \(B_{s,l}>0\) exactly when \(2q\ge s-1\), equivalently \(l\ge s+\lceil(s-1)/2\rceil\). The minima themselves, not merely their numbers, are classified.

## Assumptions and scope

Graphs are finite, simple and undirected. The vertex set is the labeled \(s\)-by-\(l\) board; different cells in a common row or column are adjacent. For each cell \(v\), let \(N[v]\) be its closed graph neighborhood and \(I_C(v)=C\cap N[v]\). Local identification requires \(I_C(v)\ne\varnothing\) for all vertices and \(I_C(u)\ne I_C(v)\) for adjacent \(u,v\). Ordinary identification requires inequality for every distinct pair. No colorings, distance-only landmarks, open-neighborhood codes or fault-tolerant variants are asserted.

## Proof

**1. Exact row/column constraints.** For fixed row \(i\), the symmetric difference of the closed neighborhoods of \((i,j)\) and \((i,k)\), where \(j\ne k\), is exactly the union of columns \(j\) and \(k\) after removing row \(i\). Thus these two adjacent vertices are separated precisely when at least one of the two columns contains a code cell outside row \(i\). For every row \(i\), therefore, **at most one column** may have all its code cells confined to row \(i\), including the possibility that the column is empty. The symmetric statement holds for columns: for every column \(j\), at most one row may have all its selected cells confined to column \(j\). These conditions are necessary and sufficient for all adjacent pairs to be separated. Domination is equivalent to never having both an entirely empty row and an entirely empty column: a cell is uncovered exactly when both its row and its column are empty.

**2. Sharp lower bound and equality structure.** Let \(z\) be the number of empty columns. The first condition gives \(z\le1\). If \(z=1\), there cannot be a column with just one selected cell, since its occupied row would have both the empty column and this singleton column as bad columns. Hence every other column contains at least two cells and
\[
|C|\ge 2(l-1)>2l-s
\]
for \(s\ge3\). If \(z=0\), let \(t\) be the number of singleton columns. The single occupied row of each singleton column is distinct from those of other singleton columns by the first condition, so \(t\le s\). All other columns have at least two selected cells, whence
\[
|C|\ge t+2(l-t)=2l-t\ge2l-s.
\]
Equality forces \(t=s\), the unique occupied cells of the singleton columns to occupy distinct rows, and all remaining columns to contain exactly two selected cells.

**3. Attainment and exact number.** Choose an injection from the \(s\) labeled rows to the \(l\) labeled columns; in the assigned column place the unique code cell in its assigned row. In every unassigned column select any two of the \(s\) rows. All columns are nonempty, so the code dominates. For every fixed row, the only column with no code cell outside that row is its assigned singleton column; a two-cell column never has this property. For every fixed column, at most one row has all its code cells within that column, because every row has a code cell in its own assigned singleton column, and at most its assigned row can have that assigned column as its unique one. The conditions in Step 1 are met. The number of injections is \(l!/(l-s)!\); each remaining column independently contributes \(\binom{s}{2}\), yielding \(A_{s,l}\).

**4. Distinguishing the nonadjacent pairs.** Denote by \(p_i\) the column assigned uniquely to row \(i\). Every trace in row \(i\) contains the selected leaf \((i,p_i)\). If two cells \((i,j)\) and \((h,k)\), with \(i\ne h\) and \(j\ne k\), have the same trace, the first leaf must belong to the other cell's closed neighborhood, forcing \(k=p_i\), and the second leaf similarly forces \(j=p_h\). Thus the only possible nonadjacent indistinguishable pair associated to \(i,h\) is \((i,p_h)\) versus \((h,p_i)\). Its two traces agree exactly when neither row \(i\) nor row \(h\) contains a selected cell in any two-cell column. Indeed, a further selected cell in either row belongs to the trace of one displayed vertex and not the other, while without further selected cells both traces consist precisely of the two leaves \((i,p_i)\), \((h,p_h)\). Consequently, a minimum local identifying code is an ordinary identifying code exactly when **at most one row is untouched by the two-cell columns**.

**5. Enumeration of globally identifying local optima.** There are \(q\) labeled two-cell columns; their selected row-pairs form a length-\(q\) sequence of two-subsets of \([s]\). By inclusion-exclusion, \(T(a,q)\) counts sequences of row-pairs from \([a]\) that collectively cover all \(a\) rows. A sequence leaving at most one row untouched either covers all \(s\) rows (\(T(s,q)\) choices), or leaves exactly one of the \(s\) rows untouched (\(sT(s-1,q)\) choices). Multiply by the independent injection count to obtain \(B_{s,l}\). Covering at least \(s-1\) rows with \(q\) pairs is possible exactly when \(2q\ge s-1\), as claimed. This also proves all boundary cases, including \(q=0\).

## Verification

The accompanying `local_ident_direct.cpp` enumerates all selected-cell masks for boards \((s,l)=(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)\), evaluating every closed-neighborhood trace and adjacent pair directly. Independently, `local_ident_occupancy.py` enumerates the same boards through the row/column constraints of Step 1. All cardinality minima and counts of minimizing codes agree, as recorded in `CHECKS.txt`.

The third independent check, `optimal_codes_direct.cpp`, generates each predicted minimum template once and tests every vertex's trace, every adjacent pair, and every pair of vertices for the seven boards up to \((5,7)\). It confirms both \(A_{s,l}\) and \(B_{s,l}\). These checks are finite confirmation, not a substitute for the preceding unrestricted proof.

## Relationship to prior work

Herva, Laihonen and Lehtilä introduce local identifying codes and derive bounds for binary hypercubes and infinite planar grids. Their object is the same local closed-neighborhood condition, but the specific all-size classification of minimum codes in a rectangular Cartesian product of complete graphs is not given there. Work on rook-graph identifying and locating-dominating codes studies globally separating, or non-codeword-separating, neighborhood requirements. The previously known necessary same-shore incidence expansion condition (Goddard–Wash, Lemma 2.3(A)) is an ingredient also underlying the present adjacent-pair argument and is **not** claimed new. The ordinary-code theorem provides the scalar bound \(\gamma_{\mathrm{ID}}(R_{s,l})=\max\{2l-s,l+\lfloor s/2\rfloor\}\), but does not give the present exact **local** minimizer family or the number of local optima that are also global codes. The distinction matters: \(R_{4,4}\) has 24 local optima of size four, none of which is a global identifying code, while global identification needs more selected vertices.

## Limitations

The theorem assumes at least three rows and no fewer columns than rows. It does not classify locally locating-dominating codes or codes in higher-dimensional Hamming graphs. The ordinary-identification threshold is consistent with known scalar bounds for ordinary identifying codes; **the novelty claimed here is the entire local minimum family and the exact global-identification subcount**, not any previously established scalar ordinary-identification theorem. Historical literature and database searches cannot certify uniqueness or priority, and no independent mathematical audit has been performed.

## References

- P. Herva, T. Laihonen and T. Lehtilä, *Optimal local identifying and local locating-dominating codes*, arXiv:2302.13351 (first public preprint 26 February 2023), https://arxiv.org/abs/2302.13351 .
- V. Junnila, T. Laihonen and T. Lehtilä, *On regular and new types of codes for location-domination*, Discrete Applied Mathematics **247** (2018), 225–241, https://doi.org/10.1016/j.dam.2018.03.050 .
- W. Goddard and K. Wash, *ID codes in Cartesian products of cliques*, J. Combin. Math. Combin. Comput. **85** (2013), 97–106, https://combinatorialpress.com/jcmcc-articles/volume-085/id-codes-in-cartesian-products-of-cliques/ .
