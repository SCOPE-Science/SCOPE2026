# Two lattice phases and a strict parity gap in cubic Boolean projection constants

## Finding
For an integer \(n\geq3\), let \(E_n\) be the **real** homogeneous degree-three Walsh subspace of \(\ell_\infty(\{-1,1\}^n)\), with its supremum norm. Write \(\lambda_n\) for its absolute Banach-space projection constant, equivalently the minimum norm of a projection from \(\ell_\infty(\{-1,1\}^n)\) onto \(E_n\).

Put
\[
\phi_0=\frac1{\sqrt{2\pi}},\qquad \phi_*=\phi_0e^{-3/2},\qquad
c=\frac{\phi_0+4\phi_*}{3},\qquad B_2(t)=\{t\}^2-\{t\}+\frac16,
\]
where \(\{t\}=t-\lfloor t\rfloor\). Set \(\varepsilon_n\in\{0,1\}\) to be the parity of \(n\), and \(\vartheta_n=\{(\sqrt{3n}-\varepsilon_n)/2\}\). Then
\[
\boxed{\lambda_n=c\,n^{3/2}+\sqrt n\left[-\phi_0\left(\frac5{12}+2B_2(\varepsilon_n/2)\right)
-\phi_*\left(\frac23+8B_2(\vartheta_n)\right)\right]+o(\sqrt n).}
\]
The leading term \(c\,n^{3/2}\) is **previously published**, not part of the novelty claim. The new conclusion is its sharp, parity-dependent second-order lattice term and the exact subsequential ranges. For \(R_n=(\lambda_n-c n^{3/2})/\sqrt n\), the set of subsequential limits along even integers is precisely
\[
\left[-\frac{3\phi_0}{4}-2\phi_*,\;-\frac{3\phi_0}{4}\right],
\]
and along odd integers it is precisely
\[
\left[-\frac{\phi_0}{4}-2\phi_*,\;-\frac{\phi_0}{4}\right].
\]
These compact intervals are disjoint: the odd lower endpoint exceeds the even upper endpoint by
\[
\phi_0\left(\frac12-2e^{-3/2}\right)>0.
\]
In particular, \(\liminf R_n=-3\phi_0/4-2\phi_*\) and \(\limsup R_n=-\phi_0/4\). The order-\(\sqrt n\) term has no single limiting coefficient, even after fixing parity.

## Assumptions and scope
For \(x=(x_1,\ldots,x_n)\in\{-1,1\}^n\) and \(S\subseteq[n]\), write \(\chi_S(x)=\prod_{i\in S}x_i\). The space \(E_n=\operatorname{span}_{\mathbb R}\{\chi_S:|S|=3\}\) is endowed with \(\|f\|_\infty=\max_x|f(x)|\). A projection is a real-linear map \(P:\ell_\infty(\{-1,1\}^n)\to E_n\) with \(P|_{E_n}=I\), and the absolute projection constant is the supremum of minimal projection norms over all isometric superspaces. These definitions give the stated equality by injectivity of finite-dimensional \(\ell_\infty\).

