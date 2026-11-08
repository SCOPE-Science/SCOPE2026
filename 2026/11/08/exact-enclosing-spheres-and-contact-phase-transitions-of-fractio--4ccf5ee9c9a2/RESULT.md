# Exact enclosing spheres and contact-phase transitions of fractionally capped cubes

## Finding

Let \(n\ge3\) be an integer and \(0<\tau\le n\) a real number. Consider the Euclidean polytope
\[
K_{n,\tau}=\bigl\{x\in[0,1]^n:\textstyle\sum_{i=1}^n x_i\le\tau\bigr\}.
\]
Put \(q=\lfloor\tau\rfloor\), \(s=\tau-q\in[0,1)\), and define
\[
u=\min\{q/n,1/2\},\qquad v=\min\{\tau/n,1/2\},\qquad
 a=\operatorname{med}\{u,s/2,v\},
\]
where \(\operatorname{med}\) is the middle of three real numbers (equivalently, \(a=\min\{v,\max\{u,s/2\}\}\), because \(u\le v\)).

**Theorem.** The unique minimum-radius closed Euclidean ball containing \(K_{n,\tau}\) has center \(a\mathbf1_n\) and squared radius
\[
\boxed{R_{n,\tau}^{\,2}=na^2+q(1-2a)+s\max\{0,s-2a\}.}
\]
Its complete contact set is classified as follows. Let \(B_j\) be the family of Boolean vectors of Hamming weight \(j\). For \(s>0\), let \(F_{q,s}\) consist of vectors with exactly \(q\) coordinates equal to one, exactly one other coordinate equal to \(s\), and all remaining coordinates zero. Then:

1. If \(a=1/2\), the contact set is \(\bigcup_{j=0}^q B_j\), containing \(\sum_{j=0}^q\binom nj\) points. The fractional vertices, if any, are strictly inside the ball.
2. If \(a<1/2\) and \(s=0\), the contact set is \(B_q\), with \(\binom nq\) points.
3. If \(a<1/2\) and \(s>0\), the contact set is \(B_q\) when \(2a>s\), is \(F_{q,s}\) when \(2a<s\), and is \(B_q\cup F_{q,s}\) when \(2a=s\). The respective counts are \(\binom nq\), \(\binom nq(n-q)\), and \(\binom nq(n-q+1)\).

Every contact is a vertex; there are no other contacting points on any nontrivial face. Thus the theorem gives every center, radius, and vertex attaining the radius for every real cap \(\tau\), including integer caps and all transitions.

There are sharp **three consecutive contact phases** in the family \(\tau=1+s\) for each \(n\ge5\): for \(0<s<2/n\), only the weight-one Boolean vertices touch; for \(2/n\le s\le 2/(n-2)\), both the weight-one and the fractional vertex orbits touch; and for \(2/(n-2)<s<1\), only the fractional vertices touch. The squared radius remains identically \((n-1)/n\) throughout the first phase, although the polytopes strictly increase. At \(n=5\) and \(\tau=8/5\), the center is \((3/10)\mathbf1_5\), the squared radius is \(17/20\), and exactly \(25\) vertices contact the ball.

## Assumptions and scope

The ambient metric is the standard Euclidean metric of \(\mathbb R^n\); linear or affine transformations generally change the minimum enclosing sphere. The polytope is full dimensional because \(\tau>0\). The notation \(\operatorname{med}\) includes coincident arguments. The endpoint \(\tau=n\) is the entire cube; there \(q=n\), \(s=0\), \(a=1/2\), and all \(2^n\) cube vertices are contacts. No general weighted-knapsack or multi-cap assertion is made.

For \(0<s<1\), the complete vertex set is
\[
\bigcup_{j=0}^q B_j\ \cup\ F_{q,s}.
\]
For \(s=0\), it is \(\bigcup_{j=0}^q B_j\). Indeed, at any vertex at most one coordinate can lie strictly between zero and one, as otherwise the active sum constraint and coordinate bounds do not determine a point. A fractional coordinate forces the sum to be \(\tau\), with the remaining integral coordinates summing to \(q\); conversely these candidates are vertices. The fractional orbit has cardinality \(\binom nq(n-q)\).

## Proof

