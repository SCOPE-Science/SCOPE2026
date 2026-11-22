# Strict anticorrelation of opposite Brownian first-passage clocks under Poisson resetting

## Finding

Consider one Brownian trajectory on the entire real line, initially at the origin, with generator \(D\partial_{xx}\), where \(D>0\). At the times of an independent rate-\(r\) Poisson process, \(r>0\), the trajectory is instantaneously returned to the origin. For arbitrary \(a,b>0\), let \(T_-\) and \(T_+\) be the **first respective visit times** to \(-a\) and \(+b\), measured along this same trajectory. Crucially, reaching either level does not kill or restart the trajectory, and the other first-visit clock continues to run.

Put \(A=a\sqrt{r/D}\) and \(B=b\sqrt{r/D}\). Then the covariance is exactly

\[
\boxed{\operatorname{Cov}(T_-,T_+)=-\frac{A+B}{r^2}\frac{\sinh A\,\sinh B}{\sinh A+\sinh B}<0.}
\]

Thus the two potentially very long first-passage times are **strictly anticorrelated for every choice of positive parameters**, even though they arise from a single particle driven by a shared reset clock. Their mixed second moment is

\[
\mathbb E[T_-T_+]=\frac{(e^A-1)(e^B-1)}{r^2}-\frac{A+B}{r^2}\frac{\sinh A\,\sinh B}{\sinh A+\sinh B}.
\]

The leading weak-resetting terms cancel: at fixed \(a,b,D\), as \(r\downarrow0\),

\[
\mathbb E[T_-T_+]\sim\frac{ab(a+b)}{2D^{3/2}\sqrt r},\qquad
\mathbb E[T_-]\mathbb E[T_+]\sim\frac{ab}{Dr},\qquad
\operatorname{Cov}(T_-,T_+)\sim-\frac{ab}{Dr}.
\]

In particular the positive mixed second moment diverges as \(r^{-1/2}\), rather than at the \(r^{-1}\) scale of the product of the means. The entire two-clock law is determined by the joint Laplace transform in the proof.

## Assumptions and scope

The path is continuous between jumps, each reset sends it to exactly zero, and the reset clock is independent of its Brownian increments. The two opposite levels are fixed and finite, with strict inequalities \(a,b,D,r>0\). At a first visit, no extra event is imposed: the same continuous-time Markov path continues, allowing the opposite target to be reached subsequently. Both first visits occur almost surely and possess all moments because each finite reset interval has a strictly positive chance of reaching any fixed level and Poisson restart cycles have exponentially integrable durations in a sufficiently small neighborhood of zero.

The result does not concern a particle killed at whichever target is reached first, nor a protocol that forces an additional reset upon first discovery. In those processes the paired clocks have a different meaning or law.

## Proof

**1. Split at the first of the two visits.** Let \(\tau=\min(T_-,T_+)\) and \(I\in\{-,+\}\) identify the first visited level (simultaneous first visits have probability zero). For \(s\ge0\) set

\[
\lambda_s=\sqrt{\frac{r+s}{D}},\qquad
f_+(s)=\frac{\sinh(a\lambda_s)}{\sinh((a+b)\lambda_s)},\qquad
f_-(s)=\frac{\sinh(b\lambda_s)}{\sinh((a+b)\lambda_s)}.
\]

For a non-reset Brownian excursion started at zero and stopped on leaving \((-a,b)\), the two functions \(f_\pm(s)\) equal the exponentially discounted probabilities of exiting by the indicated level with killing rate \(r+s\). They solve the ordinary differential equation \(D u''=(r+s)u\) with the appropriate boundary values \(0\) and \(1\).

**2. Obtain the exit-side transforms under resetting.** A cycle either exits before the first reset, with discounted probabilities \(f_\pm(s)\), or resets without exiting and restarts at zero. The Laplace transform of a failed cycle is \(r(1-f_+(s)-f_-(s))/(r+s)\). Summing the resulting geometric renewal series gives

\[
G_\pm(s):=\mathbb E[e^{-s\tau};I=\pm]
=\frac{(r+s)f_\pm(s)}{s+r(f_+(s)+f_-(s))}.
\]

