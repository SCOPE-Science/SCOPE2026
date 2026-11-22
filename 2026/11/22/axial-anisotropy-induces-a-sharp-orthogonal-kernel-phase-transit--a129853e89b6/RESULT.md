# Axial anisotropy induces a sharp orthogonal-kernel phase transition in octahedra

## Finding

For every real \(t>0\), let
\[
P_t=\operatorname{conv}\{(\pm t,0,0),(0,\pm1,0),(0,0,\pm1)\}\subset\mathbb R^3,
\qquad s=t^{-2}.
\]
Its **orthogonal kernel** \(K_t\) is the set of interior points \(x\) whose Euclidean orthogonal projection onto the affine span of **each nonempty face** of \(P_t\) belongs to that face's relative interior. Set \(u=|x_1|/t\), \(v=|x_2|\), and \(w=|x_3|\). Then, exactly,
\[
K_t=\bigl\{x:\; (2/s)u+v+w<1,\quad
u+(1+s)v+w<1,\quad u+v+(1+s)w<1\bigr\}.
\]
The closure \(\overline{K_t}\) has the full face vector \((f_0,f_1,f_2)=(26,48,24)\) and all quadrilateral facets when \(0<s<2\), but \((f_0,f_1,f_2)=(10,24,16)\) and all triangular facets when \(s\ge2\). Hence the transition occurs at exactly \(t=1/\sqrt2\), including this endpoint in the latter phase.

Writing \(R(s)=\operatorname{vol}_3(K_t)/\operatorname{vol}_3(P_t)\), its exact piecewise rational law is
\[
\boxed{
R(s)=\begin{cases}
\displaystyle\frac{s(s^3-5s^2+6s+4)}{4(s+1)(s+2)},&0<s\le2,\\[6pt]
\displaystyle\frac{2}{(s+1)(s+2)},&s\ge2.
\end{cases}}
\]
The formulas agree at \(s=2\). The sharp inequality \(R(s)\le1/4\) holds for all \(s>0\), with equality **only** for the regular octahedron \(t=1\). More precisely,
\[
\frac14-R(s)=\begin{cases}
\displaystyle\frac{(s-1)^2(2+3s-s^2)}{4(s+1)(s+2)},&0<s\le2,\\[6pt]
\displaystyle\frac{s^2+3s-6}{4(s+1)(s+2)},&s\ge2.
\end{cases}
\]
The volume ratio is twice continuously differentiable, but not three times continuously differentiable, at \(s=2\): \(R'''(2^-)-R'''(2^+)=3/8\).

## Assumptions and scope

All projections use the usual ambient Euclidean inner product, not a metric pulled back by the anisotropic linear transformation. The parameter \(t\) is strictly positive and arbitrary, and \(K_t\) is open by the relative-interior convention. The stated vertices, edges and facets belong to its closure. Lebesgue volume is normalized by the volume of the *same* octahedron \(P_t\), whose volume is \(4t/3\). The source problem's orthogonal-kernel definition is used literally; neither arbitrary triaxial octahedra nor higher dimensions are covered by the volume formula.

## Proof

**1. All-face condition.** Consider the more general orthogonal cross-polytope \(P=\operatorname{conv}\{\pm a_i e_i:1\le i\le3\}\) with all \(a_i>0\). Each proper nonempty face consists of a choice of nonempty index set \(I\subseteq\{1,2,3\}\), a sign \(\varepsilon_i\in\{\pm1\}\) for each \(i\in I\), and the conditions \(y_j=0\) outside \(I\), \(\sum_{i\in I}\varepsilon_i y_i/a_i=1\), \(\varepsilon_i y_i\ge0\) inside \(I\). Vertices, for which \(|I|=1\), impose no nontrivial relative-interior condition.

