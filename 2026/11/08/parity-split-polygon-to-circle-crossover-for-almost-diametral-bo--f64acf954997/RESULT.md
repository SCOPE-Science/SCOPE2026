# Parity-split polygon-to-circle crossover for almost-diametral boundary chords

## Finding
Let \(P_n\) be the regular Euclidean \(n\)-gon of circumradius one, for an integer \(n\ge3\). Sample \(X_n,Y_n\) independently and uniformly by arclength from its entire boundary, and write \(D_n=\lVert X_n-Y_n\rVert_2\). Define
\[
q(x)=\operatorname{dist}(x,\mathbb Z),\qquad f(x)=2q(x)(1-q(x)),\qquad \sigma_n=\begin{cases}0,&n\text{ even},\\1/2,&n\text{ odd}.\end{cases}
\]
For \(\sigma\in\{0,1/2\}\) and \(t\ge0\), set
\[
G_\sigma(u,v)=f(u)+f(u+\sigma+v)+v^2,\qquad H_\sigma(t)=\int_0^1\int_{\mathbb R}{\bf1}\{G_\sigma(u,v)<t\}\,dv\,du.
\]
Then along either parity subsequence, for every fixed real \(t\ge0\),
\[
\boxed{\lim_{\substack{n\to\infty\\\sigma_n=\sigma}} n\,\Pr\left(D_n>2-\frac{\pi^2t}{n^2}\right)=H_\sigma(t).}
\]
The limiting functions are continuous and nondecreasing. They exhibit two distinct onsets:
\[
\boxed{H_0(t)\sim\frac{t^2}{2}\quad(t\downarrow0),\qquad H_{1/2}(t)=0\quad(0\le t\le1/4),\qquad H_{1/2}(1/4+\eta)\sim\frac{16}{9}\eta^2\quad(\eta\downarrow0).}
\]
Both join the circular scale at large argument:
\[
\boxed{2\sqrt{t-1}\le H_\sigma(t)\le2\sqrt t\quad(t\ge1),\qquad H_\sigma(t)=2\sqrt t+O(t^{-1/2}).}
\]
In particular, the same geometric refinement has a parity-specific near-diameter threshold and a common large-threshold square-root envelope. For odd \(n\), the exact diameter is \(2\cos(\pi/(2n))\), with scaled deficit tending to \(1/4\).

## Assumptions and scope
The polygon's circumradius is exactly one; scaling a polygon of radius \(R>0\) multiplies all distances and thresholds by \(R\). Endpoints are selected independently from **normalized boundary arclength**, rather than interior area, the vertex set, a random offset line, or a random center-passing line. The limit takes \(n\to\infty\) along an even or odd subsequence while holding \(t\) fixed. The displayed small-\(t\) and large-\(t\) statements are properties of the limiting integral, not uniform two-variable error estimates for finite polygons. The onset equivalences mean positive asymptotic ratios.

## Proof
**1. An exact arclength coordinate.** Put \(\alpha=\pi/n\). Measure angular position around the polygon in units of one side-normal spacing, using \(u\in[0,n)\) and planar polar angle \(2\pi u/n\); translate the origin of \(u\) so the side normals occur at integers. Then the radial boundary coordinate and normalized arclength density are exactly
\[
r_n(u)=\frac{\cos\alpha}{\cos(\alpha(1-2q(u)))},\qquad \Pr(u\in du)=\frac{w_n(u)}{n}\,du,\qquad w_n(u)=\frac{\pi\cot\alpha}{n}\sec^2\!\bigl(\alpha(1-2q(u))\bigr).
\]
Indeed a side at support distance \(\cos\alpha\) has radial intersection \(\cos\alpha/\cos\theta\). Along the side, arclength differentiation gives \(ds=\cos\alpha\sec^2\theta\,d\theta\); division by perimeter \(2n\sin\alpha\) yields the formula for \(w_n\). The periodic functions obey, uniformly in \(u\),
\[
w_n(u)=1+O(n^{-2}),\qquad \frac{n^2}{\pi^2}(1-r_n(u))=f(u)+O(n^{-2}).
\]
The second uniform expansion follows by expanding the cosines: \((1-(1-2q)^2)/2=2q(1-q)\).

