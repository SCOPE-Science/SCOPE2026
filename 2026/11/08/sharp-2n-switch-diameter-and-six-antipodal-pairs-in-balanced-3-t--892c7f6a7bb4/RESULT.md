# Sharp \(2n\) switch diameter and six antipodal pairs in balanced \(3\times3\) contingency fibers

## Finding
For every integer \(n\ge1\), let \(\mathcal F_n\) be the nonnegative integer \(3\times3\) matrices whose three row sums and three column sums all equal \(n\). Join two matrices if they differ by exactly one signed \(2\times2\) checkerboard switch \(\pm(E_{ik}+E_{j\ell}-E_{i\ell}-E_{jk})\), with distinct rows and columns and with all nine entries remaining nonnegative. The resulting undirected graph is connected and has exact diameter \(2n\). Moreover, there are exactly six unordered pairs at distance \(2n\), namely \(\{nP,nQ\}\) where \(P,Q\) are \(3\times3\) permutation matrices and their underlying permutations differ by a three-cycle. Every other pair of distinct matrices has distance at most \(2n-1\). This is proved for every positive integer \(n\), not inferred from finite enumeration.

The six sharp pairs are characterized without enumerating the fiber: scale any of the six pairs of disjoint permutation matrices by \(n\). For example, let
\[
P=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad
Q=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]
Then \(d(nP,nQ)=2n\). All distinct pairs not of this form are strictly closer.

## Assumptions and scope
The row and column positions are individually labelled \(0,1,2\). A state is a \(3\times3\) matrix of nonnegative **integers**, including zeros, with every row and column sum exactly \(n\), where \(n\) is any integer \(n\ge1\). A move uses two different row indices and two different column indices and adds \(+1\) at two opposite rectangle corners and \(-1\) at the other two corners, or its negative. A move must preserve nonnegativity. All distances count individual unit moves, even if larger integer changes could be made in one circuit step. Neither row or column relabellings nor scalar multiple switches are legal single moves. The graph here is the lattice-point **Markov-basis graph**, not the vertex-edge graph of the real transportation polytope.

## Proof
**Step 1 (the universal upper bound).** Regard a state \(X\) as the incidence-multiplicity matrix of an \(n\)-regular bipartite multigraph on three row vertices and three column vertices. The standard perfect-matching decomposition of a regular bipartite multigraph gives
\[
X=P_1+\cdots+P_n,\qquad Y=Q_1+\cdots+Q_n,
\]
where every summand is a permutation matrix. Any two \(3\times3\) permutation matrices differ by a permutation with at most two transpositions: the distance in the six-vertex permutation-matrix switch graph is zero, one, or two, depending on whether the relative permutation is the identity, a transposition, or a three-cycle. Apply these at most two switches to each layer \(P_t\) while all other layers remain fixed. All intermediate sums are nonnegative. Consequently \(d(X,Y)\le2n\) for every two states, and the graph is connected. No assumption of a preferred decomposition is needed.

**Step 2 (sharpness by a dual potential).** For canonical identity and three-cycle permutation matrices \(P,Q\) above, define the integer coefficient matrix
\[
W=\begin{pmatrix}1&-1&0\\0&1&-1\\-1&0&1\end{pmatrix}
\]
and \(\Phi(X)=\sum_{i,j}W_{ij}X_{ij}\). For each of the nine choices of two rows and two columns, the checkerboard coefficient \(W_{ik}+W_{j\ell}-W_{i\ell}-W_{jk}\) belongs to \(\{-3,0,3\}\). Thus one unit switch changes \(\Phi\) by at most three. But \(\Phi(nP)=3n\) and \(\Phi(nQ)=-3n\); every route between these states therefore requires at least \(6n/3=2n\) moves. All other pairs \(nP,nQ\) whose relative permutation is a three-cycle are row/column relabellings of this pair. The upper bound makes their distance exactly \(2n\).

**Step 3 (strictness whenever the tables overlap).** Suppose \(X_{ij}>0\) and \(Y_{ij}>0\) for at least one cell. A regular bipartite multigraph can be decomposed into perfect matchings so that any specified positive edge is in one summand. Choose decompositions of \(X\) and \(Y\) beginning with permutation matrices \(P_1,Q_1\) containing that common cell. Two permutations of three letters sharing one position differ by at most one transposition, so their matrices can be joined by at most one switch. Pair the remaining \(n-1\) summands arbitrarily and use at most two moves per pair. Therefore \(d(X,Y)\le1+2(n-1)=2n-1\).