**1. Reduction to a unique diagonal center.** For a nonempty compact polytope with vertex set \(V\), the squared covering-radius objective is
\[
\Phi(c)=\max_{x\in V}\|x-c\|_2^2=\|c\|_2^2+\max_{x\in V}(\|x\|_2^2-2\langle x,c\rangle).
\]
It is strictly convex (the quadratic term is strictly convex and the second term is convex), hence has at most one minimizer. Coercivity guarantees existence. Every coordinate permutation preserves \(K_{n,\tau}\), so uniqueness forces its center to be \(a\mathbf1_n\) for some real \(a\). If \(a<0\), moving it to zero strictly decreases the distance to every nonnegative vertex. If \(a>1/2\), its distance to the origin exceeds \(\sqrt n/2\), whereas \((1/2)\mathbf1_n\) already encloses the entire cube in a ball of radius \(\sqrt n/2\). Thus \(0\le a\le1/2\).

**2. Exact competing vertex profiles.** For any Boolean vector of weight \(j\), its squared distance to \(a\mathbf1_n\) is
\[
D_j(a)=na^2+j(1-2a).
\]
For \(a\le1/2\), the maximum among Boolean vertices is \(D_q(a)\). If \(s>0\), a fractional vertex has squared distance
\[
D_F(a)=na^2+q+s^2-2(q+s)a
       =D_q(a)+s(s-2a).
\]
Thus all vertices are enclosed precisely at squared radius
\[
\Phi(a\mathbf1_n)=na^2+q(1-2a)+s\max\{0,s-2a\}.
\]
This equality holds for all real cap parameters; it has not replaced the fractional vertices by a zero-one approximation.

**3. Global minimization and the median law.** On \(0\le a\le s/2\), the controlling expression is \(D_F(a)\), with unconstrained minimizer \((q+s)/n\). On \(s/2\le a\le1/2\), the controlling expression is \(D_q(a)\), with unconstrained minimizer \(q/n\). Since \(q/n\le(q+s)/n\), the minimum of this continuous strictly convex piecewise quadratic is attained at
\[
a=\operatorname{med}\!\left\{\min(q/n,1/2),\ s/2,\ \min((q+s)/n,1/2)\right\}.
\]
This also handles \(s=0\) by continuity or direct minimization of \(D_q\). Uniqueness was established in part 1. Substitution gives the asserted radius.

**4. Exact equality cases.** If \(a<1/2\), the Boolean shell \(D_j\) is strictly increasing in \(j\), so only \(B_q\) can contribute. When \(s>0\), \(D_F-D_q=s(s-2a)\), which gives precisely the three alternatives in the theorem. If \(a=1/2\), every Boolean shell has squared distance \(n/4\), while every fractional vertex (when \(s>0\)) has squared distance \(n/4-s(1-s)<n/4\). Because the squared Euclidean norm is strictly convex on nondegenerate segments, an interior point of an edge or higher-dimensional face cannot be a maximum-distance point; therefore this vertex classification is also the entire contact set. Counting vertex orbits proves the contact-count formulas.

**5. The phase diagram and constant-radius interval.** Set \(q=1\) and \(n\ge5\). Then \(u=1/n\), \(v=(1+s)/n\) (until possible clipping at \(1/2\); this clipping does not affect the displayed transitions), and the inequalities comparing \(s/2\) with \(u,v\) are
\[
s<2/n,\qquad 2/n\le s\le2/(n-2),\qquad s>2/(n-2).
\]
These give respectively \(a=1/n\), \(a=s/2\), and \(a=(1+s)/n\). In the first interval \(2a>s\), so
\(R_{n,1+s}^{\,2}=n/n^2+1-2/n=(n-1)/n\), independent of \(s\). In the second interval equality \(2a=s\) gives the two simultaneously contacting orbits, including both boundary values. In the third interval \(2a<s\), leaving only fractional contacts. Since \(2/n<2/(n-2)<1\) for \(n\ge5\), all three nonempty phases occur. At \(n=5,\tau=8/5\), the numerical values and the count \(5+5\cdot4=25\) follow by exact substitution.

A second check of global optimality is available from the contact barycenters: the orbit means are \((q/n)\mathbf1\) for \(B_q\) and \(((q+s)/n)\mathbf1\) for \(F_{q,s}\); at a mixed contact, their convex hull contains the proposed center. In the single-orbit cases its orbit mean equals the proposed center. At \(a=1/2\), the uniform-rank Boolean layers contain a convex combination with mean \((1/2)\mathbf1\). These independently certify the necessary supporting-contact balance of a smallest enclosing ball.

