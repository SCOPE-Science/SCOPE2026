# No positive Courant window for multidimensional Haar sparse-grid upwinding

## Finding

Consider the piecewise-constant, periodic, upwind sparse-grid discontinuous Galerkin forward-Euler scheme of Huang (2026). For every dimension \(d\geq2\), every total sparse level \(N\geq2\), and every nonzero velocity vector \(\boldsymbol c\in[0,\infty)^d\), **no positive time step preserves nonnegativity of every nonnegative state in the sparse space**. Indeed a single nonnegative dyadic-quadrant state produces a negative fine-cell value at every \(\Delta t>0\), including all time steps within the sharp \(L^2\)-contractive CFL interval. A strictly positive starting state can also become negative.

This is a sharp all-level classification, not merely a finite-grid counterexample. At sparse level \(N=1\), nonnegativity is preserved for all nonnegative states exactly when \(\Delta t\max_j c_j/h\leq1\); for \(d=1\), the same threshold holds at every level \(N\geq1\). At level \(N=0\), or when every transport speed is zero, the update is the identity and preserves positivity for all nonnegative steps.

## Assumptions and scope

Fix integers \(d\geq1\), \(N\geq0\), and let \(m=2^N\), \(h=m^{-1}\). All functions are periodic piecewise constants on \([0,1)^d\), identified with arrays on the \(m^d\) fine cells. Let \(V_p\) be the one-variable dyadic piecewise-constant space of level \(p\), and set \(W_0=V_0\), \(W_p=V_p\ominus V_{p-1}\) for \(p\geq1\). The standard total-level Haar sparse space is
\[
\mathcal S_N^{(d)}=\bigoplus_{\substack{\boldsymbol p\in\{0,\ldots,N\}^d\\\sum_jp_j\leq N}}\bigotimes_{j=1}^d W_{p_j}.
\]
Let \(P_N\) denote its \(L^2\)-orthogonal projection, and define periodic backward differences \((D_ju)_{\boldsymbol k}=u_{\boldsymbol k}-u_{\boldsymbol k-\boldsymbol e_j}\), indices modulo \(m\). With nonnegative constant speeds \(c_j\) and \(\Delta t\geq0\), the unmodified forward-Euler step is
\[
\mathcal G_{\Delta t}u=u-\sum_{j=1}^d r_jP_ND_ju,\qquad r_j=\frac{c_j\Delta t}{h}.
\]
Here positivity means **each fine-cell value** of \(\mathcal G_{\Delta t}u\) is nonnegative whenever the fine-cell values of \(u\in\mathcal S_N^{(d)}\) are nonnegative. It is not a statement about modal coefficients or about a nonlinear positivity limiter.

## Proof

**Failure at every level \(N\geq2\) in every \(d\geq2\).** Select a coordinate \(i\) with \(c_i>0\), and any distinct coordinate \(j\). Write \(f(k)=1\) on fine indices \(0\leq k<m/2\) and \(f(k)=0\) otherwise, and let \(u(\boldsymbol k)=f(k_i)f(k_j)\), independent of other coordinates. Since \(f\in V_1=W_0\oplus W_1\), we have \(u\in V_1\otimes V_1\otimes W_0^{\otimes(d-2)}\subseteq\mathcal S_N^{(d)}\).

Let \(s=2f-1\), so \(s\in W_1\) and \(f=(1+s)/2\). The directional sparse projection has the **exact** tensor formula
\[
P_ND_iu=\frac12(D_Nf)(k_i)+\frac12(P_{V_{N-1}}D_Nf)(k_i)s(k_j),
\]
where \(D_Nf(k)=f(k)-f(k-1)\), and the unused coordinates have constant factor one. This holds because the transverse components belong to \(W_0\) and \(W_1\), whose retained longitudinal slices are respectively \(V_N\) and \(V_{N-1}\). The analogous formula interchanges \(i,j\); all other directional differences vanish.

Evaluate on any fine cell with \(k_i=k_j=m/2+1\) and arbitrary other indices. Since \(m\geq4\), at this cell \(f=0\), \(s=-1\), and \(D_Nf=0\). The dyadic level-\(N-1\) projection averages adjacent pairs: at index \(m/2+1\), the pair contains the negative jump \(D_Nf(m/2)=-1\), and hence \((P_{V_{N-1}}D_Nf)(m/2+1)=-1/2\). Therefore
\[
(P_ND_iu)_{\boldsymbol k}=(P_ND_ju)_{\boldsymbol k}=\frac14,
\qquad (\mathcal G_{\Delta t}u)_{\boldsymbol k}=-\frac{r_i+r_j}{4}<0.
\]
If \(c_j=0\) the last inequality still holds because \(c_i>0\). Any extra velocity coordinates contribute zero. This establishes failure even when only one direction advects. Adding a constant \(\delta>0\) to \(u\) leaves all projected differences unchanged; choosing \(0<\delta<(r_i+r_j)/4\) produces a **strictly positive** input whose output is negative. The witness works at arbitrarily small \(\Delta t>0\).

