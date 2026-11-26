# Sharp maximal-section probability and aspect-ratio rigidity for regular even-gon prisms

## Finding

For every integer \(m\ge3\), let \(P_{m,R,h}\subset\mathbb R^3\) be the right prism whose horizontal base is the regular \(2m\)-gon with circumradius \(R>0\), whose midplane is \(z=0\), and whose top and bottom faces are at heights \(h\) and \(-h\), respectively. Choose a central plane with Haar-uniform normal \(U\in S^2\). Write \(N\) for the number of sides of its polygonal intersection and \(p_m(\lambda)=\Pr(N=2m+2)\), where \(\lambda=h/R>0\).

Put \(\theta=\pi/(2m)\) and \(t=(1+\lambda^2)^{-1/2}\). Then \(N\le2m+2\) almost surely and
\[
\boxed{p_m(\lambda)=\frac{2m}{\pi}\left[2\arcsin(t\sin\theta)-\arcsin(t\sin(2\theta))\right].}
\]
For each \(m\ge3\), \(p_m\) is strictly increasing on \((0,\lambda_m^*)\) and strictly decreasing on \((\lambda_m^*,\infty)\), with the **unique** maximum at
\[
\boxed{\lambda_m^*=\sqrt{3\cos^2\theta-1}.}
\]
Its maximum value is
\[
\boxed{p_m^*=\frac{2m}{\pi}\left[2\arcsin\!\left(\frac{\tan\theta}{\sqrt3}\right)-\arcsin\!\left(\frac{2\sin\theta}{\sqrt3}\right)\right].}
\]
Moreover the sharp large-base limit is
\[
\boxed{\lim_{m\to\infty}\lambda_m^*=\sqrt2,\qquad \lim_{m\to\infty}m^2p_m^*=\frac{\pi^2}{6\sqrt3}.}
\]
For instance, a regular hexagonal prism (\(m=3\)) attains its maximal eight-sided central-section probability at \(h/R=\sqrt5/2\), with \(p_3^*=0.12260171954089\ldots\).

## Assumptions and scope

The base is a **regular, centrally symmetric** polygon with at least six sides. The cap-to-cap height is \(2h\), not \(h\); this normalization is essential to the optimizer formula. Sampling is Haar uniform over oriented normals, equivalent to uniform unoriented central planes. It is not an affine-image sampling law and does not randomize cutting-plane offsets. Directions passing through prism vertices or edges form null sets, and section counts are asserted only off those sets. No assertion is made for odd-sided prisms or generic nonregular bases. The four-sided base case is known in a stronger unequal-side form and excluded from the novel claim.

## Proof

**1. Count the intersection edges directly.** By scaling set \(R=1\) and use vertices \(v_j=(\cos(j\pi/m),\sin(j\pi/m))\), for \(0\le j<2m\). For a normal \(u=(u_x,u_y,u_z)\) with \(\sqrt{u_x^2+u_y^2}>0\), choose the planar azimuth \(\varphi\) and set
\[
q=\frac{h|u_z|}{\sqrt{u_x^2+u_y^2}},\qquad d_j=\cos(\varphi-j\pi/m).
\]
A vertical prism edge over \(v_j\) intersects the central plane in its interior exactly when \(|d_j|<q\). A horizontal top or bottom cap face has nonempty section boundary if and only if \(q<\max_j|d_j|\). When this holds, each cap contributes exactly one section segment with two endpoints on horizontal prism edges; hence the total number of section sides is the count of crossed vertical edges plus four. When it does not hold, all vertical edges and no horizontal edges are crossed, giving exactly \(2m\) sides. Because \(d_{j+m}=-d_j\), crossings of vertical edges occur in antipodal pairs. If \(b\) and \(a\) denote respectively the second-largest and largest values in \(\{|d_j|:0\le j<m\}\), the section has precisely \(2m+2\) sides if and only if \(b<q<a\). (At equality one hits an exceptional measure-zero direction.)

**2. Reduce the orientation integral.** The base has dihedral symmetry. Modulo its reflections and rotations, the azimuth is uniform on \([0,\theta]\) with density \(1/\theta=2m/\pi\), where \(\theta=\pi/(2m)\). On this interval the two largest magnitudes are
\[
a=\cos\varphi,\qquad b=\cos(2\theta-\varphi).
\]
The normal's absolute vertical coordinate \(Z=|u_z|\) is uniform on \([0,1]\), independent of azimuth, and \(q=\lambda Z/\sqrt{1-Z^2}\). For any \(w>0\),
\[
\Pr(q<w)=\frac{w}{\sqrt{\lambda^2+w^2}}.
\]
Thus
\[
p_m(\lambda)=\frac{2m}{\pi}\int_0^\theta\left[\frac{\cos\varphi}{\sqrt{\lambda^2+\cos^2\varphi}}-\frac{\cos(2\theta-\varphi)}{\sqrt{\lambda^2+\cos^2(2\theta-\varphi)}}\right]d\varphi.
\]
The antiderivative of \(\cos x/\sqrt{\lambda^2+\cos^2x}\) is \(\arcsin(\sin x/\sqrt{1+\lambda^2})\) on these angles. Evaluating both terms proves the formula.

