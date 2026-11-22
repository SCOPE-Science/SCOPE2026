# Sharp open-adjacency type growth in unit interval graphs

## Finding
Let \(\mathcal U\) be the class of finite simple unit interval graphs, equivalently proper interval graphs. For an \(m\)-element named parameter set \(A\subseteq V(G)\), put
\[
\tau^{\mathrm{op}}(G,A)=\bigl|\{N_G(v)\cap A:v\in V(G)\}\bigr|,\quad
\tau^{\mathrm{cl}}(G,A)=\bigl|\{N_G[v]\cap A:v\in V(G)\}\bigr|.
\]
The exact classwide maxima, with finite nonempty host graphs, are
\[
\max_{G\in\mathcal U,\,|A|=m}\tau^{\mathrm{op}}(G,A)
=\begin{cases}1&m=0,\\\min\{2^m,3m\}&m\ge1,\end{cases}
\quad
\max_{G\in\mathcal U,\,|A|=m}\tau^{\mathrm{cl}}(G,A)
=\begin{cases}1&m=0,\\2m&m\ge1.\end{cases}
\]
Thus the quantifier-free one-variable **open-adjacency** types over \(m\) parameters have sharp eventual growth \(3m\), as opposed to \(2m\) for closed adjacency. Their VC dimensions are respectively \(3\) and \(2\), while both VC densities are \(1\). For each \(m\ge4\), a finite unit interval graph on exactly \(3m\) vertices realizes \(3m\) pairwise different open-adjacency traces, and no smaller host can do so.

## Assumptions and scope
Graphs are finite, nonempty, simple, undirected and may be disconnected. A unit interval representation assigns a closed interval of length one to each vertex; two distinct vertices are adjacent exactly when their intervals intersect. Equal intervals are allowed as distinct vertices. The marked vertices themselves belong to the host graph, and open neighborhoods exclude the center vertex even if it is marked. We maximize over all finite hosts and all parameter subsets of the stated cardinality. The logical reading counts only the atomic formulas \(E(x,a_i)\) (or \(x=a_i\lor E(x,a_i)\) for closed adjacency), not equality formulas themselves. The result concerns only adjacency at radius one, not graph-distance balls at larger radii, higher-order formulas, or labelled graph census.

## Proof
Represent every vertex by \([x_v,x_v+1]\). Two different vertices are adjacent if and only if \(|x_u-x_v|\le1\). Let the \(m\) marked coordinates, with multiplicities if necessary, be \(a_0\le\dots\le a_{m-1}\). For a real coordinate \(x\), define its *full intersection pattern*
\[
C(x)=\{i:|x-a_i|\le1\}.
\]
As \(x\) moves monotonically along the real line, each marked coordinate enters \(C(x)\) at \(a_i-1\) and leaves after \(a_i+1\). There are at most \(2m\) boundary events. Before the first and after the last, the pattern is empty. To handle coincident events and *closed* endpoints rigorously, refine each sweep location into two phases: first perform all interval entries at that coordinate, and only then perform all exits. The actual closed-window pattern at that coordinate is the intermediate state after all entries and before all exits. Every pattern obtained anywhere on the line therefore appears in a walk of exactly \(2m\) single-index changes, beginning and ending with the empty pattern. A walk with \(2m+1\) positions whose first and last states agree visits at most \(2m\) distinct states. This also handles repeated marked coordinates. Thus the closed-neighborhood traces number at most \(2m\).

For an unmarked vertex at coordinate \(x\), its open trace equals \(C(x)\), with indices understood as named marked vertices. For the marked vertex \(a_i\), its open trace equals \(C(a_i)\setminus\{i\}\). Consequently the open traces consist of at most \(2m\) full patterns plus at most \(m\) exceptional self-deleted patterns, so there are at most \(3m\) of them. The trivial Boolean bound \(2^m\) also applies. When \(m=0\), every trace is empty.

All bounds are attained with one construction. For every integer \(m\ge1\), put the marked unit intervals at coordinates
\[
a_i=\frac{3i}{4},\qquad 0\le i<m.
\]
There are exactly \(2m\) distinct boundary coordinates \(a_i-1\) and \(a_i+1\): their coincidence would require a nonzero integer multiple of \(3/4\) to equal \(2\), which is impossible. Sweeping a coordinate from left to right gives \(2m+1\) successive open cells. Because consecutive marked coordinates differ by \(3/4<2\), the marked radius-one coordinate windows overlap, so none of the bounded sweep cells gives the empty pattern. The empty pattern occurs in both unbounded tails, and every nonempty full pattern occurs in exactly one intermediate cell, because the left/right index bounds of the consecutive block never move backwards. Thus there are exactly \(2m\) full patterns. Choose one unmarked interval coordinate in each bounded cell and one in the left tail, ensuring distinct vertices even if a coordinate equals some marked coordinate. These \(2m\) vertices realize every full pattern, while the \(m\) marked vertices are included separately.

