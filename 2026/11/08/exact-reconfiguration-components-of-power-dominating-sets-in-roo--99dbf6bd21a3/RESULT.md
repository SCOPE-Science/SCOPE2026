# Exact reconfiguration components of power-dominating sets in rook graphs

## Finding
For integers \(2\le m\le n\), consider the rook graph \(R_{m,n}=K_m\square K_n\). Write \(\mathcal T_{m,n}(k)\) for the token-addition/removal (TAR) reconfiguration graph whose vertices are all power-dominating sets of size at most the nonnegative integer \(k\), with edges joining sets differing by one vertex. Its number of connected components is \(c_{m,n}(k)\); the empty reconfiguration graph has zero components.

For \(m<n\), let
\[
B_{m,n}=n\sum_{r=1}^{m-2}\binom mr\,r!\,\left\{\begin{matrix}n-1\\r\end{matrix}\right\},
\]
where the braces are Stirling numbers of the second kind and an empty sum is zero. Then **every** nonnegative budget satisfies
\[
\boxed{c_{m,n}(k)=\begin{cases}
0,&k<m-1,\\
m n^{m-1},&k=m-1,\\
1,&m\le k\le n-2,\\
1+B_{m,n},&k=n-1,\\
1,&k\ge n.
\end{cases}}
\]
Ranges that are empty contribute no cases. In particular, when \(m=2\) the exceptional term \(B_{2,n}\) is zero.

For square rook graphs \(m=n=t\ge2\),
\[
\boxed{c_{t,t}(k)=\begin{cases}
0,&k<t-1,\\
2t^t-t^2(t-1)!,&k=t-1,\\
1,&k\ge t.
\end{cases}}
\]

Consequently, for every \(3\le m\) and \(n\ge m+2\), the bounded TAR graph is connected at every budget \(m\le k\le n-2\), becomes disconnected at budget \(n-1\), and is connected at every budget \(k\ge n\). The difference between its first connected budget and its permanently connected threshold is \(n-m\), which is unbounded.

## Assumptions and scope
The rook graph has cells \((i,j)\) for \(i\in[m]\), \(j\in[n]\), and two distinct cells are adjacent precisely when they share a row or column. A vertex set \(S\) is *power dominating* when observing its closed neighborhood and then iteratively allowing any observed vertex with exactly one unobserved neighbor to observe that neighbor eventually observes the whole graph. The usual parallel or sequential interpretation of the forcing rule gives the same closure.

Let \(r(S)\) and \(d(S)\) denote the numbers of occupied rows and columns, respectively. The primary combinatorial characterization proved here is
\[
\boxed{S\text{ is power dominating}\quad\Longleftrightarrow\quad r(S)\ge m-1\text{ or }d(S)\ge n-1.}
\]
This characterization and the displayed component formulas apply without restrictions on which rows or columns contain multiple selected cells. The empty selection is not power dominating.

## Proof
**1. Exact observation criterion.** Let \(U\) and \(V\) be the unoccupied rows and columns of a selected set \(S\). Immediately after the initial closed-neighborhood step, the unobserved cells are *exactly* the rectangle \(U\times V\): any cell in an occupied row or column is observed, and a cell in neither is not in the closed neighborhood of any selected cell.

If both \(|U|\ge2\) and \(|V|\ge2\), a currently observed cell outside this rectangle is adjacent either to zero unobserved cells or to at least \(|U|\) cells (if in an unoccupied column) or to at least \(|V|\) cells (if in an unoccupied row). No observation-forcing move is possible, so \(S\) fails to power dominate.

If \(|U|=0\) or \(|V|=0\), every cell is already observed. If \(|U|=1\) with \(|V|>0\), at least one row \(i\notin U\) is occupied because \(m\ge2\). For each \(j\in V\), the observed cell \((i,j)\) has precisely one unobserved neighbor, at the unique cell in \(U\times\{j\}\), and forces it. The case \(|V|=1\) is symmetric. This proves the characterization in both directions.

**2. Inclusion-minimal power-dominating sets.** By step 1, every power-dominating set contains a subset with precisely one chosen cell in each of \(m-1\) distinct rows (a *row basis*) or precisely one cell in each of \(n-1\) distinct columns (a *column basis*). These are power dominating and no selected cell can be deleted without losing their stated row/column coverage, unless the other coverage condition is already satisfied.

For \(m<n\), any row basis has size \(m-1<n-1\), hence cannot already cover \(n-1\) columns and is inclusion-minimal. There are \(m n^{m-1}\) such sets. A column basis is inclusion-minimal exactly when it occupies at most \(m-2\) rows: if it occupies \(m-1\) or more rows, it contains a row basis, while if it occupies at most \(m-2\) rows, deleting any selected cell leaves fewer than \(n-1\) occupied columns and still fewer than \(m-1\) occupied rows. For exactly \(r\) occupied rows, choose those rows, omit one column, and use a surjection from the \(n-1\) chosen columns to the \(r\) chosen rows. The number is \(n\binom mr r!\left\{\begin{smallmatrix}n-1\\r\end{smallmatrix}\right\}\). Summing \(1\le r\le m-2\) gives \(B_{m,n}\).

