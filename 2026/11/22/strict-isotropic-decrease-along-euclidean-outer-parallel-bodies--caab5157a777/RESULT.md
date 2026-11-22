# Strict isotropic decrease along Euclidean outer parallel bodies of every rectangle

## Finding
Let \(a,b>0\) and let \(B_2\) denote the Euclidean closed unit disk. For every \(t\ge0\), consider the convex body
\[
K_t=([-a,a]\times[-b,b])+tB_2.
\]
For \(X_t\) uniformly distributed by planar area on \(K_t\), define the affine-invariant normalized covariance determinant
\[
J_{a,b}(t)=L(K_t)^4=\frac{\det\operatorname{Cov}(X_t)}{\operatorname{area}(K_t)^2}.
\]
**For every pair of positive half-side lengths (including unequal ones), \(J_{a,b}(t)\) decreases strictly on \([0,\infty)\).** Its sharp, aspect-independent endpoints are
\[
\boxed{J_{a,b}(0)=\frac1{144},\qquad
\lim_{t\to\infty}J_{a,b}(t)=\frac1{16\pi^2}},
\]
so for every finite \(t>0\),
\[
\boxed{\frac1{16\pi^2}<J_{a,b}(t)<\frac1{144}}.
\]
The sharp short- and large-radius expansions are
\[
J_{a,b}(t)=\frac1{144}-\frac{4-\pi}{288ab}\,t^2+O_{a,b}(t^3)
\quad(t\downarrow0),
\]
\[
J_{a,b}(t)=\frac1{16\pi^2}+
\frac{(9\pi^2-88)(a^2+b^2)+(36\pi-112)ab}{36\pi^4t^2}
+O_{a,b}(t^{-3})\quad(t\to\infty).
\]
Both displayed quadratic coefficients have the stated strict signs. In particular, on measuring the rounding distance in units of \(\sqrt{ab}\), **the initial quadratic decrease is independent of the rectangle's aspect ratio**.

## Assumptions and scope
All areas, integrals, and covariance entries are in the ambient Euclidean plane; the area is strictly positive because \(a,b>0\). The parameter \(t\) is a Euclidean *outer* rounding radius. No assertion is made for nonrectangular parallelograms, arbitrary convex bodies, other Minkowski gauges, or inner erosions. The limit as \(t\to\infty\) is not attained at finite radius. The limit corresponds to a Euclidean disk after scale normalization. The non-square case is essential to the new classification; the square is included for a coherent sharp boundary case.

## Proof
**1. Independent area and moments.** Write \(A(t)=\operatorname{area}(K_t)\), \(M_x(t)=\int_{K_t}x^2\,dx\,dy\), and \(M_y(t)=\int_{K_t}y^2\,dx\,dy\). The central symmetry and coordinate reflections make the centroid zero and the off-diagonal covariance entry zero. Decomposing \(K_t\) into the original rectangle, four side strips, and four exterior quarter-disks gives
\[
A(t)=4ab+4(a+b)t+\pi t^2.
\]
For an independent direct integral, a horizontal slice with \(|y|\le b\) has half-width \(a+t\); at \(|y|=b+s\), where \(0\le s\le t\), its half-width is \(a+\sqrt{t^2-s^2}\). Consequently
\[
\begin{aligned}
M_x(t)&=\frac{4b}{3}(a+t)^3+\frac43\int_0^t(a+\sqrt{t^2-s^2})^3\,ds,\\
M_y(t)&=\frac{4(a+t)b^3}{3}+4\int_0^t(b+s)^2(a+\sqrt{t^2-s^2})\,ds.
\end{aligned}
\]
Using the elementary quarter-circle integrals, these evaluate to
\[
\begin{aligned}
M_x(t)&=\frac{4a^3b}{3}+
\left(4a^2b+\frac{4a^3}{3}\right)t+
(4ab+\pi a^2)t^2+
\frac{4b+8a}{3}t^3+\frac{\pi}{4}t^4,\\
M_y(t)&=M_x(t)\big|_{a\leftrightarrow b}.
\end{aligned}
\]
Since the two covariance diagonal entries are \(M_x/A\) and \(M_y/A\),
\[
\boxed{J_{a,b}(t)=\frac{M_x(t)M_y(t)}{A(t)^4}.}
\]
The formula applies continuously at \(t=0\), even though some curved boundary pieces collapse there.

