# A boundary-to-interior farthest-point transition and two center phases on flat Möbius bands

## Finding
Let \(M_{C,H}\) be the abstract compact flat Möbius band obtained by gluing \((0,y)\sim(C,-y)\) in \([0,C]\times[-H/2,H/2]\), where \(C,H>0\). Distances are **intrinsic shortest-path** distances. For a point at absolute transverse coordinate \(u=|y|\), let its eccentricity be \(e(u)=\max_q d(p,q)\). The following is an exact pointwise classification.

Write
\[
\alpha=\frac{C^2}{2H},\qquad
\beta=\frac{H+\sqrt{H^2+8C^2}}8,\qquad
\lambda=\frac7{\sqrt{15}}.
\]
If \(H\le C\), then throughout \(0\le u\le H/2\),
\[
\boxed{e(u)^2=\frac{C^2+H^2}{4}+\left(1+\frac{H^2}{C^2}\right)u^2.}
\]
If \(H>C\), the complete eccentricity profile is
\[
\boxed{e(u)^2=\begin{cases}
\frac{C^2+H^2}{4}+(1+H^2/C^2)u^2,&0\le u\le\alpha,\\[3pt]
C^2+(H/2-u)^2,&\alpha\le u\le\beta,\\[3pt]
C^2+\bigl(u-C^2/(4u)\bigr)^2,&\beta\le u\le H/2.
\end{cases}}
\]
Here \(0<\alpha<\beta<H/2\). The minimum eccentricity, or intrinsic Chebyshev radius, is
\[
\boxed{\rho(C,H)=\begin{cases}
\frac12\sqrt{C^2+H^2},&H\le\lambda C,\\[3pt]
\sqrt{C^2+\bigl(3H-\sqrt{H^2+8C^2}\bigr)^2/64},&H\ge\lambda C.
\end{cases}}
\]
The complete minimax-center locus is the core circle \(u=0\) if \(H<\lambda C\), the unique boundary-parallel circle \(u=\beta\) if \(H>\lambda C\), and **both disjoint circles** when \(H=\lambda C\). At coexistence \(\rho=4C/\sqrt{15}\) and \(\beta=\sqrt{15}C/6\). Thus the minimax center abruptly moves off the core, through an exact geometric first-order transition.

The intrinsic diameter is
\[
\boxed{\operatorname{diam}(M_{C,H})=\frac{C^2+H^2}{2\max\{C,H\}}.}
\]
For \(H<C\), every diametral pair consists of two boundary points, separated along the unique boundary circle by shorter boundary arclength \((C^2+H^2)/(2C)\). At \(H=C\), diametral pairs still join boundary points at shorter boundary arclength \(C\). For \(H>C\), precisely one point is on the boundary; in a common quotient chart its partner has transverse coordinate opposite in sign and magnitude \(C^2/(2H)\), with the same longitudinal coordinate. This classifies all diametral pairs, up to the stated quotient identifications and swapping the points.

As a consequence, when \(H\ge C\), the previously known boundary-only distance kernel is independent of \(H\), but measuring the **full intrinsic diameter** restores the invisible width exactly:
\[H=\operatorname{diam}(M_{C,H})+\sqrt{\operatorname{diam}(M_{C,H})^2-C^2}.\]

## Assumptions and scope
The quotient is a smooth intrinsically flat compact surface with geodesic boundary, not a claim of a smooth isometric embedding in three-dimensional space for arbitrary aspect ratios. Parameters \(C,H\) are the longitudinal identification length and the full width, respectively; its one boundary component has length \(2C\). The eccentricity supremum ranges over **all** points of the surface, including its boundary. Distances may use paths winding around the quotient. Absolute transverse height \(u\in[0,H/2]\) is an intrinsic symmetry coordinate, so formulas are independent of the longitudinal base point. The final inverse assertion assumes the boundary length (equivalently \(C\)) is known.

