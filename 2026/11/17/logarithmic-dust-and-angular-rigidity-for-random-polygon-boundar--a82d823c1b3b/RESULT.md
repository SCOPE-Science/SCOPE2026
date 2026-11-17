# Logarithmic dust and angular rigidity for random polygon-boundary cuts

## Finding
Let \(K\subset\mathbb R^2\) be a fixed convex polygon with \(m\ge3\) genuine sides, positive area \(A\), perimeter \(P\), interior angles \(\alpha_i\in(0,\pi)\), and incident side lengths \(a_i,b_i>0\) at vertex \(i\). Independently sample \(X,Y\) uniformly by arclength on \(\partial K\). The chord \([X,Y]\) cuts \(K\) into two (possibly zero-area) pieces; let \(M\) be the smaller area. Then \(\Pr(M=0)=\sum_{i=1}^m\ell_i^2/P^2\), where \(\ell_i\) are the side lengths. For \(s\downarrow0\), **excluding this atom**, the following two-term expansion holds:

\[
\Pr(0<M<s)=\frac{4s}{P^2}\sum_{i=1}^m\frac{1}{\sin\alpha_i}
\left[1+\log\left(\frac{a_i b_i\sin\alpha_i}{2s}\right)\right]+O_K(s^2).
\tag{1}
\]

In particular, for the scale-invariant statistic \(W=M/P^2\),
\[
\lim_{\varepsilon\downarrow0}
\frac{\Pr(0<W<\varepsilon)}{\varepsilon\log(1/\varepsilon)}
=H(K):=4\sum_{i=1}^m\csc\alpha_i.
\tag{2}
\]
Thus the leading nonzero small-fragment frequency depends *only* on the polygon's interior angles, not its individual side lengths. Put \(\bar\alpha=(m-2)\pi/m\). The coefficient has a globally sharp angular rigidity bound:
\[
H(K)\ge \frac{4m}{\sin(2\pi/m)}
+2\sum_{i=1}^m(\alpha_i-\bar\alpha)^2.
\tag{3}
\]
Equality holds exactly when all interior angles are equal. The coefficient \(2\) on the angular variance cannot be increased uniformly over all side counts and convex polygons.

There is also an explicit **joint total-variation law** for the geometry of small nonzero fragments. With probability tending to one conditioned on \(0<M<s\), the small piece is a corner triangle at a unique vertex \(I\). Its limiting corner weights are
\[
\Pr(I=i\mid 0<M<s)\longrightarrow
\frac{\csc\alpha_i}{\sum_j\csc\alpha_j}.
\tag{4}
\]
Let \(x\in(0,a_i)\) and \(y\in(0,b_i)\) be distances from that vertex to the two endpoints, measured along the incident sides, and put
\[
Q=\frac{\log(a_i/x)}{\log(a_i/x)+\log(b_i/y)},
\qquad Z=M/s.
\]
Together with the fair orientation label indicating which sampled endpoint lies on which incident side, the conditional law of \((I,Q,Z,\text{orientation})\) converges in total variation to the product of the corner weights (4), two independent uniform variables on \((0,1)\), and a fair binary label.

For a triangle, an additional **exact complete law** holds. If \(q=1-\sum_i\ell_i^2/P^2\), then for every \(0<s<A/2\), with \(z=s/A\),
\[
\Pr(0<M<s)=q\left[z(1-\log z)+z+(1-z)\log(1-z)\right].
\tag{5}
\]
The triangle's nonzero normalized small-fragment distribution thus depends on its shape only through the probability \(q\) of endpoints on different edges.

## Assumptions and scope
The polygon is full-dimensional and convex, with no consecutive collinear sides and no zero side lengths. The law is **independent perimeter endpoints**, not Crofton-invariant lines and not a perimeter point with independently uniform outgoing angle. Points falling exactly at vertices have probability zero. A chord whose endpoints fall on the same side coincides with a boundary segment and is assigned smaller area zero. All probabilities in (1)–(5) involving \(0<M<s\) exclude this genuine atom. The constants in \(O_K(s^2)\) may depend on the fixed polygon, including its smallest angles and edges; nothing is asserted uniformly for degenerating polygons.

