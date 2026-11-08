# Exact square-root singularities enumerate the Voronoi facets of every flat two-torus

## Finding
Let \(\Lambda\subset\mathbb R^2\) be any full-rank Euclidean lattice, let \(T=\mathbb R^2/\Lambda\) carry its intrinsic quotient distance and normalized area measure, and choose \(X,Y\) independently according to that measure. Define
\[
F_\Lambda(r)=\Pr\bigl(d_T(X,Y)\le r\bigr),\qquad r\ge0.
\]
The new result is an **exact local singularity classification** for the scalar function \(F_\Lambda\): its radial derivative has a square-root birth precisely at the perpendicular distance of each genuine Voronoi facet, with a universal coefficient that recovers the number of opposite facets at that distance, even when several facets share that distance. Voronoi vertices, including coincident radius thresholds, create no false square-root births. No genericity or rectangularity hypothesis is required. A resulting explicit reconstruction of the lattice is consistent with a pre-existing inverse-distance result; uniqueness of flat-torus reconstruction is **not** claimed here as a novel theorem.

More precisely, recover the lattice covolume by
\[
A=\lim_{r\downarrow0}\frac{\pi r^2}{F_\Lambda(r)}.
\]
For every \(r>0\) where \(F_\Lambda\) is differentiable, define the angular survival function
\[
\Theta(r)=\frac{A}{r}F_\Lambda'(r).
\]
Let \(d>0\), and let \(m(d)\) be the number of **opposite pairs** of positive-length facets of the origin-centered Voronoi polygon whose perpendicular distance from the origin is \(d\). Then the following limit exists at every \(d>0\), with the continuous version of \(\Theta\):
\[
\boxed{\displaystyle
\lim_{\varepsilon\downarrow0}
\frac{\Theta(d+\varepsilon)-\Theta(d-\varepsilon)}{\sqrt\varepsilon}
=-4m(d)\sqrt{\frac2d}.}
\]
Thus the nonzero square-root differences of the radial angular derivative recover every facet distance and its exact multiplicity. There are exactly two opposite facet pairs for a rectangular Voronoi cell, or three for a hexagonal one (counted with multiplicity). Twice these distances give the lengths of the Voronoi-relevant lattice vectors. The local coefficient formula supplies an exact, collision-resistant mechanism for extracting that data directly from the law; earlier work established reconstruction in a different manner.

## Assumptions and scope
A lattice is an integer span of two linearly independent vectors in \(\mathbb R^2\). The torus distance is \(d_T([x],[y])=\min_{v\in\Lambda}\|x-y-v\|\). Probability refers to independent normalized-Haar-uniform points, not Euclidean chord distances in an embedding. The Voronoi cell is the compact centrally symmetric polygon
\[
V_\Lambda=\{z\in\mathbb R^2:\|z\|\le\|z-v\|\text{ for all }v\in\Lambda\}.
\]
A Voronoi facet is a nondegenerate one-dimensional face. Its support line is \(z\cdot n=d\) with \(\|n\|=1\) and \(d>0\). Singular limits above refer to exact distribution functions, not estimates from finitely many sampled distances.

## Proof
**1. Uniform displacement and volume.** By translation invariance, the difference \([X-Y]\) is uniform on the quotient. Choosing its nearest-origin representative puts a uniform random point \(Z\) in \(V_\Lambda\), up to boundaries of zero area. Consequently
\[
F_\Lambda(r)=\frac{\operatorname{area}(V_\Lambda\cap B_r)}{A},\qquad
A=\operatorname{area}(V_\Lambda)=\det\Lambda>0.
\]
Because the origin lies in the interior of the Voronoi cell, a sufficiently small ball is contained in it. Thus \(F_\Lambda(r)=\pi r^2/A\) for sufficiently small positive \(r\), proving the stated recovery of \(A\).

