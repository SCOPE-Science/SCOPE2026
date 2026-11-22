# Exact convex-risk ordering of finite-time stochastic returns at fixed mean work

## Finding

For the finite-time resetting Brownian search model defined below, increasing *only* the return-phase diffusivity strictly increases total absorption time in convex order, despite leaving its expectation, the complete law of the switching work, and the absorption-side probabilities unchanged. Precisely, for every \(0<d_1<d_2\),

\[
T_{d_1}\prec_{\mathrm{cx}}T_{d_2},\qquad
\operatorname{Var}(T_{d_2})-\operatorname{Var}(T_{d_1})
=\frac{2(d_2-d_1)}{a^4}\,\mathbb E W>0.
\]

Here \(\prec_{\mathrm{cx}}\) denotes convex order, with strictly larger expectation of every strictly convex function for which the relevant expectations exist. In particular, *every* positive-strike excess-duration loss \(\mathbb E (T_d-t)_+\), for fixed \(t>0\), strictly increases with \(d\), and the variance has an exactly linear, positive response. The mean work \(\mathbb E W\) and mean time are the same for all return diffusivities.

## Assumptions and scope

Fix \(D,L,a,r>0\) and \(x\in(0,L)\). At each exploration episode a particle starts at \(x\), follows Brownian motion with generator \(D\partial_{yy}\) on \((0,L)\), and is absorbed at either endpoint. An independent exponential alarm of rate \(r\), active *only while exploring*, instead terminates an unsuccessful episode and triggers return from its alarm position \(Y\). During return, both absorbing boundaries are inactive; motion on the whole real line is governed by

\[
 dX_t=-a\operatorname{sgn}(X_t-x)\,dt+\sqrt{2d}\,dB_t,
\]

until first hitting \(x\). An independent new exploration then begins. All exploration paths, alarms, and return Brownian noises are mutually independent between episodes. The only parameter varied in the theorem is the return-phase diffusivity \(d>0\); the inward force coefficient \(a\) is fixed. Let \(T_d\) be total physical time until absorption. The switching work is \(W=a\sum_{j=1}^{N}|Y_j-x|\), where \(N\) is the count of interrupted explorations and \(Y_j\) their positions. Work is incurred when the potential \(a|y-x|\) is switched on and none is incurred when it is switched off at its minimum.

A real random variable \(U\) precedes \(V\) in convex order, \(U\preceq_{\mathrm{cx}}V\), when \(\mathbb E\phi(U)\le\mathbb E\phi(V)\) for all convex \(\phi\) for which the expectations are finite. Equal means and inequalities for the call losses \(\mathbb E(U-t)_+\), \(t\in\mathbb R\), characterize this order.

## Proof

**1. An exploration skeleton independent of return noise.** On a common probability space sample all exploration Brownian excursions and exponential alarms, and retain the successful terminal absorbing side. Write \(S\) for their combined duration, \(N\) for the number of failed excursions, and \(\ell_j=|Y_j-x|\) for their nonnegative return distances. Because every return restarts at exactly \(x\), this complete skeleton has a law independent of \(d\), and so do \(W=a\sum_j\ell_j\), \(N\), and the terminal absorption side. The one-episode success probability is \(q=\mathbb E_x e^{-r\tau_{\partial}}>0\), where \(\tau_{\partial}\) is the no-alarm Brownian exit time. Thus \(N\) is geometric with success probability \(q\), has all moments, and conditional alarm positions lie in the bounded interval. In particular all quantities used below have finite second moments.

**2. A sharp convex-order lemma for one return.** Conditional on a distance \(\ell>0\), the return duration \(R_d(\ell)\) is the first-passage time to \(\ell\) of \(at+\sqrt{2d}B_t\). Its density and Laplace transform are

