# An all-scale geodesic Laplace obstruction on real projective spaces

## Finding
Equip the real projective space \(\mathbb{RP}^{m}\), \(m\ge1\), with the quotient of the unit round-sphere metric, so that for unit representatives \(x,y\in\mathbb R^{m+1}\) the geodesic distance is
\[
\vartheta([x],[y])=\arccos|\langle x,y\rangle|\in[0,\pi/2].
\]
For any real damping parameter \(a>0\), define the continuous geodesic Laplace kernel
\[
K_a([x],[y])=e^{-a\vartheta([x],[y])}.
\]
**Sharp projective-dimension dichotomy:** \(K_a\) is strictly positive definite on every finite set of distinct projective points of \(\mathbb{RP}^{1}\), whereas it fails even positive semidefiniteness on some finite point set of \(\mathbb{RP}^{m}\) whenever \(m\ge2\), for **every** \(a>0\).

More precisely, let \(P_j\) denote the usual Legendre polynomial normalized by \(P_j(1)=1\). On \(\mathbb{RP}^{2}\), the unnormalized degree-\(2n\) zonal coefficient
\[
I_{2n}(a)=\int_{-1}^1e^{-a\arccos|t|}P_{2n}(t)\,dt
\]
satisfies, for each fixed \(a>0\),
\[
\boxed{I_{2n}(a)=\frac{(-1)^{n+1}a e^{-a\pi/2}}{2\sqrt{\pi}\,n^{5/2}}+o_a(n^{-5/2})\qquad(n\to\infty).}
\]
In particular \(I_{4k}(a)<0\) for all sufficiently large integers \(k\). Thus even after freely selecting the damping parameter, the intrinsic Laplace covariance cannot be used on any real projective space of dimension at least two. The positive-definite behavior on the projective line is the exceptional sharp boundary.

## Assumptions and scope
The distance is **intrinsic geodesic distance** on a unit-curvature real projective quotient, not chordal/projection/Frobenius distance. Positive semidefiniteness means that for all finite projective point sets the real kernel Gram matrix is positive semidefinite; strict positive definiteness additionally requires positivity for distinct sites and nonzero coefficient vectors. The negative Legendre asymptotic is a fixed-\(a\) limit, not uniform as \(a\) varies or an effective bound on the first negative degree. The conclusion is valid for each integer \(m\ge2\) and each \(a>0\). No condition on finite sample cardinality independent of \(a\) is claimed.

## Proof
**1. Projective-line positivity.** Identify \(\mathbb{RP}^{1}\) with a circle of circumference \(\pi\), using angular coordinates modulo \(\pi\). Its distance is \(\min_{j\in\mathbb Z}|\theta-\phi+j\pi|\). Apart from a positive normalization, the real Fourier coefficients of \(e^{-a\vartheta}\) are
\[
B_k(a)=\int_0^{\pi/2}e^{-at}\cos(2kt)\,dt
=\frac{a\{1-(-1)^k e^{-a\pi/2}\}}{a^2+4k^2}>0,\qquad k\in\mathbb Z.
\]
Since \(B_k(a)=O_a((1+|k|)^{-2})\), the Fourier series converges absolutely and uniformly. All its coefficients are strictly positive, so the kernel is positive semidefinite. For distinct angles \(\theta_j\) modulo \(\pi\), the quadratic form is a positive constant times \(\sum_{k\in\mathbb Z} B_k(a)|\sum_j c_j e^{2ik\theta_j}|^2\). It vanishes only if each Fourier moment vanishes, and already the moments \(k=0,\ldots,s-1\) form a nonsingular Vandermonde matrix for \(s\) distinct sites. Hence the kernel is strictly positive definite.

