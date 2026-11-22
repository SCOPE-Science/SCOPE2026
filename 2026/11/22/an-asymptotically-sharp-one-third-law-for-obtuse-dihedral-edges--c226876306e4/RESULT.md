# An asymptotically sharp one-third law for obtuse dihedral edges of simple polyhedra

## Finding

Let \(P\) be any full-dimensional simple convex three-polytope with \(F\) facets and \(E\) edges, and let \(m(P)\) count the edges of strictly obtuse *interior* dihedral angle. For every integer \(F\ge7\),
\[
 E=3F-6,\qquad m(P)\ge F-5.
\]
Conversely, for each integer \(F\ge4\) and each \(\delta>0\), there is such a polytope with \(F\) facets satisfying
\[
 m(P)=F-4,\qquad \max_e\alpha_e(P)<\pi/2+\delta.
\]
Define the minimum possible obtuse-edge proportion under that upper angle restriction by
\[
 \rho_F(\delta)=\inf\left\{\frac{m(P)}{E(P)}:\ P\text{ simple convex three-polytope},\ F(P)=F,\ \max_e\alpha_e(P)<\pi/2+\delta\right\}.
\]
Then for all \(F\ge7\) and every \(\delta>0\),
\[
 \frac{F-5}{3F-6}\le\rho_F(\delta)\le\frac{F-4}{3F-6},\qquad
 \boxed{\lim_{F\to\infty}\rho_F(\delta)=\frac13}.
\]
The contribution is the universal lower count and asymptotically exact density. The existence of the underlying near-right-angle truncation family is credited to Li, Wang and Yu [1].

## Assumptions and scope

Here *simple* means precisely three facets meet at every vertex. An edge counts as obtuse only when its interior dihedral angle is **strictly greater** than \(\pi/2\), so right angles do not count. The universal bound requires \(F\ge7\); the six-facet cube has no obtuse edges. No assertion is made that the lower bound is attained at every finite \(F\); the upper construction remains one edge above it. The claim is confined to convex Euclidean three-polytopes.

## Proof

**Normal-fan area bound.** Outward unit normals to facets lie on the unit sphere \(S^2\). Because \(P\) is simple, each vertex yields a nondegenerate convex spherical triangle formed by its three incident facet normals. These normal-fan triangles partition \(S^2\), with disjoint interiors. Euler's relation and simplicity give
\[
 V=2F-4,\qquad E=3F-6,\qquad \sum_{v}\operatorname{area}(T_v)=4\pi.
\]
A polytope edge corresponds to a spherical normal-fan side of length \(\pi-\alpha_e\), where \(\alpha_e\) is its interior dihedral angle. Thus an obtuse edge corresponds precisely to a spherical edge shorter than \(\pi/2\).

Call a normal-fan triangle *good* if its three sides are all at least \(\pi/2\), and *bad* otherwise. In a good triangle, the spherical cosine rule, for example,
\[
 \cos A=\frac{\cos a-\cos b\cos c}{\sin b\sin c}\le0,
\]
shows that every spherical angle is at least \(\pi/2\). By Girard's formula its spherical area is at least \(\pi/2\). Let \(G\) and \(B\) count good and bad triangles. Each bad triangle touches a short spherical edge, each of which is incident to exactly two normal-fan triangles, so
\[
 G+B=2F-4,\qquad B\le 2m(P).
\]
If \(F\ge7\), there cannot be eight good triangles: they would occupy area at least \(4\pi\); any bad triangle then adds positive area, while if there were no bad triangles the total would contain at least \(2F-4\ge10\) good triangles. Hence \(G\le7\). Thus
\[
 2F-4-2m(P)\le G\le7.
\]
The integrality of \(m(P)\) yields \(m(P)\ge F-5\).

**Asymptotically matching witness.** We record the exact obtuse-edge count implicit in the Li–Wang–Yu near-right-angle truncation family [1], with its crucial premises checked directly. Choose a sufficiently large transcendental \(R>4\), an integer \(M\ge3\), and set
\[
 \theta=\arccos(-1/R),\quad
 v_j=(\cos(j\theta),\sin(j\theta),R^{j-M}),\ 0\le j<M,\quad n=(0,0,-1).
\]
The halfspaces with normals \(n,v_0,v_1,v_2\) and respective support numbers \(0,R^{-M},R^{1-M},R^{2-M}\) bound a tetrahedron with bottom face in \(z=0\) and upper vertex \((0,0,1)\). Indeed, the horizontal directions of \(v_0,v_1,v_2\) positively surround the origin (their successive circular gaps are all less than \(\pi\)), preventing a nonzero recession direction, and all three side planes meet at that upper vertex.

