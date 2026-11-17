# Sharp odd-composite one-impulse Gabor tomography conditioning

## Finding
For every **odd composite integer** \(n\ge9\), define the normalized one-coordinate-impulse window on \(\mathbb Z_n\) by
\[
h_z=\frac{\mathbf1+z\delta_0}{\sqrt{n+|z|^2+2\operatorname{Re}z}},\qquad z\in\mathbb C.
\]
Take its full \(n^2\) cyclic time-frequency orbit and the complex-linear intensity lifting \(\mathcal L_z:M_n(\mathbb C)\to\mathbb C^{n^2}\). With Hilbert--Schmidt and Euclidean norms, assigning infinite condition number to singular liftings, the **exact minimax condition number** and the **unique minimizer** are
\[
\boxed{\min_{z\in\mathbb C}\kappa(\mathcal L_z)
 =\frac{\sqrt n-1}{\sin(\pi/(2n))},\qquad
 z_{\mathrm{opt}}=-\sqrt n.}
\]
The minimizing window is **real** and has coordinate \(1-\sqrt n\) at the exceptional site. Its smallest and largest lifting singular values are respectively
\[
\boxed{s_{\min}=\frac{\sqrt n\sin(\pi/(2n))}{\sqrt n-1},\qquad s_{\max}=\sqrt n.}
\]
The optimal lifting is injective on all complex matrices, and hence its intensity measurements identify every vector up to global phase. Its condition number has asymptotic behavior \(\kappa_{\mathrm{opt}}\sim(2/\pi)n^{3/2}\) along odd composite orders.

## Assumptions and scope
For \(a,b,j\in\mathbb Z_n\), let \((T_a f)(j)=f(j-a)\) and \((M_b f)(j)=e^{2\pi i bj/n}f(j)\). Put \(v_{a,b}=M_bT_a h_z\), and let
\[
\mathcal L_z(X)=\bigl(\operatorname{tr}(Xv_{a,b}v_{a,b}^*)\bigr)_{a,b\in\mathbb Z_n}.
\]
All nonzero and zero parameters \(z\) are allowed. The normalization denominator is strictly positive because it equals \(n-1+|1+z|^2\). The theorem concerns **linear operator tomography**, a sufficient but stronger property than phase retrieval, and does not claim full spark or nonlinear stability in another metric. The order \(n\) is odd and composite; the prime and even-order problems have distinct previously studied formulas, and are not included in the new result.

## Proof
**1. Diagonalization.** Let \(B=n+|z|^2+2\operatorname{Re}z\). The Weyl operators \(n^{-1/2}M_bT_a\) form an orthonormal Hilbert--Schmidt basis. Translation/modulation covariance and the two-dimensional finite Fourier transform show that the singular values of \(\mathcal L_z\) are precisely \(\sqrt n\,|A_z(a,b)|\), where \(A_z(a,b)=\langle h_z,M_bT_a h_z\rangle\) (with harmless coordinate reflection). The identity coefficient is \(A_z(0,0)=1\), and Cauchy--Schwarz bounds every \(|A_z(a,b)|\le1\), so \(s_{\max}=\sqrt n\) for every parameter.

A direct sum over exceptional sites gives all **unnormalized ambiguity magnitudes** \(B|A_z(a,b)|\):
\[
\begin{array}{c|c}
(a,b)&B|A_z(a,b)|\\ \hline
(0,0)&B\\
(0,b),\ b\ne0&\bigl||z|^2+2\operatorname{Re}z\bigr|\\
(a,0),\ a\ne0&\bigl|n+2\operatorname{Re}z\bigr|\\
(a,b),\ a\ne0,\ b\ne0&\bigl|z+\overline z\,e^{2\pi i ab/n}\bigr|
\end{array}
\]
The last row permits \(ab\equiv0\pmod n\) even though each index is nonzero; this distinction is essential at composite orders.

**2. Zero-divisor completion of the phase grid.** Every nonzero residue \(j\) is \(ab=j\) with \(a=1\) and \(b=j\). Since \(n\) is composite, choose \(1<d<n\) dividing \(n\); the nonzero labels \(a=d\), \(b=n/d\) also give \(ab=0\pmod n\). Hence the mixed labels sample **every** residue \(j\in\mathbb Z_n\). For \(z=t e^{i\phi}\) with \(t>0\), their smallest magnitude is
\[
2t\mu_n(\phi),\qquad
\mu_n(\phi)=\min_{j\in\mathbb Z_n}
\left|\cos\left(\phi-\frac{\pi j}{n}\right)\right|.
\]
The zero phases of these cosines, considered modulo \(\pi\), form a uniform grid with spacing \(\pi/n\). Thus \(\mu_n(\phi)\le\sin(\pi/(2n))\). Because \(n\) is odd, \(\phi=\pi\) is **exactly a midpoint** between consecutive zero phases, and attains equality.

