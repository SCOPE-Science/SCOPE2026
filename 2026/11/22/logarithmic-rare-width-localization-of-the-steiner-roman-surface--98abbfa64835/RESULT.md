# Logarithmic rare-width localization of the Steiner Roman-surface hull

## Finding

Let \(S\) be the unit-normalized Steiner Roman surface
\[
S=\{(yz,zx,xy): x^2+y^2+z^2=1\}\subset\mathbb R^3,
\qquad K=\operatorname{conv}(S).
\]
For a unit viewing direction \(u\), define the Euclidean directional caliper width
\[
W(u)=\max_{a\in K}\langle a,u\rangle-\min_{a\in K}\langle a,u\rangle.
\]
Let \(U\) be Haar-uniform on \(\mathbb S^2\). Set \(T=|U_1U_2U_3|\). Then **the exact directional width and full distribution** are
\[
W(u)=\cos\left(\frac13\arcsin(3\sqrt3\,|u_1u_2u_3|)\right),
\quad \frac{\sqrt3}{2}\le W(u)\le1,
\tag{1}
\]
and, with \(q(w)=\sqrt{1-w^2}(4w^2-1)/(3\sqrt3)\),
\[
\Pr(W(U)\le w)=\frac2\pi\int_{\{0<z<1:\ z(1-z^2)\ge 2q(w)\}}
\arccos\!\left(\frac{2q(w)}{z(1-z^2)}\right)\,dz,
\quad \frac{\sqrt3}{2}\le w\le1.
\tag{2}
\]
The cumulative distribution is zero below \(\sqrt3/2\) and one above \(1\).

At the two width endpoints the laws are sharply different. As \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\!\left(W(U)\le\frac{\sqrt3}{2}+\varepsilon\right)
=12\varepsilon^2+o(\varepsilon^2)}
\tag{3}
\]
whereas the *two-term* opposite-tail expansion is
\[
\boxed{\Pr(W(U)\ge1-\varepsilon)
=\frac{\sqrt6}{\pi}\sqrt\varepsilon
\left[\log\frac1\varepsilon+2+\log\frac32\right]
+o(\sqrt\varepsilon).}
\tag{4}
\]
Furthermore, conditioned on the event in (3), \(U\) converges in distribution to the uniform measure on the eight body-diagonal directions
\(\{(\pm1,\pm1,\pm1)/\sqrt3\}\); conditioned on the event in (4), \(U\) converges to the uniform measure on the six signed coordinate axes \(\{\pm e_1,\pm e_2,\pm e_3\}\). The latter localization is notable because the *entire three coordinate great circles*, rather than just the six axes, maximize width.

## Assumptions and scope

The body is exactly the convex hull of the complete unit-sphere quadratic image shown above; this normalization is **one half** of the coordinate convention \((2yz,2zx,2xy)\) used in some older sources. Widths therefore scale by one half relative to that convention. The viewing direction is uniformly distributed with respect to the normalized spherical surface-area measure. The laws refer to orthogonal projection onto the line spanned by the viewing direction, not to 2-dimensional shadow area, random boundary chords, or a uniform distribution of points in \(K\). Every asymptotic has fixed \(K\) and \(\varepsilon\to0^+\).

## Proof

**1. Quadratic support and the cubic discriminant.** For \(u=(u_1,u_2,u_3)\) put
\[
A(u)=\frac12\begin{pmatrix}0&u_3&u_2\\u_3&0&u_1\\u_2&u_1&0\end{pmatrix}.
\]
For every \(x=(x,y,z)\in\mathbb S^2\), the support pairing is
\(u_1yz+u_2zx+u_3xy=x^{\mathsf T}A(u)x\).
The Rayleigh variational principle gives \(h_K(u)=\lambda_{\max}(A(u))\) and \(h_K(-u)=-\lambda_{\min}(A(u))\). Hence \(W(u)\) is precisely the *spectral spread* of \(A(u)\). For \(\|u\|=1\), writing \(p=u_1u_2u_3\),
\[
\det(\lambda I-A(u))=\lambda^3-\frac\lambda4-\frac p4.
\tag{5}
\]
Its three real eigenvalues can be written as \(\lambda_j=\cos(\theta+2j\pi/3)/\sqrt3\), where \(\cos(3\theta)=3\sqrt3\,p\). Replacing \(p\) by \(-p\) negates the spectrum, so spread depends only on \(|p|\). Ordering the roots and using the triple-angle identity gives (1). The arithmetic-geometric mean inequality \(3\sqrt3\,|p|\le1\) proves the stated range, with the least width only at eight signed body diagonals and the greatest width exactly when \(p=0\), on three coordinate great circles. Since \(\sin(3\arccos w)=\sqrt{1-w^2}(4w^2-1)\) in the stated interval, (1) implies
\[
\{W(U)\le w\}=\{T\ge q(w)\}.
\tag{6}
\]

