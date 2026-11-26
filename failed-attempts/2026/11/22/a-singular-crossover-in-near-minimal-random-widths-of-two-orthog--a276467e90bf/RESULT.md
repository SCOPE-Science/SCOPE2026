# A singular crossover in near-minimal random widths of two orthogonal disks

## Finding
Let \(K_t\subset\mathbb R^3\) be the convex hull of two perpendicular unit disks, centered at \((0,-t/2,0)\) in \(z=0\) and \((0,t/2,0)\) in \(x=0\), with separation \(t\ge0\). Let \(U\) be Haar-uniform on the unit sphere, and let \(W_t\) be the width of \(K_t\) perpendicular to \(U\). For every \(t\ge0\), the minimum width is exactly \(\sqrt2\), attained at precisely four oriented unit normals on the sphere (two unoriented lines), namely \((\pm1,0,\pm1)/\sqrt2\).

For every **fixed** \(t>0\), the exact lower-endpoint probability has the sharp asymptotic
\[
\boxed{\Pr(W_t\le\sqrt2+\varepsilon)\sim\frac{2\sqrt2}{\pi t}\varepsilon^2}\quad(\varepsilon\downarrow0).
\]
In particular, for the distinguished separation \(t=1\), which generates the classical oloid, the coefficient equals \(2\sqrt2/\pi\). At the coincident-center limit \(t=0\), the exponent changes discontinuously:
\[
\boxed{\Pr(W_0\le\sqrt2+\varepsilon)\sim\frac{2^{11/4}}{3\pi}\varepsilon^{3/2}.}
\]

The crossover is completely resolved on the distinguished scale \(t\asymp\sqrt\varepsilon\). If \(t_\varepsilon\ge0\) and \(t_\varepsilon/\sqrt\varepsilon\to\tau\in[0,\infty)\), define
\[
y_\tau=\frac{\sqrt{\tau^2+2\sqrt2}-\tau}{\sqrt2},\qquad
F(\tau)=\frac{2\sqrt2}{\pi}\left(y_\tau-\frac{y_\tau^3}{3\sqrt2}\right).
\]
Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\Pr(W_{t_\varepsilon}\le\sqrt2+\varepsilon)}{\varepsilon^{3/2}}=F(\tau).}
\]
The function is continuous, strictly decreasing, and positive, with \(F(0)=2^{11/4}/(3\pi)\) and \(F(\tau)\sim2\sqrt2/(\pi\tau)\) as \(\tau\to\infty\). The near-minimizing viewing directions have an explicit conditional two-coordinate limit: in any of four angular charts, with longitude displacement \(s=\varepsilon x\) and equatorial-latitude coordinate \(v=\sqrt\varepsilon\,y\), their conditional rescaled distribution tends to uniform normalized area on
\[
\boxed{\mathcal D_\tau=\{(x,y)\in\mathbb R^2:y^2/\sqrt2+\max(\sqrt2|x|,\tau|y|)\le1\}.}
\]
Each of the four charts has limiting conditional probability \(1/4\).

## Assumptions and scope
The disks are *filled* unit Euclidean disks and their convex **hull** is taken, not a Minkowski sum; both disks lie in perpendicular coordinate planes and their centers separate along the common line of the planes. Directions are uniform in Euclidean solid angle; the width is the difference of two support functions, not area of an orthographic planar shadow. The fixed-separation result takes \(t>0\) fixed before \(\varepsilon\downarrow0\). The crossover permits a variable nonnegative separation with a finite \(t_\varepsilon/\sqrt\varepsilon\) limit. The conditional law is weak convergence under the spherical-area conditional measure and requires the same finite crossover scaling. No finite-sample statistical inference is claimed.

## Proof
**Exact support function and minimizers.** Write a spherical normal in coordinates
\[
U=(\sqrt{1-v^2}\cos\phi,\ v,\sqrt{1-v^2}\sin\phi),\quad -1<v<1,\quad \phi\in[0,2\pi).
\]
Set \(A=\sqrt{U_x^2+v^2}\), \(B=\sqrt{U_z^2+v^2}\). Taking maxima of the generating-disk supports in opposite normal directions gives
\[
W_t(U)=A+B+\max\{|A-B|,t|v|\}.\tag{1}
\]
This support identity appears already in the cited mean-width work and is not claimed as new. It immediately implies
\[
W_t(U)\ge2\max(A,B)\ge\sqrt{2(A^2+B^2)}=\sqrt{2(1+v^2)}\ge\sqrt2.
\]
Equality requires \(v=0\) and \(A=B\), and hence precisely \(\phi=\pi/4+k\pi/2\), \(k=0,1,2,3\). Direct substitution shows all four do attain equality, independently of \(t\).

**Uniform local expansion.** At any minimizer, set \(s=\phi-(\pi/4+k\pi/2)\). A direct Taylor expansion of the two square roots in (1), uniformly for bounded nonnegative \(t\), gives
\[
W_t-\sqrt2=\frac{v^2}{\sqrt2}+\max\{\sqrt2|s|,t|v|\}
+O(s^2+|s|v^2+v^4).\tag{2}
\]
The sign of \(A-B\) switches from chart to chart, but its absolute value has the displayed common expansion. This expansion and uniqueness of the four global minima reduce small-width probability to four disjoint angular patches. The exact Haar-area element in these coordinates is \(d\phi\,dv/(4\pi)\).

