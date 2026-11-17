# Two-term near-regular volume tails for four random ideal hyperbolic vertices

## Finding
Take four independent points uniformly distributed on the sphere at infinity of three-dimensional hyperbolic space of sectional curvature \(-1\), and let \(V\) be their (unsigned) ideal-tetrahedron volume. With \(D\) denoting the Bloch--Wigner dilogarithm and \(v_3=D(e^{i\pi/3})=1.0149416064096536\ldots\), the precise upper tail is
\[
\Pr\{V>v_3-\varepsilon\}
=\underbrace{\frac{64v_3-32\sqrt3}{9}}_{1.05895966311264\ldots}\varepsilon
+\underbrace{\frac{32(104\sqrt3\,v_3-183)}{243}}_{-0.02307626432556\ldots}\varepsilon^2
+O(\varepsilon^3),\qquad \varepsilon\downarrow0.
\]
The second coefficient is negative and much smaller in magnitude than the first. A further joint shape statement holds: the near-maximal event concentrates equally at the two conjugate cross-ratio shapes \(z_\pm=e^{\pm i\pi/3}\); conditional on the choice of \(z_\pm\), the rescaled displacement \((Z-z_\pm)/\sqrt\varepsilon\) converges to uniform area measure on the disk of radius \(2/3^{1/4}\).

## Assumptions and scope
The four ideal endpoints are independent and uniform for normalized spherical area on the Riemann sphere, not uniform in hyperbolic moduli space. Adopt the ordered cross-ratio convention of Marshall--Martin [1],
\[
Z=[Z_1,Z_2,Z_3,Z_4]=\frac{(Z_1-Z_3)(Z_2-Z_4)}{(Z_1-Z_2)(Z_3-Z_4)},\qquad V=|D(Z)|.
\]
All sampled configurations are nondegenerate almost surely. The volume is normalized for curvature \(-1\), and the probability is for the *unsigned* volume. Write \(z_+=1/2+i\sqrt3/2\). On the upper half-plane, Marshall--Martin's normalized planar density is the real-analytic function
\[
\begin{aligned}
\rho(x+iy)&=A(x,y)\log(x^2+y^2)+B(x,y)\log((1-x)^2+y^2)-\frac1{\pi y^2}+C(x,y)D(x+iy),\\
A(x,y)&=\frac{3x^2-3x^3+y^2-3xy^2}{2\pi y^4},\\
B(x,y)&=\frac{-6x^2+3x^3-2y^2+3x(1+y^2)}{2\pi y^4},\\
C(x,y)&=\frac{3(x-1)^2x^2+(2x-1)^2y^2+y^4}{\pi y^5}.
\end{aligned}
\]
The logarithmic terms are essential to the second-order tail coefficient; they cannot be dropped when differentiating the density. The lower half-plane is its complex conjugate [1, Theorems 2.1 and 3.2].