**2. Exact angular representation.** Write the distinct supporting facets as \(z\cdot n_j\le d_j\), with outward normal directions \(\phi_j\). For a radial point \(r(\cos\theta,\sin\theta)\), the \(j\)-th inequality fails precisely when \(r>d_j\) and
\[
|\theta-\phi_j|_{\mathbb S^1}<\alpha_j(r),\qquad
\alpha_j(r)=\arccos(d_j/r).
\]
Set \(I_j(r)\) to be that open circular angular interval, empty when \(r\le d_j\). Polar integration yields the exact identity
\[
\Theta(r)=2\pi-\left|\bigcup_jI_j(r)\right|,
\qquad F_\Lambda'(r)=\frac{r}{A}\Theta(r).
\]
The union of finitely many intervals has continuous length, so \(\Theta\) extends continuously to all positive radii.

**3. Detecting precisely the facet births.** At a facet threshold \(r=d_j\), its angular half-width obeys
\[
\alpha_j(d_j+\varepsilon)=\sqrt{\frac{2\varepsilon}{d_j}}+O(\varepsilon^{3/2}).
\]
For a lattice Voronoi polygon, the orthogonal foot \(d_jn_j\) is strictly inside its facet, rather than merely on its support line. Indeed, in the four-facet case it is the midpoint of an orthogonal basis vector. In the six-facet case, let \(v_0+v_1+v_2=0\) be its strict obtuse superbase. If the facet is associated with \(v_0\), the foot is \(v_0/2\). The other relevant vectors are \(\pm v_1,\pm v_2\), and for \(i=1,2\) one has \(0<-v_0\cdot v_i=\|v_i\|^2+v_i\cdot v_{3-i}<\|v_i\|^2\) (with the other index interpreted as \(2\) or \(1\)), which makes every other facet inequality strict at that foot. Thus the newborn angular interval is initially disjoint from the union of older forbidden intervals. Distinct newborn facet directions are separated, hence their intervals do not overlap for sufficiently small \(\varepsilon\). There are \(2m(d)\) such facets at a shared distance \(d\); their total new forbidden angular measure is
\[
2m(d)\cdot2\sqrt{\frac{2\varepsilon}{d}}+O(\varepsilon^{3/2}).
\]
Any previously active interval endpoint varies Lipschitz-continuously near \(d\), since \(\arccos(d_j/r)\) is smooth whenever \(r>d_j\). The length of a finite union of intervals with Lipschitz-moving endpoints is also locally Lipschitz, including when endpoints meet at Voronoi-vertex directions. Its contribution to a symmetric difference across \(d\) is therefore \(O(\varepsilon)\). These estimates give the boxed coefficient.

If \(d\) is not a facet distance, all relevant interval endpoints move locally Lipschitz-continuously; thus the same square-root-normalized symmetric difference is zero. Hence the nonzero limits identify exactly the finite multiset \(\{(d,m(d))\}\), with no spurious singularities from polygon vertices.

**4. A reconstruction consequence (with prior attribution).** The planar lattice Voronoi polygon has either four or six genuine facets. In the four-facet case, the two perpendicular pairs correspond to an orthogonal primitive lattice basis, whose two lengths are the two recovered values \(2d\), repeated as necessary. This uniquely specifies its isometry class.

In the six-facet case, the three pairs correspond to vectors \(v_0,v_1,v_2\) of a strict obtuse superbase satisfying \(v_0+v_1+v_2=0\), such that any two form a primitive lattice basis. Their three unordered lengths \(\ell_j=2d_j\) are recovered. Choose any two as a basis. Their inner product is fixed by the third length:
\[
\langle v_0,v_1\rangle=\frac{\ell_2^2-\ell_0^2-\ell_1^2}{2}.
\]
The resulting Gram matrix specifies this basis up to an orthogonal transformation. Relabeling the superbase does not change the spanned lattice, and reflection is permitted. Thus the singularity data also constructively reconstruct the lattice in every case, including equal lengths and rectangular degeneracies. Injectivity of the global law for planar flat tori is also implied by the lattice-point reconstruction described in Proposition 5.16 of the 2021 preprint version of Mémoli and Needham; it is not the originality claim here.

