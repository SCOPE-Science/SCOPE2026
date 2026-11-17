# Two limiting area-deficit moments reconstruct a triangle with known perimeter

## Finding

Fix a nondegenerate Euclidean triangle with side lengths \(a,b,c>0\), perimeter \(P=a+b+c\), and independently choose \(N\) points by uniform arclength from its entire boundary. Write \(\Delta_N\) for the area of the triangle minus the area of the convex hull of these points. Define the limiting moments
\[
\mu=\lim_{N\to\infty}N^2\mathbb E\Delta_N,
\qquad v=\lim_{N\to\infty}N^4\operatorname{Var}(\Delta_N).
\]
The existing boundary-polygon area-loss theorem ensures that these limits exist. **Given \(P\), the ordered pair \((\mu,v)\) determines the unordered triple \(\{a,b,c\}\) uniquely, hence the triangle up to Euclidean congruence.** An explicit inversion is
\[
R=\frac{P^3}{4\mu},\qquad S_2=\frac{P^2v}{3\mu^2},\qquad e_2=\frac{P^2-S_2}{2},
\]
\[
e_3=\sqrt{16P^2R^4+R^2(4P^2e_2-P^4)}-4PR^2,
\]
where \(R\) is the triangle's circumradius, \(e_2=ab+bc+ca\), and \(e_3=abc>0\). The side lengths are precisely the three positive real roots, with multiplicity, of
\[
z^3-Pz^2+e_2z-e_3=0.
\]
The number of limiting moments is **minimal**: the perimeter and \(\mu\) alone do not determine a triangle up to congruence. In addition, the ratio satisfies the sharp shape inequality
\[
\frac v{\mu^2}=\frac{3(a^2+b^2+c^2)}{P^2}\ge 1,
\]
with equality only for the equilateral triangle.

## Scope and relationship to established area-loss results

The inverse concerns the exact population moments of the \(N^2\)-rescaled missing area for one fixed, nondegenerate triangle, together with separately known perimeter. It is **not** a statement about moments of the area of one random inscribed triangle, about interior-uniform samples, or about statistical reconstruction from finitely many observed hulls. No stability guarantee as a triangle degenerates is asserted.

The boundary-sampled polygon law is **prior mathematics**, not a new claim here. In particular, *Angular product-exponential law for missed area of boundary-sampled polygons* (October 18, 2026) already establishes the full all-moment corner-product limit, and *An exponentially accurate perimeter–angle mean law for random boundary hulls* (October 25, 2026) establishes the all-order universal mean correction and the same limit. We explicitly use their established consequence: for a fixed polygon of perimeter \(P\), interior angles \(\alpha_i\), and independent standard exponentials \(E_i,F_i\),
\[
N^2\Delta_N\ \Longrightarrow\ \frac{P^2}{2}\sum_i\sin\alpha_i E_iF_i
\]
with all fixed positive integer moments converging. Consequently
\[
\mu=\frac{P^2}{2}\sum_i\sin\alpha_i,
\qquad v=\frac{3P^4}{4}\sum_i\sin^2\alpha_i.
\]
These are inputs to the inverse theorem. The sharper earlier result also gives
\(\mathbb E\Delta_N=\mu/((N+1)(N+2))+O(e^{-cN})\) for some \(c>0\). Neither this correction nor the product-exponential forward law is independently claimed as original here. Another published joint area/perimeter corner-law result establishes that the **full** area-loss distribution recovers the triangle similarity class; the distinct point addressed below is sufficiency and minimality of its **first two** limiting moments, with a constructive exact inverse.

## Proof of the inverse and optimality

