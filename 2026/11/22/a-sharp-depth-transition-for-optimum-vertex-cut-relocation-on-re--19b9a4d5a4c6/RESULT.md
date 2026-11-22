# A sharp depth transition for optimum vertex-cut relocation on rectangular grids

## Finding

For every rectangular grid \(P_n\square P_w\) with \(n\ge3\) columns and \(w\ge4\) rows, fix the terminals at \(s=(0,r)\) and \(t=(n-1,r)\), where \(1\le r\le w-2\). The minimum size of an \(s\)-\(t\) vertex separator is three. Its complete configuration family and both optimum-preserving reconfiguration graphs are as follows.

| Position of terminals | Length | Minimum cuts | Token-slide graph | Token-jump graph |
|---|---|---:|---|---|
| Next to an outer row: \(r=1\) or \(r=w-2\) | \(n=3\) | 6 | \(2P_3\) | \(K_3\square K_2\) |
| Next to an outer row | \(n\ge4\) | 6 | \(2P_3\) | \(2K_3\) |
| Two or more rows from both outer rows: \(2\le r\le w-3\) | \(n=3\) | 4 | \(4K_1\) | \(C_4\) |
| Two or more rows from both outer rows | \(n\ge4\) | 2 | \(2K_1\) | \(2K_1\) |

The interior-depth case exists only when \(w\ge5\). In particular, **all** optimal three-vertex cuts are frozen under adjacent slides as soon as neither terminal lies next to an outer row. At length three, unrestricted jumps can still connect the four deep-terminal cuts; at greater lengths even jumps are frozen. This is a sharp phase boundary for the mobility of minimum-capacity network cutsets.

## Assumptions and scope

The graph \(P_n\square P_w\) has vertices \((x,y)\) with \(0\le x\le n-1\), \(0\le y\le w-1\); two vertices are adjacent precisely when their Manhattan distance is one. A separator \(S\) excludes \(s,t\) and disconnects them in the induced graph after deleting \(S\). A minimum separator has the smallest possible cardinality. A *token jump* replaces one selected vertex by any different unselected vertex while maintaining minimum separator status; a *token slide* additionally requires the old and new selected vertices to be adjacent in the grid. Reconfiguration graphs have one vertex per minimum separator and one undirected edge per legal single-token replacement. The symbol \(P_3\) is a three-vertex path, \(K_j\) is a complete graph, and \(C_4\) is a four-cycle; juxtaposition with a numerical coefficient denotes disjoint copies.

All minimum separators have the unique coordinate representation

\[
S(a,b,c)=\{(a,r-1),(b,r),(c,r+1)\}.
\]

The exact necessary and sufficient constraints are

\[
1\le b\le n-2,\quad 0\le a,c\le n-1,\quad |a-b|\le1,\quad |c-b|\le1,
\]

\[
r\ge2\ \Longrightarrow\ a\in\{0,n-1\},\qquad r\le w-3\ \Longrightarrow\ c\in\{0,n-1\}.
\]

## Proof

**1. Minimum size and three fixed rails.** The neighborhoods of either terminal consist of three vertices, providing an \(s\)-\(t\) separator of size three. Conversely, there are three internally vertex-disjoint \(s\)-\(t\) paths: the straight middle-row path; the path that goes up to row \(r-1\), traverses that row, and comes back down at the last column; and its reflected path through row \(r+1\). Therefore every separator has at least three vertices. Moreover, each minimum separator must intersect these three disjoint paths exactly once. The chosen vertices have distinct fixed rows \(r-1,r,r+1\); the middle-row one cannot be a terminal, giving \(1\le b\le n-2\).

**2. Adjacent-rail inequalities are necessary.** Suppose \(a\le b-2\). Follow the middle row from \(s\) until column \(a+1\), switch upward to row \(r-1\), and follow that row to \(t\). This avoids both selected rail vertices; it also avoids the lower rail. If \(a\ge b+2\), start along row \(r-1\) until column \(b+1\), switch down to the middle row, and continue to \(t\). These are \(s\)-\(t\) paths avoiding all three selected vertices, which is impossible. Thus \(|a-b|\le1\); by reflection the same argument gives \(|c-b|\le1\).

**3. Extra-row endpoint constraints are necessary.** If \(r\ge2\) and \(a\notin\{0,n-1\}\), follow the path from \(s\) up through \((0,r-1)\) to \((0,r-2)\), traverse row \(r-2\), descend via \((n-1,r-1)\) to \(t\). This avoids every selected vertex. Hence \(a\) must be a column endpoint. Reflecting vertically gives the analogous restriction on \(c\) if \(r\le w-3\).

