# Complete angular contact law for zeros of mixed Gaussian–Hermite spectrograms

## Finding

For real \(0\le s\le1\), let
\[
h_0(t)=2^{1/4}e^{-\pi t^2},\quad h_1(t)=2\sqrt\pi\,t h_0(t),\quad g_s=\sqrt{1-s}\,h_0+\sqrt{s}\,h_1.
\]
Let \(\mathcal N\) be standard circular complex white noise on the real line, and consider the zeros of \(F_s(x,y)=V_{g_s}\mathcal N(x,y)\), with the convention \(V_g f(x,y)=\langle f,e^{2\pi i y(\cdot)}g(\cdot-x)\rangle\). Define \(\rho_{2,s}(u)\) as the ordered, unsigned, off-diagonal second factorial density of zeros at displacement \(u\), per unit physical \((x,y)\)-area squared. For every real direction \(\theta\), put
\[
D_s(\theta)=1+2s^2+2s(1-s)\cos(2\theta),\quad
P_s(\theta)=(1-s)\cos(3\theta)+3s\cos\theta.
\]
Then the *complete directional contact law* is
\[
\boxed{C_s(\theta):=\lim_{r\downarrow0}\rho_{2,s}(r\cos\theta,r\sin\theta)
=\frac{6s^4}{D_s(\theta)^2}+\frac{8s^3(1-s)P_s(\theta)^2}{D_s(\theta)^3}.}
\]
The limit is nonnegative, continuous in both parameters, and \(\pi\)-periodic in direction. For \(s>0\), the nonzero contact is entirely from *opposite-Jacobian-charge* pairs; the like-charge contact limits vanish. At \(s=0\), \(C_0(\theta)=0\), while at \(s=1\), \(C_1(\theta)=2/3\) for every direction. In the small first-Hermite-power regime the contact has the *uniform angular asymptotic*
\[
\boxed{\sup_{\theta\in\mathbb R}\left|s^{-3}C_s(\theta)-8\cos^2(3\theta)\right|\longrightarrow0\quad(s\downarrow0).}
\]
Thus a six-lobed angular contact envelope emerges from an arbitrarily small real admixture of the first Hermite window; its six leading-order nodal directions are \(\theta=\pi/6+j\pi/3\), for integer \(j\), even though all fixed positive admixtures have strictly positive contact in every direction.

## Assumptions and scope

The noise is the centered circular complex isonormal Gaussian generalized function on \(L^2(\mathbb R)\); the displayed Hermite windows are real and orthonormal. The parameter \(s\) is the fractional squared norm of the first Hermite component, not its linear amplitude. Zero intensities count *ordered distinct zero pairs* and are not normalized by a first intensity squared. The coordinate \(\theta\) is measured counterclockwise from the physical translation \(x\)-axis towards the modulation \(y\)-axis. Both directions \(\theta\) and \(\theta+\pi\) represent the same displacement line. The window is the *real nonnegative combination* shown, not an arbitrary complex-phase superposition. The limits send separation \(r\) to zero at fixed \(s\), followed, when requested, by \(s\downarrow0\). The noise STFT is almost surely smooth with simple isolated zeros and has stationary zero statistics. The primary MSC2020 classification is 42A38.

## Proof

**Step 1 — a directional contact identity.** For a smooth centered proper complex Gaussian field \(F\) with nondegenerate Gaussian vector \((F,F_u)\), let \(u\) be a unit physical direction and \(v\) its positive perpendicular. Assume the two-point Kac–Rice formula is valid and the relevant jets have finite moments. Condition on \(F(0)=F(ru)=0\). Gaussian regression and Taylor expansion yield
\[
F_u(0)=-\frac r2F_{uu}(0)+o_{L^2}(r),\qquad
F_u(ru)=\frac r2F_{uu}(0)+o_{L^2}(r),\qquad F_v(ru)=F_v(0)+o_{L^2}(1),
\]
where the limiting jet distributions are conditioned on \(F(0)=F_u(0)=0\). The determinant of the covariance of the two constrained field values is \(r^2\det\operatorname{Cov}(F,F_u)(1+o(1))\). Using the real oriented Jacobian \(J=\operatorname{Im}(\overline{F_u}F_v)\), the two Jacobians therefore have opposite leading signs. The Kac–Rice density has the contact limit
\[
\boxed{\lim_{r\downarrow0}\rho_2(ru)=\frac14p_{F,F_u}(0,0)
\mathbb E\!\left[(\operatorname{Im}(\overline{F_{uu}}F_v))^2\mid F=F_u=0\right].}\tag{1}
\]
For the Schwartz windows here, smoothness, Gaussian moment estimates, nonproportional time-frequency shifts, and dominated convergence justify the expansion and limit. The proof of the contact identity is standard two-point Kac–Rice regression; this work claims no novelty for (1) itself.

