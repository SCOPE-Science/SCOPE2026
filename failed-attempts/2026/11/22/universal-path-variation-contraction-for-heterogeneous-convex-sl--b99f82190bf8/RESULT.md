# Universal path-variation contraction for heterogeneous convex slope-box regression

## Finding

Fix an integer \(n\ge 2\), real edge bounds \(\ell_e\le r_e\) for \(1\le e<n\), positive observation masses \(m_i>0\), and functions \(\phi_i:\mathbb R\to\mathbb R\) that are twice continuously differentiable and satisfy \(\phi_i'(0)=0\) and \(\phi_i''(t)>0\) for every real \(t\). Define the nonempty closed slope-box constraint set
\[
C=\{u\in\mathbb R^n:\ell_e\le u_{e+1}-u_e\le r_e\ \text{for every }1\le e<n\},
\]
and the unique regression map
\[
T(x)=\operatorname*{argmin}_{u\in C}\sum_{i=1}^{n}m_i\phi_i(u_i-x_i).
\]
For adjacent total variation \(V(h)=\sum_{e=1}^{n-1}|h_{e+1}-h_e|\), the **sharp, attained two-input Lipschitz coefficient** is
\[
\boxed{\sup_{V(x-y)>0}\frac{V(T(x)-T(y))}{V(x-y)}=
\begin{cases}
0,&\ell_e=r_e\ \text{for every edge},\\
1,&\ell_e<r_e\ \text{for at least one edge}.
\end{cases}}
\]
In particular, \(V(T(x)-T(y))\le V(x-y)\) for all real inputs \(x,y\), with no uniformity assumptions on the masses, losses or slope bounds. The conclusion extends to the heterogeneous, potentially nonsmooth-curvature power-loss family \(\phi_i(t)=|t|^{p_i}\) for **arbitrary independent exponents** \(1<p_i<\infty\).

## Assumptions and scope

All vectors and coordinates are real; all bounds are finite and may be positive, zero or negative, with arbitrary prescribed edge-specific lower and upper values. Singleton intervals are allowed. The observation losses are applied to residuals \(u_i-x_i\), so changing all inputs by the same constant changes all fitted values by that constant. Strictly positive second derivatives guarantee unique block minimizers and their differentiability; in the power-loss corollary, strict convexity and approximation replace this regularity. The assertion is a **two-input** estimate for the first-difference \(\ell_1\) seminorm, not a nonexpansivity claim for Euclidean, \(\ell_p\), graph-edge weighted, or first-difference \(\ell_2\) norms.

Because each \(\phi_i'\) is strictly increasing with \(\phi_i'(0)=0\), every \(\phi_i\) grows at least linearly outside any fixed neighborhood of zero. Thus the objective is coercive; \(C\) is nonempty by choosing one permitted increment per edge, so the unique minimizer exists. The slope constraints couple **only consecutive positions** on an open path.

## Proof

**1. Finite collection of unconstrained block minimizer maps.** For any input \(x\), let \(u=T(x)\). Mark each edge on which its fitted increment hits an endpoint of the admissible interval; for an edge with a singleton interval, mark that endpoint. Connected runs of marked edges partition the path into consecutive vertex blocks \(B\). On each block the marked equalities prescribe differences, so every fitted coordinate can be written \(u_i=c_B+d_i\), where offsets \(d_i\) depend only on the marked edge choices and not on \(x\). Edges separating blocks have strict slack, so changing \(c_B\) by a sufficiently small positive or negative amount while holding other block constants fixed remains feasible. First-order optimality therefore forces
\[
\sum_{i\in B}m_i\phi_i'(c_B+d_i-x_i)=0.\tag{1}
\]
The left side is continuous, strictly increasing from negative to positive, so (1) determines a unique scalar. For any abstract pattern of marked lower, marked upper, or unmarked edges, define \(F_{\mathcal B}(x)\) to be the vector obtained by solving (1) independently on each resulting block, whether or not the pattern is the active one for that input. There are at most \(3^{n-1}\) such smooth global maps. By the preceding optimality argument, **at every input** \(T(x)\) agrees with one of them.

**2. Derivative of each block map.** Fix any such pattern and a block \(B\). Implicit differentiation of (1) in direction \(h\) yields
\[
D c_B(x)[h]=\sum_{i\in B}\alpha_i(x)h_i,\qquad
\alpha_i(x)=\frac{m_i\phi_i''(c_B+d_i-x_i)}{\sum_{j\in B}m_j\phi_j''(c_B+d_j-x_j)}.
\]
Every coefficient is strictly positive and \(\sum_{i\in B}\alpha_i=1\). All output derivative coordinates in \(B\) equal \(D c_B(x)[h]\). Thus the derivative is a positive, row-stochastic **averaging separately over consecutive blocks**. Offsets \(d_i\), fixed slopes and heterogeneous curvatures do not change this structure.

**3. A sharp variation lemma for consecutive-block averaging.** Let \(A\) send any real input to its positive-weighted mean on each block of an arbitrary consecutive partition; the weights within each block may differ. For a fixed edge \(e\), define the one-jump vector \(s^{(e)}\) by \(s_i^{(e)}=0\) for \(i\le e\), and \(s_i^{(e)}=1\) for \(i>e\). Then \(A s^{(e)}\) is a nondecreasing vector with every entry in \([0,1]\): blocks wholly left or right of the jump retain zero or one, while the only possible crossing block has an intermediate positive-weighted mean. Consequently
\[
V(A s^{(e)})\le 1.
\]
Every \(h\in\mathbb R^n\) decomposes exactly into \(h_1\mathbf 1+\sum_{e=1}^{n-1}(h_{e+1}-h_e)s^{(e)}\). As \(A\mathbf1=\mathbf1\), linearity and the variation triangle inequality give
\[
V(Ah)\le\sum_{e=1}^{n-1}|h_{e+1}-h_e|V(As^{(e)})\le V(h).\tag{2}
\]
Applying (2) to \(DF_{\mathcal B}(x)\) and integrating the derivative along any segment proves \(V(F_{\mathcal B}(x)-F_{\mathcal B}(y))\le V(x-y)\) for **every** block pattern and all \(x,y\).

**4. Pass from finitely many branches to the actual regression.** First, \(T\) is continuous: when \(x^{(k)}\to x\), the minimizers stay bounded by coercivity and comparison with a fixed feasible point; every convergent subsequence solves the limiting strictly convex problem, hence has limit \(T(x)\). Now consider a segment \(x(t)=x+t(y-x)\). At any fixed \(t_0\), discard the finitely many branch maps with \(F_{\mathcal B}(x(t_0))\ne T(x(t_0))\). Continuity and finiteness ensure that no discarded branch can equal \(T(x(t))\) in a sufficiently small neighborhood of \(t_0\). Hence, for all nearby \(t\), some branch that agrees with \(T\) at \(t_0\) also represents \(T\) at \(t\). Its inequality from step 3 gives
\[
V(T(x(t))-T(x(t_0)))\le |t-t_0|V(y-x).
\]
For any fixed \(a\in[0,1]\), the scalar continuous function \(g(t)=V(T(x(t))-T(x(a)))\) has upper right Dini derivative no greater than \(V(y-x)\), because its increments are bounded by the preceding local estimate and the reverse triangle inequality. The elementary Dini mean-value bound therefore gives \(g(b)-g(a)\le(b-a)V(y-x)\) for \(a\le b\); taking \(a=0\), \(b=1\) proves the global estimate. This argument does not assume differentiability of \(T\) at active-set boundaries.

**5. Sharpness, including degenerate slope boxes.** If every edge interval is a singleton, all feasible vectors have prescribed adjacent differences, so any two outputs differ only by a constant and their variation difference is zero. Otherwise choose a feasible vector \(u\) whose increment lies **strictly inside** every non-singleton interval and equals its prescribed value on fixed edges (choose independently on each edge). Fix an edge \(e\) of positive permitted width and take \(h=s^{(e)}\). For sufficiently small \(\varepsilon>0\), both \(u\) and \(u+\varepsilon h\) are feasible. Because each loss uniquely minimizes its residual at zero, \(T(u)=u\) and \(T(u+\varepsilon h)=u+\varepsilon h\). Their variation ratio equals one. Thus both alternatives in the coefficient formula are attained by actual finite input pairs.

**6. Independent power exponents.** For each \(p_i>1\), replace \(|t|^{p_i}\) by the smooth loss
\[
\phi_{i,\delta}(t)=(t^2+\delta^2)^{p_i/2}-\delta^{p_i},\qquad \delta>0.
\]
Its second derivative is \(p_i(t^2+\delta^2)^{p_i/2-2}\big(\delta^2+(p_i-1)t^2\big)>0\), and its derivative vanishes at zero. The theorem applies to these smooth losses for every \(\delta>0\). As \(\delta\downarrow0\), the objectives converge uniformly on bounded sets to the strictly convex, coercive mixed-power objective. Their unique minimizers stay bounded and converge to its unique minimizer by the minimizing comparison principle. Passing to the limit in the variation inequality proves the stated mixed-power extension. The same feasible-input witness establishes the same sharp coefficient. \(\square\)

## Verification

The standalone Python standard-library checker `verify.py` independently verifies the core positive-block-averaging lemma using exact rational arithmetic over \(32{,}274\) block/weight/step cases. A separate small-dimensional constrained-regression enumerator evaluates arbitrary finite lower/upper slope boxes, including fixed edges, heterogeneous positive masses and independently selected power-loss exponents. It tests \(180\) random two-input pairs and both sharpness cases. Its observed report is:

```text
EXACT_CONSECUTIVE_BLOCK_STEP_NORMS_PASS 32274
HETEROGENEOUS_POWER_SLOPE_BOX_PAIRS_PASS 180
SHARP_ONE_VERSUS_ZERO_DICHOTOMY_PASS
ALL_SLOPE_BOX_BV_CHECKS_PASS
```

Run `python verify.py` after extracting it beside this document. The numerical root finder and finite enumerations are diagnostic only: the universal assertion depends on steps 1–6 of the proof, not on exhaustion of an infinite parameter space.

## Relationship to prior work

Yeganova and Wilbur (2009) introduce Lipschitz-constrained isotonic least-squares regression and an LPAV algorithm for consecutive slope bounds. Agarwal, Phillips and Sadri (2009) treat Lipschitz/isotonic **quadratic** regression on paths and trees, principally developing algorithms. Neither derives nonlinear heterogeneous-loss sensitivity in the adjacent-variation seminorm.

Luss and Rosset (2011) develop generalized isotonic regression for separable convex losses, with recursive partitioning and examples including robust and power losses. Their constraints are order inequalities; the stated theorems concern optimization and algorithmic properties, not the exact two-input variation coefficient or arbitrary two-sided slope intervals. Their general convex-loss formulation supplies important prior context but does not, by itself, imply variation contraction.

Yang and Barber (2017) characterize contraction seminorms for the **Euclidean** isotonic least-squares projector via a neighbor-averaging condition. The ordinary unweighted quadratic isotonic subcase here is already covered by that framework, and it is **not** claimed as novel. Likewise, published sharp weighted least-squares isotonic variation results supply the quadratic path case, and published bounded-slope isotonic results use a first-difference quadratic seminorm that has larger Lipschitz constants. Those distinctions do not provide a nonlinear data-dependent block-averaging argument for independent nonquadratic losses, mixed exponents and arbitrary lower/upper slope bounds. The new contribution is the loss-insensitive exact two-input law for this jointly generalized class.

## Limitations

The theorem requires a finite open chain, separable **translation-invariant** residual losses, positive observation weights, and strictly convex losses; no conclusion is asserted for nonunique minimizers or nonsmooth non-strict losses. A different loss involving absolute fitted values, nonseparable penalties, weighted graph-edge variation, or branching graphs may behave differently. The p-power corollary covers exponents strictly greater than one only. The result is a seminorm statement on differences of **two fitted signals**, not a guarantee about statistical risk. Indexed literature searches and full-text comparisons cannot eliminate historical priority risks from unindexed or differently stated results. No independent audit has been performed.

## References

1. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, *Journal of Optimization Theory and Applications* **141** (2009), 429–443, first publicly available online 2009-01-07. DOI: 10.1007/s10957-008-9477-0; https://pmc.ncbi.nlm.nih.gov/articles/PMC5815842/ .
2. P. K. Agarwal, J. M. Phillips, and B. Sadri, *Lipschitz Unimodal and Isotonic Regression on Paths and Trees*, arXiv:0912.5182, first posted 2009-12-28; https://arxiv.org/abs/0912.5182 .
3. R. Luss and S. Rosset, *Generalized Isotonic Regression*, arXiv:1104.1779, first posted 2011-04-10; https://arxiv.org/abs/1104.1779 .
4. R. Kyng, A. Rao, and S. Sachdeva, *Fast, Provable Algorithms for Isotonic Regression in all \(\ell_p\)-norms*, arXiv:1507.00710, first posted 2015-07-02; https://arxiv.org/abs/1507.00710 .
5. F. Yang and R. Foygel Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852, first posted 2017-06-06; https://arxiv.org/abs/1706.01852 .
