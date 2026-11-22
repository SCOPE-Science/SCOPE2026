# A sharp hub-mass budget for irreversible fusion on weighted stars

## Finding
Let \(k\ge 1\) and let \(S_k\) be the star with hub \(0\) and leaves \(1,\ldots,k\). Fix arbitrary fidelity masses \(m_0,m_1,\ldots,m_k>0\) and edge penalties \(a_1,\ldots,a_k>0\). For every real observation vector \(y\) and \(\lambda\ge0\), define its uniquely fitted signal \(u(\lambda;y)\) by
\[
u(\lambda;y)=\mathop{\arg\min}_{u\in\mathbb R^{k+1}}\left\{\frac12\sum_{j=0}^{k}m_j(u_j-y_j)^2+\lambda\sum_{i=1}^{k}a_i|u_i-u_0|\right\}.
\]
A leaf edge is *fused* if \(u_i=u_0\). The following statements are equivalent:

1. **Universal irreversible fusion:** for every \(y\in\mathbb R^{k+1}\), every leaf \(i\), and all \(0\le\lambda_0\le\lambda_1\), equality \(u_i(\lambda_0;y)=u_0(\lambda_0;y)\) implies \(u_i(\lambda_1;y)=u_0(\lambda_1;y)\).
2. **Sharp local budget:** for every leaf \(i\),
\[
\boxed{m_i\sum_{j\ne i}a_j\ \le\ (m_0+m_i)a_i.}
\]
3. **Diagonal dominance:** with \(B\) the \(k\)-by-\((k+1)\) oriented weighted incidence matrix whose \(i\)-th row is \(a_i(e_i-e_0)\), and \(M=\operatorname{diag}(m_0,\ldots,m_k)\), the positive-definite matrix \(BM^{-1}B^{\mathsf T}\) is weakly row-diagonally dominant.

There is a further, sharp *weight-design* criterion. For prescribed positive masses, **some** positive penalties make every fusion irreversible for all observations if and only if
\[
\boxed{\sum_{i=1}^{k}\frac{m_i}{m_0+2m_i}\le1.}
\]
For equal leaf masses \(m_i=m\), this is precisely \(m_0\ge(k-2)m\). In particular, with equal masses at all vertices, stars with at most three leaves are universally fusion-stable for equal penalties, while a four-leaf star is not universally fusion-stable for **any** positive choice of penalties.

For the four-leaf star with \(m_j=a_i=1\), observations \(y=(0,1,100,100,100)\) give a strict positive-time *fusion followed by separation*:
\[
u(1/2;y)=(5/4,5/4,199/2,199/2,199/2),
\qquad u(3/2;y)=(3,5/2,197/2,197/2,197/2).
\]
Thus leaf \(1\) is fused at \(\lambda=1/2\) but is not fused at \(\lambda=3/2\).

## Assumptions and scope
All vertices have strictly positive fidelity masses; all star edges have fixed strictly positive penalties; observations and fits are real; a **single common** nonnegative regularization parameter scales every edge penalty; the quadratic fidelity is diagonal. The star may have any finite number \(k\ge1\) of leaves. The claimed universal property quantifies over **all** input data, including ties, and all pairs of regularization parameters. A fused edge refers to exact equality of its two fitted endpoints, not to small numerical differences. For \(k=1\), the empty sum is zero, and the property holds without restriction. No assertion is made for arbitrary non-star graphs, nonquadratic fidelity or different parameter trajectories for different edges.

## Proof
**1. Scalar reduction and exact KKT characterization.** Fix \(\lambda>0\) and a candidate hub value \(h\). Eliminating each leaf variable in the objective by one-dimensional soft thresholding gives
\[
u_i=h+\operatorname{sgn}(y_i-h)\bigl(|y_i-h|-\lambda a_i/m_i\bigr)_+,
\]
where \(r_+=\max(r,0)\). Consequently the fitted hub is the unique zero of the continuous strictly increasing function
\[
F_\lambda(h)=m_0(h-y_0)+\sum_{i=1}^{k}\operatorname{clip}\bigl(m_i(h-y_i),-\lambda a_i,\lambda a_i\bigr),
\]
where \(\operatorname{clip}(x,-b,b)=\max(-b,\min(x,b))\). The hub derivative contains the strictly increasing term \(m_0h\), and \(F_\lambda(h)\to\pm\infty\) at the corresponding infinities. Thus its zero exists and is unique, and the leaf formula gives the unique global minimizer by strict convexity. In particular, leaf \(i\) is fused precisely when
\[
|m_i(h-y_i)|\le\lambda a_i.
\]

