# A countably faceted positivity frontier for quadratically modulated circle heat kernels

## Finding
Fix \(\tau>0\) and let \(q=e^{-\tau}\). On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let
\[
H_\tau(\theta)=\sum_{k\in\mathbb Z}q^{k^2}e^{ik\theta},\qquad
K_{\alpha,\beta}(x,y)=H_\tau(x-y)\,[1+\alpha\cos(x-y)+\beta\cos(2(x-y))]
\]
for arbitrary real \(\alpha,\beta\). Define \(y_n=\cosh(2\tau n)\), \(n\ge0\), and
\[
L_n(\beta)=-\frac{1+\beta q^4(2y_n^2-1)}{q y_n},\quad
\beta_n=\frac1{q^4(1+2y_ny_{n+1})},\quad
\alpha_n=-\frac{2(y_n+y_{n+1})}{q(1+2y_ny_{n+1})}.
\]
The complete parameter region of positive semidefinite kernels on all finite circle configurations is
\[
\boxed{\beta\ge0,\qquad \alpha\ge h_\tau(\beta)},
\]
where \(h_\tau(0)=0\) and, with \(\beta_{-1}=+\infty\),
\[
\boxed{h_\tau(\beta)=L_n(\beta)\quad\text{if}\quad
\beta_n\le\beta\le\beta_{n-1}\qquad(n=0,1,2,\ldots).}
\]
The numbers \(\beta_n\) are strictly decreasing to zero. The boundary consists of the ray \(\beta=0,\alpha\ge0\), the spectral ray \(\alpha=L_0(\beta)\) for \(\beta\ge\beta_0\), and a chain of genuine exposed line segments. The vertices of this chain are exactly \((\alpha_n,\beta_n)\), each saturating **two consecutive Fourier frequencies**; every open spectral segment saturates exactly one frequency. Thus no finite set of Fourier positivity inequalities describes this family.

The spectral boundary has a sharp non-power-law cusp. As \(\beta\downarrow0\),
\[
\boxed{\liminf_{\beta\downarrow0}\frac{-h_\tau(\beta)}{\sqrt\beta}
=2\sqrt2\,q,\qquad
\limsup_{\beta\downarrow0}\frac{-h_\tau(\beta)}{\sqrt\beta}
=\sqrt2(1+q^2).}
\]
These two numbers are distinct for every \(\tau>0\).

Every admissible kernel is strictly positive definite on any finite set of distinct circle sites. It is \(C\)-universal (its RKHS is uniformly dense in continuous functions) exactly when every Fourier coefficient is positive: that holds for \(\alpha>h_\tau(\beta)\) and also for every \(\beta=0,\alpha\ge0\), but not on the spectral boundary \(\beta>0,\alpha=h_\tau(\beta)\). In particular, non-universal spectral-boundary kernels converge in parameters to the universal heat kernel at \((0,0)\).

## Assumptions and scope
All assertions hold for each fixed real \(\tau>0\), all real modulation parameters and the full circle group. Positive semidefiniteness means every finite Hermitian kernel matrix \([K_{\alpha,\beta}(x_i,x_j)]\) is positive semidefinite; strict positive definiteness concerns distinct sites. The theta Fourier series converges absolutely with all derivatives. The normalization of the kernel at zero is not imposed; every admissible kernel has strictly positive diagonal and may be divided by that value if desired. No higher-dimensional sphere or general heat-spectrum extension is asserted.

## Proof
**1. Exact Fourier criterion.** The absolutely convergent Fourier series and product-to-sum identity give, for each integer \(k\),
\[
\widehat K(k)=q^{k^2}\left[1+\alpha q\cosh(2\tau k)+\beta q^4\cosh(4\tau k)\right]
=q^{k^2}F_{\alpha,\beta}(y_{|k|}),
\]
with \(F_{\alpha,\beta}(y)=2\beta q^4y^2+\alpha qy+1-\beta q^4\). The Herglotz–Bochner criterion on \(\mathbb T\) is \(\widehat K(k)\ge0\) for every \(k\in\mathbb Z\). If \(\beta<0\), the quadratic tends to \(-\infty\) as \(y_n\to\infty\), regardless of \(\alpha\). If \(\beta=0\), nonnegativity for every \(n\) is equivalent to \(\alpha\ge0\). For \(\beta>0\), dividing each condition by the positive \(q y_n\) gives exactly \(\alpha\ge L_n(\beta)\); therefore the boundary is the upper envelope of these affine functions.

**2. Exact vertices and completeness of the facet chain.** Since \(y_n\) strictly increases, so does \(1+2y_ny_{n+1}\); hence \(\beta_n\downarrow0\). For every \(n\ge0\), direct algebra at \((\alpha_n,\beta_n)\) yields the *global* factorization
\[
F_{\alpha_n,\beta_n}(y)
=\frac{2(y-y_n)(y-y_{n+1})}{1+2y_ny_{n+1}}.
\]
On the discrete increasing set \(\{y_j:j\ge0\}\), this is nonnegative, vanishes precisely at \(j=n,n+1\) and is positive elsewhere. Thus every \((\alpha_n,\beta_n)\) is admissible. The two independent Fourier equalities at consecutive frequencies make it an exposed vertex. The convex segment joining vertices \(n-1\) and \(n\) is admissible and lies on the equality line \(\alpha=L_n(\beta)\), proving this is the *sharp* boundary for \(\beta\in[\beta_n,\beta_{n-1}]\), \(n\ge1\). For \(n=0\), substitution of \(\alpha=L_0(\beta)=-q^{-1}-\beta q^3\) gives
\[
F_{\alpha,\beta}(y_j)=(y_j-1)\,[-1+\beta q^4(2y_j+1)].
\]
These are all nonnegative exactly when \(\beta\ge\beta_0\), proving the terminal ray. The case \(\beta=0\) was settled above. Conversely no parameter below the listed lines is admissible, since its active Fourier coefficient is negative. This proves the global classification and the exact zero modes. Non-redundancy of every inequality follows from its nonempty open edge.

