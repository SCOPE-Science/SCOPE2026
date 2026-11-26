# A complete joint width law for an aligned cube and octahedron

## Finding
Let \(Q=[-1,1]^3\) and \(O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\) be polar, axis-aligned solids in Euclidean three-space. Select one direction \(U\) uniformly on the unit sphere and measure *both* directional widths in that same direction. Write their half-widths as
\[
S=\tfrac12w_Q(U)=|U_1|+|U_2|+|U_3|,
\qquad
M=\tfrac12w_O(U)=\max_{i=1,2,3}|U_i|.
\]
For \(1/\sqrt3\le m\le1\), put
\[
q(m)=\sqrt{2(1-m^2)},\quad s_+(m)=m+q(m),
\]
\[
s_-(m)=\begin{cases}
2m+\sqrt{1-2m^2},&1/\sqrt3\le m\le1/\sqrt2,\\
m+\sqrt{1-m^2},&1/\sqrt2\le m\le1.
\end{cases}
\]
Then the complete joint law is absolutely continuous, with density
\[
\boxed{f_{M,S}(m,s)=\frac{12}{\pi\sqrt{2(1-m^2)-(s-m)^2}}}
\]
when \(1/\sqrt3<m<1\) and \(s_-(m)<s<s_+(m)\), and density zero outside the closure of that region. There is no boundary atom.

A conditional representation makes the dependence explicit. For \(1/\sqrt3<m<1\), let
\[
\alpha(m)=\arcsin\frac{s_-(m)-m}{q(m)}.
\]
The marginal density of \(M\) and conditional quantiles of \(S\) are
\[
\boxed{f_M(m)=\frac{12}{\pi}\left(\frac\pi2-\alpha(m)\right)},\qquad
\boxed{Q_{S\mid M=m}(p)=m+q(m)\sin\left(\alpha(m)+p\left[\frac\pi2-\alpha(m)\right]\right)}
\]
for \(0\le p\le1\). Equivalently, conditional on \(M=m\), the random variable \(S\) has the same law as \(m+q(m)\sin T_m\), where \(T_m\) is uniform on \([\alpha(m),\pi/2]\). Above the sharp threshold \(m=1/\sqrt2\), **the conditional angular law becomes independent of \(m\)**: \(T_m\) is exactly uniform on \([\pi/4,\pi/2]\) and \(f_M(m)=3\). Below the threshold, the admissible lower endpoint instead comes from two equal largest absolute coordinates.

## Assumptions and scope
The width is the distance between two opposite supporting planes, not a center-passing chord or an area of a planar shadow. For a convex body \(K\), \(w_K(u)=h_K(u)+h_K(-u)\). The same Haar-uniform direction is reused for both solids; independently chosen directions would produce a product of marginals and an entirely different problem. Cube and octahedron share their coordinate axes and are polar under the displayed scale normalization. The open-support density determines the distribution uniquely because its complement on the support has zero spherical measure.

## Proof
**1. Exact support.** Write the descending rearrangement of the three absolute coordinates of \(U\) as \(a\ge b\ge c\ge0\), so \(a^2+b^2+c^2=1\), \(M=a\), and \(S=a+b+c\). By normalization, \(1/\sqrt3\le a\le1\). At fixed \(a=m\), the remaining pair satisfies \(b^2+c^2=1-m^2\), \(0\le c\le b\le m\). The sum \(b+c\) is maximized at \(b=c\), giving \(s_+(m)=m+\sqrt{2(1-m^2)}\). Its minimum is attained at an endpoint of the permitted circular arc. For \(m<1/\sqrt2\), the endpoint \(c=0\) is prohibited and the minimum occurs at \(b=m\), giving \(2m+\sqrt{1-2m^2}\). For \(m\ge1/\sqrt2\), the endpoint \(c=0\) is possible and gives \(m+\sqrt{1-m^2}\). Thus the displayed support is necessary and sufficient. Endpoint cases have zero probability.

**2. Spherical Jacobian and multiplicities.** On the positive ordered sector, set \(a=m\), \(b=b\), \(c=\sqrt{1-m^2-b^2}\). The surface-area element on the unit sphere is \(dm\,db/c\). Outside lower-dimensional coordinate and tie sets, the 8 sign patterns and 6 coordinate permutations have identical area: all 48 sectors contribute. After division by the total sphere area \(4\pi\), the probability measure on one ordered sector is \((12/\pi)dm\,db/c\).