**3. Unique aspect-ratio optimum.** As \(\lambda\) increases from zero to infinity, \(t=(1+\lambda^2)^{-1/2}\) decreases strictly from one to zero. Let \(s=\sin\theta\) and \(c=\cos\theta\). Differentiating the bracket in the formula with respect to \(t\) gives
\[
2s\left[\frac{1}{\sqrt{1-s^2t^2}}-\frac{c}{\sqrt{1-4s^2c^2t^2}}\right].
\]
All denominators are positive. Comparing the squares of the two positive bracket terms shows that the derivative has exactly the sign of \(1-3c^2t^2\). Because \(m\ge3\) gives \(c^2>1/2\), there is precisely one critical point in \((0,1)\), namely \(t_*=(\sqrt3c)^{-1}\). As the derivative is positive before that point and negative after it, it is the unique strict maximum. Translating back gives \(\lambda_*^2=3c^2-1\). The endpoints vanish: at \(t=0\) by continuity, and at \(t=1\) because \(2\theta\le\pi/3\) implies \(2\arcsin(\sin\theta)=\arcsin(\sin2\theta)=2\theta\). Substituting \(t_*\) yields the stated optimal probability.

**4. Exact leading asymptotics.** Put \(\theta=\pi/(2m)\). As \(\theta\to0\), \(t_*=(\sqrt3\cos\theta)^{-1}\to1/\sqrt3\). Taylor expansion of the two inverse sines at zero yields, uniformly for \(t\) in a compact subset of \((0,1)\),
\[
2\arcsin(t\sin\theta)-\arcsin(t\sin2\theta)
=\theta^3t(1-t^2)+O(\theta^5).
\]
At \(t=t_*\) this is \(2\theta^3/(3\sqrt3)+O(\theta^5)\). Multiplying by \(2m/\pi\) gives \(p_m^*=\pi^2/(6\sqrt3\,m^2)+O(m^{-4})\); the aspect-ratio limit is immediate. \(\square\)

## Verification

The standalone program `verify_prisms.py` enumerates all top, bottom, and vertical prism edge crossings by testing the signs of the plane equation at their endpoints. These geometric tests are independent of the spherical integration used in the proof. Using Gaussian normals (whose directions are Haar uniform), the program compares empirical maximal-side probabilities with the displayed analytic formula for six different prism orders and aspect ratios. It also checks maximality for nearby height perturbations, deterministic edge-crossing classifications over angular grids, and the limiting constant for several growing orders. Run `python3 verify_prisms.py` with Python 3 and NumPy installed. Its output terminates with `ALL_CHECKS_PASSED`. Finite numerical checks are diagnostic only; Steps 1–4 prove the statements for every integer \(m\ge3\).

## Relationship to prior work

Brandenburg, De Loera, and Meroni [1] develop the combinatorial chamber theory of polytope sections, including prisms among motivating examples, but their inspected arXiv manuscript does not state this all-height Haar law or its unique optimal aspect ratio. Ambrus and Gárgyán [2] analyze critical central sections of cubes by volume, a different functional. An earlier published exact Haar hexagon formula for **rectangular boxes** [3] includes the square-prism case \(m=2\), and is expressly recognized as prior knowledge: its cube extremal is not new. Another published regular-prism result [4] computes mean-square projection width, not maximum-side central-section probabilities. The present geometric result begins at six-sided regular bases and addresses the full family, its optimizing geometry and its sharp large-order behavior. Direct use of the cuboid formula cannot cover this family, whose base has more than four sides.

## Limitations

The sampling is restricted to center-passing planes under the isotropic normal law. The theorem does not give the complete distribution of all lesser section side counts, nor all-order optimization over arbitrary prism bases or polygon deformations. The asymptotic is an ordered-base limit at the optimized height; arbitrary height sequences need not have the same leading constant. Searches and inspected predecessor sources do not constitute a proof of historical priority, and an older unpublished or unindexed equivalent stereological calculation remains possible. The computational verifier does not provide independent mathematical certification.

## References

[1] M. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1 (first public version April 27, 2023), https://arxiv.org/abs/2304.14239.

[2] G. Ambrus and P. Gárgyán, *Non-diagonal critical central sections of the cube*, arXiv:2307.03792 (first public version July 7, 2023), https://arxiv.org/abs/2307.03792.

[3] *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, published-finding corpus open mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.

[4] *Exact mean-square width of every uniform regular prism*, published-finding corpus open mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-mean-square-width-of-every-uniform-regular-prism--eb371b3be549.
