# Joint recovery and local blindness in distributed Brownian resetting

## Finding

The exact mean first-passage-time response to a *movable target* determines three unknowns simultaneously: the Poisson resetting rate, the Brownian diffusivity, and the entire compactly supported distribution of reset locations. By contrast, observing targets only in an open interval leaves precisely two exponential moments of the reset distribution's exterior parts observable. The full inverse map is not stable: smooth probability densities separated by a fixed positive total-variation distance can have target-response curves differing only by order \(n^{-2}\) on every compact observation window.

More precisely, let \(r,D>0\), let \(\mu\) be any compactly supported Borel probability measure on \(\mathbb R\), and let a process start from an independent draw from \(\mu\). Between the events of a rate-\(r\) Poisson clock it follows \(dX_t=\sqrt{2D}\,dB_t\); each event replaces its location by an independent new draw from \(\mu\). A target at \(b\in\mathbb R\) terminates the process at first passage, including at time zero if the starting draw equals \(b\). Let \(M(b)=\mathbb E\tau_b\), \(\kappa=\sqrt{r/D}\), and \(H(b)=\int e^{-\kappa|b-y|}\,\mu(dy)\). Then

\[
M(b)=\frac{1-H(b)}{rH(b)}.\tag{1}
\]

**(A) Joint identification.** Knowing the function \(M:\mathbb R\to[0,\infty)\), including its physical time scale, uniquely identifies \(r,D,\mu\) among the stated models. The explicit reconstruction is

\[
\begin{split}
\kappa&=\lim_{b\to+\infty}\frac{d}{db}\log M(b),\\
\int_{\mathbb R}\frac{db}{1+sM(b)}&=\frac2\kappa\quad\text{(unique at }s=r>0\text{)},\\
D&=\frac r{\kappa^2},\qquad H(b)=\frac1{1+rM(b)},\\
\mu&=\frac{\kappa^2H-H''}{2\kappa}\quad\text{as distributions.}
\end{split}\tag{2}
\]