\[
 f_d(t\mid\ell)=\frac{\ell}{\sqrt{4\pi d\,t^3}}
 \exp\!\left[-\frac{(\ell-at)^2}{4dt}\right],\qquad
 \mathbb E e^{-sR_d(\ell)}=\exp\!\left[-\frac{\ell(\sqrt{a^2+4ds}-a)}{2d}\right].
\]

They give \(\mathbb E R_d(\ell)=\ell/a\) and \(\operatorname{Var}R_d(\ell)=2d\ell/a^3\). For \(d_2>d_1\), the likelihood ratio is

\[
\frac{f_{d_2}(t\mid\ell)}{f_{d_1}(t\mid\ell)}
=\sqrt{\frac{d_1}{d_2}}\exp\!\left[
\frac14\left(\frac1{d_1}-\frac1{d_2}\right)
\frac{(\ell-at)^2}{t}\right].
\]

The function \((\ell-at)^2/t\) decreases from infinity to zero at \(t=\ell/a\), then increases to infinity. Thus there are exactly two distinct density crossings \(0<t_-<\ell/a<t_+\), and \(f_{d_2}-f_{d_1}\) has signs \(+,-,+\). Define \(C(t)=\mathbb E(R_{d_2}(\ell)-t)_+-\mathbb E(R_{d_1}(\ell)-t)_+\). For \(t\le t_-\), equality of total mass and first moment gives \(C(t)=\int_0^t(t-u)(f_{d_2}-f_{d_1})(u)\,du>0\) whenever \(t>0\). For \(t\ge t_+\), \(C(t)=\int_t^\infty(u-t)(f_{d_2}-f_{d_1})(u)\,du>0\). In the intervening interval \(C''(t)=f_{d_2}(t)-f_{d_1}(t)<0\); concavity and the positive endpoint values give \(C(t)>0\) throughout. The equal-mean call characterization proves strict convex-order increase of each return duration.

**3. Transport through all return episodes.** Conditional on the exploration skeleton, the total duration is

\[
T_d=S+\sum_{j=1}^N R_{d,j}(\ell_j),
\]

where the return times are independent given the skeleton. Convolution by an independent law preserves convex order. By Step 2, the conditional total durations are ordered, strictly for every strictly convex test whenever some \(\ell_j>0\). Averaging over the same skeleton yields \(T_{d_1}\preceq_{\mathrm{cx}}T_{d_2}\). Since the positive-rate alarm produces at least one positive-distance return with positive probability, the order is strict for every strictly convex integrable test. In addition, for every fixed \(t>0\), there is positive probability of exactly one alarm before time \(t\), with \(S<t\) and positive return distance. Conditional on those skeletons, the call inequality in Step 2 is strict at strike \(t-S>0\); averaging establishes the asserted strict call-loss inequality.

**4. Exact variance–work sensitivity.** Conditional on the skeleton,

\[
\mathbb E[T_d\mid\mathcal E]=S+\frac1a\sum_{j=1}^N\ell_j=S+\frac{W}{a^2},\quad
\operatorname{Var}(T_d\mid\mathcal E)=\frac{2d}{a^3}\sum_{j=1}^N\ell_j
=\frac{2d}{a^4}W.
\]

The law of total variance now gives the stronger affine identity

\[
\operatorname{Var}(T_d)
=\operatorname{Var}\left(S+\frac{W}{a^2}\right)
+\frac{2d}{a^4}\mathbb E W.
\]

The first term and \(\mathbb E W\) are independent of \(d\). The latter is strictly positive because \(r>0\), \(x\) is interior, and an alarm before absorption has positive probability and positive displacement almost surely. This proves the difference formula and strict increase of variance.

**5. Exact positive coefficient from the killed Green function.** Let \(\kappa=\sqrt{r/D}\). For an exploration started at \(x\), its killed resolvent kernel is

\[
 G_r(x,y)=\frac{\sinh(\kappa\min\{x,y\})\sinh(\kappa(L-\max\{x,y\}))}{D\kappa\sinh(\kappa L)}
\quad (0<y<L),
\]

