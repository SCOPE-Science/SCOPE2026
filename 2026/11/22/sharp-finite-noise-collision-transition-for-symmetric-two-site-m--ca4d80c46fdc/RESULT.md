# Sharp finite-noise collision transition for symmetric two-site Matérn-\(3/2\) quadrature

## Finding

Let \(f\) be a zero-mean Gaussian process on \([0,1]\) with covariance
\[
 K(t,u)=(1+|t-u|)e^{-|t-u|}.
\]
Observe \(f(1/2-s)+\epsilon_1\) and \(f(1/2+s)+\epsilon_2\), where the observation errors are independent \(N(0,\eta)\), \(\eta>0\), and \(0\le s\le1/2\). Minimize the conditional variance of \(I=\int_0^1f(t)\,dt\) over this **reflection-symmetric design class**, allowing two independent observations at the same location when \(s=0\).

Define the positive functions and threshold, for \(0<s\le1/2\),
\[
\begin{aligned}
 m(s)&=4-2e^{-1/2}\bigl(\tfrac52\cosh s-s\sinh s\bigr),\\
 u(s)&=2e^{-1/2}\bigl(\tfrac32\sinh(s)/s-\cosh s\bigr),\\
 k(s)&=(1+2s)e^{-2s},\\
 T(s)&=\frac{2e^{-2s}m(s)}{u(s)}-1-k(s).
\end{aligned}
\]
Use continuous values \(u(0)=e^{-1/2}\) and \(T(0)=8\sqrt e-12\). Then \(T\) is strictly decreasing on \([0,1/2]\), with \(T(1/2)<0\), and the unique minimizing separation \(s_\eta\) is
\[
\boxed{
 s_\eta=\begin{cases}
 \text{the unique }s\in(0,1/2)\text{ with }T(s)=\eta,&0<\eta<8\sqrt e-12,\\
 0,&\eta\ge8\sqrt e-12.
 \end{cases}}
\]
The minimum posterior variance in this class is
\[
\boxed{V_\eta^{\mathrm{sym}}=\frac8e-2-\frac{2m(s_\eta)^2}{1+\eta+k(s_\eta)}.}
\]
The transition is continuous but **linear** rather than square-root:
\[
 s_\eta=\frac{8\sqrt e-12-\eta}{16\sqrt e-20}
 +O\bigl((8\sqrt e-12-\eta)^2\bigr),\qquad \eta\uparrow 8\sqrt e-12.
\]
This is an exact finite-noise switch from separated sites to independent replication at the midpoint. In particular, at \(\eta=0.1\), the unique symmetric optimum is \(s_\eta\approx0.2340266459\), with sites approximately \(0.2659733541\) and \(0.7340266459\); its posterior integral variance is approximately \(0.04735406822\), versus \(0.05183587149\) for two midpoint observations.

## Assumptions and scope

The stationary Matérn-\(3/2\) covariance has unit point variance and range parameter one. The uniform integration measure on \([0,1]\), exactly two noisy observations, equal independent positive error variances, and the reflection constraint on nodes are part of the theorem. Sampling at the same point twice means two independent noisy evaluations, not one observation reused. Posterior integration variance depends only on design, not realized data. The claim **does not optimize unrestricted asymmetric pairs**, and no inference about other smoothness or range parameters is asserted.

## Proof

**1. Gaussian conditioning and exact scalar objective.** Let \(q=\operatorname{Var}(I)\) and \(c_i=\operatorname{Cov}(I,f(t_i))\). Gaussian conditioning gives \(\operatorname{Var}(I\mid y)=q-c^\mathsf{T}(K_X+\eta I_2)^{-1}c\). Elementary integration of \((1+r)e^{-r}\) yields
\[
 q=2\int_0^1(1-r)(1+r)e^{-r}\,dr=8/e-2,
 \qquad c_1=c_2=m(s).
\]
The observation covariance matrix is \(\bigl(\begin{smallmatrix}1+\eta&k(s)\\k(s)&1+\eta\end{smallmatrix}\bigr)\). It is positive definite for every \(\eta>0\), including \(s=0\). Hence the amount of variance removed is exactly
\[
 R_\eta(s)=\frac{2m(s)^2}{1+\eta+k(s)},
\]
so minimizing variance is equivalent to maximizing \(R_\eta\).

**2. Strict one-crossing derivative.** Since \(r\mapsto(1+r)e^{-r}\) decreases strictly for \(r>0\), we have \(m'(s)<0\) for \(s>0\) and \(u(s)=-m'(s)/s>0\). Direct differentiation gives \(k'(s)=-4se^{-2s}\). Therefore
\[
 \operatorname{sgn}R_\eta'(s)=\operatorname{sgn}(T(s)-\eta),\qquad 0<s\le1/2.
\]
Differentiating the displayed expression for \(T\), and using \(m'=-su\), gives the exact identity
\[
 T'(s)=2e^{-2s}\left[s-\frac{m(s)}{u(s)}\left(2+\frac{u'(s)}{u(s)}\right)\right].
