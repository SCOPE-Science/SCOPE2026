# A unique curvature crossover at a rational Gabor half-density obstruction

## Finding
For the odd rational window
\[
 g(x)=\frac{x}{(x^2+1)(x^2+4)},\qquad g_\beta(t)=g(t/\beta),\quad \beta>0,
\]
let the Zak transform and the unnormalized two-channel energy be
\[
 Z_\beta(t,\xi)=\sum_{m\in\mathbb Z}g_\beta(t-m)e^{2\pi i m\xi},\qquad
 E_\beta(t,\xi)=|Z_\beta(t,\xi)|^2+|Z_\beta(t+\tfrac12,\xi)|^2.
\]
The two channels simultaneously vanish at \((t,\xi)=(0,0)\) for every \(\beta>0\). This is a half-density Gabor fiber obstruction, but the local geometry of that obstruction varies sharply with scale.

For every \(\beta>0\), the zero is strictly quadratic:
\[
 E_\beta(t,\xi)=A_\beta t^2+B_\beta\xi^2+o_\beta(t^2+\xi^2),\qquad A_\beta,B_\beta>0,
\]
where, setting \(x=\pi\beta\),
\[
\begin{aligned}
 a_0&=\frac{\pi^2\beta}{3}(\operatorname{csch}^2x-\operatorname{csch}^2(2x)),\\
 a_1&=\frac{\pi^2\beta}{3}(\operatorname{sech}^2(2x)-\operatorname{sech}^2x),\\
 b_0&=\frac{2\pi^2\beta^2}{3}\tanh x,\\
 b_1&=\frac{2\pi^2\beta^2}{3}(2\tanh(2x)-\tanh x),\\
 A_\beta&=a_0^2+a_1^2,\qquad B_\beta=b_0^2+b_1^2.
\end{aligned}
\]
The anisotropy ratio \(B_\beta/A_\beta\) is **strictly increasing on the entire interval \(\beta>0\)**, from zero to infinity. In particular there is exactly one isotropic scale \(\beta_*\), specified by \(A_{\beta_*}=B_{\beta_*}\), with
\[
0.3003<\beta_*<0.3004,\qquad \beta_*\simeq0.300316196879881.
\]
At smaller scales the frequency direction is softer; at larger scales the spatial direction is softer. The sharp limiting coefficients are
\[
\begin{aligned}
 A_\beta&\sim (16\beta^2)^{-1},& B_\beta&\sim\frac{40\pi^6}{9}\beta^6 &&(\beta\downarrow0),\\
 A_\beta&\sim\frac{32\pi^4}{9}\beta^2e^{-4\pi\beta},&B_\beta&\sim\frac{8\pi^4}{9}\beta^4 &&(\beta\to\infty).
\end{aligned}
\]
For any fixed \(\beta>0\) and any sufficiently small neighborhood \(U\) of the common zero containing no other zeros, the Lebesgue area satisfies
\[
 |\{(t,\xi)\in U:E_\beta(t,\xi)\le\varepsilon\}|\sim
 \frac{\pi\varepsilon}{\sqrt{A_\beta B_\beta}}
 \quad(\varepsilon\downarrow0).
\]
The corresponding sharp area prefactor is asymptotic to \(6\beta^{-2}/(\pi^2\sqrt{10})\) as \(\beta\downarrow0\), and to \(9e^{2\pi\beta}/(16\pi^3\beta^3)\) as \(\beta\to\infty\). These are iterated limits: first the local small-energy limit at fixed \(\beta\), then the scale limit.

## Assumptions and scope
All parameters and variables in the statement are real, with \(\beta>0\) and \((t,\xi)\) taken in a sufficiently small Euclidean neighborhood of \((0,0)\). The Zak convention is explicitly stated and matches the positive modulation convention in the cited motivating work. Both squared channels have coefficient one: no external frame-bound normalization is implied. Under lattice density \(1/2\), they form the squared norm of the one-column, two-row Zibulski–Zeevi Zak fiber, modulo harmless unit phases. The statements concern this *local* fiber and its Hessian, not global lower frame bounds. The zero is guaranteed by oddness and symmetry; the computed nondegeneracy and unique crossover are the new quantitative assertions.

