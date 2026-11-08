# Sharp area–Hausdorff envelope and independent asymptotic errors for rotated-square intersections

## Finding
For every integer \(m\ge2\), independently rotate \(m\) copies of the centered square \(Q=[-1,1]^2\) and intersect them. Orientations are uniform modulo \(\pi/2\). Write \(K_m\) for the intersection, \(A_m=\operatorname{area}(K_m)\), and \(H_m=d_H(K_m,B)\), with \(B\) the closed unit disk. Put \(L=\pi/2\), and order the orientations modulo \(L\); their positive circular gaps are \(\Delta_1,\ldots,\Delta_m\), with \(\sum_i\Delta_i=L\). Almost surely,
\[
 A_m=4\sum_{i=1}^m\tan(\Delta_i/2),\qquad
 H_m=\sec(\tfrac12\max_i\Delta_i)-1. \tag{1}
\]
These identities give the **complete deterministic area range conditional on the Hausdorff error**. Given \(H\) in the attainable interval \([\sec(L/(2m))-1,\sqrt2-1)\), set
\[
 M=2\arccos((1+H)^{-1}),\quad k=\lfloor L/M\rfloor,\quad r=L-kM,
\]
\[
 A_-(M)=4\left[\tan(M/2)+(m-1)\tan\left(\frac{L-M}{2(m-1)}\right)\right],\qquad
 A_+(M)=4\left[k\tan(M/2)+\tan(r/2)\right]. \tag{2}
\]
For distinct orientations, the exact attainable areas are \([A_-(M),A_+(M)]\) if \(L/m\le M<L/(m-1)\), and \([A_-(M),A_+(M))\) if \(L/(m-1)\le M<L\). At \(M=L/m\) there is just one area, \(4m\tan(L/(2m))\). Every interior value is attained; the lower boundary is attained when the other \(m-1\) gaps are equal. The upper boundary is attained precisely in the first range (where \(m-1\) gaps equal \(M\)); in the second range it is a sharp but unattained supremum. For \(m=2\), the second range is empty.

Moreover, as \(m\to\infty\), let \(G\) have the standard Gumbel distribution \(\Pr(G\le x)=\exp(-e^{-x})\), and let \(Z\) have the centered normal law of variance \(5\pi^6/32\). Then the **joint limit is a product law**:
\[
\left(m^{5/2}(A_m-\mathbb E A_m),\ 
 \frac{2m}{\pi}\sqrt{8H_m}-\log m\right)
 \xrightarrow{\mathrm d} (Z,G),\qquad Z\text{ and }G\text{ independent}. \tag{3}
\]
The normalization and variance constants are exact. The area moment estimates are
\[
 \mathbb E A_m=\pi+\frac{\pi^3}{8(m+1)(m+2)}+O(m^{-4}),\qquad
 \operatorname{Var}(A_m)\sim\frac{5\pi^6}{32m^5}. \tag{4}
\]
The two errors are not asserted to be independent at any finite \(m\).

## Assumptions and scope
The squares share the origin and each has inradius exactly one; rotations are independent and Haar-uniform on \([0,\pi/2)\). Distinct orientations hold almost surely and are required for the exact attainment statements in (2); coincident orientations may be used only in taking the stated suprema. The Hausdorff distance is the ordinary Euclidean Hausdorff distance between nonempty compact sets. Every \(K_m\) contains \(B\). Fixed-\(m\) envelopes apply to every deterministic list of distinct orientation classes, not just typical random lists. The asymptotics keep square size fixed and let \(m\) grow.

## Proof
**Geometry and exact joint parametrization.** One rotated square contributes the four tangent half-planes with outward normals at angles \(\theta+jL\) for \(j=0,1,2,3\). Sorting the \(4m\) normals cyclically repeats the \(m\) angular spacings four times. Adjacent tangent lines whose normals differ by \(\delta\in(0,L)\) meet on the angular bisector at Euclidean radius \(\sec(\delta/2)\). Along the enclosing polygon, each such vertex contributes tangent lengths \(\tan(\delta/2)\) to its two incident sides. Hence its perimeter is twice the sum of these tangent lengths, and area is half that perimeter since the inradius equals one. This proves the first identity in (1). Because \(B\subset K_m\), \(d_H(K_m,B)=\max_{x\in K_m}(\|x\|-1)\). The maximum norm over a compact polygon occurs at a vertex, giving the second identity.