The Gaussian \(\phi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and probabilists' Hermite polynomials \(H_3(z)=z^3-3z\), \(H_4(z)=z^4-6z^2+3\) will be used below. All asymptotic limits are over integer \(n\to\infty\). No analogous statement is asserted for complex projection constants, other degrees, or nonuniform signs.

## Proof
**1. Exact reduction.** Averaging any projection over sign translations produces a translation-equivariant projection without increasing its norm. The only translation-equivariant projection onto \(E_n\) is the degree-three Fourier--Walsh projection, whose convolution kernel is \(K_{n,3}(x)=\sum_{|S|=3}\chi_S(x)\). Therefore \(\lambda_n=\mathbb E|K_{n,3}(X)|\) for independent uniform signs \(X_i\). The elementary symmetric polynomial identity, with \(S_n=\sum_iX_i\), gives
\[
K_{n,3}=\frac{S_n^3-(3n-2)S_n}{6}.
\]
This exact projection formula, and its leading Gaussian asymptotic, are already covered by the general results of Defant--Galicer--Mansilla--Mastyło--Muro [2]. We invoke them only as the starting point for the new expansion.

An independent exact rational finite formula is useful for verification: set \(D_n(j)=\binom{n-3}{j}-2\binom{n-3}{j-1}+\binom{n-3}{j-2}\), with out-of-range binomial coefficients zero. Let \(J_n\) be the largest integer \(j\ge-1\) with \(n-2j>\sqrt{3n-2}\), considering indices in \(0\le j\le n\); when none exists put \(J_n=-1\), and let \(J_n^0=\lfloor(n-1)/2\rfloor\). Then
\[
\lambda_n=\frac{\binom n3}{2^n}\left(4D_n(J_n)-2D_n(J_n^0)\right).
\]
Indeed, \(\binom nk K_{n,3}(n-2k)=\binom n3[\binom{n-3}{k}-3\binom{n-3}{k-1}+3\binom{n-3}{k-2}-\binom{n-3}{k-3}]\), whose partial sum is \(\binom n3D_n(j)\). Splitting the alternating sign of the cubic kernel at its roots \(0,\pm\sqrt{3n-2}\) and using symmetry yields this formula. Points at roots contribute zero, so the strict inequality convention is immaterial.

**2. Distributional expansion with quantified remainder.** Write \(Z_n=S_n/\sqrt n\) and \(h=2/\sqrt n\). Its support is the shifted lattice \(h(\mathbb Z+\varepsilon_n/2)\). The exact identity becomes
\[
\frac{K_{n,3}}{n^{3/2}}=\frac{H_3(Z_n)}6+\frac{Z_n}{3n}.
\]
Stirling's formula applied to \(2^{-n}\binom n{(n+\sqrt n z)/2}\) gives, uniformly for lattice sites \(|z|\le n^{1/16}\),
\[
\Pr\{Z_n=z\}=h\phi(z)\left(1-\frac{H_4(z)}{12n}+O\left(\frac{1+|z|^{12}}{n^2}\right)\right).
\]
The implicit constant is absolute. For \(|z|>n^{1/16}\), Hoeffding's bound and polynomial moment bounds give a contribution smaller than every inverse power of \(n\) to the normalized first absolute moment. Consequently all \(n^{-1}\) terms may be computed from the displayed lattice expansion, with an \(o(n^{-1})\) error. In passing from \(|H_3(z)/6+z/(3n)|\) to \(|H_3(z)|/6+(z/(3n))\operatorname{sgn}H_3(z)\), the remainder in the lattice expectation is \(o(n^{-1})\): outside \(O(n^{-1})\) neighborhoods of the three simple roots the equality is exact; inside, there are at most boundedly many lattice sites, and each has probability \(O(n^{-1/2})\) and pointwise error \(O(n^{-1})\).

**3. Smooth Gaussian correction.** Taking integrals of the order-\(n^{-1}\) terms produces
\[
A=\frac13\mathbb E[Z\operatorname{sgn}H_3(Z)]-\frac1{72}\mathbb E[|H_3(Z)|H_4(Z)]
=-\frac{5\phi_0}{12}-\frac{2\phi_*}{3},
\]
where \(Z\) is standard normal. To check explicitly, integration on intervals separated by \(-\sqrt3,0,\sqrt3\), using \(\phi'(z)=-z\phi(z)\), gives \(\mathbb E[Z\operatorname{sgn}H_3(Z)]=4\phi_*-2\phi_0\) and \(\mathbb E[|H_3(Z)|H_4(Z)]=144\phi_*-18\phi_0\). The zeroth-order integral is \(\int |H_3(z)|\phi(z)\,dz/6=c\).

**4. Lattice-cusp contribution.** Set \(f(z)=\phi(z)|H_3(z)|/6\). This function and its first derivative are smooth except for three derivative jumps: \(\Delta f'(0)=\phi_0\), and \(\Delta f'(\pm\sqrt3)=2\phi_*\). The shifted trapezoidal sum for an exponentially decaying piecewise-\(C^3\) function with derivative jumps satisfies the cusp-corrected Euler--Maclaurin formula
\[
h\sum_{z\in h(\mathbb Z+\alpha)} f(z)-\int_{\mathbb R}f(z)\,dz
=-\frac{h^2}{2}\sum_{a\in\{0,\pm\sqrt3\}}\Delta f'(a)
B_2(\{a/h-\alpha\})+O(h^3).
\]
For completeness, split at the jump points, integrate by parts twice on each smooth interval, and apply the Fourier series \(B_2(\{t\})=(1/\pi^2)\sum_{k\ge1}\cos(2\pi kt)/k^2\) to the jump boundary terms; the regular second derivative has integrable first derivative away from these finitely many points and yields \(O(h^3)\). Substituting \(h=2/\sqrt n\) and \(\alpha=\varepsilon_n/2\), and using the symmetry \(B_2(\{-t\})=B_2(\{t\})\), gives
\[
\frac1n\left[-2\phi_0B_2(\varepsilon_n/2)-8\phi_*B_2\big(\{(\sqrt{3n}-\varepsilon_n)/2\}\big)\right]+o(n^{-1}).
\]
The exact nonzero roots of the finite-\(n\) cubic are \(\pm\sqrt{3n-2}\), rather than \(\pm\sqrt{3n}\); the replacement changes the phase by \(O(n^{-1/2})\) and hence the bounded Lipschitz \(B_2\) term by \(o(1)\). The smooth corrections are evaluated by ordinary lattice Riemann sums with \(o(1)\) error. Combining steps 2--4 and multiplying the normalized expectation by \(n^{3/2}\) proves the boxed expansion.

**5. All subsequential limits and separation.** On even \(n\), \(B_2(\varepsilon_n/2)=B_2(0)=1/6\), while on odd \(n\) it equals \(B_2(1/2)=-1/12\). Since the range of \(B_2\) on fractional phases is \([-1/12,1/6]\), the two claimed intervals follow. Each value is actually attained as a subsequential limit: for any chosen \(\theta\in[0,1]\) and fixed parity \(\varepsilon\), choose the nearest integer of parity \(\varepsilon\) to \((2k+2\theta+\varepsilon)^2/3\) as \(k\to\infty\). Its phase \(\{(\sqrt{3n}-\varepsilon)/2\}\) approaches \(\theta\) modulo one, so every Bernoulli value is approached. Finally, \(e^{3/2}>4\) gives the strict interval gap.

## Verification
The accompanying `verify_cubic_projection.py` independently compares the finite binomial expectation and its boundary-binomial expression in exact rational arithmetic for 148 dimensions \(3\le n\le150\); it directly enumerates Walsh cubic characters in eight dimensions \(3\le n\le10\); and it checks the phase correction against high-precision calculations at six larger dimensions. The checker reports `ALL_CUBIC_WALSH_PROJECTION_CHECKS_PASSED`. These are finite consistency tests; the asymptotic theorem is proved by the analytic estimates above, not by them. The coefficient calculations, parity cases, boundary conventions and omitted \(o(\sqrt n)\) terms are separately explicit in the proof.

## Relationship to prior work
Defant et al. [2, Chapter 8, Theorem 8.1.1] already give the **exact projection-constant expectation** for all Walsh sets. Their Theorem 8.2.5 and the displayed degree-three example on the following page already supply the **leading coefficient** \(c\). Neither of those published statements gives the displayed \(\sqrt n\)-order oscillatory correction or separates the two parity limit bands. The degree-two lattice-phase result [4] is an important comparison but concerns a different Hermite polynomial: here the third-order Gaussian kernel has three absolute-value cusps and two interacting phases, leading to disjoint parity bands rather than a single phase interval. Harrow--Kolla--Schulman [1] and Kirshner--Samorodnitsky [3] discuss relevant Boolean spherical/Krawtchouk spectral structure but not the stated correction. Thus the claim is a refinement of an existing leading asymptotic, **not** an independent discovery of the exact kernel representation or first-order constant.

## Limitations
The result treats exactly degree three, the real supremum norm and the uniform Boolean cube. It gives an \(o(\sqrt n)\) remainder and the complete second-order subsequential range, but no explicit nonasymptotic uniform error constant or third-order expansion. No assertion of precedence over all unpublished literature or of independent validation is made. The closest publicly indexed degree-two lattice-phase formula could motivate a similar approach; the absence of an identified published degree-three counterpart is not proof of absolute novelty.

## References
1. A. W. Harrow, A. Kolla and L. J. Schulman, *Dimension-free L2 maximal inequality for spherical means in the hypercube*, arXiv:1209.4148 (first public version September 19, 2012), Section 2, https://arxiv.org/abs/1209.4148.
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467 (August 12, 2022), Chapter 8, Theorems 8.1.1 and 8.2.5, https://arxiv.org/abs/2208.06467.
3. N. Kirshner and A. Samorodnitsky, *A moment ratio bound for polynomials and some extremal properties of Krawchouk polynomials and Hamming spheres*, arXiv:1909.11929 (September 26, 2019), Section 2, https://arxiv.org/abs/1909.11929.
4. *A lattice-phase second term for second-chaos projection constants on the Boolean cube*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-lattice-phase-second-term-for-second-chaos-projection-constant--ec79809353f9 (related degree-two setting; record summary consulted, not a full-text inspection).
