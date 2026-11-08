# Sharp side-count-uniform angular stability from short Crofton chords

## Finding
For every nondegenerate convex Euclidean \(m\)-gon \(K\), \(m\ge3\), with no collinear consecutive edges, perimeter \(P\), and exterior turning angles \(\alpha_1,\ldots,\alpha_m\in(0,\pi)\), let \(F_K(t)\) be the length distribution of the chord cut by a motion-invariant random unoriented line, conditioned on that line intersecting \(K\). Write
\[
q(a)=\frac{1-a\cot a}{2},\qquad a\in(0,\pi).
\]
There is an explicit \(t_0(K)>0\) such that, for all \(0\le t<t_0(K)\),
\[
F_K(t)=\frac{t}{P}\sum_{i=1}^{m}q(\alpha_i).
\]
The scale-free initial slope \(S(K)=P\lim_{t\downarrow0}F_K(t)/t\) satisfies the quantitative sharp inequality
\[
\boxed{S(K)-m q(2\pi/m)\ \ge\ \frac16\sum_{i=1}^m(\alpha_i-2\pi/m)^2.}
\]
Equality holds exactly for equiangular polygons. The coefficient \(1/6\) is optimal simultaneously for all side counts \(m\ge3\): no larger universal constant works. The already-known general polygon chord-integration formulas imply the local slope; the contribution asserted here is the sharp, side-count-uniform angular stability inequality, including its exact equality and sharpness classes.

## Assumptions and scope
A polygon is convex, compact, has nonempty interior, and has exactly \(m\) genuine vertices. Let its consecutive edges be \(E_i\), of positive lengths \(\ell_i\), and its interior angles \(\theta_i=\pi-\alpha_i\). Thus \(0<\alpha_i<\pi\), \(\sum_i\alpha_i=2\pi\), and \(P=\sum_i\ell_i\). Unoriented lines have parameters \(\ell_{\phi,p}=\{x\in\mathbb R^2:x\cdot(\cos\phi,\sin\phi)=p\}\), \(0\le\phi<\pi\), \(p\in\mathbb R\), with invariant measure \(d\phi\,dp\). The total mass of lines hitting \(K\) is exactly \(P\) by the Cauchy projection formula. Boundary-tangency lines have zero measure. All claims are invariant under Euclidean similarities.

An explicit positive validity radius is
\[
t_0(K)=\min\left\{\min_{E_i,E_j\text{ nonadjacent}}\operatorname{dist}(E_i,E_j),\quad
\min_{1\le i\le m}\sin\theta_i\min(\ell_{i-1},\ell_i)\right\},
\]
with the first minimum interpreted as \(+\infty\) if no nonadjacent edge pairs exist. The cyclic indexing has \(E_{i-1},E_i\) incident at vertex \(i\). In particular, \(t_0(K)>0\).

## Proof
**1. Short chords are vertex chords.** A chord of length \(t<t_0(K)\) cannot have its two endpoints on nonadjacent edges, because every pair of such edges is separated by at least the first quantity in \(t_0\). Nor can its endpoints lie on the same edge except for a null set of coincident supporting lines. Hence its endpoints lie on two edges meeting at a common vertex. These configurations are mutually disjoint outside measure-zero lines through vertices.

Fix a vertex with incident edge rays \(e_1,e_2\) at interior angle \(\theta\in(0,\pi)\). When the chord meets these rays at distances \(x,y\ge0\) from their common vertex, its length \(d=|xe_1-ye_2|\) obeys \(d\ge x\sin\theta\) and \(d\ge y\sin\theta\). Thus \(d<t_0(K)\) guarantees that both intersections are strictly inside their finite incident edges; no truncation by other vertices occurs.

**2. Exact local line measure.** The outward normal vectors to lines cutting both rays near this vertex form a normal sector of angular length \(\pi-\theta=\alpha\). Let \(\varphi\in(\theta-\pi/2,\pi/2)\), so that the positive incidence cosines are \(a=\cos\varphi\) and \(b=\cos(\theta-\varphi)\). At inward offset \(h\ge0\) from the supporting line through the vertex, the intersections are \(x=h/a\), \(y=h/b\), and elementary triangle geometry yields
\[
d=\frac{h\sin\theta}{ab}.
\]
Consequently, all short chords here correspond exactly to \(0\le h\le t ab/\sin\theta\). Their invariant line measure is
\[
\begin{aligned}
\mu_{\theta}(t)
&=\frac{t}{\sin\theta}\int_{\theta-\pi/2}^{\pi/2}\cos\varphi\cos(\theta-\varphi)\,d\varphi\\
&=\frac t2\bigl[1+(\pi-\theta)\cot\theta\bigr]
=tq(\alpha).
\end{aligned}
\]
Summing over all vertices and dividing by the total line measure \(P\) proves the exact initial distribution and the formula \(S(K)=\sum_i q(\alpha_i)\).