For \(|I|\ge2\), write \(H_I=\sum_{i\in I}a_i^{-2}\). Orthogonal projection of a point \(x\) onto the affine span of this face has, for \(i\in I\), coordinates
\[
y_i=x_i+\frac{\varepsilon_i}{a_i H_I}\left(1-\sum_{j\in I}\frac{\varepsilon_j x_j}{a_j}\right),
\]
and zero coordinates outside \(I\). Positivity of every signed coordinate \(\varepsilon_i y_i\) is equivalent to
\[
1+a_i\varepsilon_i x_i\sum_{j\in I\setminus\{i\}}a_j^{-2}
-\sum_{j\in I\setminus\{i\}}\frac{\varepsilon_j x_j}{a_j}>0.
\]
Minimizing over all permitted face signs independently yields the necessary and sufficient condition
\[
\sum_{j\in I\setminus\{i\}}\left(\frac{|x_j|}{a_j}+\frac{a_i|x_i|}{a_j^2}\right)<1
\quad\text{for every }i\in I.
\]
All summands are nonnegative, so the three full-index-set, facet conditions dominate all edge conditions. They also force \(\sum_i|x_i|/a_i<1\), establishing the required interior membership. Specializing \((a_1,a_2,a_3)=(t,1,1)\) gives the three claimed inequalities for \((u,v,w)\).

**2. The combinatorial transition.** In a fixed coordinate octant, the closure is the first-octant polytope in \((u,v,w)\) cut out by
\[
u,v,w\ge0,\quad (2/s)u+v+w\le1,\quad
u+(1+s)v+w\le1,\quad u+v+(1+s)w\le1.
\]
For \(0<s<2\), its nonzero vertices are the following seven points:
\[
\begin{array}{c|c}
U&(s/2,0,0)\\
V&(0,1/(1+s),0)\\
W&(0,0,1/(1+s))\\
UV&(s^2/(s+2),(2-s)/(s+2),0)\\
UW&(s^2/(s+2),0,(2-s)/(s+2))\\
VW&(0,1/(s+2),1/(s+2))\\
T&(s^2/4,(2-s)/4,(2-s)/4).
\end{array}
\]
The three noncoordinate supporting faces in this octant are the quadrilaterals \((U,UV,T,UW)\), \((V,VW,T,UV)\), and \((W,UW,T,VW)\). Their sign reflections yield \(8+8+8=24\) distinct global quadrilateral facets. Reflections of the seven positive-octant vertices, with coordinates zero identified, yield \(6\) axial, \(12\) two-coordinate and \(8\) three-coordinate vertices, hence \(26\) vertices. Euler's polyhedron relation gives \(48\) edges.

For \(s\ge2\), the first inequality is redundant: \(2/s\le1\), so it is implied by each of the other two. The only nonzero first-octant vertices are
\[
U=(1,0,0),\quad V=(0,1/(1+s),0),\quad W=(0,0,1/(1+s)),\quad VW=(0,1/(s+2),1/(s+2)).
\]
The two noncoordinate faces are triangles \((U,V,VW)\) and \((U,VW,W)\). The sign reflections yield \(16\) triangular facets and \(2+4+4=10\) distinct vertices, hence \(24\) edges. These lists are obtained by intersecting the displayed planes and coordinate planes; they exhaust the polytope because every bounded polyhedron vertex must be such a plane intersection. Positivity and the strict inequalities \(0<s<2\) verify that the indicated supports are nondegenerate.

**3. Exact volume.** Let \(V_+(s)\) be the volume of the above first-octant polytope in \((u,v,w)\)-space. For \(0<s<2\), triangulate the three quadrilateral external faces by diagonals \(U T\), \(V T\), \(W T\) and cone each of the six triangles to the origin. Summing their determinant volumes gives
\[
V_+(s)=\frac{s(s^3-5s^2+6s+4)}{24(s+1)(s+2)}.
\]
For \(s\ge2\), the two external triangles \((U,V,VW)\) and \((U,VW,W)\), again coned to the origin, give
\[
V_+(s)=\frac{1}{3(s+1)(s+2)}.
\]
Restoring all eight octants and the Jacobian \(t\) of \((u,v,w)\mapsto(x_1,x_2,x_3)=(tu,v,w)\) yields \(\operatorname{vol}_3(K_t)=8t V_+(s)\). Since \(\operatorname{vol}_3(P_t)=4t/3\), the ratio is exactly \(R(s)=6V_+(s)\), as stated. The boundary has zero volume.

