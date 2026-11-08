# A one-step obstruction and a sharp late-time penalty for fluctuating lattice jump rates

## Finding

Consider a nearest-neighbor symmetric continuous-time random walk on the positive integers, absorbed at zero, with total instantaneous jump rate \(\lambda(t)\): each possible direction has rate \(\lambda(t)/2\) away from the boundary, and jumps from site one to zero are absorbing. Let the initial position be an integer \(m\geq1\). Fix a resampling period \(\tau>0\), and set \(\lambda(t)=\lambda_j\) for \(j\tau\leq t<(j+1)\tau\), where \((\lambda_j)_{j\geq0}\) are independent copies of a nonconstant random variable supported in \([a,b]\subset(0,\infty)\), independent of all jump directions and Poisson randomness. Write \(\mu=\mathbb E\lambda_j\), \(v=\operatorname{Var}(\lambda_j)>0\), and let \(S_m(t)\) be the survival probability up to time \(t\). Let \(S_m^0(t)\) denote survival with the deterministic constant rate \(\mu\), and set \(\Delta_m(t)=S_m(t)-S_m^0(t)\).

**Theorem.** For every \(\tau>0\) and every such nondegenerate bounded positive rate distribution:

1. At the adjacent starting site \(m=1\), \(\Delta_1(t)>0\) for **every** \(t>0\). Temporal rate disorder always raises the probability of not yet reaching the absorbing site.
2. At each integer distance \(m\geq2\), \(\Delta_m(t)<0\) for every sufficiently small positive time, but \(\Delta_m(t)>0\) for every sufficiently large time. Hence at least one finite-horizon survival crossing is unavoidable; **uniqueness of this finite-disorder crossing is not asserted**.
3. For every fixed \(m\geq1\), the late-time penalty is universal up to the rate variance and resampling period:
   \[
   \lim_{t\to\infty}t^{3/2}\Delta_m(t)
     =\frac{3m\sqrt{2/\pi}\,v\tau}{8\mu^{5/2}}>0.
   \]
4. There is an exact, unique **weak-disorder** crossover horizon. Specifically, replace the rates by \(\lambda_j=\mu+\varepsilon Z_j\), where the \(Z_j\) are independent copies of a bounded centered nonconstant random variable of variance \(v_Z\), and \(\varepsilon>0\) is small enough to retain positivity. If \(t=n\tau+\rho\), where \(n=\lfloor t/\tau\rfloor\) and \(0\leq\rho<\tau\), then
   \[
   \lim_{\varepsilon\downarrow0}\frac{\Delta_m^{(\varepsilon)}(t)}{\varepsilon^2}
    =\frac{v_Z}{2}(n\tau^2+\rho^2)h_m''(\mu t),
   \]
   with \(h_m\) defined below. For \(m=1\) this coefficient is positive at every horizon. For each \(m\geq2\) it is negative before, zero at, and positive after the unique horizon \(t=u_m/\mu\), where \(u_m\) is the unique maximizer of \(u\mapsto m e^{-u}I_m(u)/u\) on \((0,\infty)\). It satisfies \(u_m>(m^2-1)/3\). In particular, the weak-disorder switch is **independent of** \(\tau\) and of the bounded centered rate-fluctuation law, except for its positive variance.

Here \(I_k\) is the modified Bessel function of the first kind of integer order \(k\). An exact formula for the unit-rate survival function is
\[
 h_m(u)=e^{-u}\left(I_0(u)+I_m(u)+2\sum_{k=1}^{m-1}I_k(u)\right),\qquad u\geq0.
\]
Consequently the controlled survival is exactly \(S_m(t)=\mathbb E[h_m(\Lambda_t)]\) for the accumulated random clock \(\Lambda_t=\int_0^t\lambda(s)\,ds\), while \(S_m^0(t)=h_m(\mu t)\).

## Assumptions and scope

Time is continuous and physical step count is an inhomogeneous Poisson process conditional on the external rate path. Every jump is equally likely to be leftward or rightward. The absorption event is the first jump into zero; the environment is independent of the random walk and is resampled **simultaneously and completely** every deterministic period \(\tau\), starting at time zero. The bounded support requirement \(0<a\leq\lambda_j\leq b<\infty\) is used for uniform small-time expansions, concentration and the quantitative late-time asymptotic. No reset is applied to the position, and the underlying walk has no drift.

The result concerns finite-horizon first-passage *survival*, not a finite mean first-passage time. For this unbiased half-line walk and bounded positive rate laws, the mean first-passage time remains infinite. Comparisons always use the **same mean physical jump rate** \(\mu\). The weak-disorder part concerns the coefficient of \(\varepsilon^2\) at fixed positive \(t\), not the assertion that finite-\(\varepsilon\) survival has exactly one crossing.

