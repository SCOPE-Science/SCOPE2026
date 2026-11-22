# Two sharp temporal transitions in the bounded-variation sensitivity of star-graph heat flow

## Finding
Let \(k\ge2\) be an integer. On the unit-conductance star with center \(0\) and leaves \(1,\ldots,k\), let \(L\) be its ordinary combinatorial graph Laplacian, \(P_t=e^{-tL}\), and \(V(x)=\sum_{i=1}^k|x_i-x_0|\). The sharp, attained temporal BV sensitivity of the heat trajectory is
\[
D_k(t)=\sup_{V(x)>0}\frac{V(\partial_tP_tx)}{V(x)}
=e^{-t}\left(\left|1-\frac{1-(k+1)e^{-kt}}{k}\right|+(k-1)\left|\frac{1-(k+1)e^{-kt}}{k}\right|\right),\quad t\ge0.
\]
Writing \(t_0=\log(k+1)/k\), this is equivalently
\[
D_k(t)=\begin{cases}
(k+1)e^{-(k+1)t},&0\le t\le t_0,\\
\dfrac{e^{-t}}k\bigl[2(k-1)-(k-2)(k+1)e^{-kt}\bigr],&t\ge t_0.
\end{cases}
\]
For \(k=2\) or \(3\), this function decreases strictly on \([0,\infty)\). For each \(k\ge4\), it decreases strictly to a nondifferentiable local minimum at \(t_0\), then increases strictly to one secondary peak at
\[
t_1=\frac1k\log\frac{(k-2)(k+1)^2}{2(k-1)}>t_0,
\]
and decreases strictly thereafter. The secondary peak height is
\[
M_k=\frac{2(k-1)}{k+1}\left[\frac{2(k-1)}{(k-2)(k+1)^2}\right]^{1/k}.
\]
These heights strictly increase with integer \(k\ge4\), approach \(2\) as \(k\to\infty\), and satisfy \(M_k>1\) **exactly for \(k\ge9\)**. For every degree and every time, a single-leaf step \(x_0=0\), \(x_j=1\), \(x_i=0\) for \(i\ne j\) attains the sharp operator norm. This is a *time-derivative* variation norm, not the norm of \(P_t\), and not the time derivative of the latter norm.

## Assumptions and scope
All vertex values are real, vertex masses and conductances are one, edge variation weights are one, the graph is exactly a finite star, time is real and nonnegative, and the derivative is the right derivative at \(t=0\). The quotient is taken only over signals with nonzero edge variation; constants form the nullspace. The same sharp coefficient controls \(V(\partial_tP_tx-\partial_tP_ty)\) relative to \(V(x-y)\) for arbitrary pairs with nonzero difference variation.

## Proof
**(1) Exact gradient evolution.** Write \(d_i=x_i-x_0\), \(\sigma=\sum_i d_i\), and \(d=(d_i)\). The unnormalized heat equation \(\dot u_i=u_0-u_i\) on leaves and \(\dot u_0=\sum_i(u_i-u_0)\) at the center gives \(\dot d=-d-\mathbf1\mathbf1^\top d\). Since the rank-one matrix \(J=\mathbf1\mathbf1^\top\) satisfies \(J^2=kJ\), the exact edge transfer matrix is \(e^{-t(I+J)}=e^{-t}[I-(1-e^{-kt})J/k]\). Differentiating yields
\[
\partial_t d(t)=e^{-t}[-I+b_k(t)J]d(0),\qquad b_k(t)=\frac{1-(k+1)e^{-kt}}k.
\]
**(2) Sharp coefficient and attainment.** Every \(d\in\mathbb R^k\) occurs as the edge difference vector of a vertex input (take \(x_0=0\)). Therefore the BV quotient norm is the induced real \(\ell^1\) norm of the edge matrix. Each column has diagonal entry \(e^{-t}[-1+b_k(t)]\) and \(k-1\) off-diagonal entries \(e^{-t}b_k(t)\). As \(b_k(t)<1\) always, their common absolute column sum is exactly \(D_k(t)\). Each column is realized by the claimed single-edge step, proving the equality for all real \(k\)-vectors, not merely a numerical lower bound.

