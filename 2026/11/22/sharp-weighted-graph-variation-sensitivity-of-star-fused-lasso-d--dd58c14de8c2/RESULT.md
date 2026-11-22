# Sharp weighted graph-variation sensitivity of star fused-lasso denoising

## Finding

Let \(k\ge1\) and consider a star with center \(0\) and leaves \(1,\ldots,k\). Give every vertex a strictly positive fidelity mass \(m_0,m_1,\ldots,m_k\), every edge a strictly positive regularization coefficient \(\alpha_1,\ldots,\alpha_k\), and every edge a strictly positive *measurement* variation weight \(w_1,\ldots,w_k\). Define the unique denoising map \(T_\alpha:\mathbb R^{k+1}\to\mathbb R^{k+1}\) by

\[
T_\alpha(x)=\underset{u\in\mathbb R^{k+1}}{\operatorname{argmin}}\left\{\frac12\sum_{j=0}^{k}m_j(u_j-x_j)^2+\sum_{j=1}^{k}\alpha_j|u_j-u_0|\right\}.
\]

Writing \(V_w(v)=\sum_{j=1}^{k}w_j|v_j-v_0|\), the exact global two-input Lipschitz coefficient in the quotient-by-constants seminorm is

\[
\boxed{\mathcal K(m,w,\alpha)=\sup_{V_w(x-y)>0}\frac{V_w(T_\alpha(x)-T_\alpha(y))}{V_w(x-y)}=\max\left\{1,\ \max_{1\le i\le k}\frac{m_i}{m_0+m_i}\frac{\sum_{j\ne i}w_j}{w_i}\right\}.}
\]

The supremum is attained by a pair of distinct inputs in an open, fixed active-face region (not merely approached as a limit). Crucially, it is **independent of every positive regularization coefficient** \(\alpha_i\), even though the denoising map depends on them. It is nonexpansive in \(V_w\) if and only if

\[
m_i\sum_{j\ne i}w_j\le(m_0+m_i)w_i\qquad (1\le i\le k).
\]

For equal vertex masses and equal measurement variation weights, \(\mathcal K=\max\{1,(k-1)/2\}\): an unweighted star is two-input variation-nonexpansive precisely up to three leaves, and is expansive from four leaves onward. If the vertex masses are equal and \(k\ge4\), **no positive choice** of measurement edge weights can restore nonexpansivity. For unit leaf masses and unit variation weights but arbitrary hub mass \(m_0>0\), the exact factor is \(\max\{1,(k-1)/(m_0+1)\}\), so nonexpansivity is equivalent to \(m_0\ge k-2\) when \(k\ge3\).

## Assumptions and scope

All vectors and coefficients are real and finite-dimensional. Every \(m_j\), \(w_j\), and \(\alpha_j\) is strictly positive. The star has exactly \(k\) leaves, and the objective is weighted quadratic fidelity plus *anisotropic* graph edge total variation. The measuring seminorm \(V_w\) may differ from the regularizer \(\sum\alpha_i|u_i-u_0|\); when \(w=\alpha\), the same sharp formula applies. All comparisons are between two potentially different input signals at the **same** regularization parameters. Zero measurement seminorm corresponds exactly to constant vectors; \(T_\alpha\) commutes with adding constants.

## Proof

**1. Open-face affine differentials.** For \(u=T_\alpha(x)\), the strictly convex objective has unique solution. For each leaf \(j\), choose a subgradient \(p_j\in\alpha_j\partial|u_j-u_0|\). The optimality equations are

\[
m_0(u_0-x_0)=\sum_{j=1}^k p_j,\qquad m_j(u_j-x_j)=-p_j\quad(1\le j\le k).
\]

