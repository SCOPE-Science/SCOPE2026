# Marked chains give the exact Euclidean inradius of regular marked order polytopes
## Finding
Let \((P,\lambda)\) be a finite regular marked poset. Assume that the marked subset \(P^*\) contains every extremal element of \(P\), so the marked order polyhedron is bounded. Write
\[
\widetilde P=P\setminus P^*
\]
and let
\[
\widetilde{\mathcal O}(P,\lambda)\subset\mathbb R^{\widetilde P}
\]
be the projected marked order polytope in the standard Euclidean metric.

A **marked interval chain** is a saturated chain
\[
C:\qquad
a=p_0\prec p_1\prec\cdots\prec p_k=b
\tag{1}
\]
such that \(a,b\in P^*\) and
\[
p_1,\ldots,p_{k-1}\in\widetilde P.
\]
For a regular marked poset there are no cover relations between marked elements, so
\[
k\ge2.
\]
Define its Euclidean chain weight by
\[
W(C)=2+(k-2)\sqrt2.
\tag{2}
\]

Then the exact Euclidean inradius is
\[
\boxed{
r_{\mathrm{in}}\bigl(\widetilde{\mathcal O}(P,\lambda)\bigr)
=
\min_C
\frac{\lambda(b)-\lambda(a)}{W(C)}.
}
\tag{3}
\]

Thus a continuous optimization over all possible centers collapses to a finite bottleneck problem over marked saturated chains.

Writing the value in (3) as \(r\), the complete incenter set is
\[
\boxed{
\begin{aligned}
\operatorname{Cent}
=
\bigl\{
c\in\mathbb R^{\widetilde P}:\
&c_q\ge\lambda(a)+r
&&\text{for }a\prec q,\ a\in P^*,\\
&c_q-c_p\ge r\sqrt2
&&\text{for }p\prec q,\ p,q\in\widetilde P,\\
&c_p\le\lambda(b)-r
&&\text{for }p\prec b,\ b\in P^*
\bigr\}.
\end{aligned}
}
\tag{4}
\]

Every marked interval chain attaining the minimum in (3) forces tangency to every facet along that chain at every incenter.

There are also canonical extremal incenters. For \(p\in\widetilde P\), define
\[
L_p
=
\max_{a\leadsto p}
\left(
\lambda(a)+r\,W(a\leadsto p)
\right),
\tag{5}
\]
where the maximum is over saturated paths beginning at a marked element and having no other marked vertex, and define
\[
U_p
=
\min_{p\leadsto b}
\left(
\lambda(b)-r\,W(p\leadsto b)
\right)
\tag{6}
\]
dually. Here \(W\) is the sum of cover-normal lengths: an edge incident with a marked endpoint contributes \(1\), while an edge between two unmarked elements contributes \(\sqrt2\).

Then
\[
\boxed{L=(L_p)\quad\text{and}\quad U=(U_p)}
\tag{7}
\]
are both incenters, and every incenter \(c\) satisfies
\[
L_p\le c_p\le U_p
\qquad(p\in\widetilde P).
\tag{8}
\]
Consequently,
\[
\boxed{
\text{the incenter is unique}
\iff
L_p=U_p\text{ for every }p\in\widetilde P.
}
\tag{9}
\]

For the ordinary order-polytope marking with one bottom mark \(0\) and one top mark \(1\), (3) reduces to the familiar longest-chain barrier. The marked theorem is genuinely more flexible: different marked intervals compete using both their marking gaps and their saturated-chain lengths.

## Assumptions and scope
Regularity is Pegel's condition that every cover relation is non-redundant. In a regular marked poset, the source proves that every cover relation corresponds to a facet, that the marking is strict, that no two marked elements are joined by a cover, and that an element covers or is covered by at most one marked element.

The assumption that all extremal elements are marked is the source's boundedness condition. It guarantees that every unmarked element lies above at least one marked element and below at least one marked element.

