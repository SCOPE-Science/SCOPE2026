# The unique nine-contact Euclidean inball of the 1,371-facet reflexive eight-polytope

## Finding
For the explicitly embedded eight-dimensional reflexive lattice polytope \(P_8\) of Hofscheier and Nill, the largest contained Euclidean ball is unique and has radius
\[
 r=\frac{222}{257+14\sqrt{15}+3\sqrt{23}+2\sqrt{770}}
 =0.5825135583658234\ldots.
\]
Its center is \((w,w,r-1,r-1)\), where \(w=(x,y,z)\) is given explicitly below. Exactly **nine** of the **1,371** facets touch this ball. In contrast, the largest ball centered at the lattice origin has radius \(1/\sqrt{1525}\); the exact ratio of optimal to origin-centered radii is \(r\sqrt{1525}=22.747881652\ldots\).

The example is the small-dimensional counterexample to a longstanding facet-count conjecture, so its exact Euclidean ball geometry is an intrinsic metric datum of a distinguished reflexive polytope rather than a parameter-picked subfamily.

## Assumptions and scope
Work in the Euclidean space \(\mathbb R^8=\mathbb R^3\oplus\mathbb R^3\oplus\mathbb R^2\), using the standard orthonormal coordinates of the cited paper, **not** an arbitrary unimodularly transformed realization. Let \(Q\subset\mathbb R^3\) be the convex hull of these 21 lattice points, in this order:

```
(6,-6,0) (4,0,-2) (3,1,-2) (3,0,0) (3,0,-3)
(2,1,-1) (2,-2,2) (1,1,-1) (1,0,1) (1,-1,2)
(0,0,-3) (0,-1,2) (0,-3,3) (0,-6,0) (0,-6,-6)
(-1,0,0) (-1,0,-1) (-1,-2,2) (-2,-1,-1)
(-2,-2,-2) (-3,-3,0)
```
Define the orthogonal free sum \(Q\circ Q=\operatorname{conv}((Q,0)\cup(0,Q))\subset\mathbb R^6\), and let
\[
P_8=\operatorname{conv}\left(((Q\circ Q),-1,-1)\ \cup\ \{(0,-1,2),(0,1,-1)\}\right),
\]
where the zeros in the last two vertices denote six-dimensional zero vectors.

Set
\[
 D=257+14\sqrt{15}+3\sqrt{23}+2\sqrt{770},\qquad r=222/D,
\]
\[
 y=\frac{r(5+\sqrt{15})-6}{2},\quad
 s=\frac{r(5+\sqrt{23})-6}{2},\quad
 d=6+y-9r,
\]
\[
 x=\frac{s+d}{2},\quad z=\frac{s-d}{2},\qquad w=(x,y,z).
\]
The center is exactly \(c=(w,w,r-1,r-1)\); numerically \(w\approx(0.0973984323830,-0.4156834488400,-0.2442960934845)\), with last two coordinates approximately \(-0.4174864416342\).

Here "a facet touches the ball" means that its supporting hyperplane is at distance exactly \(r\) from \(c\); since the ball lies inside the polytope, the nearest supporting-hyperplane point lies in the corresponding facet.

## Proof
**1. Complete facet representation.** For each facet of \(Q\), write its primitive outer inequality as \(n\cdot X\le h\). All 37 facets have positive right-hand side \(h\in\{1,3,6\}\) (respectively 8, 11, and 18 facets). Set \(a=6n/h\in\mathbb Z^3\), and let \(\mathcal A\) be the set of 37 such vectors.

Because \(0\) lies in the interior of \(Q\), the orthogonal free sum \(Q\circ Q\) has facet inequalities \(a\cdot X+b\cdot Y\le6\) for all ordered \((a,b)\in\mathcal A^2\). The two-fold pyramid construction has precisely the following 1,371 facets:
\[
 a\cdot X+b\cdot Y+3t+2u\le1
 \quad((a,b)\in\mathcal A^2),
 \qquad -t\le1,\qquad -u\le1.
\]
This is also the concrete specialization of the general facet construction in the motivating paper (Lemma 3.2). All these normals are written in the original eight-dimensional Euclidean coordinates.

