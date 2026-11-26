# Endpoint laws for random hyperbolic cyclic-polygon area deficits

## Finding

In curvature \(-1\), sample \(n\ge3\) points independently and uniformly by arclength on a circle of radius \(R\). Let \(A_{n,R}\) be their convex hull area and \(M_{n,R}\) the maximum inscribed \(n\)-gon area on that circle. The unique maximizing vertex set modulo rotation is regular. Couple all radii using the same sampled angles. If \(G_1,\ldots,G_n\) are the successive positive angular gaps, starting at the first sample, \(G/(2\pi)\sim\operatorname{Dirichlet}(1,\ldots,1)\). For fixed \(n\), almost surely,
\[
e^R(M_{n,R}-A_{n,R})\longrightarrow Z=4\sum_i\cot(G_i/2)-4n\cot(\pi/n).
\]
The support of \(Z\) is \([0,\infty)\), with no atom at zero. Put \(d=n-1\) and \(H=\cos(\pi/n)/\sin^3(\pi/n)\). Then
\[
\Pr(Z>t)\sim\frac{4n(n-1)}{\pi t}\quad(t\to\infty),\qquad
\Pr(Z\le t)\sim K_n t^{d/2}\quad(t\downarrow0),\qquad
K_n=\frac{d!\,\pi^{d/2}}{(2\pi)^d\Gamma(1+d/2)\sqrt n\,H^{d/2}}.
\]
For **real** \(p\), \(\mathbb E[Z^p]<\infty\) exactly when \(-d/2<p<1\). In particular the first moment diverges.

Let \(I\) be the label of the shortest gap (a.s. unique) and let \(D\) be the vector of remaining gaps in cyclic order after that gap, divided by their sum. Conditional on \(Z>t\), the joint limit of \((I,tG_I/8,D,Z/t)\) is \((I_*,U,D_*,1/U)\). Here the first three entries are independent, uniform on the \(n\) labels, uniform on \((0,1)\), and Dirichlet\((1,\ldots,1)\) of length \(n-1\), respectively. The last entry has Pareto tail \(1/y\) for \(y\ge1\) and is not independent of \(U\). Conditional on \(Z\le t\), \((G-(2\pi/n)\mathbf1)/\sqrt t\) converges to normalized intrinsic volume on \(\sum u_i=0,\ H\sum u_i^2\le1\).

## Proof

**Geometry and gap law.** Rotating the first sampled angle to zero leaves the other \(n-1\) angles i.i.d. uniform, and their ordered spacings from 0 to \(2\pi\) give the stated Dirichlet law. In the Poincaré disk set \(r=\tanh(R/2)\), \(C=\cosh R\). The automorphism \(z\mapsto(z-r)/(1-rz)\) taking a vertex \(r\) to zero sends its neighbor at angle \(g\) to a point in the direction with real and imaginary parts proportional to \(((1+r^2)(\cos g-1),(1-r^2)\sin g)\). Thus for adjacent gaps \(g,h>0\) the interior angle is the sum of the principal arctangents \(\arctan(C^{-1}\cot(g/2))+\arctan(C^{-1}\cot(h/2))\). This sum is in \((0,\pi)\), since \(g+h<2\pi\) gives \(\cot(g/2)+\cot(h/2)>0\); the formula also applies to one gap larger than \(\pi\). Gauss–Bonnet gives the area as \(\sum_i F_C(G_i)\), where
\[
F_C(g)=\pi-g-2\arctan(C^{-1}\cot(g/2)),\qquad
F_C'(g)=\frac{C}{1+(C^2-1)\sin^2(g/2)}-1.
\]
For a pair \(s+h,s-h\) with \(s<\pi\) and \(h>0\), the difference in the two squared sines in the denominator is \(\sin s\sin h>0\), so averaging unequal gaps strictly increases area. \(F_C\) extends continuously to the closed interval with zero endpoint values. Averaging also improves a zero–positive pair with sum less than \(2\pi\) by the same derivative argument. The remaining boundary configurations with a single nonzero gap have zero area. Compactness now gives the unique regular maximum. For every fixed positive gap vector, \(e^R/C\to 2\) and \(\arctan x/x\to1\) give the claimed limit, using \(\sum_i G_i=2\pi\).

