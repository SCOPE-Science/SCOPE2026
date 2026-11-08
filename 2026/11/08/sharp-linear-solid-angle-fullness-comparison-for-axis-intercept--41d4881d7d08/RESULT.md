# Sharp linear solid-angle–fullness comparison for axis-intercept simplices

## Finding
For an integer \(d\ge2\) and arbitrary real lengths \(a_1,\ldots,a_d>0\), consider the Euclidean axis-intercept simplex
\[
S(a)=\operatorname{conv}\{0,a_1e_1,\ldots,a_de_d\}\subset\mathbb R^d.
\]
Let \(\mu(S)=\operatorname{vol}_d(S)/\operatorname{diam}(S)^d\) be its fullness. Let \(\Omega_i\) denote the unnormalized \((d-1)\)-dimensional spherical measure of the tangent cone at vertex \(a_ie_i\), let \(\Omega_0\) denote the same measure at the origin, and put \(\Omega_{\min}=\min_{0\le i\le d}\Omega_i\). Define
\[
C_d=d(d-1)2^{d/2}\int_0^1(1-t)^{d-2}(1+t^2)^{-d/2}\,dt.
\]

**Theorem.** Exactly the coordinate vertices with maximal intercept length minimize the solid angle. Moreover,
\[
 d\mu(S)<\Omega_{\min}(S)\le C_d\mu(S).
\]
The left coefficient \(d\) is the exact, never attained infimum of \(\Omega_{\min}/\mu\). The right coefficient \(C_d\) is the exact supremum. For \(d=2\), upper equality occurs if and only if the two legs are equal; for \(d\ge3\), upper equality is not attained. Specifically, the families of leg ratios \((1,\varepsilon,\ldots,\varepsilon)\) and \((1,1,\varepsilon,\ldots,\varepsilon)\), respectively, approach the two endpoints as \(\varepsilon\downarrow0\). The first universal-side inequality follows already from an existing general simplex theorem [1]; the contribution here is the **sharp reverse linear bound** and its complete extremal structure within this class.

The constants satisfy \(C_2=\pi\), \(C_3=24-12\sqrt2\), and
\[
 C_d=d2^{d/2}\left(1-\frac1d+O(d^{-2})\right)\qquad(d\to\infty).
\]

## Assumptions and scope
The dimension is an arbitrary integer \(d\ge2\), all intercepts are positive, and angles use ordinary spherical area, not the fraction of total sphere area. The simplex is a right-corner (coordinate-axis) simplex; it is **not** the chain-orthoscheme with vertices given by successive sums of perpendicular increments. The result is invariant under rigid motions and positive homotheties, not arbitrary affine changes of shape. Its diameter is
\[
D=\sqrt{a_{(1)}^2+a_{(2)}^2},
\]
where \(a_{(1)}\ge a_{(2)}\ge\cdots\ge a_{(d)}>0\) are the intercepts in descending order. Its volume is \(\prod_i a_i/d!\).

## Proof
**1. Location of the smallest angle.** Isotropic Gaussian probability of a cone is its spherical area divided by \(|\mathbb S^{d-1}|\). At vertex \(a_ie_i\), the tangent cone can be written exactly as
\[
\{x:x_j\ge0\ (j\ne i),\quad x_i\le-a_i\textstyle\sum_{j\ne i}x_j/a_j\}.
\]
Let \(Z_1,\ldots,Z_d\) be independent standard Gaussian variables. For two indices \(i,k\) with \(a_i\ge a_k\), condition on the other nonnegative Gaussian coordinates and set \(h=\sum_{j\notin\{i,k\}}Z_j/a_j\ge0\). The Gaussian event for the angle at \(a_ie_i\) requires
\[
Z_k\ge0,\qquad Z_i\le-(a_i/a_k)Z_k-a_i h.
\]
By exchanging the identically distributed coordinates \(Z_i\) and \(Z_k\), the angle event at \(a_ke_k\) instead requires
\[
Z_k\ge0,\qquad Z_i\le-(a_k/a_i)Z_k-a_k h.
\]
The former event is contained in the latter, and the containment has positive Gaussian-measure difference whenever \(a_i>a_k\). Thus \(\Omega_i<\Omega_k\) if \(a_i>a_k\), with equality when their lengths are equal. Each coordinate-vertex cone is a strict subset of a signed orthant (the origin cone has exactly one full orthant), so \(\Omega_i<\Omega_0\). Consequently, *exactly* the indices with longest legs attain \(\Omega_{\min}\).

