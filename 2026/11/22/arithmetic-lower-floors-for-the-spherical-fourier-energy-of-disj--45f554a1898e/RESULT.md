# Arithmetic lower floors for the spherical Fourier energy of disjoint balls

## Finding
Let \(d\ge2\) and let \(\Omega=\bigcup_{j=1}^m B(c_j,r_j)\subset\mathbb R^d\), with \(m\ge2\), all radii positive, and pairwise disjoint closed balls. Normalize angular surface measure to probability measure and use the Fourier transform \(\widehat f(\xi)=\int f(x)e^{-2\pi i x\cdot\xi}\,dx\). Set
\[
E_\Omega(R)=\int_{\mathbb S^{d-1}}|\widehat{\mathbf1_\Omega}(R\omega)|^2\,d\sigma(\omega),\quad
\phi_d=\frac{\pi(d+1)}4,\quad \alpha_d=\frac{d+3}{8}.
\]
For fixed geometry and all real \(R\to\infty\),
\[
\boxed{R^{d+1}E_\Omega(R)=\frac1{\pi^2}\sum_{j=1}^m r_j^{d-1}\cos^2(2\pi r_jR-\phi_d)
+O_\Omega(R^{-\min\{1,(d-1)/2\}}).}\tag{1}
\]
In particular, define the integer relation lattice \(\Lambda_r=\{h\in\mathbb Z^m:\sum_jh_jr_j=0\}\). Then the following conditions are equivalent:

(a) There exist \(c>0\) and \(R_0\) with \(E_\Omega(R)\ge cR^{-d-1}\) for every \(R\ge R_0\).

(b) For **each** bit vector \(\varepsilon\in\{0,1\}^m\), some \(h\in\Lambda_r\) satisfies
\[
\alpha_d\sum_jh_j+\frac12\sum_jh_j\varepsilon_j\notin\mathbb Z.\tag{2}
\]
Thus the existence of an eventual positive spectral-energy floor is independent of the locations of the ball centers (provided the balls are disjoint): it is decided by exact rational relations among their radii.

For exactly two balls with \(r_1=q\rho\), \(r_2=p\rho\), where \(\rho>0\) and \(p,q\ge1\) are coprime integers, the equivalent conditions reduce to the simple congruence
\[
\boxed{4\nmid(p-q)(d+3).}\tag{3}
\]
If \(r_1/r_2\) is irrational, then \(\liminf_{R\to\infty}R^{d+1}E_\Omega(R)=0\). More generally the exact lower accumulation value for any radii is
\[
\frac1{\pi^2}\min_{\theta\in T_r}\sum_jr_j^{d-1}\cos^2(2\pi\theta_j-\phi_d),\quad
T_r=\{\theta\in(\mathbb R/\mathbb Z)^m:\ h\cdot\theta=0\pmod1\ \forall h\in\Lambda_r\}.\tag{4}
\]
For an explicit sharp instance, in the plane with two disjoint disks of radii \(\rho\) and \(2\rho\),
\[
\boxed{\liminf_{R\to\infty}R^3E_\Omega(R)=\frac\rho{\pi^2}\left(\frac32-\sqrt{\frac{2367+129\sqrt{129}}{2048}}\right)>0.}\tag{5}
\]
The right side is approximately \(0.13209244796788998024\,\rho/\pi^2\), and is the **sharp** eventual lower coefficient. In contrast, for irrational radius ratios, no strictly positive coefficient works on all large real radii. 

## Assumptions and scope
Each \(B(c,r)\) is an open Euclidean ball, and the closures of distinct balls are disjoint, so \(|c_i-c_j|>r_i+r_j\). The union is a bounded open set, not necessarily a connected domain. Angular measure \(d\sigma\) has total mass one; using unnormalized area multiplies all constants by \(|\mathbb S^{d-1}|\). The Fourier phase contains \(2\pi\); the asymptotic is for all positive **real** radii, not integer-frequency samples. All bounds fix the geometry before letting \(R\to\infty\). Formula (1) also holds for a single ball, but the floor classification is stated for \(m\ge2\).

