# Exact radial law and logarithmic boundary layer of the random Fermat–Torricelli point

## Finding

Independently choose three points \(U_1,U_2,U_3\) uniformly by arclength from the unit circle. Define their **Fermat–Torricelli point** (the geometric median) as the unique minimizer
\[
 F=\mathop{\rm argmin}_{z\in\mathbb R^2}\sum_{j=1}^3|z-U_j|,
 \qquad R=|F|.
\]
The entire distribution of \(F\) is rotationally invariant. It has a singular component equal to one third of normalized uniform arclength on the unit circle. On the open unit disk it has a smooth, strictly positive, radial planar density \(\rho(r)\), which for \(0\le r<1\) is exactly
\[
\boxed{\rho(r)=\frac{3\sqrt3}{8\pi^3}\int_0^{2\pi}
 \frac{d\phi}{\sqrt{1-r^2\sin^2\phi}\sqrt{1-r^2\sin^2(\phi+2\pi/3)}}.}
\]
In particular, for every \(0\le a<1\),
\[
 \Pr(R\le a)=2\pi\int_0^a r\rho(r)\,dr,
 \qquad \Pr(R=1)=\frac13,
 \qquad \int_0^1 2\pi r\rho(r)\,dr=\frac23.
\]
The density has two contrasting, sharp spatial limits:
\[
\boxed{\rho(0)=\frac{3\sqrt3}{4\pi^2},\qquad
 \rho(r)=\frac3{\pi^3}\log\frac1{1-r^2}+O(1)\quad(r\uparrow1).}
\]
Equivalently, with \(\varepsilon\downarrow0\),
\[
\boxed{\Pr(R<\varepsilon)=\frac{3\sqrt3}{4\pi}\varepsilon^2+O(\varepsilon^4),\qquad
 \Pr(1-\varepsilon<R<1)=\frac6{\pi^2}\varepsilon\log\frac1\varepsilon+O(\varepsilon).}
\]
The latter is only the **interior continuous component**; the separate boundary mass is exactly \(1/3\). No point of the plane carries positive individual probability mass.

## Assumptions and scope

The three circle points are independent and identically distributed with normalized arclength (not uniform in the disk). Degenerate or repeated triples have probability zero. The geometric median is defined by the actual distance-minimizing property: if a triangle angle is at least \(120^\circ\), its median is the corresponding vertex, not the extrapolated first isogonic point. If every triangle angle is below \(120^\circ\), the median is the unique interior point from which all three pairs of vertices subtend angles \(120^\circ\). All distances are Euclidean, all probabilities are unconditional, and all implied constants are absolute. \(\rho\) is a density relative to two-dimensional Lebesgue area, not a radial density relative to \(dr\).

## Proof

**1. The singular boundary component.** Start at the first labeled sample point and enumerate the remaining two in their counterclockwise cyclic order. The three successive circular gaps \((G_1,G_2,G_3)\), including the wraparound gap, have normalized lengths \((G_1,G_2,G_3)/(2\pi)\) distributed as \(\operatorname{Dirichlet}(1,1,1)\). The triangle's interior angles are the three gaps divided by two, up to permutation. The event that the geometric median coincides with a vertex is therefore precisely \(\{\max_i G_i\ge4\pi/3\}\), apart from a null equality set. These three gap events are disjoint except on null sets, and each has probability \((1-2/3)^2=1/9\); hence the total probability is \(1/3\). Rotation invariance makes the distribution of the selected vertex uniform on the circle. For nondegenerate triples the minimizer lies in their convex hull, so it cannot lie outside the closed disk.

**2. Global coordinates for the interior component.** Fix an interior point \(z\), an orientation \(s\in\{+1,-1\}\), and \(\phi\in[0,2\pi)\). Introduce three equiangular unit vectors
\[
 v_j=(\cos(\phi+s\,2\pi(j-1)/3),\ \sin(\phi+s\,2\pi(j-1)/3)),\qquad j=1,2,3.
\]
Set \(b_j=z\cdot v_j\), \(h_j=\sqrt{1-|z|^2+b_j^2}>0\), and \(t_j=h_j-b_j>0\). The three points \(u_j=z+t_jv_j\) all lie on the unit circle since \(|z+t_jv_j|^2=1\). The gradient of \(\sum_j|w-u_j|\) at \(w=z\) is \(-\sum_jv_j=0\). Strict convexity for a noncollinear triple makes \(z\) its unique geometric median. Conversely, every triple with an interior median \(z\) has the three normalized rays \((U_j-z)/|U_j-z|\) separated by \(120^\circ\) and therefore arises in exactly one of these two orientation charts, with \(\phi\) determined modulo \(2\pi\). These charts cover all interior-median triples without multiplicity, up to angle-coordinate seams of measure zero.

