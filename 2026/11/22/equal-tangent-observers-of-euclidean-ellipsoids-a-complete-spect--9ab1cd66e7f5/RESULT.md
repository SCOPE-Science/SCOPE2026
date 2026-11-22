# Equal-tangent observers of Euclidean ellipsoids: a complete spectral classification

## Finding

Let \(n\ge3\), and let \(E=o+L\overline{B}_2^n\subset\mathbb R^n\), where \(L\) is a symmetric positive-definite matrix. Call an exterior point \(p\notin E\) *equitangent* if the Euclidean lengths \(\|p-x\|\) are identical for every tangency point \(x\in\partial E\) of a line through \(p\) supporting \(E\).

**Classification theorem.** The set \(H(E)\) of such points is determined exactly by the spectrum of \(D=L^2\):

1. If \(D=\mu I\), then \(H(E)=\mathbb R^n\setminus E\).
2. If \(D=\mu I+(\lambda-\mu)vv^{\mathsf T}\), with \(\lambda,\mu>0\), \(\lambda\ne\mu\), and \(v\) a unit vector, then
   \[H(E)=\{o+hv:|h|>\sqrt\lambda\}.\]
3. Otherwise \(H(E)=\varnothing\).

Thus a strictly triaxial ellipsoid in \(\mathbb R^3\) has no equitangent exterior observer, while a nonround ellipsoid of revolution has exactly two axial rays of such observers. The sphere has every exterior observer.

For a nonround hyperspheroid, write \(a=\sqrt\mu\) for its transverse semiaxis, \(b=\sqrt\lambda\) for its axial semiaxis, and let \(p=o+hv\), \(|h|>b\). All tangent segments from \(p\) have the common squared length
\[
\ell(h)^2=h^2+a^2-2b^2+\frac{b^2(b^2-a^2)}{h^2}.
\]
Consequently the domain endpoint \(b\) and the far-field intercept \(\lim_{|h|\to\infty}(\ell(h)^2-h^2)=a^2-2b^2\) recover both semiaxes.

## Assumptions and scope

All lengths, supporting lines, orthogonality and tangencies are Euclidean. The ellipsoid is full-dimensional with a positive-definite quadratic form, and exterior means strictly outside the closed ellipsoid. Every point on the complete tangency locus is included, rather than one selected tangent line. The dimension restriction \(n\ge3\) is essential: in dimension two, nonround ellipses have additional equitangent points on their principal axes, a previously studied planar phenomenon.

## Proof

Translate to \(o=0\). For \(p\notin E\), put \(w=L^{-1}p\), so \(R=\|w\|>1\), and let \(D=L^2\). A boundary contact has the form \(x=Lu\), \(\|u\|=1\). The tangent hyperplane at \(x\) is \(\{y:u\cdot L^{-1}y=1\}\); thus the line joining \(p\) to \(x\) is tangent exactly when \(u\cdot w=1\). The complete contact locus is the nonempty sphere
\[
 u=R^{-2}w+\rho z,\qquad z\perp w,\quad\|z\|=1,\quad\rho=\sqrt{1-R^{-2}}>0.
\]
Write \(k=1-R^{-2}=\rho^2\). Then \(p-x=L(kw-\rho z)\), and its squared length is exactly
\[
Q(z)=k^2 w^{\mathsf T}Dw-2k\rho\,z^{\mathsf T}Dw+\rho^2 z^{\mathsf T}Dz.
\]
If all these tangent lengths are equal, compare \(Q(z)\) with \(Q(-z)\). Because \(k\rho>0\), this yields \(z^{\mathsf T}Dw=0\) for every \(z\perp w\), hence \(Dw=\lambda w\): the observer vector is an eigenvector of \(D\). With this linear term gone, the restriction of \(z^{\mathsf T}Dz\) to the unit sphere of \(w^\perp\) must be constant. Since \(\dim w^\perp=n-1\ge2\), polarization (or diagonalization) implies the compressed quadratic form equals \(\mu I\) on this whole subspace. The eigenvector property annihilates all cross terms, so
\[
D=\lambda P_w+\mu(I-P_w),\qquad P_w=\frac{ww^{\mathsf T}}{R^2}.
\]
If \(\lambda=\mu\), the ellipsoid is round and every exterior observer works. Otherwise its axial eigenspace is precisely \(\mathbb Rw\) and the orthogonal eigenspace has multiplicity \(n-1\). Thus every equitangent observer must be on the simple axis. Conversely, this spectral form makes the linear term zero and the quadratic term constant for every tangency contact; every exterior axial point works. This proves all three cases, with no generic-position assumption.

