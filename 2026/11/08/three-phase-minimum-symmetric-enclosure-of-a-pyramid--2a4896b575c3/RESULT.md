# Three-phase minimum symmetric enclosure of a pyramid

## Finding
Let \(d\ge2\), let \(B\subset\mathbb R^{d-1}\) be a full-dimensional convex body centrally symmetric about the origin, and let \(A=\operatorname{vol}_{d-1}(B)>0\). Choose \(a\in B\) and \(h>0\), and define the pyramid
\[
T=\operatorname{conv}\big((B\times\{0\})\cup\{(a,h)\}\big).
\]
For \(t\in\mathbb R\) write \(m(t)\) for the infimum of \(d\)-dimensional volumes of centrally symmetric convex bodies containing \(T\) and having a symmetry center whose last coordinate equals \(t\). Then
\[
m(t)=A\begin{cases}
\frac{2h}{d}-2t,&t\le0,\\
\frac{2h}{d}+2t\left(1-\frac2d\right),&0\le t\le h/2,\\
2t,&t\ge h/2.
\end{cases}
\]
The infimum is attained for all \(t\). For \(d\ge3\), the unique unrestricted minimum-volume enclosure is the double pyramid with apices \((a,h)\) and \((-a,-h)\), with volume \(2Ah/d\). When \(d=2\), the global minimum is \(Ah\) and the admissible center-height minimizers form the interval \([0,h/2]\).

## Assumptions and scope
The base is an arbitrary compact full-dimensional centrally symmetric convex body in the horizontal hyperplane; no smoothness or polyhedral assumption is made. The apex's horizontal coordinate belongs to the base, possibly to its boundary. The center-height condition prescribes only its final coordinate; horizontal center coordinates are free. Volumes are ordinary Lebesgue measures. The dimension condition \(d\ge2\) is necessary for a positive-dimensional base.

## Proof
Let \(L\supseteq T\) be centrally symmetric about \(c=(u,t)\). Because \(L\) contains the base \(B\times\{0\}\), it contains its reflection \((2u+B)\times\{2t\}\). Its section at every intermediate height contains a Minkowski interpolation of these two translates. Since both are translates of \(B\), this interpolation is again a translate of \(B\), and has \((d-1)\)-volume \(A\). The slab between the two base planes consequently contributes at least \(2|t|A\) to the volume.

The two apex points forced into \(L\) are \((a,h)\) and \((2u-a,2t-h)\). Whenever an apex lies outside the closed slab between the base planes, convexity forces a pyramid joining that apex to the nearer base section. If the distance is \(q\), that pyramid has volume \(Aq/d\). These apex pyramids are disjoint in their interiors from the slab and from each other. For \(t\le0\), the lower and upper cap heights are both \(h\); their sum with the slab yields \(A(2h/d-2t)\). For \(0\le t\le h/2\), both exterior cap heights equal \(h-2t\), yielding \(A(2t+2(h-2t)/d)\). For \(t\ge h/2\), both apices lie between the base planes, so the slab alone gives \(2tA\). These are the stated lower bounds, with all endpoint cases included.

To attain them, choose \(u=0\) and let \(C_t=\operatorname{conv}(T\cup(2(0,t)-T))\). Since \(a,-a\in B\), each of the two apices lies vertically above a point of \(B\). For \(t\le0\), \(C_t\) is exactly the union of a lower pyramid of height \(h\), the prism \(B\times[2t,0]\), and an upper pyramid of height \(h\). For \(0\le t\le h/2\), it is the union of a lower pyramid of height \(h-2t\), the prism \(B\times[0,2t]\), and an upper pyramid of height \(h-2t\). For \(t\ge h/2\), it is exactly the prism \(B\times[0,2t]\). Convexity of \(B\), including the condition \(\pm a\in B\), ensures that the extra line segments between these three pieces never enlarge their horizontal sections. Direct integration of homothetic sections yields equality in each lower bound.

For \(d\ge3\), the displayed profile decreases strictly up to \(t=0\) and increases strictly thereafter. A global minimizer thus has center height zero. If its horizontal center is \(u\ne0\), its section at height zero contains \(B\cup(2u+B)\) and hence \(B+[0,2u]\), whose \((d-1)\)-volume is strictly greater than \(A\). The two pyramids from this larger base section to the opposing apices then have total volume strictly greater than \(2Ah/d\), a contradiction. Therefore the center is \((0,0)\); the symmetric hull \(C_0\) is mandatory and already has the minimum volume. Strict inclusion of convex bodies with nonempty interior strictly increases volume, proving uniqueness. For \(d=2\), the middle branch is constant, and the outer branches are strictly larger.

Finally take \(B=[0,1]^{d-1}-(1/2,\ldots,1/2)\), \(h=1\), and \(a=(1/2,\ldots,1/2)\). Translate the resulting volume-\(2/d\) bipyramid to put its base on the bottom facet of the unit cube. It contains all \(2^{d-1}\) facet vertices and one opposite-facet vertex. For \(d\ge3\), the lattice translates of this body cannot cover \(\mathbb R^d\): a periodic covering by \(\mathbb Z^d\) requires volume at least the lattice covolume one, whereas \(2/d<1\). This distinguishes general symmetric convex enclosures from the published parallelotope covering criterion.

## Verification
The argument requires only preservation of sectional volume under translation, the elementary pyramid formula \(Aq/d\), disjoint section integration, and strict growth of volume under nonzero Minkowski addition of a segment to a full-dimensional convex base. Direct numerical convex-hull volumes of the reflected square-pyramid model in dimension three were compared at \(t=-1,-1/5,0,1/10,3/10,1/2,9/10,3/2\); all agreed with the exact formula to floating-point tolerance. The analytic argument, rather than these finite checks, proves the all-dimensional result.

## Relationship to prior work
Grozev and Nikolov, *Lattice coverings by parallelotopes containing cube vertices*, arXiv:2610.21572 (first posted 15 October 2026), prove a covering criterion specifically for parallelotopes. The last paragraph provides a sharp-volume obstruction to removing that geometric hypothesis in dimensions at least three. Shen and Dubovski, *A sharp minimum for cube-apex bodies in every dimension*, arXiv:2610.11014 (first posted 7 October 2026), instead optimize a polar volume product of bodies formed by adding pairs of exterior cube apices; their Theorem 1 assumes a fixed central cube and a fixed sum of exterior heights. It does not prescribe the symmetry-center height for enclosing a single pyramid or state the three-branch formula. Classical planar minimum symmetric-enclosure phenomena are not claimed new. The candidate contribution is the complete dimension-dependent constrained-center volume profile and its rigidity statement.

## Limitations
The centered-base and vertically projected-apex assumptions matter. No analogous formula is claimed for non-centrally-symmetric bases, apices outside the base's vertical projection, or constraints on arbitrary center coordinates. Historical priority remains provisional, and independent mathematical review has not been performed.

## References
1. D. Grozev and N. Nikolov, *Lattice coverings by parallelotopes containing cube vertices*, arXiv:2610.21572 (2026), https://arxiv.org/abs/2610.21572.
2. H. Shen and P. B. Dubovski, *A sharp minimum for cube-apex bodies in every dimension*, arXiv:2610.11014 (2026), https://arxiv.org/html/2610.11014v1.
3. Á. G. Horváth and Z. Lángi, *On the convex hull and homothetic convex hull functions of a convex body*, Geometriae Dedicata (2022), https://doi.org/10.1007/s10711-022-00673-y.
