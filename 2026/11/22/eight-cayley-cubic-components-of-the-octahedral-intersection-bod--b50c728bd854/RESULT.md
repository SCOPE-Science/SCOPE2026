# Eight Cayley cubic components of the octahedral intersection-body boundary

## Finding
Let \(O=\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}\). Its (Euclidean) intersection body \(IO\) has a radial function determined by the area of its central plane sections. For each \(v\ne0\), write \(a=|v_1|\), \(b=|v_2|\), and \(c=|v_3|\). Whenever at least two of \(a,b,c\) are positive,
\[
\rho_{IO}(v)=\frac{2(ab+ac+bc)}{(a+b)(a+c)(b+c)}.
\]
When exactly one coordinate of \(v\) is nonzero, the continuous value is \(2/|v_i|\). The normalization is \(\rho_{IO}(v)=\operatorname{area}(O\cap v^\perp)/\|v\|_2\); hence \(\rho_{IO}(u)\) is the section area for unit \(u\).

For each signed octant \(s=(s_1,s_2,s_3)\in\{\pm1\}^3\), set \(a_s=s_1x_1\), \(b_s=s_2x_2\), and \(c_s=s_3x_3\), and define
\[
F_s(x)=(a_s+b_s)(a_s+c_s)(b_s+c_s)-2(a_sb_s+a_sc_s+b_sc_s).
\]
**The real algebraic boundary is exactly**
\[
\partial_a(IO)=\bigcup_{s\in\{\pm1\}^3}\mathcal V_{\mathbb R}(F_s).
\]
These eight cubics are pairwise distinct and irreducible; each is projectively equivalent to the classical four-nodal Cayley cubic. Every one has exactly four ordinary double points in its affine real surface, at \(0\), \(2s_1e_1\), \(2s_2e_2\), and \(2s_3e_3\). The algebraic boundary has total degree \(24\), with no linear components. The origin and points on components outside their signed-octant patches may be extraneous algebraic points, not Euclidean boundary points.

## Assumptions and scope
All areas are two-dimensional Euclidean Hausdorff areas, all vectors are real, and \(O\) has vertices \(\pm e_i\). The intersection body is defined with the radial convention \(\rho_{IO}(v)=\rho_{IO}(v/\|v\|_2)/\|v\|_2\). The algebraic boundary means the real Zariski closure of the topological boundary in affine \(\mathbb R^3\). All eight signed octants, their coordinate-plane boundaries, and axis directions are included. No assertion is made for arbitrary polytopes or higher-dimensional cross-polytopes.

## Proof
**1. Laplace and section-area identity.** Let \(X_1,X_2,X_3\) be independent standard Laplace variables, each with density \(e^{-|t|}/2\), and put \(Y=v_1X_1+v_2X_2+v_3X_3\). For distinct positive \(a,b,c\), Fourier inversion and partial fractions give
\[
 f_Y(0)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\prod_{r\in\{a,b,c\}}\frac{dt}{1+r^2t^2}
 =\frac12\sum_{r\in\{a,b,c\}}\frac{r^3}{\prod_{q\ne r}(r^2-q^2)}.
\]
Directly clearing denominators, the final sum is
\[
\sum_{r\in\{a,b,c\}}\frac{r^3}{\prod_{q\ne r}(r^2-q^2)}
=\frac{ab+ac+bc}{(a+b)(a+c)(b+c)}.
\]
The coarea formula, the factor \(1/8\) in the joint Laplace density, and radial integration in the two-dimensional section imply
\[
8f_Y(0)=\frac1{\|v\|_2}\int_{O\cap v^\perp}e^{-\|x\|_1}\,d\mathcal H^2(x)
=\frac{2\operatorname{area}(O\cap v^\perp)}{\|v\|_2}.
\]
Thus the asserted radial formula follows. The identity extends continuously to coincident positive magnitudes and to one zero magnitude. On an axis, the section is the unit coordinate diamond, of area \(2\), proving the stated axial value. Continuity of section areas in direction proves that no unlisted boundary strata arise on coordinate planes.

**2. Algebraic patches.** In the open signed octant \(s_ix_i>0\), the condition \(x\in\partial(IO)\) is \(\rho_{IO}(x)=1\), which is precisely \(F_s(x)=0\), since its denominator is positive there. The diagonal point \(x=(3s_1/4,3s_2/4,3s_3/4)\) belongs to that patch, and the gradient of \(F_s\) there is nonzero: on its diagonal line the polynomial reduces to \(2r^2(4r-3)\), which has nonzero derivative at \(r=3/4\). Thus each cubic carries a smooth two-dimensional real boundary patch. The remaining coordinate-plane directions occur as limits of these patches, so the Euclidean boundary is contained in their union. Irreducibility below implies each patch is Zariski dense in its cubic.

