# Sharp checkerboard-averaging variation gain on every rectangular grid

## Finding
Let \(m,n\ge2\) be integers. Form the nearest-neighbor rectangular grid graph \(G_{m,n}\) on \(\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\), with each horizontal and vertical edge counted once. The black and white classes are \(B=\{(i,j):i+j\text{ is even}\}\) and \(W=V\setminus B\). Define the uniform two-class averaging projection \(P\): replace each black-site value with the arithmetic mean over \(B\), and each white-site value with the mean over \(W\). For real signals define the anisotropic edge total variation
\[
V_G(f)=\sum_{\{u,v\}\in E(G)}|f_u-f_v|.
\]
Then the exact, attained variation-seminorm operator norm, equivalently sharp two-input Lipschitz factor, is
\[
\boxed{\displaystyle
\sup_{V_G(f)>0}\frac{V_G(Pf)}{V_G(f)}
=\sup_{V_G(f-g)>0}\frac{V_G(Pf-Pg)}{V_G(f-g)}
=\frac{2mn-m-n}{2\lceil mn/2\rceil}.}
\]
An indicator supported at any corner of the grid attains the constant. Thus the coefficient is \(2-1/m-1/n\) when \(mn\) is even, but \((2mn-m-n)/(mn+1)\) when both side lengths are odd. The operator is nonexpansive in graph total variation only for the \(2\times2\) grid; all other rectangles amplify some input. Along rectangles with both sides diverging, the sharp gain tends to \(2\).

The odd-by-odd conclusion follows from a bounded, explicit, nonnegative edge-flux certificate obtained by combining eight Hamiltonian snake paths. It does not require a spanning cycle (which an odd-order bipartite grid cannot possess).

## Assumptions and scope
Both side lengths are at least two; the graph has free boundaries and unit edge weights. The input is an arbitrary real array, including negative values. Means are uniform **within** each checkerboard class, so the two means use different denominators when \(mn\) is odd. The projection is linear, positive, idempotent and constant preserving; no stochastic or periodic boundary assumptions are made. The numerator and denominator use the same graph-edge variation seminorm. The asserted norm is a quotient by constant signals, for which the denominator vanishes.

Write \(N=mn\), \(e=2mn-m-n\), \(b=\lceil N/2\rceil\), and \(w=\lfloor N/2\rfloor\). Set
\[
\ell(f)=\frac1b\sum_{v\in B}f_v-\frac1w\sum_{v\in W}f_v.
\]
Every edge crosses colors, so \(V_G(Pf)=e|\ell(f)|\). The main task is the sharp functional estimate \(|\ell(f)|\le V_G(f)/(2b)\).

## Proof
**1. A flow certificate and sharpness.** Orient every grid edge from its black endpoint to its white endpoint. If nonnegative edge numbers \(q_e\) have incident-edge sums \(\sum_{e\ni v}q_e=1/b\) at black vertices and \(1/w\) at white vertices, then
\[
\ell(f)=\sum_{e=(u\in B,v\in W)}q_e(f_u-f_v).
\]
Consequently, if in addition \(0\le q_e\le1/(2b)\) everywhere, then \(|\ell(f)|\le V_G(f)/(2b)\). For a corner indicator \(f=\mathbf1_{\{c\}}\), the corner has precisely two incident edges, while \(|\ell(f)|=1/b\) when \(c\) is black. When both sides are odd, all four corners are black; otherwise both colors have \(b=w\), so any corner works. Thus this indicator gives equality once the certificate exists.

**2. Even-order rectangles.** Suppose \(N\) is even. At least one dimension, say \(m\), is even. There is a Hamiltonian cycle: traverse columns \(1,\ldots,n-1\) alternately left-to-right and right-to-left down the rows, then ascend column \(0\) to close the cycle. This description applies when \(m\) is even; otherwise exchange axes. Give every edge of this cycle weight \(1/(2b)\) and all remaining edges zero. Every vertex belongs to exactly two cycle edges, hence its incident sum is \(1/b=1/w\). This is the required certificate.

**3. Odd-order rectangles: eight-path construction.** Suppose \(m,n\) are both odd, hence \(b=w+1\). A *horizontal snake* lists all vertices in row order, traversing alternate rows in opposite column directions. There are four choices, given by the first/last row and the initial horizontal direction. There are analogously four vertical snakes. Every snake is a Hamiltonian path starting and ending at black corners.

For a given snake \(v_1,\ldots,v_N\), let \(c_v=1/b\) on black vertices and \(c_v=-1/w\) on white vertices. On the edge \(\{v_t,v_{t+1}\}\), put a flow with magnitude
\[
q_t=\begin{cases}
(N-t)/(2bw),&t\text{ odd},\\
t/(2bw),&t\text{ even}.
\end{cases}
\]
Every \(q_t\) is nonnegative. Indeed, the cumulative sum \(\sum_{s\le t}c_{v_s}\) equals \((N-t)/(2bw)\) for odd \(t\), and \(-t/(2bw)\) for even \(t\); the path alternates black/white, so these quantities give the same nonnegative orientation from black to white. Set the flow to zero on edges outside the path. Telescoping the cumulative sums shows that the incident flow at each black vertex is \(1/b\) and at each white vertex is \(1/w\); thus every individual snake supplies the correct signed functional, although its largest edge load can exceed \(1/(2b)\).

Set \(\alpha=(m-1)/(m+n-2)\), \(\beta=(n-1)/(m+n-2)\). Average the four horizontal-snake flows with total weight \(\alpha\), and the four vertical-snake flows with total weight \(\beta\). Call the resulting flow \(q\). It remains nonnegative and has the desired vertex sums. We check the uniform edge capacity.

