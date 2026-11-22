# Exact Fourier curvature spectrum of mean boundary distances at the circle

## Finding
Let \(f\) be a real \(C^2\), \(2\pi\)-periodic function satisfying
\[
\int_0^{2\pi}f(\theta)\,d\theta=0,\qquad
\int_0^{2\pi}f(\theta)e^{i\theta}\,d\theta=0.
\]
Write its real Fourier series as
\[
f(\theta)=\sum_{m\ge2}(a_m\cos m\theta+b_m\sin m\theta).
\]
For sufficiently small real \(\varepsilon\), let \(K_\varepsilon\) be the strictly convex planar body whose boundary is parametrized, up to translation, by
\[
z_\varepsilon'(\theta)=i e^{i\theta}(1+\varepsilon f(\theta)),\quad 0\le\theta\le2\pi.
\]
Its perimeter is exactly \(2\pi\). For independent arclength-uniform boundary points \(X_\varepsilon,Y_\varepsilon\), define
\[
\mathcal F(\varepsilon)=\frac{\mathbb E|X_\varepsilon-Y_\varepsilon|}{\operatorname{per}(K_\varepsilon)}.
\]
Then
\[
\boxed{\mathcal F(\varepsilon)=\frac2{\pi^2}-\frac{\varepsilon^2}{4\pi^2}
\sum_{m\ge2} Q_m(a_m^2+b_m^2)+o(\varepsilon^2)}.
\]
Here, with \(H_m^{\rm odd}=\sum_{j=1}^m(2j-1)^{-1}\),
\[
\boxed{Q_m=\frac{12}{4m^2-1}-\frac1{m^2-1}-\frac{2H_m^{\rm odd}}{(m^2-1)^2}
-\frac1{2(2m+1)(m+1)^2}+\frac1{2(2m-1)(m-1)^2}}.
\]
Every \(Q_m\) is strictly positive for each integer \(m\ge2\), and
\[
Q_m=\frac2{m^2}+O\left(\frac{\log m}{m^4}\right)
\quad(m\to\infty),\qquad Q_2=\frac{44}{135},\quad Q_3=\frac4{21}.
\]
Thus the curvature-radius Hessian is strictly negative on all fixed-perimeter, closure-compatible perturbations; its high-harmonic weights have sharp order \(m^{-2}\). The coefficient for each individual harmonic is exact, not a bound on a finite set of test modes.

## Assumptions and scope
The normal angle \(\theta\) increases once around a simple convex curve. The radius of curvature is \(\rho_\varepsilon(\theta)=1+\varepsilon f(\theta)>0\); the vanishing first Fourier coefficient makes the integrated tangent field close up. The mean-zero condition fixes perimeter. We assume \(f\in C^2\); in fact the local expansion holds under lower regularity when the curve and integrals are well-defined, but no such generalization is claimed. Frequencies \(m=0\) and \(m=1\) are respectively excluded by perimeter normalization and geometric closure, rather than classified as zero Hessian modes. All bodies are Euclidean and planar; the claim is local about a radius-one circle and is not a global quantitative stability inequality.

## Proof
**1. Normal-angle setup and differentiation.** Positivity of \(\rho_\varepsilon\) makes \(z_\varepsilon\) a smooth regular curve whose tangent turns through \(2\pi\) monotonically. Since \(\int_0^{2\pi}e^{i\theta}f(\theta)d\theta=0\) and \(\int e^{i\theta}=0\), the curve closes; it is the boundary of a strictly convex body. Its arclength element is \(\rho_\varepsilon(\theta)d\theta\), hence its perimeter is \(2\pi\). Let
\[
I(\varepsilon)=\int_0^{2\pi}\!\int_0^{2\pi}
\rho_\varepsilon(\theta)\rho_\varepsilon(\phi)
|z_\varepsilon(\theta)-z_\varepsilon(\phi)|\,d\theta\,d\phi.
\]
Then \(\mathcal F(\varepsilon)=I(\varepsilon)/(2\pi)^3\). For the circular base, \(I(0)=16\pi\) and \(\mathcal F(0)=2/\pi^2\). For \(\theta\) close to \(\phi\) (modulo \(2\pi\)), the perturbed chord differs from the base chord by at most \(C|\varepsilon|\|f\|_\infty\) times its base length. Therefore the norm's second derivative is bounded by an integrable multiple of the base chord length. This supplies dominated twice differentiation despite the vanishing chord on the diagonal. Fourier-mode approximation is legitimate by continuity of the quadratic form in the uniform norm.

