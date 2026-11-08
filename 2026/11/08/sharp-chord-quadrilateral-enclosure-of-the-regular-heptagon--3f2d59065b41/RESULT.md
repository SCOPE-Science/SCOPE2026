# Sharp chord-quadrilateral enclosure of the regular heptagon

## Finding
Let \(H\) be a Euclidean regular heptagon of circumradius one, and let \(q_{\mathrm{ch}}(H)\) be the smallest area of a convex polygon containing \(H\), with at most four sides, each parallel to a side or diagonal of \(H\). Put \(c=\cos(\pi/7)\). Then
\[
q_{\mathrm{ch}}(H)=c^2\left(\tan\frac{\pi}{7}+3\tan\frac{2\pi}{7}\right),\qquad
\frac{q_{\mathrm{ch}}(H)}{\operatorname{area}(H)}
=\frac{8c^2-1}{7(2c^2-1)}
=1.258803773547004\ldots .
\]
Exactly seven supporting quadrilaterals attain equality. Each is cut out by four lines containing sides of \(H\); the cyclic separations of these four side indices are \((1,2,2,2)\), in an arbitrary cyclic rotation. All seven are rotational images of one another. By affine invariance the ratio and optimizer classification also hold for affine-regular heptagons (with their chord directions mapped affinely).

## Assumptions and scope
The polygon \(H\) is the convex hull of \((\cos(2\pi j/7),\sin(2\pi j/7))\) for integers \(0\le j<7\). A chord joins two of these vertices; a chord quadrilateral has at most four sides, each parallel to a chord. The quantity \(q_{\mathrm{ch}}\) is **direction-restricted**. No assertion is made that its value equals the unrestricted minimum enclosing quadrilateral area \(q(H)\).

## Proof
**Finite reduction.** The normal to a chord joining vertices with arguments \(2\pi a/7\) and \(2\pi b/7\) has angle \((a+b)\pi/7\) modulo \(\pi\). Thus all chord-side normals are among
\[
n_j=(\cos(j\pi/7),\sin(j\pi/7)),\qquad 0\le j<14.
\]
The support number of \(H\) in direction \(n_j\) is \(h_j=1\) for even \(j\), and \(h_j=c\) for odd \(j\). A minimum-area enclosure can be taken with every side on one of these support lines: translating a nonsupporting side inward until contact cannot increase area, and strictly decreases area if that side has positive length. Since the seven-sided polygon \(H\) cannot coincide with a triangle, a bounded three-line enclosure can be strictly cut by another of the fourteen supporting halfplanes. Hence it suffices to consider four distinct support lines.

A four-normal choice \(0\le j_1<j_2<j_3<j_4<14\) is bounded if and only if its four cyclic gaps
\[
g_i=(j_{i+1}-j_i)\bmod 14,\qquad j_5=j_1,
\]
are all at most six. Their sum is fourteen. There are exactly 511 such choices. The halfplane intersections are actual (possibly degenerate) four-sided polygons containing \(H\); the supporting-line feasibility check below verifies every consecutive intersection against the other two halfplanes.

**Area formula.** Let \(\theta=\pi/7\), \(h_i=h_{j_i}\), and \(\delta_i=g_i\theta\). Solving consecutive pairs of supporting-line equations and applying the shoelace formula gives
\[
A(j_1,j_2,j_3,j_4)
=\frac12\sum_{i=1}^4
\frac{2h_i h_{i+1}-(h_i^2+h_{i+1}^2)\cos\delta_i}{\sin\delta_i}.
\]
All denominators are strictly positive because \(1\le g_i\le6\). This same identity follows from the support-number/edge-length formula \(2A=\sum_i h_i\ell_i\).

