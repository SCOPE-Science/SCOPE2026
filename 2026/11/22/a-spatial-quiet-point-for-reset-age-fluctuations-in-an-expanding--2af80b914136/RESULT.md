# A spatial quiet point for reset-age fluctuations in an expanding Thomas–Fermi condensate

## Finding

For the self-similarly expanding one-dimensional Thomas–Fermi profile under whole-cloud Poisson resetting, the *stationary run-to-run variance of the macroscopic local density* has an exactly characterized minimum over the original cloud support. At every reset rate this minimum occurs at two symmetric positions or at the two initial edges. The optimizing squared scaled position is

\[
y_*(r)=\min\!\left\{1,\frac{\operatorname{Cov}(U,U^3)}{\operatorname{Var}(U^3)}\right\},\qquad U=\lambda(T)^{-1},\quad T\sim\operatorname{Exp}(r),
\]

where \(\lambda\) is the expansion scale defined below. This is a unique minimum in the variable \(y=(x/x_0)^2\in[0,1]\); the two minimizing positions are \(x=\pm x_0\sqrt{y_*}\).

For any fixed initial edge \(x_0>0\) and trap frequency \(\omega>0\), there are two distinct resetting regimes:

\[
y_*(r)=1\quad\text{for all sufficiently small }r>0,
\]

and, as \(r/\omega\to\infty\),

\[
\boxed{\quad y_*(r)=\frac13+\frac{28}{5}\left(\frac\omega r\right)^2+O\!\left((\omega/r)^4\right).\quad}
\]

Writing \(\mathcal R(x)\) for the stationary random-age macroscopic density, the optimal variance satisfies the two sharp equivalents

\[
\boxed{\quad\min_{|x|\le x_0}\operatorname{Var}(\mathcal R(x))\sim
\frac{107}{280x_0^2}\frac r{\sqrt2\,\omega}\quad(r/\omega\downarrow0),\quad}
\]

\[
\boxed{\quad\min_{|x|\le x_0}\operatorname{Var}(\mathcal R(x))\sim
\frac{12069}{20x_0^2}\left(\frac\omega r\right)^8\quad(r/\omega\to\infty).\quad}
\]

For every *fixed* squared position \(y\in[0,1]\) different from \(1/3\), the corresponding rapid-reset variance instead obeys

\[
\operatorname{Var}(\mathcal R(x_0\sqrt y))\sim
\frac{45(1-3y)^2}{16x_0^2}\left(\frac\omega r\right)^4.
\]

Thus optimizing the observation position changes the leading rapid-reset noise order from \(r^{-4}\) to \(r^{-8}\), with a nonzero exact coefficient. The result concerns **macroscopic, reset-age-induced fluctuations**, not microscopic quantum connected correlations.

## Assumptions and scope

Let \(x_0,\omega,r>0\). Consider the normalized longitudinal Thomas–Fermi hydrodynamic density

\[
\rho(x,t)=\frac{3}{4x_0\lambda(t)}\left(1-\frac{x^2}{x_0^2\lambda(t)^2}\right)_+,
\]