## Proof
**1. Isolated global maxima.** Write the positive dihedral angles of an ideal tetrahedron as \(\alpha,\beta,\gamma\), with sum \(\pi\). Classical Lobachevsky geometry gives \(V=\Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma)\). The sum tends to zero on the degenerate boundary; an interior critical point must satisfy \(\sin\alpha=\sin\beta=\sin\gamma\), because \(\Lambda'(t)=-\log(2\sin t)\). Positivity and the angle sum force \(\alpha=\beta=\gamma=\pi/3\). Therefore \(|D(z)|\) has exactly the two global maximizers \(z_\pm=e^{\pm i\pi/3}\), and the complement of any sufficiently small neighborhoods of them has a strictly smaller upper bound. This justifies reducing the tail integral to two local regions.

**2. The exact volume and density jets.** Write \(z=z_++u+iv\), where \(u,v\) are real. Differentiating the standard Bloch--Wigner identity
\[
 dD=\log|z|\,d\arg(1-z)-\log|1-z|\,d\arg z
\]
through order four yields
\[
\begin{aligned}
 D(z)&=v_3-\frac{\sqrt3}{4}(u^2+v^2)
 +\frac{v(3u^2+7v^2)}{12}\\
 &\quad+\frac{\sqrt3}{48}(u^4+18u^2v^2-15v^4)
 +O((u^2+v^2)^{5/2}).
\end{aligned}
\]
Let \(T=v_3\). Direct differentiation of the *complete* density above gives
\[
\begin{gathered}
\rho_0=\frac{4(2\sqrt3 T-3)}{9\pi},\qquad
(\rho_u,\rho_v)=\left(0,\frac{16(\sqrt3-2T)}{9\pi}\right),\\
\rho_{uu}=\frac{4(8\sqrt3 T-15)}{9\pi},\qquad
\rho_{uv}=0,\qquad
\rho_{vv}=\frac{4(8\sqrt3 T-13)}{3\pi}.
\end{gathered}
\]
Here all derivatives are evaluated at \(z_+\). In particular, the volume Hessian is \(-\sqrt3 I/2\), so each maximum is nondegenerate.

**3. Local cap integration.** Put \(u=r\cos\theta\), \(v=r\sin\theta\), \(a=\sqrt3/4\), and
\[
 b(\theta)=-\frac{\sin\theta(3\cos^2\theta+7\sin^2\theta)}{12},\qquad
 c(\theta)=-\frac{\sqrt3}{48}(\cos^4\theta+18\cos^2\theta\sin^2\theta-15\sin^4\theta).
\]
Then \(v_3-D(z)=ar^2+b(\theta)r^3+c(\theta)r^4+O(r^5)\). For \(s=\sqrt{\varepsilon/a}\), the cap boundary satisfies
\[
 R(\theta)=s-\frac{b(\theta)}{2a}s^2+
 \left(\frac{5b(\theta)^2}{8a^2}-\frac{c(\theta)}{2a}\right)s^3+O(s^4).
\]
Let \(\ell(\theta)=\rho_u\cos\theta+\rho_v\sin\theta\),
\(q(\theta)=\tfrac12(\rho_{uu}\cos^2\theta+2\rho_{uv}\cos\theta\sin\theta+\rho_{vv}\sin^2\theta)\). Radial integration of \(\rho(z)\,dudv\) over one cap yields
\[
\begin{aligned}
 \int_{\text{one cap}}\rho\,dudv&=\pi\rho_0 s^2+s^4 I+O(s^6),\\
 I&=\int_0^{2\pi}\left[\rho_0\left(\frac{3b^2}{4a^2}-\frac{c}{2a}\right)-\frac{b\ell}{2a}+\frac q4\right]d\theta
 =\frac{104\sqrt3\,T-183}{81}.
\end{aligned}
\]
The last equality follows from elementary even trigonometric moments. Multiplication by two accounts for the conjugate cap. Substituting \(s^2=\varepsilon/a\) yields the asserted coefficients \(C_1=2\pi\rho_0/a\) and \(C_2=2I/a^2\).

The displayed \(O(s^6)\) is justified independently of an informal parity truncation: the density and volume-deficit function are real analytic near each nondegenerate maximum. The analytic Morse lemma makes the deficit a positive quadratic form in analytic local coordinates. The transformed density is analytic, and its integral over a centered disk contains only even homogeneous Taylor terms. Thus the local mass has an integer-power analytic expansion in \(\varepsilon\), with remainder \(O(\varepsilon^3)\) after the quadratic term.

**4. Conditional shape.** In the scaled variables \(w=(z-z_\pm)/\sqrt\varepsilon\), the cap converges to \(\{|w|<1/\sqrt a\}\), and the normalized density tends to the constant \(\rho_0\). Conjugation makes the two cap masses identical. This proves both conditional assertions.

## Verification
Running `python verify_endpoint.py` checks the degree-two, degree-three, and degree-four Bloch--Wigner jets symbolically, differentiates the entire density including both logarithms, and verifies the two tail coefficients exactly using trigonometric moments. Separately, it compares the closed-form density against the positive two-dimensional simplex integral of [1], and evaluates the near-maximal probability by an independent polar quadrature. The numerical probabilities agree with the analytic two-term law to an error of order \(\varepsilon^3\) for three test thresholds. No finite quadrature or numerical test is used as an infinite proof.

## Relationship to prior work
Marshall--Martin [1] supply the normalized cross-ratio law, its positive simplex-integral representation, and a closed density in terms of \(D\); their ideal-tetrahedron application evaluates the *mean* volume. Kabluchko--Schange [2] derive expected hyperbolic volumes for broader random beta-polytopes, including \(\mathbb EV=\pi/6\) here. Neither gives the rare-event upper-volume tail or its curvature-sensitive second coefficient. Classical regular ideal-tetrahedron maximality is used, not claimed. Related exact angular-volume stability results do not fix the distribution of the angular data under four independent spherical endpoints.

## Limitations
Only the precise four-independent-uniform-spherical-vertex model and the near-maximum regime are treated. The theorem does not provide the complete volume distribution, lower-volume tails, or a universality result for other sampling measures. Historical priority against unindexed equivalent shape-density computations remains a residual risk. No independent mathematical audit has been performed.

## References
[1] T. Marshall and G. Martin, *Random complex cross ratios*, arXiv:2611.07670v1, first public 2026-11-05, https://arxiv.org/abs/2611.07670 (especially Theorems 2.1, 3.2 and Section 5.2).

[2] Z. Kabluchko and P. Schange, *Expected hyperbolic volumes of random beta polytopes*, arXiv:2604.27793, first public 2026-04-30, https://arxiv.org/abs/2604.27793 (Theorem 1.1 and Section 3.3).
