# A sharp online-gain phase boundary between typical convergence and prospective squared amplification

## Finding

For the **out-of-sample ratio-feedback branch** of stochastic online scaled gradient descent, a two-curvature quadratic family has an exactly solvable, persistently random learned stepsize. Its stationary *prospective* squared update factor crosses one at a sharp learning-gain boundary, although the **actual coupled optimization iterates converge exponentially almost surely at every admissible learning gain**.

Let \(b>1\), and let \(A_k,B_k\) be mutually independent, equiprobable samples from \(\{1,b\}\), independently across iterations. For \(0<\eta<1/(2b^2)\), the original out-of-sample ratio-feedback iteration with candidate stepsizes \([1/b,1]\) is, exactly,
\[
 X_{k+1}=(1-A_kP_k)X_k,\qquad
 P_{k+1}=(1-2\eta A_kB_k)P_k+2\eta B_k.
\]
Starting with \(X_0\ne0\) and \(P_0\in(1/b,1)\), the projection is never active and all finite \(X_k\) are nonzero.

Put \(\mu=(1+b)/2\), \(\nu=(1+b^2)/2\), and \(s^2=\nu-\mu^2=(b-1)^2/4\). The stepsize chain has a unique invariant law \(\pi_\eta\) on \([1/b,1]\). Under that law,
\[
 \mathbb E_{\pi_\eta}P=\frac1\mu,
 \qquad
 \operatorname{Var}_{\pi_\eta}(P)
 =\frac{\eta\nu s^2}{\mu^2(\mu^2-\eta\nu^2)},
 \qquad
 \operatorname{Corr}(P_k,P_{k+j})=(1-2\eta\mu^2)^j
 \quad(j\ge0).
\]

A **fresh test update**, evaluated independently of a stationary \(P\sim\pi_\eta\), has prospective squared multiplier
\[
 M_\eta:=\mathbb E_{P\sim\pi_\eta,A}\big[(1-AP)^2\big]
 =\frac{s^2}{\mu^2-\eta\nu^2}.
\]
Thus \(M_\eta>1\) precisely for \(\eta>\eta_c(b):=4b/(1+b^2)^2\). Such an \(\eta\) exists under the stipulated admissibility bound \(\eta<1/(2b^2)\) **if and only if** \(b>\beta_*\), where \(\beta_*=7.739425778\ldots\) is the unique real root greater than one of
\[
 \beta^4-8\beta^3+2\beta^2+1=0.
\]
At \(b=10\), \(\eta=1/225\) is admissible and gives \(M_\eta=18225/17024>1\), whereas the fixed population-target step \(1/\mu\) has prospective squared multiplier only \(81/121<1\).

**Nevertheless**, for every \(b>1\), every admissible \(\eta\), and every stated initial condition, almost surely
\[
 \limsup_{n\to\infty}\frac1n\log\frac{|X_n|}{|X_0|}
 \le \log\frac{b-1}{b+1}<0.
\]
Therefore \(M_\eta>1\) cannot be interpreted as divergence of the actual coupled stochastic iterates. It is an exact prospective squared-error diagnostic, not the exponential rate of \(\mathbb E X_n^2\).

## Assumptions and scope

