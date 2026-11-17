# Sharp minimum-angle/fullness constants for orthogonal-corner simplices

## Finding

For each integer \(n\ge2\), consider the nondegenerate orthogonal-corner simplex
\[
S(a)=\operatorname{conv}\{0,a_1e_1,\ldots,a_ne_n\}\subset\mathbb R^n,\qquad a_j>0.
\]
Let \(D\) be its Euclidean diameter, \(\mu(S)=\operatorname{vol}_n(S)/D^n\) its fullness, and \(\Omega_i(S)\) the unnormalized \((n-1)\)-dimensional spherical solid angle at vertex \(a_ie_i\), with \(\Omega_0\) at the origin. Write \(\Omega_{\min}=\min_{0\le i\le n}\Omega_i\). Then:

1. The minimum is attained precisely at the coordinate vertices whose orthogonal arms have maximal length. More exactly, for distinct \(i,j\in\{1,\ldots,n\}\),
\[
\Omega_i<\Omega_j\quad\Longleftrightarrow\quad a_i>a_j,
\]
with equality exactly when \(a_i=a_j\); every \(\Omega_i<\Omega_0=|\mathbb S^{n-1}|/2^n\).

2. The exact optimal comparison constants in this family are
\[
\boxed{\ n\,\mu(S)<\Omega_{\min}(S)\le \mathcal C_n\,\mu(S)\ },
\qquad
\mathcal C_n=n(n-1)2^{n/2}\int_0^1\frac{(1-u)^{n-2}}{(1+u^2)^{n/2}}\,du.
\]
For \(n=2\), the upper equality holds precisely when the two legs are equal; for \(n\ge3\) it is strict for every nondegenerate member. The number \(n\) is the sharp lower infimum coefficient (never attained), and \(\mathcal C_n\) is the sharp upper supremum coefficient. The upper sharpness degeneration has two equal longest arms and all others tending to zero, while the lower sharpness degeneration has one fixed long arm and all others tending to zero.

In particular,
\[
\mathcal C_2=\pi,\qquad \mathcal C_3=12(2-\sqrt2).
\]
The constants have dimension growth
\[
1-\frac{1}{n+1}\ \le\ \frac{\mathcal C_n}{n2^{n/2}}\ \le\ 1,
\quad\text{and hence}\quad \mathcal C_n\sim n2^{n/2}.
\]

## Assumptions and scope

All simplex vertices lie in Euclidean \(\mathbb R^n\), the \(e_i\) form an orthonormal basis, the \(n\) legs are strictly positive, and \(n\ge2\). Solid angles are unnormalized Hausdorff measures on the Euclidean unit sphere; dividing them by its area would change the constants. Equal legs are allowed. These simplices are orthogonal-corner (higher-dimensional trirectangular) simplices, not the broader class of simplices with a perpendicular chain of successive edges.

After reordering the legs, write \(t=a_1\ge s=a_2\ge a_3\ge\cdots\ge a_n>0\). Then the diameter and volume are
\[
D=\sqrt{t^2+s^2},\qquad \operatorname{vol}_n(S)=\frac{\prod_{j=1}^n a_j}{n!}.
\]
The strict lower inequality is also a consequence of the general non-strict bound \(n\mu\le\Omega_{\min}\) in Licht's Theorem 1.1, but its strictness and optimality within this special family follow from the exact representation below. The novelty asserted here is the sharp upper constant on this natural subclass, together with the complete ordering and dimension asymptotics.

## Proof

