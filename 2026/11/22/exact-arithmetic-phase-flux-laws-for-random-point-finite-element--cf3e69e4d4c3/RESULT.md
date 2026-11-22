# Exact arithmetic-phase flux laws for random-point finite-element interface assembly

## Finding

**Theorem (finite-sample law, deterministic comparison, and complete arithmetic limits).** Let a positive one-dimensional conductivity have finitely many fixed jumps at \(0<\theta_1<\cdots<\theta_m<1\). Assemble a standard continuous, piecewise-linear finite-element stiffness matrix on the uniform \(n\)-cell partition of \([0,1]\), using one independent uniformly random conductivity evaluation in each element, and solve the zero-source Dirichlet problem with endpoint values \(0\) and \(1\). For sufficiently large \(n\), the computed constant discrete flux has an **exact finite-sample Bernoulli reciprocal-resistance law**, given below. This law implies an exact positivity bias, asymptotically second-order bias despite first-order randomized flux fluctuations, and a complete classification of its mesh-phase-dependent normalized error laws.

If \(1,\theta_1,\ldots,\theta_m\) are linearly independent over \(\mathbb Q\), the scaled flux error has **no limiting distribution** when a genuine jump is present. Its entire family of weak subsequential limits is explicitly parametrized by the \(m\)-dimensional mesh phase. The Cesàro average of its probability laws nevertheless converges to a convolution of independent centered triangular distributions, with an explicit characteristic function and sharp mean-square constant. For comparison, exact integration of the same ordinary \(P_1\) stiffness matrix produces a nonnegative physical flux error of first order at generic cut locations, rather than the randomized method's second-order *mean* bias.

## Assumptions and scope

