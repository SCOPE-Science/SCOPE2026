# The seventh-order area-balance law for three random great circles

## Finding

Choose three independent great circles, each under the rotation-invariant law, on the unit two-sphere. They partition the sphere into eight geodesic triangular cells. Let \(R\) be the largest cell area minus the smallest cell area (using ordinary spherical area). The probability of nearly equal-area cells has the two-term expansion

\[
\Pr(R<\varepsilon)=\frac{\varepsilon^3}{16\pi}+\frac{7\varepsilon^7}{122880\pi}+O(\varepsilon^9),\qquad\varepsilon\downarrow0.
\]

In particular, the nominal fourth-, fifth-, sixth- and eighth-order coefficients are all zero. The coefficient at order seven is strictly positive. The conditional geometry has an explicit limit: normalized pairwise normal angles become uniformly distributed in a fixed three-dimensional polytope. The normalized area range has the \(\operatorname{Beta}(3,1)\) distribution in the limit.

## Assumptions and scope

Let \(n_1,n_2,n_3\in S^2\) be independent, uniformly distributed oriented unit vectors. Each great circle is \(\{x:n_i\cdot x=0\}\); reversing an orientation only relabels cells. Almost surely the three circles are in general position and form eight positive-area spherical triangles. For \(\sigma\in\{-1,+1\}^3\), write \(A_\sigma\) for the area of the cell \(\{x\in S^2:\sigma_i n_i\cdot x\ge0\ \text{for all }i\}\). Define

\[
R=\max_\sigma A_\sigma-\min_\sigma A_\sigma,
\qquad
t=(t_1,t_2,t_3)=\big(\arcsin(n_1\cdot n_2),\arcsin(n_2\cdot n_3),\arcsin(n_3\cdot n_1)\big).
\]

Set \(\mathcal B=\{u\in\mathbb R^3:\max_{i<j}(|u_i|+|u_j|)<1\}\), an open centrally symmetric polytope of volume \(2\). The conditional convergence claim is with respect to total-variation distance on \(\mathbb R^3\); the orientation marks are arbitrary but fixed by independent fair normal orientations.

## Proof

**Exact area-to-normal relation.** At the corner formed by the first and second great circles, the interior angle of cell \(\sigma\) is \(\pi/2+\arcsin(\sigma_1\sigma_2 n_1\cdot n_2)\). The analogous formula holds cyclically. Girard's spherical excess theorem therefore gives, almost surely,

\[
A_\sigma=\frac\pi2+\sigma_1\sigma_2t_1+\sigma_2\sigma_3t_2+\sigma_3\sigma_1t_3.
\tag{1}
\]

Antipodal cells have equal areas. The four distinct sign-product triples are \((+,+,+),(+,-,-),(-,+,-),(-,-,+)\). The difference between any two is twice a signed sum of exactly two of the \(t_i\). Taking the maximum difference yields the identity

\[
R=2\max_{i<j}\big(|t_i|+|t_j|\big).
\tag{2}
\]

Thus \(R<\varepsilon\) if and only if \(t\in(\varepsilon/2)\mathcal B\), with no asymptotic approximation here.

**Joint normal-angle density.** Put \(x=n_1\cdot n_2\), \(y=n_2\cdot n_3\), \(z=n_3\cdot n_1\) and \(\Delta=1-x^2-y^2-z^2+2xyz\). Conditional on \(n_1\), the quantities \(x\) and \(z\) are independent uniform variables on \((-1,1)\). Conditional on those, an independent azimuth \(\phi\) is uniform on \((0,2\pi)\) and

\[
y=xz+\sqrt{(1-x^2)(1-z^2)}\cos\phi.
\]

The arcsine density of \(\cos\phi\) shows that \((x,y,z)\) has density \(1/(4\pi\sqrt\Delta)\) on \(\Delta>0\), with \(|x|,|y|,|z|<1\). Transforming \(x=\sin t_1\), \(y=\sin t_2\), \(z=\sin t_3\), we obtain

\[
g(t)=\frac{\prod_{i=1}^3\cos t_i}{4\pi\sqrt{1-\sum_i\sin^2t_i+2\prod_i\sin t_i}}.
\tag{3}
\]

All square roots and cosines are positive in a sufficiently small neighborhood of the origin.

**Analytic cancellation and polytope moments.** Taylor expansion of the logarithm of (3) through degree four gives

\[
4\pi g(t)=1-t_1t_2t_3+\frac12\sum_{i<j}t_i^2t_j^2+O(\|t\|^5).
\tag{4}
\]

More precisely, the sign-symmetrization \(\overline g(t)=2^{-3}\sum_{\eta\in\{-1,1\}^3}g(\eta_1t_1,\eta_2t_2,\eta_3t_3)\) is analytic and even in every variable. Since \(\mathcal B\) is invariant under all eight independent sign flips, the odd cubic and every other sign-odd monomial integrate to zero. The symmetrized density consequently satisfies the stronger uniform expansion