**2. Opposite-point parametrization.** Write the first endpoint coordinate as \(u\) and the second as \(u+n/2+v\), with \(-n/2\le v<n/2\). Since one period is one side-normal spacing, averaging the first coordinate over \([0,n)\), then using periodicity, gives the exact formula
\[
\begin{aligned}
n\Pr\left(D_n>2-\pi^2t/n^2\right)
=\int_0^1\int_{-n/2}^{n/2} &w_n(u)w_n(u+\sigma_n+v)\\
 &\quad\times {\bf1}\left\{D_n(u,v)>2-\pi^2t/n^2\right\}\,dv\,du.
\end{aligned}
\]
The angular separation is \(\pi+2\pi v/n\). For \(v\) in a fixed compact set, the cosine law gives
\[
D_n(u,v)^2=r_n(u)^2+r_n(u+\sigma_n+v)^2+2r_n(u)r_n(u+\sigma_n+v)\cos(2\pi v/n).
\]
Thus, uniformly on compact \(v\)-ranges and all \(u\in[0,1]\),
\[
\frac{n^2}{\pi^2}\bigl(2-D_n(u,v)\bigr)=f(u)+f(u+\sigma_n+v)+v^2+O(n^{-2}).
\]

**3. Localization and convergence.** As every radial coordinate lies in \([\cos\alpha,1]\), the cosine law also gives
\[
D_n^2=(r_1+r_2)^2-2r_1r_2(1-\cos(2\pi v/n)).
\]
For a fixed \(t\) and all sufficiently large \(n\), the distance event forces \(D_n\ge2-O_t(n^{-2})\), hence \(r_1+r_2\ge2-O_t(n^{-2})\) and \(r_1r_2\ge1-O_t(n^{-2})\). Consequently \(1-\cos(2\pi v/n)\le C_t/n^2\). For \(|v|\le n/2\), the elementary lower bound \(1-\cos(2\pi v/n)\ge8v^2/n^2\) then forces \(|v|\le C'_t\), uniformly in large \(n\). The integrand is therefore supported on a fixed compact cylinder. The limiting level set \(\{G_\sigma=t\}\) has planar measure zero: for each \(u\), \(G_\sigma(u,v)\) is piecewise quadratic on the bounded \(v\)-interval, with strictly positive quadratic term \(v^2\), so it has finitely many roots except possibly at isolated breakpoints. Dominated convergence and the uniform density expansion prove the boxed limit (including \(t=0\)). Continuity and monotonicity of \(H_\sigma\) follow by the same level-set argument.

**4. The even onset.** Since \(f\ge0\) with equality exactly at integers, the unique zero of \(G_0\) modulo \(u\in[0,1)\) is \((u,v)=(0,0)\), with the periodic \(u\)-boundary identified. In local unwrapped coordinates \(x=u\), \(y=u+v\), the Jacobian is one and
\[
G_0=2|x|+2|y|+O(x^2+y^2).
\]
The diamond \(2|x|+2|y|<t\) has area \(t^2/2\), and scaling \((x,y)=t(X,Y)\) gives \(H_0(t)=t^2/2+o(t^2)\).

**5. The odd gap and onset.** Since \(f(x)\ge q(x)\), the circle metric triangle inequality shows
\[
G_{1/2}(u,v)\ge q(u)+q(u+1/2+v)+v^2\ge\operatorname{dist}(v+1/2,\mathbb Z)+v^2.
\]
For \(|v|\le1/2\) this right side is \(1/2-|v|+v^2=1/4+(|v|-1/2)^2\). For \(|v|>1/2\), the term \(v^2\) alone exceeds \(1/4\). Equality holds only at the two isolated points \((u,v)=(0,\pm1/2)\), modulo \(u\). In local coordinates \(x=u\) and \(y=u+v\mp1/2\) around either point, we get \(v=\pm1/2+y-x\), hence
\[
G_{1/2}-1/4=2|x|+2|y|\pm(y-x)+O(x^2+y^2).
\]
The positive-linear coefficients in the four quadrants are \((1,3)\) for one variable and \((3,1)\) for the other. The planar region where its piecewise-linear leading part is less than \(\eta\) has area
\[
\frac{\eta^2}{2}\left(1+\frac13\right)^2=\frac89\eta^2.
\]
Two disjoint minimizing neighborhoods contribute equally, giving \(H_{1/2}(1/4+\eta)=16\eta^2/9+o(\eta^2)\). The global lower bound gives the exact zero interval. For a regular odd polygon, the farthest vertex pair has central separation \(\pi-\pi/n\); convexity ensures a diameter is realized by vertices, so \(\operatorname{diam}P_n=2\cos(\pi/(2n))\).

**6. Large-argument connection.** The elementary bounds \(0\le f\le1/2\) imply \(v^2\le G_\sigma(u,v)\le v^2+1\). For \(t\ge1\) the sublevel region contains \(|v|<\sqrt{t-1}\) and is contained in \(|v|<\sqrt t\). Integrating in \(u\) proves \(2\sqrt{t-1}\le H_\sigma(t)\le2\sqrt t\) and its expansion. On the unit circle, two independent uniform points obey \(\Pr(D>2-\varepsilon)=(2/\pi)\sqrt\varepsilon+O(\varepsilon^{3/2})\); at \(\varepsilon=\pi^2t/n^2\) this becomes \(2\sqrt t/n+o(1/n)\), matching the envelope.

## Verification
The accompanying standard-library program `verify_boundary_crossover.py` implements radial position and exact perimeter Jacobian directly from the polygon side equations, calculates the scaling integral independently on midpoint grids, checks its two onset constants using exact rational polygonal-area calculations, and compares twelve finite-polygon probabilities in both parities to the proposed limit using deterministic double quadrature. Its execution reports `VERIFY_OK exact_onset_coefficients=2 odd_diameters=4 finite_n_quadratures=12 max_absolute_error=0.001019`. This is finite numerical and symbolic corroboration, not a substitute for the uniform limit proof and exact onset arguments.

## Relationship to prior work
The full regular-polygon chord distribution studied by Harutyunyan and Ohanyan (2009) uses motion-invariant random **lines**; the induced endpoint distribution differs from independent uniform boundary arclength. Bäsel (2012) studies motion-invariant random-line chords and distances between independently sampled **interior-area** points, with no simultaneous polygon-refinement and endpoint-near-diameter limit. Thus neither stated distribution implies the present two-boundary-endpoint limit simply by specializing a parameter. A separate previously published parity analysis of **center-passing angular** chords also uses a fundamentally different pair-selection mechanism: its near-diameter fluctuation law is a one-variable distribution, not the two-variable arclength pair probability here. These are substantive sampling-law distinctions, not proofs that no equivalent result has ever been published.

## Limitations
The result is restricted to regular Euclidean polygons of a common circumradius, independent arclength-uniform boundary points and fixed rescaled threshold as the side count grows. The finite-\(n\) probability error is not quantified uniformly in \(t\), nor is a joint large-\(t\), large-\(n\) limit asserted. The theorem does not give a full fixed-polygon chord distribution, arbitrary convex-polygon boundary tails, or sample-maxima extreme-value laws. Published or unpublished equivalent treatments using other terminology could exist; historical priority has not been certified independently.

## References
1. Uwe Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted 2012-04-12 (v1), especially its main chord section and the interior-point distance theorem.
2. H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, *Advances in Applied Probability* 41 (2009), 358–366, DOI: 10.1239/aap/1246886615.
3. G. R. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, *Journal of Applied Probability* 19 (1982), 690–695. This is a related random-line inverse problem; only the available abstract was consulted.