**Step 2 — a finite Gaussian jet model.** Up to a smooth nonvanishing gauge that does not affect zeros or the conditional Jacobian calculations in (1), use the polyanalytic Bargmann representation
\[
\mathcal F_s(z,\bar z)=aG(z)+b(G'(z)-\bar zG(z)),\quad
G(z)=\sum_{j\ge0}\xi_j\frac{z^j}{\sqrt{j!}},\quad a=\sqrt{1-s},\ b=\sqrt{s},
\]
with independent standard proper complex Gaussians \(\xi_j\) and \(z=\sqrt\pi(x-iy)\). In the physical direction \(u=(\cos\theta,\sin\theta)\), set \(t=e^{-i\theta}\). At the origin, the relevant jets are
\[
\begin{aligned}
F&=a\xi_0+b\xi_1,\\
F_u&=\sqrt\pi[-b\bar t\xi_0+at\xi_1+\sqrt2bt\xi_2],\\
F_v&=-i\sqrt\pi[b\bar t\xi_0+at\xi_1+\sqrt2bt\xi_2],\\
F_{uu}&=\pi[-2b\xi_1+\sqrt2at^2\xi_2+\sqrt6bt^2\xi_3]
\end{aligned}\tag{2}
\]
when restricted to \(F=F_u=0\); any gauge terms in the last line are multiples of \(F\) or \(F_u\) and vanish under these conditions. The first two constraints have squared determinant \(\pi D_s(\theta)\). Indeed, writing \(U=-b\xi_0+a\xi_1\) (independent of \(F\)), and \(q=(1-s)t+s\bar t\), one has \(F_u=\sqrt\pi(qU+\sqrt2bt\xi_2)\) given \(F=0\). Consequently \(\operatorname{Var}(F_u\mid F)=\pi(|q|^2+2s)=\pi D_s(\theta)\), so \(p_{F,F_u}(0,0)=1/(\pi^3D_s(\theta))\). Notice \(D_s(\theta)\ge 1-2s+4s^2>0\).

**Step 3 — conditional independent coordinates.** Under the two Gaussian constraints, independent standard circular Gaussians \(R,Z\) provide
\[
U=-\frac{\sqrt{2s}\,t}{\sqrt D}R,\quad
\xi_2=\frac q{\sqrt D}R,\quad \xi_3=Z,\quad D=D_s(\theta).
\]
Substitution into (2) yields
\[
\begin{aligned}
F_v&=-i\frac{2\sqrt{2\pi}\,s^{3/2}}{\sqrt D}R,\\
F_{uu}&=\pi\left[\frac{\sqrt{2(1-s)}}{\sqrt D}\,e^{-i\theta}((1-s)e^{-2i\theta}+3s)R+\sqrt{6s}\,e^{-2i\theta}Z\right].
\end{aligned}\tag{3}
\]
The real part of the coefficient multiplying \(|R|^2\) is \(\sqrt{2(1-s)}P_s(\theta)/\sqrt D\). Because \(\mathbb E|R|^4=2\), \(\mathbb E[\operatorname{Re}(\bar ZR)^2]=1/2\), and the cross term averages to zero,
\[
\mathbb E[(\operatorname{Im}(\overline{F_{uu}}F_v))^2\mid F=F_u=0]
=\pi^3\left[\frac{32s^3(1-s)P_s(\theta)^2}{D^2}+\frac{24s^4}{D}\right].\tag{4}
\]
Inserting (4) and the joint density into (1) proves the displayed formula for \(C_s(\theta)\).

**Step 4 — charge signs and uniform asymptotics.** The leading conditional Jacobians at separated constrained zeros are \(\mp r\operatorname{Im}(\overline{F_{uu}}F_v)/2\), respectively. For \(s>0\), the independent \(Z\)-term in (3) has nonzero variance and \(F_v\) is nondegenerate, so the leading real variable has no atom at zero. Opposite charge is therefore forced in the contact limit, and like-charge contact tends to zero. The formula also gives \(C_0=0\) and \(C_1=2/3\). As \(s\downarrow0\), the denominator \(D_s(\theta)=1+O(s)\) uniformly in angle, and \(P_s(\theta)=\cos(3\theta)+O(s)\) uniformly. Therefore \(s^{-3}C_s(\theta)=8\cos^2(3\theta)+O(s)\) uniformly. The stated six leading nodal directions follow directly; at each fixed \(s>0\) the term \(6s^4/D_s^2\) enforces positivity.

## Verification

The standalone `CHECK.py` reconstructs every jet in (2) as a vector of independent proper complex Gaussian coordinates, conditions them by a Schur-complement covariance calculation (without importing (3)), uses Wick's fourth-moment identity, and compares the result with the claimed formula at 444 parameter-angle combinations. It also checks the two previously known coordinate-axis formulas, both endpoint limits, and the uniform small-mixture scaling at 111 points; the checker prints `DIRECTIONAL_CONTACT_CHECKS_PASSED 649`. The symbolic identities in Steps 2–4 are the proof; finite numerical checks are corroboration only. Execute from the package directory with `python CHECK.py` (requires NumPy).

## Relationship to prior work

Haimi, Koliander and Romero (2022) develop the Gaussian Weyl–Heisenberg zero framework, first intensities, and general Kac–Rice machinery, including a signed two-point statistic, but not the present explicit angular unsigned contact profile for a mixed Hermite window. Abreu and Shirai (2026) study correlations *between zero sets of distinct pure Hermite/Landau levels*, rather than the zeros of a single coherent real two-level combination. Bellourak, Meignen, Polisano and Nahon (October 9, 2026) derive detailed one- and two-point intensities for *pure* Hermite windows, where rotational invariance precludes the sixfold nonradial small-mixture profile. The closely related published work *Direction-dependent contact intensities of zeros for Gaussian–first-Hermite spectrograms* gives the two physical coordinate-axis contact values, exactly recovered by this theorem, but explicitly leaves the *whole angular contact profile* undetermined. Neither two axis values nor a pure-window radial theorem implies the angular law established here.

## Limitations

The theorem is for the real, nonnegative two-mode mixing coefficients, not arbitrary relative complex phase. It concerns the contact (infinitesimal-separation) limit of the ordered unsigned factorial density, not the finite-separation two-point density or normalized pair correlation. It does not assert a uniform joint limit if separation and mixture tend to zero together. The sixfold nodal pattern is the *leading-order* small-admixture limit; the exact contact is positive at all angles for every \(s>0\). The existence of a published equivalent formulation under different covariance notation remains a publication-priority risk; no independent audit has been performed.

## References

1. A. Haimi, G. Koliander, J. L. Romero, *Zeros of Gaussian Weyl–Heisenberg Functions and Hyperuniformity of Charge*, Journal of Statistical Physics 187 (2022), article 22; https://doi.org/10.1007/s10955-022-02917-3 .
2. L. D. Abreu, T. Shirai, *Zero correlations and averaged fields of orthonormal Gaussian functions*, arXiv:2605.17296, first posted May 17, 2026; https://arxiv.org/abs/2605.17296 .
3. C. Bellourak, S. Meignen, K. Polisano, M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531, first posted October 9, 2026; https://arxiv.org/abs/2610.13531 .
4. *Direction-dependent contact intensities of zeros for Gaussian–first-Hermite spectrograms*, publicly available November 8, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-direction-dependent-contact-intensities-of-zeros-for-gaussian-fi--3c31553cb312 .