**2. One mode.** By rotational symmetry it suffices to take \(f(\theta)=\cos(m\theta)\), \(m\ge2\). Set \(\theta=t+u/2\), \(\phi=t-u/2\) modulo \(2\pi\), and write \(s=\sin(u/2)\),
\[
A=\frac{\sin((m+1)u/2)}{m+1},\qquad
B=\frac{\sin((m-1)u/2)}{m-1}.
\]
The base chord equals \(2ie^{it}s\), and the perturbation chord equals \(ie^{it}(e^{imt}A+e^{-imt}B)\). The arclength product expands as
\[
\rho_\varepsilon(\theta)\rho_\varepsilon(\phi)
=1+2\varepsilon\cos(mt)\cos(mu/2)
+\varepsilon^2(\cos^2(mt)-\sin^2(mu/2)).
\]
Expanding the norm and integrating over \(t\) eliminates the linear term. Its quadratic coefficient, after the \(t\)-average, is
\[
G_m(u)=s\cos(mu)+(A+B)\cos(mu/2)+\frac{(A-B)^2}{8s}.
\]
Consequently \([\varepsilon^2]I=2\pi\int_0^{2\pi}G_m(u)du\) and \([\varepsilon^2]\mathcal F=(4\pi^2)^{-1}\int G_m\). Elementary product-to-sum integration gives
\[
\int_0^{2\pi}s\cos(mu)du=-\frac4{4m^2-1},\qquad
\int_0^{2\pi}(A+B)\cos(mu/2)du=-\frac8{4m^2-1}.
\]
For the remaining positive term define
\[
J_m=\int_0^{2\pi}\frac{(A-B)^2}{8s}du
=\frac14\int_0^\pi\frac{1}{\sin t}
\left(\frac{\sin((m+1)t)}{m+1}-\frac{\sin((m-1)t)}{m-1}\right)^2dt.
\]
Thus the deficit coefficient is \(Q_m=12/(4m^2-1)-J_m\).

**3. Exact evaluation.** Put \(I_k=\int_0^\pi\sin^2(kt)/\sin t\,dt\). From
\(\sin^2(kt)-\sin^2((k-1)t)=\sin((2k-1)t)\sin t\),
\(I_k=2\sum_{j=1}^k(2j-1)^{-1}=2H_k^{\rm odd}\).
Also \(\sin((m+1)t)\sin((m-1)t)=\sin^2(mt)-\sin^2 t\), so the cross integral is \(I_m-2\). Expanding the square gives
\[
J_m=\frac14\left(\frac{I_{m+1}}{(m+1)^2}+
\frac{I_{m-1}}{(m-1)^2}-\frac{2(I_m-2)}{m^2-1}\right).
\]
Substituting consecutive odd harmonic sums produces the closed formula for \(Q_m\) in the statement. Direct substitution gives \(Q_2=44/135\), \(Q_3=4/21\).

**4. Positivity and high-frequency law.** Since \(H_m^{\rm odd}\le m\), dropping the final negative summand in the simplified expression for \(J_m\) yields
\[
J_m\le\frac1{m^2-1}+\frac{2m}{(m^2-1)^2}
+\frac1{2(2m+1)(m+1)^2}.
\]
The difference between \(12/(4m^2-1)\) and this upper bound is precisely
\[
\frac{16m^4-18m^3-33m^2+23}{
2(m-1)^2(m+1)^2(2m-1)(2m+1)}.
\]
Its numerator is \(3\) at \(m=2\) and is increasing on \([2,\infty)\), because its derivative is \(m(64m^2-54m-66)>0\). Therefore \(Q_m>0\) for every \(m\ge2\). Since \(H_m^{\rm odd}=O(\log m)\), the closed expression immediately gives \(Q_m=2/m^2+O(\log m/m^4)\).

**5. General perturbation.** The second variation is a continuous quadratic form on real zero-mean, first-harmonic-free \(C^2\) perturbations. Rotational invariance makes different Fourier frequencies orthogonal, and forces equal coefficients for sine and cosine within one frequency. Evaluating the cosine mode in Steps 2–4 determines every diagonal entry; uniform trigonometric approximation yields the full convergent series and the claimed \(o(\varepsilon^2)\) expansion.

## Verification
The companion standalone `CHECK.py` uses rational arithmetic to integrate the squared Chebyshev polynomial representation of \(J_m\) for each integer \(2\le m\le15\), compares this independently to the harmonic-sum formula, verifies the first two exact coefficients, and checks positivity. It separately computes arclength-weighted chord double sums directly for four perturbation frequencies and compares centered second differences to the analytic coefficients. These finite calculations are reproducibility checks only; the all-frequency conclusions use the preceding proof.

## Relationship to prior work
Tokmachev (2022) proved that the circle uniquely maximizes mean arclength-boundary distance at fixed perimeter, and obtained a Fourier argument for the squared chord. This theorem gives the exact, unsquared mean-distance **second variation** for every curvature-radius harmonic, including its strictly negative complete spectrum and its asymptotic order; a qualitative global maximum and a squared-chord bound do not specify these coefficients. Shen (2026) established the complementary sharp lower bound \(1/6\). Previous thin-body asymptotics concern degeneration toward segments, whereas this statement concerns the local shape Hessian at the disk. It does not reassert those known global bounds as novel.

## Limitations
This is an explicit **local** Hessian, not a uniform global deficit bound for arbitrary convex curves. All claims of priority are provisional subject to historical literature not indexed by the searches. The \(o(\varepsilon^2)\) remainder is for each fixed perturbation \(f\); it is not uniform over unbounded families of frequencies. There is no claim of independent external verification.

## References
- A. S. Tokmachev, *Mean distance between random points on the boundary of a convex body*, Zapiski Nauchnykh Seminarov POMI 510 (2022), 248–261, https://www.mathnet.ru/eng/znsl7205 ; full text https://www.mathnet.ru/php/getFT.phtml?jrnid=znsl&option_lang=eng&paperid=7205&what=fullt .
- Eric Shen, *A Sharp Perimeter Inequality for Mean Distances on Convex Curves*, arXiv:2611.21661v1, first public 2026-11-07, https://arxiv.org/html/2611.21661v1 .
