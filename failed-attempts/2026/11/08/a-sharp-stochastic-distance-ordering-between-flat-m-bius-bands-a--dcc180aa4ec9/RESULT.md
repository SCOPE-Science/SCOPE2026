# A sharp stochastic-distance ordering between flat Möbius bands and cylinders

## Finding

For every \(a,b>0\), a flat Möbius band of length \(a\) and half-width \(b\) has a **strictly smaller intrinsic random point-pair distance** in first-order stochastic order than the flat cylinder obtained by *untwisted* gluing of the same rectangle. The comparison is exact at every distance scale. Although the two surfaces have the same area, total boundary length, and local Gaussian curvature, the difference in their distance distributions appears at exactly half the gluing length.

Write \(F_M(r)=\Pr(D_M\le r)\) and \(F_C(r)=\Pr(D_C\le r)\) for distances between independent area-uniform points in the respective surfaces. Put
\[
r_*=\frac a2,\qquad R_C=\sqrt{\frac{a^2}{4}+4b^2}.
\]
Then
\[
F_M(r)=F_C(r)\quad(0\le r\le r_*\ \text{or}\ r\ge R_C),
\qquad F_M(r)>F_C(r)\quad(r_*<r<R_C).
\]
Moreover the threshold is sharp to leading order:
\[
F_M\!\left(\frac a2+\varepsilon\right)-F_C\!\left(\frac a2+\varepsilon\right)
=\frac{4}{3b\sqrt a}\,\varepsilon^{3/2}+O_{a,b}(\varepsilon^2)
\quad(\varepsilon\downarrow0).
\]
Thus every positive distance moment is strictly smaller for the Möbius band than for the matched cylinder.

## Assumptions and scope

Let the rectangle be \(Q=[0,a]\times[-b,b]\) with its Euclidean metric, with \(a,b>0\). Its horizontal ends are identified by \((0,y)\sim(a,-y)\) for the Möbius band \(M_{a,b}\), and by \((0,y)\sim(a,y)\) for the cylinder \(C_{a,b}\). Each has the induced intrinsic length metric and normalized two-dimensional area measure. Distances may run through the interior and along the boundary; they are **not** distances in an embedding in three-space. Both surfaces have area \(2ab\), total boundary length \(2a\), and flat interiors.

Choose each pair of points independently according to normalized area. The two random experiments need not be coupled pointwise for the stochastic comparison. Define \(z_+=\max(z,0)\). For all \(r\ge0\) and \(t\in[0,a]\) set
\[
u_r(t)=\sqrt{(r^2-t^2)_+},\qquad
v_r(t)=\sqrt{(r^2-(a-t)^2)_+},\qquad
L_b(z)=1-\left(1-\frac{z}{2b}\right)_+^2.
\]

## Proof

**1. The geodesic reductions.** The infinite Euclidean strip \(\mathbb R\times[-b,b]\) is convex. All lifts of a geodesic endpoint lie in this strip, so minimizing intrinsic length is equivalent to finding the shortest Euclidean segment between one lift and a deck-transformed lift of the other. For two representatives \((x_1,y_1),(x_2,y_2)\in Q\), put \(t=|x_1-x_2|\). The nearest even and odd horizontal deck images in the Möbius case have horizontal separations \(t\) and \(a-t\), respectively. The corresponding vertical separations are \(|y_1-y_2|\) and \(|y_1+y_2|\). Hence
\[
D_M^2=\min\{t^2+(y_1-y_2)^2,\ (a-t)^2+(y_1+y_2)^2\}.
\]
For the untwisted cylinder both choices use the same vertical difference:
\[
D_C^2=\min\{t^2,(a-t)^2\}+(y_1-y_2)^2.
\]
Because \(x_1,x_2\) are independent uniform variables on \([0,a]\), \(t\) has density \(w(t)=2(a-t)/a^2\).

**2. Exact conditional distribution.** Let \(S=|y_1-y_2|\) and \(V=|y_1+y_2|\). The linear map \((y_1,y_2)\mapsto(y_1-y_2,y_1+y_2)\) carries the square \([-b,b]^2\) to the diamond \(|s|+|v|\le2b\), with constant density \(1/(8b^2)\). Thus the joint density of \((S,V)\) equals \(1/(2b^2)\) on the triangle \(S,V\ge0\), \(S+V\le2b\). For nonnegative \(u,v\),
\[
\Pr(S\le u\ \text{or}\ V\le v)
=1-\frac{(2b-u-v)_+^2}{4b^2}=L_b(u+v).
\]
The marginal law is \(\Pr(S\le z)=L_b(z)\), for every \(z\ge0\). Inserting the two distance formulas and integrating over \(t\) yields the **complete finite-radius laws**
\[
\boxed{F_M(r)=\int_0^a\frac{2(a-t)}{a^2}
L_b\!\big(u_r(t)+v_r(t)\big)\,dt,}
\]
\[
\boxed{F_C(r)=\int_0^a\frac{2(a-t)}{a^2}
L_b\!\big(\max\{u_r(t),v_r(t)\}\big)\,dt.}
\]
The nondecreasing function \(L_b\) is strictly increasing on \([0,2b)\). Because \(u+v\ge\max(u,v)\), these formulas immediately give \(F_M\ge F_C\) for every radius.

