# Exact independent exit clocks and three-channel phase transitions at a planar repelling focus

## Finding

Let \(a,b\in\mathbb R\) obey \(b>2a\) and \(a+2b>0\), and consider the continuous piecewise-affine map
\[
 F_{a,b}(x,y)=(|x|-y+a,\ x-|y|+b).
\]
Write \(Q_2=\{x<0<y\}\), and define its consecutive-visit survivor sets and first-exit time by
\[
 S_n=\{z:F_{a,b}^{j}(z)\in Q_2\text{ for }0\le j<n\},\quad
 \tau(z)=\min\{j\ge0:F_{a,b}^j(z)\notin Q_2\}.
\]
Put \(\alpha=(b-2a)/5>0\), \(\beta=(a+2b)/5>0\), and \(t=\beta/\alpha>0\). The unique fixed point in \(Q_2\) is \(q=(-\alpha,\beta)\). Define the following nonnegative piecewise-polynomial functions:
\[
 c(t)=\begin{cases}25t^2/8&0<t\le1/3,\\(-2t^2+18t-3)/8&1/3<t<2,\\25/8&t\ge2,\end{cases}
\]
\[
 d(t)=\begin{cases}25t^2/16&0<t\le1/3,\\(2-t)(11t-2)/16&1/3<t<2,\\0&t\ge2,\end{cases}
\qquad
 h(t)=\begin{cases}0&0<t\le1/3,\\(3t-1)^2/16&1/3<t\le3/4,\\(2-t)(7t-4)/16&3/4<t<2,\\0&t\ge2.\end{cases}
\]
Set \(e_1=c/2-d\), \(e_3=d-h\), \(e_4=h\). For every integer \(n\ge3\),
\[
 \operatorname{area}(S_n)=\alpha^2c(t)2^{-(n-3)}.
\]
If \(Z\) is distributed uniformly with respect to two-dimensional Lebesgue area on the bounded nonempty set \(S_3\), and \(J\) is the quadrant of \(F_{a,b}^{\tau(Z)}(Z)\), then for every integer \(k\ge0\) and each \(j\in\{1,3,4\}\),
\[
 \boxed{\Pr(\tau(Z)=3+k,\ J=Q_j)=2^{-k}\frac{e_j(t)}{c(t)}.}
\]
Zero-coordinate exit points have area probability zero. In particular \(\tau\) and \(J\) are independent, \(\Pr(\tau=3+k)=2^{-k-1}\), and \(\Pr(J=Q_j)=2e_j/c\). The first-exit destination changes sharply with the ratio \(t\): for \(0<t\le1/3\) the exit is always to \(Q_3\), for \(t\ge2\) always to \(Q_1\), and for \(1/3<t<2\) all three destination quadrants have strictly positive probability. An additional analytic branch transition occurs at \(t=3/4\) in the probability of exit to \(Q_4\).

## Assumptions and scope

The sampling law is **planar area conditional on the first three visits to the open second quadrant**, not a whole-plane invariant probability measure. The clock counts individual applications of the original planar map and ends at the first exit; later returns are not considered. No stationarity of the initial law is asserted. The fixed point is repelling in its quadrant because the local linear matrix has eigenvalues of modulus \(\sqrt2\). At non-strict equality boundaries the polygon formulas extend by continuity for area, while the dynamics uses open quadrant tests. All parameters in the stated open cone are allowed, including positive, zero, and negative \(a\).

## Proof

**1. Branch normalization.** The fixed point is \(q=(-\alpha,\beta)\). Write a point as \(q+\alpha(u,v)\). While an orbit stays in \(Q_2\), its displacement evolves by
\[
 A(u,v)=(-u-v,\ u-v),\qquad A^2(u,v)=(2v,-2u),\quad
 A^3(u,v)=(2u-2v,2u+2v).
\]
The quadrant is characterized by \(u<1\) and \(v>-t\). Thus the normalized polygon \(P_t=(S_3-q)/\alpha\) is precisely
\[
 \boxed{u<1,\quad v>-t,\quad u+v>-1,\quad v-u<t,\quad v<1/2,\quad u<t/2.}\tag{1}
\]
All six constraints arise from the first three actual iterate sign tests. The polygon is bounded, contains the origin in its interior, and has positive area.