**3. Universal strong convexity.** Direct differentiation gives
\[
q''(a)=\frac{\sin a-a\cos a}{\sin^3 a}.
\]
Define \(g(a)=3(\sin a-a\cos a)-\sin^3 a\). Then \(g(0)=0\) and
\[
g'(a)=3\sin a\,[a-\sin a\cos a]>0\quad(0<a<\pi),
\]
since the bracket vanishes at zero and its derivative is \(2\sin^2 a>0\). Thus \(q''(a)>1/3\) on \((0,\pi)\), and \(\lim_{a\downarrow0}q''(a)=1/3\). Applying strong convexity at \(\bar a=2\pi/m\) gives
\[
q(\alpha_i)\ge q(\bar a)+q'(\bar a)(\alpha_i-\bar a)+\frac16(\alpha_i-\bar a)^2.
\]
The linear terms sum to zero because \(\sum_i\alpha_i=m\bar a\). This proves the displayed inequality. Strictness of \(q''>1/3\) shows equality if and only if all \(\alpha_i=\bar a\), precisely equiangularity.

**4. Optimality of the numerical constant.** For \(m=4k\), \(k\to\infty\), consider the closed unit-edge polygon with successive exterior turns
\[
\alpha_j=\frac{2\pi}{m}+\frac{(-1)^j}{m^2},\quad j=0,\ldots,m-1.
\]
These are positive, less than \(\pi\), and sum to \(2\pi\). Every block of \(m/2=2k\) successive turns has sum \(\pi\). Hence the edge direction at index \(j+m/2\) is opposite that at index \(j\); equal edge lengths yield closure. Their strictly increasing cyclic edge directions give a genuine convex centrally symmetric polygon. Taylor expansion at \(\bar a=2\pi/m\), with perturbations \(\pm m^{-2}\), shows
\[
\frac{\sum_j q(\alpha_j)-m q(\bar a)}{\sum_j(\alpha_j-\bar a)^2}
\longrightarrow \frac12\lim_{a\downarrow0}q''(a)=\frac16.
\]
Therefore a constant larger than \(1/6\) fails for this family.

## Verification
The included `verify.py` independently computes the local angular wedge integral, tests the strong-convexity differential inequality on a dense grid, and simulates invariant random lines intersecting four convex polygon shapes (square, rectangle, equilateral triangle, skew quadrilateral), comparing the observed short-chord frequencies with the exact predictions. Each simulation conditions on actually intersecting lines, rather than drawing uniformly from a direction-dependent chord family. Use `python verify.py` with NumPy installed. The analytic result is established by the preceding proof, not by numerical sampling.

## Relationship to prior work
Harutyunyan and Ohanyan (2009) give a convex-polygon chord integral formula and complete regular-polygon chord-length laws; in particular the local angle-dependent coefficient is recoverable from their general representation. Bäsel (arXiv:1204.2707, first submitted 2012-04-12) obtains complete regular-polygon chord laws and describes extensions of the method to irregular polygons. García-Pelayo (arXiv:1501.00292) gives formulas and algorithms for the **complete** chord distribution of arbitrary convex and nonconvex polygons, a stronger coverage of the *distribution calculation* than the local formula presented here. The new result is not the distribution formula, but the **side-count-uniform, optimally quantitative global angular stability** extracted from its local coefficient. The present statement does **not** claim to discover the local chord slope or the regular-polygon distributions. Its distinct assertion is a globally valid, sharp \(L^2\)-angular stability inequality for the initial Crofton chord slope over all convex polygons and all side counts, including the optimal constant \(1/6\), rigidity and sharpness sequence. Work on *interior-point pair distances* concerns a different probability measure and does not imply this chord statistic or its stability estimate. Gates (1982) studies shape recognition from chord-length distributions, an important related but only abstract-accessible source in this review.

## Limitations
The strong stability controls exterior-angle deviations, not deviations of side lengths, since even highly unequal equiangular polygons attain equality. The exact linear interval \([0,t_0(K))\) may be very short for nearly flat or closely spaced edges. The proof does not address smooth curves, anisotropically weighted line measures, or finite-sample statistical error. Earlier broad polygon chord formulas already contain the local slope; originality is restricted to the sharp uniform quantitative stability, and an inaccessible historical treatment might conceivably contain a comparable inequality.

## References
1. H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, Advances in Applied Probability 41 (2009), 358–366, DOI: 10.1239/aap/1246886615. General polygon integration in Sections 2–3.
2. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707 (first publicly submitted 2012-04-12), Acta Mathematica Universitatis Comenianae 83 (2014), 1–18.
3. R. García-Pelayo, *Computation of the multi-chord distribution of convex and concave polygons*, arXiv:1501.00292 (2015); full text examined.
4. J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873–879, DOI: 10.2307/3213843 (abstract and bibliographic record examined).
