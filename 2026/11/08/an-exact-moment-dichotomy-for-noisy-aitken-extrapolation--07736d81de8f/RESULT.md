# An exact moment dichotomy for noisy Aitken extrapolation

## Finding

Let \(x_j=a+bq^j\) for \(j=0,1,2\), where \(a\in\mathbb R\), \(b\ne0\), and \(-1<q<1\). Observe \(Y_j=x_j+\eta_j\), with \(\eta=(\eta_0,\eta_1,\eta_2)\) a centered jointly Gaussian vector, whose covariance matrix \(\Sigma\) may be singular. Define
\[
U=Y_1-Y_0,\qquad V=Y_2-2Y_1+Y_0,\qquad T=Y_0-\frac{U^2}{V}.
\]
The accelerated value \(T\) is defined almost surely whenever \(\operatorname{Var}(V)>0\) or \(\operatorname{Var}(V)=0\) (since in the latter case \(V=b(q-1)^2\ne0\)). The following is a complete dichotomy.

**Finite-moment cases.** If \(\operatorname{Var}(V)=0\), then \(T\) is a quadratic polynomial in a Gaussian vector, hence has every finite absolute moment. If \(\operatorname{Var}(V)>0\), let
\[
\kappa=\frac{\operatorname{Cov}(U,V)}{\operatorname{Var}(V)},\quad
\tau^2=\operatorname{Var}(U)-\frac{\operatorname{Cov}(U,V)^2}{\operatorname{Var}(V)},\quad
u_*=b(q-1)-\kappa b(q-1)^2,
\quad S=\nu_*^2+\tau^2.
\]
Then \(S=0\) exactly when \(U=\kappa V\) almost surely. In this case \(T=Y_0-\kappa^2V\) is Gaussian or deterministic, and has every finite absolute moment.

**Heavy-tail case.** If \(\operatorname{Var}(V)>0\) and \(S>0\), then
\[
\lim_{t\to\infty}t\,\mathbb P(T>t)
=\lim_{t\to\infty}t\,\mathbb P(T<-t)
=\frac{S}{\sqrt{2\pi\operatorname{Var}(V)}}
\exp\!\left(-\frac{b^2(q-1)^4}{2\operatorname{Var}(V)}\right)>0.
\]
Consequently \(\mathbb E|T|^p<\infty\) exactly for \(0<p<1\), and \(\mathbb E|T|^p=\infty\) for every \(p\ge1\). Both positive and negative parts of \(T\) have infinite expectation, so its Lebesgue mean is not defined. All these conclusions hold no matter how small the positive Gaussian noise variance is.

For \(\operatorname{Var}(V)>0\), the finite-moment exception has the explicit structural interpretation
\[
Y_2-(1+q)Y_1+qY_0=0\quad\text{almost surely}.
\]
Indeed, the equality \(U=\kappa V\) forces \(\kappa=1/(q-1)\), so the perturbed triple retains the original geometric ratio. This is the only such exception for nonconstant Gaussian curvature noise.

**Correlated-sampling consequence.** For \(\operatorname{Cov}(\eta_i,\eta_j)=\sigma^2[(1-\rho)\mathbf1_{i=j}+\rho]\), with \(\sigma>0\) and \(-1/2\le\rho\le1\), every \(\rho<1\) gives the heavy-tail case. Its one-sided tail constant is
\[
C_\rho=\frac{\frac14 b^2(1-q^2)^2+\frac12\sigma^2(1-\rho)}
{\sqrt{12\pi\sigma^2(1-\rho)}}
\exp\!\left(-\frac{b^2(q-1)^4}{12\sigma^2(1-\rho)}\right).
\]
At \(\rho=1\), the three errors are identical, and \(T=a+\eta_0\) is Gaussian. Thus arbitrarily strong but imperfect common-noise coupling cannot restore a finite first absolute moment; perfect coupling does.

## Assumptions and scope