**Minimum and boundary control.** For the cotangent sum the same pair averaging strictly *decreases* the sum, since \(\frac d{dg}\cot(g/2)=-\tfrac12\csc^2(g/2)\). The sum diverges along every approach to the boundary: at a boundary point with no gap \(2\pi\), a vanishing gap contributes \(+\infty\) while negative terms are bounded below. If \(G_j=2\pi-s\to2\pi\), then
\[
\sum_i\cot(G_i/2)=2\sum_{i\ne j}1/G_i-2/s+O(s)\ \ge\ 2((n-1)^2-1)/s+O(s).
\]
This uses Cauchy–Schwarz and \(\cot(g/2)=2/g+O(g)\) at zero. Hence the regular vector is the unique minimum, with value zero for \(Z\), and small sublevel sets localize there. Continuity, connectedness and divergence give the full support, since the open simplex has positive density. The regular vector has measure zero.

**Upper endpoint.** Fix \(1/2<a<1\). The event of two gaps below \(t^{-a}\) has probability \(O(t^{-2a})=o(t^{-1})\), by the bounded two-coordinate marginal density for fixed \(n\ge3\). If all gaps exceed that threshold the positive cotangent terms are \(O(t^a)\). If exactly one, \(G_i\), is below it, all other cotangents are \(O(t^a)\) in absolute value: another gap is at least \(t^{-a}\) from both endpoints because at least one further gap is \(\ge t^{-a}\). Uniformly there, \(Z=8/G_i+O(t^a)\). Thus the events \(Z>t\) and \(\bigcup_i\{G_i<8/t\}\) differ by probability \(o(t^{-1})\): apart from two small gaps the discrepancy lies in windows of width \(O(t^{a-2})\) around \(8/t\). By \(G_i/(2\pi)\sim\operatorname{Beta}(1,n-1)\), \(\Pr(G_i<x)=(n-1)x/(2\pi)+O(x^2)\); summing proves the upper coefficient. For a fixed label \(i\), conditional on \(G_i<8/t\), \(tG_i/8\) tends to uniform on \((0,1)\); the normalized other gaps are exactly Dirichlet and independent of \(G_i\). The discarded cases have vanishing conditional probability. Exchangeability gives the independent uniform label, and \(Z/t-8/(tG_I)\to0\) in conditional probability, giving the joint limit including the Pareto excess.

**Lower endpoint and moments.** Write \(u_i=G_i-2\pi/n\). Taylor expansion gives \(Z=H\sum_i u_i^2+O(\|u\|^3)\), because the linear term sums to zero and the second derivative of \(g\mapsto\cot(g/2)\) is \(\cos(g/2)/(2\sin^3(g/2))\). In the free coordinates \(u_1,\ldots,u_d\) the quadratic form \(\sum_i u_i^2\) has matrix \(I_d+\mathbf1\mathbf1^\top\) of determinant \(n\). By localization and the positive quadratic term, the sublevel sets after dilation by \(t^{-1/2}\) are bounded and their indicators converge off the limiting ellipsoid boundary. The constant free-coordinate density \(d!/(2\pi)^d\) times the limiting ellipsoid volume gives \(K_n\), and normalized volumes give the conditional shape law. For \(p>0\), the tail integral \(p\int_0^\infty t^{p-1}\Pr(Z>t)\,dt\) converges precisely for \(p<1\). For \(p<0\), apply the positive-power formula to \(1/Z\) and use the lower tail to get \(-p<d/2\). Both critical moment integrals diverge logarithmically, and the zeroth moment equals one.

## Scope and relation to prior work

These are fixed-\(n\) endpoint laws after the large-radius limit, not uniform tail estimates jointly in \(t\) and \(R\). Deterministic hyperbolic cyclic-polygon area and radius formulas, including separate treatment of noncentered polygons, are studied in J. DeBlois, [The Geometry of Cyclic Hyperbolic Polygons](https://arxiv.org/abs/1101.4971). The distributional claim is the pair of sharp endpoint laws and their conditional configurations, not priority for cyclic-polygon geometry or Dirichlet spacings. The area tail on an expanding horocycle segment and the inradius tail on expanding circles concern different observables or sampling laws.
