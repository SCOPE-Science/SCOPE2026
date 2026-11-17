# Spanning-forest actuation and square resonance for rook-graph Laplacians

## Finding
Let \(m,n\ge2\) be integers and \(R_{m,n}=K_m\square K_n\) the unweighted rook graph on the \(m n\) cells \((i,j)\), with the ordinary combinatorial Laplacian \(L\). For any actuator set \(S\) of cells, consider \(\dot z=-Lz+B_Su\), where the columns of \(B_S\) are the distinct coordinate vectors of the cells in \(S\). Interpret every cell \((i,j)\) as the edge between row vertex \(r_i\) and column vertex \(c_j\) of the complete bipartite graph \(K_{m,n}\). Let \(T\) consist of the edges for cells *outside* \(S\), and let \(H_S\) be the spanning bipartite graph whose edges correspond to cells *inside* \(S\), retaining all isolated row and column vertices.

The system is controllable precisely as follows:

- If \(m\ne n\), then \(T\) is a forest.
- If \(m=n\), then \(T\) is a forest **and** the vectors \((r_C,c_C)\in\mathbb R^2\), one for each connected component \(C\) of \(H_S\), are linearly independent, where \(r_C\) and \(c_C\) count its row and column vertices. Equivalently, \(H_S\) is connected, or it has exactly two components and one component has unequal row and column counts.

The minimum number of coordinate actuators and the number of labeled minimum-size actuator sets are
\[
\begin{array}{c|c|c}
\text{board}&\text{minimum size}&\text{number of minimum sets}\\\hline
m\ne n&(m-1)(n-1)&m^{n-1}n^{m-1}\\
m=n\ge3&(n-1)^2&n^{2n-2}-n^2((n-1)^2+1)\\
m=n=2&2&4.
\end{array}
\]
The same characterization and counts hold for coordinate-state observability.

## Assumptions and scope
All graphs are finite, simple, unweighted and undirected. Coordinates are independently actuated: one distinct input channel is assigned to each selected cell. The graph Laplacian is fixed, with no tunable edge weights, and the system is considered over \(\mathbb R\). The count treats all \(m n\) cells as labeled; it is not a count modulo automorphisms. A forest includes isolated vertices. The special \(2\times2\) square is excluded from the generic square counting formula.

## Proof
**1. Eigenspaces.** Write \(\mathbf1_m\) and \(\mathbf1_n\) for the all-ones vectors. Since \(L(K_d)=dI-J_d\), the Kronecker sum \(L(R_{m,n})\) has eigenspaces
\[
E_0=\langle\mathbf1_m\otimes\mathbf1_n\rangle,\quad
E_m=\mathbf1_m^\perp\otimes\langle\mathbf1_n\rangle,\quad
E_n=\langle\mathbf1_m\rangle\otimes\mathbf1_n^\perp,\quad
E_{m+n}=\mathbf1_m^\perp\otimes\mathbf1_n^\perp.
\]
They have dimensions \(1,m-1,n-1,(m-1)(n-1)\), respectively. When \(m=n\), the two middle spaces merge into one eigenspace of dimension \(2(n-1)\); otherwise all four eigenvalues are distinct. By the symmetric-matrix Popov–Belevitch–Hautus test, controllability is equivalent to injectivity of coordinate restriction to \(S\) on each *distinct-eigenvalue* eigenspace. The constant space is always observed by any nonempty \(S\).

**2. The top eigenspace is a bipartite cycle space.** Identify a vector in \(E_{m+n}\) with an \(m\)-by-\(n\) array whose row sums and column sums vanish. Such a nonzero array can be supported entirely on \(T\) if and only if the bipartite graph \(T\) has a cycle. One direction assigns alternating \(+1,-1\) entries along an even cycle. Conversely, in a forest any leaf equation forces its unique incident coefficient to vanish; stripping leaves proves that every coefficient is zero. Hence the top-space PBH condition is *exactly* that \(T\) be a forest.

**3. The middle eigenspaces.** For \(m\ne n\), an element of \(E_m\) is an array constant along each row, with its row constants summing to zero. If a nonzero such array vanished on \(S\), two rows would be wholly contained in \(T\); for \(n\ge2\), their incident edges contain a four-cycle, contradicting that \(T\) is a forest. The same argument for two columns handles \(E_n\). Thus the forest criterion is sufficient and necessary when \(m\ne n\).

For \(m=n\), the merged eigenspace consists of arrays \(X_{ij}=u_i+v_j\), with \(\sum_i u_i=\sum_j v_j=0\). The equations \(X_{ij}=0\) on every selected cell say that, on each connected component \(C\) of \(H_S\), the row potentials equal some number \(t_C\) and the column potentials equal \(-t_C\). This also applies to isolated row or column vertices. The two zero-sum constraints become
\[
\sum_C r_Ct_C=0,\qquad\sum_C c_Ct_C=0.
\]
Only the zero solution exists exactly when the vectors \((r_C,c_C)\) are linearly independent. There can be no more than two components in that event. With a single component the condition is automatic; with two components it is equivalent to \(r_C\ne c_C\) in either component, since the total numbers of rows and columns are both \(n\). This proves the all-set criterion.

**4. Minimum size and rectangular count.** The top eigenspace forces \(|S|\ge(m-1)(n-1)\). At equality, \(T\) has \(m+n-1\) edges on \(m+n\) vertices, so its being a forest is equivalent to being a spanning tree. For unequal sides this is the entire test, and the matrix-tree formula gives exactly \(m^{n-1}n^{m-1}\) spanning trees of \(K_{m,n}\). When \(m=n\ge3\), the same lower bound dominates the merged middle-space dimension \(2(n-1)\). It is attained, for example, by taking \(T\) to consist of all edges incident to one row vertex and, for every other row, just the edge to its correspondingly indexed column: the complementary selected-edge graph then has one isolated row and a connected remaining component with unbalanced row/column counts.