The unperturbed observations are three exact terms of a real scalar geometric error sequence. The Gaussian perturbation has mean zero and any positive-semidefinite \(3\times3\) covariance; it need not be independent or positive definite. The extrapolation uses the unmodified Aitken \(\Delta^2\) formula, with no denominator clipping, regularization, or threshold-based fallback. Expectations are over the Gaussian observation errors for a single triple, not over repeated independent extrapolation rounds. For \(\rho\) in the exchangeable example, the stated interval is precisely the positive-semidefinite covariance range for three variables.

## Proof

**Step 1: deterministic denominators and projections.** Write \(u_0=b(q-1)\) and \(v_0=b(q-1)^2\ne0\); thus \(\mathbb EU=u_0\) and \(\mathbb EV=v_0\). When \(\operatorname{Var}(V)=0\), \(V=v_0\) surely and \(Y_0-U^2/v_0\) is a quadratic Gaussian polynomial. When \(s_V^2=\operatorname{Var}(V)>0\), Gaussian linear regression gives a Gaussian variable \(H=U-\kappa V\), independent of \(V\), with \(\mathbb EH=\nu_*\) and \(\mathbb EH^2=S\). Likewise \(Y_0=cV+J\), where \(c=\operatorname{Cov}(Y_0,V)/s_V^2\), and the *pair* \((H,J)\) is jointly Gaussian and independent of \(V\) (the constant mean belongs in \(J\)). Substitution yields
\[
T=J-2\kappa H+(c-\kappa^2)V-\frac{H^2}{V}.
\]

**Step 2: a pole-tail lemma.** If \(V\) is a nondegenerate Gaussian with a smooth positive density \(f_V\) at zero, and \((H,J)\) is a jointly Gaussian pair independent of \(V\), then for arbitrary fixed real \(c_0,c_1\), provided \(\mathbb E H^2>0\),
\[
\lim_{t\to\infty}t\,\mathbb P\!\left(J+c_0H+c_1V-\frac{H^2}{V}>t\right)
=\lim_{t\to\infty}t\,\mathbb P\!\left(J+c_0H+c_1V-\frac{H^2}{V}<-t\right)
=f_V(0)\,\mathbb EH^2.
\]
To verify the lemma, fix \((H,J)=(h,j)\) with \(h\ne0\). In any fixed neighborhood of zero, the event above a large positive threshold is obtained from a negative-\(V\) interval ending at zero whose length is \(h^2/t+O_{h,j}(t^{-2})\); for the negative threshold the interval is on the positive side and has the same leading length. The Gaussian density contributes \(f_V(0)h^2/t\). Make this uniform first on compact \((h,j)\) ranges, then let the compact cutoff increase: Gaussian moments bound the removed tails, while outside a fixed neighborhood of \(V=0\), the event requires a large Gaussian \(|H|+|J|+|V|\) and has probability \(o(t^{-1})\). One may split at \(|H|+|J|\le t^{1/8}\) to dominate the near-zero integrals by a constant multiple of \(H^2+1\), and bound the complement by Gaussian tails. Integration and dominated convergence give the displayed limits.

**Step 3: classification and moments.** Here \(f_V(0)=\exp(-v_0^2/(2s_V^2))/\sqrt{2\pi s_V^2}\), giving the claimed coefficient. If \(S=0\), then \(H=0\) almost surely, and the pole disappears identically; \(T=Y_0-\kappa^2V\). Because \(\mathbb EU=\kappa\mathbb EV\), this entails \(\kappa=u_0/v_0=1/(q-1)\) and equivalently \(Y_2-(1+q)Y_1+qY_0=0\) surely. Conversely that identity implies \(U=V/(q-1)\). If \(S>0\), both one-sided tails are asymptotic to a positive constant divided by \(t\). The layer-cake identity \(\mathbb E|T|^p=p\int_0^\infty t^{p-1}\mathbb P(|T|>t)\,dt\) yields the sharp moment threshold \(p=1\).