**Step 1: the exact ordering of apex angles.** Fix \(i\ge1\). The tangent cone at \(a_ie_i\) consists exactly of points \(x\in\mathbb R^n\) with
\[
x_j\ge0\quad(j\ne i),\qquad x_i\le-a_i\sum_{j\ne i}\frac{x_j}{a_j}.
\]
If \(Z_1,\ldots,Z_n\) are independent standard Gaussian random variables, rotational symmetry gives \(\Omega_i/|\mathbb S^{n-1}|\) equal to the probability of those inequalities with \(x_j=Z_j\). For \(i\ne j\) and fixed positive \(Z_k\) with \(k\notin\{i,j\}\), swapping the i and j labels in the second event reduces the comparison to
\[
Z_i\le-\frac{a_i}{a_j}Z_j-a_iR\quad\hbox{versus}\quad
Z_i\le-\frac{a_j}{a_i}Z_j-a_jR,
\qquad R=\sum_{k\notin\{i,j\}}\frac{Z_k}{a_k}\ge0.
\]
Both events require \(Z_j\ge0\). If \(a_i>a_j\), the first event is strictly contained in the second up to a set of positive Gaussian measure, so \(\Omega_i<\Omega_j\). If \(a_i=a_j\), exchanging coordinates is an isometry of the simplex, giving equality. The cone at the origin is the positive orthant. Sign reversal of the \(i\)-th Gaussian coordinate maps the cone at \(a_ie_i\) strictly inside that orthant, so \(\Omega_i<\Omega_0=|\mathbb S^{n-1}|/2^n\). It follows that the smallest angles occur exactly at the longest arms.

**Step 2: a normalized exact solid-angle integral.** Choose a longest arm \(t=a_i\) and denote the remaining length ratios by \(r_j=a_j/t\) for \(j\ne i\). Let \(r=\max_{j\ne i}r_j=s/t\in(0,1]\), and let
\[
\Delta_{n-1}=\{u=(u_j)_{j\ne i}:u_j\ge0,\ \sum_{j\ne i}u_j\le1\}.
\]
The gnomonic chart of the tangent cone at \(a_ie_i\), with negative \(i\)-th coordinate normalized to \(-1\), is the Euclidean simplex \(\{z_j=r_ju_j:u\in\Delta_{n-1}\}\). Its spherical-area Jacobian is \((1+\|z\|_2^2)^{-n/2}\). Consequently, with \(U\) uniform on \(\Delta_{n-1}\),
\[
\Omega_{\min}=\frac{\prod_{j\ne i}r_j}{(n-1)!}
\mathbb E\left[\left(1+\sum_{j\ne i}r_j^2U_j^2\right)^{-n/2}\right].
\]
Meanwhile the diameter and volume formulas imply
\[
\mu(S)=\frac{\prod_{j\ne i}r_j}{n!(1+r^2)^{n/2}}.
\]
The quotient is therefore exactly
\[
Q_n(r_j)=\frac{\Omega_{\min}}{\mu(S)}
=n\,\mathbb E\left[\left(\frac{1+r^2}{1+\sum_{j\ne i}r_j^2U_j^2}\right)^{n/2}\right].\tag{1}
\]

**Step 3: strict lower bound and sharpness.** For every interior point of the simplex, \(\sum r_j^2U_j^2<r^2\), because \(\sum U_j<1\) and all \(r_j\le r\). Therefore (1) gives \(Q_n>n\). With \(t=1\) and all remaining legs equal to \(\varepsilon\), the quotient tends to \(n\) by dominated convergence as \(\varepsilon\downarrow0\). Hence the lower coefficient is optimal and unattained.

**Step 4: optimal upper bound and sharpness.** Choose one remaining index \(j_0\) with \(r_{j_0}=r\). Discarding the other nonnegative summands in the denominator of (1) yields
\[
Q_n\le n\,\mathbb E\left[\left(\frac{1+r^2}{1+r^2U_{j_0}^2}\right)^{n/2}\right].
\]
For fixed \(0\le u<1\), \(v\mapsto(1+v)/(1+vu^2)\) strictly increases on \([0,1]\); hence the last expression is at most its value at \(r=1\). The marginal distribution of one coordinate \(U_{j_0}\) of a uniform \((n-1)\)-simplex is \(\mathrm{Beta}(1,n-1)\), with density \((n-1)(1-u)^{n-2}\) on \([0,1]\). We obtain \(Q_n\le\mathcal C_n\) with the integral stated above.