Fix \(m\ge1\) and numbers \(0=\theta_0<\theta_1<\cdots<\theta_m<\theta_{m+1}=1\). Let \(a(x)=a_j>0\) on \((\theta_j,\theta_{j+1})\), for \(0\le j\le m\); point values exactly at jumps are immaterial. Define resistivities \(r_j=a_j^{-1}\), jumps \(\Delta_j=r_{j-1}-r_j\), total resistance and physical flux
\[
T=\sum_{j=0}^{m}(\theta_{j+1}-\theta_j)r_j>0,\qquad q=T^{-1}.
\]
The exact weak solution satisfies \(-(au')'=0\) and \(u(0)=0,u(1)=1\); its flux is \(au'=q\) almost everywhere.

For each integer \(n\ge2\), partition \([0,1]\) into cells \(I_i=(i/n,(i+1)/n)\), \(0\le i<n\). Draw independent \(U_i\sim\operatorname{Unif}(I_i)\) and set \(a_i^\omega=a(U_i)\). Define the ordinary continuous, piecewise-linear Dirichlet finite-element function \(u_n^\omega\) by
\[
\sum_{i=0}^{n-1}\frac{a_i^\omega}{n}\,(u_n^\omega)'\big|_{I_i}\,v_n'\big|_{I_i}=0
\]
for all piecewise-linear \(v_n\) with zero boundary traces. Equivalently, each element stiffness is \(n a_i^\omega\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\). In the first displayed variational sum, derivatives are constants; the term equals \(\frac1n a_i^\omega u'|_{I_i}v'|_{I_i}\). The discrete flux \(\widehat q_n=a_i^\omega(u_n^\omega)'|_{I_i}\) is independent of \(i\). The comparison \(q_n^{\mathrm{FE}}\) uses the *exactly integrated* element stiffness, i.e. replaces \(a_i^\omega\) with \(n\int_{I_i}a(x)\,dx\). These are distinct schemes and the error is measured against the physical flux \(q\), not against the exact-integration FE solution.

Set \(p_{j,n}=\{n\theta_j\}\in[0,1)\). Choose \(n\) sufficiently large that no mesh cell contains more than one jump. For every such \(n\), the variables \(B_{j,n}\) are independent and satisfy \(\Pr(B_{j,n}=1)=p_{j,n}\), where \(B_{j,n}=1\) denotes that the random quadrature point in the cut cell lies left of jump \(j\). For \(p_{j,n}=0\), set \(B_{j,n}=0\) deterministically. Define
\[
S_n=\sum_{j=1}^{m}\Delta_j(B_{j,n}-p_{j,n}),\quad V_n=\sum_{j=1}^{m}\Delta_j^2p_{j,n}(1-p_{j,n}).
\]

## Proof

**1. Exact resistance law and physical-flux error.** The assembled interior stiffness equations imply that \(a_i^\omega n(u_{i+1}-u_i)\) is independent of \(i\). Summing \(u_{i+1}-u_i=\widehat q_n/(n a_i^\omega)\) over the cells and imposing the total boundary difference \(1\) gives
\[
\widehat q_n^{-1}=\frac1n\sum_{i=0}^{n-1}(a_i^\omega)^{-1}.
\]
On a cell cut at fraction \(p\) by a single jump between resistivities \(r_{j-1}\) and \(r_j\), its exact resistance contribution is \(n^{-1}[p r_{j-1}+(1-p)r_j]\), while the sampled contribution is \(n^{-1}[B r_{j-1}+(1-B)r_j]\). Their difference is \(n^{-1}\Delta_j(B-p)\). Uncut cells contribute exactly. Since disjoint cut cells use independent samples,
\[
\boxed{\widehat q_n^{-1}=T+\frac{S_n}{n},\qquad n(\widehat q_n-q)=-\frac{q^2S_n}{1+qS_n/n}.}\tag{1}
\]
The denominator is strictly positive, since each sampled conductivity and resistivity is positive. Every element stiffness entry is unbiased, because \(\mathbb E[a(U_i)]=n\int_{I_i}a(x)\,dx\).

**2. Exact bias direction and sharp fixed-phase expansions.** The centered independent Bernoulli variables satisfy \(\mathbb ES_n=0\), \(\mathbb ES_n^2=V_n\), and \(|S_n|\le D:=\sum_j|\Delta_j|\). Jensen's strict convexity of \(x\mapsto 1/x\) on positive resistances implies
\[
\mathbb E\widehat q_n\ge q,
\]
with equality precisely when \(S_n\) is deterministic, equivalently \(V_n=0\). For \(n\) large, expand the exact reciprocal in (1); the remainder bounds depend only on the fixed positive conductivities and jumps, uniformly in all mesh phases:
\[
\boxed{\mathbb E\widehat q_n-q=\frac{q^3V_n}{n^2}+O(n^{-3}),\qquad n^2\mathbb E(\widehat q_n-q)^2=q^4V_n+O(n^{-1}).}\tag{2}
\]
Thus the mean flux error is second order even though individual flux errors are generally first order. The constants in the big-O bounds are independent of \(n\).

**3. Deterministically integrated Galerkin comparison.** In a cut cell, exact stiffness integration replaces conductivity by its arithmetic cell average \(\bar a_j(p)=p a_{j-1}+(1-p)a_j\). Define the nonnegative defect
\[
\gamma_j(p)=\frac{p}{a_{j-1}}+\frac{1-p}{a_j}-\frac{1}{p a_{j-1}+(1-p)a_j}
=\frac{p(1-p)(a_{j-1}-a_j)^2}{a_{j-1}a_j[p a_{j-1}+(1-p)a_j]}
\]
and \(G_n=\sum_{j=1}^{m}\gamma_j(p_{j,n})\). Repeating the cell-resistance argument with exact element conductivities gives
\[
\boxed{(q_n^{\mathrm{FE}})^{-1}=T-\frac{G_n}{n},\qquad n(q_n^{\mathrm{FE}}-q)=\frac{q^2G_n}{1-qG_n/n}\ge0.}\tag{3}
\]
This positive first-order error is generally nonzero at a cut with nontrivial contrast. Equation (3) concerns the flux, not an assertion about all norms of the FE solution. In particular, it does not establish mean-square superiority of the random method.

**4. All weak subsequential laws.** Now assume \(1,\theta_1,\ldots,\theta_m\) are linearly independent over \(\mathbb Q\). For \(p=(p_1,\ldots,p_m)\in[0,1]^m\), let independent \(B_j(p)\sim\operatorname{Bernoulli}(p_j)\), with degenerate endpoint laws, and set
\[
\mu_p=\mathcal L\left(-q^2\sum_{j=1}^{m}\Delta_j(B_j(p)-p_j)\right).
\]
By Kronecker's density theorem, every \(p\) is a limit of some sequence of mesh-phase vectors \((\{n\theta_1\},\ldots,\{n\theta_m\})\). Continuity of finite Bernoulli product laws in \(p\), the boundedness of \(S_n\), and (1) show that the associated scaled flux-error laws converge weakly to \(\mu_p\). Conversely, every convergent sequence of these laws has a further subsequence with convergent phase vector by compactness of \([0,1]^m\), so its limit must equal one of the \(\mu_p\). Hence the full set of weak subsequential limits is **exactly** \(\{\mu_p:p\in[0,1]^m\}\). If at least one \(\Delta_j\ne0\), the family contains both the point mass \(\delta_0=\mu_0\) and a nondegenerate distribution \(\mu_{(1/2,\ldots,1/2)}\); the original full sequence has no weak limit.

**5. The Cesàro law and its moments.** Weyl equidistribution strengthens density to uniform averaging of bounded continuous phase functions. Therefore, for every bounded continuous \(g:\mathbb R\to\mathbb R\), using (1) and uniform \(O(n^{-1})\) control of its normalization,
\[
\lim_{N\to\infty}\frac1N\sum_{n=1}^N\mathbb E\left[g\big(n(\widehat q_n-q)\big)\right]
=\int_{[0,1]^m}\int g(y)\,d\mu_p(y)\,dp.
\]
Let \(P_j\sim\operatorname{Unif}[0,1]\), independently; conditional on \(P_j\), let \(B_j\sim\operatorname{Bernoulli}(P_j)\). A change of variables shows \(Z_j=B_j-P_j\) has triangular density \((1-|z|)\mathbf1_{\{|z|\le1\}}\), and the \(Z_j\) are independent. The Cesàro limit law is thus \(\mathcal L(-q^2\sum_j\Delta_jZ_j)\), with characteristic function
\[
\boxed{\varphi(t)=\prod_{j=1}^{m}\left[\frac{\sin(q^2\Delta_jt/2)}{q^2\Delta_jt/2}\right]^2,\qquad\frac{\sin0}{0}:=1.}\tag{4}
\]
Since \(\mathbb EZ_j=0\) and \(\mathbb EZ_j^2=1/6\), the limiting variance is \(q^4\sum_j\Delta_j^2/6\). Averaging the uniform expansions (2) gives, explicitly,
\[
\lim_{N\to\infty}\frac1N\sum_{n=1}^{N}n^2\mathbb E(\widehat q_n-q)^2=\frac{q^4}{6}\sum_j\Delta_j^2,
\]
\[
\lim_{N\to\infty}\frac1N\sum_{n=1}^{N}n^2(\mathbb E\widehat q_n-q)=\frac{q^3}{6}\sum_j\Delta_j^2.
\]
The argument requires no probabilistic coupling between different mesh sizes; the limits concern the laws at each size and their Cesàro averages.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 standard library. The standalone script reconstructs an exactly assembled rational-coefficient tridiagonal FEM linear system, tests (1) against direct exact-arithmetic Gaussian elimination on eight mesh sizes and every admissible two-interface sampling outcome, checks the exact reciprocal-bias identity for one interface, checks (3) with exactly integrated element conductivities, evaluates triangular moments, and compares Cesàro risk and bias with their exact limit constants for a two-interface example with irrational, rationally independent locations. At package review it returned \(\texttt{VERIFY\_OK 136}\); the finite checks corroborate the formulas but do not prove the universal Kronecker–Weyl assertions, which are justified analytically above. The script is part of this package.

## Relationship to prior work

The motivating 2026 work of Yang and Zhai studies accurate geometry-aware immersed finite elements for elliptic interface problems; it does not propose the random-point \(P_1\) assembly studied here. Kruse, Polydorides and Wu (publicly available already in August 2019; journal version in 2026) develop randomized quadrature assembly for elliptic FEM and establish general error estimates, with an explicit randomized stiffness bilinear form in their Section 3.2. That is prior art for the **method**, not an invention claimed here. The present exact 1D reciprocal-resistance distribution and its arithmetic subsequential/Cesàro limits go beyond those reported estimates and 2D examples. Published numerical-quadrature phase laws for indicator functions and Bernoulli jump-phase laws for Euler grids concern different objects and do not immediately imply the exact randomly assembled elliptic flux law. The priority comparison is not a proof of global historical uniqueness.

## Limitations

This is an exact, special-model theorem for finitely many fixed positive one-dimensional piecewise-constant layers, unit Dirichlet boundary difference, zero forcing, standard continuous \(P_1\) elements, and independent one-point uniform samples per element. For finite \(n\), the exact independent Bernoulli formula requires different jumps to occupy different elements. The full torus of limiting distributions and the uniform Cesàro formula require rational independence of \(1,\theta_1,\ldots,\theta_m\), not merely irrationality of each location. No normal limit is asserted, and the theorem does not analyze multidimensional immersed DG, higher-degree elements, variable forcing, coefficient uncertainty, or practical cost. The exact-stiffness comparison is for physical **flux**, not a general comparison in solution error norms. No independent validation or priority certification has been performed.

## References

1. Lin Yang and Qilong Zhai, *The Immersed Discontinuous Galerkin Method for Elliptic Interface Problems*, arXiv:2606.01814, first public version June 1, 2026. https://arxiv.org/abs/2606.01814
2. Raphael Kruse, Nick Polydorides and Yue Wu, *Application of Randomized Quadrature Formulas to the Finite Element Method for Elliptic Equations*, arXiv:1908.08901, first public version August 23, 2019; BIT Numerical Mathematics (2026), DOI:10.1007/s10543-026-01126-8. https://arxiv.org/abs/1908.08901
3. Kronecker density theorem and Weyl equidistribution theorem, standard results on torus rotations; only their stated rational-independence implications are used.
