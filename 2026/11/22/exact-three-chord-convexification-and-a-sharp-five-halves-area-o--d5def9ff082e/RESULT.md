# Exact three-chord convexification and a sharp \(5/2\) area onset for harmonic orthoptics

## Finding

For each \(R>0\) and \(0\le\varepsilon<R/8\), consider the convex oval with support function \(p_\varepsilon(t)=R+\varepsilon\cos(3t)\). Denote its right-angle isoptic (orthoptic) by \(\Gamma_\varepsilon\). The signed area of the bounded Jordan region \(D_\varepsilon\), the area of the convex hull \(H_\varepsilon=\operatorname{conv}(\Gamma_\varepsilon)\), and their difference \(\Delta(\varepsilon)\) have a sharp transition at
\[
\varepsilon_0=\frac{R}{8\sqrt2}.
\]
The orthoptic is convex for \(0\le\varepsilon\le\varepsilon_0\). For \(\varepsilon_0<\varepsilon<R/8\), its convex hull has exactly three supporting straight chords and three intervening smooth convex arcs. After a rotation and a shift in the parameter, put \(r=\sqrt2R\) and
\[
z_\varepsilon(t)=r e^{it}-\varepsilon e^{4it},\quad x(t)=r\cos t-\varepsilon\cos4t,\quad y(t)=r\sin t-\varepsilon\sin4t.
\]
There exists exactly one \(s=s(\varepsilon)\in(0,\pi/6)\) such that
\[
16\varepsilon\cos s\cos(2s)=r.
\]
The three hull chords join \(z(2k\pi/3-s)\) to \(z(2k\pi/3+s)\), for \(k=0,1,2\). Writing \(\Delta=\operatorname{area}(H_\varepsilon)-\operatorname{area}(D_\varepsilon)\), the **exact all-amplitude formula** is
\[
\Delta(\varepsilon)=\begin{cases}0,&0\le\varepsilon\le r/16,\\
6\displaystyle\int_0^{s(\varepsilon)}[x(s(\varepsilon))-x(t)]\,[r\cos t-4\varepsilon\cos4t]dt,&r/16<\varepsilon<R/8.
\end{cases}
\]
The enclosed area is exactly \(\operatorname{area}(D_\varepsilon)=\pi(r^2+4\varepsilon^2)\). At \(\varepsilon=\varepsilon_0+\delta\), the new hull area has the sharp singular excess
\[
\boxed{\Delta(\varepsilon_0+\delta)=\frac{3r^2}{2}\left(\frac{32}{5r}\right)^{5/2}\delta^{5/2}+O_R(\delta^{7/2})}\qquad(\delta\downarrow0).
\]
Its coefficient is strictly positive; consequently the hull-area function is \(C^2\) but not \(C^3\) at \(\varepsilon_0\).

## Assumptions and scope

The support function has normal parameter \(t\in\mathbb R/(2\pi\mathbb Z)\). Since \(p_\varepsilon+p_\varepsilon''=R-8\varepsilon\cos3t>0\), the generating oval is smooth and strictly convex in the stated open amplitude interval. The orthoptic is the locus of intersections of its perpendicular pairs of support lines. The parameter \(\varepsilon\) is an amplitude (a length), not a viewing angle. The area \(\operatorname{area}(D_\varepsilon)\) means the nonnegative geometric area bounded by the orthoptic; it is not the area of the original oval. All assertions concern Euclidean planar geometry.

## Proof

