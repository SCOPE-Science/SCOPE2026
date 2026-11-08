# Distance-layer flows give all optimal fixed Kaczmarz sampling laws on graphs

## Finding

**Theorem (graph-wide optimal fixed sampling and its complete optimizer face).** Let \(G=(V,E)\) be any finite, simple, connected undirected graph with \(|V|\ge 2\). Let \(A\subseteq V\) be nonempty. The admissible unit-norm measurements are the absolute readings \(e_a\) for \(a\in A\), together with normalized differences \((e_u-e_w)/\sqrt2\) for all \(\{u,w\}\in E\). For a fixed probability law \(p\) on these rows, write

\[
M(p)=\sum_{a\in A}p_a e_ae_a^{\mathsf T}
+\frac12\sum_{\{u,w\}\in E}p_{uw}(e_u-e_w)(e_u-e_w)^{\mathsf T}.
\]

Define the unweighted graph distance to the anchor set \(d_x=\min_{a\in A}\operatorname{dist}_G(x,a)\), the strictly positive potential \(v_x=1+\sqrt2\,d_x\), and \(S=\sum_{x\in V}v_x^2\). Then

\[
\boxed{\max_{p\ge0,\;\sum p=1}\lambda_{\min}(M(p))=S^{-1}.}
\]

All maximizing laws, without exception, are precisely the following **distance-descending nonnegative flow polytope**. Every edge whose endpoints have equal distance to \(A\) receives probability zero. Every edge joining distance layers \(d_x=k\) and \(d_w=k-1\) is oriented \(x\to w\) and carries a nonnegative flow \(f_{xw}\). For every nonanchor \(x\in V\setminus A\), these flows satisfy

\[
\sum_{w\sim x,\;d_w=d_x-1}f_{xw}
-\sum_{z\sim x,\;d_z=d_x+1}f_{zx}=\frac{v_x}{S}.
\]

The corresponding sampling probabilities are \(p_{xw}=\sqrt2\,f_{xw}\) on descending edges and

\[
p_a=\frac1S+\sum_{z\sim a,\;d_z=1}f_{za}\qquad (a\in A).
\]

No other restrictions or normalizing step are necessary: these equations imply \(p\ge0\), \(\sum p=1\), and optimality. In particular, an optimal law **always has support on a multi-source breadth-first-search forest and its roots**, and can be constructed in \(O(|V|+|E|)\) arithmetic operations. The optimizer is unique exactly when each nonanchor has **one** neighbor one distance layer closer to \(A\).

## Assumptions and scope

The measured linear equations are consistent. Every row is Euclidean unit-normalized as specified, and rows are sampled independently from one fixed, freely chosen probability law. Anchors have rows \(e_a\) with no additional price or sampling constraint. Edge lengths are graph-hop lengths, not physical or resistance lengths. The optimization criterion is the sharp worst-direction **one-step expected squared Euclidean error reduction**: for error \(z\), a randomized Kaczmarz projection gives \(\mathbb E\|z^+\|^2=\|z\|^2-z^{\mathsf T}M(p)z\), and the least directional reduction equals \(\lambda_{\min}(M(p))\). The case \(A=V\) is included, with the unique optimum sampling only the \(|V|\) anchor rows uniformly.

## Proof

**Step 1: universal upper bound.** Every anchor has \(e_a^{\mathsf T}v=1\). Any edge has \(|d_x-d_w|\le1\), hence

\[
\left|\frac{v_x-v_w}{\sqrt2}\right|\le1.
\]

Therefore \(v^{\mathsf T}M(p)v\le\sum p=1\) for *every* probability law. Taking its Rayleigh quotient yields \(\lambda_{\min}(M(p))\le S^{-1}\). Equality in this quadratic bound requires zero probability on all same-layer edges. This is a global bound over all individually chosen rows; no symmetry or support restriction is assumed.

**Step 2: constructing an attaining law.** Choose an arbitrary breadth-first forest rooted at every anchor, assigning each nonanchor \(x\) one adjacent parent with distance \(d_x-1\). Let \(H_x\) be the sum of \(v_z\) over the descendants of \(x\), including \(x\) itself. Put

\[
p_{x,\operatorname{parent}(x)}=\frac{\sqrt2\,H_x}{S},
\quad x\notin A;\qquad
p_a=\frac{H_a}{S},\quad a\in A;
\]

and zero on all other edges. Each vertex \(z\) appears in one rooted subtree at its root and in exactly \(d_z\) nonroot subtrees, so

\[
\sum_{a\in A}H_a+\sqrt2\sum_{x\notin A}H_x
=\sum_{z\in V}v_z(1+\sqrt2d_z)=S.
\]

Thus these weights sum to one. The row action \(M(p)v\) has coordinate \((H_x-\sum_{y\text{ child of }x}H_y)/S=v_x/S\) at nonanchors. At anchors, the root contribution \(H_a/S\) minus the child contributions again gives \(v_a/S=1/S\). Consequently \(M(p)v=v/S\).

**Step 3: this eigenvalue is the least one.** For any symmetric matrix \(M\) with nonpositive off-diagonal entries and any strictly positive vector \(v\) satisfying \(Mv=\lambda v\), define \(D=\operatorname{diag}(v)\). Then \(D(M-\lambda I)D\) has zero row sums and nonpositive off-diagonal entries, so for every real \(y\),