For the length formula, orient the simple axis along the last coordinate and write its semiaxis as \(b>0\), the common transverse semiaxis as \(a>0\). From an axial point at height \(h\), where \(|h|>b\), all contact points have axial coordinate \(b^2/h\) and transverse radius \(a\sqrt{1-b^2/h^2}\), by the same tangent-hyperplane equation. Pythagoras gives
\[
\ell(h)^2=\left(h-\frac{b^2}{h}\right)^2+a^2\left(1-\frac{b^2}{h^2}\right)=h^2+a^2-2b^2+\frac{b^2(b^2-a^2)}{h^2}.
\]
The stated inverse determination follows directly. Since the contact locus is entirely parametrized above, no exceptional tangent generators or boundary cases are omitted.

## Verification

The proof is algebraic and holds for all positive semiaxes and all dimensions \(n\ge3\). The companion standalone `equitangent_checker.py` evaluates complete tangency-circle samples for eleven independent diagnostic scenarios (round, spheroidal, nonspheroidal, planar comparison, and four-dimensional examples). It checks both contact constraints and squared-length spreads; these finite diagnostics supplement but do not establish the classification. Run with `python3 equitangent_checker.py`. Exact derivations above are the proof; no external numerical software is necessary.

## Relationship to prior work

The 2012 study by Jerónimo-Castro, Ruiz-Hernández and Tabachnikov investigates equitangent loci of convex surfaces and proves spherical rigidity when sufficiently large prescribed exterior loci have the equal-tangents property. That rigidity direction does not classify the individual admissible exterior points of a fixed nonround ellipsoid. Lángi's 2011 characterization concerns families of sections and tangent data in a specified norm; its universal quantifiers and metric differ from this Euclidean per-observer classification. The 2014 planar study by Jerónimo-Castro and Tabachnikov discusses equitangent curves of ellipses, but its ambient dimension is two and the special planar behavior is not imported into the theorem. A geometric textbook on quadrics discusses tangent cones and focal geometry; a circular tangent cone is not equivalent to every generator having identical finite Euclidean segment length. The full book was not inspected, so a residual historical-priority risk remains. No claim of independent novelty certification is made.

## Limitations

The theorem is restricted to nondegenerate Euclidean ellipsoids in dimensions at least three. It is not a classification of arbitrary strictly convex bodies, tangent-cone circularity, equal angles, or equal lengths among merely selected tangent segments. The planar counterpart is different. The proof establishes a mathematical identity, not a claim that all earlier literature has been exhaustively examined; the sources listed here and related database searches leave historical-priority risk.

## References

1. Z. Lángi, *Ellipsoid characterization theorems*, arXiv:1105.3334v1 (2011), https://arxiv.org/abs/1105.3334.
2. J. Jerónimo-Castro, G. Ruiz-Hernández and S. Tabachnikov, *The equal tangents property*, arXiv:1205.0142v1 (2012), https://arxiv.org/abs/1205.0142.
3. J. Jerónimo-Castro and S. Tabachnikov, *Configuration spaces of plane polygons and a sub-Riemannian approach to the equitangent problem*, arXiv:1408.3747v1 (2014), https://arxiv.org/abs/1408.3747.
4. B. Odehnal et al., *The Universe of Quadrics* (2020), DOI:10.1007/978-3-662-61053-4 (indexed extract only; no full-book coverage assertion).
