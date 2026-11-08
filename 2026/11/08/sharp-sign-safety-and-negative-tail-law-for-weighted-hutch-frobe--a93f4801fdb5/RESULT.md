# Sharp sign-safety and negative-tail law for weighted Hutch# Frobenius estimation

## Finding
For the nonadaptive Gaussian Frobenius-norm estimator called weighted Hutch# in Chen--Halikias--Musco--Persson (2026), there is an exact sign-safety frontier: among fixed mixture parameters \(0\leq\alpha\leq1\), only \(\alpha=0\) is nonnegative for every sketch of every matrix. For every nonzero real matrix and every \(\alpha>0\), the output is strictly negative with positive probability, even though it estimates a nonnegative squared norm.

For rank-one input and \(r\geq1\) Gaussian columns in each sketch, put \(c=(1+\alpha)/(2\alpha)\) for \(\alpha>0\), and let \(p_{r,\alpha}\) be the probability of a negative output. Then \(p_{r,\alpha}\) has an exact one-dimensional chi-square-tail integral (given below), and for every fixed \(\alpha\in(0,1]\),
\[
p_{r,\alpha}\sim\frac{\exp[-rJ(c)]}{\sqrt{2\pi r}\,(2c-1)\sqrt{4c-1}},
\qquad J(c)=2c-1-\log(2c).
\]
The variance-optimal **oracle fixed** mixture weight for rank-one input, \(\alpha_r^*=r/(r+4)\), is already determined by the variance formula in the source paper. Its previously unquantified negative-output probability satisfies
\[
p_{r,\alpha_r^*}\sim
\frac{e^{-2}}{\sqrt{6\pi r}}\exp[-r(1-\log2)],
\qquad
\frac{p_{r,\alpha_r^*}}{p_{r,1}}\longrightarrow e^{-2}.
\]
Thus variance optimization does not enforce nonnegativity, but its rank-one negative-output rate is exponentially small, with a sharp leading constant and a limiting factor \(e^{-2}\) relative to unweighted Hutch#.

