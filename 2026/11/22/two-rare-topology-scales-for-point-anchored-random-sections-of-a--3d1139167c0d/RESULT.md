# Two rare-topology scales for point-anchored random sections of a thin solid torus

## Finding

For every real \(R>1\), let
\[
T_R=\{(x,y,z)\in\mathbb R^3:(\sqrt{x^2+y^2}-R)^2+z^2\leq1\}.
\]
Sample \(X_R\) uniformly with respect to volume in \(T_R\), independently choose a Haar-uniform unit vector \(N\in S^2\), and take the plane \(P=\{Y:N\cdot Y=N\cdot X_R\}\). Put \(D_R=\Pr(P\cap T_R\text{ is a disk})\), \(A_R=\Pr(P\cap T_R\text{ is an annulus})\), and \(B_R=\Pr(P\cap T_R\text{ is two disjoint disks})\). Tangent and transition planes have probability zero. Then
\[
\boxed{\lim_{R\to\infty}\sqrt R\,D_R
=\frac{64\,\Gamma(3/4)}{15\pi^{3/2}\Gamma(5/4)}
=1.0359209536249055\ldots,}
\]
\[
\boxed{\lim_{R\to\infty}R^2A_R=\frac{16}{9\pi^2}
=0.1801265486974894\ldots.}
\]
Consequently \(B_R=1-D_R-A_R=1-\frac{64\Gamma(3/4)}{15\pi^{3/2}\Gamma(5/4)}R^{-1/2}+o(R^{-1/2})\).

This sampling protocol is different from choosing a motion-invariant random plane conditioned on meeting the torus. For the latter protocol, the disk probability is \(8/(\pi R)+o(R^{-1})\) and the annulus probability is \(2/(3\pi R^3)+o(R^{-3})\). Thus anchoring a uniformly oriented plane at a uniform volume point changes the power laws for **both** rare topologies.

## Assumptions and scope

The tube radius is exactly one and the major radius is \(R>1\); rescaling shows only the aspect ratio matters. All randomizations are independent except for the plane offset being determined by \(X_R\). The plane is unoriented, though a random oriented normal is used for convenience. The result is an \(R\to\infty\) asymptotic, not an exact finite-\(R\) formula and not a uniform statement for other meridian geometries. It is a probability theorem about random geometric sections, under primary MSC2020 \(60D05\).

For any fixed normal, the offset \(N\cdot X_R\) has density proportional to the area of the corresponding section, by the coarea/Cavalieri identity. Thus this is exactly **section-area-size-biased sampling**, not uniform-offset conditional sampling.

## Proof

**1. Parametrization and topology.** By axial symmetry and reflection, write the normal as \(N=(s,0,q)\), with \(s=\sin\beta\), \(q=\cos\beta\), and \(0\leq\beta\leq\pi/2\). The angle has probability density \(\sin\beta\,d\beta\). Parametrize a volume-uniform torus point by
\[
X_R=((R+H)\cos\Phi,(R+H)\sin\Phi,V),\qquad H^2+V^2\leq1.
\]
Here \(\Phi\) is uniform on \([0,2\pi)\); independently, \((H,V)\) has density \((1+H/R)/\pi\) on the unit disk. This follows from the toroidal Jacobian \(R+H\). Set \(c=Rs\) and \(M=N\cdot X_R=(R+H)s\cos\Phi+qV\). The planar-section classification for a circular torus gives, except on null boundaries,
\[
\begin{aligned}
\text{annulus}&\iff c<1\ \text{and }|M|<1-c,\\
\text{disk}&\iff |c-1|<|M|<c+1,\\
\text{two disks}&\iff c>1\ \text{and }|M|<c-1.
\end{aligned}
\]
The categories are exhaustive. They follow by intersecting the normalized plane with the two unit meridian disks; both, exactly one, and neither produce the three topologies.