Let \(R\) denote the circumradius. The sine law \(\sin\alpha_a=a/(2R)\), etc., applied to the previously established corner-law moments gives
\[
\mu=\frac{P^2}{2}\frac{a+b+c}{2R}=\frac{P^3}{4R},
\qquad
v=\frac{3P^4}{4}\frac{a^2+b^2+c^2}{4R^2}
=\frac{3P^4 S_2}{16R^2}.
\]
Therefore the formulas for \(R\), \(S_2\), and \(e_2\) in the Finding are exact. To recover the side product \(e_3=abc\), write \(A>0\) for the triangle's area. Heron's identity, rewritten via the elementary symmetric polynomials of \(a,b,c\), reads
\[
16A^2=-P^4+4P^2e_2-8Pe_3.
\]
The standard circumradius identity \(4RA=abc=e_3\) then yields
\[
e_3^2+8PR^2e_3-R^2(4P^2e_2-P^4)=0.
\]
The left-hand side is strictly increasing for \(e_3\ge0\). Because the input data arise from a nondegenerate triangle, it has the strictly positive solution \(abc\), so there is exactly one admissible positive solution. Solving this quadratic gives precisely the expression displayed in the Finding. The cubic determined by \((e_1,e_2,e_3)=(P,e_2,e_3)\) has roots \(a,b,c\), including any repeated roots. Thus the inverse is unique for all triangle shapes in the claimed domain, including equilateral, isosceles, and right triangles.

To show that just the first moment cannot suffice, fix the circumradius to \(R=1\) and consider isosceles triangles with apex angle \(2\arcsin t\), \(0<t<1\). Their two equal sides have length \(2\sqrt{1-t^2}\), their base length is \(4t\sqrt{1-t^2}\), and hence
\[
P(t)=4(1+t)\sqrt{1-t^2}.
\]
This function is strictly increasing on \((0,1/2)\) from \(4\) to \(3\sqrt3\), and strictly decreasing on \((1/2,1)\) from \(3\sqrt3\) to \(0\). Since \(4<5<3\sqrt3\), the equation \(P(t)=5\) has two distinct solutions on opposite sides of \(1/2\). The resulting noncongruent triangles have the same perimeter \(5\), circumradius \(1\), and therefore the same limiting mean \(\mu=5^3/4\). This proves minimality in the natural hierarchy of first two limiting moments.

Finally, dividing the two formulas above gives \(v/\mu^2=3S_2/P^2\). Cauchy–Schwarz implies \(3(a^2+b^2+c^2)\ge(a+b+c)^2\), with equality precisely when \(a=b=c\), establishing the sharp ratio and its rigidity.

## Exact diagnostic

For a \((3,4,5)\) triangle, \(P=12\), \(R=5/2\), and \(S_2=50\). The established forward moments are \(\mu=864/5\) and \(v=31104\). Substituting them into the explicit inverse gives \(e_2=47\), \(e_3=60\), and \(z^3-12z^2+47z-60=(z-3)(z-4)(z-5)\). This exact arithmetic check supports, but is not a replacement for, the preceding unrestricted proof. The original forward corner-gap checkers may independently corroborate the pre-existing limit law; they do not establish its historical originality.

## Limitations and priority

The result uses exact asymptotic mean and variance and a known perimeter; no finite-data statistical guarantee, numerically stable reconstruction near degeneracy, or higher-dimensional analogue follows. The underlying polygonal product-exponential limit and exponentially accurate finite-sample expectation are published previously and expressly credited. The two-moment inverse is a constructive specialization of a previously known distributional angle signature; although no checked earlier source supplied this particular low-order inverse, a historical equivalent algebraic reconstruction cannot be excluded without an exhaustive literature review.

## References

1. *Angular product-exponential law for missed area of boundary-sampled polygons*, published October 18, 2026, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-angular-product-exponential-law-for-missed-area-of-boundary-samp--bf3dbf28911a .
2. *An exponentially accurate perimeter–angle mean law for random boundary hulls*, published October 25, 2026, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-an-exponentially-accurate-perimeter-angle-mean-law-for-random-bo--377791ac0736 .
3. *Boundary-sampled polygon deficits: a joint corner law and an inverse angle signature*, published November 8, 2026, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-boundary-sampled-polygon-deficits-a-joint-corner-law-and-an-inve--fb04d21cf191 .
4. M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (2019), *Discrete & Computational Geometry* **69** (2023), 453–504, https://arxiv.org/abs/1911.05917 .
