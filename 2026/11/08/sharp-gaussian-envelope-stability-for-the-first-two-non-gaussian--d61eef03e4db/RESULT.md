# Sharp Gaussian-envelope stability for the first two non-Gaussian Hermite windows

## Finding
For the first two non-Gaussian normalized Hermite windows, consider the squared gain of two independent, exposure-weighted ambiguity channels, after factoring out their common Gaussian envelope. Among all allocations of one unit of squared acquisition precision, the uniquely optimal allocation is
\[w_*=1-\frac1{\sqrt5}\quad\text{to }h_1,\qquad 1-w_*=\frac1{\sqrt5}\quad\text{to }h_2.\]
Its exact globally sharp Gaussian-relative squared gain is \(9-4\sqrt5\). More precisely, for every \((x,\xi)\in\mathbb R^2\), with \(\tau=\pi(x^2+\xi^2)\),
\[w_*|\mathcal A h_1(x,\xi)|^2+(1-w_*)|\mathcal A h_2(x,\xi)|^2\ge(9-4\sqrt5)e^{-\tau}.\]
Equality occurs exactly when \(\tau=3-\sqrt5\), a complete circle of least relative ambiguity sensitivity. No other allocation achieves this universal constant. The two windows both have ambiguity zeros, but never at the same radius; both are necessary for a strictly positive Gaussian-relative margin.

## Assumptions and scope
Use the centered ambiguity convention
\[\mathcal A g(x,\xi)=\int_{\mathbb R}g(u+x/2)\overline{g(u-x/2)}e^{-2\pi i\xi u}\,du.\]
The unit-norm Hermite functions are normalized by
\[h_0(u)=2^{1/4}e^{-\pi u^2},\quad h_1(u)=2\sqrt\pi\,u h_0(u),\quad h_2(u)=\frac{4\pi u^2-1}{\sqrt2}h_0(u).\]
For \(0\le w\le1\) define
\[G_w(x,\xi)=w|\mathcal A h_1(x,\xi)|^2+(1-w)|\mathcal A h_2(x,\xi)|^2\]
and the *Gaussian-relative* squared gain \(C(w)=\inf_{(x,\xi)\in\mathbb R^2}e^\tau G_w(x,\xi)\). The total channel precision is fixed: channel amplitudes are multiplied by \(\sqrt w\) and \(\sqrt{1-w}\), with equal variance per whitened channel. The optimization is **not** over physical sampling lattices, changing Hermite shapes, or additive noise before whitening.