**3. Exact complex minimax upper bound.** For \(z\ne0\), the mixed labels give
\[
\frac{s_{\min}}{s_{\max}}
\le\frac{2t\mu_n(\phi)}{n+t^2+2t\cos\phi}
\le\frac{\mu_n(\phi)}{\sqrt n+\cos\phi}
\le\frac{\sin(\pi/(2n))}{\sqrt n-1}.
\]
The middle inequality is \(t+n/t\ge2\sqrt n\), with equality only at \(t=\sqrt n\); the last inequality uses \(\mu_n\le\sin(\pi/(2n))\) and \(\cos\phi\ge-1\). All denominators are positive for \(n\ge9\). Both equality conditions hold simultaneously only when \(t=\sqrt n\) and \(\phi=\pi\pmod {2\pi}\). If \(z=0\), all mixed ambiguity coefficients vanish and the lifting is singular.

**4. Attainment, including unmixed directions.** Set \(z=-\sqrt n\) and \(\delta=\pi/(2n)\). Now \(B=2n-2\sqrt n\); the minimum mixed unnormalized magnitude equals \(2\sqrt n\sin\delta\). Each nontrivial unmixed magnitude equals \(n-2\sqrt n\). For odd composite \(n\ge9\),
\[
n-2\sqrt n\ge2\sqrt n\sin\delta,
\]
since \(\sqrt n-2\ge1>2\sin(\pi/18)\ge2\sin\delta\). Thus no unmixed coefficient undercuts the mixed minimum. Every coefficient is strictly positive, and
\[
\frac{s_{\min}}{s_{\max}}
=\frac{2\sqrt n\sin\delta}{2n-2\sqrt n}
=\frac{\sin\delta}{\sqrt n-1}.
\]
This attains the global upper bound and proves both uniqueness and the exact smallest singular value. Injectivity of the lifted map implies uniqueness of rank-one projectors from intensity data, and hence global-phase retrieval. Taylor expansion of the sine gives the asserted asymptotic.

## Verification
The companion `CHECK.py` directly reconstructs all ambiguity magnitudes at the analytic optimizer for several odd composite dimensions, checks the closed sharp bound against sampled complex parameters, and constructs the actual Hilbert--Schmidt lifting matrix at order nine to compare its singular values. Run `python3 CHECK.py` with Python 3 and NumPy. The finite checks are corroboration only: the proof above establishes the result for **every** odd composite order and **every** complex parameter.

## Relationship to prior work
The standard Weyl-ambiguity singular-value diagonalization is due to established finite Gabor-frame theory, including Bojarovska--Flinth (2015); it is not new here. A previously published sharp minimax theorem for the **same window family at prime orders** gives a different optimum, \(\sqrt p/\sin(\pi/p)\), attained at imaginary impulse \(z=\pm i\sqrt p\). That prime statement cannot cover composite orders: nonzero translation and modulation labels now have a product equal to zero, making its imaginary optimizer singular. A prior exact one-impulse minimax theorem at **even composite** orders gives \((\sqrt n-\cos(\pi/(2n)))/\sin(\pi/(2n))\), attained at two nonreal impulses. Neither of these results implies the real, uniquely optimal **odd-composite** branch. An earlier all-order one-coordinate rank discriminant establishes which impulses are informationally complete, but not their sharp conditioning. The 2026 paper by Li develops other explicit Gabor windows with quantitative stability; its publicly available abstract does not assert the restricted odd-composite minimax proved here. The distinct optimizer and exact phase-grid mechanism supply the remaining natural arithmetic regime of this particular family.

## Limitations
The theorem is restricted to one-coordinate modifications of a flat cyclic window, full time-frequency measurements, and odd composite dimensions. It does not assert optimality among general windows, full spark, resilience to deleted measurements, or nonlinear noise stability. The comparison with Li (2026) is abstract-level because its full text was inaccessible during this investigation; a hidden specialized result in that or unindexed literature remains a publication-priority risk. No independent mathematical audit has been performed.

## References
1. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614, first submitted 2026-09-09, MSC2020 42C15 (among listed classes). https://arxiv.org/abs/2609.09614
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first submitted 2015-03-19. https://arxiv.org/abs/1503.05800
3. *Optimal complex impulse in prime-cyclic Gabor tomography: a sharp conditioning barrier*, research record `c114096c73ba`. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-optimal-complex-impulse-in-prime-cyclic-gabor-tomography-a-sharp--c114096c73ba
4. *Exact rank discriminant for one-coordinate cyclic Gabor measurements*, research record `4ad1eba7465a`. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rank-discriminant-for-one-coordinate-cyclic-gabor-measurem--4ad1eba7465a
5. X. Zhu and Y. Wang, *Uniformly Stable Minimal Weyl--Heisenberg Measurements Approaching the SIC Benchmark*, arXiv:2608.11850, 2026. https://arxiv.org/abs/2608.11850