The positive-coefficient identity
\[
 v_{j+3}=Rv_j+v_{j+1}+(R-2/R)v_{j+2}
\]
ensures that the next normal uniquely maximizes its linear functional at the vertex common to the previous three side facets. A support number chosen strictly between its value there and the maximum over all other old vertices truncates exactly this vertex, creates one triangular facet, and preserves simplicity. Iterating gives a polytope with side facets \(F_0,\ldots,F_k\) and one bottom facet, so \(F=k+2\) and \(E=3k\). The bottom face meets exactly \(F_0,F_1,F_2\), while the side facets share an edge exactly when their indices differ by \(1\), \(2\) or \(3\). The next top vertex always lies in the three most recent side facets, proving the induction.

The scalar products of unnormalized side normals are
\[
 v_i\cdot v_j=\cos((j-i)\theta)+R^{i+j-2M}.
\]
For adjacent side facets the sign depends only on the index gap: for a gap of one, the cosine term equals \(-1/R\) and the positive correction is at most \(R^{-3}\), so the product is negative; for a gap of two, the cosine term is \(2/R^2-1\) and the correction at most \(R^{-4}\), again negative; and for a gap of three, the cosine term is \(3/R-4/R^3>0\), giving a positive product. Every bottom-to-side scalar product is \(-R^{j-M}<0\). An interior dihedral is obtuse exactly when its outward normals have positive scalar product. Thus the only obtuse edges correspond to the pairs of side facets at index gap three, exactly \(k-2=F-4\) edges.

Furthermore, every adjacent pair of unit outward side normals has scalar product strictly smaller than \(4/R\), by the same cosine formulas and \(j\le M-1\). Consequently every interior dihedral angle is smaller than \(\pi/2+\arcsin(4/R)\); choosing \(R\) sufficiently large ensures the prescribed \(\delta\) bound. Taking \(M=F-1\) constructs the example for each \(F\ge4\).

**Limit.** Combining the universal lower count with the just-verified witness, and substituting \(E=3F-6\), gives the two-sided bounds for \(\rho_F(\delta)\). Both endpoints tend to \(1/3\), proving the asserted limit for every fixed \(\delta>0\).

## Verification

The universal theorem relies on the area argument, not numerical tests. The witness construction's recurrence, initial boundedness, truncation incidence, and dihedral sign pattern are established analytically above. The included standalone `CHECKER.py` independently constructs small truncated polyhedra by high-precision halfspace intersection and verifies their vertex, edge and obtuse-edge counts for \(F=4,\ldots,10\) and \(F=4,\ldots,8\) at two distinct parameters. Run `python CHECKER.py` with `mpmath` installed. Finite checks corroborate but do not certify the infinite theorem.

## Relationship to prior work

Li, Wang and Yu [1, Theorem 1.2, Section 2] already prove arbitrary facet counts at an arbitrarily small excess over a right-angle dihedral upper bound. Their truncation family, recurrence, and facet incidences are not presented as new. The additional universal lower inequality \(m(P)\ge F-5\) for *all* simple polytopes is not a consequence of their construction alone; its spherical normal-fan counting proof and the resulting asymptotically sharp one-third law are the contribution. Coxeter [2, Theorem 2] classifies the zero-obtuse case as products of simplices, not a partial-obtuse quantitative inequality. Gromov [3] considers dihedral restrictions through different methods. A nearby mathematical record on two-sided angular pinching gives a facet upper bound under an additional lower-angle hypothesis, not a general count of strictly obtuse edges. Historical priority is provisional.

## Limitations

The exact fixed-facet minimum is unknown from these arguments: it lies between \(F-5\) and \(F-4\) for \(F\ge7\). No claim is made for nonsimple polytopes, higher dimensions, or an exact optimum at finite \(F\). A full historical priority check and independent mathematical audit remain outstanding.

## References

1. Z. Li, J. Wang and J. Yu, *Infinitely many convex polytopes with dihedral angles bounded above by \(\pi/2+\delta\)*, arXiv:2611.09021v1, first posted 6 November 2026. https://arxiv.org/abs/2611.09021
2. H. S. M. Coxeter, *Discrete Groups Generated by Reflections*, Annals of Mathematics **35** (1934), 588–621, especially Theorem 2. https://sites.math.washington.edu/~billey/classes/reflection.groups/references/Coxeter.1934.pdf
3. M. Gromov, *Convex Polytopes, Dihedral Angles, Mean Curvature and Scalar Curvature*, Discrete & Computational Geometry **72** (2024), 849–875, arXiv:2207.13346. https://arxiv.org/abs/2207.13346