**2. Exact one-dimensional probability integral.** The random variable \(Z=|U_3|\) is uniform on \([0,1]\). Conditional on \(Z=z\), the azimuth \(\Phi\) is uniform on \([0,2\pi)\), and
\[
T=\frac12z(1-z^2)|\sin(2\Phi)|.
\tag{7}
\]
For \(0\le s\le1\), \(\Pr(|\sin(2\Phi)|\ge s)=2\arccos(s)/\pi\). Conditioning on \(Z\) in (6) gives (2). In particular, the expression is not a Monte Carlo approximation.

**3. The low-width conical contact.** Fix one of the eight unit vectors \(v=(\pm1,\pm1,\pm1)/\sqrt3\), and use a local tangent coordinate \(a\perp v\) with \(u=(v+a)/\sqrt{1+\|a\|^2}\). A direct product expansion gives
\[
3\sqrt3\,|u_1u_2u_3|=1-3\|a\|^2+O(\|a\|^3).
\tag{8}
\]
Using \(\arcsin(1-s)=\pi/2-\sqrt{2s}+O(s^{3/2})\) in (1), uniformly over tangent directions,
\[
W(u)=\frac{\sqrt3}{2}+\frac{\|a\|}{\sqrt6}+O(\|a\|^2).
\tag{9}
\]
Thus each of eight disjoint near-minimum patches has spherical geodesic radius \(\sqrt6\varepsilon(1+o(1))\) and surface area \(6\pi\varepsilon^2(1+o(1))\). Division by \(4\pi\) and multiplication by eight prove (3). The symmetry group permutes the eight patches transitively, proving their equal conditional limiting masses.

**4. The two-term logarithmic high-width law.** Write \(F_T(q)=\Pr(T\le q)\) and \(b(z)=z(1-z^2)/2\). From (7),
\[
F_T(q)=\int_0^1 H\!\left(\frac{q}{b(z)}\right)dz,
\qquad H(s)=\begin{cases}(2/\pi)\arcsin s,&0\le s\le1,\\1,&s>1.\end{cases}
\tag{10}
\]
The endpoints \(z=0\) and \(z=1\) are both singular, and the contributions must be matched to preserve the finite term. For fixed small \(\eta>0\) with \(q\ll\eta\), split the integral into \([0,\eta]\), \([\eta,1-\eta]\) and \([1-\eta,1]\). The elementary identity
\[
\int_0^\eta H(a/z)\,dz
=\frac{2}{\pi}\left[\eta\arcsin(a/\eta)+a\operatorname{arcosh}(\eta/a)\right]
=\frac{2a}{\pi}\left[1+\log(2\eta/a)\right]+o(a)
\tag{11}
\]
for \(a/\eta\to0\) controls the endpoint models \(b(z)\sim z/2\) and \(b(1-y)\sim y\). Thus the three respective contributions, retaining errors that vanish after \(q\to0\) and then \(\eta\to0\), are
\[
\begin{aligned}
I_0&=\frac{4q}{\pi}\bigl[1+\log(\eta/q)\bigr]+O(q\eta^2)+o(q),\\
I_1&=\frac{2q}{\pi}\bigl[1+\log(2\eta/q)\bigr]+O(q\eta)+o(q),\\
I_{\mathrm{mid}}&=\frac{4q}{\pi}\int_\eta^{1-\eta}\frac{dz}{z(1-z^2)}+o(q)\\
&=\frac{4q}{\pi}\bigl[-\tfrac32\log\eta-\tfrac12\log2+O(\eta)\bigr]+o(q).
\end{aligned}
\tag{12}
\]
Here the interior expression follows by the uniform Taylor expansion of \(\arcsin\), and the endpoint model errors follow from \(b(z)/(z/2)=1+O(z^2)\), \(b(1-y)/y=1+O(y)\), with the bounded non-linear transition zones contributing only their already included \(O(q)\) terms. All \(\eta\)-dependent logarithms and \(\log2\) terms cancel, leaving the sharp two-term statement
\[
F_T(q)=\frac{6q}{\pi}\left[\log(1/q)+1\right]+o(q).
\tag{13}
\]
Finally (6) gives, as \(\varepsilon\downarrow0\),
\[
q(1-\varepsilon)=\sqrt{\frac{2\varepsilon}{3}}\,[1+O(\varepsilon)].
\tag{14}
\]
Substitution into (13) yields (4), including the previously easy-to-miss constant \(2+\log(3/2)\).

