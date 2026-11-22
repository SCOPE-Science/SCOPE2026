# Arbitrarily many diffusion enhancement–suppression reversals in telegraph-switched smooth periodic potentials

## Finding
A single smoothly varying periodic potential, flipped between opposite signs by a two-state Markov clock, can alternately enhance and suppress long-time diffusion relative to free Brownian motion **arbitrarily many times** as the clock rate varies. The statement is an existence theorem, not a claim that every flashing potential exhibits reentrance.

For every integer \(m\ge 1\), there are distinct positive odd integers \(k_1<\cdots<k_m\), positive real weights \(w_1,\ldots,w_m\), and a positive potential amplitude \(\varepsilon_m\), such that the diffusion coefficient of
\[
dX_t=\varepsilon S_tF(X_t)\,dt+\sqrt{2}\,dB_t,\qquad F(x)=\sum_{j=1}^m\sqrt{2w_j}\cos(k_jx),
\]
where \(S_t\in\{-1,+1\}\) flips at constant rate \(\nu>0\), has at least \(2m-1\) distinct positive-rate crossings of the thermal baseline \(D_{\mathrm{eff}}=1\). Consecutive crossing intervals alternate suppression and enhancement. The potential \(U\) with \(-U'=F\) is smooth and satisfies \(U(x+\pi)=-U(x)\).

In particular, take \(m=2\), \((k_1,w_1)=(1,1)\), \((k_2,w_2)=(25,50)\). For every sufficiently small \(\varepsilon>0\), the signs of \(D_{\mathrm{eff}}(\varepsilon,\nu)-1\) at \(2\nu=1/2,2,25,1250\) are, respectively, negative, positive, negative, positive. There are therefore at least **three separate crossing rates**, despite just two spatial Fourier scales. The proof also provides a uniform weak-amplitude formula for each fixed switching rate:
\[
D_{\mathrm{eff}}(\varepsilon,\nu)=1+\varepsilon^2H(2\nu)+O_{\nu,F}(\varepsilon^3),\qquad
H(t)=\sum_{j=1}^{m}w_j\frac{t-k_j^2}{(t+k_j^2)^2}.
\]
Here the remainder is a fixed-rate asymptotic, not a claim of uniformity over all rates or over the inductive family of potentials.

## Assumptions and scope
The unwrapped coordinate \(X_t\) evolves on \(\mathbb R\), with force periodic in \(x\) with period \(2\pi\). The Brownian motion \(B_t\) is independent of the symmetric, stationary two-state chain \(S_t\) with transition intensity \(\nu\) from each state to the other. Thermal diffusivity is normalized to one. The periodic position and internal state possess a unique smooth stationary density because diffusion is uniformly elliptic and the switching is irreducible. The effective diffusivity is
\[
D_{\mathrm{eff}}=\lim_{T\to\infty}\frac{\operatorname{Var}(X_T-X_0)}{2T},
\]
independent of the initial law. The stationary drift is identically zero for the even force \(F\) because \((x,s)\mapsto(-x,-s)\) reverses velocity and preserves the process. Odd harmonics guarantee the potential half-period sign-flip symmetry used in the classical flashing-potential literature. All statements concern fixed finite Fourier sums, finite positive rates, and sufficiently weak nonzero potential amplitude selected after the finite set of rates.

## Proof
**1. Corrector representation.** On the periodized state space \(\mathbb T\times\{-1,+1\}\), let
\[
\mathcal L_\varepsilon\phi_s=\partial_x^2\phi_s+\varepsilon sF(x)\partial_x\phi_s+\nu(\phi_{-s}-\phi_s).
\]
For each fixed \(\nu>0\), the invariant densities \(\rho_s\), normalized so their sum integrates to one, depend analytically on sufficiently small \(\varepsilon\). Let \(\chi\) be the mean-zero periodic solution of \(-\mathcal L_\varepsilon\chi_s=\varepsilon sF(x)\). The usual martingale decomposition of displacement plus corrector gives
\[
D_{\mathrm{eff}}=\sum_s\int_0^{2\pi}\rho_s\bigl(1+\partial_x\chi_s\bigr)^2dx
+\frac{\nu}{2}\sum_s\int_0^{2\pi}\rho_s(\chi_{-s}-\chi_s)^2dx.
\]
Using invariance, integration by parts and \(-\mathcal L\chi=b\), the same exact identity is
\[
D_{\mathrm{eff}}=1+2\mathbb E_\rho[\partial_x\chi]+\mathbb E_\rho[b\chi],\qquad b=\varepsilon SF.
\]
The last identity is the standard homogenization identity; it is not claimed as new.

**2. First perturbative orders.** Expand
\[
\rho_s(x)=\frac1{4\pi}+\varepsilon s h(x)+O(\varepsilon^2),\quad
\chi_s(x)=\varepsilon s g(x)+O(\varepsilon^2).
\]
The stationary forward equation and the corrector equation respectively give
\[
(\partial_x^2-2\nu)h=\frac{F'(x)}{4\pi},\qquad
(\partial_x^2-2\nu)g=-F(x),\qquad h=-\frac{g'}{4\pi}.
\]
For Fourier coefficients \(\widehat F_n=(2\pi)^{-1}\int_0^{2\pi}F(x)e^{-inx}dx\),
\[
\widehat g_n=\frac{\widehat F_n}{n^2+2\nu}\qquad(n\ne0).
\]
Consequently,
\[
2\mathbb E_\rho[\chi']=-2\varepsilon^2\sum_{n\ne0}\frac{n^2|\widehat F_n|^2}{(n^2+2\nu)^2}+O(\varepsilon^3),
\]
\[
\mathbb E_\rho[b\chi]=\varepsilon^2\sum_{n\ne0}\frac{|\widehat F_n|^2}{n^2+2\nu}+O(\varepsilon^3).
\]
Combining these yields \(H(2\nu)=\sum_{n\ne0}|\widehat F_n|^2(2\nu-n^2)/(2\nu+n^2)^2\). The symmetric modes at \(\pm k_j\) have total Fourier power \(w_j\), proving the displayed coefficient. Analytic perturbation is justified by the simple invariant eigenvalue and the fixed-rate spectral gap of the elliptic generator on the compact state space.

**3. Unbounded alternating sign witnesses.** With a single mode \(k_1=1,w_1=1\), the coefficient \(H_1(t)=(t-1)/(t+1)^2\) is strictly negative at \(t=1/2\) and strictly positive at \(t=2\). Suppose a finite positive weighted sum \(H_m\) admits ordered \(2m\) witnesses with alternating signs, ending positive. Choose an odd integer \(k\) larger than every previous wavenumber, its square root scale, and every witness, and add a new mode with weight \(w=k^{3/2}\). For each old fixed witness \(t\), the new summand satisfies
\[
k^{3/2}\frac{t-k^2}{(t+k^2)^2}=-k^{-1/2}(1+o(1)),
\]
so all old strict signs persist for sufficiently large \(k\). At the additional witness \(t=k\), the old modes contribute \(H_m(k)=O(k^{-1})\), while the new mode contributes \(-k^{-1/2}(1+o(1))\); hence the sum is negative. At the further witness \(t=2k^2\), *every* mode term is positive because its numerator is positive. Thus two new, later alternating witnesses exist. Induction yields \(2m\) witnesses and therefore at least \(2m-1\) distinct crossing intervals for \(H_m\).

For each constructed finite sum, analyticity and its finite set of strict nonzero witnesses permit choosing one \(\varepsilon_m>0\) so small that \(D_{\mathrm{eff}}(\varepsilon_m,\nu)-1\) has all the same signs. Continuity in \(\nu>0\) and the intermediate value theorem force the claimed number of crossings in the actual diffusion coefficient, not merely in its leading perturbative term. No explicit lower bound on \(\varepsilon_m\) is claimed.

**4. Two-mode rational witness.** For the displayed \(k=1,25\), \(w=1,50\), the exact four coefficient evaluations at \(t=1/2,2,25,1250\) are
\[
-\frac{472678}{1565001},\qquad\frac{4177}{131043},\qquad-\frac6{169},\qquad\frac{379003}{39125025}.
\]
All four signs are strict, giving three distinct intervals in which the actual diffusion coefficient crosses the thermal baseline for sufficiently weak nonzero amplitude.

## Verification
The standalone `verification/certify.py` uses exact rational arithmetic to reproduce the four displayed witnesses and their alternation. The independent truncated Fourier–Galerkin calculation in `verification/galerkin.py` solves the coupled stationary and corrector equations and evaluates the martingale diffusion formula for the two-mode example. For \(\varepsilon=0.015\), its four calculated values of \(D_{\mathrm{eff}}-1\) are approximately \(-6.79476924\times10^{-5},+7.17170872\times10^{-6},-7.98825934\times10^{-6},+2.17956515\times10^{-6}\), agreeing in sign and leading order with the perturbative values. This finite truncation is a corroboration only; the analytic induction and continuity argument prove the infinite family.

## Relationship to prior work
Frydel (arXiv:2611.13526v1, public November 10, 2026) studies effective diffusivity of periodic forces refreshed at Poisson times, including an equal-probability two-state model, and derives a general homogenization/duality representation. That representation encompasses the present switching mechanism and supplies established methodological foundations, but its inspected model, analysis and applications do not assert the alternating Fourier-scale threshold or an unbounded number of baseline crossings. For a symmetric independent-redraw clock of mean interval \(\tau\), its effective sign-flip rate is \(\nu=1/(2\tau)\).

Spagnolo and Dubkov (arXiv:cond-mat/0510170v1, public October 7, 2005) derive general mean-first-passage equations for supersymmetric periodically switching potentials and explicit sawtooth and rectangular-potential examples. They report enhanced diffusion for some switching rates but do not state an unbounded number of enhancement–suppression crossings for smooth multiscale profiles. Their first-passage equations cover arbitrary force shapes, but their single-cell mean-first-passage approximation is not generally equal to the exact effective diffusivity, as Frydel demonstrates explicitly. Consequently the present proof uses the independent homogenization corrector rather than relying on that approximation. Dubkov and Spagnolo, Phys. Rev. E 72, 041104 (2005), is particularly close; its accessible abstract reports general equations and a sawtooth example, but its full text was not available for comparison. A separate published weak-potential analysis of thermally diffusing run-and-tumble motion concerns *additive telegraph propulsion with a fixed potential*, not a sign-flipping potential; a published Fourier-spectroscopy analysis concerns an *exogenous active driver without feedback*, not the position-coupled flashing force.

## Limitations
The result guarantees at least \(2m-1\) crossings for a potentially very small amplitude chosen separately for every constructed force. It does not bound the maximal number of crossings for a fixed small number of Fourier modes, guarantee simple zeros or exactly the claimed number, or establish a finite-amplitude uniform-in-rate theorem. The inductive construction uses increasing spatial frequency and force magnitude, so it does not hold a common force norm or spectral cutoff fixed as the number of switches grows. The general homogenization and first-passage machinery is prior art. An inaccessible close full text and unindexed reductions from general earlier formulas remain scholarly-priority risks; independent scientific review is required.

## References
1. D. Frydel, *A new representation of effective diffusion in fluctuating periodic potentials through stochastic duality*, arXiv:2611.13526v1 (2026-11-10), https://arxiv.org/html/2611.13526v1.
2. B. Spagnolo and A. Dubkov, *Diffusion in Flashing Periodic Potentials*, arXiv:cond-mat/0510170v1 (2005-10-07), https://arxiv.org/pdf/cond-mat/0510170.
3. A. A. Dubkov and B. Spagnolo, *Acceleration of diffusion in randomly switching potential with supersymmetry*, Phys. Rev. E 72, 041104 (2005), https://doi.org/10.1103/PhysRevE.72.041104.
