# Convex-order monotonicity of stationary cluster mass under dispersed binary splitting

## Finding

Consider a well-mixed continuous-mass coagulation–fragmentation model with mass-independent merging and binary splitting. Let \(A\in(0,1)\) be the random fraction of a parent mass assigned to one daughter, independently at every splitting event. Define the **symmetrized daughter-fraction law** \(\nu=\tfrac12\mathcal L(A)+\tfrac12\mathcal L(1-A)\), and let \(Z\sim\nu\). The first moment is necessarily \(\mathbb E Z=1/2\). Normalize total cluster mass density to one and fragmentation rate to \(\lambda>0\).

**Theorem.** For every such \(\nu\), there exists a unique stationary cluster-mass law \(W_\nu\) of mean one and finite second moment, expressed in rescaled mass \(W=\lambda X\), where \(X\) is the mass of a cluster sampled uniformly by cluster number. For two symmetrized daughter-fraction laws \(\nu_1,\nu_2\),

\[
\nu_1\le_{\mathrm{cx}}\nu_2\quad\Longrightarrow\quad W_{\nu_1}\le_{\mathrm{cx}}W_{\nu_2}.
\]

Here \(\le_{\mathrm{cx}}\) denotes convex order: \(\mathbb E\varphi(U)\le\mathbb E\varphi(V)\) for every convex function for which both expectations exist, with equal means. Moreover, when \(\nu_1\ne\nu_2\) and \(\nu_1\le_{\mathrm{cx}}\nu_2\), the stationary Laplace transforms satisfy the strict inequality

\[
\mathbb E e^{-sW_{\nu_1}}<\mathbb E e^{-sW_{\nu_2}}\qquad(s>0).
\]

The second moment and a constructive error bound are

\[
\mathbb E W_\nu^2=\frac{2}{1-2\mathbb E Z^2}=\frac{4}{1-4\operatorname{Var}(Z)},\qquad
\mathcal W_2(\mathcal L(W_n),\mathcal L(W_\nu))
\le a_\nu^{n/2}\sqrt{\mathbb E W_\nu^2-1},
\quad a_\nu=\frac{2+2\mathbb E Z^2}{3}<1.
\]

In the last inequality, \(W_0=1\) and \(W_n\) is the \(n\)-fold distributional iteration defined below. Consequently **equal-half splitting** \(Z=1/2\) minimizes the entire stationary mass distribution in convex order among all admissible symmetric fragmentation kernels, with the sharp minimum \(\mathbb E W^2=4\). Every other daughter-fraction law gives a strictly larger stationary Laplace transform for each \(s>0\) and a strictly larger second moment.

## Assumptions and scope

We work with nonnegative finite Borel measures \(c\) on \((0,\infty)\) that obey the weak stationary mean-field equation for a constant aggregation kernel normalized as in Krapivsky's model, at fragmentation rate \(\lambda>0\). The total number density is \(\int c(dx)=\lambda\), the conserved mass density is \(\int x\,c(dx)=1\), and the normalized cluster law has finite second moment. Splitting sends a parent of mass \(x\) to daughters \(Ax\) and \((1-A)x\); \(A\) lies strictly between zero and one almost surely and is independently sampled at each event. No density, smoothness, deterministic split ratio, or positive lower bound on \(A\) is assumed. We do not assert convergence in physical time of the kinetic evolution, nor uniqueness among infinite-second-moment stationary solutions.

Stationarity in weak form means that for every bounded measurable \(g\), with \(X_1,X_2\) independent and distributed according to \(c/\lambda\),

\[
3\mathbb E g(X)=\mathbb E g(X_1+X_2)+2\mathbb E g(ZX_1).
\]

This is equivalent to the mass-independent stationary balance equation after the stated number-density normalization; it includes the deterministic and uniform split cases of the motivating paper. Under \(W=\lambda X\), this equation has the same form with \(X\) replaced by \(W\).

## Proof

**1. Distributional fixed point.** For a probability law \(\mu\) on \([0,\infty)\), define \(T_\nu\mu\) as the law of

\[
\begin{cases}
U_1+U_2,&\text{with probability }1/3,\\
ZU_1,&\text{with probability }2/3,
\end{cases}
\]