## Proof
**1. Zero-area atom and edge allocation.** Independent arclength sampling assigns probability \(\ell_i^2/P^2\) to both endpoints landing on the same side \(i\). In that case the chord is contained in the boundary, giving \(M=0\). Conversely, a chord between two different genuine sides has positive smaller area almost surely. Summing disjoint side-pair events proves the atom.

**2. A corner's exact product-area calculation.** Consider the two sides meeting at vertex \(i\), and let \(x\in[0,a_i]\), \(y\in[0,b_i]\) be distances along them. The triangle cut off at that corner has area \(c_i xy\), where \(c_i=\sin\alpha_i/2\). For \(0<t<a_i b_i\), elementary integration gives the exact parameter-domain area
\[
\int_0^{a_i}\int_0^{b_i}\mathbf1_{\{xy<t\}}\,dy\,dx
=t\left[1+\log\left(\frac{a_i b_i}{t}\right)\right].
\tag{6}
\]
There are two endpoint orders, each with density \(P^{-2}\). Inserting \(t=s/c_i=2s/\sin\alpha_i\) gives the \(i\)-th summand in (1) exactly. When \(s<A/2\), the event \(c_i xy<s\) always makes the corner triangle itself the smaller piece.

**3. All other small fragments have probability \(O_K(s^2)\).** For two endpoints on nonincident sides, the continuous smaller-area function can vanish only when they approach the endpoints of a *single intervening polygon side*, so that their chord approaches that side. Near each such configuration, the area of the narrow cap has positive first-order coefficients in both endpoint displacements, proportional to the intervening side length and the sines of its two exterior turning angles. Thus a fragment smaller than \(s\) forces both nonnegative endpoint displacements to be \(O_K(s)\); the parameter area is \(O_K(s^2)\). Compactness away from the finitely many configurations bounds the fragment area below. For endpoints on incident sides, the only additional small-piece configuration can occur in the triangular case, when the *complement* of their corner triangle becomes small. In normalized edge-distance variables \(U,V\) independent uniform on \((0,1)\), its area is \(A(1-UV)\), so \(\Pr(1-UV<s/A)=O((s/A)^2)\). For polygons with four or more vertices, the complement of any corner triangle on two incident full sides has positive minimum area. Summing finitely many edge allocations proves (1), including its order-\(s\) term and the claimed remainder.

**4. The marked conditional limit, with an explicit local density.** Conditional on both endpoints occupying a specified pair of incident sides, write \(x=a_i e^{-u}\), \(y=b_i e^{-v}\). Their normalized logarithmic gaps \(u,v\) are independent \(\operatorname{Exp}(1)\) random variables. The small-corner event is \(u+v>T_i\), with
\[
T_i=\log\left(\frac{a_i b_i\sin\alpha_i}{2s}\right)\longrightarrow\infty.
\]
The classical Gamma–Dirichlet change of variables shows that \(Q=u/(u+v)\) is **exactly uniform on \((0,1)\)**, independent of \(u+v\), even after the threshold condition. Moreover \(Z=e^{-(u+v-T_i)}\) has the exact conditional density
\[
f_{i,s}(z)=\frac{T_i-\log z}{T_i+1},\quad 0<z<1.
\tag{7}
\]
Its total-variation distance to a uniform variable is exactly \(1/[e(T_i+1)]\). The corner probability is proportional to \(\csc\alpha_i(T_i+1)\), which converges to (4); endpoint orientation is independently fair. The \(O_K(s^2)\) exceptional probability from Step 3, divided by the leading \(s\log(1/s)\) mass, tends to zero. These finite-mixture and density estimates prove convergence of the entire marked law in total variation, not merely weak convergence.

**5. Sharp angle rigidity.** For \(0<t<\pi\), \(g(t)=\csc t\) satisfies \(g''(t)=\csc t(1+2\cot^2 t)\ge1\). By Taylor's theorem with integral remainder, \(g(t)\ge g(\bar\alpha)+g'(\bar\alpha)(t-\bar\alpha)+(t-\bar\alpha)^2/2\). The polygon angle-sum identity \(\sum_i\alpha_i=m\bar\alpha\) cancels the linear terms. Multiply by four to obtain (3). Strict convexity gives equality only when all angles agree. For a sequence of rhombi with angles \(\pi/2\pm\delta\), as \(\delta\to0\), the quotient of the excess in (3) by \(\sum_i(\alpha_i-\bar\alpha)^2\) tends to \(2\), proving global optimality.

