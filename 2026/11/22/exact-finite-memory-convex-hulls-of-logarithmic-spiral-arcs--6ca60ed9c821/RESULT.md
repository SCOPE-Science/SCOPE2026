# Exact finite-memory convex hulls of logarithmic spiral arcs

## Finding
For every \(a>0\) and \(T>0\), the convex hull of \(\gamma_a(t)=e^{at}(\cos t,\sin t)\), \(0\le t\le T\), has a boundary containing only the last \(h=\min\{T,\ell(a)\}\) radians of spiral, and one closing chord. The finite contact memory \(\ell(a)\in(\pi,2\pi)\) is the unique solution of
\[
e^{a\ell}(\cos\ell-a\sin\ell)=1.
\]
Write \(q=e^{-ah}\), \(Q=\sqrt{1+a^2}\) and \(d=\sqrt{1+q^2-2q\cos h}\). The exact perimeter and area are
\[
P_a(T)=e^{aT}\left[\frac Qa(1-q)+d\right],\qquad
A_a(T)=e^{2aT}\left[\frac{1-q^2}{4a}-\frac{q\sin h}{2}\right].
\]
After normalization \(p_a(T)=e^{-aT}P_a(T)\) and \(b_a(T)=e^{-2aT}A_a(T)\), both functions become exactly constant for \(T\ge\ell(a)\). Yet their contact is nonanalytic: as \(\delta\downarrow0\),
\[
p_a(\ell)-p_a(\ell-\delta)=\frac{Qe^{-a\ell}}6\delta^3+O_a(\delta^4),
\]
\[
b_a(\ell)-b_a(\ell-\delta)=\frac{e^{-a\ell}(1+a^2)(-\sin\ell)}4\delta^2+O_a(\delta^3).
\]
Thus normalized perimeter is \(C^2\) but not \(C^3\), and normalized area is \(C^1\) but not \(C^2\) at the first loss of an earlier visible spiral point. The lag \(\ell(a)\) strictly decreases from \(2\pi\) to \(\pi\) as \(a\) increases from zero to infinity.

## Assumptions and scope
All convex hulls, areas and perimeters use the ordinary Euclidean metric in \(\mathbb R^2\). The parameter \(a\) is fixed and strictly positive, and the finite domain of \(\gamma_a\) is the closed interval \([0,T]\). The boundary arc is understood as one regular curve and the chord has length zero only in an excluded degenerate limit. No claim is made for negative pitch, arbitrary spiral perturbations, or sampled vertices.

## Proof
**1. Unique lag.** Put \(g_a(s)=e^{as}(\cos s-a\sin s)\). Direct differentiation gives
\[
g'_a(s)=-(1+a^2)e^{as}\sin s.
\]
Thus \(g_a\) decreases strictly on \((0,\pi)\), then increases strictly on \((\pi,2\pi)\), with \(g_a(0)=1\), \(g_a(\pi)=-e^{a\pi}\), \(g_a(2\pi)=e^{2\pi a}>1\). There is exactly one root \(\ell\in(\pi,2\pi)\) of \(g_a(\ell)=1\), and \(g_a(s)<1\) for \(0<s<\ell\).

**2. Supporting tangents.** The oriented tangent of \(\gamma_a(t)\) has direction \((a\cos t-\sin t,a\sin t+\cos t)\). Its inward-side cross product with \(\gamma_a(t+w)-\gamma_a(t)\), divided by the positive number \(e^{2at}\), equals \(e^{aw}(\cos w-a\sin w)-1=g_a(w)-1\) up to a fixed sign convention. For forward displacement \(0<w<\ell\) this is strictly negative. For backward displacement \(w=-s<0\), the expression is \(e^{-as}(\cos s+a\sin s)-1<0\) for every \(s>0\): on each half-turn it has extremal values only at integer multiples of \(\pi\), and the positive even multiples have value \(e^{-2\pi ak}<1\). Consequently every point in the terminal arc \([T-h,T]\) is supported by its tangent against all older and newer spiral points, hence appears exposed on the hull boundary (apart from the two chord endpoints).

