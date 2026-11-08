# Minimal total domination of rook graphs: a three-regime component enumerator

## Finding
Let \(m,n\ge 2\) be integers and let \(R_{m,n}=K_m\square K_n\), the graph whose vertices are the cells of an \(m\)-by-\(n\) board, with two cells adjacent when they share a row or column. Let \(M_{m,n}(z)=\sum_D z^{|D|}\), where the sum runs over **inclusion-minimal total dominating sets** \(D\) of \(R_{m,n}\): every cell, including each selected cell, must have a distinct selected adjacent cell.

Define a formal three-variable series
\[
H(x,y,z)=x(e^{yz}-1-yz)+\frac{x^2yz^2}{2}+y(e^{xyz^2}-1-xyz^2).
\]
Then, for all \(m,n\ge2\),
\[
\boxed{M_{m,n}(z)=m!n![x^m y^n]\left((e^x-1)e^{H(x,y,z)}+(e^y-1)e^{H(y,x,z)}+\exp\!\left(\frac{z^2(xy^2+x^2y)}{2}\right)\right).}
\]
The coefficient extraction is in the ordinary formal expansion in \(x,y\); the resulting coefficients are nonnegative integers. This identity counts all labeled placements with their exact selected-cardinality, not merely optimum solutions.

There is also a complete structural classification. Identify a selected cell \((i,j)\) with the edge between row vertex \(i\) and column vertex \(j\) in \(K_{m,n}\). Every minimal total dominating set is in exactly one of three regimes:

1. **At least one empty row.** Every column is occupied. On its used rows and all columns, the selected-edge graph is a disjoint union of components of types \(A_k\), \(B\), and \(C_k\) below, where \(k\ge2\).
2. **At least one empty column.** Every row is occupied. The analogous statement holds after interchanging rows and columns.
3. **No empty row or column.** The selected-edge graph is a spanning disjoint union of two-edge stars, with each star having one row and two columns or two rows and one column.

In the first regime the permitted components are: \(A_k\), one selected row joined to \(k\) singleton columns (\(k\) edges); \(B\), two singleton rows joined to a common column (two edges); and \(C_k\), one column center joined to \(k\) rows, each of which is joined additionally to its own distinct private singleton column (\(2k\) edges). The component types are vertex-disjoint in the row-column incidence graph. The second regime uses their transposes.

The formula reveals nonconsecutive possible minimal-set sizes. For instance,
\[
M_{5,5}(z)=410z^5+5700z^6+1200z^8,
\]
so no inclusion-minimal total dominating set of this natural rook graph has seven vertices. For another example,
\[
M_{6,6}(z)=5112z^6+36720z^7+251100z^8+8640z^{10}.
\]

## Assumptions and scope
All graphs are finite, simple and undirected. Total domination uses **open neighborhoods**. Inclusion-minimal means deleting any selected cell invalidates total domination; because total domination is upward-closed, checking all single deletions is sufficient. The row-column incidence graph is bipartite, with \(m\) distinguishable row vertices and \(n\) distinguishable column vertices. An isolated row or column has degree zero in this selected-edge graph. The assertions hold without parity or aspect-ratio conditions for every pair of integers \(m,n\ge2\), including the boundary \(2\)-by-\(2\) board. Coefficient extraction is formal and does not require analytic convergence.

## Proof
**1. The total-domination criterion.** Let \(F\subseteq E(K_{m,n})\) correspond to selected cells, and let \(r_i\) and \(c_j\) be row and column degrees in \(F\). For an unselected cell \((i,j)\), the number of adjacent selected rooks equals \(r_i+c_j\). For a selected cell it equals \(r_i+c_j-2\). Consequently, \(F\) is total dominating if and only if (a) all rows or all columns are occupied, and (b) \(r_i+c_j\ge3\) on every selected edge \((i,j)\). Condition (a) follows because an empty row and an empty column would leave their intersection undominated. Condition (b) excludes an isolated selected rook.