At each marked coordinate \(a_i\), exactly its immediate marked predecessor and successor (when present) are adjacent, since \(3/4<1<3/2\). For \(m\ge2\), the marked vertices form an induced path: the two endpoint vertices have open traces \(\{1\}\) and \(\{m-2\}\) in zero-based marked indices, and an internal vertex has open trace \(\{i-1,i+1\}\). For \(m\ge4\), these \(m\) traces are pairwise different. The internal two-point sets are not consecutive-index intervals, so they are not full patterns. The two endpoint singleton sets select an *internal* marked index; such singleton sets cannot be full patterns, since any coordinate within unit distance of an internal \(a_j\) is within unit distance of at least one of \(a_{j-1}\) and \(a_{j+1}\). Hence all \(m\) self-deleted patterns are new, proving exactly \(3m\) open traces for \(m\ge4\).

For \(m=3\), the two endpoint self-deleted patterns agree, while the internal self-deleted pattern is distinct from both and from every full pattern. This supplies exactly \(2m+2=8\) open traces. For \(m=2\), the full patterns already realize all \(4\) subsets. For \(m=1\), they realize both subsets. The closed traces attain \(2m\) at every positive \(m\). In the case \(m\ge4\), the construction uses exactly \(3m\) vertices and gives a distinct open trace at each; since each vertex generates only one trace, fewer vertices cannot suffice.

Finally, every subset of three marked vertices occurs as an open trace for \(m=3\), whereas \(\tau^{\mathrm{op}}\le12<16\) for \(m=4\); hence the open VC dimension is exactly three. The closed system shatters two points, but \(\tau^{\mathrm{cl}}\le6<8\) at \(m=3\), yielding closed VC dimension two. Both displayed sharp functions grow linearly, and hence both VC densities equal one. \(\square\)

## Verification
The standalone `verify.py` constructs the explicit marked-coordinate progression with exact rational geometry and checks all \(m=0,\dots,40\), including the exact counts of open and closed traces and the \(3m\)-vertex minimum witnesses for \(m\ge4\). Independently, it builds adjacency matrices for every nondecreasing tuple of up to seven centers on the nine-point quarter-unit grid, checking every marked subset against both claimed upper bounds (1,066,494 pairs of graphs and marked sets). Run `python3 verify.py` with a standard Python 3 interpreter. These finite checks corroborate, but do not replace, the all-parameter sweep proof.

## Relationship to prior work
Dreier, Mählmann, McCarty, Pilipczuk and Toruńczyk (2026) prove almost-linear neighborhood complexity for monadically dependent graph classes, without an exact constant for proper/unit interval graphs. Beaudou, Bok, Foucaud, Quiroz and Raymond (first public 2025) discuss profile bounds for interval graphs and known \(O(dk)\) metric-dimension-type bounds for unit interval graphs, not this sharp radius-one *open* trace function. Rutter, Strash, Stumpf and Vollmer (2025) recall the proper-interval/unit-interval graph equivalence. In particular, a general interval-graph radius-profile bound does not imply the sharp constant for open one-point adjacency types of the proper subclass. The closed-pattern estimate is an elementary consequence of the standard consecutive-neighborhood representation; the nontrivial comparison here is the simultaneous sharpness of the larger open system and the exact VC-dimension shift.

## Limitations
This is an exact one-variable radius-one profile statement, not a result for arbitrary first-order formulas or for non-unit intervals. The proof does not classify all extremal representations. Searches and full-text comparisons establish no absolute historical-priority guarantee, and independent mathematical or historical validation has not been performed. Potential earlier formulations in locating/identifying-code literature may involve comparable trace systems; those have different domination/nonemptiness conditions and should be checked independently before claims of priority.

## References
1. J. Dreier, N. Mählmann, R. McCarty, M. Pilipczuk, S. Toruńczyk, *Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes* (first public 2026-07-12), arXiv:2607.10941, https://arxiv.org/abs/2607.10941.
2. L. Beaudou, J. Bok, F. Foucaud, D. A. Quiroz, J.-F. Raymond, *Profile and neighbourhood complexity of graphs excluding a minor and tree-structured graphs* (first public 2025-01-15), arXiv:2501.08895, https://arxiv.org/html/2501.08895v3.
3. I. Rutter, D. Strash, P. Stumpf, M. Vollmer, *Simultaneous Representation of Proper and Unit Interval Graphs*, Algorithmica 87 (2025), https://doi.org/10.1007/s00453-025-01296-x.