**5. Geometric interpretation of a published flat-torus example.** Example 3.18 of Mémoli and Needham (arXiv:1810.09646) describes two lattices generated respectively by \((1,0),(1/3,1)\) and \((1,0),(2/3,1)\), asserting that the quotient tori are nonisometric although their distance laws agree. However the Euclidean reflection \(R(x,y)=(-x,y)\) sends the first lattice to the second: its generators become \((-1,0),(-1/3,1)\), and replacing this pair by \((1,0),(2/3,1)\) is an integral unimodular basis change. Hence those two quotient tori are isometric, so that example does not contradict the reconstruction theorem.

## Verification
Run `python verify_torus_law.py` with Python 3 and NumPy. The standalone program constructs origin Voronoi polygons using lattice halfspace clipping, computes their facet-distance multiplicities, numerically tests the predicted square-root thresholds, and independently compares radial cumulative distribution functions to direct samples of quotient distances. It also checks the reflection and basis-change identity above using exact rational arithmetic. A recorded execution reported `VERIFY_OK exact_reflection_isometry=1 polygon_cases=17 facet_threshold_groups=46 max_signature_relative_error=7.0705357e-05 independent_pair_cdf_checks=10 max_cdf_error=0.00225397`.

The proof above establishes the infinite family of lattices and all exact singular coefficients; the computations are reproducible checks rather than proof of an infinite assertion.

## Relationship to prior work
McKilliam, Grant, and Clarkson (2014) give the Voronoi-relevant-vector and obtuse-superbase formalism for nearest-lattice-point geometry. Herman and Pakianathan (2014) study homogeneous-space distance distributions and mean-distance bounds. Mémoli and Needham (arXiv:1810.09646v3, Proposition 5.16) explicitly describe reconstruction of a planar lattice point set from the global distance distribution by reading critical radii; that **covers the general uniqueness consequence** and must be credited. Their later arXiv version 5, Example 3.18, calls two particular planar flat tori nonisometric, but these are related by the elementary reflection and basis change shown above. Kurlin (2022) supplies a complete independent classification of planar lattices by obtuse superbases. The specific contribution here is different from the earlier inverse claim: an exact two-sided square-root coefficient at **every** facet-birth radius, including all multiplicity coincidences, together with proof that no Voronoi vertex radius creates a spurious coefficient. The inspected sources discuss critical radii and lattice invariants but do not state this coefficient formula or its full no-spurious-threshold classification.

## Limitations
Isometry includes orientation reversal. An intrinsically oriented or marked lattice cannot be recovered from this orientation-blind distribution. The coefficient extraction uses an exact continuum distribution and is potentially ill-conditioned under sampling error; no statistical error bound is asserted. The argument relies on the four/six-facet classification of planar lattice Voronoi polygons and makes no claim for higher-dimensional nonrectangular flat tori or general nonflat metric surfaces. The already-established qualitative recoverability of the lattice from the distance law is not presented as original; the new assertion is the precise local threshold signature. Mathematical correctness and historical priority have not been independently audited.

## References
1. R. G. McKilliam, A. Grant, and I. V. L. Clarkson, *Finding a closest point in a lattice of Voronoi's first kind*, arXiv:1405.7014v1, May 27, 2014; https://arxiv.org/abs/1405.7014.
2. M. Herman and J. Pakianathan, *On the distribution of distances in homogeneous compact metric spaces*, arXiv:1407.5607v1, July 21, 2014; https://arxiv.org/abs/1407.5607.
3. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646, first posted October 23, 2018, Example 3.18; published in *Studies in Applied Mathematics* 149 (2022), 943–1001; https://arxiv.org/abs/1810.09646.
4. V. Kurlin, *Mathematics of 2-dimensional lattices*, arXiv:2201.05150v3, March 28, 2022, Theorems 2.9 and 3.7; https://arxiv.org/abs/2201.05150.
