# A sharp two-orbit minimum-sphere transition for panhandle matroid base polytopes

## Finding
For every integer triple \(2\le r<p\), \(t\ge2\), put \(n=p+t\), let \(A=[p]\) and \(B=\{p+1,\dots,p+t\}\), and form the canonical panhandle matroid base polytope
\[
P_{r,p,t}=\operatorname{conv}\{\mathbf1_S:S\subseteq A\cup B,\ |S|=r,\ |S\cap B|\le1\}\subset\mathbb R^n.
\]
Its unique minimum enclosing Euclidean ball has center
\[
c_{r,p,t}=\begin{cases}
\frac r n\mathbf1_n,&(r-1)t\le p,\\[4pt]
\frac{r-1}{p}\mathbf1_A+\frac1t\mathbf1_B,&(r-1)t\ge p,
\end{cases}
\]
where the two expressions agree at equality, and squared radius
\[
\boxed{R_{r,p,t}^2=
 r-\frac{r^2}{n}-\frac{\bigl((r-1)t-p\bigr)_+^2}{ptn}
 =\begin{cases}
 r-\frac{r^2}{n}, &(r-1)t\le p,\\[4pt]
 r-\frac{(r-1)^2}{p}-\frac1t,&(r-1)t\ge p.
\end{cases}}
\]
Here \(u_+=\max\{u,0\}\). In the regime \((r-1)t\le p\), **every** vertex of \(P_{r,p,t}\) touches the minimum enclosing sphere. If \((r-1)t>p\), **exactly** the \(t\binom{p}{r-1}\) vertices indexed by bases having one element in \(B\) touch; the other \(\binom p r\) vertices lie strictly inside. Their common squared-distance clearance from the sphere is
\[
\boxed{\frac{2\bigl((r-1)t-p\bigr)}{pt}.}
\]
Thus the inequality \((r-1)t=p\) is the exact contact transition. The squared-radius loss from the uniform-hypersimplex sphere has a quadratic onset beyond this transition.

## Assumptions and scope
All distances are ordinary Euclidean distances in the standard orthonormal basis of \(\mathbb R^n\), equivalently the induced Euclidean metric on the affine hull \(\sum_i x_i=r\). No rescaling or affine equivalence is used. The family consists of all nonminimal panhandle matroids with \(r\ge2\), \(p>r\) and \(t\ge2\). For these parameters, both base orbits described below are nonempty.

The squared radius is for the unique smallest closed Euclidean ball containing \(P_{r,p,t}\), not its largest inscribed ball. Both extremal centers lie inside the polytope, as certified below. The case \(p=r\), excluded here, is the minimal-matroid family and has a previously recorded enclosing-sphere formula.

## Proof
Every vertex is the indicator of a basis containing either \(r\) pan coordinates and no handle coordinate (orbit \(\mathcal A\)), or \(r-1\) pan coordinates and exactly one handle coordinate (orbit \(\mathcal B\)). The two nonempty orbits have sizes \(\binom p r\) and \(t\binom p{r-1}\). Their barycenters are respectively
\[
a=\frac rp\mathbf1_A,\qquad b=\frac{r-1}{p}\mathbf1_A+\frac1t\mathbf1_B.
\]
Put \(u=\frac rn\mathbf1_n\), and \(\lambda=\frac{rt}{n}\). Direct coordinate calculation gives
\[
u=(1-\lambda)a+\lambda b.
\]
The coefficient condition \(\lambda\le1\) is equivalent to \((r-1)t\le p\).

We use the following elementary exact sphere certificate. Suppose a finite point set has center \(c\), and some nonempty subset of its points is all at squared distance \(R^2\) from \(c\), with a convex combination of those points equal to \(c\). For any other center \(y\), the same convex combination of squared distances to \(y\) equals \(R^2+\|y-c\|^2\) by expansion and cancellation of the cross term. Hence any ball containing that subset has squared radius at least \(R^2+\|y-c\|^2\). If the remaining points have squared distance at most \(R^2\) from \(c\), then \(c\) is the unique global minimum-ball center for the entire set. This applies to the polytope because a Euclidean ball is convex.