**2. An all-radius positivity certificate.** Differentiating the exact rational expression gives
\[
J'_{a,b}(t)=-\frac{t}{A(t)^5}\sum_{k=0}^{6}c_k(a,b)t^k,
\]
where the coefficients are
\[
\begin{aligned}
c_0&=\tfrac{64}{9}a^4b^4(4-\pi),\\
c_1&=\tfrac{64}{9}a^3b^3(\pi-1)(a+b),\\
c_2&=\tfrac{16}{9}a^2b^2[(9\pi-20)(a^2+b^2)+(84\pi-248)ab],\\
c_3&=\tfrac{20}{9}ab(a+b)[\pi(a^2+b^2)+(12\pi^2+10\pi-144)ab],\\
c_4&=\tfrac29[2\pi(a^4+b^4)+(51\pi^2+64\pi-672)(a^3b+ab^3)\\
&\hspace{3em}+(18\pi^3+324\pi-1536)a^2b^2],\\
c_5&=\tfrac{a+b}{9}[(27\pi^2-256)(a^2+b^2)+(54\pi^2+36\pi-640)ab],\\
c_6&=\tfrac{\pi}{18}[(9\pi^2-88)(a^2+b^2)+(36\pi-112)ab].
\end{aligned}
\]
Every \(c_k(a,b)\) is **strictly positive** whenever \(a,b>0\). For \(c_0\) use \(\pi<4\); for the remaining coefficients all explicitly displayed scalar coefficients of positive monomials are positive. This follows without numerical approximation by \(157/50<\pi<22/7\): each is increasing in \(\pi>0\) and is strictly positive when \(\pi=157/50\). (For instance, \(9(157/50)^2-88>0\), \(36(157/50)-112>0\), and \(18(157/50)^3+324(157/50)-1536>0\).) Hence \(J'_{a,b}(t)<0\) for every \(t>0\), proving strict monotonicity on the entire closed half-line by continuity. This is an infinite-parameter proof, not a sampled sign test.

**3. Sharp endpoints and curvature.** The constant terms give \(A(0)=4ab\), \(M_x(0)=4a^3b/3\), and \(M_y(0)=4ab^3/3\), whence \(J_{a,b}(0)=1/144\). Leading terms at infinity are \(A(t)\sim\pi t^2\), \(M_x(t),M_y(t)\sim\pi t^4/4\), giving the disk limit \(1/(16\pi^2)\). Taylor expansion of the same rational function gives exactly the two displayed second-order terms; both first-order terms vanish. Their strict signs follow from \(\pi<4\), \(9\pi^2>88\), and \(36\pi>112\). The strict all-radius inequality rules out finite-radius equality with the disk limit.

## Verification
Run `python check.py` with SymPy; SciPy enables additional independent quadrature checks. The program independently evaluates exact horizontal-slice moments, reconstructs all seven derivative coefficients as a polynomial identity, checks rational sign certificates for the coefficients, verifies endpoint and short-/large-radius expansions, tests symmetry and scale invariance, and compares the moments against direct one-dimensional numerical quadratures for six disparate aspect-radius triples. The finite quadratures corroborate but do not prove the infinite-parameter derivative sign; the exact polynomial coefficient proof does that.

## Relationship to prior work
Richter and Saorín Gómez (2020) establish monotonicity of isoperimetric and quermassintegral quotients for parallel bodies, an important motivation for examining a different, affine-invariant quantity along the same deformation. Their theorems involve mixed volumes rather than a covariance determinant; a decrease of those quotients alone does not imply the result here. Kipp (2023, 2024) develops perturbation and extremality restrictions for the isotropic constant, but the cited statements do not yield an exact all-radius outer-parallel profile. Related known calculations for *regular polygons*, including the square, establish the square subcase; the contribution here is uniform rigorous monotonicity for every unequal rectangle and the aspect-independent quadratic response. A published all-dimensional cube-rounding calculation supplies an infinitesimal square result but no all-radius non-square rectangle theorem. Mechanical section-property tables may supply individual moments, but formulas for moments by themselves do not establish strict decrease of the normalized covariance determinant for all parameters.

## Limitations
The stated universality is over positive rectangular half-side lengths, not over all convex bodies. Polynomial positivity is specific to the Euclidean disk as outer gauge. No independent peer review or general isotropic-constant extremality theorem is claimed. The originality comparison is necessarily provisional: older engineering inertia sources or unindexed convex-geometric accounts could give an equivalent monotonicity statement; their absence from indexed searches is not a uniqueness proof.

## References
- Christian Richter and Eugenia Saorín Gómez, *On the monotonicity of the isoperimetric quotient for parallel bodies*, first posted 2020-03-31, arXiv:2003.14182. https://arxiv.org/abs/2003.14182
- Christian Kipp, *Small perturbations of polytopes*, first posted 2023-03-31, arXiv:2303.18033. https://arxiv.org/abs/2303.18033
- Christian Kipp, *Isotropic constants and regular polytopes*, first posted 2024-07-01, arXiv:2407.01353. https://arxiv.org/abs/2407.01353
- *Sharp isotropic response to Euclidean rounding of cubes*, public result, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-isotropic-response-to-euclidean-rounding-of-cubes--c7d29f80bf57/RESULT.md