**3. Cayley normal form and irreducibility.** Homogenize \(F_s\) using a new variable \(t\). Put \(a=a_s,b=b_s,c=c_s\) and perform the invertible projective linear substitution
\[
q_0=t-(a+b+c)/2,\qquad q_1=a/2,\quad q_2=b/2,\quad q_3=c/2.
\]
The homogenized polynomial becomes exactly
\[
\widehat F_s=-8(q_0q_1q_2+q_0q_1q_3+q_0q_2q_3+q_1q_2q_3).
\]
For \(C(q)=\sum_{i<j<k}q_iq_jq_k\), the equations \(\partial_iC=0\) say that every \(q_i\) solves the same quadratic \(\lambda^2-S\lambda+E_2=0\), where \(S=\sum_iq_i\) and \(E_2=\sum_{i<j}q_iq_j\). Thus there are at most two distinct coordinate values. If all are equal, the gradient vanishes only at the zero vector, excluded in projective space. If the distinct values have multiplicities \(1,3\), their sum constraint forces the thrice-repeated value to vanish. Multiplicities \(2,2\) force opposite values, but the quadratic equation then forces both to vanish. The only projective singularities are therefore the four coordinate points \([1:0:0:0]\), and its three permutations. Each has a nonsingular quadratic tangent cone, giving an ordinary double point. An irreducible factorization of a projective cubic would force two positive-degree surface components to intersect along a curve of singularities, contradicting this finite singular locus. Hence \(F_s\) is absolutely irreducible. The inverse projective substitution maps the four nodes to the stated affine points; no projective singularities lie at infinity.

**4. Eight distinct components.** Each octant gives a polynomial with quadratic part \(-2(a_sb_s+a_sc_s+b_sc_s)\). Equality up to a nonzero scalar between two such cubics would force their signed pair-products to be equal or opposite; their cubic parts eliminate the opposite possibility and force the same signed triple, so the polynomials are distinct. More directly, a polynomial for one signed octant vanishes at its positive smooth diagonal boundary point, whereas any differently signed polynomial evaluates to a nonzero value there (this can also be checked by the preceding explicit formula), or compare homogeneous coefficients. The eight irreducible hypersurfaces are exactly the Zariski closures of the eight open patches. Their reduced product has degree \(8\cdot3=24\), with no linear irreducible factors.

## Verification
Run \(python check.py\) with Python 3, SymPy and NumPy installed. The standalone test checks the Laplace partial-fraction identity exactly, all eight projective Cayley transformations, eight distinct factorizations, all four ordinary nodes for each cubic, smooth real octant patches, and independently reconstructed Euclidean sections obtained by intersecting octahedron edges with randomly oriented planes. At preparation it completed **320 checks** successfully. All-dimensional algebraic assertions follow from the proof, not finite tests.

## Relationship to prior work
Berlow, Brandenburg, Meroni and Shankar established an algebraic-boundary computation framework for general intersection bodies of polytopes and explicitly reported the three-cube's 14 components, including six planes and eight cubics. That work does not report this octahedral radial formula, its eight-Cayley-cubic classification, or the degree-24 result. Brandenburg and Meroni later studied translations and convexity, rather than this exact octahedral algebraic boundary. The presence of Cayley/elliptope cubics in the cube case is **known** and is not claimed as new here. This result addresses the polar-dual octahedron, whose boundary has no plane components; polar duality alone does not interchange intersection bodies.

## Limitations
The novelty assessment is literature-limited, not a formal proof of priority. It remains possible that an unindexed classical computation or unreviewed supplementary notebook contains an equivalent result. This is a three-dimensional standard-coordinate calculation only; its projective singular points are not all points of the actual topological boundary. The analytic proof and self-consistency tests are not independent mathematical audit.

## References
1. K. Berlow, M.-C. Brandenburg, C. Meroni, I. Shankar, *Intersection Bodies of Polytopes*, first public preprint 2021-10-12, [arXiv:2110.05996](https://arxiv.org/abs/2110.05996), [DOI 10.1007/s13366-022-00621-7](https://doi.org/10.1007/s13366-022-00621-7); in particular Section 5 and Example 5.3 (three-cube).
2. M.-C. Brandenburg, C. Meroni, *Intersection bodies of polytopes: translations and convexity*, [arXiv:2302.11764](https://arxiv.org/abs/2302.11764), [DOI 10.1007/s10801-024-01328-9](https://doi.org/10.1007/s10801-024-01328-9).
3. [MATHREPO: Intersection Bodies of Polytopes](https://mathrepo.mis.mpg.de/intersection-bodies/), associated method and cube example notebooks. The listed repository methods are not asserted to be a published exact octahedral computation.