**Exact finite comparison.** Let \(T_m\) and \(U_m\) be Chebyshev polynomials, \(T_0=1\), \(T_1=z\), \(U_0=1\), \(U_1=2z\), and \(W_m=2zW_{m-1}-W_{m-2}\). Then
\[
\cos(g\theta)=T_g(c),\qquad \frac{\sin(g\theta)}{\sin\theta}=U_{g-1}(c).
\]
Consequently \(2\sin\theta\,A\) is a rational function of \(c\) in every one of the 511 cases. Moreover \(c\) is the unique root in \((9/10,91/100)\) of \(8c^3-4c^2-4c+1=0\). The strict rational interval
\[
\frac{9009688679024}{10^{13}}<c<\frac{9009688679025}{10^{13}}
\]
is certified by the cubic's endpoint signs and positive derivative. The standalone script `heptagon_cert.py` uses only exact rational interval arithmetic and this cubic relation to check **all 511** bounded configurations and all their support-line intersections; it does not use floating-point comparisons in any mathematical decision. The 14 exact-zero line-feasibility slacks are identified by reducing their numerator polynomials modulo the cubic.

The exhaustive comparison returns exactly seven minima, and these are precisely the four-odd-index sets with cyclic gap multiset \(\{2,4,4,4\}\). Every one of the other 504 candidates has strictly larger area; the exact rational interval lower bound on the gap in the scaled quantity \(2\sin\theta\,A\) is greater than \(0.02251624\). This is an **exhaustive finite proof**, not a sample or a numerical optimization heuristic: the complete candidate generation and sign certificates are in the included script.

**Attainment and simplification.** For the seven minimizing sets, all support numbers equal \(c\). Their normal gaps are one \(2\theta\) and three \(4\theta\). Hence the tangential-quadrilateral area formula yields
\[
A_{\min}=c^2\left(\tan\theta+3\tan 2\theta\right).
\]
Since \(\operatorname{area}(H)=\frac72\sin(2\theta)=7c\sin\theta\) and \(\tan2\theta=2c\sin\theta/(2c^2-1)\), division gives the stated rational expression in \(c\). Four odd-index normals are precisely four edge-supporting lines, and their normal gap multiset corresponds to the side-index gaps \((1,2,2,2)\). There are exactly seven rotations. No other enclosures tie, by the strict finite comparison.

## Verification
Run `python3 heptagon_cert.py` with a standard Python 3 interpreter. The reproducible exact certificate reports `HEPTAGON_CHORD_QUADRILATERAL_EXACT_OK`, 511 bounded configurations, seven minimizers, and fourteen algebraically zero feasibility slacks. It evaluates all possible chord-normal quadruples, rules out unbounded choices by their normal gaps, checks the feasibility of each consecutive supporting-line intersection and proves strict positive area differences for every nonoptimizer. The previously noted decimal approximation is independently recovered by substitution; it is not used to establish any sign.

## Relationship to prior work
Viktor Vígh, *A note on Kuperberg's quadrilateral conjecture* (first posted 2026-10-06, arXiv:2610.08168), introduces chord quadrilaterals and reports a numerical value \(1.2588\ldots\) at the affine-regular heptagon during optimization experiments. The present result proves an exact radical/trigonometric expression and completely classifies **all** minimum chord enclosures. The numerical observation and the general finite-candidate framework belong to Vígh and are not claimed as new. Fodor and Grundbacher (arXiv:2506.05185, first posted 2025-06-05) prove a universal upper bound for the unrestricted circumscribed-quadrilateral problem; it does not imply this exact restricted heptagon value or its minimizing directions. The classical pentagon case of Hong, Ismailescu, Kwak and Park (arXiv:2108.00326) concerns a different number of polygon vertices.

## Limitations
Only chord-direction-restricted quadrilateral enclosures of affine-regular heptagons are classified. The result does not evaluate the unrestricted \(q(H)\), establish optimality among all heptagons, or resolve Kuperberg's or Vígh's general conjectures. The finite exact certificate proves its stated 511-case classification without a hand-derived reduction to a smaller list of cases. Historical priority relative to specialist earlier geometric approximation literature is provisional; independent mathematical audit has not been performed.

## References
1. V. Vígh, *A note on Kuperberg's quadrilateral conjecture*, arXiv:2610.08168v1, first submitted 2026-10-06, https://arxiv.org/html/2610.08168v1.
2. F. Fodor and F. Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies*, arXiv:2506.05185v1, first submitted 2025-06-05, https://arxiv.org/html/2506.05185v1.
3. E. Hong, D. Ismailescu, A. Kwak, and G. Y. Park, *On the smallest area \((n-1)\)-gon containing a convex \(n\)-gon*, arXiv:2108.00326, first submitted 2021-07-31, https://arxiv.org/abs/2108.00326.