**6. The exact triangle distribution.** A triangle's every pair of distinct edges meets at one vertex; the corner triangle area is \(AUV\), where \(U,V\) are independent uniforms, regardless of side lengths. Its complementary area is \(A(1-UV)\). Since the two events \(UV<z\) and \(UV>1-z\) are disjoint for \(0<z<1/2\), and \(\Pr(UV\le z)=z(1-\log z)\), multiplying by the probability \(q\) of distinct-edge sampling gives (5).

## Verification
The standalone script `verify_polygon_fragments.py` calculates polygon areas and interior angles from vertices, independently samples perimeter endpoints, constructs the smaller cut area from the boundary path and shoelace formula, compares observations to (1) and the atom, checks the exact triangle expression (5), verifies the explicit density (7) and its total-variation formula by quadrature, and tests the sharp rhombus stability quotient. Run `python3 verify_polygon_fragments.py`; the terminal success marker is `BOUNDARY_FRAGMENT_CHECKS_OK`. Numerical tests provide finite-sample corroboration, not an infinite proof; Steps 1–6 give the analytic argument.

## Relationship to prior work
Parisio and Dias (2011) study mass distributions of minimally fragmented rectangular plates. Their sampling mechanism chooses one uniform perimeter starting point and a **uniform outgoing angle**, giving a square-root dust law, not two independent arclength endpoints. Dias and Parisio (2014) extend that protocol to regular polygonal plates. Both full texts were inspected (2011 in openly accessible HTML, 2014 in its open PDF). Their square-root exponent and angle sampling do not imply the logarithmic boundary-endpoint law (1), its marks or its rigidity inequality (3). Bäsel (2012) uses motion-invariant random *lines* and analyzes chord **length** in regular polygons and interior-point distances; its complete full-text treatment does not calculate cut-off area for independently sampled boundary endpoints. A published invariant-line small-fragment result likewise has a square-root exponent under its distinct measure. Another published endpoint-sampled polygon result gives a small **chord-length** expansion, not the cut-off-area statistic. Neither alternative measure nor chord length alone supplies (1)–(5). Existing random boundary-hull area-deficit laws involve multiple sampled points and product-exponential corner gaps, not the two-endpoint cut partition. These similarities motivate the contrast but do not constitute a complete literature-exhaustiveness certificate.

## Limitations
Only fixed planar convex polygons with genuine vertices are considered. In the atom-free event, the two-term formula has a shape-dependent \(O_K(s^2)\) remainder, and the total-variation limit has no uniform rate over degenerating polygons. The coefficient determines an angular sum, not the full polygon. No claim is made for smooth boundaries, dependent endpoint sampling, invariant-line cuts, or a uniform-in-side-count polygon-to-circle limit. Historical priority is established only relative to the specifically checked sources; unindexed or inaccessible geometric-probability results remain a risk. Independent mathematical validation has not been performed.

## References
1. F. Parisio and L. Dias, *Minimal fragmentation problem*, arXiv:1109.2006, first publicly posted 2011-09-09, https://arxiv.org/abs/1109.2006 . Open full text inspected via the arXiv-accessible article representation.
2. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted 2012-04-12, https://arxiv.org/abs/1204.2707 ; author-published journal PDF, https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/download/71/18/ . Full text inspected.
3. L. Dias and F. Parisio, *Minimal Fragmentation of Regular Polygonal Plates*, arXiv:1404.6106, first posted 2014-04-24, https://arxiv.org/pdf/1404.6106 . Full text inspected.
4. *Sharp Crofton dust coefficient for convex polygons and its parallelogram extremum*, publicly available mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-crofton-dust-coefficient-for-convex-polygons-and-its-paral--95feff9c2a54 . Complete result inspected, using motion-invariant random lines.
5. *Exact short-chord laws and sharp angular rigidity for convex polygon boundaries*, publicly available mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-short-chord-laws-and-sharp-angular-rigidity-for-convex-pol--6aa43036918b . Complete result inspected, using endpoint-sampled chord length.