**5. Exact square correction.** Let \(n\ge3\) and \(T\) be any spanning tree of \(K_{n,n}\). Its selected complement \(H_S\) has \((n-1)^2\) edges. For any component of \(H_S\) with \(r\) rows and \(c\) columns, all \(n(r+c)-2rc\) edges crossing its vertex cut must lie in the tree \(T\). Choosing a component with at most \(n\) vertices, this cut-size condition shows that a disconnected \(H_S\) can only isolate a row vertex, isolate a column vertex, or isolate one selected row–column edge. Indeed, for \(n\ge4\) and \(3\le r+c\le n\), the lower bound \(n(r+c)-(r+c)^2/2>2n-1\) exceeds the number of tree edges; for \(n=3\), the only remaining \((r,c)=(1,2),(2,1)\) splits force a four-cycle into \(T\).

If one row is isolated, \(T\) contains its entire star. Since \(T\) is a tree, every other row attaches by exactly one edge. The rest of \(H_S\) is connected unless another column is also isolated. A lone isolated row (or column) gives two *unbalanced* components and is controllable. If both a row and a column are isolated, \(T\) is the double-star with these centers, and \(H_S\) has three components: there are exactly \(n^2\) such forbidden trees.

If \(H_S\) instead has an isolated two-vertex selected component \(\{r_i,c_j\}\), \(T\) contains all \(2n-2\) edges from \(r_i\) to the other columns and from the other rows to \(c_j\). The single additional tree edge must join some other row to some other column. There are \((n-1)^2\) choices for each \((i,j)\), so \(n^2(n-1)^2\) forbidden trees. The two components of \(H_S\) are balanced, of sizes \((1,1)\) and \((n-1,n-1)\), hence they fail the middle-space condition. These two forbidden families are disjoint and exhaust all failures. Subtracting their sizes from the \(n^{2n-2}\) spanning trees of \(K_{n,n}\) gives the stated square count.

For \(n=2\), the top eigenspace alone requires one actuator but the merged middle eigenspace has dimension two, so at least two are needed. Precisely the four choices comprising a full row or a full column are controllable. This proves the final exceptional case and completes the theorem.

## Verification
The accompanying `verify_rook.py` independently builds the eigenspace restrictions and computes exact ranks over the prime field with \(1{,}000{,}003\) elements. All tested restriction matrices have at most nine columns and entries in \(\{-1,0,1\}\); Hadamard's bound makes every relevant nonzero integer minor smaller than this prime, so modular and rational ranks agree. The program exhaustively checks *all* actuator subsets on boards \(2\times2\), \(2\times3\), \(2\times4\), \(3\times3\), \(3\times4\), and every possible minimum-size subset on \(4\times4\). It verifies both the all-set combinatorial test and the minimum-size counts, including the \(4\times4\) count \(3936\). Run with `python3 verify_rook.py` from the extracted files. The finite checks are independent corroboration; the all-size assertion follows from the preceding proof, not exhaustive computation.

## Relationship to prior work
Notarstefano and Parlangeli study Laplacian coordinate controllability for Cartesian products of **paths**; their spectral/PBH framework is relevant, but path grids do not have the complete-graph-factor eigenspaces or the square resonance treated here. Olshevsky develops general minimal-coordinate controllability and complexity theory, but does not give this rook-graph classification. Brunetti, Andjelic and Stanic analyze controllability of graph products for a *single binary input vector*, a different model from independent inputs at selected cells; their openly listed preprint was not retrievable, so only its full repository abstract was inspected. Burgarth and collaborators prove that zero forcing is a sufficient, not necessary, criterion for linear controllability; no zero-forcing enumeration yields these if-and-only-if conditions. Other exact line-graph results for multipartite bases having at least three parts and exact subdivision results have different state graphs and different collision constraints: neither implies the square correction or the all-set component-rank test here.

## Limitations
The result concerns independent coordinate inputs under a fixed unweighted Laplacian; it does not classify single shared-input actuation, arbitrary weighted edges, other graph products, or cost-optimal selection with heterogeneous placement prices. Literature coverage cannot rule out all unpublished or unindexed priority claims. Independent external mathematical review has not been performed.

## References
1. D. Burgarth, D. D'Alessandro, L. Hogben, S. Severini, M. Young, *Zero forcing, linear and quantum controllability for systems evolving on networks*, arXiv:1111.1475 (initial public version November 7, 2011), https://arxiv.org/abs/1111.1475.
2. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129 (initial public version March 1, 2012), https://arxiv.org/abs/1203.0129.
3. A. Olshevsky, *Minimal Controllability Problems*, arXiv:1304.3071 (initial public version April 10, 2013), https://arxiv.org/abs/1304.3071.
4. G. Kirchhoff, *Über die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Ströme geführt wird*, Annalen der Physik und Chemie 72 (1847), 497–508 (matrix-tree theorem; historical origin, not an asserted first-public date for the focal research sources).

5. M. Brunetti, M. Anđelić and Z. Stanić, *Laplacian Controllability for Graphs Obtained by Some Standard Products*, Graphs and Combinatorics 36 (2020), 1593–1602, https://doi.org/10.1007/s00373-020-02212-6. (Single binary input vector, distinct control model; the openly listed manuscript link returned HTTP 403.)