\]
The following elementary uniform inequalities establish strict negativity without numerical assumptions. The power series
\[
 u(s)=e^{-1/2}\left[1-\sum_{j=1}^\infty
 \frac{4j-1}{(2j+1)(2j)!}s^{2j}\right]
\]
shows \(u(s)\le e^{-1/2}\). Using \(\sinh s/s\ge1+s^2/6\) and \(\cosh s\le1+s^2/2+s^4/20\) on \([0,1/2]\) yields
\[
 u(s)\ge e^{-1/2}(1-s^2/2-s^4/10)\ge(139/160)e^{-1/2}.
\]
From the derivative of \(u\), the positive term \((s\cosh s-\sinh s)/s^2\) can be discarded to obtain \(u'(s)>-2e^{-1/2}\sinh(1/2)\), and therefore \(u'(s)/u(s)>-1.21\). Also \(m(s)\ge m(1/2)=2-3/e>0.89\), so \(su(s)/m(s)<0.35\), using \(e^{-1/2}<0.607\). Consequently
\[
 2+\frac{u'(s)}{u(s)}>0.79>\frac{s u(s)}{m(s)},
\]
which substituted into the exact expression above proves \(T'(s)<0\). The decimal inequalities here are strict rational bounds (e.g. \(1.21=121/100\)) established by elementary exponential-series estimates, not floating-point premises.

**3. Boundary values and unique optimum.** Taking \(s\downarrow0\) gives \(m(0)=4-5e^{-1/2}\), \(u(0)=e^{-1/2}\), hence \(T(0)=8\sqrt e-12\). At the opposite endpoint,
\[
 T(1/2)=\frac{1+2e-e^2}{e(e-2)}<0,
\]
since \(e>1+\sqrt2\). Strict monotonicity means \(T(s)=\eta\) has exactly one solution in \((0,1/2)\) when \(0<\eta<T(0)\), and no positive solution otherwise. The derivative sign in Step 2 gives a strictly increasing-then-decreasing objective in the first case and strictly decreasing objective on \((0,1/2]\) in the second. This also excludes both endpoint minima (except the stated midpoint collision), proves all uniqueness assertions, and identifies the equality case at the critical noise.

**4. Linear collision law.** The analytic continuation of \(u\) is even near zero, while \(k(s)=(1+2s)e^{-2s}\) has an odd cubic term when \(s\ge0\). A direct Taylor expansion gives
\[
 T(s)=8\sqrt e-12-(16\sqrt e-20)s+O(s^2),\qquad s\downarrow0.
\]
The coefficient \(16\sqrt e-20\) is strictly positive. Solving \(T(s_\eta)=\eta\) with the inverse-function theorem on the right half-line proves the stated linear approach of the optimal separation.

## Verification

The accompanying `verify.py` uses only the Python standard library. Run `python3 verify.py` in the same directory. The separate `symbolic_check.py` uses SymPy for exact identity checks. It compares the exact integrated kernel mean against composite Simpson integration at 999 positive separations, checks threshold monotonicity and positivity at those separations, evaluates the two-by-two Gram inverse independently, and compares the analytic optimum against 1,001 separation-grid points for each of eight noise variances. All checks pass in the supplied `verification_output.txt` and `symbolic_output.txt` logs. These finite tests supplement, but do not replace, Steps 1–4.

## Relationship to prior work

Karvonen, Kanagawa and Särkkä (2018 preprint, 2019 journal) study positivity and magnitudes of Bayesian quadrature weights, including the Matérn-\(3/2\) kernel, but their inspected Sections 3 and 4 do not provide the fixed-two-measurement, positive-noise, reflection-paired optimizer or its finite collision threshold. Cai, Lam and Scarlett (2022 preprint) study noisy Matérn Bayesian-quadrature error rates, with a query budget growing asymptotically; their inspected problem setup and Theorem 1 do not give an exact finite-budget location classification. Pronzato and Zhigljavsky (2020) develop a broad quadrature-design/energy-minimization framework rather than this exact symmetric nugget transition. The ordinary Gaussian conditioning identity and kernel integration are standard; they are not claimed new.

Related exact noisy two-node results for *rough exponential* and *Brownian bridge* kernels use different covariance laws. The present sharp **finite collision** threshold for a once-mean-square-differentiable Matérn kernel is not implied by their positive-noise separated-node formulas. Search-based priority assessment is not a uniqueness guarantee; a historical symmetric optimal-design formula may predate these sources.

## Limitations

The symmetric restriction is essential. The theorem does not establish global optimality over arbitrary asymmetric pairs, nor characterize optimal designs for other length scales, observation-error correlations or more than two observations. The noise variance is strictly positive. The interpretation is Bayesian posterior integral variance (equivalently, squared worst-case kernel quadrature error with observation regularization), not the variance of a particular Monte Carlo estimator. No practical runtime gain is inferred. No independent mathematical validation has been performed.

## References

1. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509v1 (first public 2018-12-20), https://arxiv.org/abs/1812.08509; *Statistics and Computing* (2019), https://doi.org/10.1007/s11222-019-09901-0.
2. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615v1 (first public 2022-02-22), https://arxiv.org/abs/2202.10615.
3. L. Pronzato and A. Zhigljavsky, *Bayesian Quadrature, Energy Minimization, and Space-Filling Design*, *SIAM/ASA Journal on Uncertainty Quantification* **8** (2020), 959–1011, https://doi.org/10.1137/18M1210332.
