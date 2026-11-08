# Exact Fourier–Bessel shape spectrum of Gaussian localization Hilbert–Schmidt energy

## Finding

Let \(A>0\). Among planar regions of area \(A\), a disk maximizes the squared Hilbert–Schmidt norm of the Gaussian short-time Fourier localization operator, as established by Nicola and Riccardi. The new result here resolves **every quadratic shape mode** of that maximization problem.

For any real \(u\in C^2(\mathbb T)\) of angular mean zero, put
\[
\Omega_{\varepsilon,u}=\{z\in\mathbb C:\ \pi|z|^2<A+\varepsilon u(\arg z)\},\qquad
\widehat u(n)=\frac1{2\pi}\int_0^{2\pi}u(\theta)e^{-in\theta}\,d\theta.
\]
When \(|\varepsilon|\) is small, \(|\Omega_{\varepsilon,u}|=A\) exactly. For the localization operator \(L_\Omega\) defined below,
\[
\boxed{\ \|L_{\Omega_{\varepsilon,u}}\|_{\mathrm{HS}}^2
=\|L_{D_A}\|_{\mathrm{HS}}^2
-\varepsilon^2 e^{-2A}\sum_{|n|\ge2}
\left[I_1(2A)-I_{|n|}(2A)\right]|\widehat u(n)|^2
+o_{A,u}(\varepsilon^2).\ }
\]
Here \(D_A=\{z:\pi|z|^2<A\}\) and \(I_k\) is the modified Bessel function of the first kind of integer order \(k\). The degree-one Fourier modes are precisely the quadratic null directions (infinitesimal translations). The quadratic costs obey, for every \(A>0\),
\[
0<I_1(2A)-I_2(2A)<I_1(2A)-I_3(2A)<\cdots<I_1(2A).
\]
Consequently, on the orthogonal complement of constants and translations the optimal local coefficient is
\[
\boxed{\ c(A)=e^{-2A}[I_1(2A)-I_2(2A)]\ },
\]
attained at quadratic order precisely by nonzero real combinations of \(\cos(2\theta)\) and \(\sin(2\theta)\). The coefficient has the two scale limits
\[
c(A)=A+O(A^2)\quad(A\downarrow0),\qquad
c(A)\sim\frac3{8\sqrt\pi\,A^{3/2}}\quad(A\to\infty).
\]

## Assumptions and scope

Use the normalized Gaussian window \(\varphi(x)=2^{1/4}e^{-\pi x^2}\) in \(L^2(\mathbb R)\), its short-time Fourier transform \(V_\varphi\), and \(L_\Omega=V_\varphi^*\mathbf1_\Omega V_\varphi\) for measurable \(\Omega\subset\mathbb R^2\). The Hilbert–Schmidt norm is the operator-ideal norm (not the operator norm). Area is planar Lebesgue measure, without further normalization. For each fixed \(A>0\) and real \(u\in C^2(\mathbb T)\) with \(\widehat u(0)=0\), the expansion holds as \(\varepsilon\to0\) through values for which \(A+\varepsilon u(\theta)>0\) for all \(\theta\). No uniformity over all \(u\) or all \(A\) is asserted. The Fourier inner product is normalized by \((2\pi)^{-1}\int_0^{2\pi}\), so Parseval reads \(\sum_n|\widehat u(n)|^2=(2\pi)^{-1}\int|u|^2\).

## Proof

**1. Reduction to a smooth double-boundary integral.** Formula (3.5) of Nicola–Riccardi gives
\[
H(\Omega):=\|L_\Omega\|_{\mathrm{HS}}^2
=\int_{\Omega}\int_{\Omega}e^{-\pi|z-w|^2}\,dA(z)\,dA(w).
\]
Set \(z=\pi^{-1/2}\sqrt t\,e^{i\theta}\). Then \(dA(z)=dt\,d\theta/(2\pi)\) and
\[
H(\Omega_{\varepsilon,u})
=\frac1{4\pi^2}\int_0^{2\pi}\!\int_0^{2\pi}
\int_0^{A+\varepsilon u(\theta)}\!\int_0^{A+\varepsilon u(\phi)}
K(t,s,\theta-\phi)\,ds\,dt\,d\phi\,d\theta,
\]
where \(K(t,s,\psi)=e^{-t-s+2\sqrt{ts}\cos\psi}\). For fixed positive \(A\), all relevant integrands have continuous derivatives near \(t=s=A\). Taylor expansion of these moving upper limits is therefore valid, with remainder \(o(\varepsilon^2)\) for each fixed \(u\).

**2. The first variation vanishes and the second is explicit.** The first variation is a constant multiple of \(\int u\), hence zero. In the second-order coefficient, the term coupling the two moving boundaries is
\[
e^{-2A}\frac1{4\pi^2}\int_0^{2\pi}\!\int_0^{2\pi}
 u(\theta)u(\phi)e^{2A\cos(\theta-\phi)}\,d\phi\,d\theta
=e^{-2A}\sum_{n\in\mathbb Z}I_{|n|}(2A)|\widehat u(n)|^2.
\]
The two self-boundary terms combine to
\[
\frac1{4\pi^2}\int_0^{2\pi}u(\theta)^2\left[
\int_0^{2\pi}\!\int_0^A \partial_t K(A,s,\theta-\phi)\,ds\,d\phi\right]d\theta.
\]
To evaluate the bracket, define the normalized disk potential
\[
F_A(\rho)=\frac1\pi\int_{|w|<\sqrt A}e^{-|\rho e_1-w|^2}\,dA(w).
\]
By differentiating in \(\rho\) and integrating the derivative over the disk by the divergence theorem,
\[
F_A'(\sqrt A)=-2\sqrt A\,e^{-2A}I_1(2A).
\]
Since \(t=\rho^2\) and the bracket equals \(2\pi\partial_tF_A(\sqrt t)|_{t=A}\), it is \(-2\pi e^{-2A}I_1(2A)\). The self-boundary contribution is therefore
\[
-e^{-2A}I_1(2A)\sum_{n\in\mathbb Z}|\widehat u(n)|^2.
\]
Adding cross-boundary and self-boundary contributions proves the stated expansion; the term for \(n=0\) is absent by the area constraint. The terms \(n=\pm1\) cancel identically.