## Proof
**1. Exhaustive lift formula.** The flat covering strip is convex. The deck map is \(T(x,y)=(x+C,-y)\), hence a path lifts to a straight segment to a deck image. Fix lifts \(p=(0,u)\) with \(0\le u\le H/2\) and \(q=(t,z)\) with \(0\le t\le C\), \(-H/2\le z\le H/2\). Nearest even and odd deck images are respectively at horizontal offsets \(t\) and \(C-t\). Consequently
\[d(p,q)^2=\min\{t^2+(u-z)^2,(C-t)^2+(u+z)^2\}.\tag{1}\]
This is exact for all pairs; additional deck shifts cannot improve a same-parity vertical difference. Replacing \(z\) by \(-z\) and \(t\) by \(C-t\) preserves the expression, so it suffices to maximize over \(z\in[0,H/2]\).

**2. Optimize the longitudinal coordinate.** Set \(a=|u-z|\), \(b=u+z\), \(s=a+b=2\max\{u,z\}\), and \(v=b-a=2\min\{u,z\}\). The two terms in (1) increase and decrease, respectively, as \(t\) runs from zero to \(C\). Their equalizing point is
\[t_*=(C^2+sv)/(2C).\]
When \(sv\le C^2\), this lies inside the interval and gives
\[\max_t d(p,q)^2=\frac{C^2+s^2}{4}+\frac{1+s^2/C^2}{4}v^2.\tag{2}\]
When \(sv\ge C^2\), the maximum occurs at \(t=C\), with value
\[\max_t d(p,q)^2=C^2+(u-z)^2.\tag{3}\]
At equality the formulas agree. These alternatives include all extremizers because the two quadratic branches are strictly monotone in opposite directions.

**3. Optimize the transverse coordinate.** For fixed \(u\), the expression (2) strictly increases with \(z\) on its admissible range: when \(z\le u\), \(s=2u\) is fixed and \(v=2z\) increases; when \(z\ge u\), \(v=2u\) is fixed and \(s=2z\) increases. The crossing region is exactly \(4uz\le C^2\). Thus, if \(u\le\alpha=C^2/(2H)\), its global maximum is at \(z=H/2\), giving the first formula for \(e(u)^2\). If \(u>\alpha\), the maximum over the crossing region is at \(z_*=C^2/(4u)\), where the value equals \(C^2+(u-z_*)^2\). On the remaining interval \([z_*,H/2]\), (3) is a convex quadratic in \(z\) and therefore achieves its maximum at \(z=z_*\) or \(z=H/2\). Comparing the two endpoints amounts to comparing \(|u-z_*|\) with \(|u-H/2|\). Since \(z_*<H/2\), equality away from the opening point requires \(2u=z_*+H/2\). Its positive solution is \(u=\beta=(H+\sqrt{H^2+8C^2})/8\). For \(H>C\), \(\alpha<\beta<H/2\), with the outer-boundary competitor winning for \(\alpha<u<\beta\), and the interior competitor winning for \(\beta<u\le H/2\). For \(H\le C\), \(u\le\alpha\) throughout. This proves the complete profile without numerical approximation.

**4. Global minima and equality classification.** When \(H\le C\), \(e(u)\) increases strictly for positive \(u\), so the core is the complete center locus. When \(H>C\), the first branch increases from \(u=0\), the middle branch decreases strictly from \(\alpha\) to \(\beta\), and the final branch increases strictly from \(\beta\), since \(\beta>C/2\). Thus the only possible minimizers are \(0\) and \(\beta\). Their squared eccentricities differ by
\[e(0)^2-e(\beta)^2=\frac{3H^2-28C^2+3H\sqrt{H^2+8C^2}}{32}.\tag{4}\]
The numerator is strictly increasing in \(H>0\), and its unique positive zero satisfies \(H/C=7/\sqrt{15}\), by squaring after isolating the positive radical (or solving \(3H(H+\sqrt{H^2+8C^2})=28C^2\)). The claims about centers and the Chebyshev radius follow, including the exact equality case. The \(u>0\) level set forms one connected circle, because the deck map exchanges its two strips.