For a horizontal edge joining \((i,j)\) to \((i,j+1)\), with \(0\le j\le n-2\), the mean of the four horizontal-snake flows is exactly
\[
R_{i,j}=\frac{N+(-1)^{i+j}(n-2j-2)}{4bw}.
\]
The mean of the four vertical-snake flows is zero unless \(i=0\) or \(i=m-1\); at those boundary rows it equals
\[
C_{i,j}=\frac{m}{4bw}\,s_j,\qquad
s_j=\begin{cases}n-1-j,&j\text{ even},\\j+1,&j\text{ odd}.\end{cases}
\]
For the horizontal-snake mean, the same horizontal edge occurs after \(t_1=in+j+1\) or \(t_2=in+n-1-j\) vertices, depending on the row direction. These positions have opposite parity; the two reversed snakes reproduce the same unoriented flow. For vertical snakes, the horizontal edge appears only at a first/last row connector, after \(km\) vertices with \(k=j+1\) or \(k=n-1-j\). Averaging the corresponding \(q_t\) values gives the displayed formulas. Therefore \(q_{i,j}=\alpha R_{i,j}+\beta C_{i,j}\).

For an interior row \(0<i<m-1\), \(C_{i,j}=0\) and
\[
4bw\,q_{i,j}\le\alpha(N+n-2)<N-1=2w,
\]
because the positive difference after clearing the denominator \(m+n-2\) is exactly \(m(n-1)^2\). For either boundary row, \((-1)^i=1\). When \(j\) is even, the numerator \(4bw\,q_{i,j}\) is
\[
\alpha(N+n-2j-2)+\beta m(n-1-j),
\]
strictly decreasing with \(j\); when \(j\) is odd it is
\[
\alpha(N-n+2j+2)+\beta m(j+1),
\]
strictly increasing with \(j\). The two largest endpoint values, at \(j=0\) and \(j=n-2\), agree and equal
\[
\alpha(N+n-2)+\beta m(n-1)=N-1=2w.
\]
Thus every horizontal edge satisfies \(q_{i,j}\le 1/(2b)\). Interchanging \(m,n\) and the two coordinate axes gives the same conclusion for vertical edges. This completes the odd-order capacity certificate.

**4. Exact norm and stability consequences.** Parts 1–3 prove the bound and corner attainment for every rectangle, so the norm is \(e/(2b)\). For even \(N\), \(e/N=2-1/m-1/n\); with \(m,n\ge2\) it is at most one exactly at \(m=n=2\). For odd \(N\), both sides are at least three and \(e/(N+1)>1\); indeed \(mn-m-n-1=(m-1)(n-1)-2\ge2\). Finally, as both dimensions tend to infinity, \(e/(2b)\to2\).

## Verification
The standalone Python 3 standard-library checker `verify.py` constructs all eight snake flows with exact rational arithmetic, compares them with the explicit edge formulas, and verifies vertex conservation and the edge-capacity inequalities on all \(144\) rectangles with side lengths from \(2\) through \(13\). It independently enumerates all nonconstant binary cuts for seven small rectangles, including odd-by-odd examples, and verifies the sharp formula. Larger odd rectangles receive additional exact rational flow checks. Run `python3 verify.py`. These finite computations test the formulas and their implementation; the unrestricted all-grid theorem is the symbolic proof above.

## Relationship to prior work
Chambolle, Giacomini and Lussardi (arXiv:0902.2313, first posted February 13, 2009) develop discrete perimeter/total-variation energies and a generalized coarea formula. These establish the natural edge-variation setting, not the norm of the particular two-class grid projector. The classical rectangular grid Hamiltonian literature of Itai, Papadimitriou and Szwarcfiter (1982) addresses existence of paths and cycles; the even-grid cycle constructed above is a proof ingredient, not a new Hamiltonicity assertion.

A previously published result on *cyclic* two-color conditional expectations gives an exact prefix-discrepancy norm and equal-run stability classification for cycles. The present claim concerns the edge norm of the entire two-dimensional grid. The cyclic theorem can help bound even-order rectangles via a spanning cycle; it does not supply an odd-by-odd bipartite cycle, nor the eight-path edge-capacity construction and sharp odd-order denominator. Prior results on two-color averages for linearly ordered paths or complete-pair Gini variation concern different edge geometries or norms. No novelty is asserted for linear conditional expectations, Hamiltonian snake paths, elementary coarea, or flow duality themselves.

## Limitations
The exact formula uses free-boundary, nearest-neighbor, unit-weight rectangular grids and unweighted within-color means. It does not address nonuniform edge weights, unequal averaging masses within a color, other grid shapes, or graph total variation on arbitrary bipartite graphs. The proof and checks do not constitute historical-priority certification; an unindexed equivalent could exist. The exhaustive cut enumeration is confined to small grids and is not used to justify the infinite family.

## References
1. A. Chambolle, A. Giacomini, L. Lussardi, *Continuous limits of discrete perimeters*, arXiv:0902.2313v1, first posted 2009-02-13, https://arxiv.org/abs/0902.2313 ; original analysis in Sections 1 and 3.
2. A. Itai, C. H. Papadimitriou, J. L. Szwarcfiter, *Hamilton Paths in Grid Graphs*, SIAM Journal on Computing 11 (1982), 676–686, https://doi.org/10.1137/0211056 .
3. *Sharp cyclic-variation stability of two-cell conditional expectations*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-cyclic-variation-stability-of-two-cell-conditional-expecta--19779f163091 .
