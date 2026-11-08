# A sharp reentrant stability window for implicit Euler with Gaussian coefficient error

## Finding

For the scalar stable test equation \(y'(t)=-\lambda y(t)\), introduce independent, unbounded Gaussian errors in the drift coefficient used **inside** the backward-Euler solve. This produces an exact, parameter-independent threshold separating a regime where every positive noise level is almost surely stabilizing from a regime with an open interval of almost surely destabilizing noise levels. At the same time, every positive noise level destroys all absolute moments of order at least one after a single step.

More precisely, let \(a>1\), \(s>0\), \(Z_j\) be independent standard real Gaussians, and \(U_0\ne0\). Define
\[
U_{j+1}=\frac{U_j}{a+sZ_j},\qquad j=0,1,\ldots.
\]
Set
\[
w(t)=e^{-t^2/2}\int_0^t e^{v^2/2}\,dv,
\qquad H(t)=\mathbb E\log|t+Z|,
\]
where \(Z\) is standard normal. There is exactly one \(t_*>0\) solving \(t_*w(t_*)=1\). Define
\[
a_* =t_*e^{-H(t_*)}=1.27807758752610\ldots,
\qquad t_*=1.30692972771928\ldots.
\]
Writing \(F_a(s)=\mathbb E\log|a+sZ|\), the following exhaustive classification holds:

1. If \(a>a_*\), then \(F_a(s)>0\) for every \(s>0\), so \(|U_j|\to0\) exponentially almost surely.
2. If \(a=a_*\), the same holds except at the unique level \(s=a/t_*\). At this level, \(\liminf_{j\to\infty}|U_j|=0\) and \(\limsup_{j\to\infty}|U_j|=\infty\) almost surely.
3. If \(1<a<a_*\), exactly two levels \(0<s_-(a)<a/t_*<s_+(a)\) solve \(F_a(s)=0\). The iterates grow exponentially almost surely for \(s_-(a)<s<s_+(a)\) and decay exponentially almost surely outside the closed interval. At either endpoint, the liminf and limsup are respectively zero and infinity almost surely.

For all \(a>1\), \(s>0\), integers \(j\ge1\), and real \(p\ge1\),
\[
\mathbb E|U_j|^p=\infty.
\]
For \(0<p<1\) these moments are finite, and exponential almost-sure decay is equivalent to existence of *some* \(p\in(0,1)\) with \(\mathbb E|U_j|^p\to0\) exponentially.

In numerical-method parameters, \(a=1+h\lambda\), \(s=h\sigma\), where \(h>0\), \(\lambda>0\), and \(\sigma>0\). The universal critical scaled drift is therefore \(h\lambda=a_*-1=0.27807758752610\ldots\).

## Assumptions and scope

The underlying ODE is scalar, deterministic and strictly dissipative: \(y'=-\lambda y\), \(\lambda>0\). Each implicit Euler step substitutes an independently perturbed coefficient \(\lambda+\sigma Z_j\) for \(\lambda\). The perturbation is *not* a Brownian forcing term in an Itô SDE and need not remain nonnegative. It is an explicitly defined error-in-operator model, not a claim that any particular probabilistic ODE filter uses this update. Computations use exact real arithmetic; Gaussian denominator zeros have probability zero and, by countable union, no finite iteration encounters one almost surely. The starting value is any fixed nonzero real number.

The terms almost surely exponentially decaying and growing mean respectively that the almost-sure limit \(\lim_{j\to\infty}j^{-1}\log|U_j|\) is strictly negative and strictly positive. There is no claim of exponential behavior at a zero-exponent boundary.

## Proof

**Step 1: the logarithmic potential.** The Gaussian convolution
\[
H(t)=\int_{\mathbb R}\frac{e^{-(x-t)^2/2}}{\sqrt{2\pi}}\log|x|\,dx
\]
is smooth and finite, since the logarithmic singularity is locally integrable and Gaussian tails control infinity. Differentiating the Gaussian density and integrating by parts using \(x\log|x|\to0\) at the origin gives
\[
H''(t)+tH'(t)=1,\qquad H'(0)=0.
\]
The unique solution is \(H'(t)=w(t)\). Consequently,
\[
H(0)=-\frac{\gamma+\log 2}{2},\qquad
H(t)=-\frac{\gamma+\log 2}{2}+\int_0^t w(u)\,du,
\]
where \(\gamma\) denotes Euler's constant.

**Step 2: unique maximizer of a Gaussian attenuation deficit.** For \(t>0\), \(w(t)>0\), \(w'(t)=1-tw(t)\), and \(w(t)\sim1/t\) as \(t\to\infty\), the last fact following directly by l'Hôpital's rule applied to its integral representation. Put \(g(t)=tw(t)\). We have \(g(0)=0\). If \(g\) never crossed level one, then \(w'=1-g\ge0\) for all positive \(t\), contradicting \(w(t)>0\) and \(w(t)\to0\). At **every** crossing \(g(t)=1\),
\[
g'(t)=w(t)+t(1-tw(t))=\frac1t>0.
\]
All crossings are therefore strictly upward; continuity precludes more than one. This proves existence and uniqueness of \(t_*\), with \(g(t)<1\) below and \(g(t)>1\) above it.

**Step 3: the sharp minimum and both stability boundaries.** Scaling the Gaussian gives
\[
F_a(s)=\log s+H(a/s),\qquad
F'_a(s)=\frac{1-(a/s)w(a/s)}s.
\]
By Step 2 the derivative is strictly negative for \(0<s<a/t_*\) and strictly positive for \(s>a/t_*\). Thus \(s_*=a/t_*\) is the unique global minimum and
\[
\min_{s>0}F_a(s)
=\log(a/t_*)+H(t_*)
=\log(a/a_*).
\]
By local logarithmic uniform integrability, \(F_a(s)\to\log a>0\) as \(s\downarrow0\), while \(F_a(s)=\log s+H(a/s)\to\infty\) as \(s\to\infty\). Because the same formulas hold at \(a=1\), the strict initial decrease of \(F_1(s)\) from \(F_1(0+)=0\) gives \(\log(1/a_*)<0\), so \(a_*>1\) without relying on decimal approximations. Strict monotonicity on either side of the minimum gives the claimed zero counts, endpoint cases and open unstable interval.

For instance, when \(a=1.1\), the two zeroes are approximately \(s_-=0.41239587047708\) and \(s_+=1.45407701771656\). Their existence is proved by monotonicity and not inferred from these decimals.

**Step 4: almost-sure and fractional-moment behavior.** The logarithmic increments \(L_j=\log|a+sZ_j|\) are independent, identically distributed, nondegenerate, and have finite moments of all finite polynomial orders. Therefore the strong law yields
\[
\lim_{j\to\infty}\frac{\log|U_j|}{j}=-F_a(s)
\quad\text{almost surely}.
\]
When \(F_a(s)=0\), the centered increments \(-L_j\) have strictly positive finite variance. The law of the iterated logarithm implies unbounded positive and negative partial sums, proving the asserted limsup and liminf for \(|U_j|\).

The density of \(a+sZ\) is strictly positive at zero. Accordingly, its reciprocal has infinite absolute \(p\)-moment for every \(p\ge1\), while \(\mathbb E|a+sZ|^{-p}<\infty\) for \(0<p<1\). Independence gives
\[
\mathbb E|U_j|^p=|U_0|^p\big(\mathbb E|a+sZ|^{-p}\big)^j,
\qquad 0<p<1.
\]
Writing \(M(p)=\mathbb E e^{-pL_0}\), the right derivative \((\log M)'(0+)=-F_a(s)\) is justified by integrability of \(|L_0|e^{\epsilon|L_0|}\) for every \(\epsilon\in(0,1)\). Hence \(F_a(s)>0\) gives \(M(p)<1\) for sufficiently small \(p>0\). Conversely, Jensen's inequality yields \(M(p)\ge e^{-pF_a(s)}\ge1\) whenever \(F_a(s)\le0\). This proves the fractional-moment equivalence and completes the classification.

## Verification

A reproducible checker is included at `verification/check.py`, requiring Python, NumPy and SciPy. Run `python verification/check.py` from the package root. It independently integrates the Gaussian logarithmic potential across its singularity, checks the Dawson differential equation, verifies the stationary threshold, compares analytic slopes to finite differences, inspects 603 sampled global-minimum inequalities, solves two critical noise levels for each of five subcritical drifts, and checks four finite-sample logarithmic means with a fixed pseudorandom seed. The complete checker executed successfully with `CHECKS_OK 824`.

These are finite corroborating calculations only. The uniqueness, infinite-horizon classification, and moment-divergence conclusions follow from the proof above, not simulation.

## Relationship to prior work

Bosch (2026) studies scalable, stable probabilistic numerical ODE filters, using Jacobian-vector products, stochastic covariance estimation and iterative relinearization. Its main proposed method retains the full Jacobian; the Gaussian perturbation of the implicit drift coefficient considered here is a *different* test mechanism, prompted by the broader issue of numerical stability under uncertain operators. No equivalence with or failure of Bosch's algorithm is asserted.

Bochacik and Przybyłowicz (2021) analyze randomized Euler schemes under inexact information. Their Section 5 stability classification explicitly specializes to exact information and randomized time evaluation, with a different nonautonomous test equation; it does not give a Gaussian-random implicit denominator phase diagram.

Higham, Mao and Yuan (2007) characterize almost-sure and moment stability for numerical discretizations of Itô stochastic differential equations. Their stochastic theta method uses a deterministic drift term inside the implicit solve and Brownian increments as state forcing, rather than independently perturbing the implicit drift coefficient. This changes the multiplier law and its moment integrability. The general principle that independent logarithmic multipliers determine almost-sure stability is classical and is *not* claimed as new. The claimed contribution is the explicit unique minimum, universal critical constant, two-boundary reentrant phase classification, and simultaneous infinite integer moments for the stated Gaussian-coefficient implicit Euler model.

## Limitations

The Gaussian error is unbounded and can make a nominally positive decay coefficient negative; bounded, sign-preserving, correlated or differently distributed errors need not exhibit the same phase diagram. This is a model-specific stability benchmark, not a general theorem for stochastic differential equations, nonlinear systems, arbitrary implicit solvers, or finite-precision implementation. Near-pole events may cause immense transients even in almost-sure stable regimes. Numerical values are approximations of analytically defined constants; they are not interval-certified. Completeness of historical-priority searches cannot be proved, and an equivalent unindexed random-recurrence specialization remains possible. No independent mathematical validation has been performed.

## References

- Nathanael Bosch, *Stable and Scalable Probabilistic Numerical Solvers for Stiff and High-Dimensional ODEs*, arXiv:2606.08203, first submitted 2026-06-06. https://arxiv.org/abs/2606.08203
- Tomasz Bochacik and Paweł Przybyłowicz, *On the randomized Euler schemes for ODEs under inexact information*, arXiv:2104.15071, first submitted 2021-04-30, especially Section 5. https://arxiv.org/abs/2104.15071
- Desmond J. Higham, Xuerong Mao and Chenggui Yuan, *Almost sure and moment exponential stability in the numerical simulation of stochastic differential equations*, SIAM Journal on Numerical Analysis 45 (2007), 592–609, DOI:10.1137/060658138, especially Sections 2, 4 and 6. https://strathprints.strath.ac.uk/4547/
