# A sharp inverse theorem for non-even fourth dual curvature data on four coordinate normals

## Finding
Let \(e_1,e_2\) denote the coordinate unit vectors in the Euclidean plane. For any \(A,B,C>0\) with \(B\ne C\), consider the genuinely non-even four-atomic measure
\[
\mu=A(\delta_{e_1}+\delta_{-e_1})+B\delta_{e_2}+C\delta_{-e_2}.
\]
There is a compact convex body \(K\subset\mathbb R^2\) with the origin in its interior and fourth dual curvature measure \(\widetilde C_4(K,\cdot)=\mu\) **if and only if**
\[
\frac16<\frac{A}{B+C}<\frac32.
\]
When this strict condition holds, the solution is unique **among all origin-interior planar convex bodies**, not merely among polygons, and is a rectangle symmetric about the horizontal axis's perpendicular reflection \((x,y)\mapsto(-x,y)\). Its four sides generally are not centered vertically.

Here is an explicit inverse. Put \(\lambda=A/(B+C)\), \(\beta=B/C\), and
\[
\kappa=\frac{3-2\lambda}{6\lambda-1}>0,\qquad u(t)=t^2-t+1.
\]
There is precisely one positive solution \(t\) of
\[
\beta=\frac{3\kappa+u(t)}{t[3\kappa t^2+u(t)]}.
\]
Define \(s=\sqrt{\kappa/u(t)}\) and \(a=(B/(s^3+s/3))^{1/4}\). Then
\[
\boxed{K=[-a,a]\times[-ast,as].}
\]
Both inequalities on \(\lambda\) are sharp and cannot be replaced by non-strict inequalities for origin-interior bodies.

## Assumptions and scope
The fourth dual curvature measure uses the exact normalization
\[
\widetilde C_4(K,\eta)=\frac12\int_{\alpha_K^*(\eta)}\rho_K(\theta)^4\,d\theta,
\]
where \(\rho_K\) is radial distance and \(\alpha_K^*\) is the reverse radial Gauss image. The domain consists of every compact convex body with nonempty interior containing the origin strictly within it. The atomic normal directions are exactly \(\pm e_1,\pm e_2\), with equal masses on the horizontal pair, and \(B\ne C\) ensures the measure is not centrally even. No constraints on \(A,B,C\) other than their positivity are assumed.

## Proof
**1. Support rigidity.** The radial Gauss map pushes forward the positive density \(\rho_K^4/2\) on the circle. At almost every regular boundary point \(x\) with outward normal \(\nu(x)\), radial change of variables yields
\[
 d\widetilde C_4=\frac12\lVert x\rVert^2\langle x,\nu(x)\rangle\,d\mathcal H^1(x).
\]
Since the origin is strictly inside, the scalar weight is uniformly strictly positive on the compact boundary, and the measure is concentrated on four normals only. Every positive-length portion of the boundary must therefore have one of those normals almost everywhere. Parametrizing its boundary by arc length, this implies that all boundary tangent vectors almost everywhere are one of the four coordinate unit tangents and, because convex normal angle is monotone, each normal direction can occupy at most one connected facet. Thus the boundary consists of four coordinate-parallel segments, a rectangle \([-a,b]\times[-c,d]\) with \(a,b,c,d>0\). This also excludes an undisclosed nonpolygonal realizer.

**2. Four exact facet masses.** For an arbitrary such rectangle, integrate \(\rho_K(\theta)^4/2\) along rays hitting each side, using the slope substitution \(z=\tan\theta\). On the side \(x=b\), \(\rho=b\sqrt{1+z^2}\), \(d\theta=dz/(1+z^2)\), and \(z\in[-c/b,d/b]\). Hence
\[
\begin{aligned}
2\widetilde C_4(K,\{e_1\})&=b^3(c+d)+\frac b3(c^3+d^3),\\
2\widetilde C_4(K,\{-e_1\})&=a^3(c+d)+\frac a3(c^3+d^3),\\
2\widetilde C_4(K,\{e_2\})&=d^3(a+b)+\frac d3(a^3+b^3),\\
2\widetilde C_4(K,\{-e_2\})&=c^3(a+b)+\frac c3(a^3+b^3).
\end{aligned}
\]
For fixed \(c,d>0\), the right side of the first identity is strictly increasing as a function of \(b>0\), and similarly for \(a\). Therefore equal masses at \(\pm e_1\) force \(b=a\), not just the existence of one symmetric solution.