with \(U_1,U_2\) independent of each other and of \(Z\), and each distributed as \(\mu\). The weak stationary equation is exactly \(T_\nu\mu=\mu\). Since \(\mathbb E Z=1/2\), \(T_\nu\) preserves the class \(\mathcal P_2^1\) of nonnegative probability laws having mean one and finite second moment.

**2. Existence and uniqueness.** Couple \(U\sim\mu\) and \(V\sim\eta\) optimally in quadratic Wasserstein distance, independently repeat this coupling for the second summand, and use the same branch and the same \(Z\) for both outputs. Because \(\mathbb E(U-V)=0\), the cross term in the addition branch vanishes. Thus

\[
\mathcal W_2^2(T_\nu\mu,T_\nu\eta)
\le\frac{2+2\mathbb E Z^2}{3}\,\mathcal W_2^2(\mu,\eta)
=a_\nu\mathcal W_2^2(\mu,\eta).
\]

Since \(0<Z<1\) almost surely and \(\mathbb E Z=1/2\), we have \(\mathbb E Z^2<1/2\) and hence \(a_\nu<1\). The nonempty set \(\mathcal P_2^1\) is complete in \(\mathcal W_2\), so Banach's fixed-point theorem supplies a unique fixed point \(\mu_\nu\), and the iterations \(\mu_n=T_\nu^n\delta_1\) converge geometrically in \(\mathcal W_2\). The displayed quantitative bound follows from the contraction and \(\mathcal W_2^2(\delta_1,\mu_\nu)=\mathbb E W_\nu^2-1\). If \(p=\Pr(W_\nu=0)\), strict positivity of \(Z\) implies \(3p=p^2+2p\), so \(p=0\) because the mean is one.

**3. Monotonicity under convex order.** Convolution of independent variables, multiplication by a common nonnegative factor, and convex mixtures preserve convex order when means agree. Consequently \(\mu\le_{\mathrm{cx}}\eta\) implies \(T_\nu\mu\le_{\mathrm{cx}}T_\nu\eta\). For any common input law \(\mu\), the hypothesis \(\nu_1\le_{\mathrm{cx}}\nu_2\) gives \(T_{\nu_1}\mu\le_{\mathrm{cx}}T_{\nu_2}\mu\): condition on \(U_1=u\), and note that \(z\mapsto g(zu)\) is convex for every convex \(g\). Induction from \(\delta_1\) yields \(T_{\nu_1}^n\delta_1\le_{\mathrm{cx}}T_{\nu_2}^n\delta_1\). The Wasserstein limits inherit convex order, for example by convergence of stop-loss expectations \(\mathbb E(W_n-t)_+\) at each real \(t\) and equality of means. This proves the order of the full stationary laws.

**4. Strict Laplace comparison.** Set \(f_i(s)=\mathbb E e^{-sW_{\nu_i}}\). Their fixed-point identities read

\[
3f_i(s)=f_i(s)^2+2\mathbb E_{Z\sim\nu_i}f_i(sZ).
\]

Convex order gives \(f_1(u)\le f_2(u)\) for every \(u\ge0\). For fixed \(s>0\), the map \(z\mapsto f_2(sz)\) is strictly convex: its second derivative is \(s^2\mathbb E[W_{\nu_2}^2e^{-szW_{\nu_2}}]>0\), because \(W_{\nu_2}>0\) almost surely and has a finite second moment. Distinct probability laws in strict convex order have strictly different expectations of every strictly convex integrable function; this follows also from strict conditional Jensen in a martingale coupling. Therefore

\[
3f_1(s)\le f_2(s)^2+2\mathbb E_{\nu_1}f_2(sZ)
< f_2(s)^2+2\mathbb E_{\nu_2}f_2(sZ)=3f_2(s).
\]

This establishes strictness for all positive \(s\), not just a local moment inequality.