**4. Sharp rigidity and smoothness.** Subtracting the two rational branches from \(1/4\) and factoring yields the displayed deficit. For \(0<s\le2\), the factor \(2+3s-s^2\) is strictly positive; for \(s\ge2\), \(s^2+3s-6\) is strictly positive. Consequently equality occurs iff \(s=1\), or \(t=1\), with exact quadratic local deficit \(1/4-R(s)=(s-1)^2/6+O((s-1)^3)\).

Finally, extending the second branch analytically to \(s<2\), the exact difference is
\[
R(s)-\frac{2}{(s+1)(s+2)}=\frac{(s-2)^3}{4(s+2)}\qquad(0<s\le2).
\]
It vanishes to order three at \(s=2\), establishing continuity of the first two derivatives and the nonzero third-derivative jump \(3/8\).

## Verification

The standalone `verify.py` uses only Python's standard library and exact fractions. It checks the independent signed-halfspace and vertex descriptions, the facet counts, determinant-volume identities, and the sharp-deficit factorizations at \(16\) rational shape parameters on both sides of the phase boundary and at the boundary. It additionally compares the face-by-face orthogonal-foot criterion against the three kernel inequalities for \(1725\) exactly rational interior test points at three physical aspect ratios. These are reproducibility diagnostics; the proof above, not the finite tests, proves the statements for all real \(t>0\). Run with `python3 verify.py`.

## Relationship to prior work

Pavlík's *Thales's theorem in higher dimensions* (2026) supplies the orthogonal-kernel definition and proves an orthogonal-cutout tiling equivalence in dimension three, but does not state the three-dimensional axis-stretched octahedral phase diagram, normalized volume law, or sharp optimizing aspect ratio. The companion paper on bipolar polytopes supplies the broader combinatorial framework but its accessible abstract does not resolve these Euclidean metric computations. Nasonov, Panina and Siersma (2024) develop concurrent normals and face active regions, but not this all-face orthogonal-kernel volume classification.

The previously reported result *The regular octahedron's full-normal locus has one-quarter volume* gives precisely the \(t=1\) shape and the fraction \(1/4\). Its full result was inspected. The present result does **not** claim those known special-case facts as original; it proves the previously absent aspect-ratio classification, combinatorial collapse at \(t=1/\sqrt2\), piecewise volume, and sharp rigidity. Normal-cone activity and orthogonal feet are distinct notions in general and are not silently identified away from the regular case.

## Limitations

The exact volume and combinatorial classification cover only the one-axis stretched family, not arbitrary three-axis stretches, general cross-polytopes or higher dimensions. No universal upper bound on orthogonal-kernel fraction for all convex polytopes is claimed. The literature comparison includes full text of the motivating paper, a concurrent-normals paper and the closest published regular-octahedron result, but not the complete companion-paper text; historical priority against other terminology remains a residual risk. An independent mathematical audit has not been performed.

## References

1. J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1 (first public 2026-11-10 UTC), especially Section 6. https://arxiv.org/html/2611.14277v1
2. J. Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1 (first public 2026-11-10 UTC). https://arxiv.org/abs/2611.13896
3. I. Nasonov, G. Panina and D. Siersma, *Concurrent normals problem for convex polytopes and Euclidean distance degree*, arXiv:2406.01773v1 (first public 2024-06-03 UTC). https://arxiv.org/html/2406.01773v1
4. *The regular octahedron's full-normal locus has one-quarter volume*, public mathematical record (2026-10-25 UTC), full RESULT.md consulted. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-regular-octahedron-s-full-normal-locus-has-one-quarter-volum--596428720a97