## Assumptions and scope
Let \(A\in\mathbb R^{m\times n}\), let \(r\) be a positive integer, and let \(\Omega\in\mathbb R^{n\times r}\) and \(\Psi\in\mathbb R^{m\times r}\) have independent, independent-standard-normal entries. The estimator, in exact real arithmetic, is
\[
H_{r,\alpha}^{\#}(A)
=\frac{1+\alpha}{2r}\bigl(\|A\Omega\|_{\mathrm F}^2+\|\Psi^{\mathsf T}A\|_{\mathrm F}^2\bigr)
-\frac{\alpha}{r^2}\|\Psi^{\mathsf T}A\Omega\|_{\mathrm F}^2.
\]
For the asymptotic statements, \(A\) is any nonzero rank-one real matrix (its dimensions and singular value may be fixed); all limits are for integer \(r\to\infty\) with independent fresh Gaussian sketches at each \(r\). The parameter \(\alpha\in(0,1]\) is fixed except in the explicitly stated oracle-optimal sequence. Zero matrices have identically zero output. These statements do not cover the paper's data-dependent estimated mixture weight, where \(\alpha\) may depend on the same sketches.

## Proof
**1. Universal classification.** At \(\alpha=0\), both terms of \(H_{r,0}^{\#}\) are sums of squares, so the estimator is nonnegative for every realization. Let \(A\ne0\) and choose a singular triplet \(Av=\sigma u\), \(A^{\mathsf T}u=\sigma v\) with \(\sigma>0\), \(\|u\|=\|v\|=1\). Choose deterministic sketches whose first columns are \(tv\) and \(tu\), respectively, and whose other columns are zero. The output becomes
\[
\sigma^2\left(\frac{(1+\alpha)t^2}{r}-\frac{\alpha t^4}{r^2}\right),
\]
which is negative when \(t^2>r(1+\alpha)/\alpha\). Continuity gives an open neighborhood of such sketches with negative output, and the joint Gaussian law has positive density on every nonempty open set. Hence the negative-output probability is strictly positive for every \(A\ne0\), \(r\ge1\), and \(\alpha>0\). No assertion of a uniform lower bound over all matrices is made.

**2. Exact rank-one distribution.** Write \(A=\sigma uv^{\mathsf T}\), where \(\sigma>0\), \(u,v\) are unit vectors. Define
\[
X=\|v^{\mathsf T}\Omega\|_2^2/r,\qquad
Y=\|u^{\mathsf T}\Psi\|_2^2/r.
\]
Then \(X,Y\) are independent copies of \(\chi_r^2/r\), and
\[
H_{r,\alpha}^{\#}(A)/\sigma^2
=\frac{1+\alpha}{2}(X+Y)-\alpha XY.
\]
For \(\alpha>0\), its negativity is equivalent to \(XY>c(X+Y)\). Since \(X,Y>0\), this holds exactly when \(X>c\) and \(Y>cX/(X-c)\). Let
\[
f_r(x)=\frac{(r/2)^{r/2}}{\Gamma(r/2)}x^{r/2-1}e^{-rx/2}
\qquad (x>0),
\]
and let \(Q(a,z)=\Gamma(a,z)/\Gamma(a)\) be the regularized upper incomplete gamma function. Independence gives the exact finite-sample formula
\[
p_{r,\alpha}=\int_c^\infty f_r(x)\,Q\!\left(\frac r2,\frac{rcx}{2(x-c)}\right)\,dx.
\]
In particular, for \(r=2\), the integral reduces by \(x=c+u\) to \(2ce^{-2c}K_1(2c)\), where \(K_1\) denotes the modified Bessel function of the second kind. This identity is a finite-sample check, not an input to the asymptotic proof.

**3. Sharp large-deviation saddle point.** The density obeys, uniformly on compact subsets of \((0,\infty)\),
\[
f_r(x)\sim\frac{\sqrt r}{2\sqrt\pi\,x}\,e^{-rI(x)},
\qquad I(x)=\frac{x-1-\log x}{2},
\]
by Stirling's formula. Introduce \(s=x+y\) and \(d=x-y\). The negative region is exactly
\[
s>4c,\qquad |d|<\sqrt{s(s-4c)}.
\]
The two-variable rate is
\[
I(x)+I(y)=\frac{s-2-\log[(s^2-d^2)/4]}2.
\]
For fixed \(s\), it is minimized uniquely at \(d=0\); the resulting function \(s/2-1-\log(s/2)\) is strictly increasing for \(s>4c\) because \(c\ge1\). Thus the unique minimum of the rate on the closure of the negative region is the boundary point \((x,y)=(2c,2c)\), with value \(J(c)=2c-1-\log(2c)\). This also proves the stated sharp exponential rate.

To obtain the prefactor, use local coordinates \(s=4c+t/r\) and \(d=w/\sqrt r\). Then the constraint converges to \(t>w^2/(4c)\), the area Jacobian is \(dx\,dy=dt\,dw/(2r^{3/2})\), and the rate expands as
\[
r\,[I(x)+I(y)-J(c)]
=\frac{2c-1}{4c}t+\frac{w^2}{32c^2}+o(1)
\]
on compact subsets of the limiting region. The uniquely minimizing boundary point, coercivity of the rate, and the positive normal rate gradient give exponentially smaller contributions away from this shrinking neighborhood. The same bounds justify dominated convergence in the scaled local integral. The density prefactor yields
\[
\begin{aligned}
\lim_{r\to\infty}\sqrt r\,e^{rJ(c)}p_{r,\alpha}
&=\frac1{32\pi c^2}\int_{\mathbb R}
\int_{w^2/(4c)}^\infty
\exp\!\left(-\frac{2c-1}{4c}t-\frac{w^2}{32c^2}\right)dt\,dw\\
&=\frac1{\sqrt{2\pi}\,(2c-1)\sqrt{4c-1}}.
\end{aligned}
\]
This proves the sharp prefactor for every fixed \(c\ge1\). The estimates are uniform when \(c\) remains in any compact subset of \([1,\infty)\), by the same compact-coordinate bounds and a uniform positive normal gradient.

**4. Variance-optimal mixture and its sign cost.** For rank one, write \(X=1+\varepsilon\), \(Y=1+\eta\). Independence, centering and \(\operatorname{Var}(\varepsilon)=\operatorname{Var}(\eta)=2/r\) show
\[
\operatorname{Var}\!\left(H_{r,\alpha}^{\#}(A)/\sigma^2\right)
=\frac{(1-\alpha)^2}{r}+\frac{4\alpha^2}{r^2}.
\]
Its unique minimizer is \(\alpha_r^*=r/(r+4)\), in agreement with the source paper. For this weight, \(c_r=1+2/r\). Uniformity of the local saddle-point formula as \(c_r\to1\), together with
\[
rJ(c_r)=r(1-\log2)+2+o(1),
\]
gives the oracle-optimal probability formula. Taking the ratio against the \(c=1\) case gives \(e^{-2}\). None of the rank-one variance optimization itself is claimed as new.

## Verification
The standalone script `verify.py` performs 35,456 checks, including exact-rational variance minimization and sign-equivalence tests, randomized matrix-to-scalar rank-one reductions, exact negative witnesses, quadrature of the chi-square survival integral, the \(r=2\) Bessel identity, and numerical checks of the asymptotic prefactor for \(r=20,40,80\). It prints `VERIFY_OK 35456 checks` with the stated numerical dependencies. These finite checks are corroboration; the proof above supplies the all-matrix and large-\(r\) quantifiers. Run with `python verify.py` after installing NumPy and SciPy.

## Relationship to prior work
Chen, Halikias, Musco and Persson (2026), Sections 1--3, introduce the estimator and derive unbiasedness, the variance formula, and the variance-optimal mixture. Those statements are **prior work** and are used here only to identify the natural mixture and comparison. Their inspected main text, numerical section and appendix do not state the universal sign-safety dichotomy, chi-square negative-output integral, sharp negative-tail prefactor, or \(e^{-2}\) oracle-weight probability ratio. Their Chebyshev bounds concern absolute estimation error and do not imply these sharp one-sided rare-event formulas. Earlier Hutchinson and Hutch++ methods provide relevant stochastic trace-estimation baselines but not the signed-product formula for the newly defined nonadaptive estimator. A general product-gamma-distribution result not located by the searches could potentially imply part of the rank-one integral; this remains a priority risk, not a proven novelty guarantee.

## Limitations
The sharp probability asymptotic is **only for nonzero rank-one inputs** and fixed \(\alpha>0\), or for the indicated deterministic oracle sequence \(\alpha_r^*\). It does not quantify negative probability for general full-rank matrices, random estimated weights, non-Gaussian sketches, finite-precision algorithms, or effects of clipping on bias. Positive probability does not imply a frequent event: the explicit rank-one decay is exponential. No claim of independent verification, historical-priority certification or empirical efficiency improvement is made.

## References
- T. Chen, D. Halikias, C. Musco, and D. Persson, *Hutch#: Optimal non-adaptive Frobenius norm estimation*, arXiv:2609.28472, publicly submitted 2026-09-23. https://arxiv.org/abs/2609.28472
- R. A. Meyer, C. Musco, C. Musco, and D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, SOSA 2021, DOI:10.1137/1.9781611976496.16. https://pubmed.ncbi.nlm.nih.gov/34723248/
