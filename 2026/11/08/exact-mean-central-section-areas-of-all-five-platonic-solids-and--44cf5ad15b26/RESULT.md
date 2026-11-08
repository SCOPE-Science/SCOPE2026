# Exact mean central-section areas of all five Platonic solids and their strict scale-free order

## Finding
Let \(P\) be a regular three-dimensional Platonic solid with **unit edge length**, centered at the origin, and let \(U\) be uniform on the unit sphere. Define \(M(P)=\mathbb E_U\operatorname{area}(P\cap U^\perp)\), using ordinary two-dimensional Euclidean area and orientation-uniform, **origin-passing** planes (not random translated planes or projections).

Write \(F\) for the number of congruent faces, \(p\) for the number of edges in one face, \(h\) for the inradius, \(c=\pi/p\), and \(a=1/(2\tan c)\) for the face apothem. Put
\[
\mathcal I(h,a,c)=a\operatorname{arsinh}\!\left(\frac{a\tan c}{\sqrt{h^2+a^2}}\right)+h\arctan\!\left(\frac{h\tan c}{\sqrt{h^2+a^2\sec^2c}}\right).
\]
Then **all five means are exact elementary constants** given by
\[
\boxed{M(P)=\frac{Fhp}{2}\bigl(\mathcal I(h,a,c)-hc\bigr),\qquad \operatorname{Vol}(P)=\frac{Fpah}{6}.}
\]
The complete unit-edge substitution table is:

| Solid | \(F\) | \(p\) | \(h\) | \(M(P)\), approximate |
|---|---:|---:|---|---:|
| Tetrahedron | 4 | 3 | \(\sqrt6/12\) | 0.274348800838802 |
| Cube | 6 | 4 | \(1/2\) | 1.190038681989777 |
| Octahedron | 8 | 3 | \(\sqrt6/6\) | 0.722851704682162 |
| Dodecahedron | 12 | 5 | \(\sqrt{250+110\sqrt5}/20\) | 4.685218585130753 |
| Icosahedron | 20 | 3 | \(\sqrt3(3+\sqrt5)/12\) | 2.029417482235651 |

The accompanying dimensionless, scale-independent central-section constants \(Q(P)=M(P)/\operatorname{Vol}(P)^{2/3}\) satisfy the **strict complete ordering**
\[
\boxed{Q(\text{tetrahedron})<Q(\text{cube})<Q(\text{octahedron})<Q(\text{dodecahedron})<Q(\text{icosahedron}).}
\]
In that order, rigorous outward-rounded brackets for \(Q\) are respectively \((1.141336,1.141338)\), \((1.190037,1.190040)\), \((1.193400,1.193403)\), \((1.205385,1.205388)\), and \((1.206447,1.206450)\). The inequalities, including the close cube–octahedron and dodecahedron–icosahedron comparisons, follow from nonoverlapping interval enclosures, not a floating-point guess.

## Assumptions and scope
Every body is a solid three-dimensional regular convex polyhedron with the usual centroid as origin. Its edges have length one. Uniform orientations are with respect to normalized spherical area measure on \(S^2\); opposite normals represent the same plane and do not change the distribution. The same formula applies, more generally, to any tangential convex polyhedron whose faces are congruent regular \(p\)-gons of common apothem \(a\), with the common insphere centered at the origin and radius \(h\). It is *not* an assertion about generic non-tangential polyhedra or translation-invariant plane measures.

## Proof
**1. Mean section identity (classical geometric reduction).** For any bounded convex three-dimensional body \(K\) containing the origin in its interior, polar-coordinate slicing gives \(A_K(U)=\frac12\int_{S^2\cap U^\perp}\rho_K(\omega)^2\,d\omega\), where \(\rho_K\) is its radial function. Rotational invariance of normalized spherical measure and the fact that a random great-circle point is uniform on \(S^2\) imply
\[
\mathbb E A_K(U)=\frac1{4\pi}\int_{S^2}\pi\rho_K(\omega)^2\,d\omega=\frac14\int_{S^2}\rho_K(\omega)^2\,d\omega=\frac12\int_K\frac{dx}{\lVert x\rVert}.
\]
Indeed the innermost radial integral \(\int_0^{\rho_K}r\,dr=\rho_K^2/2\). This identity is a standard consequence of the spherical Radon transform and **is not claimed as original**. A separate direct derivation uses \(\mathbb E_U\delta(U\cdot x)=1/(2\lVert x\rVert)\) for \(x\ne0\).

