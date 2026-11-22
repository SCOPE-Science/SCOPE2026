# Exact four-dimensional similarity-containment volume for all right-triangle targets

## Finding
Let \(T=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\) and \(Q_{a,b}=\operatorname{conv}\{(0,0),(a,0),(0,b)\}\), where \(a,b>0\). Let \(\mathcal C_{a,b}\subset\mathbb R^4\) be the collection of all \((u,v,p,q)\) such that the orientation-preserving similarity
\[
(x,y)\longmapsto(ux-vy+p,\;vx+uy+q)
\]
sends \(T\) into \(Q_{a,b}\). The zero-scale transformations are included and have zero four-dimensional measure. Put \(m=\min(a,b)\) and \(M=\max(a,b)\). Then the exact ordinary Lebesgue four-volume is
\[
\boxed{\operatorname{vol}_4(\mathcal C_{a,b})=
\frac{m^3M\bigl(-3m^3+10m^2M-3mM^2+12M^3\bigr)}{48(m+M)(m^2+M^2)}.}
\]
For fixed area \(\operatorname{area}(Q_{a,b})=ab/2\), this volume is uniquely maximal at the isosceles target:
\[
\operatorname{vol}_4(\mathcal C_{a,b})\le\frac{(ab)^2}{12},
\qquad\text{with equality iff }a=b.
\]
The projection \(F_{a,b}\) onto the two multiplier coordinates \((u,v)\) is an octagon when \(a\ne b\), but a pentagon when \(a=b\). In particular, at fixed \(b=1\), the volume as a function of \(a>0\) is twice continuously differentiable across \(a=1\), but its third derivative has the explicit jump
\[
\boxed{V^{(3)}(1^+)-V^{(3)}(1^-)=\frac5{32}},
\qquad V(a)=\operatorname{vol}_4(\mathcal C_{a,1}).
\]

## Assumptions and scope
The parameter-space measure is ordinary \(du\,dv\,dp\,dq\), not Haar measure on the similarity group. Scaling by \(\sqrt{u^2+v^2}\) and rotation are encoded in the linear pair \((u,v)\). Both source and target triangles are closed; both leg lengths are positive. Reversing orientation is excluded. Scaling symmetry shows that the volume is homogeneous of degree four in \((a,b)\); symmetry under swapping the two target legs follows from simultaneous coordinate reflection of source and target, which conjugates rotation to rotation with its angle negated and preserves parameter-space volume.

## Proof
**1. Exact translation fibers.** For a multiplier \(z=(u,v)\), the transformed source vertices before translation are
\[
(X_0,Y_0)=(0,0),\quad(X_1,Y_1)=(u,v),\quad(X_2,Y_2)=(-v,u).
\]
Their images lie in \(Q_{a,b}\) exactly when, for \(j=0,1,2\),
\[
p+X_j\ge0,\qquad q+Y_j\ge0,\qquad
\frac{p+X_j}{a}+\frac{q+Y_j}{b}\le1.
\]
Define the positively homogeneous convex function
\[
W_{a,b}(z)=\max_j\left(\frac{X_j}{a}+\frac{Y_j}{b}\right)
-\frac{\min_jX_j}{a}-\frac{\min_jY_j}{b}.
\]
At fixed \(z\), the translation coordinates form a translated copy of \((1-W_{a,b}(z))Q_{a,b}\) if \(W_{a,b}(z)\le1\), otherwise they form the empty set. Consequently their area equals \(ab(1-W_{a,b}(z))^2/2\) on the footprint \(F_{a,b}=\{z:W_{a,b}(z)\le1\}\). Since the footprint is a bounded convex neighborhood of the origin and \(W_{a,b}\) is its gauge, its sublevel areas scale as \(r^2\operatorname{area}(F_{a,b})\). Layer integration gives
\[
\operatorname{vol}_4(\mathcal C_{a,b})=\frac{ab}{2}
\int_{F_{a,b}}(1-W_{a,b})^2\,dz
=\frac{ab}{12}\operatorname{area}(F_{a,b}).
\]
The gauge-integral identity in the special case of *self*-containment has appeared previously; the calculation is included here to fix normalization for two different triangles.