If \((r-1)t\le p\), the displayed decomposition makes \(u\) a convex combination of the two orbit barycenters, and therefore of the full vertex set. Every vertex \(v\) has precisely \(r\) coordinates equal to one, so
\[
\|v-u\|^2= r-\frac{r^2}{n}.
\]
All vertices contact and the sphere certificate proves optimality and uniqueness, including equality at the transition.

Suppose now \((r-1)t>p\). The orbit-\(\mathcal B\) barycenter is \(b\); every \(w\in\mathcal B\) satisfies
\[
\|w-b\|^2=r-\|b\|^2=r-\frac{(r-1)^2}{p}-\frac1t.
\]
For every \(v\in\mathcal A\), the difference between squared distances to \(b\) is
\[
\|w-b\|^2-\|v-b\|^2
=2\left(\frac{r-1}{p}-\frac1t\right)
=\frac{2((r-1)t-p)}{pt}>0.
\]
Thus all \(\mathcal B\) vertices contact, while every \(\mathcal A\) vertex lies strictly inside. The sphere certificate applied to the \(\mathcal B\) orbit gives global minimality and uniqueness. Lastly the exact identity
\[
\left(r-\frac{r^2}{n}\right)-\left(r-\frac{(r-1)^2}{p}-\frac1t\right)
=\frac{((r-1)t-p)^2}{ptn}
\]
proves the unified radius formula. All assertions follow for every integer triple in the specified domain.

## Verification
An independent standard-library exact-arithmetic enumerator, `verify_panhandle.py`, constructs all vertices for each of 105 parameter triples satisfying \(2\le r<p\le8\), \(2\le t\le6\). For every vertex it checks the proposed center and squared-radius inequality, exact contact classification, both orbit barycenters, the global squared-distance variance certificate at five off-center probes, and the radius-deficit identity. It includes 28 strict all-contact cases, 68 strict handle-contact cases, and nine boundary ties. Run `python verify_panhandle.py`; success prints `PANHANDLE_OUTER_BALL_EXACT_PASS`. The exhaustive checks are finite corroboration; the preceding proof establishes the theorem for all allowed parameters.

## Relationship to prior work
Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez and Yin define these panhandle matroids and prove their base-polytope inequalities in arXiv:2201.12442, Definition 4.1 and Proposition 4.4, in the course of studying Ehrhart polynomials and paving-matroid slices. Deligeorgaki, McGinnis and Vindas-Meléndez study Ehrhart positivity for the same objects in arXiv:2311.01640. Neither of these inspected texts establishes the outer Euclidean sphere and two-orbit contact transition stated here.

The public record *Minimal-matroid base polytopes have a one-exception minimum-sphere transition* computes the enclosing ball at \(p=r\), where \(\binom pr=1\). This is a genuine special case but does not imply the present complete family \(p>r\), in which the departing orbit has \(\binom pr>1\) vertices. A public result on panhandle **inballs** concerns facet distance optimization rather than the vertex-based minimum enclosing ball. These are close prior comparisons, not claims of general priority or an independent novelty certificate.

## Limitations
The contact and radius claims use exactly the specified canonical indicator-vector realization; they need not survive arbitrary affine transformations. No statement is made for all matroid base polytopes, about other kinds of enclosing ellipsoids, or about intrinsic inballs. The construction uses a standard barycentric minimum-ball certificate; an unindexed equivalent formula could exist in the extensive generalized-permutohedron or matroid-polytope literature. Independent mathematical review has not been performed.

## References
1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first posted 2022-01-28. https://arxiv.org/abs/2201.12442
2. D. Deligeorgaki, D. McGinnis, A. R. Vindas-Meléndez, *Ehrhart Bounds for Panhandle and Paving Matroids Through Enumeration of Chain Forests*, arXiv:2311.01640, first posted 2023-11-02. https://arxiv.org/abs/2311.01640
3. *Minimal-matroid base polytopes have a one-exception minimum-sphere transition*, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-minimal-matroid-base-polytopes-have-a-one-exception-minimum-sphe--82125c812c6f/RESULT.md (covers only the \(p=r\) limit).
4. *Three Euclidean inball phases of panhandle matroid base polytopes*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-three-euclidean-inball-phases-of-panhandle-matroid-base-polytope--3e805ae8aac8/RESULT.md (different metric optimization).