**Step 4: exchangeable covariance.** With \(\ell_U=(-1,1,0)\) and \(\ell_V=(1,-2,1)\), direct multiplication by the covariance matrix gives \(\operatorname{Var}(U)=2\sigma^2(1-\rho)\), \(\operatorname{Var}(V)=6\sigma^2(1-\rho)\), and \(\operatorname{Cov}(U,V)=-3\sigma^2(1-\rho)\). Thus \(\kappa=-1/2\), \(\tau^2=\sigma^2(1-\rho)/2\), and \(\nu_*=b(q^2-1)/2\); hence \(S>0\) for \(\rho<1\), and substitution gives \(C_\rho\). If \(\rho=1\), the Gaussian differences vanish, so direct deterministic cancellation produces \(T=a+\eta_0\).

## Verification

The standalone `verify.py` uses SymPy and mpmath to check the extrapolation identity, all exchangeable covariance contractions, degenerate and geometric-aligned exceptional cases, one exactly solvable rank-one Gaussian tail, and a collection of positive-semidefinite covariance examples. Reproduce with `python verify.py`; the recorded run reports 93 passed assertions. Finite checks are supporting evidence, not a substitute for the pole-tail lemma and its analytic limiting argument. For example, when \(a=0\), \(b=1\), \(q=1/2\), and only the third observation has independent standard Gaussian error, the two one-sided tail constants equal \(e^{-1/32}/(4\sqrt{2\pi})\).

## Relationship to prior work

Aitken's \(\Delta^2\) process and its cancellation-sensitive denominator are classical. Pomeranz (2017) develops deterministic sign-pattern extensions and analyzes extrapolation, without a Gaussian perturbation covariance classification or precise stochastic tail coefficients. Chen, Gan, Zhu, Narayan, and Liu (2021) investigate Aitken-accelerated gradient estimation and flag potential abnormal estimates from small denominators; their displayed convergence analysis is for a fixed regression dataset and does not give the complete one-triple random-noise moment dichotomy. Hodgkinson and Mahoney (2020) study heavy tails arising from stochastic optimization dynamics, a distinct mechanism from this one-shot rational pole. The new contribution is the full covariance-dependent moment classification, explicit balanced one-sided tail constant, and sharp perfect-versus-imperfect coupling boundary, rather than merely noticing the small-denominator hazard.

## Limitations

The result is restricted to a scalar three-term geometric input and jointly Gaussian additive noise; the covariance may be singular. It does not establish analogous constants for arbitrary non-Gaussian errors, nonlinear contraction histories, higher-order Shanks transforms, or practical clipped extrapolators. The asymptotic constant may be exponentially small when the denominator noise is tiny, so enormous finite samples could be needed to observe its tail numerically. A preexisting equivalent calculation in specialized statistical extrapolation literature cannot be excluded by the available comparisons, and no independent audit has been performed.

## References

1. S. B. Pomeranz (2017), “Aitken's \(\Delta^2\) method extended,” *Cogent Mathematics* **4**, 1308622. [DOI](https://doi.org/10.1080/23311835.2017.1308622). Accepted-author version posted online 20 March 2017; published online 3 April 2017.
2. J. Chen, M. Gan, Q. Zhu, P. Narayan, and Y. Liu (2021), “Robust Standard Gradient Descent Algorithm for ARX Models Using Aitken Acceleration Technique,” *IEEE Transactions on Cybernetics* **52**, 9646–9655 (final issue 2022). [DOI](https://doi.org/10.1109/TCYB.2021.3063113); [author manuscript](https://uwe-repository.worktribe.com/output/7231652).
3. L. Hodgkinson and M. Mahoney (2020), “Multiplicative Noise and Heavy Tails in Stochastic Optimization,” [arXiv:2006.06293](https://arxiv.org/abs/2006.06293).
4. C. Brezinski, “Aitken \(\Delta^2\) process,” *Encyclopedia of Mathematics*, [entry](https://encyclopediaofmath.org/wiki/Aitken_Delta%5E2_process).