**The sharp boundary levels.** At \(N=1\), every sparse-grid state has the unique representation \(u(\boldsymbol k)=a+\sum_{j=1}^db_js_j(k_j)\), where each \(s_j\) equals \(+1\) or \(-1\) on the two cells in coordinate \(j\). Its fine-cell nonnegativity is equivalent to \(a\geq\sum_j|b_j|\). Since \(D_js_j=2s_j\), the Euler update maps \(b_j\) to \((1-2r_j)b_j\), preserving this cone for every input if and only if \(|1-2r_j|\leq1\) for each \(j\), or equivalently \(0\leq r_j\leq1\). Necessity is witnessed by \(u=1\pm s_j\).

When \(d=1\), the sparse space is the complete full-grid piecewise-constant space, and the update is the usual periodic upwind map \(u_k^+=(1-r)u_k+ru_{k-1}\); for \(N\geq1\) it preserves every nonnegative array precisely when \(0\leq r\leq1\). At \(N=0\) all directions act on constants only, so the update is the identity. If \(\boldsymbol c=0\) the same is true at every level. These cases exhaust the stated scope.

## Verification

The standalone standard-library script `verify.py` constructs the dyadic one-variable orthogonal projectors exactly with rational arithmetic and then constructs the total-level tensor projector independently of the displayed proof. It checks the quadrant certificate and exact \(1/4\) projected directional values for \((d,N)=(2,2),(2,3),(2,4),(3,2)\), including zero contributions in inactive dimensions, and checks the extreme-ray level-one boundary for dimensions one through three. Run `python3 verify.py` next to this document. The expected final line is `VERIFY_OK: independent exact rational projection and boundary certificates`.

These finite tests are **not** an exhaustive check of arbitrary dimensions or levels. The universal proof rests on the slice identity, the explicit jump average, and the exact level-one cone classification above.

## Relationship to prior work

Huang's 2026 theorem establishes the sharp \(L^2\)-contractive forward-Euler CFL condition \(\Delta t\leq h/\max_jc_j\) for \(d\geq2\), \(N\geq1\) (arXiv:2609.17312, Theorem 4.3). That result concerns a Hilbert-space norm, not order preservation. The present theorem identifies the complementary sharp positivity classification: for \(N\geq2\), **every** positive time step fails the fine-cell order condition, while the lowest nontrivial sparse level retains the usual CFL positivity bound.

Guo and Cheng's original sparse-grid DG formulation establishes \(L^2\) stability, convergence and conservation (arXiv:1602.02124); it does not provide the present all-level discrete positivity classification. Gong–Lee–Li–Yu (arXiv:2405.16117) establish positivity for a *different* locally conservative lowest-order DG method without this globally truncated sparse tensor space. Zeiser (2023) studies a different stabilized, implicit, space-time sparse Galerkin discretization. General positivity-limiting literature explains why monotonicity can require corrections, but does not supply the exact no-time-step barrier for this unmodified projected-upwind scheme.

## Limitations

The result assumes exact \(L^2\) projection, standard isotropic Haar total-level truncation, periodic dyadic meshes, piecewise constant basis functions, constant nonnegative velocities, and the *unmodified* forward-Euler endpoint step. It does not assert that all nonlinear or limited sparse-grid methods lose positivity. It does not characterize every anisotropic downward-closed index set, variable-coefficient velocity, or later-time behavior. The novelty comparison is based on the sources listed below and subject to historical-priority uncertainty from unindexed or differently phrased results.

## References

1. Juntao Huang, *The sharp CFL condition of the piecewise constant sparse grid discontinuous Galerkin method for high-dimensional transport equations*, arXiv:2609.17312, first public version September 15, 2026. https://arxiv.org/abs/2609.17312
2. Wei Guo and Yingda Cheng, *A sparse grid discontinuous Galerkin method for high-dimensional transport equations and its application to kinetic simulations*, arXiv:1602.02124, first public version February 5, 2016. https://arxiv.org/abs/1602.02124
3. Shihua Gong, Young-Ju Lee, Yukun Li, Yue Yu, *Positivity and Maximum Principle Preserving Discontinuous Galerkin Finite Element Schemes for a Coupled Flow and Transport*, arXiv:2405.16117, May 25, 2024. https://arxiv.org/abs/2405.16117
4. Andreas Zeiser, *Sparse grid time-discontinuous Galerkin method with streamline diffusion for transport equations*, Partial Differential Equations and Applications **4**, article 38 (2023). https://doi.org/10.1007/s42985-023-00250-2