**5. Why the conditional extreme direction is an axis.** Outside any fixed neighborhoods of the six coordinate-axis points, the zero set of \(u_1u_2u_3\) consists of nonintersecting regular curves on the sphere, and its \(q\)-sublevel neighborhood has surface area \(O(q)\). Equation (13) shows that the total probability is of order \(q\log(1/q)\), so this complement has vanishing conditional probability. Symmetries permute the six axes transitively, proving the equal atomic limiting law. This also shows why the endpoint logarithm cannot be deduced solely from the existence of the three maximizing great circles: their transverse intersections dominate the rare event.

## Verification

The included `verify.py` is a complete standalone numerical diagnostic requiring Python 3, NumPy and SciPy. From a directory containing that file, run `python verify.py`. It independently compares (1) to eigenvalue differences of the explicit symmetric matrices at 2,500 normalized random directions, checks the extrema, evaluates (2) using one-dimensional quadrature, compares it to 524,288 independently generated spherical coordinates at five interior thresholds, and checks both endpoint expansions against direct quadrature. The verified execution reported **2,577 successful deterministic assertions**. At \(\varepsilon=0.001\), the ratio of the exact low-tail integral to \(12\varepsilon^2\) was approximately \(1.00348153\). At \(\varepsilon=0.0001\), the ratio of the exact upper-tail probability to the two-term expression in (4) was approximately \(0.99984787\). These diagnostics do not establish the asymptotic theorem by themselves; the analytic arguments above do.

## Relationship to prior work

The same Roman surface with the doubled coordinate normalization appears explicitly in Didier Henrion, *Semidefinite Representation of Convex Hulls of Rational Varieties*, arXiv:0901.1821, §5.3 (public preprint dated 2009-01-13). Its convex hull is represented there as a three-by-three positive-semidefinite matrix projection. The present proof uses that familiar quadratic-image geometry but does not claim the semidefinite representation is new. The new mathematical assertion is the exact *Haar-directional caliper-width distribution* and the unequal, sharply normalized endpoint and conditional-orientation laws.

Bengtsson, Weis and Życzkowski, *Geometry of the Set of Mixed Quantum States: An Apophatic Approach*, arXiv:1112.2347 (2011), §IV.A, analyze the related Cayley-cubic/Steiner-surface dual pair and its disk facets. Rodman, Spitkovsky, Szkoła and Weis, *Continuity of the Maximum-Entropy Inference: Convex Geometry and Numerical Ranges Approach*, arXiv:1502.02018 (2015), near Corollary 8.3, likewise invoke the hull's disk facets. The inspected passages concern convex representations and face structures, not a random caliper-width pushforward law or the specific endpoint asymptotics (3)–(4). The elementary spherical-coordinate sampling representation is classical; the exact geometric interpretation and the logarithmic two-term rare-width calculation here are not asserted as consequences stated in those papers.

## Limitations

The result is restricted to the exact normalized Roman-surface hull, unit-sphere-uniform viewing directions and Euclidean widths. It does not provide a closed elementary antiderivative for (2), a distribution of orthographic shadow *areas*, or robustness under asymmetric perturbations. Geometric priority remains provisional: related matrix eigenvalue statistics or coordinate-product distributions could yield a reducible formulation not identified in the inspected sources. Independent validation has not been performed.

## References

1. D. Henrion, *Semidefinite Representation of Convex Hulls of Rational Varieties*, arXiv:0901.1821, first public version 2009-01-13, §5.3, https://arxiv.org/abs/0901.1821.
2. I. Bengtsson, S. Weis, K. Życzkowski, *Geometry of the Set of Mixed Quantum States: An Apophatic Approach*, arXiv:1112.2347, first public version 2011-12-11, §IV.A, https://arxiv.org/abs/1112.2347.
3. L. Rodman, I. M. Spitkovsky, A. Szkoła, S. Weis, *Continuity of the Maximum-Entropy Inference: Convex Geometry and Numerical Ranges Approach*, arXiv:1502.02018, first public version 2015-02-06, §8, https://arxiv.org/abs/1502.02018.
4. The MSC2020 classification, code 52A22, *Random convex sets and integral geometry*, https://mathscinet.ams.org/msc/msc2020.html?t=52A21.