**2. The exact Legendre integration identity.** On the northern half interval put
\[
f(t)=e^{-a\arccos t},\quad 0\le t\le1,\qquad g(t)=(1-t^2)f'(t)=a\sqrt{1-t^2}\,f(t).
\]
Then \(f'(0)=a e^{-a\pi/2}\), \(g(1)=0\), and \(g\) is absolutely continuous with \(g'(t)=a f(t)\bigl(a-t/\sqrt{1-t^2}\bigr)\in L^1(0,1)\). For even \(\ell\ge2\), use \(P_\ell'(0)=0\) and the Legendre Sturm–Liouville equation
\[
\bigl((1-t^2)P_\ell'(t)\bigr)'=-\ell(\ell+1)P_\ell(t).
\]
Two integrations by parts, justified first on \([0,1-\varepsilon]\) and then by absolute continuity of \(g\), give the **exact** identity
\[
\boxed{\int_{-1}^1 f(|t|)P_\ell(t)\,dt
=-\frac{2f'(0)P_\ell(0)}{\ell(\ell+1)}
-\frac{2}{\ell(\ell+1)}\int_0^1g'(t)P_\ell(t)\,dt.}
\]
The nonzero endpoint term at \(t=0\) captures the cut-locus cusp of \(f(|t|)\). It is absent for a smooth even function of \(t\), and it is the source of the alternating sign.

**3. The remainder is asymptotically smaller.** Set \(J_\ell=\int_0^1g'(t)P_\ell(t)\,dt\). Under \(t=\cos\theta\),
\[
J_\ell=a\int_0^{\pi/2} e^{-a\theta}\bigl(a\sin\theta-\cos\theta\bigr)P_\ell(\cos\theta)\,d\theta.
\]
We show \(J_\ell=o_a(\ell^{-1/2})\) as \(\ell\to\infty\). Fix \(0<\delta<\pi/4\). On \([\delta,\pi/2]\), the standard compact-angle Legendre asymptotic
\[
P_\ell(\cos\theta)
=\sqrt{\frac{2}{\pi(\ell+1/2)\sin\theta}}
\cos\bigl((\ell+1/2)\theta-\pi/4\bigr)+O_\delta(\ell^{-3/2})
\]
and the Riemann–Lebesgue lemma give \(\sqrt\ell\,\int_\delta^{\pi/2}e^{-a\theta}(a\sin\theta-\cos\theta)P_\ell(\cos\theta)\,d\theta\to0\). For the remaining interval, the classical Legendre bounds
\[
|P_\ell(\cos\theta)|\le1,\qquad |P_\ell(\cos\theta)|\le C\bigl(\ell\sin\theta\bigr)^{-1/2}
\]
imply, by splitting at \(\theta=1/\ell\),
\[
\sqrt\ell\left|\int_0^\delta e^{-a\theta}(a\sin\theta-\cos\theta)P_\ell(\cos\theta)\,d\theta\right|
\le C_a(\ell^{-1/2}+\sqrt\delta).
\]
Taking the limit superior as \(\ell\to\infty\), and then letting \(\delta\downarrow0\), yields the required \(J_\ell=o_a(\ell^{-1/2})\). The quoted bounds follow from the usual Legendre Hilb/Bernstein estimates; no numerical limit is used to justify this step.

**4. Sharp alternating coefficient and the obstruction.** For \(\ell=2n\), the exact central value and Stirling formula are
\[
P_{2n}(0)=(-1)^n\frac{\binom{2n}{n}}{4^n}
=\frac{(-1)^n}{\sqrt{\pi n}}\bigl(1+O(n^{-1})\bigr).
\]
Substitute this and Step 3 into Step 2 and use \((2n)(2n+1)=4n^2(1+O(n^{-1}))\) to obtain the announced asymptotic, including its nonzero coefficient and alternating sign. Because a continuous rotation-invariant positive semidefinite kernel on the sphere has nonnegative integral-operator eigenvalues in every spherical-harmonic degree, a negative even-degree Legendre coefficient contradicts positive semidefiniteness on \(\mathbb{RP}^{2}\) (equivalently, on its double cover \(S^2\), where the kernel is antipodally invariant). This follows directly from the spherical addition theorem/Funk–Hecke formula, or from approximation of the continuous integral quadratic form by finite weighted point sums. Finally, for \(m\ge2\), the coordinate embedding \(\mathbb R^3\hookrightarrow\mathbb R^{m+1}\) induces an isometric totally geodesic embedding \(\mathbb{RP}^{2}\hookrightarrow\mathbb{RP}^{m}\). Every finite negative witness in the smaller space persists in the larger one. Combined with Step 1 this proves the dichotomy.

## Verification
The companion `CHECK.py` uses Python's standard library to compare the exact two-integration-by-parts identity with independent smooth-angle Simpson quadrature for 18 damping/order pairs, to exhibit three illustrative negative Legendre coefficients at specified finite orders, and to check 90 strictly positive projective-circle Fourier coefficients against numerical integrals. Running `python3 CHECK.py` produces `VERIFY_OK 111`. These finite observations supplement rather than establish the quantified all-parameter result; the proof is Steps 1–4. The large-degree threshold may be very high at strong damping, and the proof gives no effective universal finite-point witness count.

## Relationship to prior work
Robertson, *Crofton formulae and geodesic distance in hyperbolic spaces* (arXiv:1302.5790, Section 5), gives an explicit six-point witness that projective geodesic **distance is not of negative type**. By Schoenberg's equivalence, this rules out Laplace-kernel positive definiteness **for all scales collectively**, not at each individual scale. Feragen–Lauze–Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict* (arXiv:1411.0296, Theorem 4 and Table 2), state precisely the all-scales/negative-type equivalence, without the present individual-scale no-go or alternating Legendre asymptotic. Da Costa–Mostajeran–Ortega (arXiv:2302.10623v1) establish an every-scale failure for the **squared-distance Gaussian** kernel via circles, which is different: the **linear-distance Laplace** kernel is strictly positive definite on the projective circle. Bilyk–Grabner (arXiv:2410.22104v1, especially Sections 2, 3 and 6) give projective Jacobi spectral criteria and detailed **geodesic Riesz power** analysis, including the negative-type obstruction and projective-space parameter subtleties; they do not establish the fixed-scale Laplace exponential coefficient asymptotic proved here. The use of the standard Legendre operator, Fourier positivity, and Bernstein/Hilb estimates is classical; the new statement is the sharp all-positive-damping failure, its explicit signed asymptotic, and its dimension-one boundary.

## Limitations
The result is specific to the intrinsic round metric on **real** projective spaces. The proof of universal failure uses a projective-plane restriction and does not classify all coefficients, the lowest negative degree, or a smallest finite negative witness. The little-oh term is for fixed positive damping and need not be uniform as damping becomes large or small. The conclusion is not about other projective distances or Gaussian kernels. Theoretical priority remains conditional on the inspected literature; a historically unindexed equivalent is possible. No independent mathematical audit has been performed.

## References
1. N. Da Costa, C. Mostajeran and J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623v1 (first posted 2023-02-21), https://arxiv.org/abs/2302.10623.
2. G. Robertson, *Crofton formulae and geodesic distance in hyperbolic spaces*, arXiv:1302.5790 (posted 2013; earlier paper), https://arxiv.org/abs/1302.5790, Section 5.
3. A. Feragen, F. Lauze and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (posted 2014), https://arxiv.org/abs/1411.0296, Theorem 4.
4. D. Bilyk and P. Grabner, *Positive definite singular kernels on two-point homogeneous spaces*, arXiv:2410.22104v1 (posted 2024-10-29), https://arxiv.org/abs/2410.22104, Sections 2, 3, 6.
5. NIST Digital Library of Mathematical Functions, Chapter 18 (orthogonal-polynomial asymptotics and classical Legendre estimates), https://dlmf.nist.gov/18.15; see also G. Szegő, *Orthogonal Polynomials*, AMS, 4th ed. (1975).