**(3) Turning points.** The coefficient \(b_k\) changes sign once at \(t_0\). In its negative phase the column sum simplifies to \((k+1)e^{-(k+1)t}\), strictly decreasing. The positive phase has the stated two-exponential expression; its derivative has sign equal to
\[
-2(k-1)+(k-2)(k+1)^2e^{-kt}.
\]
At \(t_0\) that sign equals \(k(k-3)\). Consequently \(k=2,3\) give strict decrease for all positive times, while \(k\ge4\) have exactly one later zero at \(t_1\) and the asserted decrease–increase–decrease pattern. The left derivative at \(t_0\) is negative, and the right derivative is different, so \(t_0\) is a cusp when \(k\ge4\). Substitution of the critical exponential gives \(M_k\).

**(4) Strict size monotonicity and the first superunit peak.** Extend \(M_k\) to real \(x\ge4\). Direct differentiation gives
\[
x^2\frac{d}{dx}\log M_x
=\log\frac{(x-2)(x+1)^2}{2(x-1)}
+\frac{x(x-5)}{(x-1)(x-2)(x+1)}.
\]
The logarithm has argument at least \(25/3\) and increases with \(x\). The rational remainder is nonnegative for \(x\ge5\) and no less than \(-2/15\) on \([4,5]\); hence the whole expression is positive. Exact rational powers establish
\[
M_8^8=\frac{10330523392}{10460353203}<1,\qquad M_9^9=\frac{536870912}{341796875}>1.
\]
Strict size monotonicity proves the precise integer threshold. Finally \(\log M_x=\log 2+O((\log x)/x)\), so \(M_k\to2\).

## Verification
The included Python 3 standard-library script `check_star_heat_derivative.py` reconstructs the formula independently from vertex heat evolution, compares finite-difference temporal gradients with the exact edge formula, checks one-edge equality for 2 through 80 leaves, tests arbitrary real signals at 1,740 random instances, checks stationary points for 4 through 150 leaves, and verifies the threshold at degrees eight and nine by exact rational arithmetic. Its reported PASS lines are finite corroboration; the rank-one exponentiation, column-sum identity and monotonicity arguments above constitute the proof for every integer degree and every real time.

## Relationship to prior work
Keller and Lenz [1] establish the graph Dirichlet-form semigroup framework, without an exact finite-star edge-BV temporal derivative norm. Chen, Coulhon and Hua [2] establish general \(\ell^p\) heat-gradient estimates for \(1<p\le2\), rather than the sharp \(p=1\) time-derivative BV norm or its degree-nine rebound threshold. A published complete-bipartite heat-flow result [3] gives a **graph-Lipschitz norm of \(P_t\)** and thus describes a related operator on the star, but its indexed statement does not give the BV norm of \(\partial_tP_t\); these are distinct norms, and in general differentiating an operator norm does not yield the norm of the derivative. A published weighted-tree variation result [4] characterizes **all-time contraction of \(P_t\)**, not its sharp time-derivative norm or its secondary extremum. A friendship-graph result [5] studies time derivatives in a different graph and a different input/output norm. The present calculation adds an exact edge-variation temporal-sensitivity profile, its full turning-point classification, and the superunit degree boundary. Indexed summaries of [3]–[5] were available, but their complete underlying texts could not be inspected here; this is an explicit priority limitation.

## Limitations
The numerical checker does not establish the infinite-degree assertions. No independent audit has been performed. The conclusion does not cover degree-normalized generators, unequal spoke conductances, nonuniform vertex masses, general trees, or general \(p\)-variation. Historical priority is not guaranteed: the exact finite-star formula may appear implicitly in an unindexed calculation or fuller version of a related paper. For \(k=2,3\), the corner at \(t_0\) does not produce a secondary local minimum; the degree-four boundary in the statement is exact.

## References
1. M. Keller and D. Lenz, *Dirichlet forms and stochastic completeness of graphs and subgraphs*, arXiv:0904.2985, first submitted 20 April 2009. https://arxiv.org/abs/0904.2985
2. L. Chen, T. Coulhon and B. Hua, *Riesz transforms for bounded Laplacians on graphs*, arXiv:1708.05476, first submitted 18 August 2017. https://arxiv.org/abs/1708.05476
3. *Exact transient Lipschitz amplification for complete-bipartite heat semigroups*, indexed mathematical finding, 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-transient-lipschitz-amplification-for-complete-bipartite-h--469537d6a8c8
4. *A conductance-independent contraction criterion for weighted tree heat flow in total variation*, indexed mathematical finding, 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-conductance-independent-contraction-criterion-for-weighted-tre--9fedb9294a7c
5. *Two sharp temporal sensitivity transitions for heat flow on friendship graphs*, indexed mathematical finding, 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-two-sharp-temporal-sensitivity-transitions-for-heat-flow-on-frie--08990441c272
