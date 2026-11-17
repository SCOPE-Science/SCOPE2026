# Sharp graph-variation stability of softmax by weighted minimum cuts

## Finding

Let \(G=(V,E,w)\) be a finite connected simple undirected graph on \(n\ge2\) vertices, with strictly positive edge weights \(w_e\), and let \(\beta>0\). The inverse-temperature-\(\beta\) softmax is
\[
\sigma_\beta(x)_i=\frac{\exp(\beta x_i)}{\sum_{j\in V}\exp(\beta x_j)}.
\]
With weighted edge total variation
\[
\operatorname{TV}_w(h)=\sum_{\{u,v\}\in E}w_{uv}|h_u-h_v|,
\]
write \(d_w(i)=\sum_{e\ni i}w_e\) and
\[
\lambda_w(i,j)=\min_{S\subset V:\ i\in S,\ j\notin S}\sum_{e\in\partial S}w_e.
\]
Then the **exact global two-input graph-variation Lipschitz constant** is
\[
\boxed{\ \sup_{\operatorname{TV}_w(x-y)>0}
\frac{\operatorname{TV}_w(\sigma_\beta(x)-\sigma_\beta(y))}
{\operatorname{TV}_w(x-y)}
=\frac{\beta}{4}\max_{i\ne j}\frac{d_w(i)+d_w(j)}{\lambda_w(i,j)}.\ }
\]
In particular, the map is variation-nonexpansive if and only if \(\beta(d_w(i)+d_w(j))\le4\lambda_w(i,j)\) for every distinct pair.

For **unit edge weights** and \(\beta=1\), every connected graph on \(n\) vertices has constant at most \(n/4\). Equality holds precisely when some bridge joins two vertices that are each adjacent to every other vertex on their respective side of that bridge. In particular, a star on \(n\) vertices attains the sharp \(n/4\) envelope.

On a unit-weight tree with degrees sorted as \(d_{(1)}\ge d_{(2)}\ge\cdots\), the sharp constant is \((d_{(1)}+d_{(2)})/4\); the only trees on which it is at most one are paths and the four-vertex, three-leaf star (including all shorter paths). On a complete bipartite graph \(K_{a,b}\) with \(1\le a\le b\), it is \(\max\{1/2,(a+b)/(4a)\}\), with strict amplification exactly when \(b>3a\).

The displayed global constants are suprema. For \(n>2\), sharpness is exhibited by sequences of finite input pairs approaching a two-atom softmax distribution, not by an assertion that softmax can assign zero probability to any coordinate.

## Assumptions and scope

All signals are real vectors indexed by \(V\); all input pairs have nonzero graph total variation in their difference. Graph connectivity and positive edge weights ensure that \(\operatorname{TV}_w\) is a norm modulo constant vectors. Edge weights multiply absolute edge differences and are not used in the definition of the softmax map. No restriction to nonnegative input scores is required. A weighted cut's capacity is the sum of its crossing edge weights; \(\lambda_w(i,j)>0\).

The argument also proves a finite-dimensional norm principle: if \(N\) is *any* norm on \(\mathbb R^n/\operatorname{span}\{\mathbf1\}\) (regarded as a seminorm on \(\mathbb R^n\)) and \(N^*\) is the dual norm on zero-sum vectors, then
\[
\sup_{N(x-y)>0}\frac{N(\sigma_\beta(x)-\sigma_\beta(y))}{N(x-y)}
=\frac{\beta}{4}\max_{i\ne j}N(e_i-e_j)N^*(e_i-e_j).
\]
The graph formula is the specialization in which the two factors are weighted degree sum and reciprocal minimum cut.

## Proof