**3. All older points are screened.** For any unit normal \(n=(\cos\phi,\sin\phi)\), the projection is \(f(t)=e^{at}\cos(t-\phi)\). Local maxima, whenever they occur, repeat every \(2\pi\), and the later one's value is greater by \(e^{2\pi a}\), since each local maximum is positive. Accordingly any global maximum over \([0,T]\) lies at the endpoint \(T\), at the initial endpoint \(0\), or at the last interior maximum. For a last interior maximum \(t=T-s\) with \(s\in[\ell,2\pi)\), its normal is the outward tangent-normal at that spiral point. The endpoint's projection exceeds or equals this local maximum precisely when \(g_a(s)\ge1\), which holds for \(s\ge\ell\). If no latest maximum occurs within the terminal interval, all earlier local maxima are dominated by this comparison or by an even later maximum. Finally, the tangent at \(t=0\) is not supporting once \(T>\ell\), by \(g_a(\ell+\eta)>1\) for small \(\eta>0\). Hence every support face belongs to the terminal arc or the segment connecting its endpoints. Together with Step 2 this proves the claimed complete boundary decomposition; the case \(T\le\ell\) follows directly from Step 2.

**4. Intrinsic volumes.** The arc speed is \(Qe^{at}\). Integrating from \(T-h\) to \(T\) and adding the direct Euclidean distance between endpoints gives the displayed perimeter formula. Green's formula along the counterclockwise spiral arc gives \(\frac12\int e^{2at}\,dt=(e^{2aT}-e^{2a(T-h)})/(4a)\). Adding the oriented closing chord contributes \(-\frac12e^{2aT-ah}\sin h\), yielding the area formula.

**5. Contact regularity.** On \(T<\ell\) substitute \(h=T\), differentiate the two explicit expressions, and use \(\cos\ell-a\sin\ell=e^{-a\ell}\). This gives \(p'_-(\ell)=p''_-(\ell)=0\), \(p'''_-(\ell)=Qe^{-a\ell}>0\), while \(b'_-(\ell)=0\) and \(b''_-(\ell)=\tfrac12e^{-a\ell}(1+a^2)\sin\ell<0\). Taylor's theorem yields both claimed deficits. For \(T>\ell\), \(h\) is constant, so the normalized quantities have all positive-order derivatives zero. Their asserted exact differentiability follows.

**6. Pitch dependence.** Implicit differentiation of \(g_a(\ell(a))=1\) gives a negative derivative: \(\partial_a g_a(\ell)=\ell+a\)-dependent positive factor, more precisely \(\partial_a g_a(\ell)=\ell-e^{a\ell}\sin\ell>0\), and \(\partial_s g_a(\ell)=-(1+a^2)e^{a\ell}\sin\ell>0\). Hence \(\ell'(a)<0\). The root equation and monotonicity imply limits \(\ell\to2\pi\) as \(a\downarrow0\), and \(\ell\to\pi\) as \(a\uparrow\infty\).

## Verification
The accompanying self-contained `checker.py` samples the spiral, constructs Euclidean polygonal convex hulls, integrates the closed expressions, and independently compares support maxima for numerous normals. Run `python3 -S checker.py`. It reports 40 polygonal hull comparisons and 600 support comparisons passed. These finite checks are diagnostics and not the proof; the infinite-domain support argument and differentiability derivations above are analytic.

## Relationship to prior work
The logarithmic spiral's exponential radial law, equiangular tangent geometry, and elementary arc-length calculation are classical. Anatriello and Vincenzi (2016) study related continuous/discrete triangle-chain geometry of logarithmic spirals but not the finite-arc convex-hull boundary decomposition or its terminal-contact regularity. Ghomi's later sphere-containing shortest-curve work uses spiral-type convex-hull constructions for a different extremal problem. Previously identified convex-hull formulas for an Archimedean spiral concern a radially *linear*, not exponential, growth law; its tail length is not a pitch-dependent constant and does not imply the present exact self-similar finite-memory property.

## Limitations
This work does not prove a universal finite-memory theorem for all spirals or establish priority beyond the sources inspected. In particular, obscure historical equiangular-spiral convexification results may contain related formulas. Numerical tests cannot replace the analytic proof. No independent mathematical audit has been performed.

## References
- Anatriello and Vincenzi, *Logarithmic Spirals and Continuous Triangles*, Journal of Computational and Applied Mathematics, DOI: 10.1016/j.cam.2015.09.004, lawful full-text manuscript at https://www.iris.unisa.it/retrieve/e2915b35-5525-8981-e053-6605fe0a83a3/JCAM%20Spirals%20and%20triangles%20Editing%20version%20%281%29.pdf.
- *Variational Formulation of Log-Aesthetic Surface*, arXiv:1304.7852 (2013-04-30), introductory logarithmic-spiral context, not a source for this convex-hull result.
- Ghomi, *Shortest closed curve to contain a sphere in its convex hull*, Bulletin of the London Mathematical Society (2024), DOI: 10.1112/blms.13066, different convex-hull spiral context.
- *Logarithmic spiral*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Logarithmic_spiral (classical definitions).
