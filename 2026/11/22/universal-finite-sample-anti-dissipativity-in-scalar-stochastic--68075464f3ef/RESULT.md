# Universal finite-sample anti-dissipativity in scalar stochastic dynamic mode decomposition

## Finding

A strictly dissipative population generator need not yield even an almost-surely stable finite-data generator in one-dimensional stochastic dynamic mode decomposition. This failure is **universal among strictly positive, nonconstant generator-domain observables** for conservative invariant Markov models with strict population dissipation, and it forces divergent long-horizon mean-square prediction risk for every fixed sample size. An explicit smooth diffusion supplies an exact exponential lower bound although its population Richardson step contracts.

For the circle diffusion and observable specified below, all integers \(m\ge1\), \(k\ge0\), and all real \(h>0\) obey

\[
\mathbb E\left\|\widehat Q_{h,m}^{k}\psi-e^{kh\mathcal L}\psi\right\|_{L^2(\rho)}^{2}
\ge\frac92\,3^{-m}\left[\left(1+\frac h3+\frac{h^2}{18}\right)^k-1\right]^2.
\]

Here \(\widehat Q_{h,m}\) denotes the scalar SDMD-R map fitted *once* from \(m\) independent invariant samples and then reused for all \(k\) steps. The population scalar step is strictly contractive when \(0<h<18\). The statements concern long horizons at **fixed data size**, not a contradiction to fixed-horizon sampling convergence.

## Assumptions and scope

Let \(\rho\) be an invariant probability for a conservative Markov semigroup \((P_t)_{t\ge0}\) with generator \(\mathcal L\), contractive on \(L^2(\rho)\). Fix one real generator-domain observable satisfying \(0<a\le\psi\le b<\infty\) \(\rho\)-almost everywhere, \(\mathcal L\psi\in L^1(\rho)\), the invariant identity \(\int\mathcal L\psi\,d\rho=0\), \(\mathcal L\psi\not\equiv0\), and strict population dissipation \(\int\psi\mathcal L\psi\,d\rho<0\). These properties hold for every positive, bounded, nonconstant smooth observable of an ergodic reversible uniformly elliptic diffusion on a connected compact manifold.

For \(m\ge1\), take independent \(X_1,\dots,X_m\sim\rho\) and a finite nonnegative scalar ridge \(\gamma\ge0\). Define

\[
\widehat G_m=\frac1m\sum_{i=1}^m\psi(X_i)^2,\qquad
\widehat H_m=\frac1m\sum_{i=1}^m\psi(X_i)(\mathcal L\psi)(X_i),\qquad
\widehat\lambda_{m,\gamma}=\frac{\widehat H_m}{\widehat G_m+\gamma}.
\]

The SDMD-R step is the fixed fitted multiplier \(\widehat Q_{h,m,\gamma}=1+h\widehat\lambda_{m,\gamma}+\frac12h^2\widehat\lambda_{m,\gamma}^2\), with positive step \(h\). Prediction from \(\psi\) after \(k\) steps is \(\widehat Q_{h,m,\gamma}^{k}\psi\). Independent samples are used for the *fitting*, not resampled between time steps.

For the explicit example, take \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), stationary Brownian motion \(dX_t=\sqrt2\,dW_t\pmod{2\pi}\), uniform \(\rho\), \(\mathcal L=\partial_x^2\), \(\psi(x)=2+\cos x\), and \(\gamma=0\).

## Proof

**(1) A positive empirical growth event always exists.** Since \(\int\mathcal L\psi\,d\rho=0\) and \(\mathcal L\psi\not\equiv0\), the set \(\{\mathcal L\psi>0\}\) has positive measure. Some \(\varepsilon>0\) thus gives \(p=\rho(\{\mathcal L\psi\ge\varepsilon\})>0\). On the event that every one of the \(m\) independent samples lies in this set, of probability \(p^m\), positivity and boundedness of the observable yield

\[
\widehat\lambda_{m,\gamma}\ge\delta:=\frac{a\varepsilon}{b^2+\gamma}>0.
\]

For every \(h>0\), the polynomial \(q_h(z)=1+hz+\tfrac12h^2z^2\) is increasing for positive \(z\), and \(q_h(\delta)>1\). Hence \(\mathbb E|\widehat Q_{h,m,\gamma}|^{2k}\ge p^m q_h(\delta)^{2k}\to\infty\). The population Galerkin scalar \(\lambda_{\rm pop}=\int\psi\mathcal L\psi\,d\rho/\int\psi^2\,d\rho\) is negative by assumption; no population instability was used.

**(2) The forecast error diverges, not just the empirical operator norm.** Markov contraction gives \(\|P_{kh}\psi\|_{L^2(\rho)}\le\|\psi\|_{L^2(\rho)}\). On the event above, the reverse triangle inequality implies

\[
\|\widehat Q_{h,m,\gamma}^{k}\psi-P_{kh}\psi\|_{L^2(\rho)}
\ge (q_h(\delta)^k-1)\|\psi\|_{L^2(\rho)}.
\]