**2. Disk limit.** Fix \(0<\beta\leq\pi/2\) and a meridian point \((H,V)\) in the unit disk. As \(R\to\infty\), \(c=Rs\to\infty\). A disk requires the azimuth \(\Phi\) to be within order \(R^{-1/2}\) of either of the two extrema \(0,\pi\). Taylor-expanding \(1-\cos\Phi\) at the extrema and using the preceding exact inequalities gives
\[
\lim_{R\to\infty}\sqrt R\Pr_\Phi(\text{disk}\mid\beta,H,V)
=\frac{\sqrt2}{\pi\sqrt{s}}
\bigl(\sqrt{1+sH+qV}+\sqrt{1+sH-qV}\bigr).
\]
All square roots are real because \(|sH\pm qV|\leq1\). Uniformly in the disk point, the probability is bounded by \(C\min(1,(Rs)^{-1/2})\) when \(Rs\geq1\), with a numerical \(C\); for \(Rs<1\) the trivial bound is enough. Therefore \(\sqrt R\Pr_\Phi(\text{disk}\mid\beta,H,V)\leq C' s^{-1/2}\). Multiplication by the normal density \(s\) makes this integrable in \(\beta\). The disk-point density is bounded by \(2/\pi\) and converges to uniform area density, so dominated convergence applies jointly.

For \((H,V)\) uniform on the disk, any unit linear projection \(Z=sH+qV\) has density \(2\sqrt{1-z^2}/\pi\) on \((-1,1)\). Both square-root expectations in the last display are therefore equal, and
\[
\mathbb E\sqrt{1+Z}=\frac2\pi\int_{-1}^1\sqrt{1+z}\sqrt{1-z^2}\,dz
=\frac{32\sqrt2}{15\pi}.
\]
Also \(\int_0^{\pi/2}\sqrt{\sin\beta}\,d\beta=\sqrt\pi\Gamma(3/4)/(2\Gamma(5/4))\). Combining these gives
\[
\lim_{R\to\infty}\sqrt R D_R
=\frac{2\sqrt2}{\pi}\frac{32\sqrt2}{15\pi}
\int_0^{\pi/2}\sqrt{\sin\beta}\,d\beta
=\frac{64\Gamma(3/4)}{15\pi^{3/2}\Gamma(5/4)}.
\]

**3. Annulus limit.** The annulus condition forces \(c=R\sin\beta<1\). Substitute \(t=R\sin\beta\), so that
\[
\sin\beta\,d\beta=\frac{t\,dt}{R^2\sqrt{1-t^2/R^2}}.
\]
For fixed \(t\in(0,1)\), the offset is \(M=(t+tH/R)\cos\Phi+V\sqrt{1-t^2/R^2}\to t\cos\Phi+V\). The density factor \(1+H/R\to1\) as well. All integrands are bounded on \(R\geq2\), and hence
\[
\lim_{R\to\infty}R^2 A_R
=\int_0^1t\,\Pr\bigl(|V+t\cos\Phi|<1-t\bigr)\,dt,
\]
where \(V\) is the vertical coordinate of a uniform unit-disk point, independent of uniform \(\Phi\). Put \(U=\cos\Phi\), with density \(1/(\pi\sqrt{1-u^2})\). For fixed \(v,u\in(-1,1)\), the event is \(0<t<\tau(v,u)\), where
\[
\tau(v,u)=\min\left(\frac{1-v}{1+u},\frac{1+v}{1-u}\right)\in[0,1].
\]
By the simultaneous sign symmetry \((v,u)\mapsto(-v,-u)\), the integral is
\[
C_A=\frac12\mathbb E\tau(V,U)^2
=\mathbb E\left[\frac{(1-V)^2}{(1+U)^2}\mathbf1_{\{V+U\geq0\}}\right].
\]
Condition on \(V=v\) and integrate \(U\geq-v\). With \(T=\sqrt{(1+v)/(1-v)}\), the tangent half-angle substitution yields
\[
\int_{-v}^1\frac{du}{\pi\sqrt{1-u^2}(1+u)^2}
=\frac{T+T^3/3}{2\pi}.
\]
Using the semicircle density of \(V\), algebra reduces the remaining integral to
\[
C_A=\frac1{\pi^2}\int_{-1}^1\left((1-v)^2(1+v)+\frac13(1-v)(1+v)^2\right)dv
=\frac{16}{9\pi^2}.
\]
This proves both limits and the stated two-disk complement.

**4. Comparison with uniform-offset sections.** Under the motion-invariant plane measure conditioned on hitting the torus, the normal has weight \(\sin\beta\) and, for each \(\beta\), the allowable positive offsets have length \(1+R\sin\beta\). The disk offsets have length \(2\min(R\sin\beta,1)\); the annulus offsets have length \((1-R\sin\beta)_+\). The common normalizer is \(1+\pi R/4\). Elementary limiting integration gives \(8/(\pi R)\) and \(2/(3\pi R^3)\), respectively, confirming that the anchored exponents are different. These baseline probabilities are not the new finding.

## Verification

The standalone file `check_torus_area.py` evaluates the exact finite-radius angular-probability identities using an arcsine CDF and deterministic Gaussian quadrature over the meridian disk and normal tilt. It independently compares those CDF identities with direct angular-grid section classification in 130 randomly chosen nondegenerate configurations. It prints the scaled topological probabilities for \(R=5,20,80,320\), corroborating convergence toward the two exact constants. The code is a finite numerical check only; the proof of the infinite claims is in Steps 2–3 above.

## Relationship to prior work

Finch (2026, arXiv:2611.15546v1), Sections 4–5 and 7, establishes the meridian-disk topology criterion and probabilities under **motion-invariant planes conditioned on meeting the torus**, including the disk optimum and formulas for other topologies. That work is the geometric foundation of Step 1 and is not re-claimed. A published note on a general three-topology Crofton law for convex-meridian toroids similarly treats **uniform offset**, not offset fixed by a random interior point. A separate published note on the Villarceau transition treats **central planes**, not offset random planes. Standard stereological sampling theory supplies the motivation for distinguishing section-selection mechanisms. None of these inspected statements states the two area-size-biased asymptotics or their constants; the area weighting changes the required integrals and powers of the aspect ratio.

## Limitations

The two constants have been proved only for circular, unit-tube ring tori in the thin-aspect-ratio limit. The result does not classify finite-radius extrema, other smooth toroids, area distributions, or bias created by nonuniform orientation. Prior-work comparison is based on the identified primary texts and indexed records; unindexed stereological or geometric-probability coverage remains a historical-priority risk. No independent mathematical assessment has been performed.

## References

1. S. Finch, *Slicing a Doughnut at Random*, arXiv:2611.15546v1, first posted 11 November 2026, especially Sections 4–5 and 7. https://arxiv.org/html/2611.15546v1
2. *A three-topology Crofton law and inverse support tomography for convex-meridian toroids*, published mathematical research note (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-three-topology-crofton-law-and-inverse-support-tomography-for--8cf34e87984a
3. *Logarithmic area cusp and Haar topology law at the Villarceau transition*, published mathematical research note (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-logarithmic-area-cusp-and-haar-topology-law-at-the-villarceau-tr--3f2e0b5e194a
4. Stereology Society, *Isotropic Uniform Random Sections*, general sampling-design discussion. https://www.stereologysociety.org/stereology/sampling/isotropic-sections/