A fixed open active face consists of the fused leaf set \(S=\{j:u_j=u_0\}\), strict inequalities \(|p_i|<\alpha_i\) on \(S\), and nonzero differences of fixed signs on \(S^c\). Put \(M_S=m_0+\sum_{i\in S}m_i\). On that region the map is affine: all fused output values equal a center \(c\), while each unfused output differs from its input by a fixed constant. Differentiating in a direction \(h\) gives

\[
\delta c=\frac{m_0h_0+\sum_{i\in S}m_i h_i}{M_S},\qquad\delta u_i=\delta c\ (i\in S),\qquad\delta u_j=h_j\ (j\notin S).
\]

Put \(d_i=h_i-h_0\). The input seminorm becomes \(\sum_i w_i|d_i|\), and the output edge differences are zero on \(S\), and on \(S^c\) equal

\[
d_j-\frac{\sum_{i\in S}m_i d_i}{M_S}.
\]

The exact induced weighted \(\ell_1\) matrix norm is its largest weighted column sum:

\[
\|DT_\alpha|_S\|_{V_w\to V_w}=
\max\left\{\mathbf{1}_{S^c\ne\varnothing},\ \max_{i\in S}\frac{m_i}{M_S}\frac{\sum_{j\notin S}w_j}{w_i}\right\}
\]

(with empty maxima interpreted as zero). Every open active face is realized: prescribe output \(u_0=u_i=0\) for \(i\in S\) and \(u_j=1\) for \(j\notin S\), prescribe \(p_i=0\) for \(i\in S\) and \(p_j=\alpha_j\) for \(j\notin S\), and set \(x_0=-\sum_jp_j/m_0\) and \(x_j=u_j+p_j/m_j\). These satisfy all optimality equations with strict complementarity on fused edges and strict positive output gaps on unfused edges, hence define an open affine region.

**2. Exact optimization over faces.** For each \(i\in S\), positivity implies

\[
\frac{m_i}{M_S}\frac{\sum_{j\notin S}w_j}{w_i}
\le \frac{m_i}{m_0+m_i}\frac{\sum_{j\ne i}w_j}{w_i}.
\]

The right side is realized by the singleton fused set \(S=\{i\}\). The unfused face \(S=\varnothing\) is the identity derivative and has norm one. Thus the largest local matrix norm equals the displayed \(\mathcal K\).

**3. Global upper bound and attainment.** As a proximal map for a finite polyhedral convex function with positive quadratic fidelity, \(T_\alpha\) is continuous and piecewise affine on finitely many polyhedra. On any line segment between inputs, the output difference is the integral (equivalently, a finite sum) of the corresponding affine differentials applied to the fixed input difference. Subadditivity and the local face bound therefore yield \(V_w(T_\alpha(x)-T_\alpha(y))\le\mathcal K V_w(x-y)\), even across face boundaries. Translation equivariance covers directions in the kernel of \(V_w\).

For the lower bound \(1\), select the fully unfused open region and perturb any leaf slightly. For each \(i\), realize the singleton face as in Step 1 and perturb only the \(i\)-th input leaf by sufficiently small \(\varepsilon>0\). Its fused output center shifts by \(m_i\varepsilon/(m_0+m_i)\), all other leaves remain unchanged, and the \(i\)-th leaf follows the center. The input variation difference is \(w_i\varepsilon\); the output variation difference is \((\sum_{j\ne i}w_j)m_i\varepsilon/(m_0+m_i)\). Thus every candidate term is actually attained, proving the formula and the asserted equality cases.

**4. Consequences.** Evaluating the minimizing objective at the competitor \(u=x\) gives \(\sum_ilpha_i|T_lpha(x)_i-T_lpha(x)_0|\le\sum_ilpha_i|x_i-x_0|\), so each individual input decreases its own regularizing variation, despite possible expansion of two-input differences. Nonexpansivity is equivalent to every singleton-face ratio being at most one. Under equal masses this reads \(\sum_{j\ne i}w_j\le2w_i\), or \(w_i\ge(\sum_jw_j)/3\) for each \(i\). Summation makes this impossible at \(k\ge4\), and forces equal edge weights at \(k=3\). With all \(w_i=m_i=1\) and arbitrary \(m_0\), the coefficient simplifies to \(\max\{1,(k-1)/(m_0+1)\}\). These conditions are sharp and do not involve the positive \(\alpha_i\).