**3. Exact change-of-variables Jacobian.** Let \(\theta_j=\arg u_j\), and write \(J(x,y)=(-y,x)\) for quarter-turn rotation. Differentiating \(u_j=z+t_jv_j\), with \(|u_j|=1\), gives
\[
 d\theta_j=\frac{(Jv_j)\cdot dz}{h_j}+\frac{t_j}{h_j}\,d\phi.
\]
Thus the absolute determinant of the matrix \(\partial(\theta_1,\theta_2,\theta_3)/\partial(z_x,z_y,\phi)\) is
\[
 \frac{\sqrt3}{2}\frac{t_1+t_2+t_3}{h_1h_2h_3}
 =\frac{\sqrt3}{2}\left(\frac1{h_1h_2}+\frac1{h_2h_3}+\frac1{h_3h_1}\right),
\]
because each pairwise sine of the three directions has magnitude \(\sqrt3/2\) and \(\sum_jb_j=z\cdot\sum_jv_j=0\), so \(\sum_j t_j=\sum_jh_j\). The original labeled angles have joint probability density \((2\pi)^{-3}\) relative to \(d\theta_1d\theta_2d\theta_3\). Integrating over \(\phi\) and summing the two orientations therefore yields
\[
 \rho(|z|)=\frac{\sqrt3}{8\pi^3}\int_0^{2\pi}
 \left(\frac1{h_1h_2}+\frac1{h_2h_3}+\frac1{h_3h_1}\right)d\phi.
\]
A shift of \(\phi\) by \(2\pi/3\) makes the three integrals equal; rotation puts \(z=(r,0)\) and \(h_j=\sqrt{1-r^2\sin^2(\phi+2\pi(j-1)/3)}\). This is exactly the displayed one-integral density formula. It is strictly positive and \(C^\infty\) on \(0\le r<1\), since its denominators stay bounded away from zero on compact subdisks. As the two orientation charts exhaust the interior event, the total integral over the disk is \(2/3\) by Step 1, without needing a separate numerical normalization.

**4. Center and rim limits.** At \(r=0\), both square roots in the density are one, so \(\rho(0)=3\sqrt3/(4\pi^2)\). The integrand is analytic in \(r^2\) on every compact subinterval of \([0,1)\), hence \(\rho(r)=\rho(0)+O(r^2)\). Integration in polar coordinates proves the center probability expansion.

For the rim let \(\delta=1-r^2\). The first square-root denominator vanishes in the limit at \(\phi=\pi/2,3\pi/2\), and the second at \(\phi=-\pi/6,5\pi/6\), modulo \(2\pi\). These four points are distinct; at each, the *other* denominator tends to \(\sqrt3/2\). In a fixed sufficiently small neighborhood of any one of them the singular denominator is \(\sqrt{\delta+(1-\delta)\sin^2u}\), where \(u\) is local angular displacement. Uniform Taylor bounds on the other factor reduce that neighborhood's integral to
\[
 \frac2{\sqrt3}\int_{-c}^c\frac{du}{\sqrt{\delta+u^2}}+O(1)
 =\frac2{\sqrt3}\log(1/\delta)+O(1).
\]
Here replacing \(\sin u\) by \(u\), and the smooth nonvanishing factor by its limit, makes an integrable uniformly bounded difference. Outside the four neighborhoods the full integrand is uniformly bounded. The total integral is therefore \((8/\sqrt3)\log(1/\delta)+O(1)\), and multiplying by \(3\sqrt3/(8\pi^3)\) gives \(\rho(r)=(3/\pi^3)\log(1/(1-r^2))+O(1)\). Finally integrate \(2\pi r\rho(r)\) over \(1-\varepsilon<r<1\), using \(1-r^2\asymp1-r\), to obtain the interior rim-shell probability. The independent singular mass at \(r=1\) is unchanged. \(\square\)

## Verification

The accompanying standalone checker evaluates the density integral and the radial CDF, independently computes Fermat points of randomly sampled triangles by finite Weiszfeld iteration, numerically checks the \(1/3\) boundary frequency, and compares the analytical change-of-variables Jacobian against finite differences. The fixed random seed makes the diagnostic reproducible. Numerical simulation is not part of the proof, does not certify asymptotic remainders, and cannot establish novelty. Run `python checker.py` with Python, NumPy, and SciPy installed; the checker prints `FERMAT_RADIAL_DENSITY_DIAGNOSTICS_OK` and `FERMAT_JACOBIAN_FINITE_DIFFERENCE_OK` upon success.

## Relationship to prior work

The deterministic Fermat–Torricelli characterization and its classical \(120^\circ\) boundary rule are standard [1,2]. Várilly [1], first publicly available February 1, 2000, studies loci of Fermat points under restrictions on the *Euler line*, not the push-forward law under independently random points on a fixed circumcircle. Mordukhovich and Nam [2] give convex-analytic solution criteria and iterative methods, but no finite-three-point stochastic spatial density. Classical random-inscribed-triangle calculations [3] and published results on its inradius, angle-count statistics, and Steiner-tree length concern different push-forwards of the angle-simplex law. The distinctive claim here is the **complete positional distribution** of the geometric median, including its singular boundary component and logarithmically divergent interior density near the circle.

## Limitations

The theorem is only for three i.i.d. **uniform** points on one Euclidean circle, not area-uniform points, weighted medians, general convex curves, other sample sizes, or the untruncated first isogonic center outside the \(120^\circ\) regime. The local rim expansion has a bounded, unevaluated remainder and does not provide a full elementary CDF. Earlier probability literature may contain an equivalent geometric-median density under different terminology; the historical priority comparison is provisional, and the scientific review is not an independent audit.

## References

[1] Anthony Várilly, *Location of incenters and Fermat points in variable triangles*, first arXiv submission 2000-02-01, https://arxiv.org/abs/math/0002004 (full web-accessible text, especially the section "The whereabouts of the Fermat point").

[2] Boris S. Mordukhovich and Nguyen Mau Nam, *The Fermat-Torricelli Problem and Weiszfeld's Algorithm in the Light of Convex Analysis*, arXiv:1302.5244, first public 2013-02-21, https://arxiv.org/abs/1302.5244 (full text, Sections 2–3).

[3] Eric W. Weisstein, *Circle Triangle Picking*, MathWorld, https://mathworld.wolfram.com/CircleTrianglePicking.html (distribution of sampled circle-angle coordinates; not a Fermat-location result).