## Proof
**1. Convergence, common zero, and first derivatives.** Since \(g_\beta(t)=O_\beta((1+|t|)^{-3})\), the Zak sum and its first partial derivatives converge locally uniformly: the spatial derivative has decay of order four and the frequency derivative series has decay of order two. Oddness gives \(Z_\beta(0,0)=Z_\beta(\tfrac12,0)=0\) by pairing symmetric integers and half-integers. For \(a>0\), the partial-fraction identity and Fourier convention yield
\[
 g(t)=\tfrac13\left(\frac{t}{t^2+1}-\frac{t}{t^2+4}\right),\qquad
 \widehat g(\omega)=-\frac{i\pi}{3}\operatorname{sgn}(\omega)
       (e^{-2\pi|\omega|}-e^{-4\pi|\omega|}).
\]
Poisson summation therefore gives the absolutely convergent Fourier series
\[
 Z_\beta(t,0)=\frac{2\pi\beta}{3}\sum_{k=1}^{\infty}
 (e^{-2\pi\beta k}-e^{-4\pi\beta k})\sin(2\pi kt).
\]
Differentiating at \(t=0\) and \(t=\frac12\), evaluating the resulting geometric sums, and using standard hyperbolic identities gives \(\partial_tZ_\beta(0,0)=a_0>0\) and \(\partial_tZ_\beta(\frac12,0)=a_1<0\) exactly as displayed.

Direct differentiation in frequency gives
\[
 \partial_\xi Z_\beta(t,0)=2\pi i\sum_{m\in\mathbb Z}m g_\beta(t-m).
\]
At the two symmetry points, apply the classical Mittag–Leffler sums
\[
 \sum_{m\in\mathbb Z}\frac1{m^2+a^2}=\frac{\pi}{a}\coth(\pi a),\qquad
 \sum_{m\in\mathbb Z}\frac1{(m+\frac12)^2+a^2}=\frac{\pi}{a}\tanh(\pi a),
\]
with the same partial fraction. They give \(\partial_\xi Z_\beta(0,0)=-i b_0\) and \(\partial_\xi Z_\beta(\frac12,0)=-i b_1\), with the coefficients above. The spatial derivatives are real and frequency derivatives imaginary, so the mixed real quadratic term vanishes. Taylor's theorem now proves the strictly positive diagonal quadratic expansion of \(E_\beta\).

