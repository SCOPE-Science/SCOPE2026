# The first two-point threshold for random lattice encounters with smooth convex bodies

## Finding
Let \(K\subset\mathbb R^2\) be a compact planar convex body, \(D=\operatorname{diam}K\), and \(A=\operatorname{area}K\). Independently choose a uniform planar rotation \(R_\Theta\), with \(\Theta\) uniform on \([0,2\pi)\), and a uniform lattice translation class \(U\in\mathbb R^2/\mathbb Z^2\). Set
\[
N_t=\#((tR_\Theta K+U)\cap\mathbb Z^2),\qquad t>0.
\]
For every \(0<t<\sqrt2/D\), this count is at most two almost surely, and the exact distribution is
\[
\begin{split}
p_2(t)&=\frac1{2\pi}\int_0^{2\pi}\left[g_{tR_\theta K}(e_1)+g_{tR_\theta K}(e_2)\right]\,d\theta,\\
p_1(t)&=t^2A-2p_2(t),\qquad p_0(t)=1-t^2A+p_2(t),
\end{split}
\]
where \(g_C(z)=\operatorname{area}(C\cap(C+z))\). In particular \(p_2(t)=0\) for \(t\le1/D\).

Suppose next that \(\partial K\) is \(C^4\), its curvature is strictly positive, and its Euclidean diameter is attained at exactly one unordered pair \(\{p,q\}\). Denote the curvatures there by \(\kappa_p,\kappa_q\), and set
\[
\kappa_\Sigma=\kappa_p+\kappa_q,\qquad
\kappa_B=\frac{\kappa_p\kappa_q}{\kappa_\Sigma}.
\]
Assume the nondegeneracy condition \(D\kappa_B>1\). For \(\varepsilon\downarrow0\),
\[
\boxed{\displaystyle
p_2(D^{-1}+\varepsilon)
=\frac{2D^{3/2}}{\sqrt{\kappa_\Sigma(D\kappa_B-1)}}\,\varepsilon^2
+o_K(\varepsilon^2).}
\]
The correction to the lattice-free probability is precisely the same \(p_2\), since \(p_0(t)=1-t^2 A+p_2(t)\).

There is also a conditional **universal collision-orientation law**. Let \(\theta_1,\ldots,\theta_4\) be the four distinct rotations that align the unique diameter of \(K\) with a signed coordinate direction. Conditioned on \(N_t=2\), the rotation chooses these four neighborhoods with asymptotically equal probability \(1/4\). Within a selected neighborhood, write \(\alpha=\Theta-\theta_j\), taken as its small signed angular difference, and put
\[
Z_\varepsilon=\alpha\sqrt{\frac{D\kappa_B-1}{2D\varepsilon}}.
\]
Its conditional limiting density is
\[
\boxed{\displaystyle f_Z(z)=\frac8{3\pi}(1-z^2)^{3/2}\,\mathbf1_{\{|z|<1\}}.}
\]
Thus \(Z^2\sim\operatorname{Beta}(1/2,5/2)\) in the limit.

For an ellipse with semiaxes \(a>b>0\) the coefficient specializes to
\[
\boxed{\displaystyle p_2((2a)^{-1}+\varepsilon)
=\frac{4ab^2}{\sqrt{a^2-b^2}}\varepsilon^2+o(\varepsilon^2).}
\]
By contrast, for a disk of radius \(a\), whose diameter directions are not isolated,
\[
\boxed{\displaystyle p_2((2a)^{-1}+\varepsilon)
=\frac{16}{3}a^{3/2}\varepsilon^{3/2}
+O_a(\varepsilon^{5/2}).}
\]
Consequently the isotropic and nondegenerate anisotropic cases have different sharp first-collision exponents.

## Assumptions and scope
All probabilities refer to independent normalized Haar rotation and translation. The translation class can be represented by any fundamental unit square; its precise representative does not matter. There is no independence assumption among lattice inclusion indicators. The exact three-point-count formula applies to every compact convex planar body, without smoothness, whenever \(tD<\sqrt2\). The curvature formula requires a unique diametral pair, positive \(C^4\) boundary curvature, and the displayed strict nondegeneracy. Bodies with multiple diameter pairs or degenerate extremal curvature are not covered by that local formula. The round disk is handled separately. Boundaries have zero probability of containing lattice points for this translation model.

