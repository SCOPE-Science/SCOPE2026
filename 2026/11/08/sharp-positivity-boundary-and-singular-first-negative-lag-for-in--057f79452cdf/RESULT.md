# Sharp positivity boundary and singular first negative lag for inertial active-trap correlations

## Finding

A harmonically confined inertial particle, driven by exponentially persistent active forcing without an additional independent white-noise bath, can retain *strictly positive stationary positional autocovariance at every lag* even when its mechanical response is underdamped. The precise dividing line is that the forcing-correlation decay rate equal the oscillator's damping rate. Just beyond the dividing line, negative correlations occur only after a singularly long delay.

**Theorem.** Let \(\alpha,\Omega,\lambda,\sigma^2>0\). Suppose a stationary, mean-zero, second-order forcing \(\eta\) has covariance \(\mathbb E[\eta(t)\eta(s)]=\sigma^2 e^{-\lambda|t-s|}\). Define the stationary linear-response solution to
\[
\ddot X(t)+2\alpha\dot X(t)+\Omega^2 X(t)=\eta(t),
\]
with no additional thermal/white noise, and put \(C_\lambda(t)=\mathbb E[X(t)X(0)]\). Then, for every finite \(t\ge0\),
\[
C_\lambda(t)>0\quad\text{for all such }t
\quad\Longleftrightarrow\quad
(\Omega\le\alpha)\ \text{or}\ (\lambda\le\alpha).
\]
If \(\Omega>\alpha\) and \(\lambda>\alpha\), there are infinitely many strictly positive and strictly negative lag intervals. If \(\Omega>\alpha\), define \(t_-(\lambda)=\inf\{t>0:C_\lambda(t)<0\}\) for \(\lambda>\alpha\). Then
\[
\lim_{\lambda\downarrow\alpha}(\lambda-\alpha)t_-(\lambda)
=\log\frac{2\Omega}{\sqrt{\Omega^2+3\alpha^2}}>0.
\]
In particular, the boundary \(\lambda=\alpha\) has *no* negative lags, although arbitrary nearby values on the \(\lambda>\alpha\) side eventually do.

## Assumptions and scope

The force is stationary and has the stated two-time covariance; Gaussianity, independence of increments, and a Markov-property assumption are **not** required. The stable oscillator defines a unique mean-square stationary response by convolution with its causal Green function. Time is continuous. The claim addresses the covariance of one Cartesian position coordinate, not a normalized finite-time displacement distribution or velocity autocorrelation. The strict all-lag result concerns finite lags, with \(C_\lambda(t)\to0\) as \(t\to\infty\). The assumptions exclude any independent white noise in the positional acceleration: such an additional term has its own oscillating autocorrelation and generally changes the sign classification.

In particular, a Cartesian component of a stationary isotropic active Brownian force in dimension \(d\ge2\) has this covariance with \(\lambda=(d-1)D_r\) and \(\sigma^2=F^2/d\), where \(D_r\) is rotational diffusivity and \(F\) the force magnitude. An active Ornstein--Uhlenbeck force with the same covariance gives precisely the same second-order result.

## Proof