**2. Exact inverse trapping.** The inverse branch is \(A^{-1}(u,v)=((-u+v)/2,(-u-v)/2)\). When \(t<2\), the inequalities \(u<t/2\), \(v-u<t\) imply the first coordinate of \(A^{-1}(u,v)\) is less than \(t/2<1\); also \(u+v<2u+t<2t\), hence its second coordinate exceeds \(-t\). When \(t\ge2\), the closure of \(P_t\) is the triangle with vertices \((1,-2)\), \((1,1/2)\), and \((-3/2,1/2)\). Its inverse vertices are \((-3/2,1/2)\), \((-1/4,-3/4)\), and \((1,1/2)\), all satisfying the non-strict quadrant bounds; the inverse of the open polygon satisfies them strictly. Therefore in every regime \(q+\alpha A^{-1}P_t\subset Q_2\). Invariance of the branch then proves, by induction, the exact set equality
\[
 S_{3+k}=q+\alpha A^{-k}P_t\qquad(k\ge0).\tag{2}
\]
As \(|\det A|=2\), equation (2) gives \(\operatorname{area}(S_{3+k})=\alpha^2\operatorname{area}(P_t)2^{-k}\). Since \(A^{-1}\) is a rotation and contraction of ratio \(1/\sqrt2\), the unique infinite-time survivor is the fixed point \(q\).

**3. Polygonal exit channels.** On a point in \(P_t\), after three visits the displacement is \(A^3(u,v)=(2u-2v,2u+2v)\). The exit to the right of the quadrant happens exactly if \(u-v\ge1/2\); exit below happens exactly if \(u+v\le-t/2\). Hence exit to \(Q_1\) means right but not below; to \(Q_3\) means below but not right; to \(Q_4\) means both. The remaining points make at least one more visit and form \(A^{-1}P_t\), of area \(\operatorname{area}(P_t)/2\).

For completeness, here is an exact shoelace computation of the areas. For \(0<t<1/3\), the closure of \(P_t\) has vertices \((t/2,3t/2),(-2t,-t),(t/2,-t)\). For \(1/3<t<2\), they are \((t/2,1/2),(1/2-t,1/2),(-(t+1)/2,(t-1)/2),(t-1,-t),(t/2,-t)\). For \(t\ge2\), they are the triangle stated in step 2. Their shoelace areas are the three respective branches of \(c(t)\). The polygon cut out by \(u+v\le-t/2\) has, for \(1/3<t<2\), vertices \((-3t/4,t/4),(-(t+1)/2,(t-1)/2),(t-1,-t),(t/2,-t)\), with area \((2-t)(11t-2)/16\); for \(0<t<1/3\), it is the triangle with vertices \((-3t/4,t/4),(-2t,-t),(t/2,-t)\), with area \(25t^2/16\); for \(t\ge2\), it is empty up to boundary. These yield \(d(t)\).

The polygon cut out by both exit conditions has, for \(1/3<t<3/4\), vertices \((1/2-t,-t),(t/2,-t),((1-t)/4,-(t+1)/4)\), with area \((3t-1)^2/16\). For \(3/4<t<2\), its vertices are \((-1/4,-3/4),(t-1,-t),(t/2,-t),((1-t)/4,-(t+1)/4)\), with area \((2-t)(7t-4)/16\). It is empty up to boundary for \(t\le1/3\) or \(t\ge2\). These yield \(h(t)\). At all endpoints the pieces agree by continuity. Since the total first-exit area in normalized coordinates is \(c/2\), the disjoint destination areas are exactly \(e_1=c/2-d\), \(e_3=d-h\), and \(e_4=h\), as asserted.