**2. Structure when some row is empty.** In this situation every column must be occupied. Any selected edge \(e\) whose column has degree one is indispensable: deleting it empties that column, while an already-empty row remains empty. Consider now a selected edge \(e\) whose column has degree at least two. Deleting \(e\) keeps all columns covered; therefore \(e\) is indispensable only if some other selected cell \(f\) becomes isolated after the deletion. In the selected rook graph, \(f\) then has exactly one selected neighbor, namely \(e\).

If \(f\) and \(e\) lie in the same column, the column has degree exactly two and the row of \(f\) has degree one. As \(f\) must itself be indispensable while its deletion leaves that column covered, its unique neighbor \(e\) must also become isolated when \(f\) is deleted. Thus the row of \(e\) has degree one. These two edges form precisely a \(B\)-component, with no further attachments.

If \(f\) and \(e\) instead lie in the same row, that row has degree exactly two and the column of \(f\) has degree one. Hence \(e\) attaches a degree-two row to its own column center and to one private singleton column. Every edge of any column center of degree at least two, unless in a \(B\)-component, must have this form; each such center gives exactly one \(C_k\)-component, and \(k\ge2\). Finally, all selected edges in degree-one columns not belonging to the preceding components form stars centered at rows. Each such row must have degree at least two by the total-domination criterion, giving an \(A_k\)-component. No other component is possible.

Conversely, take any disjoint union of these components covering every column, together with at least one unused row. It is total dominating: its selected edges have adjacent selected edges, and every board cell is in an occupied column. It is inclusion-minimal: deleting an edge at a singleton column leaves that column uncovered, and deleting an edge at a center column isolates another selected edge in the same \(B\)-component or its associated private \(C_k\) leaf. Thus the first-regime classification is necessary and sufficient. Interchanging the two bipartition classes gives the second regime. Both regimes cannot occur simultaneously, because a missing row and a missing column violate domination.

**3. Structure when every row and column is occupied.** Let \(F\) be total dominating. No selected edge has both endpoints of selected degree one, since that edge would itself be an isolated selected rook. Accordingly, deleting any selected edge leaves at least one entire bipartition class occupied: to lose both coverage properties simultaneously, the deleted edge would have to be the unique selected edge at both endpoints.

Thus a deletion can destroy total domination only by leaving another selected rook isolated. Equivalently, each vertex of the induced selected rook graph must be essential for total domination within that selected graph. A finite graph of minimum degree at least one has this property precisely when each connected component is \(K_2\). Indeed, in any component other than \(K_2\), either the minimum degree is at least two (then deleting any vertex leaves no isolated selected vertex), or a leaf is adjacent to a vertex of degree at least two (then deleting that leaf leaves no isolated selected vertex). The deleted rook is itself still attacked by its former neighbor, and at least one entire row-column shore stays covered. Such a deletion would contradict minimality. Conversely, deleting one endpoint from a \(K_2\)-component isolates its partner, so every selected rook is indispensable.

Under the line-graph correspondence, each selected \(K_2\)-component is a pair of incident edges in \(K_{m,n}\): either one row joined to two columns or one column joined to two rows. Two distinct components have disjoint row and column vertices, otherwise the corresponding rooks would be adjacent. As every row and column is used, these two-edge stars span the row-column incidence graph. This proves the third regime and its converse.

**4. Labeled component enumeration.** Use exponential generating variables \(x\) for row labels and \(y\) for column labels, and give each selected edge weight \(z\). An \(A_k\)-component contributes \(xy^kz^k/k!\), for \(k\ge2\), summing to \(x(e^{yz}-1-yz)\). The \(B\)-component contributes \(x^2yz^2/2\). A \(C_k\)-component consists of \(k\) labeled rows and \(k+1\) labeled columns. Choosing its center column and bijecting the rows with the remaining private columns gives \((k+1)!\) structures on those labels. Its exponential generating weight is therefore \(x^ky^{k+1}z^{2k}/k!\). Summing over \(k\ge2\) gives \(y(e^{xyz^2}-1-xyz^2)\). Their sum is exactly \(H(x,y,z)\).