When \(m=n=t\), all row bases and all column bases are inclusion-minimal, as deleting any of their \(t-1\) cells leaves both fewer than \(t-1\) rows and columns covered. There are \(t\,t^{t-1}=t^t\) row bases and as many column bases. Their intersection consists of partial permutation matrices occupying exactly \(t-1\) rows and \(t-1\) columns, counted by \(t^2(t-1)!\). Inclusion-minimal sets in the square case therefore number \(2t^t-t^2(t-1)!\), all of size \(t-1\).

**3. Connectivity of the row-good subgraph.** Call a set *row-good* if it occupies at least \(m-1\) rows. Repeatedly delete redundant cells while retaining at least \(m-1\) occupied rows. This reaches a row basis through valid TAR steps, with no size increase. For two row bases at budget at least \(m\), each cell can change its column by adding a cell in the same occupied row and then removing the old cell; row coverage is preserved and the intermediate size is \(m\). To change which row is omitted, add a cell in the omitted row and then delete the cell in any row designated to become omitted. This again uses only \(m\) cells and maintains \(m-1\) occupied rows throughout. Thus all row-good vertices belong to one connected component for \(k\ge m\). For \(k=m-1\), row bases are isolated, since deleting one cell destroys power domination and additions exceed the budget.

**4. Emergence and eventual merger of column-good components when \(m<n\).** When \(k\le n-2\), every power-dominating set must be row-good: a column-good set needs at least \(n-1\) cells. Thus the preceding analysis gives \(m n^{m-1}\) isolated components at \(k=m-1\), then precisely one component throughout \(m\le k\le n-2\).

At budget \(k=n-1\), every column-good set outside the row-good component has exactly \(n-1\) chosen cells, one in each of \(n-1\) occupied columns, and at most \(m-2\) occupied rows. Such a set is inclusion-minimal and hence isolated at its exact budget: deletion is invalid and addition violates the budget. There are exactly \(B_{m,n}\) of them, giving \(1+B_{m,n}\) components. The same conclusion holds when the row-good part first becomes connected at budget \(n-1=m\); the two contributions are still disjoint.

At budget \(n\), all column-good sets join one component by the symmetric reasoning of step 3, using one spare cell above the column-basis size \(n-1\). Since \(n-1\ge m-1\), a column basis can be chosen to occupy at least \(m-1\) different rows, so this component intersects the row-good component. Therefore every power-dominating set is connected to every other for \(k\ge n\).

**5. Square boards.** At budget \(k=t-1\), only the row bases and column bases are present, and all are isolated. Step 2 counts them as \(2t^t-t^2(t-1)!\). At budget \(t\), step 3 and its transposed version show that row-good and column-good sets each induce connected subgraphs; these intersect on any partial permutation matrix of size \(t-1\). The entire graph is therefore connected. For \(k<t-1\), no power-dominating set exists. All component formulas now follow.

**6. Nonmonotone regime.** For \(3\le m\) and \(n\ge m+2\), the two regimes in step 4 have at least one connected budget, and \(B_{m,n}>0\) because the \(r=1\) summand equals \(nm\). Hence there is genuine disconnection at \(n-1\), and step 4 gives permanent connectedness starting at \(n\). This establishes the final assertion.

## Verification
An independent-from-formula exhaustive checker is supplied as `verify_rook.py`. For each of eight boards \((m,n)\in\{(2,2),(2,3),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4)\}\), it enumerates every nonempty cell subset, runs the observation and propagation process on the directly constructed rook graph, checks the row/column characterization for every subset, and computes the connected components of every bounded TAR graph from the minimum possible budget through budget \(n\). All tested counts agree with the formulas.

For instance, for \((m,n)=(3,5)\) the component profile at successive budgets \(2,3,4,5\) is \((75,1,16,1)\); for \((3,6)\), budgets \(2,3,4,5,6\) give \((108,1,1,19,1)\). This is finite corroboration rather than the unrestricted proof, which is steps 1–6.

## Relationship to prior work
Soh and Koh (2014) determined the power-domination number of Cartesian products of complete graphs, including the scalar optimum \(m-1\) when \(m\le n\). The present result does **not** claim that optimum as new. Bjorkman and collaborators (2022) developed token-addition/removal reconfiguration of power dominating sets, including general threshold bounds. Curtis, Flagg, and Hogben (2024) developed general TAR reconfiguration methods for vertex-set parameters. These give the motivation and general setting, but the inspected statements do not themselves determine this two-parameter rook-graph component profile, its Stirling-number jump, or the reentrant range. Published searches may miss equivalent results in unindexed literature.

## Limitations
Novelty is assessed against identified accessible sources, not certified as globally unique; a currently unindexed equivalent theorem could exist. The finite computation covers the listed boards only, whereas the mathematical classification and connectivity proof cover all integers \(2\le m\le n\) and \(k\ge0\). No independent mathematical audit is claimed.

## References
- F. Soh and K. M. Koh, "A note on Power Domination Problem in Diameter Two Graphs," *AKCE International Journal of Graphs and Combinatorics* 11 (2014), 51–55. DOI: 10.1080/09728600.2014.12088762.
- L. Bjorkman and coauthors, "Power domination reconfiguration," arXiv:2201.01798, first posted 2022-01-05, https://arxiv.org/abs/2201.01798.
- B. Curtis, M. Flagg, and L. Hogben, "TAR reconfiguration for vertex set parameters," arXiv:2406.05509, first posted 2024-06-08, https://arxiv.org/abs/2406.05509.