**1. A sharp covariance maximization lemma.** For arbitrary fixed vectors \(u,v\in\mathbb R^n\), and for every probability vector \(p\), set
\[
F(p)=\sum_i p_i u_i v_i-\Big(\sum_i p_i u_i\Big)\Big(\sum_i p_i v_i\Big).
\]
Then
\[
\max_{p\in\Delta_n}F(p)
=\frac14\max\!\left\{0,\ \max_{i\ne j}(u_i-u_j)(v_i-v_j)\right\}.
\]
To prove the upper bound, choose a maximizer \(p\) with smallest support. If its support contained distinct \(i,j\) with \((u_i-u_j)(v_i-v_j)\le0\), transferring probability mass between just these coordinates would give a convex (or affine) function of the transfer: its quadratic coefficient is \(-(u_i-u_j)(v_i-v_j)\ge0\). An endpoint would be a maximizer with smaller support, a contradiction. Thus all supported pairs have strictly concordant \(u\)- and \(v\)-ordering. The maximum and minimum of both vectors on the support occur at the same two indices. Cauchy--Schwarz followed by the elementary bound \(\operatorname{Var}(X)\le(\max X-\min X)^2/4\) shows \(F(p)\le(\max u-\min u)(\max v-\min v)/4\) on that support. This product belongs to the displayed pairwise maximum. A one-point support gives zero. Conversely, placing mass \(1/2\) on each of any maximizing concordant pair realizes a quarter of its product; one-point mass realizes zero. This establishes equality without assuming all entries of \(p\) are positive.

**2. Dual-norm reduction.** For a positive probability vector \(p=\sigma_\beta(x)\), differentiation gives
\[
D\sigma_\beta(x)=\beta\bigl(\operatorname{Diag}(p)-pp^{\mathsf T}\bigr).
\]
Since this matrix annihilates constants, it induces a bounded linear map on the quotient. For input \(h\) and zero-sum dual functional \(z\), its bilinear pairing is \(\beta F(p)\) for \(u=h,v=z\). Apply step 1, take the supremum over \(N(h)\le1\) and \(N^*(z)\le1\), and use finite-dimensional norm duality:
\[
\sup_{N(h)\le1}|h_i-h_j|=N^*(e_i-e_j),\qquad
\sup_{N^*(z)\le1}|z_i-z_j|=N(e_i-e_j).
\]
Interchanging the finitely many pair maxima with the norm-ball suprema gives the norm principle in the previous section. The boundary probability vectors are limits of positive softmax outputs: assign equal large scores to the chosen two coordinates and scores tending to minus infinity to the others. Thus the supremum of Jacobian norms at *actual finite scores* equals the boundary maximum. Integrating the Jacobian along a line segment proves the upper bound for all two-input pairs, and small increments in a norming direction near any score vector establish the converse supremum. The inverse temperature contributes the factor \(\beta\).

**3. Identifying the graph dual factors.** The vector \(e_i-e_j\) changes along every edge incident with exactly one of its two nonzero coordinates by magnitude one, and along edge \(\{i,j\}\), if present, by magnitude two. Therefore
\[
\operatorname{TV}_w(e_i-e_j)=d_w(i)+d_w(j).
\]
For any signal \(h\), discrete coarea gives
\[
\operatorname{TV}_w(h)=\int_{-\infty}^{\infty}\sum_{e\in\partial\{v:h_v>t\}}w_e\,dt.
\]
If \(h_i>h_j\), every level cut for \(h_j<t<h_i\) separates \(i,j\), so \(\operatorname{TV}_w(h)\ge\lambda_w(i,j)(h_i-h_j)\); similarly for the opposite inequality. Conversely, the indicator of an \(i,j\)-minimum cut has \(h_i-h_j=1\) and variation exactly \(\lambda_w(i,j)\). Hence
\[
N^*(e_i-e_j)=\sup_{\operatorname{TV}_w(h)\le1}|h_i-h_j|=\lambda_w(i,j)^{-1}.
\]
Substitution proves the main formula with equality in the supremum. For a direct sharpness sequence, choose a maximizing pair \(i,j\), a minimum-cut indicator \(h\), and scores whose softmax tends to \((e_i+e_j)/2\); the Jacobian applied to \(h\) approaches \(\beta(e_i-e_j)/4\), after which an infinitesimal perturbation of the scores along \(h\) gives the ratio.