**1. Exact orthoptic and embeddedness.** The intersection of support lines with outward normal directions \(t\) and \(t+\pi/2\) is, in complex coordinates,
\[
Z(t)=e^{it}\{p_\varepsilon(t)+i p_\varepsilon(t+\pi/2)\}
=e^{it}\{(1+i)R+\varepsilon e^{3it}\}.
\]
Replacing \(t\) by \(t-\pi/4\) gives \(Z(t-\pi/4)=r e^{it}-\varepsilon e^{4it}\), with \(r=\sqrt2R\). Since \(\varepsilon/r<1/(8\sqrt2)<1/4\),
\[
\operatorname{Im}(\overline z z')=r^2+4\varepsilon^2-5r\varepsilon\cos3t
\ge (r-4\varepsilon)(r-\varepsilon)>0.
\]
Thus the polar argument increases strictly over one full turn; the orthoptic is an embedded, positively oriented, star-shaped Jordan curve.

**2. Exact curvature and onset.** Its signed curvature numerator is
\[
\operatorname{Im}(\overline {z'}z'')=r^2+64\varepsilon^2-20r\varepsilon\cos3t.
\]
The minimum is \((r-4\varepsilon)(r-16\varepsilon)\), nonnegative exactly when \(\varepsilon\le r/16\) in the admissible range. A regular simple closed curve with nonnegative curvature everywhere is convex (the tangent angle is nondecreasing through a full turn); this proves the initial branch, including equality. Above the threshold the curvature is negative near exactly the three symmetry-axis parameters \(2k\pi/3\).

**3. Global supporting chords.** By rotation symmetry it suffices to inspect the symmetry axis \(t=0\). The horizontal coordinate is \(x(t)=r\cos t-\varepsilon\cos4t\); writing \(c=\cos t\),
\[
x=r c-\varepsilon(8c^4-8c^2+1),\qquad\frac{dx}{dc}=r-16\varepsilon c(2c^2-1).
\]
If \(\varepsilon>r/16\), then \(q=r/(16\varepsilon)\in(1/\sqrt2,1)\). The polynomial \(c(2c^2-1)\) is at most \(2/(3\sqrt6)<1/\sqrt2\) on \([-1,0]\), is nonpositive on \([0,1/\sqrt2]\), and is strictly increasing from zero to one on \([1/\sqrt2,1]\). Consequently \(x\) has its unique maximum value at the two parameters \(\pm s\), where \(s\in(0,\pi/6)\) solves \(16\varepsilon\cos s\cos2s=r\). These give the globally supporting vertical line \(x=x(s)\). Its rotated copies supply the other two supporting chords. On \([-s,s]\), the ordinate is strictly increasing, since \(y'(t)=r\cos t-4\varepsilon\cos4t>r\sqrt3/2-r/(2\sqrt2)>0\).

At \(t=s\), the supporting maximum is strict and \(x''(s)<0\); since \(y'(s)>0\), the signed curvature numerator \(x'(s)y''(s)-y'(s)x''(s)\) is positive. It is positive throughout each remaining smooth interval \([s,2\pi/3-s]\), because \(\cos3t\le\cos3s\) there. Hence the curve formed by those three smooth pieces and their three supporting chords has a continuous nondecreasing tangent direction with total turn \(2\pi\). It bounds a convex domain. The discarded pieces lie on the inward side of their supporting chords and within that domain (strict radial embeddedness, monotone \(y\) on each discarded piece); thus the patched boundary is precisely \(\partial H_\varepsilon\). This also proves that no additional hull chords or contact arcs occur.

**4. Areas and exact formula.** Fourier orthogonality in Green's formula gives
\[
\operatorname{area}(D_\varepsilon)=\frac12\int_0^{2\pi}\operatorname{Im}(\overline z z')dt=\pi(r^2+4\varepsilon^2).
\]
For one inward dent the area between the curve and the supporting chord is \(\int_{-s}^s[x(s)-x(t)]y'(t)dt\); the integrand is nonnegative and even, and the three congruent dents give exactly the displayed integral formula for \(\Delta\).

**5. Critical asymptotics.** Put \(\varepsilon=r/16+\delta\), \(\delta\downarrow0\). Expanding the chord condition yields
\[
s^2=\frac{32}{5r}\delta+O_r(\delta^2).
\]
The Taylor expansion of \(x\), uniformly for \(|t|\le s\), gives
\[
x(s)-x(t)=\frac{5r}{8}(s^2-t^2)^2+O_r(s^6),\qquad
y'(t)=\frac{3r}{4}+O_r(s^2).
\]
Since \(\int_0^s(s^2-t^2)^2dt=8s^5/15\),
\[
\Delta=6\frac{5r}{8}\frac{3r}{4}\frac{8s^5}{15}+O_r(s^7)
=\frac{3r^2}{2}s^5+O_r(s^7),
\]
which proves the claimed \(5/2\) coefficient and \(O_R(\delta^{7/2})\) remainder. Below the threshold \(\Delta=0\), so the first two amplitude derivatives of the full hull area agree at the transition but its third derivative from above is singular.

## Verification

The accompanying `check_orthoptic_hull.py` uses 65-digit arithmetic to solve the unique chord equation and integrate the nonnegative pocket integrand for four amplitudes approaching the threshold. The scaled coefficients converge to the exact constant, and a separate optional 60,000-point planar convex-hull numerical comparison agrees with the exact total area within a stated finite-grid tolerance. The program prints `THREEFOLD_ORTHOPTIC_HULL_AREA_CHECKS_OK` on success. The proof above, not finite sampling or a numerical code run, establishes the continuum and all admissible amplitudes.

## Relationship to prior work

The support-function description of isoptics, including orthoptics, is classical; see Csima--Szirmai (2013) for background and Csima (2023) for isoptics of cycloidal curves. Michalska (2003) proves convexity conditions for the **area as a function of viewing angle**, including the threefold harmonic support example; this is a different question from the convex hull of a fixed orthoptic. Skrzypiec (2021) already studies **curvature-sign and angle transitions** of precisely the support family \(p=a+\cos3t\). Those curvature observations are not claimed to be new. Here the claimed new result is the exact three-chord hull boundary, the *difference* between hull and Jordan area, and its sharp \(5/2\) amplitude onset coefficient. The existence of the prior curvature transition by itself does not determine which distant contact points generate hull chords or quantify the area lost to convexification. Cross-parameter literature and indexed records were checked; priority remains provisional.

## Limitations

This is an exact result for the right-angle isoptic of the one-harmonic, threefold-symmetric support family, with \(R>0\) and \(\varepsilon<R/8\). It does not classify isoptics at other viewing angles, higher harmonics, or nonconvex generating curves. The law is asymptotic at fixed \(R\). Neither a general stability theorem nor independent mathematical validation is claimed. A previously unnoticed classical computation of the same convexification area could reduce originality.

## References

1. G. Csima and J. Szirmai, *Isoptic curves of conic sections in constant curvature geometries*, first publicly available 2013-01-29, https://arxiv.org/abs/1301.6991.
2. M. Michalska, *A sufficient condition for the convexity of the area of an isoptic curve of an oval*, Rend. Sem. Mat. Univ. Padova 110 (2003), 161--169, https://www.numdam.org/item/RSMUP_2003__110__161_0.pdf.
3. H. L. Resnikoff, *On Curves and Surfaces of Constant Width*, arXiv first public 2015-04-25, https://arxiv.org/abs/1504.06733.
4. M. Skrzypiec, *Convexity limit angles for isoptics*, first published online 2021-03-04, https://doi.org/10.1007/s13366-021-00564-5.
5. G. Csima, *Isoptic curves of cycloids*, first preprint 2023-04-15, https://arxiv.org/abs/2304.07517.