**2. A nine-facet upper-bound certificate.** Four members of \(\mathcal A\) are
\[
 a_0=(0,-1,0),\quad a_1=(-2,1,-2),\quad
 a_2=(-6,24,12),\quad a_3=(1,0,-1).
\]
Among the 1,369 side facets, select the seven ordered pairs
\[
 (a_0,a_0),\ (a_0,a_1),(a_1,a_0),\ (a_0,a_2),(a_2,a_0),\ (a_0,a_3),(a_3,a_0).
\]
Give them strictly positive weights \(14,\frac32,\frac32,1,1,9,9\), respectively, and give the base inequalities \(-t\le1\), \(-u\le1\) weights \(111\), \(74\). The weighted side-facet coordinate normals cancel because
\[
14(2a_0)+3(a_0+a_1)+2(a_0+a_2)+18(a_0+a_3)=0.
\]
Their Euclidean normal lengths, for the four unordered pair types, are \(\sqrt{15},\sqrt{23},\sqrt{770},4\). The coefficients in the two apex coordinates cancel against the weighted base inequalities. Thus for any ball of radius \(R\ge0\) centered anywhere in \(P_8\), summing the nine valid conditions "normal dot center plus \(R\) times normal length is at most 1" gives
\[
(257+14\sqrt{15}+3\sqrt{23}+2\sqrt{770})R\le222.
\]
In particular \(R\le r\) for **all** possible ball centers.

**3. An exact attaining center.** Substitution of the displayed values of \(x,y,z,r\) shows the following four identities:
\[
-2y+r(5+\sqrt{15})=6,\quad
-2x-2z+r(5+\sqrt{23})=6,
\]
\[
-6x+23y+12z+r(5+\sqrt{770})=6,\quad
x-y-z+9r=6.
\]
These are precisely the seven selected side inequalities at equality after the symmetric substitution \((X,Y,t,u)=(w,w,r-1,r-1)\); the two base inequalities are also equalities. The final identity containing \(\sqrt{770}\) is equivalent to \(rD=222\).

All **remaining 1,362 side inequalities hold strictly** at this center. This last finite comparison is certified without floating point in the enclosed `VERIFY.py`: the 37 primitive facet planes are exhaustively reconstructed from all noncollinear triples of the 21 input points; the script evaluates all 1,369 side-facet distances with rational intervals enclosing every square root via integer square roots. For the 1,362 nonactive pairs the lower bound on the unnormalized slack is strictly greater than \(1/500\). Consequently the ball of radius \(r\) centered at \(c\) is contained in \(P_8\), attains the upper bound, and touches exactly nine facets.

**4. Uniqueness.** All nine upper-bound weights are strictly positive; equality in their sum forces each of those nine radius constraints to be tight for any optimal center. The two base constraints force \(t=u=r-1\). Subtraction of the three swapped pairs forces
\[
(a_j-a_0)\cdot(X-Y)=0\qquad(j=1,2,3).
\]
The determinant of these three difference rows is \(148\ne0\), hence \(X=Y\). The four remaining side equalities then force the displayed \(x,y,z,r\) uniquely, establishing uniqueness of the maximum ball center.

**5. The origin-centered radius.** The full list of facet normals has maximum squared Euclidean norm \(1525=13+756+756\); the maximum \(756\) comes from \(a_2\in\mathcal A\). Every facet has right-hand side one, so the largest ball centered at the lattice origin has radius precisely \(1/\sqrt{1525}\).

## Verification
Run `python3 VERIFY.py` in an ordinary Python 3 environment; no third-party library is required. The program enumerates the 1,330 triples of the 21 supplied points, reconstructs exactly 37 supporting planes, verifies the four selected facet vectors, the positive normal-cancellation certificate, the nonzero uniqueness determinant, the squared-norm bound, and all 1,362 strict nonactive side inequalities. It constructs rigorous rational intervals using integer `isqrt` on scaled nonnegative integers; hence its sign comparisons are **certificates**, not approximate numerical experiments. The seven active side equalities are proved by the displayed algebraic identities, not by interval comparison.

## Relationship to prior work
Hofscheier and Nill introduced this exact reflexive polytope and proved that it has 44 vertices and 1,371 facets, exceeding a formerly conjectured extremal facet bound (arXiv:2611.08819v1, Theorem 2.1). Their Lemma 3.2 gives the general pyramid facet construction. Their paper does not calculate the Euclidean maximal inscribed ball, its center, the count of its contact facets, or the metric discrepancy from the lattice origin. Those are the additional claims here. The general ability to formulate a largest-inscribed-ball problem as linear inequalities is standard and is not claimed as novel.

## Limitations
This theorem concerns the single explicit eight-dimensional lattice realization given above, not all reflexive polytopes or all unimodular embeddings of this combinatorial type. The Euclidean quantities change under general unimodular coordinate transformations. The finite facet enumeration is exhaustive for this input; it is not evidence of a uniform theorem in arbitrary dimension. Novelty is assessed against identified accessible sources, not independently certified mathematical priority.

## References
Hofscheier, J., and Nill, B. *Reflexive polytopes can have doubly exponentially many vertices*, arXiv:2611.08819v1 (first submitted 2026-11-06), in particular Theorem 2.1, Lemma 3.2, and the vertex appendix. https://arxiv.org/abs/2611.08819

Haase, C., and Melnikov, I. *The reflexive dimension of a lattice polytope*, Annals of Combinatorics 10 (2006), 211–217, for the earlier general reflexive-extension framework, as cited by Hofscheier and Nill.