**4. Unit-weight structure.** If \(\lambda(i,j)\ge2\), then \((d_i+d_j)/\lambda(i,j)\le n-1<n\). If \(\lambda(i,j)=1\), a one-edge minimum cut is a bridge separating vertex sets \(S\) and \(V\setminus S\) with \(i\in S,j\notin S\); consequently \(d_i\le|S|\) and \(d_j\le n-|S|\), giving a ratio at most \(n\). Equality requires \(i,j\) to be the endpoints of the bridge and each to be adjacent to every other vertex on its own side, and these conditions suffice. Every tree has \(\lambda(i,j)=1\), proving its degree formula and nonexpansivity classification: if a tree has a degree-three vertex and is not the four-vertex star, it has another vertex of degree at least two, while a degree-four vertex already forces expansion. In \(K_{a,b}\), same-side vertex pairs give ratio \(2\) and cross-side pairs give ratio \((a+b)/a\), proving the asserted formula and threshold.

## Verification

The included standalone Python checker, `verify_softmax_graph.py`, uses only the Python standard library and exact integer/fraction arithmetic. Run `python verify_softmax_graph.py`. It tests the covariance pair inequality on \(240570\) finite rational/value cases, verifies \(1547790\) softmax-Jacobian/cut inequalities on all \(771\) connected labelled simple graphs with two to five vertices, checks \(30308\) weighted graph cases, and tests rational sharpness approaches on fourteen stars plus fifteen biclique parameters. The checker evaluates the proposed formulas independently using minimum-cut enumeration. The universal proof does not rely on these finite tests.

## Relationship to prior work

Martins and Astudillo (2016, Section 2.5) give the softmax Jacobian \(\operatorname{Diag}(p)-pp^{\mathsf T}\) and contrast it with sparsemax, but do not calculate its sharp variation norm on a weighted graph. Sandryhaila and Moura (2013) motivate variation of graph signals; their adjacency-shift definition differs from the edgewise weighted \(\ell_1\) seminorm here. Nair (2025) proves the sharp \(1/2\) Lipschitz constant for standard \(\ell_p\) norms; it does not determine graph-edge variation constants that may exceed one and grow with graph size. Liu and Yin (2021/2023) propose a *different*, graph-variation-regularized softmax/graphmax optimization map, and do not provide the coefficient here for ordinary softmax. The current theorem combines an exact covariance probability optimization with graph minimum cuts; it is not a restatement of these results.

## Limitations

The result concerns finite real score vectors, positive inverse temperature, symmetric positive edge weights, and undirected connected graphs. For disconnected graphs the variation seminorm has a larger kernel and different quotient-domain behavior. Directed graphs, signed edge weights, alternative softmax definitions with nonuniform base probabilities, and infinite graphs are not analyzed. On dimensions above two the two-atom boundary probabilities used for sharpness are limiting states, so finite input-pair attainment is not asserted. Literature comparison is not a formal guarantee against unindexed equivalent earlier work.

## References

1. A. Sandryhaila and J. M. F. Moura, *Discrete Signal Processing on Graphs: Frequency Analysis*, arXiv:1307.0468, first posted July 1, 2013; graph variation background (different normalization).
2. A. F. T. Martins and R. F. Astudillo, *From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification*, arXiv:1602.02068, first posted February 5, 2016; especially Eq. (8) and Section 2.5. Published in PMLR 48 (2016), pages 1614--1623.
3. B. Liu and G. Yin, *A Graph Total Variation Regularized Softmax for Text Generation*, arXiv:2101.00153, initially posted January 1, 2021; later published as *Graphmax for Text Generation*, JAIR 78 (2023).
4. P. Nair, *Softmax is 1/2-Lipschitz: A Tight Bound across All \(\ell_p\) Norms*, arXiv:2510.23012, October 27, 2025.
