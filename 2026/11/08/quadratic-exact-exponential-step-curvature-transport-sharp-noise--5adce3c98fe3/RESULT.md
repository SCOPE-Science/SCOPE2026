# Quadratic-exact exponential-step curvature transport: sharp noise kernels and a comparison of two unbiased estimators

## Finding

Let \(S\) be exponential with mean \(\eta>0\), let \(U\) be independent uniform on \([0,1]\), and let \(h:[0,\infty)\to\mathcal H\) be continuously differentiable into a real Hilbert space. Define the actual path increment and two estimators by
\[
D=\int_0^S h(t)\,dt,\qquad
C=\eta h(S)+(S-\eta)h(0),\qquad
Q=S h(US).
\]
Assume \(\sup_{t\ge0}\|h'(t)\|\le L<\infty\). Both estimators are unbiased for the *mean* path increment, and they are exactly equal to \(D\) for every constant \(h\) (equivalently, for quadratic objectives along a fixed search direction). Their exact mean-square path errors are
\[
\mathbb E\|C-D\|^2=\eta^2\int_0^\infty\!\int_0^\infty e^{-\max(u,v)/\eta}\langle h'(u),h'(v)\rangle\,du\,dv,
\tag{1}
\]
\[
\mathbb E\|Q-D\|^2=\eta\int_0^\infty\!\int_0^\infty \min(u,v)e^{-\max(u,v)/\eta}\langle h'(u),h'(v)\rangle\,du\,dv.
\tag{2}
\]
Consequently, for both methods,
\[
\sup_{\|h'\|_\infty\le L}\mathbb E\|\mathrm{estimator}-D\|^2=2L^2\eta^4,
\tag{3}
\]
and the bound is attained by each affine \(h(t)=a+tLv\) with \(\|v\|=1\). Their risks have **no uniform ordering**: \(C\) has strictly larger mean-square path error if a nonzero scalar derivative \(h'\ge0\) is supported inside \((0,\eta)\), but strictly smaller error if it is supported inside \((\eta,\infty)\). Smooth compactly supported derivatives suffice.

Among all scalar-weighted two-endpoint rules \(a(S)h(S)+b(S)h(0)\) that are unbiased for the mean increment for every smooth \(h\) and exactly recover the path increment for every constant \(h\), \(C\) is unique up to almost-sure equality. The one-endpoint exponential Stein estimator \(\eta h(S)\), in contrast, has mean-square path error \(\eta^2\|h(0)\|^2\) for constant \(h\).

## Assumptions and scope

The mean \(\eta\) is strictly positive. The Hilbert space is real (finite or infinite dimensional), \(h\) is continuously differentiable, and its derivative is bounded by \(L\). This ensures all displayed expectations and kernel integrals converge absolutely. A locally absolutely continuous \(h\) with an essentially bounded derivative also suffices. Randomization is only over \(S\) and, for \(Q\), \(U\); no stochastic-oracle noise is included.

For optimization, take \(h(t)=\nabla^2 f(x+td)d\) for a fixed search direction \(d\). Then \(D=\nabla f(x+Sd)-\nabla f(x)\). If the Hessian of \(f\) is \(\rho\)-Lipschitz in operator norm, then \(L\le\rho\|d\|^2\). In this case \(C\) uses Hessian-vector products at the two endpoints \(x\) and \(x+Sd\), while \(Q\) uses one Hessian-vector product at an auxiliary point \(x+USd\). These are different oracle-cost and evaluation-location choices.

## Proof

**Unbiasedness.** The exponential survival function is \(\Pr(S>t)=e^{-t/\eta}\); Fubini gives
\[
\mathbb ED=\int_0^\infty h(t)e^{-t/\eta}\,dt=\eta\mathbb Eh(S).
\]
Since \(\mathbb E(S-\eta)=0\), \(\mathbb EC=\mathbb ED\). Conditional on \(S=s\), uniformity gives \(\mathbb E[Q\mid S=s]=\int_0^s h(t)\,dt\), hence \(\mathbb EQ=\mathbb ED\). For constant \(h\equiv a\), both \(C=Q=Sa=D\) pointwise.

**Kernel for \(C\).** Writing \(v(t)=h'(t)\) and applying the fundamental theorem of calculus twice yields
\[
C-D=\int_0^S(\eta-S+t)v(t)\,dt.
\]
For \(u,v\ge0\), put \(M=\max(u,v)\) and \(m=\min(u,v)\). The memoryless exponential law gives \(S\mid\{S\ge M\}\stackrel d=M+E\) with \(E\) exponential of mean \(\eta\). Thus
\[
\mathbb E[(\eta-S+u)(\eta-S+v)\mathbf1_{S\ge M}]
=e^{-M/\eta}\mathbb E[(\eta-E)(\eta-E-(M-m))]
=\eta^2e^{-M/\eta},
\]
because \(\mathbb E(\eta-E)=0\) and \(\mathbb E(\eta-E)^2=\eta^2\). Fubini gives (1). The absolute-integrability bound is \(L^2\eta^2\int\!\int e^{-\max(u,v)/\eta}\,du\,dv=2L^2\eta^4\).

**Kernel for \(Q\).** Again put \(v=h'\). Conditional on \(S=s\),
\[
Q-D=\int_0^s\bigl(s\mathbf1_{\{Us\ge t\}}-(s-t)\bigr)v(t)\,dt.
\]
For \(s\ge M\), the covariance of the two centered indicator weights is \(s\min(u,v)-uv\). Taking the expectation in \(S\) and using \(\mathbb E[S\mathbf1_{\{S\ge M\}}]=(M+\eta)e^{-M/\eta}\) yields
\[
\mathbb E[(S\min(u,v)-uv)\mathbf1_{S\ge M}]
=\eta\min(u,v)e^{-M/\eta},
\]
which proves (2).

**Sharp bounds and variance reversal.** Since \(\langle v(u),v(v)\rangle\le L^2\), each kernel is nonnegative pointwise, and
\[
\eta^2\int_0^\infty\!\int_0^\infty e^{-\max(u,v)/\eta}\,du\,dv
=\eta\int_0^\infty\!\int_0^\infty\min(u,v)e^{-\max(u,v)/\eta}\,du\,dv
=2\eta^4.
\]
For \(v(t)=Lv_0\), \(\|v_0\|=1\), both inequalities are equalities. Subtraction of (2) from (1) gives the exact signed comparison
\[
\mathbb E\|C-D\|^2-\mathbb E\|Q-D\|^2
=\eta\int_0^\infty\!\int_0^\infty e^{-\max(u,v)/\eta}(\eta-\min(u,v))
\langle h'(u),h'(v)\rangle\,du\,dv.
\tag{4}
\]
For a nonzero nonnegative smooth scalar derivative supported below \(\eta\), the integrand is nonnegative and positive on a set of positive measure; a support above \(\eta\) gives the strict opposite sign. In either case one may choose a smooth primitive \(h\). The bound is still sharp if \(h\) itself must remain bounded: smoothly truncate the affine extremizers farther and farther along the ray and use dominated convergence.

**Uniqueness.** Suppose \(A=a(S)h(S)+b(S)h(0)\) has integrable random coefficients and is mean-unbiased for every smooth test \(h\). For test functions supported away from zero, equality of expectations implies \(\mathbb E[(a(S)-\eta)h(S)]=0\). Positivity of the exponential density and the fundamental lemma for test functions imply \(a(S)=\eta\) almost surely. Exactness for every constant test function then forces \(\eta+b(S)=S\) almost surely, proving the claimed uniqueness. (The argument applies componentwise in any real Hilbert space.)

## Verification

Run \(\texttt{python verify.py}\) with Python 3 and no external dependencies. The checker evaluates the two kernel integrals and the corresponding path-error moments independently, using exact fractions and the factorial moments \(\mathbb ES^k=k!\eta^k\). It checks polynomials up to degree four for five positive means and 19,525 coefficient configurations, including quadratic exactness, affine equality and nonnegative risk. This finite checker corroborates algebraic identities; the proof above establishes the infinite-dimensional and non-polynomial statements.

An explicit affine example is \(h(t)=a+Lt\) in one dimension. For the endpoint-corrected rule the error is \(L(\eta S-S^2/2)\), with mean zero and mean square \(2L^2\eta^4\). For the uniform-interior rule it is \(LS^2(U-1/2)\), with the same mean square. The uncorrected endpoint rule on constant \(h\equiv a\) has root-mean-square path error \(\eta|a|\), whereas both quadratic-exact rules have zero error.

## Relationship to prior work

The exponential integration-by-parts identity, the original single-endpoint correction \(\eta h(S)\), and the path-noise observation on a deterministic quadratic are established in *RanSOM: Second-Order Momentum with Randomized Scaling for Constrained and Unconstrained Optimization* (arXiv:2602.06824, Sections 3.1 and B.10). Randomly sampling an interior point of a fixed optimization step to estimate an integral of Hessian-vector products is established in *One Sample Stochastic Frank-Wolfe* (arXiv:1910.04322, Section 3.2). Endpoint-Hessian momentum corrections with Lipschitz-Hessian assumptions are established in *Better SGD Using Second-Order Momentum* (arXiv:2103.03265, Section 2). The present theorem does not claim these principles; it analyzes the distinct two-endpoint zero-mean control variate on the exponential path and derives exact competing risk kernels, a common sharp minimax constant, strict nonordering and a uniqueness statement for all-h unbiased quadratic-exact endpoint rules.

## Limitations

The error is measured against the realized path increment, not against an optimization objective or a downstream iterate's convergence rate. The endpoint-corrected rule needs an additional initial-point Hessian-vector product unless it is cached; it does not preserve the original algorithm's single-endpoint oracle cost. The sharp bound assumes Lipschitz curvature along the ray, unlike the source method's unbiasedness, which needs no Lipschitz Hessian. The displayed errors omit stochastic HVP sampling noise and correlations with a random search direction; extension to those settings requires further analysis. General control-variate and randomized-quadrature literature could contain a stronger formulation not identified in the inspected sources.

## References

1. *RanSOM: Second-Order Momentum with Randomized Scaling for Constrained and Unconstrained Optimization*, arXiv:2602.06824, first submitted 2026-02-06. https://arxiv.org/abs/2602.06824
2. M. Zhang, Z. Shen, A. Mokhtari, H. Hassani, A. Karbasi, *One Sample Stochastic Frank-Wolfe*, AISTATS 2020, PMLR 108, pp. 4012–4023. https://proceedings.mlr.press/v108/zhang20i.html
3. H. Tran and A. Cutkosky, *Better SGD Using Second-Order Momentum*, NeurIPS 2022. https://papers.nips.cc/paper_files/paper/2022/hash/1704fe7aaff33a54802b83a016050ab8-Abstract-Conference.html