**5. Diameter and all diametral pairs.** The profile's only maximum candidates are its boundary branch at \(u=H/2\) and, for \(H>C\), its local peak at \(u=\alpha\). For \(H\le C\), the boundary value is \((C^2+H^2)/(2C)\). For \(H>C\), direct substitution shows \(e(\alpha)=e(H/2)=(C^2+H^2)/(2H)\), larger than all other eccentricities. The unique optimizing \(z\) in step 3 and the unique equalizing longitudinal offset from step 2 yield the stated boundary-pair and boundary–interior pair classifications (taking account of the reflection under one deck shift). At \(H=C\), the two descriptions coalesce. The inverse width identity is the positive solution of \(2DH=H^2+C^2\) in the regime \(H\ge C\).

## Verification
The attached independent numerical evaluator computes the exact two-image distance for a two-dimensional grid of target positions and maximizes the longitudinal offset analytically. It compares that brute transverse search against all three asserted eccentricity branches across aspect ratios on both sides of the two transitions. Numerical tests cannot establish the global all-real-variable maximization; the preceding monotonicity and convexity proof is exhaustive.

## Relationship to prior work
The rectangular flat Möbius quotient and its deck-distance formula are classical and appear in previously published flat-band random-distance studies. In particular the boundary-distance study cited below already gives the narrow-width boundary diameter and proves that the entire boundary metric cannot distinguish \(H\ge C\). Those parts are not claimed as new. The **pointwise farthest-distance profile**, the complete interior-versus-boundary farthest-pair description, and the distinct sharp Chebyshev-center transition \(H/C=7/\sqrt{15}\) concern different extremization questions: neither an area-averaged two-point distance law nor the restriction of the distance kernel to boundary pairs provides those center loci. The cited 2007 and 2014 elastic-strip papers instead study extrinsic equilibrium geometry, not these intrinsic minimax problems. The very simple known lift formula is a strong source of derivative-priority risk, explicitly retained below.

## Limitations
Only abstract **rectangular flat** Möbius bands are classified, not physical embedded ribbons, variable-width bands, arbitrary Riemannian metrics, or general surfaces. This is a direct exact minimax theorem, not a classification of arbitrary distance distributions. Prior elementary lift formulas make unnoticed historical antecedents possible; originality has not been independently certified. No numerical grid is asserted to prove continuous optimization.

## References
- E. L. Starostin and G. H. M. van der Heijden, *The shape of a Möbius strip*, Nature Materials **6** (2007), 563–567, published online 2007-07-15, https://doi.org/10.1038/nmat1929. Studies embedded inextensible equilibrium geometry, not a pointwise intrinsic eccentricity profile.
- E. L. Starostin and G. H. M. van der Heijden, *Equilibrium Shapes with Stress Localisation for Inextensible Elastic Möbius and Other Strips*, Journal of Elasticity **119** (2015), 67–112, first posted 2014-08-27, https://doi.org/10.1007/s10659-014-9495-0. Full open-access HTML studied: developable-strip variational geometry, not the intrinsic minimax-center problem.
- *Distance statistics detect the half-twist of a flat Möbius band* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-distance-statistics-detect-the-half-twist-of-a-flat-m-bius-band--cbaf47596178. Published intrinsic two-point distance distribution and an underlying lift formula.
- *Exact geodesic dispersion and unique area-constrained optimum of flat Möbius bands* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-geodesic-dispersion-and-unique-area-constrained-optimum-of--8010a90e7384. Published squared-distance expectation with the lift formula.
- *A width-invisibility transition in boundary-distance statistics of flat Möbius bands* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-width-invisibility-transition-in-boundary-distance-statistics--5ced922ce0bf. Published boundary-point distance kernel and its width-blind regime; the narrow-width boundary diameter is previously known.
- *A complete two-point distance ordering for the flat Möbius band and its matched cylinder* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-complete-two-point-distance-ordering-for-the-flat-m-bius-band--d61dc15f6cd5. Published pair-distance CDF and compared distance-law supports; does not describe the pointwise eccentricity or minimax center locus.
