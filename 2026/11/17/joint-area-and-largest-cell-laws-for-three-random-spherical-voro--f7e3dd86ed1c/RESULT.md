# Joint area and largest-cell laws for three random spherical Voronoi lunes

## Finding

Let \(X_1,X_2,X_3\) be independent, surface-area-uniform points on the unit sphere \(S^2\). Let \(A_i\) be the ordinary spherical area of the geodesic Voronoi cell of site \(X_i\). Almost surely, \(0<A_i<2\pi\) and \(\sum_{i=1}^3 A_i=4\pi\). The **complete joint density** of the labelled area vector, expressed in the two coordinates \((A_1,A_2)=(a,b)\) with \(A_3=4\pi-a-b\), is
\[
\boxed{f(a,b)=\frac{2}{3\pi}\sin\frac a2\sin\frac b2\sin\frac{4\pi-a-b}{2}}
\]
on \(0<a,b,4\pi-a-b<2\pi\), and zero outside this open triangle (up to null boundaries).

Let \(M=\max(A_1,A_2,A_3)\). Its **exact complete CDF** is
\[
\boxed{\Pr(M\le m)=\frac{(3m/2-2\pi)\cos m-\tfrac12(\sin(2m)+\sin m)}{\pi}},
\qquad 4\pi/3\le m\le2\pi,
\]
with value zero below \(4\pi/3\) and one above \(2\pi\). In particular,
\[
\boxed{\mathbb E M=2\pi-\frac{27}{8\pi}},\qquad
\Pr(M\le3\pi/2)=\frac{1}{2\pi}.
\]
The endpoint probabilities have the sharp expansions
\[
\Pr(M\le4\pi/3+t)=\frac{9\sqrt3}{8\pi}t^2+O(t^4),\qquad
\Pr(M>2\pi-t)=\frac12t^2+O(t^4)
\]
as \(t\downarrow0\). These are statements about the joint area vector and the *largest* cell; the previously known single-cell CDF and covariance are not claimed as new.

## Assumptions and scope

The sampling space is \(S^2=\{x\in\mathbb R^3:\|x\|=1\}\) with normalized rotation-invariant surface area. Set
\[
C_i=\{u\in S^2:u\cdot X_i\ge u\cdot X_j\ \text{for all }j\in\{1,2,3\}\},\quad A_i=\operatorname{area}(C_i).
\]
The cells are labelled by the original sites. Ties, antipodal coincidences, and collinear triples have probability zero. The ordinary spherical areas are measured in steradians, not divided by \(4\pi\). In particular this is not an area-biased cell sample. The probability law is about *Euclidean chord-triangle angles* formed by the three points, not intrinsic angles of their spherical geodesic triangle.

## Proof

**Step 1: a deterministic lune–angle identity.** The three sites, as points of \(\mathbb R^3\), form a nondegenerate Euclidean triangle. Let \(\alpha_i\in(0,\pi)\) denote its ordinary interior angle at \(X_i\), so \(\sum_i\alpha_i=\pi\). Fix \(i\), and write \(b_j=(X_i-X_j)/\|X_i-X_j\|\) for its two other site indices. Then
\[
C_i=\{u\in S^2:u\cdot b_j\ge0\ \text{for both }j\ne i\}.
\]
The angle between these two hemisphere normals is precisely \(\alpha_i\). Their halfspace intersection is a spherical lune of opening \(\pi-\alpha_i\), with spherical area twice its opening. Thus
\[
\boxed{A_i=2(\pi-\alpha_i).}
\]
This also shows that all three areas sum to \(4\pi\) and lie strictly below \(2\pi\).

