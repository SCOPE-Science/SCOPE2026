# The Pareto moment transition and grazing-line boundary layer of thin circular annuli

## Finding
Let \(0<r<1\) and let \(A_r=\{x\in\mathbb R^2:r\le\|x\|\le1\}\). Choose an unoriented line from the Euclidean-motion-invariant line measure, conditioned to intersect the unit disk. Write \(L_r\) for the **sum of the lengths of all connected components** of its intersection with \(A_r\); in particular, an inner-disk-crossing line contributes both material segments. Put \(\delta=1-r\) and \(X_\delta=L_r/(2\delta)\).

The entire line-intercept distribution is elementary. For \(0\le w\le 2(1-r)\),
\[
\Pr(L_r>w)=\sqrt{1-w^2/4}.
\]
For \(2(1-r)<w<2\sqrt{1-r^2}\), writing \(q=w/2\),
\[
\Pr(L_r>w)=\sqrt{1-q^2}-\sqrt{1-\left(\frac{q+(1-r^2)/q}{2}\right)^2}.
\]
For \(w\ge2\sqrt{1-r^2}\), the survival probability is zero. In particular, \(\max L_r=2\sqrt{1-r^2}\), and the mean is \(\mathbb E L_r=\pi(1-r^2)/2\).

As the annulus becomes thin, \(\delta\downarrow0\), the normalized material length \(X_\delta\) converges in distribution to \(Y=(1-S^2)^{-1/2}\), \(S\sim\operatorname{Unif}[0,1]\). Thus \(\Pr(Y\le x)=0\) for \(x<1\) and \(\sqrt{1-x^{-2}}\) for \(x\ge1\). Its tail is asymptotic to \(1/(2x^2)\).

The critical moment order is exactly two. For every fixed real \(p>0\):
\[
\begin{aligned}
0<p<2:\quad&\mathbb E X_\delta^p\longrightarrow\frac{\sqrt\pi\,\Gamma(1-p/2)}{2\Gamma(3/2-p/2)},\\
p=2:\quad&\mathbb E X_\delta^2=\tfrac12\log(1/\delta)+\log(2\sqrt2)+\tfrac34+O(\delta\log(1/\delta)),\\
p>2:\quad&\delta^{p/2-1}\mathbb E X_\delta^p\longrightarrow\frac{2^{p/2+1}(p-1)}{p^2-4}.
\end{aligned}
\]
At the distinct grazing-line scale, for each fixed \(0<t<\sqrt2\),
\[
\lim_{\delta\downarrow0}\frac{\Pr(L_r>2t\sqrt\delta)}{\delta}
=G(t):=\frac1{2t^2}+\frac12-\frac{3t^2}{8}.
\]
For \(t\ge\sqrt2\) this limit is zero. Moreover, conditional on \(L_r>2t\sqrt\delta\), the rescaled line-offset deficit \((1-S)/\delta\) converges to the uniform law on
\[
\left[\frac{t^2}{2},\frac1{2t^2}+\frac12+\frac{t^2}{8}\right].
\]
The formulas involve the motion-invariant random line model, **not** uniform random endpoints or a randomly selected individual connected component.

## Assumptions and scope
The Euclidean invariant line measure is \(d\theta\,da\) for a normal angle \(\theta\in[0,\pi)\) and signed offset \(a\in\mathbb R\). Conditioning on intersecting the outer unit disk makes \(\theta\) uniform and \(a\sim\operatorname{Unif}[-1,1]\) independently. Hence \(S=|a|\) is uniform on \([0,1]\). All limits hold with the displayed \(p\) or \(t\) fixed as \(r=1-\delta\uparrow1\). The closed annulus convention changes no probability because tangency events have measure zero.

## Proof
For fixed offset \(s\in[0,1]\), the line intersects the outer disk in length \(2\sqrt{1-s^2}\). The inner disk removes length \(2\sqrt{r^2-s^2}\) for \(s<r\), and removes zero for \(s\ge r\). Therefore
\[
\ell_r(s)=2\left[\sqrt{1-s^2}-\sqrt{(r^2-s^2)_+}\right].\tag{1}
\]
On \((0,r)\) it increases strictly, since its derivative is \(2s[(r^2-s^2)^{-1/2}-(1-s^2)^{-1/2}]>0\). On \((r,1)\) it decreases strictly. The central value is \(2(1-r)\), and the maximum is \(2\sqrt{1-r^2}\). For \(w\le2(1-r)\), the exceedance offsets form \([0,\sqrt{1-w^2/4})\). Above this value, there is also a lower threshold \(s_-(w)\) on the inner crossing branch. Let \(q=w/2\) and \(a=\sqrt{1-s^2}\), \(b=\sqrt{r^2-s^2}\). Then \(a-b=q\), \(a^2-b^2=1-r^2\), and \(a=[q+(1-r^2)/q]/2\). This yields the two exact CDF branches without any numerical inversion. Integrating (1) gives \(\mathbb E L_r=\pi(1-r^2)/2\).

For fixed \(0\le s<1\), rationalizing the square-root difference in (1) gives
\[
X_\delta(s)\longrightarrow (1-s^2)^{-1/2}.
\]
For all \(s\), \(0\le X_\delta(s)\le2(1-s^2)^{-1/2}\). Dominated convergence yields the complete weak limit and all moment limits with \(0<p<2\), including the beta integral stated above.