**2. Global strict monotonicity and one crossover.** Put \(u=\tanh^2(\pi\beta)\in(0,1)\). Exact algebra gives
\[
 \frac{B_\beta}{A_\beta}=64\beta^2H(u),\quad
 H(u)=\frac{2u^3(1+u)^2(u^2-2u+5)}{(1-u)^2(3+u)^2(17u^4+4u^3+6u^2+4u+1)}.
\]
A rational derivative calculation (also reproducible by ordinary polynomial expansion) yields
\[
 H'(u)=\frac{-2u^2(1+u)P(u)}{(u-1)^3(u+3)^3(17u^4+4u^3+6u^2+4u+1)^2}
\]
with
\[
 P(u)=17u^9-51u^8+284u^7+348u^6+886u^5-50u^4
       +188u^3+220u^2+161u+45.
\]
For \(0<u<1\), group \(284u^7-51u^8+17u^9\ge233u^7\) and \(188u^3-50u^4\ge138u^3\); all ungrouped monomials of \(P\) have positive coefficients. Thus \(P(u)>0\), and the displayed denominator is negative, proving \(H'(u)>0\). Since \(\beta\mapsto u\) and \(\beta\mapsto\beta^2\) are strictly increasing positive functions, \(B_\beta/A_\beta\) increases strictly. Its limits are respectively zero and infinity by the formulas of step 3, so it crosses one at a unique \(\beta_*\). Direct substitution gives the numerical enclosure; it is not needed for the uniqueness proof.

**3. Endpoint asymptotics and local area.** Expand \(\tanh x\), \(\operatorname{csch}^2x\), and \(\operatorname{sech}^2x\) at zero. Then \(a_0\sim(4\beta)^{-1}\), \(a_1=O(\beta^3)\), \(b_0\sim(2\pi^3/3)\beta^3\), and \(b_1\sim2\pi^3\beta^3\), yielding the two small-scale coefficients. At infinity, \(a_0\sim-a_1\sim(4\pi^2\beta/3)e^{-2\pi\beta}\) and \(b_0\sim b_1\sim(2\pi^2/3)\beta^2\), yielding the two large-scale coefficients. The positive quadratic approximation is uniform up to arbitrarily small relative error in a sufficiently small neighborhood; a standard ellipse comparison then gives the area asymptotic. Inserting the coefficient equivalents yields the two endpoint prefactors. No numerical experiment is used to extend a finite computation to a universal claim.

## Verification
The accompanying `CHECK.py` uses standard-library rational arithmetic to check the derivative formula at finite rational points, sums a symmetric truncation of the original Zak derivative series independently at several scales, tests the algebraic ratio and crossover bracket, and compares endpoint coefficients. It reports precisely the finite tests run. The proof of strict monotonicity is the positivity decomposition of \(P\), not sampled monotonicity. The claimed area law follows from the positive-definite Hessian, not an exhaustive grid search.

## Relationship to prior work
Ghosh (2026, arXiv:2608.10568), originally posted August 11, treats this same rational generator and gives its Zak representation and matrix-rank criteria for rational Gabor densities; odd-window nonframeness at density one-half follows from earlier symmetry obstructions (Lyubarskii–Nes and Faulhuber). That work establishes the zero/rank obstruction but does not state the scale-dependent Hessian, unique isotropy transition, or local sublevel-area laws computed here. A related analysis for the *different* first-Hermite Gaussian-derivative window obtains a two-channel Zak-energy Hessian and is analogous in method and geometric interpretation, but its window is not rational and its formulas cannot imply the present unique scale transition. Another result on this very rational window treats a two-coset frequency perturbation around half-shift, rather than the variation of the local two-variable half-density Zak Hessian with window scale. Comparisons with those closely related statements are recorded in the accompanying review; full-text access to every related report was not available.

## Limitations
The theorem only describes the prescribed common zero and its local sublevel sets, not every Zak zero on the fundamental domain or the optimal global Gabor frame bound. The area limits are iterated, not uniform jointly in small energy and extreme scale. The result is for the exact window \(g\) and the stated Zak normalization. Broader formulas for other pole configurations are not claimed. Publication-priority risk remains from equivalent local expansions in older literature or from unpublished calculations.

## References
1. R. Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, arXiv:2608.10568, initial public submission 2026-08-11, https://arxiv.org/abs/2608.10568.
2. M. Faulhuber, *A Short Note on the Frame Set of Odd Functions*, arXiv:1710.00753, https://arxiv.org/abs/1710.00753.
3. M. Faulhuber and collaborators, *On the non-frame property of Gabor systems with Hermite generators and the frame set conjecture*, Applied and Computational Harmonic Analysis (2025), https://doi.org/10.1016/j.acha.2025.101747.
4. A. J. E. M. Janssen, *On generating tight Gabor frames at critical density*, Journal of Fourier Analysis and Applications 9 (2003), 175–214, https://doi.org/10.1007/s00041-003-0011-3.
5. Closely related mathematical research reports: *Sharp local spectral geometry at the half-density first-Hermite Gabor obstruction* (2026); *Two-coset Gabor frame classification and sharp half-shift instability for an odd rational window* (2026). See linked identifiers in the accompanying originality assessment.