## Proof

**1. Operational-time survival and exact derivatives.** Let \(Y_u\) be the symmetric unit-total-rate absorbed walk, started at \(m\). The reflection principle for its killed kernel gives, for \(j\geq1\),
\[
 \Pr(Y_u=j,\,T_0>u)=e^{-u}\big(I_{j-m}(u)-I_{j+m}(u)\big).
\]
Summing over positive \(j\), using \(I_{-k}=I_k\), gives the displayed formula for \(h_m(u)=\Pr(T_0>u)\). Standard Bessel recurrences yield the positive first-passage density
\[
 f_m(u)=-h_m'(u)=\frac{m e^{-u}I_m(u)}{u},\qquad u>0.
\]
In particular, \(h_m\) is smooth on \((0,\infty)\), with an analytic extension to zero. For fixed \(m\), the power series and large-argument Bessel expansion give
\[
 h_m(u)=1-\frac{u^m}{2^m m!}+O(u^{m+1})\quad(u\downarrow0),
 \qquad h_m(u)=c_m u^{-1/2}+O(u^{-3/2})\quad(u\to\infty),
\]
where \(c_m=m\sqrt{2/\pi}\), and differentiation of the full asymptotic expansion gives
\[
 h_m''(u)=\frac{3c_m}{4}u^{-5/2}+O(u^{-7/2}),
 \qquad h_m'''(u)=O(u^{-7/2}).
\]

**2. Exactly one curvature change beyond one lattice step.** Using the modified-Bessel differential equation, the positive function \(f_m(u)=m e^{-u}I_m(u)/u\) solves
\[
 f_m''(u)+\left(2+\frac3u\right)f_m'(u)
 +\left(\frac3u+\frac{1-m^2}{u^2}\right)f_m(u)=0.
\]
Set \(J_m(u)=e^{2u}u^3 f_m'(u)\). The equation becomes the exact one-sign identity
\[
 J_m'(u)=e^{2u}u\big(m^2-1-3u\big)f_m(u).
\]
For every \(m\geq1\), \(J_m(0+)=0\), while the large-time density asymptotic gives \(J_m(u)\to-\infty\). When \(m=1\), \(J_1'(u)<0\) for all \(u>0\), so \(f_1'<0\) and \(h_1''>0\) everywhere. When \(m\geq2\), \(J_m\) increases strictly until \((m^2-1)/3\), then decreases strictly to \(-\infty\). Hence \(J_m\), and therefore \(f_m'\), has exactly one positive zero \(u_m>(m^2-1)/3\), changing from positive to negative. Since \(h_m''=-f_m'\), this proves the claimed one-step exception and the unique weak-disorder curvature transition, including its exact lower bound.

**3. Disorder sign at any horizon for \(m=1\).** Conditional on the jump-rate environment, the walk is the deterministic time change \(Y_{\Lambda_t}\). Thus \(S_m(t)=\mathbb E h_m(\Lambda_t)\) and \(\mathbb E\Lambda_t=\mu t\). For \(t>0\), \(\Lambda_t\) is nonconstant because its first resampling block has positive duration and \(v>0\). The strict convexity of \(h_1\), established above, gives by strict Jensen
\[
 S_1(t)=\mathbb E h_1(\Lambda_t)>h_1(\mathbb E\Lambda_t)=S_1^0(t).
\]

**4. Early-time acceleration at \(m\geq2\).** For \(0<t<\tau\), \(\Lambda_t=t\lambda_0\). Uniformly over the bounded rates, the small-\(u\) expansion gives
\[
 \Delta_m(t)=-\frac{t^m}{2^m m!}
 \big(\mathbb E[\lambda_0^m]-\mu^m\big)+O(t^{m+1}).
\]
For \(m\geq2\), strict convexity of the \(m\)-th power on positive rates shows the coefficient in parentheses is strictly positive. Hence \(\Delta_m(t)<0\) for all sufficiently small \(t>0\).

**5. Universal late-time penalty.** Write \(t=n\tau+\rho\), \(0\leq\rho<\tau\), and \(X_t=\Lambda_t-\mu t\). Independence of the resampled rates yields exactly
\[
 \mathbb E X_t=0,\qquad
 \mathbb E X_t^2=v(n\tau^2+\rho^2)=v\tau t+O(1).
\]
Boundedness of the independent summands gives \(\mathbb E|X_t|^3=O(t^{3/2})\) and an exponential concentration bound for \(\Pr(|X_t|>\mu t/2)\). Taylor's theorem on the complementary event, together with \(h_m'''(u)=O(u^{-7/2})\) when \(u\asymp t\), implies
\[
 \Delta_m(t)=\frac12h_m''(\mu t)\,\mathbb E X_t^2+O(t^{-2})
 =\frac{3c_m v\tau}{8\mu^{5/2}}t^{-3/2}+O(t^{-2}).
\]
Exponential concentration controls the omitted tail (including the Taylor polynomial there). The leading coefficient is positive; thus \(\Delta_m(t)>0\) at all sufficiently late times. In combination with Step 4 and continuity of \(S_m(t)\), this forces at least one crossing for \(m\geq2\). It establishes no upper bound on the number of such crossings.

