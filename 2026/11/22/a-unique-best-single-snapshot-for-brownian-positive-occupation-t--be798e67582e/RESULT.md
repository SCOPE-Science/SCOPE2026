# A unique best single snapshot for Brownian positive occupation time

## Finding

Let \(B=(B_t)_{0\le t\le1}\) be standard Brownian motion starting at zero and let
\[
Q=\int_0^1\mathbf 1_{\{B_t>0\}}\,dt.
\]
For each deterministic \(x\in(0,1]\), observe exactly one noiseless real state \(B_x\), and use the conditional-mean estimator \(\widehat Q_x=\mathbb E[Q\mid B_x]\). Among all deterministic \(x\in[0,1]\), **the unique global minimizer** of \(\mathbb E[(Q-\widehat Q_x)^2]\) is \(x_*=e^{-r_*}\), where \(r_*>0\) is the unique solution of
\[
H(2r_*)-2H(r_*)=\frac\pi4(2\log 2-1),\qquad
H(r)=2\left(\sqrt{e^r-1}-\arctan\sqrt{e^r-1}\right).
\]
Numerically,
\[
x_*=0.58958511090724239247\ldots,\quad
\min_x\mathbb E[(Q-\widehat Q_x)^2]
=0.02553546323245417006\ldots.
\]
The optimal snapshot explains \(79.5716294140\ldots\%\) of \(\operatorname{Var}(Q)=1/8\). The terminal snapshot \(B_1\) explains \(2(1-\log2)\approx61.37056388\%\); its captured variance is exactly \((1-\log 2)/4\). These percentages concern Bayes mean-square reduction for the **occupation-time functional**, not pointwise recovery of the entire path.

## Assumptions and scope

The Brownian law, time horizon, sign threshold, and observation time are known. There is precisely one noiseless real-valued point observation (not just its sign). Observation times must be selected in advance independently of the path. Arbitrary square-integrable estimators measurable with respect to that observation are allowed; the conditional mean is optimal for squared error. At \(x=0\), \(B_0=0\) provides no information. The target uses ordinary Lebesgue time and the strict sign convention; Brownian zero-level times have zero Lebesgue measure almost surely. All risks below are unconditional over the Brownian law.

For reproducibility, set \(C=\pi(2\log2-1)/4\), and define for \(0\le x\le1\)
\[
\begin{aligned}
A(x)&=\tfrac32x\sqrt{1-x^2}+\tfrac12\arcsin x-x^2\arccos x,\\
D(x)&=\tfrac14\arcsin\sqrt{x}-2x^2\arccos\sqrt{x}
   +\tfrac{10x-1}{4}\sqrt{x(1-x)}.
\end{aligned}
\]
The exact captured variance \(V(x)=\operatorname{Var}(\widehat Q_x)\) is
\[
V(x)=\frac{A(x)-D(x)-Cx^2/2}{\pi}.
\]
The resulting squared-error risk is \(1/8-V(x)\) for every \(x\in[0,1]\), with \(V(0)=0\).

## Proof

**1. Gaussian sign conditioning and information kernel.** For \(x>0\) write \(Z=B_x/\sqrt{x}\), so \(Z\sim N(0,1)\). The standardized correlation between \(B_t\) and \(Z\) is
\[
\rho_x(t)=\frac{\min(t,x)}{\sqrt{tx}},\qquad t>0.
\]
Given \(Z=z\), \(B_t\) is normal with mean \(\rho_x(t)\sqrt t\,z\) and variance \(t(1-\rho_x(t)^2)\). Consequently
\[
\widehat Q_x(z)=\int_0^1
\Phi\left(\frac{\rho_x(t)z}{\sqrt{1-\rho_x(t)^2}}\right)dt,
\]
where the integrand at \(t=x\) is interpreted as \(\mathbf1_{\{z>0\}}\). This is a valid bounded conditional expectation.