**2. Surface potential reduction.** On \(\mathbb R^3\setminus\{0\}\), \(\operatorname{div}(x/\lVert x\rVert)=2/\lVert x\rVert\). Apply the divergence theorem to \(K\) minus a ball of radius \(\varepsilon\), then send \(\varepsilon\downarrow0\); the small-sphere boundary flux tends to zero. Therefore
\[
M(K)=\frac14\int_{\partial K}\frac{x\cdot n(x)}{\lVert x\rVert}\,dS(x).
\]
For a tangential polyhedron, \(x\cdot n=h\) on each face. Thus every face contributes \(hJ/4\), with \(J=\int_{\text{face}}\lVert x\rVert^{-1}dS\).

**3. A regular face integral.** Use orthonormal planar coordinates around the point where the common insphere touches a face. Since the face is a regular \(p\)-gon, split it into \(p\) identical sectors of polar angle \(-c\le\varphi\le c\). On each sector, \(0\le r\le a\sec\varphi\). Therefore
\[
J=p\int_{-c}^c\int_0^{a\sec\varphi}\frac{r\,dr\,d\varphi}{\sqrt{h^2+r^2}}=2p\int_0^c\bigl(\sqrt{h^2+a^2\sec^2\varphi}-h\bigr)d\varphi.
\]
With \(t=\tan\varphi\), the first integral becomes \(\int_0^{\tan c}\frac{\sqrt{h^2+a^2(1+t^2)}}{1+t^2}\,dt\). Its antiderivative, equal to zero at \(t=0\), is
\[
a\operatorname{arsinh}\left(\frac{at}{\sqrt{h^2+a^2}}\right)+h\arctan\left(\frac{ht}{\sqrt{h^2+a^2(1+t^2)}}\right).
\]
Differentiation confirms the identity. Hence \(J=2p(\mathcal I-hc)\), yielding the formula in Finding. Since each unit-edge regular face has area \(pa/2\), decomposition into pyramids of height \(h\) gives \(\operatorname{Vol}(P)=Fpah/6\).

**4. Complete substitution and strict order.** The table's face numbers, side counts, and insphere radii are obtained from standard unit-edge vertex descriptions; `check_sections.py` independently constructs all five vertex sets and checks the inradii against their actual supporting planes. Substitution gives the five exact constants. Finally the explicitly displayed formula for \(Q(P)\), evaluated by outward-rounded real interval arithmetic at 65 decimal digits, gives the five rational brackets in Finding. The nonoverlap proves each strict inequality. `check_intervals.py` is a separate finite interval certificate: it checks both all brackets and their order; neither random simulation nor decimal approximations by themselves are used as proof of strictness.

## Verification
Run `python check_intervals.py` with `mpmath` installed to reproduce the five certified disjoint intervals; it prints `CERTIFIED_STRICT_NORMALIZED_ORDER_OK`. Run `python check_sections.py` with `numpy` and `scipy` installed to construct geometric vertex models, confirm all five inradii from convex-hull facets, compare each analytic face integral with numerical quadrature, and independently estimate section areas via polygon intersections with 1,200 uniformly sampled orientation normals per solid. It prints `CENTRAL_PLATONIC_SECTION_CHECKS_OK`. The random check is a reproducibility test with a fixed numerical seed, not proof of the continuous expectation.

## Relationship to prior work
The spherical Radon-transform formula for central hyperplane sections is classical; see the full original paper by Alexander Koldobsky, *A sqrt(n) estimate for measures of hyperplane sections of convex bodies*, arXiv:1309.5271, sections 1–2, especially equations (5)–(8) (2013). That source studies hyperplane inequalities, not the five exact Platonic means or their normalized order. Published records on Platonic projection/shadow-area distributions, mean-square widths, random section vertex counts, and central section polygon-type laws are different invariants; they do not state the mean area of random **central sections**. The contribution here is the simultaneous elementary evaluation of this natural complete family and the dimensionless strict ranking, not the underlying Radon identity or elementary regular-polyhedron geometry.

## Limitations
There is no claim of a new general Radon formula, solution of the high-dimensional slicing problem, or a result for noncentral sections. The five constants are specialized explicit consequences of established integral geometry. The literature search did not find a pre-existing exact five-solid table, but obscure historical tables and handbooks remain a material originality risk. Independent mathematical auditing has not been performed.

## References
1. A. Koldobsky, *A sqrt(n) estimate for measures of hyperplane sections of convex bodies*, arXiv:1309.5271v1, first public 2013-09-20. https://arxiv.org/abs/1309.5271
2. R. J. Gardner, *Geometric Tomography*, 2nd ed., Cambridge University Press, 2006, background on spherical Radon transforms and intersection bodies (bibliographic background; full text not inspected here).
3. Published mathematical records on Platonic shadows, widths and section types, specifically the separately attributed identifiers recorded in the accompanying scientific review; these concern distinct statistics and do not supply the table in this work.