**1. Stationary linear-filter covariance.** Set \(Y=\dot X\), and define
\[
U=\mathbb E[X(0)\eta(0)],\qquad
V=\mathbb E[X(0)^2],\qquad
W=\mathbb E[Y(0)\eta(0)].
\]
Because the response is causal and the input autocovariance is exponential, the time-convolution representation gives \(\mathbb E[\eta(t)X(0)]=Ue^{-\lambda t}\) for \(t\ge0\). The same representation, or stationary mean-square moment balance, yields
\[
U=\frac{\sigma^2}{\Omega^2+\lambda(\lambda+2\alpha)},\quad
W=\lambda U,\quad
\mathbb E[Y^2]=\frac{\lambda U}{2\alpha},\quad
V=\frac{U}{\Omega^2}\left(1+\frac{\lambda}{2\alpha}\right),\quad
\mathbb E[XY]=0.
\]
Thus \(C_\lambda(0)=V\), \(C_\lambda'(0)=0\), and
\[
C_\lambda''(t)+2\alpha C_\lambda'(t)+\Omega^2C_\lambda(t)=Ue^{-\lambda t}\qquad(t>0).
\]

**2. Positivity without mechanical oscillations.** If \(\Omega<\alpha\), the causal Green function is
\[
g(s)=\mathbf 1_{\{s\ge0\}}e^{-\alpha s}
\frac{\sinh(\sqrt{\alpha^2-\Omega^2}\,s)}{\sqrt{\alpha^2-\Omega^2}},
\]
and when \(\Omega=\alpha\), it is \(g(s)=\mathbf 1_{\{s\ge0\}}s e^{-\alpha s}\). In either case \(g(s)>0\) for \(s>0\). Accordingly
\[
C_\lambda(t)=\sigma^2\int_0^\infty\!\!\int_0^\infty
g(s)g(u)e^{-\lambda|t-s+u|}\,ds\,du>0
\]
for every finite \(t\), proving the assertion whenever \(\Omega\le\alpha\).

**3. The underdamped boundary.** Assume \(\Omega>\alpha\) and write \(\omega=\sqrt{\Omega^2-\alpha^2}>0\). The unique solution to the covariance initial-value problem is
\[
C_\lambda(t)=A_\lambda e^{-\lambda t}+e^{-\alpha t}
\bigl(B_\lambda\cos(\omega t)+H_\lambda\sin(\omega t)\bigr),
\]
where
\[
A_\lambda=\frac{U}{\Omega^2+\lambda(\lambda-2\alpha)}>0,\quad
B_\lambda=V-A_\lambda,\quad
H_\lambda=\frac{\alpha B_\lambda+\lambda A_\lambda}{\omega}.
\]
All denominators are positive because \(\Omega^2+\lambda(\lambda-2\alpha)=(\lambda-\alpha)^2+\omega^2>0\). At \(\lambda=\alpha\), put \(R_\alpha=\sqrt{B_\alpha^2+H_\alpha^2}\). Direct substitution and simplification give
\[
\frac{R_\alpha^2}{A_\alpha^2}=
\frac{\Omega^2+3\alpha^2}{4\Omega^2}<1.
\]
Consequently \(C_\alpha(t)\ge e^{-\alpha t}(A_\alpha-R_\alpha)>0\) at every finite lag.

**4. Positivity for all slower force-decay rates.** The two-sided Fourier transform of the covariance is the nonnegative spectrum
\[
S_\lambda(\xi)=\frac{2\sigma^2\lambda}
{(\lambda^2+\xi^2)[(\Omega^2-\xi^2)^2+4\alpha^2\xi^2]}.
\]
For \(0<\lambda<\alpha\), its exact ratio with the critical spectrum is
\[
S_\lambda(\xi)=\frac{\lambda}{\alpha}
\left(1+\frac{\alpha^2-\lambda^2}{\lambda^2+\xi^2}\right)
S_\alpha(\xi).
\]
By Fourier inversion (with convolution in time),
\[
C_\lambda(t)=\frac{\lambda}{\alpha}\left[
C_\alpha(t)+\frac{\alpha^2-\lambda^2}{2\lambda}
\int_{-\infty}^\infty e^{-\lambda|t-s|}C_\alpha(s)\,ds
\right]>0.
\]
Evenness of stationary real-valued covariance extends the preceding critical-lag positivity to all real \(s\). Both terms are strictly positive. Hence every \(\lambda\le\alpha\) satisfies the all-lag positivity property.

**5. Infinite negative intervals beyond the boundary.** If \(\lambda>\alpha\), set \(R_\lambda=\sqrt{B_\lambda^2+H_\lambda^2}\). This is positive: if \(B_\lambda=0\), then \(H_\lambda=\lambda A_\lambda/\omega>0\). Writing the oscillatory term as \(R_\lambda\cos(\omega t-\phi_\lambda)\), we have
\[
e^{\alpha t}C_\lambda(t)=A_\lambda e^{-(\lambda-\alpha)t}
+R_\lambda\cos(\omega t-\phi_\lambda).
\]
The first summand vanishes as \(t\to\infty\), while the second attains both extreme signs indefinitely, proving infinitely many open positive and negative intervals.

**6. First-negative-lag asymptotics.** As \(\lambda\downarrow\alpha\) from above, \(A_\lambda/R_\lambda>1\) in a right neighborhood of the boundary by Step 3. Define
\[
T_\lambda=\frac{\log(A_\lambda/R_\lambda)}{\lambda-\alpha}.
\]
For \(t<T_\lambda\), the decaying positive envelope exceeds the oscillation amplitude, so \(C_\lambda(t)>0\). By the periodicity of the cosine, within at most two full oscillation periods after \(T_\lambda\), a time with cosine equal to \(-1\) occurs strictly after \(T_\lambda\) and then \(C_\lambda<0\). Thus
\[
T_\lambda\le t_-(\lambda)\le T_\lambda+\frac{4\pi}{\omega}.
\]
Multiplying by \(\lambda-\alpha\) and taking the limit yields
\[
\lim_{\lambda\downarrow\alpha}(\lambda-\alpha)t_-(\lambda)
=\log\frac{A_\alpha}{R_\alpha}
=\log\frac{2\Omega}{\sqrt{\Omega^2+3\alpha^2}},
\]
which is strictly positive for \(\Omega>\alpha\). This proves the theorem.

## Verification

The standalone \(\texttt{CHECK.py}\) uses exact symbolic covariance balance and rational identities; a separately evaluated finite-dimensional stationary Lyapunov system and matrix exponential independently recover the lag covariance on six parameter sets and five lags each. It also checks the boundary-amplitude identity and Fourier ratio. Its additional finite grid contains 4,509 tested time/parameter points, **not** a proof of the global sign theorem. The global sign classification and singular limit rest on Steps 2--6 above, not on finite numerical sampling. Reproduce by running \(\texttt{python CHECK.py}\) with Python, SymPy, NumPy and SciPy.

## Relationship to prior work

Caprini and Marconi (2020), especially their Section IV.2, Eq. (33) and Appendix C, already derive the full stationary position autocorrelation of a harmonically trapped inertial active Ornstein--Uhlenbeck particle, and qualitatively observe that sufficiently persistent active forcing suppresses negative-lag correlations. The covariance representation used here is therefore **not new**. The assessed contribution is an all-parameter if-and-only-if sign boundary, a positive-convolution proof valid for any force with the same two-time covariance, and the singular explicit first-negative-lag delay. These do not appear explicitly in the inspected discussion/formulas; they can nonetheless be derived using the established formula, so any publication-priority assessment must recognize that strong implicit prior coverage is possible.

Nguyen, Wittmann and Löwen (2021) examine harmonic inertial AOUP mean-square displacement and related two-time statistics, while Chaudhuri (2024) calculates exact stationary moments and kurtosis regimes of inertial active Brownian particles, rather than this all-lag sign boundary. These works support the physical setting without directly stating the present global sign/delay classification.

## Limitations

This is a purely second-order stationary result, not a full probability-law classification. It does not establish new formulas for the previously known stationary correlation itself, and it does not apply unchanged if an independent thermal white-noise component is added. The finite-delay asymptotic assumes fixed \(\Omega>\alpha\) and \(\lambda\downarrow\alpha\); it is not claimed to be uniform as \(\Omega\downarrow\alpha\). The result does not establish publication priority or independent scientific validation.

## References

1. L. Caprini and U. Marini Bettolo Marconi, *Inertial self-propelled particles*, arXiv:2009.14032v1 (29 September 2020), especially Section IV.2, Eq. (33), and Appendix C. https://arxiv.org/html/2009.14032v1
2. G. H. P. Nguyen, R. Wittmann and H. Löwen, *Active Ornstein-Uhlenbeck model for self-propelled particles with inertia*, arXiv:2108.14005 (31 August 2021), Section III.3. https://arxiv.org/abs/2108.14005
3. D. Chaudhuri, *Exact moments for trapped active particles: inertial impact on steady-state properties and re-entrance*, arXiv:2404.01107v1 (1 April 2024), Sections 2--5 and Appendices. https://arxiv.org/html/2404.01107v1