**Sharp conditional envelope and endpoints.** Fix the maximum spacing \(M\in[L/m,L)\). At least one gap equals \(M\), and the remaining \(m-1\) positive gaps sum to \(L-M\). Strict convexity of \(f(t)=\tan(t/2)\) on \([0,L]\), followed by Jensen's inequality, gives \(A_m\ge A_-(M)\), with equality exactly when all remaining gaps equal \((L-M)/(m-1)\); this is feasible because \(M\ge L/m\). The vector of \(m\) gaps is majorized by \((M,\ldots,M,r,0,\ldots,0)\), with \(k\) copies of \(M\) and \(r=L-kM\). Karamata's inequality gives \(A_m\le A_+(M)\). Equality under strict convexity requires exactly this multiset. For positive gaps this can occur only when \(k=m-1\) and \(r>0\), or at the equal-gap case \(M=L/m\). The condition \(k=m-1,r>0\) is exactly \(L/m<M<L/(m-1)\). Otherwise, the upper bound is approached by positive gaps tending to the zero entries of the majorizing vector, with the positive gaps adjusted to preserve total \(L\) and maximum \(M\). The locus of the remaining positive gaps \(0<\Delta_i\le M\) with sum \(L-M\) is convex and nonempty, and the area functional is continuous; therefore its image is the full claimed interval with the just-established endpoint convention. Formula (1) translates \(M\) monotonically into \(H\), completing (2).

**Dirichlet law, mean, and variance.** For independent uniform orientation classes, the circular gap vector satisfies
\[
 (\Delta_1,\ldots,\Delta_m)\ \overset{\rm d}=\ L(E_1,\ldots,E_m)/(E_1+\cdots+E_m), \tag{5}
\]
where the \(E_i\) are independent unit-rate exponentials. In particular the normalized gaps have the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Taylor's theorem uniformly on \([0,L]\) gives
\[
 A_m=\pi+\tfrac16 S_{3,m}+R_m,\quad
 0\le R_m\le C S_{5,m},\quad
 S_{j,m}=\sum_i\Delta_i^j. \tag{6}
\]
The exact Dirichlet moments yield
\[
 \mathbb E S_{3,m}=\frac{6L^3}{(m+1)(m+2)},\quad
 \operatorname{Var}(S_{3,m})=
 \frac{72L^6(m-1)(5m+11)}{(m+1)^2(m+2)^2(m+3)(m+4)(m+5)}
 \sim\frac{360L^6}{m^5}, \tag{7}
\]
while \(\mathbb E S_{5,m}^2=O(m^{-8})\). Thus \(\mathbb E|R_m|=O(m^{-4})\) and \(\mathbb E R_m^2=O(m^{-8})\). Cauchy–Schwarz applied to (6) proves (4) with \((360/36)L^6=10L^6=5\pi^6/32\).

**Joint Gaussian and extreme-value limit, including independence.** Set \(\overline E_m=m^{-1}\sum_iE_i\) and \(\overline{E^3}_m=m^{-1}\sum_iE_i^3\). Formula (5) gives \(S_{3,m}=L^3m^{-2}\overline{E^3}_m/\overline E_m^3\). The bivariate central limit theorem and delta method at \((\overline E_m,\overline{E^3}_m)=(1,6)\) give influence variable
\[
 Y_i=E_i^3-18E_i+12,\qquad \mathbb E Y_i=0,\quad \mathbb E Y_i^2=360. \tag{8}
\]
Consequently the area coordinate in (3) differs in probability by \(o(1)\) from \((L^3/6)m^{-1/2}\sum_iY_i\); the remainder estimate in (6) controls this assertion in \(L^2\) after centering.

Write \(T_m=\max_i E_i\). For any fixed real \(x,t\), set \(u_m=\log m+x\). Since \(\Pr(E_i>u_m)=e^{-x}/m\) and \(\mathbb E(|Y_i|;E_i>u_m)=O((\log m)^3/m)\),
\[
 \mathbb E\big(e^{itY_i/\sqrt m}\mathbf1_{E_i\le u_m}\big)
 =1-\frac{180t^2+e^{-x}}m+o(m^{-1}). \tag{9}
\]
Independence across \(i\) turns its \(m\)-th power into \(e^{-180t^2}e^{-e^{-x}}\). This factorization proves the joint convergence of \(m^{-1/2}\sum_iY_i\) and \(T_m-\log m\) to independent normal and Gumbel limits (the characteristic functions determine the joint distribution with its second-coordinate CDF). Finally, \(m^{-1}\sum_iE_i=1+O_{\mathbb P}(m^{-1/2})\), and \(T_m=O_{\mathbb P}(\log m)\), so
\[
 \frac{m}{L}\max_i\Delta_i-\log m=T_m/\overline E_m-\log m
 =T_m-\log m+o_{\mathbb P}(1). \tag{10}
\]
For \(M=\max_i\Delta_i\), the deterministic expansion \(\sqrt{8(\sec(M/2)-1)}=M+O(M^3)\), with \(M=O_{\mathbb P}((\log m)/m)\), shows that replacing \(M\) by \(\sqrt{8H_m}\) changes (10) by \(o_{\mathbb P}(1)\). Equations (6)–(10) give the joint product limit (3).