**Step 4 (disjoint support).** Suppose no cell is positive in both \(X\) and \(Y\). Take any permutation-matrix layers \(P\) and \(Q\) from respective matching decompositions. Their supports are disjoint, and the three unused edges of the complete \(3\times3\) bipartite graph form the support of a third permutation matrix \(R\). Because \(X\) is zero on the support of \(Q\), and \(Y\) is zero on the support of \(P\), the supports of \(X\) and \(Y\) lie respectively inside those of \(P+R\) and \(Q+R\). Equal row and column sums on the alternating six-cycle \(P\cup R\) force \(X=aP+(n-a)R\) for an integer \(0\le a\le n\); likewise \(Y=bQ+(n-b)R\). If both \(a<n\) and \(b<n\), the two tables share all three \(R\)-cells, a contradiction. Hence at least one state is a multiple of a permutation matrix. Swap the roles if needed, and relabel so \(X=nP\), \(Y=bQ+(n-b)R\), with \(P,Q,R\) the three pairwise edge-disjoint permutation matrices.

If \(b\in\{0,n}\}\), both states are pure permutation multiples, and because their supports are disjoint their relative permutation is a three-cycle; these are precisely the sharp pairs. Otherwise \(1\le b\le n-1\), so \(n\ge2\). An explicit three-switch route converts \(2P\) into \(Q+R\) (matrices displayed below). Convert the remaining \(n-2\) layers of \(P\) into \((b-1)\) layers of \(Q\) and \((n-b-1)\) layers of \(R\) using at most two switches per layer. Hence \(d(X,Y)\le3+2(n-2)=2n-1\).

For \(P=I\), \(Q\) the cyclic shift \((1,2,0)\) and \(R\) the reverse shift \((2,0,1)\), the promised three-switch route is
\[
\begin{pmatrix}2&0&0\\0&2&0\\0&0&2\end{pmatrix}
\to\begin{pmatrix}1&1&0\\1&1&0\\0&0&2\end{pmatrix}
\to\begin{pmatrix}0&1&1\\1&1&0\\1&0&1\end{pmatrix}
\to\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}=Q+R.
\]
Direct entrywise differences show each arrow is one permissible signed rectangle switch. Independent row/column relabellings transfer the route to every ordered triple \((P,Q,R)\). This covers every possible pair \((X,Y)\), completes the extremal classification, and proves the theorem for all \(n\).

**Step 5 (counting the pairs).** There are six \(3\times3\) permutation matrices. For each one, precisely two permutations differ by a three-cycle. Therefore there are \(6\cdot2/2=6\) unordered sharp pairs and no others.

## Verification
Two self-contained Python 3 scripts, `verify_row_parameter.py` and `verify_independent.py`, independently enumerate all states for \(1\le n\le8\), construct all nine unsigned rectangle switches, and perform complete breadth-first distances (one script additionally verifies the exact set of diametral pairs). They agree with the proved diameter \(2n\), and six diameter pairs at every tested \(n\). At \(n=6\) the graph has 406 states and diameter twelve; at \(n=8\) it has 1035 states and diameter sixteen. The second script also checks all nine linear-potential rectangle coefficients and replays the displayed three-switch compression. The finite checks are supplementary to the all-\(n\) proof above and do not certify untested margins by extrapolation.

## Relationship to prior work
Diaconis and Sturmfels developed the basic integer-table Markov-basis framework and connectivity of fixed-margin contingency tables; our connectivity argument is standard and **not claimed new**. De Loera, Kim, Onn and Santos (2007) investigate edges and diameters of the associated real transportation polytopes. Such a polytope graph has **only extreme points** as vertices and its edges are not unit rectangle moves; its diameter does not imply our lattice-point move diameter. A publicly available small-margin exhaustive fiber census [3] establishes diameter twelve for the uniform three-by-three margins \((6,6,6)\) but explicitly bounds its scope to margins at most six, and does not state an all-margin formula or count the six extremal pairs. The contribution claimed here is the exact all-positive-\(n\) diameter law and complete six-pair extremal classification. Full historical priority beyond the inspected sources is not asserted.

## Limitations
Rows and columns are exactly three each, all six margins are equal to the same integer, and moves are **unit** checkerboard changes. No bound is given here for arbitrary margin vectors, rectangular tables, mixing time, or the one-skeleton diameter of the real transportation polytope. The construction is an ordinary mathematical proof and two finite checks, not an independent external certification. Unindexed earlier results using different terminology could cover the theorem.

## References
1. P. Diaconis and B. Sturmfels, *Algebraic algorithms for sampling from conditional distributions*, *Annals of Statistics* **26** (1998), 363–397, DOI 10.1214/aos/1030563990; Stanford technical report EFS NSF 430 dated June 1993 (exact original public day not established).
2. J. A. De Loera, E. D. Kim, S. Onn and F. Santos, *Graphs of transportation polytopes*, arXiv:0709.2189v1 (posted 14 September 2007), later *Journal of Combinatorial Theory, A* **116** (2009), 1306–1325.
3. *Exact Markov fiber diameters for small-margin 3x3 and 3x4 contingency tables*, publicly available 8 September 2026, https://github.com/published-finding corpus/2026/blob/main/2026/9/8/SCOPE057/RESULT.md ; its theorem and limitations concern a finite list of margin vectors only.
