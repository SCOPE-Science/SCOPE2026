# A weak-shear thermal shift of two competing extreme-excursion reset ages

## Finding

Consider the stationary law of planar Brownian diffusion with linear shear and complete Poisson resetting. In the natural simultaneous rare-position and weak-shear scaling, there is a first-order switching of the most likely time since the last reset. The coexistence threshold has a strictly positive correction due to the longitudinal Brownian noise which disappears in the randomly accelerated limit.

Let \(D,r>0\), let \(R\to\infty\), and set
\[
\gamma_R=\frac{\eta r}{\sqrt R},\qquad
(x_R,y_R)=\sqrt{\frac{DR}{r}}\,(\eta,q),\qquad \eta>0.
\]
Here \(q\) is restricted to a fixed small open interval containing the number \(q_c\) defined below. Write \(T\) for the age since the last reset, conditional on observing this stationary endpoint. Define, for \(s>0\),
\[
F_\eta(s,q)=s+\frac{\eta^2-\eta^2sq+(1+\eta^2s^2/3)q^2}{s(4+\eta^2s^2/3)},
\quad g_\eta(s)=\frac1{s\sqrt{1+\eta^2s^2/12}}.
\]
There exist constants \(\eta_0<\infty\) and \(\varepsilon>0\) such that, for every \(\eta>\eta_0\), there is **exactly one** \(q_\eta\in(q_c-\varepsilon,q_c+\varepsilon)\) for which \(F_\eta(\cdot,q_\eta)\) has two distinct global minimizers \(s_a(\eta)<s_b(\eta)\). For \(q<q_\eta\) close to \(q_\eta\), the short-age minimizer alone is global; for \(q>q_\eta\), the long-age minimizer alone is global.

The limiting threshold \(q_c=3.722419436408398\ldots\) is uniquely characterized as follows. For \(q>2\sqrt3\), put
\[
a(q)=\frac{\sqrt{q^2+12}-q}{2},\qquad
b(q)=\frac{q+\sqrt{q^2-12}}{2},\qquad
F_\infty(s,q)=s+\frac{q^2}{s}-\frac{3q}{s^2}+\frac3{s^3}.
\]
Then \(q_c\) is the unique root above \(2\sqrt3\) of \(F_\infty(a(q),q)=F_\infty(b(q),q)\). With \(a_c=a(q_c)\), \(b_c=b(q_c)\) and
\[
L=\frac3{a_c^2}-\frac3{b_c^2}-4>0,\qquad
c=\frac9L\left[\frac{(q_ca_c-2)^2}{a_c^5}-\frac{(q_cb_c-2)^2}{b_c^5}\right]=6.447419590941246\ldots>0,
\]
the finite-shear threshold satisfies the **sharp thermal shift**
\[
\boxed{q_\eta=q_c+\frac{c}{\eta^2}+O(\eta^{-4})\quad(\eta\to\infty).}
\]

At coexistence, the conditional last-reset age has a genuinely two-point limiting law:
\[
\frac{rT}{\sqrt R}\ \Big|\ (X,Y)=(x_R,y_R)
\ \Longrightarrow\ \pi_a(\eta)\,\delta_{s_a(\eta)}+(1-\pi_a(\eta))\,\delta_{s_b(\eta)},
\]
where \(0<\pi_a(\eta)<1\) is explicitly
\[
\pi_a(\eta)=\frac{g_\eta(s_a)/\sqrt{\partial_s^2F_\eta(s_a,q_\eta)}}{g_\eta(s_a)/\sqrt{\partial_s^2F_\eta(s_a,q_\eta)}+g_\eta(s_b)/\sqrt{\partial_s^2F_\eta(s_b,q_\eta)}}.
\]
Away from coexistence, within the same fixed neighborhood, the limiting conditional age is a single atom at the unique global minimizer. This is a statement about a regular conditional density at the specified point, not conditioning on a positive-probability point event.

## Assumptions and scope

The between-reset stochastic differential equations are
\[
dX_t=\gamma_R Y_t\,dt+\sqrt{2D}\,dW_t^{(1)},\qquad
dY_t=\sqrt{2D}\,dW_t^{(2)},
\]
with independent standard Brownian motions. At every event of an independent rate-\(r\) Poisson process, both coordinates return to zero. Stationarity is considered separately for each value of \(R\). The theorem concerns \(q\) in a sufficiently small, fixed open neighborhood of \(q_c\) and \(\eta>\eta_0\); it makes no complete global classification for smaller \(\eta\) or arbitrary negative \(q\). The asymptotic parameter \(R\) is dimensionless. Primary MSC2020: 82C31.