**Step 2: the joint chord-angle density.** We give an explicit specialization of the classical affine Blaschke–Petkantschin change of variables, rather than treating conditional circle angles as independently uniform. For three noncollinear points \(x_1,x_2,x_3\in\mathbb R^3\), this formula disintegrates ordinary volume into the affine two-plane \(E\) containing the points and their three in-plane coordinates, weighted (up to a constant independent of shape) by the Euclidean triangle area \(\Delta(x_1,x_2,x_3)\). Represent surface area on \(S^2\) by a constant multiple of \(\delta(\|x\|^2-1)\,d^3x\). If \(E\) has signed distance \(h\in(-1,1)\) from the origin, its intersection with \(S^2\) is a circle of radius \(r=\sqrt{1-h^2}\). For in-plane polar coordinates \((\rho_j,\theta_j)\), each radial surface delta contributes
\[
\int_0^\infty\delta(\rho_j^2+h^2-1)\rho_j\,d\rho_j=\tfrac12,
\]
independent of \(h\) and \(\theta_j\). The in-plane area of the triangle with angles \(\alpha_1,\alpha_2,\alpha_3\) and circumradius \(r\) is
\[
\Delta=\frac{(2r\sin\alpha_1)(2r\sin\alpha_2)(2r\sin\alpha_3)}{4r}
=2r^2\prod_{j=1}^3\sin\alpha_j.
\]
The \(h\)-integration contributes the finite, positive common factor \(\int_{-1}^1(1-h^2)\,dh=4/3\), and plane orientations contribute another common factor. Thus the law of the three circle angles is the **area-weighted** law of three independent uniform points on a circle. The ordered circular spacings of three uniform angles, divided by two, are uniform on the simplex \(\alpha_i>0,\sum_i\alpha_i=\pi\). (Labelling and the two cyclic orders have constant multiplicity.) It follows that the density of \((\alpha_1,\alpha_2)=(u,v)\), with \(\alpha_3=\pi-u-v\), is proportional to \(\sin u\sin v\sin(u+v)\).

The elementary normalization integral is
\[
\int_0^\pi\int_0^{\pi-u}\sin u\sin v\sin(u+v)\,dv\,du=\frac{3\pi}{8}.
\]
Therefore
\[
\boxed{f_{\alpha_1,\alpha_2}(u,v)=\frac8{3\pi}\sin u\sin v\sin(u+v)},
\quad u,v>0,\ u+v<\pi.
\]
By Step 1, \(u=\pi-a/2\), \(v=\pi-b/2\) has absolute Jacobian \(1/4\); also \(\sin(\pi-z)=\sin z\). This gives the claimed complete joint area density. The derivation has no unaccounted atom: the joint angle domain is open with full probability and its density integrates to one.

**Step 3: exact CDF for the largest cell.** For \(4\pi/3\le m\le2\pi\), put \(x=\pi-m/2\in[0,\pi/3]\). Step 1 shows
\[
\{M\le m\}=\{\alpha_i\ge x\ \text{for all }i\}.
\]
Use the identity valid when \(u+v+w=\pi\):
\[
\sin u\sin v\sin w=\frac14[\sin(2u)+\sin(2v)+\sin(2w)].
\]
Symmetry and integration over the truncated simplex give
\[
\begin{aligned}
\Pr(\min_i\alpha_i\ge x)
&=\frac2\pi\int_x^{\pi-2x}(\pi-2x-u)\sin(2u)\,du\\
&=\frac{(\pi-3x)\cos(2x)+\tfrac12[\sin(2x)+\sin(4x)]}{\pi}.
\end{aligned}
\]
The identity and symmetry of its three summands reduce the two-dimensional truncated-simplex integral to the displayed one-dimensional integral. Substituting \(x=\pi-m/2\) yields precisely the stated CDF. Continuity at \(4\pi/3\) and \(2\pi\) gives the endpoint values; there is no atom.

**Step 4: moment, threshold, and endpoint expansions.** From \(M\in[4\pi/3,2\pi]\), its expectation is
\[
\mathbb E M=\frac{4\pi}{3}+\int_{4\pi/3}^{2\pi}[1-F_M(m)]\,dm
=2\pi-\frac{27}{8\pi}.
\]
Substitution \(m=3\pi/2\) gives \(F_M(m)=1/(2\pi)\). Taylor expansion of this explicit analytic CDF at both endpoints yields
\[
F_M(4\pi/3+t)=\frac{9\sqrt3}{8\pi}t^2-\frac{9\sqrt3}{32\pi}t^4+O(t^5),
\]
\[
1-F_M(2\pi-t)=\frac12t^2-\frac1{24}t^4+O(t^5),
\]
proving both stated sharp asymptotic laws.