**2. Exact angular integral.** Relabel so \(a_1=A=a_{(1)}\) and \(a_2=B=a_{(2)}\), and set \(r=B/A\in(0,1]\), \(q_j=a_j/A\in(0,r]\) for \(j\ge3\). In the hemisphere \(x_1<0\), the gnomonic chart \(z_j=x_j/(-x_1)\) has spherical-area Jacobian \((1+\|z\|^2)^{-d/2}\). At the vertex \(Ae_1\), the cone is the simplex \(z_j\ge0\), \(\sum_{j=2}^d(A/a_j)z_j\le1\). The substitution \(z_j=(a_j/A)u_j\) maps it onto the standard simplex
\[
\Delta_{d-1}=\{(u_2,\ldots,u_d):u_j\ge0,\ \sum_{j=2}^du_j\le1\}.
\]
Thus, with \(\Omega_{\min}=\Omega_1\),
\[
\Omega_1=\Bigl(\prod_{j=2}^dq_j\Bigr)
\int_{\Delta_{d-1}}\left(1+r^2u_2^2+\sum_{j=3}^dq_j^2u_j^2\right)^{-d/2}du,
\]
and
\[
\mu(S)=\frac{\prod_{j=2}^dq_j}{d!(1+r^2)^{d/2}}.
\]
The exact ratio, therefore, is
\[
R_d(r,q)=\frac{\Omega_{\min}}{\mu}=d!\int_{\Delta_{d-1}}
\left(\frac{1+r^2}{1+r^2u_2^2+\sum_{j=3}^dq_j^2u_j^2}\right)^{d/2}du.
\]

**3. Sharp lower and upper constants.** Throughout the standard simplex interior,
\[
r^2u_2^2+\sum_{j=3}^dq_j^2u_j^2<r^2\left(\sum_{j=2}^du_j\right)^2\le r^2,
\]
so the integrand of \(R_d\) exceeds one; since \(\operatorname{vol}(\Delta_{d-1})=1/(d-1)!\), \(R_d>d\). Letting \(r=q_3=\cdots=q_d=\varepsilon\downarrow0\) and applying dominated convergence proves \(R_d\to d\), hence the exact infimum.

For the upper bound, dropping the nonnegative \(q_j^2u_j^2\) terms only increases the integral. Hence
\[
R_d(r,q)\le d!(1+r^2)^{d/2}\int_{\Delta_{d-1}}(1+r^2u_2^2)^{-d/2}du.
\]
The right integrand after moving the outside factor inside is \(((1+r^2)/(1+r^2u_2^2))^{d/2}\). Its derivative with respect to \(r\) is positive whenever \(0\le u_2<1\) and \(r>0\), so the bound strictly increases on \(0<r\le1\). Its maximum is at \(r=1\). Integrating out \(u_3,\ldots,u_d\), whose slice has volume \((1-u_2)^{d-2}/(d-2)!\), yields precisely \(C_d\). For \(d\ge3\), at least one dropped term is positive on the interior, so equality is impossible for positive intercepts. Taking \(q_3=\cdots=q_d=\varepsilon\downarrow0\), \(r=1\), gives the supremum by dominated convergence. For \(d=2\), no term was dropped and the strictly increasing dependence on \(r\) gives equality exactly at \(r=1\). This proves all sharpness and equality assertions.