The Gaussian sign/orthant identity says that if two standard jointly normal variables have correlation \(q\), their positive-sign indicator covariance equals \(\arcsin(q)/(2\pi)\). Conditional on a shared standard normal \(Z\), independent residual copies of \(B_s\) and \(B_t\) have unconditional correlation \(\rho_x(s)\rho_x(t)\). By the tower property and the orthant identity,
\[
V(x)=\frac1{2\pi}\int_0^1\int_0^1
\arcsin(\rho_x(s)\rho_x(t))\,ds\,dt.\tag{1}
\]
This is an exact identity, not a finite-grid approximation. The arcsine law for Brownian occupation time yields \(\operatorname{Var}(Q)=1/8\).

**2. Log-time transformation.** Let \(x=e^{-r}\), \(s=e^{-u}\), \(t=e^{-v}\), where \(r,u,v\ge0\). Then \(ds\,dt=e^{-u-v}du\,dv\) and \(\rho_x(e^{-u})=e^{-|u-r|/2}\). Put \(F(w)=\arcsin(e^{-w/2})\). Equation (1) becomes
\[
V(e^{-r})=\frac1{2\pi}\int_0^\infty\int_0^\infty
 e^{-u-v}F(|u-r|+|v-r|)\,du\,dv.\tag{2}
\]
For \(w>0\), \(-F'(w)=1/(2\sqrt{e^w-1})\); its integrable singularity at zero justifies differentiation under the integral by a local dominated-convergence argument (the two-dimensional singularity is integrable). On the two cross rectangles \(u<r<v\) and \(v<r<u\), the sum of absolute values is \(|u-v|\) and does not vary with \(r\). Differentiation on the remaining two squares, followed by translation, gives
\[
\frac{d}{dr}V(e^{-r})=\frac{e^{-2r}}\pi\bigl(C-G(r)\bigr),\tag{3}
\]
where
\[
\begin{aligned}
C&=\frac12\int_0^\infty\frac{w e^{-w}}{\sqrt{e^w-1}}dw,\\
G(r)&=\frac12\int_0^r\int_0^r
\frac{e^{a+b}}{\sqrt{e^{a+b}-1}}da\,db.
\end{aligned}
\]
By \(y=e^{-w}\), the beta-integral derivative evaluates
\[
C=\tfrac12\int_0^1(-\log y)\sqrt{\tfrac{y}{1-y}}\,dy
 =\frac\pi4(2\log2-1)>0.
\]
Set \(H(r)=\int_0^r\sqrt{e^s-1}\,ds\), which has the elementary form stated in the Finding. Since \(dH/ds=\sqrt{e^s-1}\), integrating the two triangular slices of the square \([0,r]^2\) by parts yields \(G(r)=H(2r)-2H(r)\).

**3. A strict global sign change.** The function \(G\) is continuous, \(G(0)=0\), and
\[
G'(r)=2\bigl(\sqrt{e^{2r}-1}-\sqrt{e^r-1}\bigr)>0
\quad(r>0).
\]
Moreover, \(G(r)\to\infty\) as \(r\to\infty\). Equation \(G(r)=C\) therefore has exactly one positive solution \(r_*\). By (3), \(V(e^{-r})\) increases strictly for \(0\le r<r_*\) and decreases strictly for \(r>r_*\). Also \(V(0)=0\), by (1) and bounded convergence, while \(V(1)>0\). Thus \(x_*=e^{-r_*}\) is the **unique** maximizer of captured variance on the full closed observation interval. Orthogonal projection in \(L^2\) gives \(\mathbb E[(Q-\widehat Q_x)^2]=\operatorname{Var}(Q)-V(x)\), proving the minimax statement among estimators based on the selected snapshot.

**4. Closed captured-variance formula.** Equation (3), combined with \(V(e^{-r})\to0\) at \(r\to\infty\), gives
\[
V(x)=\pi^{-1}\left(2\int_0^x[\sqrt{1-s^2}-s\arccos s]ds
 -4\int_0^x[\sqrt{s(1-s)}-s\arccos\sqrt{s}]ds
 -Cx^2/2\right).
\]
Elementary antiderivatives are exactly \(A(x)\) and \(D(x)\) in Assumptions and scope, proving their formula. At \(x=1\), it simplifies to \(V(1)=(1-\log2)/4\). Numerical constants follow from evaluating this formula and the monotone equation; they are not prerequisites for the proof of uniqueness.

## Verification

Run `python verify.py` after installing the dependency listed in `requirements.txt`. It independently compares the integral representation with the closed formula and the convergent arcsine series, verifies symbolic derivative identities at high precision, locates the unique root with bracketing, and checks the stated numerical risks. Supplementary finite-grid scans are diagnostic only; the all-time uniqueness proof is the monotone derivative equation, not a scan. The source code and dependencies are supplied within this finding.

A separately useful exact series is
\[
V(x)=\frac1{2\pi}\sum_{n=0}^\infty
\frac{\binom{2n}{n}}{4^n(2n+1)}a_n(x)^2,
\]
where \(a_0(x)=2\sqrt{x}-4x/3\) and for \(n\ge1\),
\[
a_n(x)=\frac{x}{n+3/2}+\frac{x-x^{n+1/2}}{n-1/2}.
\]
For \(N\ge2\), truncating before index \(N\) has absolute error at most
\[
\frac1\pi\left(\frac1{(N-1/2)^3}+\frac1{2(N-1/2)^2}\right),
\]
using \(\binom{2n}{n}/4^n\le1\), \(a_n(x)\le2/(n-1/2)\), and a decreasing-series integral bound. This is a conservative rigorous all-\(x\in[0,1]\) tail certificate.

## Relationship to prior work

Brownian sign occupation obeys the classical Lévy arcsine law. Altmeyer (2017) studies strong approximation and bounds for occupation functionals from high-frequency regular grids. Ivanovs and Podolskij (2020), especially Section 3 and Appendix B, derive conditional-mean occupation estimators and asymptotics from fixed dense grids. Altmeyer and Le Guével (2021), Sections 1–3, study asymptotic lower errors on regular grids for stable processes. Cui and Chronopoulou (2023), Section 3, optimize sparse observation times for *pathwise state reconstruction*, not the nonlinear sign-occupation integral. None of these inspected results states the unique best one-shot time or the above global Bayes-risk identity as an optimization result.

Related published claims on Brownian positive-sojourn/end-point covariance concern a linear covariance, rather than the variance of the **conditional occupation-time expectation** as the time moves. Claims on randomized fractional-Brownian occupation quadrature concern sampling the sign integrand at many random time points, not observing one real Brownian state to reconstruct the whole positive occupation duration. This distinction is mathematical, not merely terminological. An equivalent one-shot design theorem in less easily indexed older work remains a publication-priority uncertainty.

## Limitations

The theorem does not optimize noisy, adaptive, random-time, sign-only, or multi-snapshot sensing; nor does it apply automatically to other stochastic processes, nonzero thresholds, weighted occupation functionals, or unknown drift. Its analytic uniqueness proof is specific to the logarithmic-time exponential covariance of **zero-start Brownian motion** and to this positive-sign target. Exact publication priority has not been independently established. The decimal expansions are numerical evaluations of exact formulas, not independently validated constants.

## References

- R. Altmeyer, *Approximation of occupation time functionals*, first public 2017-06-11, https://arxiv.org/abs/1706.03418.
- J. Ivanovs and M. Podolskij, *Optimal estimation of some random quantities of a Lévy process*, first public 2020-01-08, https://arxiv.org/abs/2001.02517.
- R. Altmeyer and R. Le Guével, *Optimal \(L^2\)-approximation of occupation and local times for symmetric stable processes*, first public 2021-08-26, https://arxiv.org/abs/2108.11632.
- X. Cui and A. Chronopoulou, *Optimal Sampling for Estimation of Fractional Brownian Motion*, first public 2023-04-16, https://arxiv.org/abs/2304.07661.
- P. Lévy, classical arcsine laws for Brownian occupation time; these are background, not a claim of new arcsine probabilities.