## Verification

The standalone `verify.py` independently samples 350,000 triples of normalized Gaussian directions, computes each ordinary Euclidean chord angle from chord dot products, reconstructs spherical cell areas using the geometric lune law, and tests the exact maximum-area CDF at four nontrivial thresholds. It numerically integrates the proposed joint angle density over the entire simplex and over an interior rectangle. For six independently chosen triples it checks geometric cell areas a second way, by direct assignment of 85,000 fresh uniform sphere points to their nearest sites. It also verifies the mean maximum area and the acute-chord probability as consistency checks. The executed checker returned `THREE_SITE_JOINT_AREA_CHECKS_OK` and completed without an assertion failure. Numerical checks are finite diagnostics; the preceding change-of-variables and integrations are the proofs.

Reproduce with `python verify.py` and the versions or later specified in `requirements.txt`.

## Relationship to prior work

The general spherical Voronoi halfspace representation and typical-cell combinatorial framework are established by Kabluchko–Thäle [1]. Two separately published analyses [2,3] derive the **marginal** area CDF and covariance for the same three-site model; both explicitly leave the **joint** three-cell area distribution uncomputed. Those already-known univariate formulas are not credited to this result. The area-weighted circumcircle disintegration in Step 2 follows the general spherical Blaschke–Petkantschin shape/size theorem applied by Akopyan–Edelsbrunner–Nikitenko [4]; the general disintegration itself is not claimed to be new. Their acute-triangle probability is a consequence of a less detailed marginal event and does not supply the maximum-area CDF. Finch–Jones [5] study *intrinsic spherical geodesic triangle* angles and area; these are not Euclidean chord-triangle angles or the Voronoi area vector.

The asserted new, self-contained information is the explicit **joint** site-labelled spherical Voronoi area density and the derived exact **largest-cell CDF**, mean, and endpoint coefficients. We have not identified these statements in the full primary works inspected; this is a best-knowledge priority assessment, not proof of historical uniqueness. Miles's 1971 paper [6] and Arbeiter–Zähle's 1994 spherical mosaics study [7] are plausible earlier sources but their complete texts were not available for adequate comparison. In particular, a general integral-geometry disintegration may imply the density after a special-case calculation, although it does not directly state the maximum statistic. That implication is explicitly acknowledged rather than disguised as an independently invented general principle.

## Limitations

Exactly three i.i.d. surface-uniform sites on the curvature-one two-sphere are considered. There is no claim for four or more sites, nonuniform site measures, the area-biased cell, other dimensions, or non-spherical spaces. The probability laws are exact, while numerical trials provide only corroboration. No independent mathematical audit or exhaustive historical-priority proof has been performed. The previously established single-cell CDF, acute-chord probability, Blaschke–Petkantschin disintegration, and combinatorial Voronoi facts are not novel contributions.

## References

1. Z. Kabluchko and C. Thäle, *The Typical Cell of a Voronoi Tessellation on the Sphere*, arXiv:1911.07221, first posted 2019-11-17, https://arxiv.org/abs/1911.07221 .
2. *Exact area distribution of a three-site spherical Voronoi cell*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-area-distribution-of-a-three-site-spherical-voronoi-cell--b37584669581 .
3. *Exact area law for three-site spherical Voronoi cells*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-area-law-for-three-site-spherical-voronoi-cells--b9898181a26a .
4. A. Akopyan, H. Edelsbrunner and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-Sphere*, arXiv:2007.07783 (first posted 2020-07-15), especially Section 4, https://arxiv.org/abs/2007.07783 .
5. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, first posted 2010-09-27, https://arxiv.org/abs/1009.5329 .
6. R. E. Miles, *Random points, sets and tessellations on the surface of a sphere*, Sankhyā Ser. A 33 (1971), 145–174; https://www.jstor.org/stable/25049720 . Full text not inspected.
7. E. Arbeiter and M. Zähle, *Geometric measures for random mosaics in spherical spaces*, Stochastics and Stochastics Reports 46 (1994), 63–77, https://doi.org/10.1080/17442509408833870 . Full text not inspected.