The metric is the standard Euclidean metric after projecting away the fixed marked coordinates. This projection is an isometry on the free-coordinate affine space.

The theorem is not asserted for a nonregular presentation without first identifying its actual facets. Redundant cover inequalities define the same polytope but do not themselves represent supporting facets and therefore must not be used as Euclidean clearance constraints.

## Proof
The source proves that for a regular marked poset the facets of the marked order polytope are in bijection with cover relations.

There are three possible kinds of cover relation.

If
\[
a\prec q,
\qquad
a\in P^*,
\quad
q\in\widetilde P,
\]
the facet inequality is
\[
c_q\ge\lambda(a),
\]
whose normal has Euclidean norm \(1\).

If
\[
p\prec q,
\qquad
p,q\in\widetilde P,
\]
the facet inequality is
\[
c_q-c_p\ge0,
\]
whose normal
\[
e_q-e_p
\]
has Euclidean norm \(\sqrt2\).

If
\[
p\prec b,
\qquad
p\in\widetilde P,
\quad
b\in P^*,
\]
the facet inequality is
\[
c_p\le\lambda(b),
\]
again with unit normal.

Therefore a radius-\(\rho\) Euclidean ball centered at \(c\) lies in the marked order polytope exactly when
\[
c_q\ge\lambda(a)+\rho,
\tag{10}
\]
\[
c_q-c_p\ge\rho\sqrt2,
\tag{11}
\]
and
\[
c_p\le\lambda(b)-\rho
\tag{12}
\]
for all covers of the corresponding types.

Now let
\[
C:\quad
a=p_0\prec p_1\prec\cdots\prec p_k=b
\]
be a marked interval chain. Summing the shifted inequalities along \(C\) gives
\[
\lambda(b)-\lambda(a)
\ge
\rho\left(2+(k-2)\sqrt2\right)
=
\rho W(C).
\tag{13}
\]
Hence every feasible radius satisfies
\[
\rho
\le
\frac{\lambda(b)-\lambda(a)}{W(C)}.
\]
Taking the minimum proves the upper bound in (3).

For the converse, fix \(\rho\) satisfying every marked-chain bound. Direct every cover edge upward and assign it the length
\[
w(p,q)=
\begin{cases}
1,&\text{if exactly one endpoint is marked},\\
\sqrt2,&\text{if both endpoints are unmarked}.
\end{cases}
\tag{14}
\]

For an unmarked element \(p\), set
\[
x_p
=
\max
\left\{
\lambda(a)+\rho\,W(\gamma):
\gamma\text{ is a directed saturated path from marked }a\text{ to }p
\right\}.
\tag{15}
\]
Because every minimal element is marked, the maximum is over a nonempty finite set.

If \(p\prec q\) are both unmarked, appending that edge to any path ending at \(p\) gives
\[
x_q\ge x_p+\rho\sqrt2.
\]
If \(a\prec q\) with \(a\) marked, the one-edge path gives
\[
x_q\ge\lambda(a)+\rho.
\]

Finally, let
\[
p\prec b
\]
with \(b\) marked. Any path realizing \(x_p\), followed by the edge \(p\prec b\), is a marked-to-marked path. If it contains intermediate marked elements, split it at those elements. Each segment is a marked interval chain, and the assumed chain bounds add to give the bound for the whole path. Thus
\[
x_p+\rho\le\lambda(b).
\]
So \(x=(x_p)\) satisfies every shifted facet inequality. Hence radius \(\rho\) is feasible. Taking \(\rho\) equal to the minimum in (3) proves equality.

At the optimal radius, equations (10)--(12) are exactly the condition for a center to support a radius-\(r\) ball, so they give the complete center set (4).

If \(C\) attains the minimum in (3), then the sum of the nonnegative facet slacks along \(C\) is
\[
\lambda(b)-\lambda(a)-rW(C)=0.
\]
Every summand must therefore vanish. Hence every facet along a minimizing marked chain is tangent at every incenter.