## Proof
**1. Exact Bessel decomposition.** The Fourier transform of the radius-\(r\) ball, translated to \(c\), is
\[
\widehat{\mathbf1_{B(c,r)}}(R\omega)=e^{-2\pi iR c\cdot\omega} A_r(R),\qquad
A_r(R)=r^{d/2}R^{-d/2}J_{d/2}(2\pi rR).\tag{6}
\]
As the balls are disjoint, the indicator of their union is the sum. On expanding its squared transform and integrating over the sphere, the self-terms are exactly \(\sum_j A_{r_j}(R)^2\). Every cross-term is \(2A_{r_i}(R)A_{r_j}(R)\mathcal J_d(2\pi R|c_i-c_j|)\), where
\[
\mathcal J_d(s)=\int_{\mathbb S^{d-1}}e^{is\omega\cdot e_1}\,d\sigma(\omega)
=\Gamma(d/2)(2/s)^{d/2-1}J_{d/2-1}(s).\tag{7}
\]
Here \(\mathcal J_d(s)=O_d(s^{-(d-1)/2})\) at infinity. Because all center separations are strictly positive, the cross-terms are \(O_\Omega(R^{-(d+1)-(d-1)/2})\).

**2. Uniform high-frequency reduction.** For each fixed order, the standard Bessel asymptotic is \(J_\nu(z)=\sqrt{2/(\pi z)}[\cos(z-\pi\nu/2-\pi/4)+O_\nu(z^{-1})]\), valid for real \(z\to+\infty\). Substituting \(\nu=d/2\) into (6),
\[
A_r(R)=\frac{r^{(d-1)/2}}{\pi R^{(d+1)/2}}\cos(2\pi rR-\phi_d)
+O_{r,d}(R^{-(d+3)/2}).\tag{8}
\]
Squaring, adding, and including the cross-terms proves (1) with the stated uniform-in-\(R\) remainder. In particular the remainder tends to zero after multiplication by \(R^{d+1}\), even at simultaneous cosine zeros.