The labeled SET construction of pairwise vertex-disjoint permitted components contributes \(e^{H(x,y,z)}\). At least one empty row contributes \(e^x-1\), and coefficient extraction at \(x^my^n\) forces every column to be used. This is the first summand. The second summand is its transpose. For the third regime, one-row/two-column and two-row/one-column stars contribute respectively \(xy^2z^2/2\) and \(x^2yz^2/2\); their disjoint labeled SET gives \(\exp(z^2(xy^2+x^2y)/2)\). Multiplication by \(m!n!\) completes the cardinality polynomial, with no overlap between the three regimes. \(\square\)

## Verification
The companion standalone program `VERIFY.cpp` enumerates every nonempty selected-cell subset for eleven boards: \((2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5)\). It directly tests the open-neighborhood total-domination condition and every single-cell deletion. Independently, it checks each minimal set's incidence-component type, and compares the resulting cardinality counts against a separate labeled-component recurrence equivalent to the displayed coefficient extraction.

The actual run examined **51,745,605** nonempty subsets and identified **17,045** minimal total dominating sets; every tested coefficient and component type agreed. A separate recurrence check confirmed the \(6\)-by-\(6\) example. Compile and run with `c++ -O2 -std=c++17 VERIFY.cpp -o verify && ./verify`. The exhaustive test is finite and is not an unrestricted proof; the general result follows from the preceding structural argument.

## Relationship to prior work
Velammal and Arumugam (2012, Example 2.2(iv) and Remark 2.5) already establish the minimum total edge domination number of \(K_{m,n}\), equivalently the minimum total domination cardinality \(\min\{m,n\}\) for the rook graph; this minimum is **not** a novelty claim. They define the upper total edge domination number but do not give the present all-minimal-set enumerator. Mertens (2024) determines the ordinary domination polynomial of rook graphs by counting all dominating placements via row-column coverage (Theorems 1–4, Corollary 5, and numerical tables). Ordinary domination permits a chosen rook without another chosen neighbor and does not impose inclusion-minimality; its all-set polynomial does not establish the three minimal-total-domination component regimes or this enumerator. Pahlavsay, Palezzato, and Torielli (2018) determine the **minimum \(3\)-tuple total domination number** of rook graphs; requiring at least three selected neighbors and finding an extremal cardinality does not classify minimal ordinary \(1\)-tuple total dominating sets. Standard database interfaces expose finite-graph minimal-total-domination polynomials, but the consulted material did not supply an equivalent all-parameter rook-graph theorem. These are scientific comparisons, not assertions of exhaustive publication coverage.

## Limitations
The finding is restricted to Cartesian products of **two** complete graphs; it does not classify general Hamming products, arbitrary line graphs, or higher-tuple total domination. No independent mathematical audit has been performed. Publication priority is provisional: differently named results, unavailable full texts, or unindexed enumerative formulas could contain equivalent statements. The finite verification tests only the stated board sizes.

## References
1. S. Mertens, “Domination Polynomial of the Rook Graph,” arXiv:2401.00716 (first public version January 1, 2024), https://arxiv.org/html/2401.00716v2 .
2. B. Pahlavsay, E. Palezzato, M. Torielli, “3-tuple total domination number of rook’s graphs,” arXiv:1807.08104 (first public version July 21, 2018), https://arxiv.org/html/1807.08104v1 .
3. S. Velammal and S. Arumugam, “Total edge domination in graphs,” Elixir Discrete Mathematics 44 (2012), 7213–7217, https://www.elixirpublishers.com/articles/1681456907_201203027.pdf .
4. Wolfram Research, “GraphData,” documentation for minimal-total-domination enumerative graph properties, https://reference.wolfram.com/language/ref/GraphData.html .