Set \(t=s-m=b+c\) and \(D=\sqrt{2(1-m^2)-t^2}=b-c\). The unique ordered inverse is \(b=(t+D)/2\), \(c=(t-D)/2\). Differentiation at fixed \(m\) gives \(|\partial b/\partial s|=c/D\), and hence
\[
\frac{12}{\pi}\frac{dm\,db}{c}
=\frac{12}{\pi D}\,dm\,ds.
\]
The change of variables is one-to-one on the interior of the domain. This is the claimed joint density and proves its normalization from normalized spherical area without appealing to any numerical integration.

**3. Conditional angular law.** At fixed \(m\), make the substitution \(s=m+q(m)\sin t\) with \(q(m)=\sqrt{2(1-m^2)}\). Because \(D=q(m)\cos t\), the joint probability differential becomes exactly \((12/\pi)dm\,dt\). The allowed angle runs from \(\alpha(m)\) to \(\pi/2\), so integration over \(t\) gives the claimed marginal, and conditioning makes \(t\) uniformly distributed over that interval. For \(1/\sqrt2\le m<1\), the lower endpoint is \(m+\sqrt{1-m^2}\), so \(\sin\alpha(m)=1/\sqrt2\) and \(\alpha(m)=\pi/4\). Consequently \(f_M(m)=3\) there. Inverting the conditional angular CDF gives the displayed quantile formula. At \(m=1\) the geometric fiber gives \(S=1\) and \(q(1)=0\); the standardized angle formula is not defined there, and no endpoint value is needed for the probability law.

## Verification
The accompanying standard-library script `CHECK.py` numerically integrates the proposed joint density for normalization and the marginal means, and compares the resulting mixed first moment to the exact prior formula
\[
\mathbb E[SM]=\frac13+\frac{2\sqrt2}{\pi}.
\]
It also numerically tests the conditional-angle formula at 599 values of \(m\) and compares four rectangular joint event probabilities to frequencies from 240,000 simulated directions sampled by normalizing independent standard Gaussian coordinates. The moment targets include \(\mathbb E[S]=3/2\) and \(\mathbb E[M]=(3\sqrt2/(2\pi))\arccos(1/3)\), which are independently known. These checks are finite consistency tests; the exact joint density, normalization, and conditional laws follow from the proof above, not from simulation.

## Relationship to prior work
Finch's 2011 cube-width analysis and cross-polytope analysis investigate individual widths and their moments. Kabluchko, Litvak, and Zaporozhets (2015) provide higher-moment identities for the **individual** projection widths of regular polytopes. The published exact cube width CDF and octahedron width CDF separately determine the laws of \(S\) and \(M\), but two marginal laws do not determine the dependence or the conditional law. The published orientation-dependent cube–octahedron covariance supplies the single joint moment \(\mathbb E[SM]\) for aligned solids and a rotated comparison, but not the two-variable density. The present result is the full aligned-pair joint distribution together with its conditional angular representation and support phase boundary. The generic distribution of sphere coordinates in elementary spherical probability is acknowledged as the starting measure, not as a new discovery.

## Limitations
This is an explicit finite-dimensional result for the *aligned* three-dimensional polar pair, not an arbitrary relative rotation, a general centrally symmetric body, or a higher-dimensional joint law. Exact individual width marginals, the aligned covariance, and the underlying spherical-coordinate Jacobian are prior mathematical facts. A previously unnoticed treatment of the joint \(\ell_1\)- and \(\ell_\infty\)-norm distribution, or a sufficiently strong general multivariate angular formula, could subsume the displayed closed form; historical priority is therefore provisional. The numerical checks do not certify exhaustive literature coverage or independent mathematical correctness. Independent audit has not been performed.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, first posted 4 October 2011, arXiv:1110.0671, https://arxiv.org/abs/1110.0671.
2. S. R. Finch, *Mean Width of a Regular Cross-Polytope*, first posted 2 December 2011, arXiv:1112.0499, https://arxiv.org/abs/1112.0499.
3. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, first posted 26 November 2015, arXiv:1511.08479, https://arxiv.org/abs/1511.08479. See Section 3.
4. *Exact directional width law of the cube and its first spherical-cap transition*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2.
5. *Exact width distribution of the unit-edge regular octahedron*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-width-distribution-of-the-unit-edge-regular-octahedron--953206d3d8c4.
6. *Orientation-controlled covariance sign reversal for polar Platonic widths*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-orientation-controlled-covariance-sign-reversal-for-polar-platon--9a4508ced953.