**Fixed positive separation.** Fix \(t>0\). The first two terms of (2) show that \(W_t-\sqrt2\le\varepsilon\) requires \(|s|=O(\varepsilon)\) and \(|v|=O_t(\varepsilon)\). Put \(s=\varepsilon x\), \(v=\varepsilon y\), so the rescaled indicator converges almost everywhere to that of the rectangle
\[
\{(x,y):\sqrt2|x|\le1,\ t|y|\le1\}.
\]
The local lower bounds provide a fixed compact dominating set. This rectangle has area \(2\sqrt2/t\). Summing four equal patches with spherical probability density \(1/(4\pi)\) proves the fixed-\(t\) coefficient \(2\sqrt2/(\pi t)\).

**Critical crossover and conditional normals.** Suppose \(t_\varepsilon/\sqrt\varepsilon\to\tau\in[0,\infty)\). In (2), use \(s=\varepsilon x\), \(v=\sqrt\varepsilon\,y\). On bounded \((x,y)\), division by \(\varepsilon\) yields the limiting profile
\[
\frac{y^2}{\sqrt2}+\max\{\sqrt2|x|,\tau|y|\}.
\]
Moreover, the quadratic lower bound in \(v\) and the linear lower bound in \(|s|\) give uniform compactness of the scaled sublevel sets. Thus dominated convergence applies to their areas and conditional bounded test-function integrals. The limiting set is \(\mathcal D_\tau\). Its \(y\)-range follows from \(y^2/\sqrt2+\tau|y|\le1\), so \(|y|\le y_\tau\). At fixed \(y\) in this range, \(|x|\le(1-y^2/\sqrt2)/\sqrt2\). Therefore
\[
\operatorname{area}(\mathcal D_\tau)
=\int_{-y_\tau}^{y_\tau}\frac{2}{\sqrt2}\left(1-\frac{y^2}{\sqrt2}\right)dy
=2\sqrt2\left(y_\tau-\frac{y_\tau^3}{3\sqrt2}\right).
\]
Since four equal patches each have probability area divided by \(4\pi\), the entire probability is \(\varepsilon^{3/2}\operatorname{area}(\mathcal D_\tau)/\pi+o(\varepsilon^{3/2})\), proving the formula for \(F\). The same area convergence for bounded test functions yields the stated uniform conditional law and equal chart weights. At \(\tau=0\), \(y_0=2^{1/4}\), giving the \(3/2\)-power constant. Since \(y_\tau\) is strictly decreasing in \(\tau\), the domain sets are strictly nested with positive lost area, hence \(F\) is strictly decreasing. Finally, rationalizing the radical gives \(y_\tau\sim1/\tau\), and the claimed large-\(\tau\) matching follows.

## Verification
The included `verify_width.py` (Python 3, NumPy, SciPy) runs 1,071 deterministic finite assertions, with 1,000 independent support-vs-width/minimum evaluations at five separations; 20 exact minimum-direction checks; 15 numerical finite-width quadrature checks at fixed separations; 15 crossover quadrature checks; and 21 independent area-integral checks. It outputs `WIDTH_DIAGNOSTICS_PASSED 1071`. The direct numerical probability uses one-dimensional angular integration of the *unexpanded* support expression, not the asymptotic formula. Sample convergence at fixed \(t=1\) approaches \(2\sqrt2/\pi\), and at \(\tau=0\) approaches \(2^{11/4}/(3\pi)\). These numerical checks are diagnostics, not proofs of infinite limiting statements; the analytic local-profile and area arguments above supply the proof.

## Relationship to prior work
Finch (2012) introduces and analyzes convex hulls of two orthogonal unit disks, with the oloid and other special separations. Bäsel (2016) evaluates the oloid's *mean* width. An earlier published exact mean-width derivative study proves (1), strict convexity of the averaged width as separation varies, and its asymptotic slope. That exact support identity is a prior ingredient, not a new result here. The separately published three-coordinate-disk hull width distribution is a different convex body: it contains three co-centered coordinate disks, with no separating parameter and no singular two-disk crossover. The assessed new result is the exact sharp random-direction *lower-tail* coefficient for separated perpendicular disks, its change of exponent at coincident centers, its resolved critical scaling, and the limiting conditional angular shape. Broad mean-width formulas integrate the directional width and do not themselves state or imply these sharp localized distributional laws without a further local geometric analysis. The references and sources were compared by objects and implications, not just keyword/title matching.

## Limitations
The small-width asymptotics are not uniform for arbitrary two-parameter paths; the finite-\(\tau\) crossover and fixed-positive-separation cases are distinct regimes. The theorem does not give the complete distribution at general nonzero separations, nor a robust inverse method for noisy width samples. Width and random-shadow area must not be conflated. An unindexed classical oloid-width distribution or an equivalent local asymptotic could predate these statements; the literature comparisons are not independent priority certification.

## References
1. Steven R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first public preprint November 19, 2012, https://arxiv.org/abs/1211.4514 .
2. Uwe Bäsel, *The mean width of the oloid and integral geometric applications of it*, arXiv:1604.07245, https://arxiv.org/abs/1604.07245 .
3. H. Dirnböck and H. Stachel, *The Development of the Oloid*, Journal for Geometry and Graphics 1 (1997), 105–118.
4. *A one-dimensional derivative law for orthogonal-disk mean width*, published mathematical result October 4, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-dimensional-derivative-law-for-orthogonal-disk-mean-width--6e52fbc79bdf .
5. *Exact random widths of the orthogonal three-disk hull and sharp hyperdisk endpoint laws*, published mathematical result November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-random-widths-of-the-orthogonal-three-disk-hull-and-sharp--d1df18476a61 .