Squaring, then averaging over independent fitting samples, proves a positive exponential lower bound. Each fixed-\(k\) risk is finite in the compact smooth example; the divergence is a long-horizon effect.

**(3) Exact circle specialization and constants.** Since \(\mathcal L\psi=-\cos x\) and \(\int\cos x\,d\rho=0\), \(\int\cos^2x\,d\rho=1/2\), one has \(G=9/2\), \(H=-1/2\), and \(\lambda_{\rm pop}=-1/9\). The true forecast is \(P_{kh}\psi=2+e^{-kh}\cos x\). The population multiplier equals \(1-h/9+h^2/162\), strictly between \(0\) and \(1\) for \(0<h<18\).

Let \(B=\{x:\cos x\le-1/2\}\), which has stationary probability exactly \(1/3\). For \(x\in B\), \(\psi(x)>0\) and

\[
\frac{(\mathcal L\psi)(x)}{\psi(x)}=\frac{-\cos x}{2+\cos x}\ge\frac13.
\]

The empirical \(\widehat\lambda_{m,0}\) is a positive-weight average of these pointwise ratios, with weights \(\psi(X_i)^2\). Hence on the event \(X_1,\dots,X_m\in B\), probability \(3^{-m}\), one has \(\widehat\lambda_{m,0}\ge1/3\) and \(\widehat Q_{h,m,0}\ge q_h(1/3)=1+h/3+h^2/18\). The general error inequality from step (2), and \(\|\psi\|_{L^2(\rho)}^2=9/2\), give the advertised bound for every integer \(k\ge0\). The threshold \(1/3\) is attained at \(\cos x=-1/2\), so the stated samplewise growth floor is sharp on this explicitly chosen event.

## Verification

The included standalone `verify.py` checks the exact population integrals through trigonometric moments, verifies the polynomial factors and symbolic inequalities with rational arithmetic, and tests the stated samplewise event inequality on an exhaustive finite rational grid of cosine values for several sample counts, steps and ridge values. Run `python verify.py` with Python 3 and no external packages. All-domain and probability claims follow from the proof, not finite-grid enumeration.

## Relationship to prior work

Xu, *A Second-Order Stochastic Dynamic Mode Decomposition by Richardson Extrapolation* (arXiv:2611.00793, Sections 2.1, 2.2, 2.4, 3.1–3.3, 4), defines the same empirical Gram/generator ratio, applies this Richardson polynomial, and proves fixed-horizon high-probability sampling bounds. Its perturbation estimates permit exponential constants depending on the observation horizon. The present statement instead quantifies an unavoidable positive-growth event for a non-invariant one-observable dictionary **at every finite sample size**, yielding explicit divergence of the expected long-horizon true prediction error even in a smooth reversible diffusion with a strictly contracting population step. The source's observation that invariant dictionaries give exact empirical generators is consistent with this result: \(\operatorname{span}\{2+\cos x\}\) is not generator-invariant.

The original SDMD formulation by Xu et al. (arXiv:2501.13301, Sections 3.1 and 4.1) studies the first-order empirical map and sampling limits, not the above fixed-sample all-horizon failure. Llamazares-Elias et al. (arXiv:2405.00539; *Journal of Computational Dynamics* 2026) derive operator-error and spectral-convergence bounds as data increase, which do not impose samplewise dissipativity at fixed size. Schurig et al. (arXiv:2602.04720) study multi-step EDMD prediction residuals; its accessible abstract does not establish the specific universal sign-event and smooth-diffusion lower bound, and full-text equivalence remains to be excluded by subsequent independent literature assessment.

## Limitations

The construction uses a one-dimensional dictionary containing a positive nonconstant observable and exact generator evaluations; a generator-invariant dictionary or an explicitly enforced dissipativity constraint may eliminate the mechanism. The result does not refute fixed-horizon high-probability convergence or imply that typical samples diverge. The exponential lower bound describes expectation at fixed finite \(m\), not the large-data-first limit. It assumes independent invariant sampling and a fixed empirical propagator; newly sampled operators at each step are not covered. It does not compare optimal choices of regularization or the rate of the rare-event probability as sample size grows. Independent verification has not been performed.

## References

- Yuanchao Xu, *A Second-Order Stochastic Dynamic Mode Decomposition by Richardson Extrapolation*, arXiv:2611.00793, initial posting 2026-10-31. https://arxiv.org/abs/2611.00793
- Yuanchao Xu et al., *A Data-Driven Framework for Koopman Semigroup Estimation in Stochastic Dynamical Systems*, arXiv:2501.13301. https://arxiv.org/abs/2501.13301
- Liam Llamazares-Elias et al., *Data-driven approximation of Koopman operators and generators: Convergence rates and error bounds*, arXiv:2405.00539; *Journal of Computational Dynamics* 15 (2026), 163–206. https://arxiv.org/abs/2405.00539
- Roland Schurig et al., *On Data-Driven Unbiased Predictors using the Koopman Operator*, arXiv:2602.04720. https://arxiv.org/abs/2602.04720