Write \(u=f_+(0)+f_-(0)\), \(u'=f_+'(0)+f_-'(0)\). Differentiating the total and side-specific transforms at zero yields the exact identities

\[
\mathbb E[\tau^2]=\frac{2(1-u+r u')}{r^2u^2},\qquad
\mathbb E[\tau\mathbf1_{\{I=\pm\}}]
=\frac{f_\pm(0)(1+r u')-u(f_\pm(0)+r f_\pm'(0))}{r u^2}.
\]

Here primes denote derivatives in \(s\), so these formulas are dimensionally correct. The first is obtained by differentiating \(G_++G_-\) twice; the second by differentiating \(G_\pm\) once with a minus sign.

**3. Continue after the first visit.** Upon first reaching \(+b\), the remaining clock for \(-a\) is a fresh Markov process started from \(+b\), with the original resets to zero. Its mean is

\[
m_{-|+}=\frac{1-e^{-(a+b)\sqrt{r/D}}}{r e^{-a\sqrt{r/D}}}
=\frac{e^A-e^{-B}}r.
\]

Similarly, when \(-a\) is visited first,

\[
m_{+|-}=\frac{e^B-e^{-A}}r.
\]

These are obtained from the non-reset discounted one-sided hitting transform \(e^{-d\sqrt{(r+s)/D}}\) and a renewal equation with initial displacement \(a+b\) and subsequent reset distances \(a\) or \(b\). The strong Markov property gives

\[
\mathbb E[T_-T_+]
=\mathbb E[\tau^2]
+m_{-|+}\,\mathbb E[\tau\mathbf1_{\{I=+\}}]
+m_{+|-}\,\mathbb E[\tau\mathbf1_{\{I=-\}}].
\]

The one-sided resetting renewal also gives the exact marginal means

\[
\mathbb E[T_-]=\frac{e^A-1}{r},\qquad
\mathbb E[T_+]=\frac{e^B-1}{r}.
\]

Substitute the explicit hyperbolic functions from step 1 into these equations. To verify the only nontrivial algebraic reduction without hiding a sign, put \(x=e^A\), \(y=e^B\), and represent differentiation with respect to \(s\) at zero by \((Ax\partial_x+By\partial_y)/(2r)\). Then

\[
u=\frac{x+y}{xy+1},\qquad
r^2\bigl(\mathbb E[T_-T_+]-\mathbb E[T_-]\mathbb E[T_+]\bigr)
=-\frac{(A+B)(x^2-1)(y^2-1)}{2(x+y)(xy-1)}.
\]

The right side is exactly \(-(A+B)\sinh A\sinh B/(\sinh A+\sinh B)\). Every factor in its denominator and every omitted positive factor is strictly positive for \(A,B>0\), proving strict negativity.

**4. Complete joint transform.** The preceding decomposition also yields the two-dimensional Laplace transform for arbitrary \(s,t\ge0\):

\[
\begin{aligned}
\mathbb E[e^{-sT_+-tT_-}]
&=G_+(s+t)H_-(t)+G_-(s+t)H_+(s),\\
H_-(t)&=\frac{t e^{-(a+b)\lambda_t}+r e^{-a\lambda_t}}{t+r e^{-a\lambda_t}},\\
H_+(s)&=\frac{s e^{-(a+b)\lambda_s}+r e^{-b\lambda_s}}{s+r e^{-b\lambda_s}}.
\end{aligned}
\]

Indeed \(G_+\) discounts the time to the first right-side visit, after which \(H_-\) discounts the independent remaining left-side search; the other term is analogous. At the origin, the transform is one; differentiation recovers the cross moment in step 3.

**5. Weak-reset singularity.** Put \(h=\sqrt{r/D}\), so \(A=ah\), \(B=bh\). Expanding \(e^z-1=z+z^2/2+O(z^3)\) and \(\sinh z=z+z^3/6+O(z^5)\), the numerator in the mixed-moment identity satisfies

\[
(e^{ah}-1)(e^{bh}-1)-(a+b)h\frac{\sinh(ah)\sinh(bh)}{\sinh(ah)+\sinh(bh)}
=\frac{ab(a+b)}2 h^3+O(h^4).
\]

Division by \(r^2=D^2h^4\) proves the stated \(r^{-1/2}\) mixed-moment asymptotic. The separate mean-product and covariance expansions follow at order \(h^2\).

## Verification

Run `python check.py` using Python with `sympy`, `mpmath`, `numpy` and `scipy`. The script checks the rational identity of the cross moment by exact symbolic elimination, the weak-reset limit by a symbolic limit, six high-precision mixed derivatives of the independent two-variable transform, four independent one-sided variance derivatives, and three finite-lattice continuous-time generator approximations. The lattice approximations at mesh sizes \(1/8\), \(1/16\), \(1/32\) converge toward the same covariance, but those finite checks are **not** used as proof of the continuum statement. The symbolic derivation and the Markov/renewal arguments establish the theorem for all allowed parameters.

For completeness, the one-sided variances are

\[
\operatorname{Var}(T_-)=\frac{e^{2A}-Ae^A-1}{r^2},\qquad
\operatorname{Var}(T_+)=\frac{e^{2B}-Be^B-1}{r^2}.
\]

Both are strictly positive, and the Pearson correlation is strictly negative. As \(r\downarrow0\) it behaves as \(-\sqrt{ab}\sqrt{r/D}\), while for \(r\to\infty\) it also tends to zero. These limits do not assert a unique correlation optimum.

## Relationship to prior work

Linn and Lawley (first public arXiv version, June 17, 2024) evaluate the **mean** Brownian cover time for an interval with Poisson resetting, including asymmetric endpoints, and obtain frequent-resetting asymptotics. Their relevant first-version full-text section 2.1 is a close source for the *same moving particle and persistent coverage* but provides neither the two individual first-visit clocks' joint Laplace transform nor their exact covariance or the weak-reset mixed-moment cancellation.

Pal and Prasad (arXiv 2018, later publication) derive the first-exit survival and exit-side transforms for a particle **killed at the first encountered endpoint**. These first-stage formulas are used in the proof, but killed first exit is not the paired, continuing first-visit process and does not imply the displayed joint law without a further Markov decomposition.

Calvert and Evans (European Physical Journal B 2021) study search for two target locations in a related protocol that **forcibly restarts at the origin when the first target is found**, whereas the present trajectory receives no special intervention at that hit. Their main results concern mean completion times, not the cross moment of the two continuing clocks. Wang and Chen (arXiv 2025) examine correlations among occupation, maximum, and last-return times over fixed horizons rather than the opposite fixed-level first-passage times considered here.

A related previously published result on the variance of cover time on a *reflecting* interval concerns a different boundary protocol and does not supply a covariance between the two full-line first-visit clocks. These distinctions establish best-knowledge noncoverage, not mathematical proof of worldwide publication priority.

## Limitations

The exact identity depends on one-dimensional Brownian paths, Poissonian complete returns to the initial point, and a reset site strictly between the targets. It is not claimed for non-Poisson restart clocks, nonlocal motion, drift, random reset locations, exterior reset positions, or path killing at either first visit. Strict negativity is a covariance statement; **negative quadrant dependence, independence of reset cycles across endpoints, and a global optimal reset rate are not claimed**. The proof is analytic and self-contained modulo standard Brownian hitting-transform and strong Markov facts; no independent scientific validation or external certification is represented. Priority remains uncertain with respect to specialized unindexed multi-target renewal literature.

## References

1. S. Linn and S. D. Lawley, *Cover times with stochastic resetting*, arXiv:2406.12154, first posted 2024-06-17, especially version 1, Section 2.1, https://arxiv.org/abs/2406.12154.
2. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009, first posted 2018-12-07, Sections II–IV, https://arxiv.org/abs/1812.03009.
3. G. R. Calvert and M. R. Evans, *Searching for clusters of targets under stochastic resetting*, European Physical Journal B 94, 228 (2021), https://doi.org/10.1140/epjb/s10051-021-00238-0.
4. Y. Wang and H. Chen, *Pairwise correlations of global times in one-dimensional Brownian motion under stochastic resetting*, arXiv:2508.11387, 2025, https://arxiv.org/abs/2508.11387.