**3. Exhaustive equality and strictness regions.** If \(r\le a/2\), the intervals on which \(u_r\) and \(v_r\) are positive do not overlap, so the two integrands coincide pointwise. If \(a/2<r<R_C=\sqrt{a^2/4+4b^2}\), take \(t=a/2\). Then both \(u_r(t)\) and \(v_r(t)\) are positive and equal to \(\sqrt{r^2-a^2/4}<2b\); consequently \(L_b(u+v)>L_b(\max(u,v))\) on a positive-length neighborhood of \(t=a/2\). The weight \(w(t)\) is positive there, proving strict inequality. Finally, for \(r\ge R_C\), the smaller of \(t\) and \(a-t\) is at most \(a/2\), so \(\max(u_r(t),v_r(t))\ge2b\) for all \(t\). Both integrands are then one, and both distributions are one. These cases cover every radius.

**4. Sharp onset.** Write \(c=a/2\) and \(r=c+\varepsilon\). For sufficiently small \(\varepsilon>0\), the difference of the two integrands is supported in \(c-\varepsilon<t<c+\varepsilon\). In this window both \(u_r\) and \(v_r\) are \(O(\sqrt\varepsilon)\), and, using the polynomial branch of \(L_b\),
\[
L_b(u+v)-L_b(\max(u,v))
=\frac{\min(u,v)}{b}+O_{a,b}(\varepsilon).
\]
Uniformly in \(s\in[-1,1]\), setting \(t=c+\varepsilon s\) gives
\[
\min\{u_r(t),v_r(t)\}
=\sqrt{a\varepsilon}\,\sqrt{1-|s|}+O_a(\varepsilon^{3/2})
\]
(with a harmless integrated interpretation at the endpoints). Also \(w(c+\varepsilon s)=1/a+O_a(\varepsilon)\). The leading integral is therefore
\[
\frac{\sqrt a}{ab}\,\varepsilon^{3/2}
\int_{-1}^{1}\sqrt{1-|s|}\,ds
=\frac{4}{3b\sqrt a}\,\varepsilon^{3/2},
\]
and the remaining integrated terms are \(O_{a,b}(\varepsilon^2)\). The coefficient is positive for every \(a,b>0\).

**5. Consequence for moments.** Both distances have compact support. A strict cumulative-distribution gap on an open interval implies, by layer cake, \(\mathbb E[D_M^p]<\mathbb E[D_C^p]\) for every \(p>0\).

## Verification

The standalone file `mobius_cylinder_distance_check.py` uses only NumPy and SciPy. Run `python mobius_cylinder_distance_check.py`. It performs deterministic quadrature of both exact CDF integrals for four aspect ratios and 124 radius tests, checks the exact equality/strictness intervals, tests the leading threshold coefficient at three shrinking scales, and independently samples one million pairs of points (250,000 at each aspect ratio) using the two deck-transformation distance formulas. The resulting execution ends with `MOBIUS_CYLINDER_CHECK_OK`. This finite verification is supplementary: the argument above proves the complete inequalities for **all** positive parameters and radii.

## Relationship to prior work

El Mir and Yassine, *Conformal Geometric Inequalities on the Klein Bottle* (arXiv:1209.6202v1, September 27, 2012), provide a flat-quotient description of the Klein bottle and an induced flat Möbius band, and prove extremal conformal inequalities involving essential curves. The present theorem instead compares **two-point intrinsic distance laws** under normalized area and gives a sharp stochastic ordering with a nonanalytic onset.

Granata and Carnevale, *Accurate Estimation of the Intrinsic Dimension Using Graph Distances* (2016, PMCID: PMC4980871), discuss graph-approximated distances on a multiply twisted strip and compare its plotted behavior to a cylinder. Their study does not state the two exact one-dimensional quotient-distance formulas, their global strict ordering, or the \(3/2\) onset coefficient for the flat one-twist Möbius band.

## Limitations

This is a comparison of **matched rectangular flat quotients**: the same positive \(a,b\), normalized area measures, and intrinsic length metrics. It does not claim an ordering for arbitrary Riemannian metrics, embedded surfaces with extrinsic distances, arbitrary nonuniform sampling, or unmatched shapes. The conclusion has been checked against accessible primary literature and published mathematical search records, but historical priority has not been independently certified.

## References

1. C. El Mir and Z. Yassine, *Conformal Geometric Inequalities on the Klein Bottle*, arXiv:1209.6202v1 (first posted 2012-09-27), https://arxiv.org/html/1209.6202v1 .
2. D. Granata and V. Carnevale, *Accurate Estimation of the Intrinsic Dimension Using Graph Distances: Unraveling the Geometric Complexity of Datasets*, *Scientific Reports* **6**, 31377 (2016), https://pmc.ncbi.nlm.nih.gov/articles/PMC4980871/ .