**3. Exact accumulation set and the arithmetic test.** The closure of the continuous rotation orbit \(\{R(r_1,\ldots,r_m)\pmod{\mathbb Z^m}:R\in\mathbb R\}\) is the compact connected subgroup \(T_r\) in (4): characters that vanish identically on this orbit are exactly those indexed by \(h\in\Lambda_r\). The positive half-orbit has the same closure and every point is approached along a sequence \(R_k\to+\infty\), by compact-torus recurrence (or the continuous form of Kronecker's theorem). Therefore (1) proves (4) and shows that an eventual strictly positive lower coefficient exists exactly when the continuous, nonnegative trigonometric sum in (4) has positive minimum.

That sum vanishes precisely when every \(\theta_j\) is one of the two classes \(\alpha_d\) or \(\alpha_d+1/2\) modulo one. Such a point lies in \(T_r\) exactly if some \(\varepsilon\in\{0,1\}^m\) makes \(h\cdot(\alpha_d\mathbf1+\varepsilon/2)\) an integer **for every** \(h\in\Lambda_r\). Its negation is condition (2). This proves (a)\(\Longleftrightarrow\)(b) without assuming any rational independence. When \(r_1/r_2\) is irrational, \(\Lambda_r=\{0\}\), so \(T_r\) is the full two-torus and contains a simultaneous zero, proving the stated liminf.

**4. Two-ball congruence.** If \(r_1=q\rho\), \(r_2=p\rho\) with coprime \(p,q\), the full relation lattice is generated by \((p,-q)\). A simultaneous zero requires
\[
(p-q)\frac{d+3}{8}+\frac{p\varepsilon_1-q\varepsilon_2}{2}\in\mathbb Z.\tag{9}
\]
Since coprime \(p,q\) cannot both be even, \(p\varepsilon_1-q\varepsilon_2\) can be chosen of either parity. Thus (9) is solvable if and only if \((p-q)(d+3)/4\) is an integer. Negating gives (3). The sharp lower coefficient is the minimum of the continuous periodic trigonometric sum in (1); its positivity is strict exactly in the congruence-failing cases.

**5. Exact planar radius-\(1{:}2\) constant.** Put \(r_1=\rho\), \(r_2=2\rho\), \(t=2\pi\rho R\), and \(d=2\). The sum in (1), after factoring out \(\rho\), is
\[
F(t)=\cos^2(t-3\pi/4)+2\cos^2(2t-3\pi/4)
=\frac32-\frac12\sin(2t)-\sin(4t).\tag{10}
\]
To maximize \(g(u)=\frac12\sin u+\sin(2u)\), set \(c=\cos u\). Every stationary point of \(g\) obeys \(8c^2+c-4=0\), hence \(c_\pm=(-1\pm\sqrt{129})/16\). At these points, the squared maximum magnitudes are respectively \((2367\pm129\sqrt{129})/2048\); the plus sign is strictly larger. Consequently \(\min_tF(t)=3/2-\sqrt{(2367+129\sqrt{129})/2048}\). Since the phase \(t\) traverses arbitrarily many periods as \(R\to\infty\), and the error in (1) tends to zero, this gives precisely (5), independently of the centers. The minimum is strictly positive by (3), and also directly because no common zero exists in (10).

## Verification
The displayed formulae (6)–(8), the full relation-lattice characterization, and the stationary-point computation provide an analytic proof for all dimensions, numbers of balls, radii and real frequency radii in scope. The companion `verify.py` checks the elementary congruence algebra over a finite range, the exact planar algebraic constant against high-resolution periodic minimization, and the high-frequency expansion in dimension three using elementary closed forms for half-integer Bessel functions. These are reproducibility checks, not a replacement for the infinite-domain argument. Run with `python3 verify.py` using only Python's standard library.

## Relationship to prior work
Iosevich, Merlo and Mourgoglou (2026) establish sharp *upper* decay rates for spherical averages over broad regularity classes, and explicitly observe that the ball average can vanish at individual radii. Their theorem does not classify when a disconnected smooth-ball union has a positive lower bound at **every sufficiently large radius**. Brandolini, Hofmann and Iosevich (2003) prove convex-domain upper decay, not this arithmetic lower-floor statement. Iosevich and Rudnev (2005) study extremal spherical-average bounds for classes of measures under energy hypotheses, rather than a fixed two-ball indicator and its exact pointwise lower envelope. A recent exact Fourier-intensity Hessian recovery theorem for two balls concerns only derivatives at frequency zero, and a recent rectangular circular-average resonance theorem concerns polygonal boundary contributions and a different decay scale. Neither contains the radius-congruence criterion or the all-finite-ball torus classification. These are statement/implication distinctions, not claims of exhaustive historical uniqueness.

## Limitations
The radii and centers are fixed as the frequency tends to infinity; constants are not uniform under coalescing centers or vanishing radii. The open set may be disconnected, and no conclusion is claimed for connected perturbations, overlapping balls, general smooth components, or nonreal/nonuniform weights. The torus minimum (4) is exact but need not be a simple closed algebraic expression for more than two balls or irrational dependencies. The method uses standard Bessel and compact-torus theory; the novelty assessment is relative to inspected sources, and older diffraction or almost-periodic literature could contain an equivalent formulation. No independent audit has been performed.

## References
1. A. Iosevich, A. Merlo, M. Mourgoglou, *Sharp decay of the spherical averages of the Fourier transform of open sets*, arXiv:2611.04426v1 (first public 2026-11-03), https://arxiv.org/abs/2611.04426.
2. L. Brandolini, S. Hofmann, A. Iosevich, *Sharp rate of average decay of the Fourier transform of a bounded set*, Geom. Funct. Anal. 13 (2003), 671–680, arXiv:math/0303188.
3. A. Iosevich, M. Rudnev, *On lower bounds for spherical averages of Fourier transforms*, manuscript dated 2005-06-21, https://people.maths.bris.ac.uk/~maxmr/lowerbound3.pdf.
4. NIST Digital Library of Mathematical Functions, §10.17 (fixed-order Bessel asymptotics), https://dlmf.nist.gov/10.17.