**3. Cusp and its two sharp constants.** For \(n\ge1\), on its active facet write
\[
-h_\tau(\beta)=a_n+b_n\beta,
\quad a_n=(q y_n)^{-1},\quad b_n=q^3(2y_n-y_n^{-1}).
\]
The ratio to \(\sqrt\beta\) is \(a_n/\sqrt\beta+b_n\sqrt\beta\); it is minimized at
\(\beta_n^*=a_n/b_n=[q^4(2y_n^2-1)]^{-1}\).
As \(n\to\infty\), one has
\[
\beta_n\sim2q^{4n-2},\quad
\beta_{n-1}\sim2q^{4n-6},\quad
\beta_n^*\sim2q^{4n-4},
\]
so \(\beta_n^*\) lies strictly inside the active segment for all sufficiently large \(n\). Its minimum ratio is
\(2\sqrt{a_nb_n}=2q\sqrt{2-y_n^{-2}}\to2\sqrt2\,q\).
As a function of \(\sqrt\beta\), the ratio is convex, so its maximum on each closed segment occurs at one of its two endpoints. At either vertex, the exact formulas above yield
\[
\frac{-\alpha_n}{\sqrt{\beta_n}}\longrightarrow\sqrt2(1+q^2).
\]
As the active segments exhaust all sufficiently small \(\beta>0\), these are precisely the liminf and limsup. Their difference is \(\sqrt2(1-q)^2>0\).

**4. Strictness versus universality.** Every admissible kernel has strictly positive Fourier coefficients at all sufficiently large positive and negative integer frequencies: for \(\beta>0\), the positive quadratic term dominates; for \(\beta=0\), all coefficients are positive. If a finite distinct-site Gram quadratic form vanishes, its nonnegative Fourier sum forces \(\sum_jc_je^{ikx_j}=0\) for all sufficiently large consecutive \(k\). A square Vandermonde matrix in the distinct numbers \(e^{ix_j}\) is invertible, so all coefficients \(c_j\) vanish. This proves finite-site strict positive definiteness. The RKHS contains each trigonometric character whose kernel Fourier coefficient is positive. Hence, if all coefficients are positive, it contains the trigonometric polynomials, which are dense by Stone–Weierstrass. If one Fourier coefficient vanishes, the corresponding bounded Fourier functional annihilates the RKHS and its uniform closure, excluding the associated character. The boundary factorization and strict inequalities already determine the exact spectral zeros and complete the universality claim.

## Verification
`CHECK.py` evaluates the Fourier polynomial and vertex factorization exactly over rational values of \(q\), checks each proposed exposed segment, tests the forced high-frequency obstruction for negative \(\beta\) or for \(\beta=0,\alpha<0\). The cusp constants are established analytically above, not by finite sampling. These finite checks supplement, rather than establish, the all-parameter and asymptotic proofs.

## Relationship to prior work
Arhancet and Li (2026) describe the global convex structure of normalized positive-definite functions on compact groups and the Fourier-multiplier interpretation. Their general framework does not compute the two-parameter theta-kernel section, its countably infinite exposed edges, or its cusp constants. The accessible published geodesic-exponential circle modulation result studies \(e^{-a|\theta|}(1+b\cos\theta)\) with **one** signed parameter and rational/parity-dependent Fourier coefficients, not the periodic Gaussian heat kernel with two harmonics and quadratic-in-\(\cosh\) spectrum. The published two-cosine exponential kernel instead has an exponential-of-cosines profile and a nonnegative-quadrant parameter cone; that result neither implies nor contains the present infinite-facet cone. General circle Fourier positivity and standard wrapped-normal heat-kernel identities are used as known premises, not claimed as discoveries.

## Limitations
The sharp cone and cusp are only for the stated two-harmonic multiplicative perturbation of the wrapped Gaussian heat kernel at fixed \(\tau>0\). A literature search cannot establish global historical uniqueness; older covariance-model or theta-function literature might contain an equivalent parameter description. The result is an analytic derivation with finite supplemental checks, not an independently audited mathematical certification. No claims are made about arbitrary trigonometric multipliers, noisy kernel estimation, or higher-dimensional groups.

## References
1. C. Arhancet and L. Li, *On the convex structure of the space of quantum channels which act as Fourier multipliers*, arXiv:2603.00276, first submitted 2026-02-27, https://arxiv.org/html/2603.00276v4 .
2. *Sharp circle-covariance modulation threshold and an unbounded Fourier-mode staircase*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-circle-covariance-modulation-threshold-and-an-unbounded-fo--3df14ed06eed .
3. *Two-harmonic circle exponentials: the sharp positive-type cone and infinite spectral obstructions*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-harmonic-circle-exponentials-the-sharp-positive-type-cone-an--8f4e14149944 .
4. *Wrapped normal distribution*, standard circle heat-kernel Fourier-series description, https://en.wikipedia.org/wiki/Wrapped_normal_distribution .