**2. No leaf can leave its fused set under the local budgets.** Introduce \(\tau=1/\lambda\) and \(v(\tau)=\tau u_0(1/\tau;y)\). The scalar KKT equation becomes
\[
m_0(v-\tau y_0)+\sum_{i=1}^{k}\operatorname{clip}\bigl(m_i(v-\tau y_i),-a_i,a_i\bigr)=0.
\]
The leaf fusion condition now reads \(|r_i(\tau)|\le a_i\), where \(r_i(\tau)=m_i(v(\tau)-\tau y_i)\). The function \(v\) is continuous and piecewise affine in \(\tau>0\), with finitely many pieces on compact intervals: it is the unique root of a finite piecewise-linear monotone system, or equivalently follows from its finitely many clipping patterns.

On any open affine interval, let \(I\) be the set of leaves whose clips are unsaturated, and put \(T=\{1,\ldots,k\}\setminus I\). Let \(\sigma_j\in\{-1,1\}\) be the saturated signs, and \(M_I=m_0+\sum_{j\in I}m_j\). Direct solution of the scalar equation gives
\[
v(\tau)=\frac{\tau(m_0y_0+\sum_{j\in I}m_jy_j)-\sum_{j\in T}\sigma_ja_j}{M_I}.
\]
For a fused \(i\in I\), its affine residual has a formal value at \(\tau=0\) of
\[
r_i^{\mathrm{aff}}(0)=-\frac{m_i}{M_I}\sum_{j\in T}\sigma_ja_j.
\]
The local budget implies
\[
|r_i^{\mathrm{aff}}(0)|\le\frac{m_i}{m_0+m_i}\sum_{j\ne i}a_j\le a_i.
\]
As \(\tau\) decreases within an affine interval where \(i\) is unsaturated, the value of \(r_i\) is a convex combination of its present value and this formal intercept, both in \([-a_i,a_i]\). To rule out a first exit exactly at a boundary, including ties and simultaneous clipping changes, also consider a one-sided affine cell on which \(i\) is saturated. Write \(c_i=a_i/m_i\), \(q_i(\tau)=v(\tau)-\tau y_i\), and let \(M_I\) denote the hub-plus-unsaturated mass in that cell. At a point with \(q_i=c_i\), solving the hub equation and differentiating the affine branch gives, if \(i\) is unsaturated,
\[
\tau M_I q_i'=M_Ic_i+\sum_{j\in T}\sigma_ja_j\ge M_Ic_i-\sum_{j\ne i}a_j\ge0,
\]
and, if \(i\) is saturated,
\[
\tau M_I q_i'=M_Ic_i+a_i+\sum_{j\in T\setminus\{i\}}\sigma_ja_j\ge m_0c_i+a_i-\sum_{j\ne i}a_j\ge0.
\]
The final inequalities are precisely the budget \(\sum_{j\ne i}a_j\le(m_0+m_i)c_i\), together with \(M_I\ge m_0+m_i\) in the unsaturated case and \(M_I\ge m_0\) in the saturated case. At \(q_i=-c_i\), the analogous formulas give \(q_i'\le0\). Thus on **every** incident affine cell, an upper-bound contact has nonnegative slope with increasing \(\tau\), and a lower-bound contact has nonpositive slope. Decreasing \(\tau\) therefore cannot take a currently fused edge out through either boundary, even at a simultaneous event. Continuity and finiteness of affine pieces prove persistence for all positive \(\lambda_0\) and larger \(\lambda\).

If \(\lambda_0=0\) and \(y_i=y_0\), consider the block \(I_0=\{j\ge1:y_j=y_0\}\). For all sufficiently small positive \(\lambda\), every leaf outside \(I_0\) remains saturated with sign determined by its nonzero data difference, while the candidate fused-block hub is its fidelity-weighted value plus a drift of magnitude at most \(\lambda\sum_{j\notin I_0}a_j/M_{I_0}\). The same budget inequality gives \(m_i|u_0-y_i|\le\lambda a_i\) for every \(i\in I_0\), so this candidate satisfies every KKT inequality. Hence the initially fused edges are fused for small positive \(\lambda\), and the preceding argument propagates them indefinitely.

**3. Necessity by an actual later separation.** Suppose that the budget fails for some leaf \(i\). Write \(B=\sum_{j\ne i}a_j\), \(M_*=m_0+m_i\), and \(c=M_*a_i/m_i\). Then \(B>c>0\). Choose \(H>0\), set \(y_0=0\), \(y_i=H\), and set every other observation equal to a common sufficiently large \(R>0\). On any preselected bounded \(\lambda\)-interval, the other leaves remain strictly above the fitted hub if \(R\) is large enough: the hub KKT equation bounds \(|u_0|\le\lambda\sum_j a_j/m_0\) independently of \(R\), and an unfused outside leaf equals \(R-\lambda a_j/m_j\).

If leaf \(i\) is fused and all others lie above the hub, the hub must equal
\[
h=(m_iH+\lambda B)/M_*.
\]
Its fusion inequality is equivalent to
\[
\frac{m_0H}{B+c}\le\lambda\le\frac{m_0H}{B-c}.
\]
Choose \(\lambda_1\) in the **strict interior** of this nonempty interval and a finite \(\lambda_2>m_0H/(B-c)\). Increase \(R\) so the outside leaves remain strictly above the hub up to \(\lambda_2\). At \(\lambda_1\), the displayed hub and the soft-thresholded leaves satisfy all KKT conditions, so leaf \(i\) is fused. At \(\lambda_2\), no fused solution for leaf \(i\) can satisfy its necessary fusion inequality, so it is unfused. This directly contradicts universal irreversible fusion. It also constructs counterexamples with a genuine positive-length fusion interval, rather than relying solely on a coincidence at \(\lambda=0\).

**4. Diagonal dominance and existence of stabilizing weights.** The \(i\)-th diagonal entry of \(BM^{-1}B^{\mathsf T}\) is \(a_i^2(1/m_0+1/m_i)\); each off-diagonal entry \((i,j)\) is \(a_i a_j/m_0\). Row \(i\) is diagonally dominant exactly when \((m_0+m_i)a_i\ge m_i\sum_{j\ne i}a_j\), proving equivalence with Statement 3.

Let \(A=\sum_j a_j>0\) and \(c_i=m_i/(m_0+2m_i)\). The local budget rearranges to \(a_i/A\ge c_i\). Summing proves necessity of \(\sum_i c_i\le1\). Conversely, if \(\sum_i c_i\le1\), choose \(A=1\) and \(a_i=c_i+(1-\sum_j c_j)/k\), which is strictly positive and has total weight one, and meets every budget. Equal leaf masses reduce the inequality to \(km/(m_0+2m)\le1\), i.e. \(m_0\ge(k-2)m\). This gives the claimed sharp design and degree thresholds. The explicit four-leaf fit in the statement follows by substituting the stated rational vectors in the scalar KKT equation.

## Verification
The included standalone Python 3 script `checks/verify_star_fusion.py` uses the standard library's exact rational arithmetic. It reconstructs the hub root by enumerating finite clipping intervals, checks all primal and dual KKT equalities and sign conditions, confirms the explicit four-leaf fusion/unfusion vectors, and exercises many randomly generated *stable* mass/penalty systems over increasing regularization grids. It also tests unstable equal-mass stars with explicit positive-time fusion followed by separation. Execute `python3 checks/verify_star_fusion.py` from the package root. The successful finite computations corroborate the calculations; the universal assertions are proved by Steps 1–4, **not** by the tests.

## Relationship to prior work
The graph fused-lasso path algorithm of Hoefling (arXiv:0910.0526, 2009) explicitly allows edge fusions to split on general graphs, using a max-flow test for when this is necessary (the general-graph discussion in Section 3). Tibshirani and Taylor (arXiv:1005.1971, 2010, Section 6) proved that diagonal dominance of \(DD^{\mathsf T}\) is **sufficient** for their dual boundary-persistence lemma. After whitening the diagonal fidelity, their sufficient condition already covers **the sufficient direction** of the present star criterion; that direction is not claimed as independently novel. The contribution here is a constructive **converse for all weighted stars**, its equivalence to universal *primal edge* fusion persistence including degenerate data, and the exact nontrivial hub-mass budget deciding whether any positive penalty design can work. Chiquet, Gutierrez and Rigaill (arXiv:1407.5915, 2014, Section 5) give a different no-split sufficient family based on data-dependent pairwise penalties on a complete fusion graph, not the all-observations star-edge converse here. Prior weighted-path and weighted-cycle classifications address different underlying graphs; the two-leaf star is a path special case, not a separate novelty claim.

## Limitations
The result is exact only for finite star graphs and diagonal positive quadratic fidelity. It is not an assertion that diagonal dominance is necessary for irreversible fusion on arbitrary graphs. The sufficient implication from diagonal dominance is already in generalized-lasso theory, as acknowledged above. No claim is made for adaptive or data-dependent edge penalties, graph families beyond stars, or statistical risk optimality. Priority is provisional because an unindexed specialized converse could still exist; no independent mathematical audit has been performed.

## References
1. H. Hoefling, *A path algorithm for the Fused Lasso Signal Approximator*, arXiv:0910.0526, first submitted 2009-10-03. https://arxiv.org/abs/0910.0526
2. R. J. Tibshirani and J. Taylor, *The solution path of the generalized lasso*, arXiv:1005.1971, first submitted 2010-05-11; Annals of Statistics 39 (2011), 1335–1371. https://arxiv.org/abs/1005.1971
3. J. Chiquet, P. Gutierrez and G. Rigaill, *Fast tree inference with weighted fusion penalties*, arXiv:1407.5915, first submitted 2014-07-22. https://arxiv.org/abs/1407.5915