For low dimensions, \(C_2=4\int_0^1(1+t^2)^{-1}dt=\pi\). Moreover,
\[
C_3=12\sqrt2\int_0^1\frac{1-t}{(1+t^2)^{3/2}}dt=12\sqrt2(\sqrt2-1)=24-12\sqrt2.
\]
Finally, if \(U_d\) has the beta distribution with density \((d-1)(1-u)^{d-2}\) on \([0,1]\), then
\[
\frac{C_d}{d2^{d/2}}=\mathbb E(1+U_d^2)^{-d/2}.
\]
The moments \(\mathbb EU_d^2=2/[d(d+1)]\), \(\mathbb EU_d^4=24/[d(d+1)(d+2)(d+3)]\), together with the Taylor bound \((1+v)^{-d/2}=1-(d/2)v+O(d^2v^2)\) for \(0\le v\le1\), uniformly in \(d\), show this expectation equals \(1-1/(d+1)+O(d^{-2})\). This is \(1-1/d+O(d^{-2})\), proving the stated asymptotic.

## Verification
The accompanying standalone script `verification/check.py` computes \(C_d\) by deterministic Simpson integration for dimensions \(2\) through \(10\), checks \(C_2=\pi\) and \(C_3=24-12\sqrt2\), and uses the independent trihedral-solid-angle formula to check angle ordering and the sharp bounds on \(2{,}400\) randomly sampled, nondegenerate trirectangular tetrahedra. It also checks both degenerating extremal families numerically. These experiments verify implementation sanity, not the infinite-dimensional-range proof, which is given above. Execute with `python3 verification/check.py` (Python standard library only).

## Relationship to prior work
Licht's October 2026 theorem [1, Theorem 1.1] proves for **all** simplices \(\mu\le\Omega_{\min}/d\) and a quadratic lower estimate for \(\mu\) in terms of \(\Omega_{\min}\). Consequently, the inequality \(\Omega_{\min}\ge d\mu\) is *not* novel and is not presented as such here. Licht's general quadratic converse does not imply a linear converse for the coordinate-axis family, much less its optimal constant and extremizers. The earlier tetrahedral-mesh analysis of Liu and Joe [2] motivates using minimum solid angle as a shape measure and discusses comparisons between tetrahedral quality metrics. The author-uploaded historical survey by Dompierre and coauthors [4, Section 2.3] defines minimum-angle shape measures and discusses the right-tetrahedron vertex angle, but does not state the present sharp all-dimensional ratio in the inspected material. Historical literature on right tetrahedra may contain specialized formulas, but no directly dominating sharp all-dimensional linear comparison was located in the consulted records. The potentially relevant complete older manuscript was not available for full-text checking, so priority is provisional. This is a constrained-family theorem, not a refutation or replacement of the sharp exponent in the general simplex setting.

## Limitations
The statement applies only to nondegenerate coordinate-axis (orthogonal-corner) simplices. No assertion is made for arbitrary simplices, more general orthoschemes, arbitrary affine images, or mesh assemblies. Constants use unnormalized spherical area; normalizing by the sphere area requires rescaling. The lower-side inequality was previously known in greater generality. The cited older mesh paper was assessed by accessible abstract and bibliographic content, not a full-text reading. No independent mathematical audit has been performed.

## References
1. M. W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883v1, first submitted 2026-10-05, Theorem 1.1 and sections 2–4, https://arxiv.org/abs/2610.05883.
2. A. Liu and B. Joe, *Relationship between tetrahedron shape measures*, BIT Numerical Mathematics 34 (1994), 268–287, DOI:10.1007/BF01955874.
3. A. Akopyan and R. Karasev, *Bounding minimal solid angles of polytopes*, arXiv:1505.05263 (2015), https://arxiv.org/abs/1505.05263.
4. J. Dompierre, M.-G. Vallet, P. Labbé and F. Guibault, *On Simplex Shape Measures with Extension for Anisotropic Meshes*, CERCA Report R2003-10 (2003), Section 2.3, https://www.researchgate.net/publication/236578194_On_Simplex_Shape_Measures_with_Extension_for_Anisotropic_Meshes.