**3. Reduce the inverse to one strictly monotone scalar equation.** Set \(d=as\), \(c=ast\) with \(s,t>0\). The three independent masses become
\[
\begin{aligned}
A&=a^4\left[\frac{s(t+1)}2+\frac{s^3(t^3+1)}6\right],\\
B&=a^4\left[s^3+\frac s3\right],\\
C&=a^4\left[s^3t^3+\frac{st}3\right].
\end{aligned}
\]
Because \((t^3+1)/(t+1)=u(t)=t^2-t+1>0\), the first ratio is
\[
\lambda=\frac A{B+C}=\frac{3+\kappa}{2(1+3\kappa)},\qquad \kappa=s^2u(t)>0.
\]
This expression decreases strictly from \(3/2\) to \(1/6\) as \(\kappa\) runs over positive values, giving the **necessary and sharp** strict interval and \(\kappa=(3-2\lambda)/(6\lambda-1)\).

The second ratio becomes \(\beta=F_\kappa(t)\), with
\[
F_\kappa(t)=\frac{3\kappa+u(t)}{t(3\kappa t^2+u(t))},\quad
F_\kappa'(t)=-\frac{(3\kappa+1)[9\kappa t^2+u(t)^2]}{t^2[3\kappa t^2+u(t)]^2}<0.
\]
The derivative identity follows by direct polynomial expansion; the denominator never vanishes for positive \(t,\kappa\). Furthermore \(F_\kappa(t)\to+\infty\) as \(t\downarrow0\) and \(F_\kappa(t)\to0\) as \(t\to\infty\). Thus for every positive \(\beta\) there is exactly one positive \(t\). The formulas stated above now yield the sole \(s,a,c,d\); substitution verifies **all four** mass identities exactly. This proves existence and uniqueness, including against bodies without an assumed reflection symmetry.

**4. Boundary sharpness.** Endpoints \(\lambda=1/6\) and \(3/2\) would require respectively \(\kappa\to\infty\) or \(\kappa\downarrow0\), neither possible for positive finite \(s,t\). Both can be approached through positive rectangles with fixed non-unit \(t\), so the two bounds are best possible even within genuinely non-even targets.

## Verification
The companion `verify.py` uses SymPy to verify the derivative identity and both algebraic inverse substitutions exactly. It independently integrates \(\rho_K^4/2\) over all four angular side sectors with numerical quadrature for four nonsymmetric rectangles, and checks five non-even positive target triples by solving the monotone inverse. Numerical tests are finite corroboration only; the universal classification follows from the preceding analytic argument. The program can be run with `python verify.py` where SymPy and SciPy are installed.

## Relationship to prior work
Monahan (2026) develops discrete dual-Minkowski existence by degree theory when outer normals satisfy a **general-position** arrangement such as diamond configuration or an odd-count planar condition. The exact antipodal cross of four directions used here fails the general-position hypothesis (opposite normals are linearly dependent), so its existence theorem does not subsume this sharp four-atom inverse theorem. Ge and Yang (2026) address *even* dual curvature measures, whereas the present targets have \(B\ne C\). A previously established classification for *even* cross-supported data does not imply a non-even inverse or its unique horizontal-reflection emergence. Henk and Pollehn (2018) study subspace concentration for even measures, not arbitrary non-even four-atom data. Liu and Lu (2022) study isotropic constant densities rather than four atomic normals.

## Limitations
The theorem concerns exactly exponent four and one reflection-balanced non-even family, not all four-atom data, other exponents, or other normal configurations. General historical priority cannot be established from electronic index searches, and a classical expression equivalent to the inverse could remain unindexed. The accompanying computations corroborate the algebra but do not prove an infinite-dimensional statement by enumeration.

## References
- C. Monahan, *A Topological Approach to the Discrete Dual Minkowski Problem*, arXiv:2611.13375v1 (2026-11-09), https://arxiv.org/abs/2611.13375.
- X. Ge and K. Yang, *The uniqueness and non-uniqueness of solutions to the even dual Minkowski problem*, arXiv:2608.01912 (2026), https://arxiv.org/abs/2608.01912.
- M. Henk and H. Pollehn, *Necessary subspace concentration conditions for the even dual Minkowski problem*, Advances in Mathematics 323 (2018), 114–141, https://doi.org/10.1016/j.aim.2017.10.037.
- Y. Liu and J. Lu, *On the number of solutions to the planar dual Minkowski problem*, arXiv:2209.15385 (2022), https://arxiv.org/abs/2209.15385.
- Y. Huang, E. Lutwak, D. Yang, and G. Zhang, *Geometric Measures in the Dual Brunn–Minkowski Theory and Their Associated Minkowski Problems*, Acta Mathematica 216 (2016), 325–388.