**6. Unique second-order weak-disorder switch.** Under \(\lambda_j=\mu+\varepsilon Z_j\), write \(\Lambda_t=\mu t+\varepsilon W_t\), where \(\mathbb E W_t=0\) and \(\mathbb E W_t^2=v_Z(n\tau^2+\rho^2)>0\) for \(t>0\). Taylor's formula at fixed \(t\) gives
\[
 \Delta_m^{(\varepsilon)}(t)
 =\frac{\varepsilon^2v_Z}{2}(n\tau^2+\rho^2)
 h_m''(\mu t)+O_t(\varepsilon^3).
\]
Step 2 identifies exactly the sign, single zero and lower bound for the coefficient. Notice that the resampling period only scales its positive magnitude, not the location of its sign reversal. This completes the proof.

## Verification

The accompanying `verify.py` is standalone relative to this result and requires Python 3, NumPy and SciPy. Execute `python verify.py` from the folder containing this document. It reconstructs unit-rate survival by both modified-Bessel functions and finite killed-generator matrix exponentials, checks exact rational generator Taylor jets, brackets density modes, evaluates the resampled-clock mixture exactly for a symmetric two-point rate law, and tests the late-time coefficient. In the recorded execution it passed 168 finite checks. These calculations test implementations and representative parameters; the all-distribution and all-time conclusions follow from the preceding proof.

For illustration, with \(\mu=\tau=1\) and equally likely rates \(1/2\) and \(3/2\), numerical curvature locations are \(u_2=1.253877441969\ldots\), \(u_3=3.047804959898\ldots\), and \(u_5=8.463252358833\ldots\). They are not required for any argument.

## Relationship to prior work

Levit and Reuveni (arXiv:2609.26925, first submitted September 22, 2026) develop the doubly stochastic continuous-time random walk and an exact clock-based survival representation, emphasizing heavy-tailed jump-rate laws and the transition from infinite to finite mean first-passage time. Their general operational-time representation is the relevant starting point. The present claim instead assumes **bounded positive finite-variance rates** and determines the strict nearest-neighbor obstruction, the all-distribution early/late comparison, an explicit \(t^{-3/2}\) survival penalty and the single weak-disorder switching horizon. Those statements are not stated in the inspected source.

Sposini, Chechkin and Metzler (arXiv:1809.09186, first submitted September 24, 2018) find an early/late survival crossover for a continuous-space diffusing-diffusivity model and discuss its quenched/superstatistical limit. Consequently **the general idea that disorder can accelerate early passage and retard later passage is already known** and is not claimed as new in isolation. Their continuum model has no one-lattice-step exception, and neither that finding nor their reported crossover yields the finite-variance periodic-clock coefficient or the unique Bessel curvature location here. Grebenkov (arXiv:1812.07249, first submitted December 18, 2018) provides the general integrated-diffusivity spectral framework; this covers the time-change methodology but does not establish the discrete half-line curvature and quantitative sign classification.

The mathematical ingredients include standard Bessel recurrences and Markov time change. What is being distinguished is their conjunction in a sharp, directly testable classification for a specific lattice first-passage observable. No claim of priority over an uninspected specialized result is made.

## Limitations

The rate environment is bounded and bounded away from zero, independently resampled at fixed periods and independent of jump directions. Unbounded heavy-tail laws in the motivating work fall outside the late-time expansion. The survival crossing for fixed, finite disorder is proved to exist, **not** to be unique, and its location is not universal. A *unique* crossover is proved only for the second-order weak-disorder response. Finite-horizon survival is the observable; all bounded-rate models in this theorem still have divergent mean first-passage time on the half-line. Possible earlier recognition of the Bessel unimodality fact or of related clock-mixture asymptotics remains a publication-priority risk, not a mathematical assumption.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925 (2026), https://arxiv.org/html/2609.26925 . First submitted September 22, 2026.
2. V. Sposini, A. V. Chechkin and R. Metzler, *First passage statistics for diffusing diffusivity*, arXiv:1809.09186 (2018), https://arxiv.org/html/1809.09186v1 . First submitted September 24, 2018.
3. D. S. Grebenkov, *A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models*, arXiv:1812.07249 (2018), https://arxiv.org/abs/1812.07249 . First submitted December 18, 2018.