\[
4\pi\overline g(t)=1+\frac12\sum_{i<j}t_i^2t_j^2+O(\|t\|^6).
\tag{5}
\]

The polytope is symmetric under coordinate permutations. In one of its \(48\) ordered octants, put \(u_1=x\ge u_2=y\ge u_3=z\ge0\), so \(0\le y\le1/2\), \(y\le x\le1-y\) and \(0\le z\le y\). Direct polynomial integration therefore gives

\[
\begin{aligned}
\operatorname{vol}(\mathcal B)
 &=48\int_0^{1/2}\int_y^{1-y}\int_0^y 1\,dz\,dx\,dy=2,\\
\int_{\mathcal B}\sum_{i<j}u_i^2u_j^2\,du
 &=48\int_0^{1/2}\int_y^{1-y}\int_0^y(x^2y^2+x^2z^2+y^2z^2)\,dz\,dx\,dy=\frac7{120}.
\end{aligned}
\tag{6}
\]

For sufficiently small \(\varepsilon\), the entirety of \((\varepsilon/2)\mathcal B\) lies in the interior of the Gram-positive domain. Substitute \(t=(\varepsilon/2)u\) into the probability integral of (3) and use (5) and (6):

\[
\begin{aligned}
\Pr(R<\varepsilon)
&=\frac{\varepsilon^3}{32\pi}\left[2+\frac{\varepsilon^4}32\cdot\frac7{120}+O(\varepsilon^6)\right]\\
&=\frac{\varepsilon^3}{16\pi}+\frac{7\varepsilon^7}{122880\pi}+O(\varepsilon^9).
\end{aligned}
\]

This proves both the stated coefficients and the absence of intervening powers.

**Conditional shape.** The conditional density of \(U_\varepsilon=2t/\varepsilon\) on \(\mathcal B\) is proportional to \(g((\varepsilon/2)u)\), which converges uniformly on \(\overline{\mathcal B}\) to \(1/(4\pi)\). Because \(\operatorname{vol}(\mathcal B)=2\), the normalized density converges in \(L^1\), hence in total variation, to the uniform density \(\frac12\mathbf 1_{\mathcal B}(u)\). By (2), \(R/\varepsilon=\max_{i<j}(|U_{\varepsilon,i}|+|U_{\varepsilon,j}|)\). Homogeneity of \(\mathcal B\) gives the limiting cumulative distribution \(s^3\) for \(0\le s\le1\), which is \(\operatorname{Beta}(3,1)\).

## Verification

The standalone checker `check_random_great_circles.py` independently constructs the eight triangular cells from pairwise great-circle intersections and evaluates each area using the oriented spherical-triangle solid-angle formula. On \(80\) randomly generated triples it matches (1) and (2), including the total area \(4\pi\). Symbolic integration independently verifies (6) and both asymptotic coefficients. Simulations of \(2{,}500{,}000\) independent normal triples compare observed rare-event probabilities with the two-term formula at \(\varepsilon\) equal to \(0.30\), \(0.45\), and \(0.65\). Independent Gaussian quadrature over the ordered octant gives positive residuals of the predicted order \(O(\varepsilon^9)\) at thresholds \(0.20\), \(0.50\), and \(1.00\). Details and observed outputs are recorded in `VERIFICATION.md`.

## Relationship to prior work

The spherical excess identity, the normal-vector/Gram-coordinate density, and the classical trivariate Gaussian orthant formula are known tools; none is claimed as novel here. Finch and Jones, *Random Spherical Triangles*, analyze individual primal and dual spherical triangle areas. Hug and Schneider, *Random conical tessellations*, establish mean geometric and mixed second-moment identities for conical tessellations. Kabluchko and Thäle analyze face counts and expected intrinsic volumes in great-hypersphere tessellations. These results do not specify the within-configuration area spread of **all eight** cells, its cancellation through order six, or its marked near-balance distribution. The precise new claim is the two-term near-equal-area law, including the seventh-order coefficient and conditional geometry, not the underlying deterministic area identities.

## Limitations

The result concerns exactly three independent isotropic great circles on the unit two-sphere and the small-range regime. It does not provide a full global distribution of the cell-area spread, any higher-order coefficient, or generalizations to more circles. The proof is an analytical calculation supported by finite computational checks, not an independent mathematical audit; priority among all possible older sources remains subject to external review.

## References

- Steven R. Finch and Antonia J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, first submitted 2010-09-27; dual coordinates and area distributions. https://arxiv.org/abs/1009.5329
- Daniel Hug and Rolf Schneider, *Random Conical Tessellations*, arXiv:1508.07768, first submitted 2015-08-31; spherical/conical tessellation face contents and moments. https://arxiv.org/abs/1508.07768
- Zakhar Kabluchko and Christoph Thäle, *Faces in Random Great Hypersphere Tessellations*, arXiv:2005.01055, first submitted 2020-05-03; general tessellation face statistics. https://arxiv.org/abs/2005.01055