The reconstruction includes atomic reset laws: the singular component is obtained from jumps of \(H'\).

**(B) Exact local observational equivalence.** With \(r,D\) fixed, take two compactly supported reset probabilities \(\mu,\nu\) and an open finite target window \(I=(a,c)\), with \(a<c\). Write \(\sigma=\mu-\nu\). Their mean first-passage curves agree at every target in \(I\) **if and only if**

\[
\sigma|_{(a,c)}=0,\qquad
\int_{(-\infty,a]}e^{\kappa y}\,\sigma(dy)=0,\qquad
\int_{[c,\infty)}e^{-\kappa y}\,\sigma(dy)=0.\tag{3}
\]

Hence target scanning on \(I\) identifies the reset law *within* \(I\) but cannot distinguish arbitrary exterior rearrangements preserving these two weighted masses. For example, at any \(\kappa>0\), let \(\nu=(\delta_{-2}+\delta_{-3})/2\) and \(\mu=\delta_z\) with
\[
z=\frac1\kappa\log\!\left(\frac{e^{-2\kappa}+e^{-3\kappa}}2\right).
\]
Then \(\mu\ne\nu\) yet their responses coincide for every positive target \(b>0\).

**(C) Sharp quadratic resolution loss.** For any fixed \(r,D>0\) and any \(0<\varepsilon<1\), choose an even, strictly positive on \((-1,1)\), smooth compactly supported probability density \(\varphi\) on \(\mathbb R\). Set
\[
\mu_0(dx)=\varphi(x)\,dx,\qquad
\mu_n(dx)=\varphi(x)(1+\varepsilon\sin(nx))\,dx,\qquad n=1,2,\ldots.
\]
These are all smooth, nonnegative, unit-mass densities. Then
\[
\lim_{n\to\infty}\|\mu_n-\mu_0\|_{\mathrm{TV}}=\frac{\varepsilon}{\pi}>0,
\]
where total variation is \(\sup_A|\mu_n(A)-\mu_0(A)|\). If \(M_n\) denotes the corresponding full-target response, then for every compact interval \(J\) with nonempty interior meeting \((-1,1)\),
\[
0<\liminf_{n\to\infty} n^2\|M_n-M_0\|_{C(J)}
\le\limsup_{n\to\infty} n^2\|M_n-M_0\|_{C(J)}<\infty.\tag{4}
\]
In fact, uniformly in \(b\in\mathbb R\),
\[
n^2(H_n(b)-H_0(b))-2\kappa\varepsilon\varphi(b)\sin(nb)\longrightarrow0.\tag{5}
\]
Thus the rate \(n^{-2}\) is intrinsic to the exponential-kernel inverse response, rather than a chosen numerical error level.

## Assumptions and scope

All targets are point targets on the real line, and the underlying free motion has generator \(D\partial_{xx}\). Both initial positions and subsequent reset positions are sampled independently from the *same* compactly supported probability law. Resetting is instantaneous and occurs at a constant, position-independent Poisson rate. No drift, finite-size confining geometry, or target-gating mechanism is included. The observable is the complete ensemble mean first-passage time as a function of target location, not the mean conditioned on a fixed initial point. Part (B) assumes the physical \(r,D\) are fixed and known for the local comparison; part (A) does not.

## Proof

**1. Forward identity.** Let \(S\sim\operatorname{Exp}(r)\) be independent of a free Brownian excursion, and let \(\tau_b^{(0)}\) be the free first hitting time of \(b\). The classical one-dimensional Brownian hitting transform gives \(\mathbb E_x[e^{-r\tau_b^{(0)}}]=e^{-\sqrt{r/D}|x-b|}\). Starting from \(\mu\), the probability to succeed before the first reset is \(H(b)\). The mean duration of that attempt is \(\mathbb E\min(\tau_b^{(0)},S)=(1-H(b))/r\), by integrating the survival function (including a time-zero hit). Each failed attempt restarts the same independent experiment. A renewal equation therefore reads \(M=(1-H)/r+(1-H)M\), and rearranging yields (1). The compact support and positivity of the exponential kernel imply \(0<H(b)\le1\) and finite \(M(b)\) for every target.

**2. Tail slope and calibration.** Choose \(R\) larger than the support of \(\mu\). For \(b>R\),
\[
H(b)=e^{-\kappa b}\int e^{\kappa y}\,\mu(dy)=C_+e^{-\kappa b},\quad C_+>0.
\]
Hence \(M(b)=(C_+^{-1}e^{\kappa b}-1)/r\) and the positive-limit logarithmic derivative in (2) equals \(\kappa\). Since \(\int_{\mathbb R} e^{-\kappa|b-y|}\,db=2/\kappa\), Tonelli's theorem gives \(\int H=2/\kappa\). Consider \(F(s)=\int_{\mathbb R}(1+sM(b))^{-1}\,db\) for \(s>0\). It is finite: on the tails \(M(b)\) grows exponentially and the integrand decays exponentially; on compact sets the integrand is bounded. It is continuous and strictly decreasing because \(M(b)>0\) except possibly at one point when \(\mu\) is a Dirac measure. By monotone convergence, \(F(s)\uparrow\infty\) as \(s\downarrow0\), since the integrand tends pointwise to one on an infinite-measure space. By dominated convergence, \(F(s)\downarrow0\) as \(s\to\infty\), dominated by \((1+s_0M)^{-1}\), since \(M>0\) almost everywhere. Thus \(F(s)=2/\kappa\) has exactly one positive root. The physical \(r\) is a root by (1) and normalization, proving the calibration. The identity \((\kappa^2-\partial_b^2)e^{-\kappa|b-y|}=2\kappa\delta_y\) holds in Schwartz distributions, hence the last recovery formula in (2); it identifies all measures including atoms. Finally \(D=r/\kappa^2\), proving injectivity of the entire parameter triple.

**3. Characterization on an observation interval.** For fixed \(r,D\), the mapping \(h\mapsto (1-h)/(rh)\) is strictly decreasing on \((0,1]\); hence equal responses on \(I\) are equivalent to \(H_\sigma=K_\kappa*\sigma=0\) there, where \(K_\kappa(x)=e^{-\kappa|x|}\). Apply \(\kappa^2-\partial_b^2\) locally in the sense of distributions. This yields \(\sigma|_I=0\). The remaining convolution on \(I\) splits into the exact expression
\[
H_\sigma(b)=e^{-\kappa b}\int_{(-\infty,a]}e^{\kappa y}\sigma(dy)+e^{\kappa b}\int_{[c,\infty)}e^{-\kappa y}\sigma(dy).
\]
The independent functions \(e^{-\kappa b}\) and \(e^{\kappa b}\) cannot have a vanishing linear combination on a nonempty open interval unless both coefficients vanish. The reverse direction is immediate. In the explicit two-versus-one-point example, the reset laws are both supported strictly to the left of the scanning half-line and have the same \(e^{\kappa y}\)-moment by the definition of \(z\).

**4. High-frequency smoothing with an exact rate.** Let \(f_n(b)=\varphi(b)e^{inb}\). With the Fourier convention \(\widehat f(\xi)=\int f(b)e^{-i\xi b}\,db\), the kernel has multiplier \(\widehat K_\kappa(\xi)=2\kappa/(\kappa^2+\xi^2)\). Since \(\varphi\in C_c^\infty\), its Fourier transform is rapidly decreasing. Fourier inversion and the mean-value bound for the multiplier on \(|\eta|\le n/2\), together with rapid decay on its complement, give
\[
\left\|K_\kappa*f_n-\frac{2\kappa}{n^2+\kappa^2}\varphi(b)e^{inb}\right\|_\infty=O(n^{-3}).
\]
To justify the tail estimate despite the multiplier peak near \(\eta=-n\), bound the multiplier globally by \(2/\kappa\) and use arbitrary polynomial decay of \(\widehat\varphi(\eta)\). Taking imaginary parts and multiplying by \(\varepsilon\) proves (5) uniformly; the \(O(n^{-3})\) error is quantitative. The density normalization follows because \(\varphi\) is even and the sine is odd, and nonnegativity follows from \(\varepsilon<1\). The mean of \(|\sin(nb)|\) against continuous compactly supported \(\varphi\) tends to its circle average \(2/\pi\), by periodic averaging, hence the total variation limit. On any fixed compact \(J\), \(H_0\) has a positive minimum, and \(H_n\to H_0\) uniformly. The exact quotient identity
\[
M_n-M_0=-\frac{H_n-H_0}{rH_nH_0}
\]
then gives the upper \(O(n^{-2})\) bound. For a lower bound choose any closed subinterval of the interior of \(J\cap(-1,1)\); \(\varphi\) there has a positive minimum. For all sufficiently large \(n\), it contains a point with \(|\sin(nb)|=1\). Formula (5) forces a lower bound by a positive constant times \(n^{-2}\). This proves (4).

## Verification

A standalone standard-Python verification script, `checker.py`, checks finite numerical identities by direct evaluation, numerical quadrature of the full-rate calibration in an atomic example, the exact one-vs-two-atom local indistinguishability at multiple targets, and the high-frequency Fourier multiplier asymptotics. It reports a count of passed finite diagnostics when run with `python checker.py`. These computations are not used to infer the statements for all measures or asymptotic indices; those follow from the proof above.

## Relationship to prior work

The forward identity (1) is known: Méndez, Flaquer-Galmés, and Campos (2024), arXiv:2401.01125v1, Eqs. (14)–(15), derive the mean for a random reset distribution, and discuss forward optimization and equivalent one-target resetting points. Toledo-Marin and Boyer (2022), arXiv:2206.14387, analyze forward first-passage observables and information for specified random reset laws. Abundo (2024), arXiv:2410.16889v1, formulates inverse first-passage problems using a fixed target and assigned time distribution or mean, including random reset positions with fixed reset rate; its Section 4.3 explicitly has nonunique single-observation inverse mean solutions. None of these inspected materials states the combined reconstruction of *unknown* rate, diffusion coefficient, and reset law from the full spatial mean-time scan, the exact two-moment partial-window equivalence, or the quadratic instability in (4). The novel claim is the combined inverse classification and resolution limit, **not** the established forward renewal formula or Helmholtz Green-function identity themselves.

## Limitations

The full-data reconstruction requires ideal mean-time observations at all real target positions and access to far-tail target behavior; it is not a stable finite-noise algorithm. The sharp instability is demonstrated by a specific smooth family, not a universal minimax lower bound for a statistical experiment. The local equivalence classification assumes the physical reset rate and diffusivity are fixed; it does not assert the same fiber with those parameters unknown. Physical continuity at a target initially occupied is treated by an immediate first-passage event. Novelty comparison was limited to searched and materially inspected sources; unindexed inverse-problem treatments may predate this formulation. No independent external audit or experimental validation is claimed.

## References

1. V. Méndez, R. Flaquer-Galmés, and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125v1 (first public 2024-01-02), https://arxiv.org/html/2401.01125v1 .
2. M. Abundo, *Inverse first-passage problems of a diffusion with resetting*, arXiv:2410.16889v1 (first public 2024-10-22), https://arxiv.org/abs/2410.16889 .
3. J. Quetzalcoatl Toledo-Marin and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387v1 (first public 2022-06-29), https://arxiv.org/abs/2206.14387 .
4. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Phys. Rev. Lett. 106, 160601 (2011), https://arxiv.org/abs/1102.2704 .