**4. The constraints are sufficient.** Remove the three selected vertices. In each of rows \(r-1,r,r+1\), color positions strictly to the left of that row's selected column \(L\), and positions to the right \(R\). No surviving horizontal edge joins \(L\) to \(R\). The adjacent-column inequalities ensure that no surviving vertical edge between two of these three rows joins an \(L\)-vertex to an \(R\)-vertex. If any rows exist above row \(r-1\), color all of them \(R\) when \(a=0\), or \(L\) when \(a=n-1\); this is consistent with their surviving neighbors in row \(r-1\). Color all rows below \(r+1\) analogously using \(c\). No surviving edge joins the two classes, but the terminal \(s\) is in \(L\) and \(t\) is in \(R\). The set is therefore a separator, completing the exact classification.

**5. Enumeration and move graphs.** The selected tokens lie on three different fixed rows. Any legal one-vertex replacement can only modify one of \(a,b,c\); under sliding, the modified coordinate changes by exactly one. When \(r=1\) (the case \(r=w-2\) is its reflection), the outer coordinate \(c\) is in \(\{0,n-1\}\). If \(c=0\), necessarily \(b=1\), and the free coordinate \(a\) runs over \(0,1,2\); if \(c=n-1\), necessarily \(b=n-2\), and \(a\) runs over \(n-3,n-2,n-1\). The slide graph is consequently two three-vertex paths. Jumping completes each path to \(K_3\). For \(n\ge4\), the two branches differ in at least two selected coordinates and have no cross-branch jump. For \(n=3\), \(b=1\) in both branches and changing only \(c\) links matched positions, yielding the triangular prism \(K_3\square K_2\).

When \(2\le r\le w-3\), both outer coordinates are endpoints. For \(n=3\), the middle coordinate is \(b=1\), giving four independently chosen endpoint pairs. Each coordinate endpoint change skips one intervening column, so no token slides occur. Token jumps flip one of the two outer coordinates, giving \(C_4\). For \(n\ge4\), \(a=c=0\) forces \(b=1\), while \(a=c=n-1\) forces \(b=n-2\); mixed endpoint choices are impossible. The two remaining configurations differ in all three coordinates and therefore admit neither slide nor jump. This proves every table entry for all integers in the stated ranges.

## Verification

The accompanying independent Python standard-library programs run as `python3 verify_grid_bruteforce.py` and `python3 verify_grid_states.py`. The first directly enumerates all subsets of up to three nonteminal vertices on the corresponding finite rectangular graphs, checks disconnection by breadth-first search, and independently constructs both reconfiguration graphs. It checks 56 instances with column counts 3–6, widths 4–7, and all interior terminal rows. The second separately enumerates coordinate triples and checks complete component-size and degree distributions for 1,232 instances with column counts 3–30 and widths 4–11. Both tests passed. The infinite-parameter conclusions rest on the preceding proof, not on this finite census.

## Relationship to prior work

Gomes, Legrand-Duchesne, Mahmoud, Mouawad, Okamoto, dos Santos and van der Zanden (first public 2023) developed general polynomial-time token-slide algorithms for minimum-separator reconfiguration, proved confinement to canonical disjoint paths, and studied the contrasting complexity of shortest token-jump sequences. Our argument specializes the canonical-path insight but determines the exact cut coordinates and both entire reconfiguration graphs for the stated multi-parameter grid family; their general algorithm does not itself state this phase portrait. Gomes, Nogueira and dos Santos (2020) studied vertex-separator reconfiguration without restricting to minimum-cardinality separators. This result does not claim the already-studied width-three strip or any general complexity or algorithmic results from those works.

## Limitations

The classification concerns simple rectangular path grids with two opposite-boundary terminals in the **same interior row** and **strictly minimum** vertex cuts of size three. It says nothing about other terminal placements, nonminimum separator budgets, arbitrary graphs, or simultaneous multi-token changes. The 2020 related source was checked through its accessible abstract rather than a full-text analysis; an unindexed or inaccessible equivalent may remain. Scientific originality requires independent literature assessment; independent mathematical validation has not been performed.

## References

1. G. C. M. Gomes, C. Legrand-Duchesne, R. Mahmoud, A. E. Mouawad, Y. Okamoto, V. F. dos Santos, and T. C. van der Zanden, *Minimum Separator Reconfiguration*, arXiv:2307.07782, first posted 2023-07-15, https://arxiv.org/abs/2307.07782.
2. G. C. M. Gomes, S. H. Nogueira, and V. F. dos Santos, *Some results on Vertex Separator Reconfiguration*, arXiv:2004.10873, first posted 2020-04-22, https://arxiv.org/abs/2004.10873.