## Verification

The standalone `verify.py` uses only Python's standard library and exact `fractions.Fraction` arithmetic. It enumerates **all actual vertices** for \(3\le n\le8\) at rational cap values (including integer parameters, fractions, and exact transition values) and checks the stated squared radius, every vertex-distance inequality, the complete contact count, orbit-barycenter constraints, and independent trial-center bounds. It covered **401 parameter instances and 45,451 exact rational assertions**. The special point \(n=5,\tau=8/5\) was checked separately, with 25 equality vertices. Execute `python3 verify.py` in the extracted package directory.

As an independent corroboration not required by the verifier, direct nonsymmetric SLSQP minimization of the enclosing-ball epigraph agreed with the formula on five additional parameter pairs. Finite tests do not substitute for the proof of the all-dimension, all-real-parameter result.

## Relationship to prior work

Black and Steiner (2026) analyze shortest paths and **vertex-edge graph diameter** on general fractional knapsack polytopes, rather than Euclidean minimum enclosing spheres; the standard one-cut cube is a particularly symmetric fractional-knapsack subclass. Gunluk (2026) studies **volume-approximation algorithms** for truncated hypercubes and discusses the same one-halfspace model. Their geometric objects motivate the present question, but their claims do not give an enclosing-sphere center, radius, or contacting-vertex classification.

The previously published **sharp minimum-sphere theorem for matroid independence polytopes** includes the integral-cap bodies \(K_{n,q}\) (uniform matroids), where every vertex is Boolean. Its general Boolean-vertex projection argument does not extend to nonintegral \(\tau\), because the new fractional vertices violate the identity \(\|x\|^2=\sum_i x_i\). For instance, at \(n=5,\tau=8/5\), projecting the cube midpoint onto this truncated cube gives \((8/25)\mathbf1_5\), while the actual minimum-sphere center is \((3/10)\mathbf1_5\). Hence the present continuous-cap law, the mixed-contact region, and the early radius plateau are not consequences of the integral-rank statement.

The previously published **three-phase John ellipsoid of a capped hypercube** covers exactly this same body for real \(\tau\) but solves the *maximum-volume inscribed ellipsoid*, not the minimum-radius **enclosing sphere**. Its facet tangencies do not determine the present vertex-contact phase diagram. General convex minimum-ball duality is used as standard background, with no novelty claim for convexity or the symmetrization step alone.

## Limitations

The proof uses equal coordinate caps and a single uniformly weighted sum constraint. It does not classify weighted knapsack cuts, intersections with multiple halfspaces, or minimum-volume enclosing ellipsoids. All contact counts refer to geometric vertices in the standard Euclidean embedding, not edges of the polytope's one-skeleton. The exact continuous rank law and contact phases are asserted as a mathematical contribution; discovery of an equivalent prior theorem under another name remains possible, and no independent review is claimed.

## References

1. Alexander E. Black and Raphael Steiner, *Finding Short Paths on Simple Polytopes*, arXiv:2603.05482v1, first public 2026-03-05, Sections 1–3; https://arxiv.org/abs/2603.05482. The full open manuscript is also available at https://optimization-online.org/2026/04/finding-short-paths-on-simple-polytopes/.
2. Kyra Gunluk, *Deterministic Volume Estimation of Truncated Hypercubes*, arXiv:2605.19809v1, first public 2026-05-19; https://arxiv.org/abs/2605.19809. The inspected open PDF was version 2, dated 2026-10-15, especially its introduction and Theorems 1.2–1.4.
3. *Sharp minimum-sphere bounds for matroid independence polytopes distinguish uniform density from arboricity two*, published research record https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-minimum-sphere-bounds-for-matroid-independence-polytopes-d--8fea8c7015da, full `RESULT.md` inspected; the integral uniform-rank case is prior.
4. *Three-phase John ellipsoid of a capped hypercube*, published research record https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-phase-john-ellipsoid-of-a-capped-hypercube--9b8726b32127, full `RESULT.md` inspected; the corresponding inscribed-ellipsoid result is prior.