**4. Joint law and independence.** On \(S_{3+k}\), the first \(k\) iterates follow the same affine branch, and \(F_{a,b}^k\) sends normalized uniform area on \(S_{3+k}\) **exactly** to normalized uniform area on \(S_3\), because the branch Jacobian is the constant \(2^k\). The event of surviving \(k\) extra visits has conditional probability \(2^{-k}\). Among points with this survival, the normalized area of those exiting after another three iterates into \(Q_j\) is \(e_j/c\). Thus
\[
 \Pr(\tau=3+k,J=Q_j)=2^{-k}e_j/c.
\]
Summing over the three destinations gives \(2^{-k-1}\) because \(e_1+e_3+e_4=c/2\). Dividing proves the independence. The signs and explicit positivity of all branches establish the destination phase diagram. No finite sampling is used as an infinite-iterate proof.

## Verification

The standalone Python standard-library checker `check_exact.py` builds each polygon directly from the first \(n\) affine branch conditions by rational half-plane clipping (not from the stated formula). Across 94 exact rational parameter ratios, including the three transition ratios, it verifies the three area functions, destination decomposition, and exact inverse similarity through nine consecutive levels. It also tests the original absolute-value map on 54 original-coordinate rational branch cases. Run `python3 check_exact.py` from the package directory. Observed output: `THREE_CHANNEL_EXACT_RATIONAL_CHECK_OK cases=94 polygon_steps=9 original_branch_cases=54`. All infinite-parameter and infinite-iterate statements are established by the polygon and inverse-similarity arguments above, not by finite tests.

## Relationship to prior work

Cima, Gasull, Mañosa and Mañosas (2024), especially their fixed-point and invariant-graph analysis, establish the model and its qualitative dynamics. A prior exact three-visit survivor theorem for the negative-offset normalized slice \(a=-1\), \(b>1/2\), already establishes the area decay and geometric **time marginal**; those results are credited and not presented as independently new. The present claim resolves instead the **joint distribution of the clock and the destination quadrant** uniformly over the full two-parameter repelling-focus cone. In particular, its two absorbing destination regimes, the three-channel interior phase, and the internal \(t=3/4\) channel transition are not implications of the scalar area decay or the known time marginal. A separate positive-offset result calculates arclength phase selection on a one-dimensional image section, rather than planar area and exit destination from \(Q_2\). Another prior survivor computation studies a repelling three-cycle under a prescribed three-quadrant itinerary, not the single-quadrant fixed-point exit channels. The later original-authors' entropy paper concerns graph-supported dynamics and does not determine the present planar exit law. General exact polygon-clipping methods may be related, but no general result inspected gives these destination probabilities.

## Limitations

These are conditional transient laws for uniform planar initial area on \(S_3\), not the full-plane long-term basin proportions or an invariant measure. The model is restricted to \(b>2a\) and \(a+2b>0\) so that its second-quadrant fixed point exists. The first-exit quadrant is a coarser observable than the complete outgoing point distribution. Singular quadrant-boundary exits are excluded by the area-zero convention. Precise priority relative to unidentified published calculations remains to be assessed independently. No external independent mathematical audit has been performed.

## References

1. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052v1, publicly submitted 2024-10-01, particularly the quadrant fixed-point classification and invariant-graph descriptions. https://arxiv.org/abs/2410.01052
2. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Further results for a family of continuous piecewise linear planar maps* (later version titled *Entropy and \(\omega\)-limit sets on invariant graphs for a class of planar piecewise linear maps*), arXiv:2503.02411v1, publicly submitted 2025-03-04. https://arxiv.org/abs/2503.02411
3. *Sharp three-visit onset and geometric escape from a repelling quadrant focus*, public mathematical record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-three-visit-onset-and-geometric-escape-from-a-repelling-qu--6aab6efd2c66
4. *Universal geometric capture and phase bias on a polygonal section of an absolute-value planar map*, public mathematical record, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-universal-geometric-capture-and-phase-bias-on-a-polygonal-sectio--28e9aa5876f3
5. *Exact survival-area phase transitions near a repelling three-cycle*, public mathematical record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-survival-area-phase-transitions-near-a-repelling-three-cyc--b99c0542d5f5