## Verification
The companion standalone Python program `verify.py` runs without external libraries. It computes rotated-square intersections by an independent planar half-plane clipping routine, comparing their actual areas and maximum vertex distances against both formulas in (1) for 360 distinct random configurations; the largest absolute errors were below \(5\times10^{-15}\) and \(2\times10^{-15}\), respectively. It also tests 600 gap configurations against both sharp envelopes, verifies explicit lower/upper equality constructions, checks the exact Dirichlet third-gap moments against an independently expanded formula, and runs fixed-seed numerical mean checks for \(m=2,5\). The output was `ROTATED_SQUARE_CHECK_OK` and `AREA_HAUSDORFF_ENVELOPE_OK`. The limit theorem is established analytically by (5)–(10); finite simulations do not certify asymptotic independence.

## Relationship to prior work
Fodor, Hug, and Ziebarth (2014, full text inspected) study intersections of independently sampled supporting half-spaces around convex bodies, deriving expected-volume asymptotics and variance upper bounds. Here each random rotation contributes four **dependent** tangent lines, and the model is defined for a fixed nonsmooth square; their theorem does not supply this pair of exact area/Hausdorff statistics or their joint law. Brazitikos and Stavrakakis (2014) study random-rotation intersections of symmetric convex bodies but report general volume and radius estimates in the available abstract; their complete text was not accessible. The published exact rotation-area theorem for tangential polygons establishes expected intersection area and its sharp polygonal minimizer, but explicitly leaves variance unspecified. In particular, its expected-area benchmark and the area identity considered alone are not claimed as novel.

Classical circular-spacing theory (Pyke, 1965) and the general Dirichlet power-sum central limit theorem used by Wang, Li, and Xu (2023, full HTML inspected) already supply the Gaussian spacing mechanism. Xu (2015) likewise studies random circumscribed polygons; the available abstract discusses normal area limits for independently sampled tangent points, with a different sampling architecture and no reported joint Hausdorff result. Those Gaussian or spacing ingredients are not claimed as new. A published exact circular-gap law for intersecting *disks* also establishes an analogous area central limit theorem but has no common rotated-square geometry or joint extreme-value/area envelope. The contribution here is the **sharp fixed-error attainable area classification with its attainment transition**, together with the **paired, exactly normalized and asymptotically independent Gaussian area/Gumbel Hausdorff errors** for the same intersected-square sample. No located source implies this combined conclusion, but older unindexed coverage remains possible.

## Limitations
This concerns identical centered squares with independent uniform rotations, not translations, nonsquare rectangles or independently sampled tangent lines. The exact envelope conditions distinguish distinct orientations from limits of repeated orientations. The product limit is asymptotic only: area and Hausdorff errors can be strongly dependent at practically accessible finite sample sizes, and no quantitative joint convergence rate is established. The full papers of Xu (2015) and Brazitikos–Stavrakakis (2014) were unavailable under current access conditions; the present originality assessment remains provisional. No independent mathematical audit has been performed.

## References
1. F. Fodor, D. Hug, I. Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105v1, first posted 2014-09-29; primary MSC 52A22. https://arxiv.org/abs/1409.8105
2. S. Brazitikos, P. Stavrakakis, *On the intersection of random rotations of a symmetric convex body*, Math. Proc. Camb. Philos. Soc. 157 (2014), 13–30, first online 2014-03-28. https://doi.org/10.1017/S0305004114000115
3. W.-Q. Xu, *Random circumscribing polygons and approximations of pi*, Statist. Probab. Lett. 106 (2015), 52–57. https://doi.org/10.1016/j.spl.2015.06.026
4. S. Wang, Z. Li, W.-Q. Xu, *Nonlinear random extrapolation estimates of pi under Dirichlet distributions*, J. Numer. Anal. Approx. Theory 52 (2023), 273–294. https://doi.org/10.33993/jnaat522-1360
5. R. Pyke, *Spacings*, J. R. Statist. Soc. B 27 (1965), 395–449 including discussion. https://doi.org/10.1111/j.2517-6161.1965.tb00602.x
6. *Sharp random-rotation area order and exponential shape memory for tangential polygons*, publicly archived research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-random-rotation-area-order-and-exponential-shape-memory-fo--9cc93a56f053
7. *Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks*, publicly archived research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-circular-gap-area-laws-and-gaussian-fluctuations-for-inter--1c25b18e16e8