## Proof
**Hermite ambiguity reduction.** The standard Gaussian-Hermite identity (also obtainable by integrating the products of the explicit Hermite polynomials against a Fourier-transformed Gaussian) is
\[\mathcal A h_n(x,\xi)=e^{-\tau/2}L_n(\tau).\]
For \(n=1,2\) the Laguerre polynomials are exactly
\[L_1(t)=1-t,\qquad L_2(t)=1-2t+\tfrac12t^2.\]
Thus, because every \(t\ge0\) is achieved by some \((x,\xi)\),
\[C(w)=\inf_{t\ge0}F_w(t),\qquad F_w(t)=w(1-t)^2+(1-w)(1-2t+t^2/2)^2.\]
**Universal upper certificate.** Put \(t_0=3-\sqrt5>0\) and \(\delta=\sqrt5-2>0\). Direct substitution gives \(L_1(t_0)=\delta\) and \(L_2(t_0)=-\delta\). Hence \(F_w(t_0)=\delta^2=9-4\sqrt5\) for *every* \(w\in[0,1]\), implying
\[\sup_{0\le w\le1} C(w)\le 9-4\sqrt5.\]
**Sharp lower certificate.** Choose \(w_*=1-1/\sqrt5\). Exact polynomial multiplication produces the identity
\[F_{w_*}(t)-(9-4\sqrt5)=\frac{\sqrt5}{20}(t-3+\sqrt5)^2\Big[(t-1-\sqrt5)^2+4\Big].\]
Its right-hand side is nonnegative for all real \(t\), with equality exactly at \(t=t_0\). Thus \(C(w_*)=9-4\sqrt5\), with the stated equality circle.
**Uniqueness.** At the fixed interior point \(t_0>0\), direct differentiation gives
\[F_w'(t_0)=2\delta\big[(1-w)(\sqrt5-1)-w\big].\]
Any allocation attaining the upper certificate must have \(F_w(t)\ge F_w(t_0)\) for every \(t\ge0\); hence \(F_w'(t_0)=0\). Its unique solution is \(w=w_*\). All endpoint allocations fail this condition as well. Therefore the maximizer is unique.

**Interpretation for direct inversion.** Pointwise in the ambiguity plane, suppose two complex observations satisfy \(y_j=\sqrt{w_j}\,\overline{\mathcal A h_j}\,a+\eta_j\), with \((w_1,w_2)=(w,1-w)\), common unknown ambiguity value \(a\in\mathbb C\), and arbitrary noise vector \(\eta\in\mathbb C^2\). Ordinary two-channel least squares gives \(|\widehat a-a|\le\|\eta\|_2/\sqrt{G_w}\). The optimal allocation therefore obeys the sharp *Gaussian-relative* estimate
\[|\widehat a-a|\le\frac{e^{\tau/2}}{\sqrt{9-4\sqrt5}}\|\eta\|_2.\]
At \(t=t_0\) and aligned noise the coefficient cannot be improved uniformly in \(\tau\) after the prescribed Gaussian normalization. This is a linear ambiguity-stage estimate, not a global nonlinear STFT phase-reconstruction theorem.

## Verification
The standalone Python script `check/verify_hermite.py` performs exact symbolic substitution, derivative uniqueness, a factorization check with the strictly positive quadratic, and an exact discriminant check. It also performs direct quadrature of the normalized Hermite ambiguity integrals at ten noncollinear phase-space test cases and 20,000 deterministic random radial/weight stress cases. Execute `python check/verify_hermite.py` in an environment with SymPy and SciPy. Algebraic identities establish the infinite-domain claim; the finite checks only independently corroborate them.

## Relationship to prior work
Alaifari and Yang introduced complementary Hermite ambiguity windows and derived recovery guarantees using sets where individual windows exceed an amplitude threshold; their 2024 preprint (first public October 7, 2024), particularly Sections 2.2 and 3.2, supplies the standard Hermite-Laguerre identity and the stability motivation. It does not state the present two-window sharp weighted Gaussian-relative maximin constant or its unique allocation. Hansson-Sandsten and Sandberg (2010) optimize mean-squared error weights in averaged multitaper spectrograms, including Hermite choices; that is a different signal-dependent objective and does not imply the exact ambiguity multiplier inequality. Grohs, Liehr and Rathmair (2022) address lattice-sampled multi-window phase-retrieval uniqueness, not this all-radius pointwise sharp gain.

## Limitations
The common Gaussian factor means \(G_{w_*}(x,\xi)\to0\) at infinity. There is **no** globally uniform lower bound on the *unweighted* ambiguity gain, and no global stable inverse on the full plane is claimed. The optimal exposure allocation is for the stated common-Gaussian-normalized worst-case criterion, not necessarily the optimum for a fixed finite disk under unweighted noise. It also does not address higher Hermite pairs, other normalization conventions, or a full nonlinear phase-retrieval stability constant. Novelty is assessed against the specified accessible literature and is subject to independent historical and mathematical verification.

## References
1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486, first publicly available October 7, 2024, https://arxiv.org/abs/2410.05486; journal version DOI 10.1137/24M1701332.
2. M. Hansson-Sandsten and J. Sandberg, *Optimization of Weighting Factors for Multiple Window Spectrogram of Event-Related Potentials*, EURASIP Journal on Advances in Signal Processing (2010), DOI 10.1155/2010/391798, https://link.springer.com/article/10.1155/2010/391798.
3. P. Grohs, L. Liehr and M. Rathmair, *Multi-window STFT phase retrieval: lattice uniqueness*, arXiv:2207.10620, July 21, 2022, https://arxiv.org/abs/2207.10620.