## Verification

The standalone standard-library checker `verify_star_tv.py` enumerates all \(2^k\) possible fused-leaf faces for each of 90 positive rational mass-and-weight cases at every \(1\le k\le9\), compares exact rational face norms to the closed formula, and constructs 4,050 exact KKT-certified strict-face attaining input pairs. It independently implements a scalar monotone-root solver for the star denoiser and tests 700 random real two-input inequalities. Its reported checks are:

```
EXACT_ALL_2_POWER_K_FUSED_FACES_VS_SINGLE_SPOKE_FORMULA_PASS k=1..9 cases=810
EXACT_KKT_REALIZABLE_STRICT_WITNESSES_PASS 4050
UNWEIGHTED_DEGREE_FOUR_AND_HUB_MASS_PHASE_PASS
INDEPENDENT_SCALAR_ROOT_TWO_INPUT_STRESS_PASS cases=700
ALL_STAR_GRAPH_TV_MODULUS_CHECKS_PASS
```

The finite enumerations are consistency checks, **not** a substitute for the proof for arbitrary \(k\) and positive real parameters.

## Relationship to prior work

The 2011 graph-TV conference treatment by Couprie et al. develops primal-dual proximal algorithms rather than a sharp data-pair stability factor. The 2014 analysis of partly smooth regularizers by Vaiter et al. gives a general local derivative framework for convex analysis penalties, including fused lasso, but does not compute the graph-variation norm of the global data-to-denoiser map, optimize it over star fusion patterns, or classify weighted contraction. The 2016 DFS fused-lasso work by Madrid Padilla et al. studies graph-TV denoising and statistical error rates, including tree and star settings, but its theorems compare statistical risk or variations of individual signals, not this sharp two-input nonlinear operator coefficient. An established path-only edge-proximal contraction test does not cover stars with three or more leaves. Graph-heat one-input variation contraction at a related degree threshold likewise does not establish the present two-input resolvent estimate. The stated formula specifically concerns the global Lipschitz map between *pairs* of signals and the decoupling of that map's sharp modulus from arbitrary positive regularization strengths.

## Limitations

The result is restricted to a finite star, strictly positive observation masses and edge regularization strengths, weighted quadratic fidelity, and the specified edge-variation seminorm. It does not assert analogous sharp formulas for general trees, cycles, multigraphs, vanishing regularization strengths, nonquadratic losses, or the time-dependent graph TV flow. The fixed-mass and all-positive-coefficient limits are not uniform as a penalty tends to zero: setting **all** regularization coefficients identically zero makes the denoiser the identity, with sharp coefficient one. Historical novelty is assessed against the specifically inspected sources and indexed results; unindexed equivalents may exist.

## References

1. S. Vaiter, C.-A. Deledalle, J. Fadili, G. Peyré and C. Dossal, *The Degrees of Freedom of Partly Smooth Regularizers*, initial arXiv posting 22 April 2014, https://arxiv.org/abs/1404.5557 (especially Section 4.2 on local sensitivity).
2. O. H. Madrid Padilla, J. G. Scott, J. Sharpnack and R. J. Tibshirani, *The DFS Fused Lasso: Linear-Time Denoising over General Graphs*, initial arXiv posting 11 August 2016, https://arxiv.org/abs/1608.03384 (Sections 1, 2 and 3.2).

3. C. Couprie, H. Talbot, L. Grady, J.-C. Pesquet and L. Najman, *Dual Constrained TV-based Regularization*, ICASSP conference paper (2011), https://doi.org/10.1109/ICASSP.2011.5946561 (graph-TV models and parallel proximal algorithms).