Formula (15) is exactly \(L_p\), so \(L\) is an incenter. The dual construction, taking minimum backward marked-path bounds, gives \(U\). Every feasible center is bounded below by every forward path and above by every backward path, which proves (8). Since both \(L\) and \(U\) are feasible, uniqueness is equivalent to coordinatewise equality, proving (9).

## Verification
The proof is symbolic for every finite regular bounded marked poset.

The source-dependent facts were checked in the primary full text: marked order polytopes are the order-preserving extensions of a marking; marking every extremal element makes the polyhedron bounded; and, for regular marked posets, cover relations are exactly the facets. The source also proves the structural properties of regular marked posets used above.

A later full paper on a continuous family of marked poset polytopes was inspected because it revisits the same regularization and facet theory and contains marked order polytopes as an endpoint of its family. Its main results concern transfer maps, Ehrhart equivalence, degenerations, tropical subdivisions, vertices, and facet counts; it does not state an inradius or Chebyshev-center theorem.

The accompanying `verify.py` independently checks deterministic regular marked posets with nonuniform markings. For each case it enumerates all marked interval chains to obtain (3), then separately solves the full Chebyshev linear program by active-set enumeration over the actual cover facets. It also verifies the canonical lower and upper centers. The finite replay is corroborative only.

## Relationship to prior work
Pegel's paper develops the face structure of marked order polyhedra and corrects the regularity condition needed for cover relations to correspond exactly to facets. It also studies recession cones, products, Minkowski decompositions, and lattice properties.

Fang, Fourier, Litza, and Pegel later place marked order polytopes inside a continuous family connecting marked order and marked chain polytopes. Their treatment emphasizes transfer maps, Ehrhart equivalence, degenerations, tropical subdivisions, and the Hibi--Li facet comparison.

Neither inspected full text contains an inradius or Chebyshev-center theorem.

The formula is not merely the ordinary order-polytope height formula with renamed parameters. Different marked intervals can have different gaps
\[
\lambda(b)-\lambda(a),
\]
so a short chain with a small marking gap can dominate a much longer chain with a large gap. The exact invariant is therefore a weighted bottleneck over marked intervals, not a single global height.

Likewise, known marked-order/flow-polytope correspondences are generally affine rather than Euclidean-isometric, so they do not transfer the radius.

Targeted published-result searches under “marked order polytope”, “Gelfand--Tsetlin polytope”, “inradius”, “Chebyshev center”, “largest inscribed ball”, and “saturated chain” did not locate a statement implying (3)--(9).

## Limitations
The theorem is stated for regular marked posets in the standard projected realization.

A nonregular marked presentation can contain redundant cover inequalities; using their hyperplanes as if they were facets would give incorrect Euclidean clearances. The source gives a procedure for obtaining a regular presentation defining the same polyhedron, but the theorem here is deliberately stated only once the actual facet presentation is regular.

The result determines the Euclidean inradius, every incenter, canonical extremal centers, and forced tangent chains. It does not determine minimum enclosing spheres or extremal ellipsoids.

Generic longest-path feasibility for systems of difference inequalities is an underlying proof mechanism. The mathematical content specific to marked order polytopes is the exact Euclidean edge weighting \(1,\sqrt2,1\), the marked-chain bottleneck formula, and its all-center/tangency consequences.

## References
1. Christoph Pegel, *The Face Structure and Geometry of Marked Order Polyhedra*, arXiv:1610.01393, first public version 2016-10-05; *Order* 35 (2018), 467--488, DOI 10.1007/s11083-017-9443-2.
2. Xin Fang, Ghislain Fourier, Jan-Philipp Litza, and Christoph Pegel, *A Continuous Family of Marked Poset Polytopes*, arXiv:1712.01037, first public version 2017-12-04; *SIAM Journal on Discrete Mathematics* 34 (2020), 611--639, DOI 10.1137/18M1228529.
