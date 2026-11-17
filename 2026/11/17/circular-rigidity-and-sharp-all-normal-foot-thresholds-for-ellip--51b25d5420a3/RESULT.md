# Circular rigidity and sharp all-normal-foot thresholds for ellipse polygons

## Finding
For a convex polygon \(P\), define its *orthogonal-foot kernel* \(K(P)\) as the set of interior points whose perpendicular projections to the supporting lines of **every** side lie in their respective **open** side segments. A single theorem gives a smooth rigidity principle and its sharp finite discretization for affinely regular even polygons on ellipses.

**Smooth rigidity.** Let \(\Gamma\) be a strictly convex simple closed \(C^2\) curve, parametrized by arclength \(\gamma\), with convex hull \(C\), diameter \(D\), and maximum curvature \(\kappa\). Write \(\tau=\gamma'\) and
\[
\Delta(\Gamma)=\min_{z\in C}\max_s|\langle z-\gamma(s),\tau(s)\rangle|.
\]
Then \(\Delta(\Gamma)=0\) exactly for circles. For **every** cyclic inscribed polygon with largest arclength gap \(h\),
\[
K(P)\ne\varnothing\quad\Longrightarrow\quad\Delta(\Gamma)\le 2(1+D\kappa)h.
\]
Hence every noncircular curve has an explicitly positive mesh cutoff beyond which **no** inscribed polygon admits a point projecting inside every side; circles always admit their centers once the mesh is sufficiently fine. For an ellipse with semiaxes \(a\ge b>0\),
\[
\boxed{\Delta(\Gamma_{a,b})=a-b.}
\]
In particular, if \(a>b\), kernels are empty whenever \(h<(a-b)/(2(1+2a^2/b^2))\).

**Sharp finite ellipse law.** Fix an even integer \(n\ge4\), and let \(P_n(a,b)\) be the polygon with vertices \((a\cos(2\pi j/n),b\sin(2\pi j/n))\), \(0\le j<n\). Put \(x=\pi/n\), and, for \(n\ge6\),
\[
R_n=\min_{\substack{j\ge0\\ (2j+2)x<\pi/2}}\sqrt{\frac{\tan((2j+2)x)}{\tan((2j+1)x)}}.
\]
The minimum runs over a nonempty, finite set. Set \(R_4=+\infty\). Then, **exactly**,
\[
\boxed{K(P_n(a,b))\ne\varnothing\ \Longleftrightarrow\ 1\le a/b<R_n.}
\]
The kernel is empty at the threshold itself because projections onto endpoints are excluded. The first thresholds are \(R_6=\sqrt3\), \(R_8=\sqrt{1+\sqrt2}\), and \(R_{10}=5^{1/4}\). As even \(n\to\infty\),
\[
\boxed{n(R_n-1)\longrightarrow\pi.}
\]
Thus the exact all-feet condition for an even, equally eccentric-parameter-sampled ellipse exhibits a sharp vanishing anisotropy tolerance of order \(\pi/n\); no amount of translating the candidate projection point can improve this threshold.

## Assumptions and scope
All projections are Euclidean orthogonal projections to complete side lines and must land in the *relative interior* of each finite side. The candidate projection center lies strictly inside the polygon. For the smooth result, sampled vertices follow the cyclic order of the curve, the largest arclength gap includes the closing gap, and no equal-spacing assumption is made. The finite ellipse classification requires **even** \(n\), which guarantees central symmetry, and equally spaced *eccentric anomalies* (not equally spaced ellipse arclengths). The assertions are about feasibility of all-side perpendicular feet, not the similarity factor of iterated pedal polygons. The sharp finite condition and uniform smooth obstruction are components of one classification of all-side normal-foot feasibility.

## Proof
**1. Foot strips and a chord–tangent estimate.** For a side \([u,v]\), writing \(t=(v-u)/\|v-u\|\), its foot condition is equivalent to \(0<\langle z-u,t\rangle<\|v-u\|\). This is an open strip, so the intersection of all foot-admissibility strips with the open polygon is convex. On a curve arc of length \(\ell\) from \(u=\gamma(s_0)\) to \(v=\gamma(s_0+\ell)\), the normalized average tangent \(w=(v-u)/\ell\) satisfies \(\|w-\tau(s_0)\|\le\kappa\ell/2\), while \(\|w-(w/\|w\|)\|\le\|w-\tau(s_0)\|\). Hence \(\|t-\tau(s_0)\|\le\kappa\ell\).

**2. Uniform obstruction and circle characterization.** If \(z\in K(P)\), then \(z,u\in C\) and the strip condition imply
\[
|\langle z-\gamma(s_0),\tau(s_0)\rangle|\le\ell+D\kappa\ell\le(1+D\kappa)h.
\]
For \(g_z(s)=\langle z-\gamma(s),\tau(s)\rangle\), differentiation gives \(g_z'=-1+\langle z-\gamma,\gamma''\rangle\), so \(|g_z'|\le1+D\kappa\). Every boundary parameter is at arclength at most \(h\) from a preceding vertex, yielding \(\max|g_z|\le2(1+D\kappa)h\). Minimizing over \(z\in C\) proves the bound. Compactness gives a minimizer for \(\Delta\); if \(\Delta=0\), the derivative of \(\|\gamma(s)-z\|^2\) vanishes everywhere, forcing the entire closed curve to be a circle. A circle's center projects to the midpoint of every inscribed chord and lies inside every inscribed polygon with maximum gap smaller than half the circumference, proving the converse.

**3. Explicit elliptic residual.** For \(\gamma(\theta)=(a\cos\theta,b\sin\theta)\), at the origin,
\[
|g_0(\theta)|=\frac{(a^2-b^2)|\sin\theta\cos\theta|}{\sqrt{a^2\sin^2\theta+b^2\cos^2\theta}}.
\]
Writing \(t=\tan^2\theta\), the square is \((a^2-b^2)^2t/((1+t)(a^2t+b^2))\). Its maximum occurs at \(t=b/a\) and equals \((a-b)^2\). For any displacement \(z\), an antipodal pair of ellipse points produces residuals of the form \(c\pm\langle z,\tau\rangle\), whose maximum absolute value is at least \(|c|\). Therefore \(z=0\) minimizes the global residual and \(\Delta=a-b\). The ellipse has \(D=2a\) and \(\kappa=a/b^2\), giving the claimed quantitative cutoff.

**4. Even ellipse polygons reduce to their centers.** The polygon \(P_n(a,b)\) is centrally symmetric for even \(n\). Its foot strips are carried to one another by reflection through the origin; therefore the convex set \(K(P_n)\) is centrally symmetric. If it contains a point \(z\), then it contains \(-z\) and hence their midpoint \(0\). Conversely \(0\) lies strictly inside \(P_n\), so feasibility is equivalent to all of its perpendicular feet landing inside the corresponding sides.

**5. Exact edge-by-edge threshold.** Write \(x=\pi/n\) and \(\phi_j=(2j+1)x\). The side between eccentric parameters \(\phi_j-x\) and \(\phi_j+x\) has midpoint
\[
m_j=\cos x\,(a\cos\phi_j,b\sin\phi_j)
\]
and displacement vector
\[
d_j=2\sin x\,(-a\sin\phi_j,b\cos\phi_j).
\]
The perpendicular foot from \(0\) belongs to the open side precisely when \(|m_j\cdot d_j|<\|d_j\|^2/2\), equivalently
\[
(a^2-b^2)|\sin\phi_j\cos\phi_j|
<\tan x\,(a^2\sin^2\phi_j+b^2\cos^2\phi_j).
\]
By quadrant and central symmetries, it suffices to inspect \(0<\phi_j<\pi/2\). When \(\phi_j+x\ge\pi/2\) the inequality holds for every \(a\ge b\); otherwise, rearrangement yields
\[
\left(\frac ab\right)^2<\frac{\tan(\phi_j+x)}{\tan\phi_j}.
\]
The possible angles are exactly \(\phi_j=(2j+1)x\), with \(\phi_j+x=(2j+2)x<\pi/2\) for the restrictive cases. Taking the minimum proves the sharp threshold, strictness at equality, and the vacuous \(n=4\) case. Direct tangent-angle identities give the displayed small-\(n\) values.

**6. Sharp large-\(n\) scaling.** Put \(f_x(\phi)=\tan(\phi+x)/\tan\phi\). On \((0,\pi/2-x)\), elementary differentiation gives
\[
\frac{d}{d\phi}\log f_x(\phi)=\frac{2}{\sin(2\phi+2x)}-\frac{2}{\sin2\phi},
\]
so its sole minimum occurs at \(\phi=\pi/4-x/2\). The minimum over the continuum is
\[
f_x(\pi/4-x/2)=\left(\frac{1+\tan(x/2)}{1-\tan(x/2)}\right)^2=1+2x+O(x^2).
\]
At least one admissible sampled angle \((2j+1)x\) differs from \(\pi/4-x/2\) by at most \(x\) for all sufficiently large even \(n\). The Taylor expansion of \(f_x\) on a fixed neighborhood of \(\pi/4\), uniform for these angles, gives \(f_x((2j+1)x)=1+2x+O(x^2)\). Since the sampled minimum lies between these two expressions, \(R_n^2=1+2x+O(x^2)\), whence \(R_n=1+x+O(x^2)\) and \(n(R_n-1)\to\pi\).

## Verification
The independent standard-library file `verify_orthogonal_kernel.py` checks the exact finite threshold by comparing the symbolic angle condition with direct vector dot-product foot calculations for numerous even polygon sizes, anisotropy ratios on both sides of the threshold, and borderline cases. It also tests the known elliptic residual \(a-b\) against deterministic numerical maximization and examines the \(n(R_n-1)\) limit. These finite regression tests cannot replace the complete analytical proof above.

## Relationship to prior work
The source on iterated pedal constructions studies perpendicular feet on **supporting lines** and similarity of returned shapes, rather than simultaneous containment of all perpendicular feet in finite sides. The elementary characterization by intersection of foot strips for a fixed convex polygon was stated publicly in 2024 and is used without novelty claim. In particular, a 2026 published result on the *maximal normal chamber of a regular polygon* already contains exact circular regular-polygon kernel formulas, including an even/odd area law: **none of those regular-polygon formulas are claimed here**. The new statements are the uniform fine-mesh circle rigidity, the exact elliptic tangential residual, and the all-even-\(n\) *anisotropic ellipse* threshold and its asymptotic. A separate 2026 odd-polygon radial/support inverse rigidity result concerns recovery of a fixed polygon from its direction and support data and does not imply the uniform fine-mesh dichotomy or exact anisotropy cutoff.

## Limitations
The smooth obstruction assumes a closed strictly convex \(C^2\) curve; its mesh bound is sufficient but not generally sharp. The exact finite threshold assumes even vertex count and equally spaced eccentric parameters; it does not classify odd-sided polygonal approximations. The accessible 2026 pedal paper metadata and abstract were checked, but its complete paper could not be read via the available lawful routes; the complete text could not be obtained through accessible lawful routes. No independent mathematical review or priority certification has occurred.

## References
1. M. Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247, first public submission 2026-10-31, https://arxiv.org/abs/2611.01247.
2. *Point that can be projected onto each side of a convex polygon?*, mathematical discussion and slab characterization, 2024-09-12, https://math.stackexchange.com/questions/4970563/point-that-can-be-projected-onto-each-side-of-a-convex-polygon.
3. *Parity law for the maximal-normal chamber of a regular polygon*, published 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-parity-law-for-the-maximal-normal-chamber-of-a-regular-polygon--e8c77bf2f5b1.
4. *Odd-polygon radial–support rigidity under interior normal feet*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-odd-polygon-radial-support-rigidity-under-interior-normal-feet--d05310ca3cb8.