## Proof
**1. Exact low-diameter count.** Any three distinct points of \(\mathbb Z^2\) contain a pair at distance at least \(\sqrt2\). Indeed, if every pair distance were smaller, then each squared interpoint distance would equal one. The unit-distance graph of \(\mathbb Z^2\) is bipartite and has no triangles. Hence \(N_t\le2\) whenever \(tD<\sqrt2\). A pair in this range must differ by \(\pm e_1\) or \(\pm e_2\). The area unfolding identity for a random lattice translation gives
\[
\mathbb E[N_t\mid\Theta]=t^2A,
\qquad \mathbb E\!\left[\binom{N_t}{2}\middle|\Theta\right]
=\frac12\sum_{z\in\mathbb Z^2\setminus\{0\}}g_{tR_\Theta K}(z)
=g_{tR_\Theta K}(e_1)+g_{tR_\Theta K}(e_2).
\]
Since \(N_t\in\{0,1,2\}\), the latter expectation is \(\Pr(N_t=2\mid\Theta)\), proving all three exact expressions. A pair cannot fit if \(tD\le1\); at equality an intersection has zero area.

**2. The contact geometry.** Write \(B=K-K\). Its diameter-direction boundary point is \(p-q\), of length \(D\), whose supporting normal is parallel to \(p-q\). Its curvature there equals
\[
\kappa_B=\left(\kappa_p^{-1}+\kappa_q^{-1}\right)^{-1},
\]
by addition of planar curvature radii under Minkowski addition. If \(\rho_B(\alpha)\) is its radial function at signed angular deviation \(\alpha\) from the diameter direction, Taylor expansion of the strictly curved boundary gives
\[
\rho_B(\alpha)
=D-\frac D2(D\kappa_B-1)\alpha^2+O_K(|\alpha|^3).
\]
The coefficient is strictly negative under the hypothesis. Since the two extremal support points are the unique diametral pair, all nonzero covariogram contributions at \(t\downarrow1/D\) localize to four disjoint orientation neighborhoods, one for each signed unit lattice direction. They have the same leading mass by quarter-turn rotation symmetry and the identity \(g_C(z)=g_C(-z)\).

**3. Local lens calculation.** At a near-contact translation, write \(\delta\) for its signed overlap depth along the common normal. In tangent-normal coordinates the opposing boundaries of \(tK\) differ by
\[
\delta-\frac{\kappa_\Sigma}{2t}x^2+O_K(|x|^3+|\alpha|x^2),
\]
after translating the tangential origin to the local point of maximum gap. Integrating its positive part gives, uniformly in the critical angular window \(|\alpha|=O(\sqrt\varepsilon)\),
\[
 g_{tR_\Theta K}(e_i)
=\frac43\sqrt{\frac{2}{D\kappa_\Sigma}}
\left[D\varepsilon-\frac{D\kappa_B-1}{2}\alpha^2\right]_+^{3/2}
+o_K(\varepsilon^{3/2}),
\]
where \(t=D^{-1}+\varepsilon\); outside the four windows the overlap vanishes for sufficiently small \(\varepsilon\). The little-oh is uniform after rescaling \(\alpha/\sqrt\varepsilon\) on bounded sets. The bound by a constant times \(\varepsilon^{3/2}\) and compactness of the rescaled support justify the following dominated-convergence step.

**4. Orientation integral and conditional law.** With \(c=(D\kappa_B-1)/2\), four identical neighborhoods contribute
\[
\begin{aligned}
p_2(t)&\sim\frac4{2\pi}\frac43\sqrt{\frac{2}{D\kappa_\Sigma}}
\int_{-\sqrt{D\varepsilon/c}}^{\sqrt{D\varepsilon/c}}
(D\varepsilon-c\alpha^2)^{3/2}\,d\alpha\\
&=\frac4{2\pi}\frac43\sqrt{\frac{2}{D\kappa_\Sigma}}
\frac{D^2\varepsilon^2}{\sqrt c}\cdot\frac{3\pi}{8}
=\frac{2D^{3/2}}{\sqrt{\kappa_\Sigma(D\kappa_B-1)}}\varepsilon^2.
\end{aligned}
\]
Here \(\int_{-1}^{1}(1-z^2)^{3/2}\,dz=3\pi/8\). The same computation with a bounded test function of \(Z_\varepsilon\) proves weak convergence to the stated normalized density; the four neighborhood weights are equal in the limit. Squaring the limiting variable yields the beta parameters \((1/2,5/2)\).