For grazing lines set \(y=(1-s)/\delta\), so \(0\le y\le1/\delta\), and define \(H_\delta(y)=\ell_{1-\delta}(1-\delta y)/(2\sqrt\delta)\). The exact formulas are
\[
H_\delta(y)=
\begin{cases}
\sqrt{2y-\delta y^2},&0\le y\le1,\\
\sqrt{2y-\delta y^2}-\sqrt{2(y-1)-\delta(y^2-1)},&1<y\le1/\delta.
\end{cases}
\]
They converge pointwise to
\[
H(y)=\sqrt{2y}-\sqrt{2(y-1)_+}.
\]
On \(0\le y\le1\), \(H_\delta\le\sqrt{2y}\); on \(1\le y\le1/\delta\), rationalization shows \(H_\delta=(2-\delta)/(\sqrt{2y-\delta y^2}+\sqrt{2(y-1)-\delta(y^2-1)})\le2/\sqrt y\). Thus, for \(p>2\), dominated convergence after \(s=1-\delta y\) gives
\[
\delta^{p/2-1}\mathbb E X_\delta^p\longrightarrow\int_0^\infty H(y)^p\,dy.
\]
The first part of the integral is \(2^{p/2+1}/(p+2)\). On \(y\ge1\), putting \(z=H(y)\), one has \(y=1/(2z^2)+1/2+z^2/8\) and \(-dy/dz=z^{-3}-z/4\), with \(0<z\le\sqrt2\). Integrating \(z^p(z^{-3}-z/4)\) and adding the first part yields \(2^{p/2+1}(p-1)/(p^2-4)\).

The same monotonicity of the two parts of \(H\) shows \(H(y)>t\), for \(0<t<\sqrt2\), precisely on
\[
\frac{t^2}{2}<y<\frac1{2t^2}+\frac12+\frac{t^2}{8}.
\]
Since the line-offset variable \(s\) has constant density one, the probability of this event is \(\delta\) times the width of the interval up to \(o(\delta)\). This proves \(G(t)\). Conditioned on exceedance, the transformed offset is uniform between its two exact prelimit roots, which converge to the displayed limits, proving the marked uniform law. At and above \(t=\sqrt2\) the scaled exceedance probability is zero, using the exact maximum bound.

It remains to treat the borderline moment. Define the complete elliptic integrals
\[
K(r)=\int_0^{\pi/2}\frac{d\phi}{\sqrt{1-r^2\sin^2\phi}},\qquad E(r)=\int_0^{\pi/2}\sqrt{1-r^2\sin^2\phi}\,d\phi.
\]
Squaring (1) and integrating both branches gives the exact identity
\[
\mathbb E X_\delta^2=\frac{2}{3\delta^2}\left[1+r^3-(1+r^2)E(r)+(1-r^2)K(r)\right].\tag{2}
\]
Indeed the cross term reduces to \(J=\int_0^r\sqrt{(1-s^2)(r^2-s^2)}\,ds=[(1+r^2)E(r)-(1-r^2)K(r)]/3\). The latter reduction follows on setting \(s=r\sin\phi\) and integrating the derivative of \(\sin\phi\cos\phi\sqrt{1-r^2\sin^2\phi}\) between its zero boundary values. With \(m=1-r^2\) and \(B=\log(4/\sqrt m)\), the standard expansions are
\[
\begin{aligned}
K(r)&=B+\frac m4(B-1)+\frac{9m^2}{64}(B-7/6)+O(m^3B),\\
E(r)&=1+\frac m2(B-1/2)+\frac{3m^2}{16}(B-13/12)+O(m^3B).
\end{aligned}
\]
Substituting \(m=2\delta-\delta^2\) into (2) yields \(\mathbb E X_\delta^2=B+3/4+O(\delta B)=\tfrac12\log(1/\delta)+\log(2\sqrt2)+3/4+O(\delta\log(1/\delta))\), completing the proof.

## Verification
A standalone `verify.py` reproduces the explicit survival probabilities by deterministic offset sampling, independently quadratures the first two moments, compares the elliptic-integral identity, and checks finite-thickness convergence of the grazing probabilities and fourth-moment coefficient. These finite checks corroborate the analytic identities but do not replace the proof. Run using `python verify.py` in a directory containing only the embedded files; SciPy is required.

## Relationship to prior work
Motion-invariant random-line normalization and convex-body chord laws are classical. Bäsel, *Random chords and point distances in regular polygons* (arXiv:1204.2707, first posted 12 April 2012), and Harutyunyan–Ohanyan, *The chord length distribution function for regular polygons* (2009), treat convex regular polygons, not total material intercepts of a nonconvex annulus. Aharonyan–Harutyunyan–Ohanyan (2010) relates finite-segment intersections to convex-body chord laws. Those methods motivate the line model, but neither their geometric objects nor their stated results supply the thin-annulus critical moment spectrum or grazing marked law. Related annular intrinsic-distance, nested-circle chord-crossing and affine-projector results study different observables. Priority outside the inspected sources is not certified.

## Limitations
Only concentric planar circular annuli and conditioned invariant affine lines are treated. The total material length differs from either separate connected chord length and from endpoint-generated chords. No assertion is made for eccentric holes, noncircular boundaries, three-dimensional shells, or arbitrary line sampling; independent mathematical and historical verification remains outstanding.

## References
- U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707 (public 2012-04-12), https://arxiv.org/abs/1204.2707.
- H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, *Advances in Applied Probability* **41** (2009), 358–366, https://doi.org/10.1239/aap/1246886615.
- N. G. Aharonyan, H. S. Harutyunyan, and V. K. Ohanyan, *Random copy of a segment within a convex domain*, *Journal of Contemporary Mathematical Analysis* **45** (2010), 348–356, https://doi.org/10.3103/S1068362310060063.
- L. A. Santaló, *Integral Geometry and Geometric Probability*, Addison–Wesley (1976), classical invariant-line background.