## Proof

**1. Exact renewal kernel and scaled action.** At fixed age \(t>0\), the reset-free endpoint is centered Gaussian with covariance
\[
\Sigma_t=\begin{pmatrix}2Dt+2D\gamma_R^2t^3/3&D\gamma_Rt^2\\ D\gamma_Rt^2&2Dt\end{pmatrix}.
\]
Its determinant is \(4D^2t^2(1+\gamma_R^2t^2/12)\). In stationarity the reset age is exponential with density \(re^{-rt}\). The change of variables \(t=s\sqrt R/r\) gives the **exact**, not asymptotic, joint-density representation
\[
p_{\eta,R}(x_R,y_R)=\frac{r}{4\pi D}\int_0^\infty g_\eta(s)e^{-\sqrt R\,F_\eta(s,q)}\,ds.
\]
Thus the conditional scaled reset-age density is proportional to the integrand.

**2. The limiting competing minima.** Put \(\delta=\eta^{-2}\). Straight algebra gives
\[
F_\eta(s,q)=F_\infty(s,q)-\frac{9\delta(qs-2)^2}{s^3(s^2+12\delta)}.
\]
The derivative of the limit factorizes:
\[
s^4\partial_sF_\infty=-(qs-s^2-3)(qs+s^2-3).
\]
For \(q>2\sqrt3\), \(a(q)\) and \(b(q)\) are strict local minima separated by a local maximum \((q-\sqrt{q^2-12})/2\). Writing \(\Delta(q)=F_\infty(a(q),q)-F_\infty(b(q),q)\), the envelope theorem gives
\[
\Delta'(q)=\frac3{a(q)^2}-\frac3{b(q)^2}-4.
\]
This expression increases strictly for \(q>2\sqrt3\), and at the left endpoint equals \(2(\sqrt2-1)>0\). Moreover,
\[
\Delta(2\sqrt3)=-4\sqrt3+\frac83\sqrt6<0,
\]
whereas \(\Delta(q)\to\infty\) as \(q\to\infty\). Hence there is a unique simple crossing \(q_c\), and at that crossing the two global minima are distinct and nondegenerate.

**3. Persistence and globality.** In a sufficiently small closed interval about \(q_c\), the two limiting minima and separating maximum are simple, so the implicit-function theorem continues them smoothly for small \(\delta\ge0\). The limiting action is coercive at both ends. This remains uniform for small \(\delta\): at small \(s\), the numerator \(1-sq+s^2q^2/3+\delta q^2\) is bounded below by a positive constant for all nearby \(q\), while its denominator is \(s(s^2/3+4\delta)\); at large \(s\), \(F_\eta\ge s\) because the Gaussian quadratic form is nonnegative. Consequently, no unaccounted global minimum can escape to zero or infinity. Uniform convergence on a compact interval and the positive action gap away from the three continued critical points eliminate other competing minima. The difference of the two continued minimum values has strictly positive \(q\)-derivative near \((q_c,\delta=0)\); the implicit-function theorem therefore yields one and only one coexistence value \(q_\eta\) locally, with the stated change of preferred age.

