# Sharp six-to-seven-side stability threshold for affine least squares on filled regular polygons

## Finding

For every integer \(n\ge3\), let \(G_n\subset\mathbb R^2\) be the regular \(n\)-gon inscribed in the unit circle, equipped with normalized uniform **area** measure. Let \(P_n\) be the real \(L^2(G_n)\)-orthogonal projector onto \(\operatorname{span}\{1,x_1,x_2\}\). Its exact Lebesgue constant is known from earlier all-polygon formulas, but the following **complete sharp threshold in side count** is the conclusion here:

\[
\boxed{\|P_n\|_{L^\infty\to L^\infty}>2\quad(3\le n\le6),\qquad
\|P_n\|_{L^\infty\to L^\infty}<2\quad(n\ge7).}
\]

Equivalently, if \(f\colon G_n\to[0,1]\) is measurable, the largest possible downward excursion of \(P_nf\), taken over \(f\) and points of \(G_n\), is greater than \(1/2\) exactly for triangles through hexagons, and is less than \(1/2\) for every regular polygon with at least seven sides. The sharp threshold is strict: no finite regular polygon in this family has norm exactly \(2\).

The equality \(\inf_{0\le f\le1}\min_x(P_nf)(x)=(1-\|P_n\|)/2\), the affine-kernel cap formula, the exact norms for all regular polygons, their vertex normers, and the previously proved polygon-to-disk coefficient \(5\pi\sqrt{15}/12\) are background results, **not** claimed as new here. The additional result is the global all-side-count comparison with the distinguished amplification value \(2\) and the resulting sharp positivity-defect boundary.

## Domain and notation

All polygons are filled, planar, regular, inscribed and carry area probability measure (not boundary arclength or discrete vertex measure). Only real affine orthogonal least squares is considered. Write
\[
q_n=\frac{2+\cos(2\pi/n)}{12},\quad k_n=1/q_n,\quad
A_n=\frac n2\sin(2\pi/n),\quad D_n=G_n\cap\{y_1<-q_n\}.
\]
Set \(C_n=-A_n^{-1}\int_{D_n}(1+k_ny_1)\,dy\). The established reproducing-kernel formula \(K_n(x,y)=1+k_n x\cdot y\), strict vertex norming, and normalization \(\int K_n(x,y)\,d\mu_n(y)=1\) yield \(\|P_n\|=1+2C_n\). Thus the new all-index comparison is equivalent to \(C_n>1/2\) for \(3\le n\le6\) and \(C_n<1/2\) for \(n\ge7\). This reformulation makes \(2\) a natural threshold: the maximum magnitude of a negative output from a unit-range nonnegative input is \(C_n\), and crossing \(1/2\) means it exceeds one-half of the input range.

## Proof of the sharp threshold

**Finite side counts.** The clipped-cap area and its horizontal first moment have the exact shoelace representation. If \(p_0,\ldots,p_{r-1}\) are the counterclockwise vertices of \(D_n\), including intersections of polygon edges with \(y_1=-q_n\), put \(\Delta_j=\det(p_j,p_{j+1})\) (cyclic indices). Then
\[
C_n=-\frac1{A_n}\left[\frac12\sum_j\Delta_j+
\frac{k_n}{6}\sum_j\Delta_j(p_{j,1}+p_{j+1,1})\right].
\]
Every coordinate is an explicit elementary trigonometric expression: for an edge \(a\to b\) that crosses \(y_1=-q_n\), the intersection is \(a+((-q_n-a_1)/(b_1-a_1))(b-a)\). In particular \(\|P_3\|=19/8\), \(\|P_4\|=233/108\), and \(\|P_6\|=361/180\), all above \(2\). The complete rigorous rational-interval certificate in the unchanged accompanying `check_polygon.py` computes the cap by this exact expression and proves \(C_n>1/2\) for each \(3\le n\le6\) and \(C_n<1/2\) for each \(7\le n\le11\). It uses Machin's arctangent formula and alternating-series enclosures for \(\pi\), Taylor bounds for sine/cosine, and exact rational shoelace arithmetic. The finite script certifies precisely these finitely many cases, not the unbounded tail.