**5. Exact variance and sharp minimizer.** Squaring the fixed-point branches gives \(3m_2=2m_2+2+2\mathbb E Z^2\,m_2\), yielding \(m_2=2/(1-2\mathbb E Z^2)\). Any probability measure of mean \(1/2\) dominates \(\delta_{1/2}\) in convex order by Jensen; equality of \(\mathbb E Z^2\) at its lower bound \(1/4\) forces \(Z=1/2\) almost surely. Thus the convex-order minimum is global, and the second-moment and Laplace strictness assertions follow. The deterministic-ratio case \(A=r\) reproduces \(\mathbb E W^2=[r(1-r)]^{-1}\), while the uniform-ratio case reproduces \(\mathbb E W^2=6\), in agreement with previously known calculations.

## Verification

The standalone file `checker.py` implements the fixed-point distributional operator using exact fractions through four finite iterations for three ordered daughter laws: equal halves, a mixture of equal and quarter splits, and quarter splitting alone. It verifies probability and first-moment preservation, the exact finite-step second-moment recursion, stop-loss convex ordering at every support knot, the stationary second- and third-moment formulas, and independent Laplace evaluations. It also computes seven iterations of the Laplace recursion and tests strict ordering at six positive Laplace parameters. Running `python checker.py` produced `PASS: 509 finite exact-rational and numerical checks; analytical proof needed for limits`. The finite checks do not establish the universal theorem, which follows from the preceding analytic argument.

## Relationship to prior work

P. L. Krapivsky's 2026 study of mass-independent coagulation and binary fragmentation derives the stationary mass balance, deterministic-ratio Laplace equation, and exact low-order moments, and treats uniform random splitting. Those physical equations and their known moment identities are used here, not claimed as new. The addition is a distribution-wide convex-order comparison across **arbitrary** daughter-fraction laws, its strict all-parameter Laplace consequence, a sharp unique minimizer, and a Wasserstein uniqueness/convergence statement for the stationary equation.

Alsmeyer, Biggins and Meiners study the general smoothing-transform fixed-point problem. Their fixed-point framework is relevant, but their cited results do not themselves give the ordered-kernel comparison for this aggregation–fragmentation model. Matsoukas addresses discrete pure fragmentation and its partition ensemble, not the specified continuous-mass stationary competition with constant-kernel aggregation. Kerr and Langer establish solution theory for discrete coagulation–fragmentation equations, rather than this continuous-mass comparison. Caliebe and Rösler investigate existence and uniqueness of finite-variance smoothing-transform fixed points, an overlapping part of the framework; the full text could not be obtained to assess all implications. These distinctions do not constitute a proof of worldwide novelty.

## Limitations

The comparison assumes the two **symmetrized** daughter-fraction laws are comparable in convex order. Two arbitrary splitting laws can be incomparable; no universal total ranking is asserted. The result concerns stationary mean-field solutions with finite second moment and fixed total mass, not finite-particle stochastic systems, spatial clustering, kinetic convergence in physical time, mass-dependent coagulation/fragmentation rates, fragmentation into more than two daughters, or laws that place positive mass at exactly zero or one. The stationary transform may not have an elementary density, and no explicit density formula is claimed. A more general published smoothing-transform monotonicity theorem could imply parts of the comparison; publication-priority verification remains a distinct task.

## References

1. P. L. Krapivsky, *Aggregation-Fragmentation Processes with Broken Detailed Balance*, arXiv:2605.22383v1 (first public 2026-05-21), https://arxiv.org/html/2605.22383v1 . Relevant sections II–III, especially equations (40)–(44) and (51)–(57).
2. G. Alsmeyer, J. D. Biggins, M. Meiners, *The functional equation of the smoothing transform*, Annals of Probability **40** (2012), 2069–2105, arXiv:0906.3133, https://arxiv.org/abs/0906.3133 .
3. T. Matsoukas, *Stochastic Theory of Discrete Binary Fragmentation—Kinetics and Thermodynamics*, Entropy **24** (2022), 229, https://doi.org/10.3390/e24020229 .
4. L. Kerr, M. Langer, *Discrete Coagulation–Fragmentation Systems in Weighted \(\ell^1\) Spaces*, Integral Equations and Operator Theory **98** (2026), 21, https://doi.org/10.1007/s00020-026-02838-w .
5. A. Caliebe, U. Rösler, *Fixed points with finite variance of a smoothing transformation*, Stochastic Processes and their Applications **107** (2003), 105–129, https://doi.org/10.1016/S0304-4149(03)00075-9 . Full text was not available for inspection.