**5. Ellipses and disk.** For the ellipse, \(D=2a\), \(\kappa_p=\kappa_q=a/b^2\), so \(\kappa_\Sigma=2a/b^2\) and \(D\kappa_B=a^2/b^2\). Substitution gives the coefficient \(4ab^2/\sqrt{a^2-b^2}\).

For a disk, let \(r=at\). The overlap of two radius-\(r\) disks with centers distance one is exactly
\[
L_r=2r^2\arccos\frac1{2r}-\frac12\sqrt{4r^2-1}
\quad(r>1/2).
\]
There are two unordered unit lattice directions, so \(p_2(t)=2L_r\) for \(1<2r<\sqrt2\). The elementary near-tangency expansion \(L_r=(8/3)(r-1/2)^{3/2}+O((r-1/2)^{5/2})\), obtained by integrating the two circular parabolas or expanding the exact formula, proves the disk assertion.

## Verification
The accompanying standalone Python program `check_lattice.py` evaluates exact ellipse/disk covariogram integrals independently of the curvature formula, for several semiaxis pairs and decreasing threshold gaps. It checks the asymptotic coefficient, the normalized conditional angular second moment \(\mathbb E[Z^2]=1/6\), exact beta-density normalization, and the elementary lattice triangle obstruction. The optional `nonsymmetric_test.py` tests a noncentrally symmetric, strictly convex support-function perturbation by direct polygon-clipping quadrature of the covariogram. The code uses NumPy, SciPy and Shapely. Successful output ends with `RIGID_MOTION_LATTICE_TWO_POINT_ONSET_OK` and `ASYMMETRIC_CURVATURE_LENS_CHECK_OK`, respectively. These finite tests support but do not establish the asymptotic proof.

## Relationship to prior work
The lattice-free probability of a Haar-random rigid-motion copy of a convex body was studied by Bárány (2006), particularly in a large-volume regime. Roldán-Pensado's 2013 thesis analyzes rigid-motion lattice occupancy with a focus on large bodies and thin shapes. Bäsel (2013) computes probabilities for the number of **triangular lattice cells hit** by a randomly placed convex body, not the number of square-lattice **points contained**. The present formulas concern the opposite, diameter-critical end of the lattice-point occupancy problem, and supply curvature-controlled onset exponents and a conditional collision-orientation limit. The local \(3/2\)-power tangency lens and the covariogram themselves are classical ingredients; those facts alone are not claimed as discoveries. No historical-uniqueness claim is made.

## Limitations
The quadratic exponent is not universal for all convex bodies: disks have exponent \(3/2\), and degenerate or multiple diameter directions can have other behavior. The nondegenerate coefficient and the conditional law are asymptotic for fixed \(K\); the ellipse formula is not uniform as \(b\uparrow a\). A separate joint near-circle/asymptotic regime is not analyzed. Additional older literature on small-body lattice occupancy and boundary covariogram asymptotics could imply parts of this statement; independent priority review remains necessary.

## References
- I. Bárány, “The chance that a convex body is lattice-point free: A relative of Buffon's needle problem,” *Random Structures & Algorithms* 30 (2007), 414–426. First published online 2006-09-26. DOI: 10.1002/rsa.20138.
- E. Roldán-Pensado, *Problems in Convex Geometry*, University College London PhD thesis, 2013, Chapter 2, “Random copies of a convex body.” https://discovery.ucl.ac.uk/id/eprint/1388895/1/Thesis.pdf.
- U. Bäsel, “Hitting probabilities for random convex bodies and lattices of triangles,” arXiv:1312.5131v1, posted 2013-12-18; subsequently *Applied Mathematical Sciences* 8 (2014), 8295–8307.
- G. Averkov and G. Bianchi, “Confirmation of Matheron's conjecture on the covariogram of a planar convex body,” *J. Eur. Math. Soc.* 11 (2009), 1187–1202. DOI: 10.4171/JEMS/179.