**Uniform tail bound.** Let \(B(k)\) denote the negative-kernel mass of \(1+ky_1\) on the *uniform unit disk*. For \(k>1\), direct circular-segment integration yields
\[
B(k)=-\frac12+\frac{k^{-1}\sqrt{1-k^{-2}}+\arcsin(k^{-1})}{\pi}
+\frac{2k}{3\pi}(1-k^{-2})^{3/2}.
\]
Since \(G_n\) is contained in the unit disk and the negative-part integrand is nonnegative, \(C_n\le(\pi/A_n)B(k_n)\). As \(n\) increases, \(A_n\) strictly increases and \(k_n=12/(2+\cos(2\pi/n))\) strictly decreases. The function \(B(k)\) increases with \(k\), as is evident from its negative-part integral over the negative half-disk. Consequently, for every \(n\ge11\),
\[
 C_n\le\frac\pi{A_{11}}B(k_{11})<\frac12.
\]
The final strict numerical-looking inequality is also certified with **rational intervals** by the unchanged `check_polygon.py`: its `disk_upper_at_11()` bounds the square root and arcsine with explicit rational remainders. The computed value is approximately \(0.49790106\); its strict certified upper enclosure is below \(1/2\). Together with the finite cases, this settles every \(n\ge3\) and both strict sides of the threshold. No finite enumeration is extrapolated to infinite \(n\).

**Sharp positivity interpretation.** For a fixed point \(x\), the minimum of \((P_nf)(x)\) over \(0\le f\le1\) equals the integral of the negative part of \(K_n(x,\cdot)\), attained by the indicator of that negative set. Since \(\int K_n=1\), the minimum over points and inputs equals \((1-\|P_n\|)/2=-C_n\). The earlier vertex-norming theorem identifies the attaining evaluation points as polygon vertices. This standard reduction transfers the established strict threshold to the sign/size of worst-case downward overshoot, without asserting it as a separate new kernel theorem.

## Validation and limits

The unchanged standalone Python-standard-library `check_polygon.py` provides exact rational interval tests for the nine finite cases and the needed \(n=11\) disk majorant. The proof of the infinite tail depends on disk inclusion, monotonicity of \(A_n\) and \(k_n\), and the rigorously bounded \(n=11\) inequality, not on numerical samples. The theorem makes no assertion of monotonicity of \(\|P_n\|\) itself for all \(n\), no optimality over irregular polygons, and no analogous threshold for higher-degree or complex projections. Priority beyond the specifically inspected literature remains best-of-knowledge.

## Relationship to prior work

Earlier complete all-\(n\) norm and polygon-to-disk asymptotic formulas already appear in *Sharp affine projection norms on regular polygons and their disk-limit excess* (published October 18, 2026), *Sharp affine least-squares stability on regular polygons and its disk-limit defect* (October 25, 2026), and *Sharp affine least-squares projection norms on regular polygons and the disk-limit defect* (November 2, 2026). They provide the cap-moment formula, exact endpoint norms, vertex norming and the disk limit with second-order coefficient \(5\pi\sqrt{15}/12\). Those parts of the earlier broader claim are expressly excluded from the present novelty assertion. The new conclusion compares the entire infinite regular-polygon family with the fixed operator threshold \(2\), proves the exact transition between six and seven sides, and translates it to the half-range negativity defect. These comparisons do not follow from substituting a single parameter into the older closed formula; the global tail requires the disk majorant and a rigorous strict finite certificate. They remain a focused corollary of a previously known all-\(n\) formula, not a new formula for that norm.

The general theorem of Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424) concerns bounds for different projector spaces and provides no side-number boundary. As with any explicit formula, an equivalent inequality may be implicit in the earlier full-norm literature; this is the residual priority risk.

## References

- *Sharp affine projection norms on regular polygons and their disk-limit excess*, Resultary, 2026-10-18: https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-sharp-affine-projection-norms-on-regular-polygons-and-their-disk--d054d71b4597
- *Sharp affine least-squares stability on regular polygons and its disk-limit defect*, Resultary, 2026-10-25: https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-sharp-affine-least-squares-stability-on-regular-polygons-and-its--20ba7c1db388
- *Sharp affine least-squares projection norms on regular polygons and the disk-limit defect*, Resultary, 2026-11-02: https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-affine-least-squares-projection-norms-on-regular-polygons--ac0c9cd53708
- T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424 (2010).