\[
y^{\mathsf T}D(M-\lambda I)Dy
=\sum_{i<j}(-M_{ij})v_iv_j(y_i-y_j)^2\ge0.
\]

The formula is valid even with disconnected positive-probability edge support. As \(D\) is invertible, \(M-\lambda I\succeq0\), proving \(\lambda=\lambda_{\min}(M)\). The constructed law has \(\lambda=S^{-1}\), so Step 1 is attained.

**Step 4: characterizing every optimizer.** At an optimum \(\lambda_{\min}(M)=S^{-1}\), and the sandwich \(S^{-1}\le v^{\mathsf T}Mv/S\le S^{-1}\) is equality. Equality in Step 1 removes all same-layer edges. Equality in Rayleigh–Ritz also requires \(Mv=v/S\). For an edge descending from \(x\) to \(w\), the difference \(v_x-v_w=\sqrt2\), so its contribution to \((Mv)_x\) is \(p_{xw}/\sqrt2=f_{xw}\). The coordinate equations at nonanchors become exactly the displayed incoming/outgoing flow balances; at anchors they determine exactly the displayed \(p_a\). Conversely, any nonnegative solution of those balances gives \(Mv=v/S\) and all unused edges have zero probability. Dotting this eigenvector identity with \(v\), using \(v^{\mathsf T}M v=\sum_a p_a+\sum_{x\to w}p_{xw}\) and \(v^{\mathsf T}v=S\), proves \(\sum p=1\). Step 3 then establishes optimality. Thus no optimizers are missing.

**Step 5: uniqueness.** If every nonanchor has one predecessor, the balance equation can be solved uniquely by descending induction from the maximum distance layer; then each anchor weight is determined. If some nonanchor has two predecessors, two breadth-first forests differing only in the parent choice for that vertex give different probabilities (the moved subtree has strictly positive \(H_x\)). Both are optimal by Step 2. Hence the stated uniqueness condition is necessary and sufficient.

## Verification

Run \(`python3 verify_graph_kaczmarz.py`\) with Python's standard library. Exact arithmetic in \(\mathbb Q(\sqrt2)\) checked the forest normalization, vector eigen-identity, distance inequality, and the unique-predecessor criterion for **23,169** pairs of connected labelled graphs with at most five vertices and nonempty anchor sets, returning `VERIFY_OK 23169 cases; unique 6891 nonunique 16278`. These are finite consistency checks; Steps 1–5 are the proof for all graphs.

For a complete graph \(K_n\) with only its distinguished vertex anchored, every other vertex is at distance one. Thus \(S=1+(n-1)(3+2\sqrt2)\). The optimal law assigns \(p_a=[1+(n-1)(1+\sqrt2)]/S\) at the anchor and \(p_{au}=(2+\sqrt2)/S\) on each incident edge, while **every** edge between two nonanchors is never sampled. For a four-cycle with one anchored vertex, the opposite vertex has two predecessors and the optimal face contains multiple laws.

## Relationship to prior work

Strohmer and Vershynin (2007) proved exponential convergence for randomized row projections and developed the canonical row-norm sampling framework. The present graph-specific problem asks a different, sharp E-optimal fixed-row question: how to maximize the smallest eigenvalue of the sampling information matrix and describe **every** maximizing probability law. Steinerberger (2020) studies residual-dependent adaptive Kaczmarz sampling; it does not choose a fixed graph-wide optimum. Classical E-optimal design provides a semidefinite characterization, not the explicit distance-potential value and entire shortest-layer flow polytope.

The published *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* covers square nonsingular inverse-positive Hessian settings and in particular can subsume some single-root tree cases through their square row-incidence transforms. Its stated assumption does not cover the **rectangular, redundant** anchor-plus-edge rows on arbitrary cycles or graphs with multiple anchors, for which the row Gram matrix is singular. The previously recorded endpoint-anchored path calculation is a special case, not a claimed new theorem here. The claim advanced here is the universal all-graph distance law, exact support/flow face, and the graph-theoretic if-and-only-if uniqueness criterion.

Rosa's work on E-optimal treatment comparisons represented by graphs optimizes treatment replication proportions in a vertex-weighted Laplacian design; it does not optimize one-step selection of both anchor and normalized graph-difference rows as defined here. We cannot rule out equivalent results in unindexed literature or unpublished E-optimal experimental design studies.

## Limitations

The conclusion depends on the **unit-normalized** edge differences, freely variable probabilities, fixed iid sampling, and Euclidean one-step worst-case squared-error criterion. It does not optimize finite-horizon errors, actual long-run error exponents, adaptive sampling, noisy or inconsistent equations, or edge-specific costs. The theorem does not imply that choosing the fewest nonzero measurements always gives the best alternative convergence metric. Independent verification has not been performed; available full-text and index comparisons cannot guarantee publication novelty.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226v1, publicly submitted 2007-02-08, https://arxiv.org/abs/math/0702226 .
2. S. Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, arXiv:2007.02910v1, publicly submitted 2020-07-06, https://arxiv.org/abs/2007.02910 .
3. S. Rosa, *Optimal designs for treatment comparisons represented by graphs*, arXiv:1612.06571v1, publicly submitted 2016-12-20, https://arxiv.org/abs/1612.06571 .
4. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995 .