Each component is the scalar interpolation loss \(f_A(x)=\tfrac12 Ax^2\), with \(A\in\{1,b\}\), \(b>1\), and common minimum \(f^\star=0\) at zero. The update sample \(A_k\) and evaluation sample \(B_k\) are fresh, independent and equiprobable at every iteration. The gradient is \(f_A'(x)=Ax\). The preconditioner is scalar; there is no momentum, no regularizer, and no hypergradient null step. The ratio feedback is evaluated from sampled function values as in equation (4) and Algorithm 2 of the cited 2026 paper. The OSGM gain is \(0<\eta<1/(2b^2)\), the convex admissible set is \([1/b,1]\), and initially \(X_0\ne0\), \(P_0\in(1/b,1)\). All statements about the invariant law concern the stepsize marginal, not a stationary law for the decaying optimization state.

## Proof

**1. Exact source reduction and invariant interval.** For \(x\ne0\), the ratio feedback from independent update/evaluation samples equals
\[
 r_{x,A,B}(p)=\frac{f_B(x-pf_A'(x))}{f_A(x)}
 =\frac BA(1-Ap)^2,\qquad
 \partial_pr_{x,A,B}(p)=-2B(1-Ap).
\]
Projected online gradient descent consequently gives \(P^+=\Pi_{[1/b,1]}[(1-2\eta AB)P+2\eta B]\). Let \(w=2\eta AB\in(0,1)\). The argument is the strict convex combination \((1-w)P+w/A\). Since \(1/A\) is an endpoint of \([1/b,1]\), the projection is inactive and an interior \(P\) remains interior. Therefore \(1-AP\ne0\) at every finite iteration and the feedback denominator never vanishes.

**2. Uniqueness and exact second moments.** Each of the four affine maps \(p\mapsto (1-2\eta AB)p+2\eta B\) has slope in \((0,1-2\eta)\). Synchronous coupling of two trajectories therefore contracts their distance geometrically, proving existence and uniqueness of an invariant law on the compact interval and convergence toward it. Write \(\mu=\mathbb EA=\mathbb EB\), \(\nu=\mathbb EA^2=\mathbb EB^2\). Independence of the current pair from \(P_k\) gives
\[
 \mathbb E[P_{k+1}\mid P_k]=(1-2\eta\mu^2)P_k+2\eta\mu.
\]
Thus the invariant mean is \(p_*=1/\mu\). Center at that value: \(Y_{k+1}=(1-2\eta A_kB_k)Y_k+2\eta B_k(1-A_k/\mu)\). The innovation has mean zero and variance \(4\eta^2\nu s^2/\mu^2\), while the squared random slope has mean \(1-4\eta\mu^2+4\eta^2\nu^2\). In stationarity the cross term vanishes because \(Y_k\) is independent of the fresh samples and has mean zero. Solving the resulting second-moment equation gives
\[
 V_\eta=\frac{4\eta^2\nu s^2/\mu^2}{4\eta(\mu^2-\eta\nu^2)}
 =\frac{\eta\nu s^2}{\mu^2(\mu^2-\eta\nu^2)}.
\]
The denominator is positive because \(\nu\le b\mu\) and \(\eta b^2<1/2\). Iterated conditional expectation gives \(\mathbb E[Y_{k+j}\mid Y_k]=(1-2\eta\mu^2)^jY_k\); the covariance and correlation formula follow, with positive variance since \(b>1\).

**3. Prospective squared amplification and sharp boundary.** Since the fresh test curvature is independent of stationary \(P\),
\[
 M_\eta=1-2\mu p_*+\nu(p_*^2+V_\eta)
 =\frac{s^2}{\mu^2-\eta\nu^2}.
\]
For equiprobable curvatures \(1,b\), \(2\mu^2-\nu=b\), so \(M_\eta>1\) exactly when \(\eta>\eta_c(b)=b/\nu^2=4b/(1+b^2)^2\). The open interval \((\eta_c(b),1/(2b^2))\) is nonempty precisely when \((1+b^2)^2>8b^3\). Its difference is \(F(b)=b^4-8b^3+2b^2+1\). Because \(F'(b)=4b(b^2-6b+1)\), \(F\) decreases on \((1,3+\sqrt8)\) and increases thereafter. Given \(F(1)<0\) and \(F(b)\to+\infty\), there is exactly one root \(\beta_*>1\). Direct rational substitution at \(b=10,\eta=1/225\) proves the stated example.

**4. Almost-sure contraction of the actual coupled state.** Let \(P_k^*\) be the stationary stepsize process driven by the same future sample pairs; it can be constructed from the infinite iid past since the affine maps contract uniformly. Synchronous contraction implies \(|P_k-P_k^*|\le(1-2\eta)^k|P_0-P_0^*|\). For every integer \(K\ge1\), the truncated logarithm
\[
 \ell_K(p,A)=\max\{\log|1-Ap|,-K\}
\]
is bounded and Lipschitz in \(p\) on \([1/b,1]\) for each \(A\in\{1,b\}\). Hence the empirical averages of \(\ell_K(P_k,A_k)\) and \(\ell_K(P_k^*,A_k)\) differ by a quantity tending to zero. The stationary sample-pair process is ergodic, so these averages converge almost surely to \(\mathbb E\ell_K(P^*,A)\). Since \(\log|1-Ap|\le\ell_K(p,A)\), taking the limsup and then \(K\to\infty\) yields
\[
 \limsup_{n\to\infty} n^{-1}\log|X_n/X_0|
 \le \mathbb E\log|1-AP^*|.
\]
The expectation on the right is allowed to equal \(-\infty\); monotone convergence after a common upper shift justifies the truncation limit. Independence of current \(A\) from \(P^*\) and the invariant interval give
\[
 \mathbb E[\log|1-AP^*|\mid P^*=p]
 =\tfrac12\log(1-p)+\tfrac12\log(bp-1)=:g(p).
\]
Both logarithms are concave on the interval; therefore Jensen's inequality, also valid for an extended-negative expectation, gives \(\mathbb Eg(P^*)\le g(\mathbb EP^*)=g(2/(1+b))=\log((b-1)/(b+1))<0\). This proves the stated bound for every interior starting stepsize, not merely in the stationary initialization.

## Verification

The standalone standard-library script `artifacts/verify_online_scaling.py` checks the exact conditional and stationary first/second-moment identities using rational arithmetic for four independent two-curvature laws, verifies 512 finite steps remain interior without zero state, and checks the rational phase example, including \(M_\eta=18225/17024\), the stationary variance \(8181/1029952\), and the isolated root bracket \(7.739<\beta_*<7.740\). The infinite-horizon stationary and almost-sure claims are proved analytically above; finite checks are not substitutes for that proof.

## Relationship to prior work

The 2026 source introduces the out-of-sample feedback and online scaling update; the present calculation specializes that **published** algorithm rather than introducing a new optimizer. An earlier mathematical analysis of the same stochastic OSGM feedback establishes the population targets \(\mathbb E[P]_{\mathrm{target}}=1/\mathbb EA\) and fixed-target mean-square stability thresholds. Those statements alone do not determine the invariant distribution of the **actually learned** online stepsize, the exact gain-controlled prospective squared-amplification transition, or the simultaneous pathwise contraction bound. Classical stochastic approximation already supplies generic affine-recursion and ergodic tools; the new comparison is the particular coupled ratio-feedback classification, including its exact critical curvature ratio and the distinction between stationary prospective risk and actual pathwise behavior. Analogous separations between typical and second-moment behavior for other stochastic algorithms are known, but involve different update laws and observables.

## Limitations

The result is for an equal-probability, two-positive-curvature, one-dimensional interpolation model and independent out-of-sample feedback. The scalar curvature contrast \(b\) is not a condition number of a matrix problem. For growing \(b\), the chosen interval \([1/b,1]\) is much wider than an interval of uniform diameter proportional to \(1/b\); the sharp phase should not be interpreted as a result under the source paper's most restrictive diameter scaling. The sharp \(\beta_*\) threshold refers to the **stationary prospective squared multiplier** \(M_\eta\), not to divergence of \(\mathbb EX_k^2\). No mean-square divergence of the coupled optimization state is asserted. The proof of almost-sure convergence does not supply the exact Lyapunov exponent. The source's published large-batch guarantees concern other assumptions and are not contradicted. Unexamined analyses of random affine recursions or stochastic adaptation under different language remain possible prior-art risks.

## References

1. W. Zhang, W. Gao, Y. Ye, M. Udell, *Stochastic Gradient Methods with Online Scaling*, public repository version dated 2026-05-28, https://optimization-online.org/2026/05/stochastic-gradient-methods-with-online-scaling/; updated preprint arXiv:2609.11751, https://arxiv.org/abs/2609.11751.
2. *Population feedback targets and sharp curvature-stability thresholds in stochastic OSGM*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-sosgm-feedback-curvature-stability--021cc30589a6.
3. W. Gao, Y.-C. Chu, Y. Ye, M. Udell, *Gradient Methods with Online Scaling Part I. Theoretical Foundations*, arXiv:2505.23081, https://arxiv.org/abs/2505.23081.
4. Y. Wang et al., *Steady-State Behavior of Constant-Stepsize Stochastic Approximation: Gaussian Approximation and Tail Bounds*, ICML 2026, https://proceedings.mlr.press/v306/wang26il.html.