and the probability of absorption before an alarm is

\[
 q=\frac{\sinh(\kappa x)+\sinh(\kappa(L-x))}{\sinh(\kappa L)}.
\]

Renewal of the geometric number of failed attempts yields

\[
 \mathbb E W=\frac{ar}{q}\int_0^L G_r(x,y)|y-x|\,dy>0.
\]

Consequently the variance sensitivity is explicitly calculable using only the exploration killed Green function and expected switching work; no return-time simulation is necessary. The absorption-side probabilities are the corresponding no-alarm discounted endpoint fluxes divided by \(q\), also independent of \(d\).

## Verification

The included `verify.py` uses high-precision quadrature and independent Laplace-transform differentiation for \(D=L=1\), \(x=0.3\), \(r=2\), \(a=3\), and return diffusivities \(d_1=0.25\) and \(d_2=1.5\). It checks return-density normalization and moments; first-passage transform identities; positive call-loss gaps; global renewal-transform monotonicity; mean invariance; and the variance–work formula. Its 38 assertions passed. The computed mean time is approximately \(0.1190518943251817\), and the two variances are \(0.0157068468878447\) and \(0.0193607080290913\), giving the predicted difference \(0.00365386114124666\). The infinite-family convex-order conclusion is proved analytically in Steps 1–4, not inferred from numerical tests. To replay, install `mpmath` and run `python verify.py` in the directory containing the extracted files.

## Relationship to prior work

Chen, Tang, and Li (2026) introduce exactly the bounded two-target finite-time-resetting system, derive the return Laplace transform, the global completion-time transform, mean return time, splitting probabilities, work generating function, and the identity \(\mathbb E W=a^2\mathbb E t_R\). These forward-model results are inputs here, not claimed as new. The additional result is an entire-family convex-risk comparison across return diffusivities, with a strict and exact variance-response coefficient determined by mean work. The difference requires identifying the two-crossing structure of the return-time densities and passing its convex order through the correlated exploration and geometric renewal skeleton; ordering only their Laplace transforms does not establish convex order.

Singh (2024) develops an earlier general joint work–completion-time renewal identity and mean cost–time Pareto analysis for stochastic return, in a different (half-line) search geometry. Those results give a broad transform representation and must be credited; the strict all-convex-loss comparison and affine variance–work derivative are not presented in its examined analysis. Classical inverse-Gaussian first-passage densities and stop-loss criteria are standard tools, not innovations. An unlocated implicit equivalent in the general stochastic-return or stochastic-order literature remains possible.

## Limitations

The targets are completely inactive during return, and the return potential is exactly linear, giving constant-magnitude inward drift. The diffusivity changes at fixed drift coefficient; a physical system coupling diffusivity and mobility may not permit this independent adjustment. The result concerns mathematical convex order and exact moments, not noise-limited parameter inference, finite-data uncertainty, or a pointwise order of time densities or survival probabilities. The theorem is restricted to positive rates, a fixed interior reset site, and independent exploration/return episodes. Although the mean is independent of the return diffusivity, the complete time law is not. Strictness in convex expectations is asserted only when expectations are well defined.

## References

- H. Chen, C. Tang, and G. Li, *Finite-time stochastic resetting in bounded domains: competing targets, energetic cost, and optimal search strategies*, arXiv:2611.23790v1, first submitted 18 November 2026. https://arxiv.org/html/2611.23790v1
- P. Singh, *Emerging cost-time Pareto front for diffusion with stochastic return*, arXiv:2407.02071 (2024), *New Journal of Physics* **26**, 103014, DOI:10.1088/1367-2630/ad825c. https://arxiv.org/abs/2407.02071
- S. Gupta, C. A. Plata, A. Kundu, and A. Pal, *Stochastic resetting with stochastic returns using external trap*, arXiv:2004.11679 (2020). https://arxiv.org/abs/2004.11679