**4. Thermal shift.** The exact correction expands uniformly near the two minima as
\[
F_\eta=F_\infty-9\delta\frac{(qs-2)^2}{s^5}+O(\delta^2).
\]
Because the first derivative vanishes at each minimum, its first-order perturbed action is obtained by evaluating this correction at the unperturbed minimum. Differentiating the equality of the two minimum values gives
\[
\left.\frac{dq_\eta}{d\delta}\right|_{\delta=0}=
\frac9{\Delta'(q_c)}\left[\frac{(q_ca_c-2)^2}{a_c^5}-\frac{(q_cb_c-2)^2}{b_c^5}\right]=c>0.
\]
Smoothness in \(\delta\) supplies the \(O(\eta^{-4})\) remainder. The strict sign follows from the displayed explicit algebraic quantities (numerically the bracket is \(1.432759909\ldots>0\)), or from direct substitution of the defining algebraic expressions into a rational sign comparison.

**5. Sharp density and conditioned-age law.** For fixed sufficiently large \(\eta\) and fixed \(q\) in the stated neighborhood, write \(I_\eta(q)=\min_{s>0}F_\eta(s,q)\), and \(\mathcal M_\eta(q)\) for its one or two global minimizers. Their second derivatives are strictly positive. Ordinary one-dimensional Laplace expansion then yields
\[
p_{\eta,R}(x_R,y_R)\sim\frac{r}{4\pi D}\sqrt{2\pi}\,R^{-1/4}e^{-\sqrt R I_\eta(q)}
\sum_{u\in\mathcal M_\eta(q)}\frac{g_\eta(u)}{\sqrt{\partial_s^2F_\eta(u,q)}}.
\]
The same localization applied to the normalized conditional age density gives one atom off coexistence, or the displayed two-atom mixture at coexistence. No finite-grid calculation is used to infer this asymptotic limit.

## Verification

The accompanying `checker.py` verifies the exact action identity symbolically, the cubic stationary equation factorization, the sign and magnitude of the threshold shift, independently computes five coexistence points, checks the Gaussian covariance quadratic form at multiple rare-event scales, and compares direct numerical integration of the **exact** stationary age integral with the two-saddle Laplace prefactor. Representative values: \(q_{25}=3.7327210531395205\ldots\) with age modes \(0.6882933208245269\ldots\), \(2.5443379364353014\ldots\); \(q_{60}=3.724209955666349\ldots\). These numerical computations corroborate, but do not replace, the analytic all-large-\(\eta\) proof. Run `python checker.py` from this self-contained package; dependencies are standard Python, NumPy, SciPy, and SymPy.

## Relationship to prior work

Singh (2020) derives the joint stationary law of a completely Poisson-reset random-acceleration process and its marginal tail. In its shear-dominated reduction, the present action \(F_\infty\) is an already accessible limiting rate description; **no claim of novelty is made for that limiting rate alone**. Related published mathematical work, “Extreme displacement, velocity and reset-age laws for random acceleration” (2026), provides an oriented-velocity large-deviation rate and conditional Gaussian fluctuations in the pure random-acceleration model. Its limiting-rate coverage is explicitly acknowledged. Abdoli, Olsen and Löwen (2024) derive the exact sheared Gaussian propagator and reset renewal density and examine moments, stationary perturbation theory and resetting costs. Another related 2026 result analyzes Gaussian age/transverse fluctuations of extreme sheared excursions about their typical path. The contribution assessed here is instead the **weak-shear double scaling with longitudinal thermal diffusion retained at leading exponential order**, yielding persistence of two global age mechanisms and the explicit positive \(\eta^{-2}\) displacement of their equality boundary. The cited antecedents do not state this threshold shift. This is a best-knowledge priority assessment, not proof of worldwide uniqueness.

## Limitations

The existence and uniqueness result is local in \(q\), valid only for sufficiently large \(\eta\). No explicit sharp minimal admissible shear parameter \(\eta_0\) is claimed. The conclusion concerns an asymptotic family whose physical shear decreases as \(R^{-1/2}\), not a phase transition at fixed finite rare-displacement scale in one fixed experimental setup. Conditional age at a point is understood via regular conditional densities. An independent literature and scientific review has not been performed. General large-deviation and asymptotic techniques could potentially imply parts of the result without this exact wording.

## References

1. P. Singh, *Random acceleration process under stochastic resetting*, arXiv:2007.05576, first made public 2020-07-10. https://arxiv.org/abs/2007.05576
2. I. Abdoli, K. S. Olsen and H. Löwen, *Shear-Driven Diffusion with Stochastic Resetting*, arXiv:2410.10333, first made public 2024-10-14. https://arxiv.org/abs/2410.10333
3. *Extreme displacement, velocity and reset-age laws for random acceleration*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-extreme-displacement-velocity-and-reset-age-laws-for-random-acce--c202451627eb
4. *Universal age–transverse fluctuation correlation in extreme sheared reset excursions*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-universal-age-transverse-fluctuation-correlation-in-extreme-shea--2c4d5a8bd4fb
5. *A directional moment-determinacy boundary for shear diffusion under resetting*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-directional-moment-determinacy-boundary-for-shear-diffusion-un--24df71ab6294