**3. Strict ordering and the sharp shape mode.** For every integer \(k\ge1\), set \(r_k(x)=I_{k+1}(x)/I_k(x)\) for \(x>0\). The standard Bessel differentiation identities give
\[
r_k'(x)=1-\frac{2k+1}{x}r_k(x)-r_k(x)^2.
\]
Near zero \(r_k(x)\sim x/[2(k+1)]<1\). At a hypothetical first upward crossing of \(1\), the displayed derivative would be \(-(2k+1)/x<0\), a contradiction. Thus \(0<I_{k+1}(x)<I_k(x)\) for all \(x>0\), \(k\ge1\). Moreover \(I_k(x)\to0\) as \(k\to\infty\) for fixed \(x\). It follows that the nonzero quadratic costs are strictly increasing in \(|n|\). Parseval then yields the sharp inequality
\[
H(D_A)-H(\Omega_{\varepsilon,u})
\ge\varepsilon^2 c(A)\sum_{|n|\ge2}|\widehat u(n)|^2+o_{A,u}(\varepsilon^2).
\]
Here the remainder is signed and is not claimed uniform. The coefficient is attained in the limiting ratio precisely when only degrees \(\pm2\) occur among the nontranslation modes. Thus degree two is the unique least-expensive genuine deformation, modulo the phase of that mode.

**4. Small and large aperture regimes.** The defining series of \(I_k\) gives \(I_1(2A)=A+O(A^3)\), \(I_2(2A)=A^2/2+O(A^4)\), and \(e^{-2A}=1+O(A)\), proving \(c(A)=A+O(A^2)\). For fixed integer \(k\), the standard large-argument expansion
\[
e^{-2A}I_k(2A)=\frac1{\sqrt{4\pi A}}
\left(1-\frac{4k^2-1}{16A}+O_k(A^{-2})\right)
\]
implies \(c(A)=3/(8\sqrt\pi A^{3/2})+O(A^{-5/2})\). This proves both scale limits.

## Verification

A standalone program, `checks.py`, evaluates the original fourfold Gaussian interaction integral by tensor-product Gaussian quadrature independently of the Bessel formula. It compares symmetric second differences against the predicted coefficient for four angular degrees and three different areas; it also tests special-function monotonicity and both aperture regimes. The finite program is not used to prove the infinite Fourier series, Bessel monotonicity, or differentiability. Run it with Python and the `numpy` and `scipy` packages: `python checks.py`.

## Relationship to prior work

Nicola and Riccardi proved the global Hilbert–Schmidt rearrangement inequality, uniqueness of disk maximizers, and a quantitative deficit estimate for arbitrary measurable sets; their Section 5 supplies qualitative sharpness of the deficit's asymmetry power. The result above takes the same squared Hilbert–Schmidt functional but resolves its **full area-constrained disk shape Hessian**, including an exact coefficient for every angular mode, the sharp least-curved mode, and the area dependence of that coefficient. The earlier global result and the input identity are not claimed as new. Gómez, Guerra, Ramos, and Tilli treat the different, operator-norm/Faber–Krahn extremal problem, not the squared Hilbert–Schmidt shape spectrum. Classical nonlocal second-variation theory (Acerbi–Fusco–Morini) gives related methodology for different interaction kernels and energies, not this Gaussian localization multiplier formula. The claim is a specific explicit calculation, not the invention of generic shape calculus or Fourier diagonalization.

## Limitations

The analysis is planar (one-dimensional signal phase space), perturbative in \(\varepsilon\), and restricted to smooth squared-radius graphs. The proof does not produce a global sharp Fraenkel-asymmetry constant, a uniform remainder over high-frequency profiles, or an identical formula for the operator norm or for more general windows. Earlier broad second-variation methods may contain implicit reductions that could narrow claims of historical priority.

## References

1. F. Nicola and F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert–Schmidt norm of localization operators*, arXiv:2401.04659 (first public 2024-01-09), especially formula (3.5), Proposition 3.4, and Section 5. https://arxiv.org/abs/2401.04659
2. J. Gómez, A. Guerra, J. P. G. Ramos, and P. Tilli, *Stability of the Faber–Krahn inequality for the Short-time Fourier Transform*, arXiv:2307.09304 (2023). https://arxiv.org/abs/2307.09304
3. E. Acerbi, N. Fusco, and M. Morini, *Minimality via second variation for a nonlocal isoperimetric problem*, arXiv:1211.0164 (2012). https://arxiv.org/abs/1211.0164
4. H. Knüpfer and W. Shi, *Second Order Expansion for the Nonlocal Perimeter Functional*, Communications in Mathematical Physics (2022). https://doi.org/10.1007/s00220-022-04549-w