where \(\lambda(0)=1\), \(\lambda'(0)=0\), and \(\lambda''(t)=\omega^2/\lambda(t)^2\) for \(t\ge0\). The entire profile is restored to its initial shape at independent Poisson events of rate \(r\). At a stationary observation time, the age since the last reset is \(T\sim\operatorname{Exp}(r)\), and \(\mathcal R(x)=\rho(x,T)\). Expectations and variances are taken solely over this age randomness. We optimize **only over the closed original support** \(|x|\le x_0\). Globally over the whole line the density variance tends to zero far away, so the restricted optimization is essential and physically tied to monitoring inside the original condensate.

The exact inversion of the deterministic expansion law is

\[
t(\lambda)=\frac{\sqrt{\lambda(\lambda-1)}+\operatorname{arsinh}\sqrt{\lambda-1}}{\sqrt2\,\omega},\qquad\lambda\ge1.
\]

The law of \(U=1/\lambda(T)\) is nondegenerate and has a positive density on \((0,1)\). Its moments are

\[
\mu_k=\mathbb E[U^k]=r\int_0^\infty e^{-rt}\lambda(t)^{-k}\,dt.
\]

For \(|x|\le x_0\), the positive-part cutoff is inactive for every age since \(\lambda(t)\ge1\). Setting \(y=(x/x_0)^2\) gives the identity

\[
\mathcal R(x)=\frac3{4x_0}(U-yU^3).
\]

No statement is made for finite-particle shot noise, nondeterministic evolution between resets, non-Poisson resetting, or unbounded-position optimization.

## Proof

**1. Exact quadratic optimization.** Since \(U\) has a continuous positive law on \((0,1)\), \(\operatorname{Var}(U^3)>0\). Also \(\operatorname{Cov}(U,U^3)>0\), by the strict covariance inequality for two increasing functions of a nondegenerate random variable. Therefore

\[
\operatorname{Var}(\mathcal R(x_0\sqrt y))
=\frac9{16x_0^2}\bigl[\operatorname{Var}(U)-2y\operatorname{Cov}(U,U^3)+y^2\operatorname{Var}(U^3)\bigr].
\]

This quadratic is strictly convex for \(y\in[0,1]\); projecting its unconstrained minimizer onto this interval gives the formula for \(y_*\). In terms of the moments, the ratio is \((\mu_4-\mu_1\mu_3)/(\mu_6-\mu_3^2)\).

The already-known *central-to-local covariance-zero front* on the same original support, when present there, is situated at \(y_c=\operatorname{Var}(U)/\operatorname{Cov}(U,U^3)\). Strict Cauchy–Schwarz implies

\[
\frac{\operatorname{Cov}(U,U^3)}{\operatorname{Var}(U^3)}
<\frac{\operatorname{Var}(U)}{\operatorname{Cov}(U,U^3)},
\]

since \(U^3\) is not an affine function of \(U\) on \((0,1)\). Hence whenever both points lie in the initial support, the noise-minimizing point is strictly closer to the center than the previously studied covariance sign front. The exact optimizer is not determined by that previous front law.

**2. Slow resetting.** As \(t\to\infty\), \(\lambda(t)\sim\sqrt2\,\omega t\). For any \(k>1\), dominated convergence gives

\[
\frac{\mu_k}{r}\longrightarrow
\int_0^\infty\lambda(t)^{-k}\,dt
=\frac{B(k-1,1/2)}{\sqrt2\,\omega}.
\]

Here the beta integral follows by changing variables to \(\lambda\) and using \(dt/d\lambda=\sqrt{\lambda/(\lambda-1)}/(\sqrt2\,\omega)\). Moreover \(\mu_1=O(r\log(1/r))\), and \(\mu_3=O(r)\), so \(\mu_1\mu_3=o(r)\) and \(\mu_3^2=o(r)\). Thus

\[
\frac{\operatorname{Cov}(U,U^3)}{\operatorname{Var}(U^3)}
\longrightarrow\frac{B(3,1/2)}{B(5,1/2)}=\frac{21}{16}>1.
\]

By continuity in \(r\), the constrained minimum is exactly at \(y_*=1\) for all sufficiently small positive rates. There the raw variance is \(\operatorname{Var}(U-U^3)\). The mean-squared term is \(o(r)\), while the second moment divided by \(r\) tends to

\[
\frac{B(1,1/2)-2B(3,1/2)+B(5,1/2)}{\sqrt2\,\omega}
=\frac{214}{315\sqrt2\,\omega}.
\]

Multiplying by \(9/(16x_0^2)\) gives the stated edge-variance coefficient \(107/(280x_0^2)\).

**3. Rapid resetting and optimal-order cancellation.** Write \(h=\omega/r\) and \(Y=rT\sim\operatorname{Exp}(1)\). The Taylor expansion of the ODE solution and its reciprocal gives

\[
U=1-\tfrac12 h^2Y^2+\tfrac13h^4Y^4+O(h^6Y^6),
\quad U^3=1-\tfrac32h^2Y^2+\tfrac74h^4Y^4+O(h^6Y^6).
\]

These expansions may be passed through the required moments: truncate to \(Y\le h^{-\varepsilon}\) for small fixed \(\varepsilon>0\), use the uniform analytic Taylor remainder there, and use the exponentially small tail of \(Y\), together with \(0<U\le1\), outside. The result gives moment errors of the displayed orders, sufficient for the variance and covariance expansions.

Let \(A=Y^2\) and \(B=Y^4\). From the exponential moments \(\mathbb E[Y^k]=k!\),

\[
\operatorname{Var}(A)=20,\qquad\operatorname{Cov}(A,B)=672,
\qquad\operatorname{Var}(B)=39744.
\]

Expanding the exact quotient from Step 1 through the first correction yields

\[
\frac{\operatorname{Cov}(U,U^3)}{\operatorname{Var}(U^3)}
=\frac13+\frac{\operatorname{Cov}(A,B)}{6\operatorname{Var}(A)}h^2+O(h^4)
=\frac13+\frac{28}{5}h^2+O(h^4).
\]

This lies strictly between zero and one for sufficiently small \(h>0\). Set \(y_*=1/3+\delta h^2+O(h^4)\), where \(\delta=28/5\). Then

\[
U-y_*U^3=\frac23-\delta h^2+
 h^4\left(\frac{3\delta}{2}A-\frac14B\right)+O_{L^2}(h^6).
\]

The deterministic terms do not contribute to variance. Since \(\delta=\operatorname{Cov}(A,B)/(6\operatorname{Var}(A))\), the residual random coefficient has variance

\[
\operatorname{Var}\left(\frac{3\delta}{2}A-\frac14B\right)
=\frac1{16}\left(\operatorname{Var}(B)-\frac{\operatorname{Cov}(A,B)^2}{\operatorname{Var}(A)}\right).
\]

Multiplication by \(9/(16x_0^2)\) gives \(12069/(20x_0^2)\), strictly positive by non-affine dependence of \(Y^4\) on \(Y^2\). Hence the optimized variance is asymptotic to that coefficient times \(h^8\). For any fixed \(y\ne1/3\), the uncancelled \(h^2(3y-1)A/2\) fluctuation gives \(45(1-3y)^2h^4/(16x_0^2)\). This completes the exact and asymptotic claims.

## Verification

The standalone `check.py` independently integrates the reset-age law using the change of variables \(\lambda=1+s^2\); it also evaluates local variance by a separate centered-profile integral. It checks symbolic beta integral identities and exponential-moment coefficients, strict numerical convex minimizers across nine resetting rates, low-rate edge equivalents and the high-rate optimized \(r^{-8}\) coefficient by independent arbitrary-precision quadrature. Execute `python check.py` with dependencies in `requirements.txt`. These finite computations support the algebra and numerical normalization, but the preceding analytic arguments prove the universal assertions; no finite numerical check proves a limit.

## Relationship to prior work

Mesquita, Kulkarni, Majumdar and Sabhapandit [1] establish the expansion law, exact random expansion-scale distribution, stationary **mean** density, edge statistics and full counting statistics. Those underlying results are fully credited. Their main text and appendices do not give the core-restricted minimum of **run-to-run pointwise density variance** or its sharp \(r^{-8}\) law. The separate published result [2] gives a unique sign front for covariance between the central density and a local density, with two extreme-rate front locations. The front can be described using \(\operatorname{Var}(U)/\operatorname{Cov}(U,U^3)\), while the present quiet-point minimizer uses the inequivalent quotient \(\operatorname{Cov}(U,U^3)/\operatorname{Var}(U^3)\). Strict Cauchy–Schwarz distinguishes their implications, and neither [1] nor [2] supplies the exact optimizing variance coefficients. The related renewal-reset condensate work [3] studies a non-Poisson clock and large-scale edge laws, not this Poisson core variance problem.

## Limitations

All assertions are within the one-dimensional, large-particle-number, Thomas–Fermi mean-field expansion model of [1]. Variance is solely over the stationary reset age, not over quantum or particle-number measurement noise. The minimization is over the original cloud support, not all positions; far outside, variance vanishes asymptotically. There is no assertion that the edge-to-interior change occurs at a *unique* reset rate or that the optimizing position changes monotonically with rate. No finite-\(N\) correction, experimental detectability estimate, imperfect reset model or generalization to other profile shapes is proved. Originality is assessed against inspected primary and accessible indexed results, not guaranteed against all unpublished or unindexed equivalents.

## References

[1] N. Mesquita, M. Kulkarni, S. N. Majumdar and S. Sabhapandit, *Weakly interacting Bose-Einstein condensate with stochastic resetting*, arXiv:2609.37110v1, first publicly available 2026-09-29, https://arxiv.org/abs/2609.37110 , full text https://pdfs.assets.alphaxiv.org/2609.37110v1.pdf .

[2] *A unique spatial anticorrelation front in a reset-expanding Thomas–Fermi condensate* (2026), public record https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-unique-spatial-anticorrelation-front-in-a-reset-expanding-thom--a02b45fafe32 .

[3] *Pareto renewal resetting of an expanding Thomas–Fermi condensate: algebraic tails and two aging limits* (2026), public record https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-pareto-renewal-resetting-of-an-expanding-thomas-fermi-condensate--bc4c6f0acef0 .