For \(n=2\), there are no discarded coordinates, and equality occurs exactly for \(r=1\). For \(n\ge3\), every discarded term is positive with positive probability, making the upper inequality strict for positive legs. To establish sharpness, take \(a_1=a_2=1\) and \(a_3=\cdots=a_n=\varepsilon\) (for \(n=2\), simply take \(a_1=a_2=1\)). Equation (1), with \(i=1\), converges by dominated convergence to the integral defining \(\mathcal C_n\) as \(\varepsilon\downarrow0\). The minimum-angle location remains at either of the two longest arms by Step 1.

**Step 5: evaluation and dimension growth.** For \(n=2\), \(\int_0^1(1+u^2)^{-1}du=\pi/4\), so \(\mathcal C_2=\pi\). For \(n=3\), elementary antiderivatives give
\[
\int_0^1\frac{1-u}{(1+u^2)^{3/2}}du=\sqrt2-1,
\quad \mathcal C_3=12(2-\sqrt2).
\]
If \(U\sim\mathrm{Beta}(1,n-1)\), then
\[
\frac{\mathcal C_n}{n2^{n/2}}
=\mathbb E(1+U^2)^{-n/2},\qquad
\mathbb EU^2=\frac{2}{n(n+1)}.
\]
The tangent-line bound \(1-\frac n2u^2\le(1+u^2)^{-n/2}\le1\) proves \(1-1/(n+1)\le\mathcal C_n/(n2^{n/2})\le1\), and the asymptotic equivalence follows.

## Verification

The included standard-library Python program `verify.py` independently evaluates the beta-integral constants by numerical quadrature; checks the exact values in dimensions two and three; compares the independent three-dimensional trihedral-angle formula with two-dimensional gnomonic integration at the longest-leg vertices of seven distinct tetrahedra; checks the strict angular ordering in those tetrahedra; tests the dimension-dependent upper/lower interval on 60 independently sampled leg configurations of dimensions two through six; and checks two explicit degenerating boundary families. The program reports `REPRODUCIBLE_CHECKS_OK 181` on execution. These computations test finite examples and the normalization, not the quantified proof across all dimensions. The proof above supplies the universal inequalities and sharpness.

## Relationship to prior work

M. W. Licht, *On solid angles and simplex shape measures* (arXiv:2610.05883v1, 2026-10-05), proves the general bound \(n\mu(S)\le\Omega_{\min}(S)\) and the dimension-dependent quadratic converse \(\Omega_{\min}(S)^2\le C_n\mu(S)\), with examples demonstrating optimality of exponent two for unrestricted simplices in dimensions at least three. Its Section 3 develops the gnomonic integral used as a starting point here. It does not give the sharp upper **linear** coefficient for the orthogonal-corner subclass or order these vertices' solid angles.

A. Akopyan and R. Karasev, *Bounding minimal solid angles of polytopes* (arXiv:1505.05263, 2015), study maximal values of the least vertex solid angle, rather than comparison with volume over diameter within this subclass. Earlier studies of right-corner tetrahedra contain elementary metric and angular identities, but none of the specifically inspected sources supplies the present all-dimensional sharp optimal ratio. The exact source-comparison limitation is that exhaustive historical priority cannot be established by the accessible searches alone.

## Limitations

The result applies only to a simplex possessing a vertex with mutually orthogonal incident edges. It does not assert linear comparability for arbitrary simplices; in fact Licht's global quadratic-exponent sharpness examples prohibit such a universal generalization. The upper sharpness configurations for \(n\ge3\), and every lower sharpness configuration, are degenerating sequences rather than nondegenerate equality cases. The constants concern the unnormalized spherical solid angle, and the diameter uses the two longest coordinate-arm endpoints. No independent mathematical audit has been carried out.

## References

1. M. W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883v1 (submitted 2026-10-05), https://arxiv.org/html/2610.05883v1. Especially Theorem 1.1, Sections 3–4.
2. A. Akopyan and R. Karasev, *Bounding minimal solid angles of polytopes*, arXiv:1505.05263 (2015), https://arxiv.org/abs/1505.05263.
3. A. Liu and B. Joe, *Relationship between tetrahedron shape measures*, BIT Numerical Mathematics 34 (1994), 268–287. Discussed in Licht's Section 4.8.