**2. A complete finite polar certificate.** It suffices by the symmetry and scaling above to put \(a=t,b=1\), with \(0<t\le1\). Write \(X_j(z)=\langle x_j,z\rangle\), \(Y_j(z)=\langle y_j,z\rangle\), where
\[
x_0=y_0=(0,0),\quad x_1=(1,0),\ y_1=(0,1),\quad x_2=(0,-1),\ y_2=(1,0).
\]
Then
\[
W_{t,1}(z)=\max_{i,j,k\in\{0,1,2\}}\left\langle
\frac{x_j-x_i}{t}+y_j-y_k,z\right\rangle.
\]
Thus the polar of \(F_{t,1}\) is the convex hull of these 27 explicitly stated rational normal vectors. For \(0<t<1\), its eight consecutive vertices are
\[
\begin{aligned}
N_0&=(-\frac{1+t}{t},0),&N_1&=(-\frac1t,-\frac1t),\\
N_2&=(\frac{t-1}{t},-\frac{1+t}{t}),&N_3&=(1,-\frac{1+t}{t}),\\
N_4&=(\frac1t,0),&N_5&=(\frac1t,\frac{1+t}{t}),\\
N_6&=(\frac{1-t}{t},\frac{1+t}{t}),&N_7&=(-1,\frac1t).
\end{aligned}
\]
This list is an *exhaustive symbolic certificate*, not a drawing or a finite parameter sample: (i) substitution in the displayed 27-vector formula shows that each \(N_i\) belongs to the list; (ii) for every oriented edge \(N_iN_{i+1}\) (indices cyclic) and each of the 27 vectors \(w\), one has
\[
\det(N_{i+1}-N_i,w-N_i)\ge0\qquad(0<t<1).
\]
To verify all 216 inequalities without numerical approximation, multiply every determinant by \(t^2\). Each resulting polynomial has degree at most two, and **all of its Bernstein coefficients on \([0,1]\) are nonnegative**; the exhaustive symbolic verifier supplies and checks this finite certificate. Consecutive normal vectors are distinct and consecutive turns are strictly positive for \(0<t<1\). These facts prove that the eight vectors, and no others, are the polar vertices. The primal footprint has the eight cyclic vertices obtained by intersecting the successive supporting lines \(\langle N_i,z\rangle=1\):
\[
\begin{aligned}
P_0&=(-\frac{t}{1+t},-\frac{t^2}{1+t}),&
P_1&=(-\frac t2,-\frac t2),\\
P_2&=(0,-\frac{t}{1+t}),&
P_3&=(t,\frac{t(t-1)}{1+t}),\\
P_4&=(t,0),&
P_5&=(0,\frac{t}{1+t}),\\
P_6&=(-\frac{t^2}{1+t^2},\frac{t}{1+t^2}),&
P_7&=(-\frac{t}{1+t},\frac{t}{1+t}).
\end{aligned}
\]
Their shoelace area simplifies exactly to
\[
\boxed{f(t)=\operatorname{area}(F_{t,1})=
\frac{t^2(-3t^3+10t^2-3t+12)}{4(1+t)(1+t^2)}}.
\]
At \(t=1\), the list contracts to five distinct vertices
\((1,0),(0,1/2),(-1/2,1/2),(-1/2,-1/2),(0,-1/2)\), forming a pentagon of area one. Continuity of the footprint supplies its area from \(f(1)\); its complete vertex list follows directly by intersecting the 27 inequalities at \(t=1\).

**3. Four-volume formula and optimal shape.** The fiber formula gives \(V(t,1)=tf(t)/12\), and homogeneity and leg symmetry yield the asserted rational function of \(m,M\). At fixed \(ab\),
\[
\frac{\operatorname{vol}_4(\mathcal C_{a,b})}{(ab)^2/12}
=\frac{f(t)}{t},\qquad t=m/M.
\]
Direct differentiation gives the strictly positive derivative for \(0<t<1\):
\[
\frac{d}{dt}\frac{f(t)}t=
\frac{(1-t)(3t^5+9t^4+5t^3+21t^2+6t+12)}{4(1+t)^2(1+t^2)^2}>0.
\]
As \(f(1)=1\), the fixed-area maximum is unique.

**4. Smoothness transition.** At \(b=1\), the footprint area is \(f(a)\) on \(0<a\le1\), and \(a^2f(1/a)\) for \(a\ge1\). Their values and their first and second derivatives match at one, while their third derivatives differ by \(15/8\). Multiplying by the fiber factor \(a/12\) proves \(V^{(3)}(1^+)-V^{(3)}(1^-)=5/32\) and shows failure of \(C^3\) regularity.

## Verification
The accompanying `verify.py` is an executable algebraic checker. It creates all 27 normal vectors, proves the eight claimed polar vertices belong to them, checks all 216 edge-support inequalities by **exact** nonnegative Bernstein-basis coefficients, constructs the eight primal vertices, verifies the shoelace formula and differentiation identities, and separately enumerates the original nine halfspace intersections in four variables for several rational leg pairs. The symbolic certificate verifies the continuum \(0<t<1\), rather than extrapolating from samples. Numerical four-dimensional hull volumes, where computed, are supplementary only.

## Relationship to prior work
Choi and Choi (2026) define the same four-dimensional containment polytope for arbitrary triangle–polygon pairs and study its silhouette complexity and largest placements, not this exact all-aspect volume and footprint transition. The publicly available 2026 note *A sharp equilateral extremum and a universal beta law for triangle self-containment polytopes* proves a general gauge-fiber identity **only when source and target are the same triangle**, and the special isosceles self-case and its gauge arguments are credited. Its conclusion does not imply the asymmetric-target formula: anisotropic coordinate dilation converts the target to an isosceles triangle but does not preserve the orientation-preserving similarity multiplier plane, so it does not reduce distinct triangle containment to self-containment. The independent rectangle containment formulas for a right-isosceles source concern three-/four-facet targets, not the three-facet target here. The new contribution is the full right-triangle target volume rational function, all-aspect planar-footprint classification, unique fixed-area extremizer and exact differentiability transition.

## Limitations
This proves the stated result for one fixed right-isosceles source and all right-triangle targets; arbitrary source triangles or nontriangular targets are not covered. The full four-polytope face lattice is not claimed classified. The polar vertex certificate is an elementary but extensive exact computation supplied by the checker. Historical priority against all unindexed literature is not certified; the older 1998 containment work was compared using accessible descriptions, not fully inspected text. Independent mathematical review has not been performed.

## References
- Y. Choi and S. Choi, *The Containment Polytope of a Triangle and a Convex Polygon*, arXiv:2611.08556v1, first publicly posted 2026-11-05, https://arxiv.org/html/2611.08556v1.
- *A sharp equilateral extremum and a universal beta law for triangle self-containment polytopes*, public mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-sharp-equilateral-extremum-and-a-universal-beta-law-for-triang--0f26f49ae237.
- P. K. Agarwal, N. Amenta and M. Sharir, *Largest Placement of One Convex Polygon Inside Another*, Discrete & Computational Geometry 19 (1998), https://doi.org/10.1007/PL00009337.
- T. M. Chan and E. Hair, *Convex Polygon Containment: Improving Quadratic to Near Linear Time*, SoCG (2024), https://doi.org/10.4230/LIPIcs.SoCG.2024.34.
