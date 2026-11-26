# Anticanonical volume of truncated-simplex toric Fano models

## Finding
For every integer \(n\ge2\), define the rank-\(n\) lattice
\[N=\{(z_0,\dots,z_n)\in\mathbb Z^{n+1}:\sum_{i=0}^{n}z_i=0\}\]
and the full-dimensional lattice polytope
\[Q_n=\{z\in N_{\mathbb R}:- (2n-1)\le z_i\le2\ \text{for }0\le i\le n\}.\]
Let \(X_n\) be the projective toric variety associated with the complete fan of cones over faces of \(Q_n\). Then \(X_n\) is a \(\mathbb Q\)-Fano toric variety and
\[\boxed{(-K_{X_n})^n=\frac{n(n+1)}{2^{n-1}(2n-1)}}.\]
The anticanonical degree is \(1\) in dimension two, \(3/5\) in dimension three, \(5/14\) in dimension four, and tends to zero with leading behavior \(n/2^n\). The result is an exact volume calculation for a family of rational toric Fano polytopes closely associated with small-alpha constructions.

## Assumptions and scope
The base field is algebraically closed of characteristic zero. All volumes are Euclidean volumes normalized with respect to the indicated character lattice; \((-K)^n\) denotes rational intersection theory on a possibly singular \(\mathbb Q\)-Fano variety. Set \(\ell=2n-1\). The characters of the torus of \(X_n\) form \(M=\operatorname{Hom}(N,\mathbb Z)\). Coordinate restrictions \(u_i:N\to\mathbb Z\), \(u_i(z)=z_i\), satisfy \(\sum_i u_i=0\). Each set of any \(n\) of the \(n+1\) coordinate functionals is a lattice basis of \(M\).

## Proof
**(1) Rays and the Fano polytope.** The polytope \(Q_n\) is the intersection of the simplex \(\{z_i\le2\}\) with \(z_i\ge-\ell\). Every vertex has exactly one coordinate \(-\ell\), one coordinate \(1\), and the other \(n-1\) coordinates \(2\). This follows because an intersection vertex has \(n\) active coordinate bounds, two lower bounds are impossible since \(-2\ell+2(n-1)<0\), and no vertex can have only upper active bounds because the last coordinate would be \(-2n<-\ell\). Therefore all vertices are integral and primitive (each has a coordinate equal to one), the origin is strictly inside \(Q_n\), and the face fan is a complete Fano fan. In particular its anticanonical divisor is \(\mathbb Q\)-Cartier and ample, with rational moment polytope the negative of the polar (which has the same volume). For volume computation use the polar
\[P_n=Q_n^\circ=\operatorname{conv}\{u_i/2,-u_i/\ell:0\le i\le n\}.\]
(The polar uses the convention that the facet inequalities on \(Q_n\) have right side one after dividing by their constants.)

**(2) Volume of the double simplex.** Let \(\Delta=\operatorname{conv}\{u_0,\dots,u_n\}\), an \(n\)-simplex centered at zero. Write \(\alpha=1/2\), \(\beta=1/\ell\), and \(r=\beta/\alpha=2/(2n-1)\). Thus \(1/n<r<1/(n-1)\). Every point \(-\beta u_i\) has barycentric coordinates relative to \(\alpha\Delta\) given by
\[\lambda_i=\frac{1-nr}{n+1}<0,\qquad \lambda_j=\frac{1+r}{n+1}>0\quad(j\ne i).\]
The point lies beyond precisely the facet \(F_i\) opposite \(\alpha u_i\). In the given range of \(r\), all segments joining distinct negative vertices stay in the corresponding positive barycentric halfspaces whenever the other coordinates would become negative. Consequently, the convex hull consists of \(\alpha\Delta\) together with exactly \(n+1\) pairwise interior-disjoint facet pyramids \(\operatorname{conv}(F_i,-\beta u_i)\). More explicitly, a convex combination of negative vertices cannot have two negative barycentric coordinates, since for each possible negative coordinate the positive contribution from any different vertex exceeds its negative magnitude: \((1+r)>(nr-1)\). This proves disjointness of the attached caps and that no further cells occur.

The altitude of the pyramid beyond \(F_i\), divided by the original altitude from \(\alpha u_i\) to \(F_i\), is
\[\frac{n\beta-\alpha}{(n+1)\alpha}.\]
Since all \(n+1\) facets have equal simplex altitude and facet volume, adding the caps gives
\[\operatorname{vol}(P_n)=\left(1+(n+1)\frac{n\beta-\alpha}{(n+1)\alpha}\right)\operatorname{vol}(\alpha\Delta)=\frac{n\beta}{\alpha}\operatorname{vol}(\alpha\Delta).\]

**(3) Lattice normalization.** In the lattice basis \(u_1,\dots,u_n\) of \(M\), the remaining vertex is \(u_0=-\sum_{i=1}^n u_i\). The edge matrix of \(\Delta\) based at \(u_0\) is \(I+\mathbf1\mathbf1^\top\), which has determinant \(n+1\). Therefore \(n!\operatorname{vol}(\Delta)=n+1\). Substitute \(\alpha=1/2\), \(\beta=1/(2n-1)\):
\[n!\operatorname{vol}(P_n)=\frac{2n}{2n-1}\frac{n+1}{2^n}=\frac{n(n+1)}{2^{n-1}(2n-1)}.\]
The toric top-intersection/normalized-volume identity now proves the claim. The displayed rational function is asymptotic to \(n/2^n\).

## Verification
The proof is symbolic for all integers \(n\ge2\). The independent standalone checker `verify_volume.py` constructs the \(2n+2\) polar vertices in a lattice basis, computes their convex-hull volume for dimensions two through six, and verifies the exact formula. These finite checks are not substituted for the general pyramid decomposition. The complete input polytope is given above, so the argument does not depend on reconstructing it from a citation.

## Relationship to prior work
Liu and Zhu, *K-polystable toric Fano varieties with small alpha invariants* (arXiv:2607.04005v1, first publicly posted 2026-07-04), motivate the use of toric polytopes formed from cyclic coordinate differences, with alpha invariant \(2/(2n+1)\). Their publicly accessible abstract and detailed indexed summaries emphasize the alpha invariant, the vertex description, and K-polystability; the exact anticanonical degree formula above was not identified in the searched records. The face-fan toric model is specified here independently by its coordinate inequalities; no new assertion about alpha invariants or K-polystability beyond the published context is needed. The general identity between anticanonical self-intersections and polar-polytope volumes is classical and is not claimed as new.

## Limitations
This statement concerns the explicit bounded hyperplane-slice polytopes \(Q_n\), not all toric Fano varieties and not the optimal anticanonical volume for any larger class. The published source full text was inaccessible during this comparison, so implicit prior coverage is a meaningful priority risk. The normalization and exact identification with every differently presented cyclic model must be checked independently before attributing an equality of constructions. No independent expert audit has been performed.

## References
1. Jihao Liu and Ziwen Zhu, *K-polystable toric Fano varieties with small alpha invariants*, arXiv:2607.04005v1 (2026-07-04), https://arxiv.org/abs/2607.04005.
2. William Fulton, *Introduction to Toric Varieties*, Princeton University Press, 1993, section on lattice-polytope volumes and degrees.
3. David Cox, John Little and Henry Schenck, *Toric Varieties*, AMS, 2011, chapters on toric divisors and polytope intersection theory.
