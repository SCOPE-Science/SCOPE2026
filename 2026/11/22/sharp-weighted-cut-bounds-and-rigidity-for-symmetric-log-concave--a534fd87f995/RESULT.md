# Sharp weighted-cut bounds and rigidity for symmetric log-concave line measures

## Finding

Let \(X,Y\) be independent samples from the same nondegenerate probability density \(f\) on the line, where \(f\) is even and log-concave. For a point \(t\in\mathbb R\), let \(C_f(t)\) be the expected Euclidean length of segments joining \(X\) to \(Y\) which are crossed by the point \(t\), counting a segment with its full length:
\[
C_f(t)=\mathbb E\bigl[|X-Y|\,\mathbf1_{\{\min(X,Y)<t<\max(X,Y)\}}\bigr].
\]
Write \(L_f=\mathbb E|X-Y|\) and \(\eta_f=\sup_t C_f(t)/L_f\). Then
\[
\boxed{\frac23\le\eta_f\le\frac34.}
\]
The unique maximizing cut is the symmetry center \(t=0\). Equality at \(2/3\) holds exactly for the two-sided exponential (Laplace) densities \(f(x)=e^{-|x|/b}/(2b)\), \(b>0\); equality at \(3/4\) holds exactly for the uniform densities on \([-a,a]\), \(a>0\). Both endpoints are attainable. Every intermediate efficiency occurs for a symmetric compactly supported log-concave density.

There are two exact, nonnegative *defect identities* which additionally quantify the two rigidity statements. Let \(g(t)=\Pr(|X|>t)\) for \(t\ge0\). Then
\[
\frac32\max_t C_f(t)-L_f
=\int_0^\infty\bigl(g(t)^2-g(2t)\bigr)\,dt\ge0.
\]
Further, write \(X\overset d=AU\), where \(U\) is uniform on \([-1,1]\) and \(A>0\) is an independent mixing radius. With \(A'\) an independent copy,
\[
L_f-\frac43\max_t C_f(t)
=\frac16\mathbb E\frac{(A-A')^2}{\max(A,A')}\ge0.
\]
The latter identity is valid for an even unimodal density with finite first absolute moment, without log-concavity.

## Assumptions and scope

The line carries its standard Euclidean metric. Segment lengths are weighted by \(|X-Y|\); no normalizing by the number of crossing pairs is used. The same absolutely continuous distribution generates both endpoints. An even log-concave density is allowed to have bounded support and to have an endpoint discontinuity; it is nondegenerate and has finite, strictly positive \(\mathbb E|X|\). In the extension to even unimodal densities, finiteness of \(\mathbb E|X|\) is a separate hypothesis, needed for the finite ratios and the subtraction of expectations. The mixing radius is strictly positive almost surely. No inequality here is asserted for arbitrary unequal pairs of measures or for higher-dimensional cuts.

## Proof

**1. Optimizing the cut.** More generally take any finite-mean density \(f\), its cumulative distribution \(F\), and mean \(\mu\). Put \(a(t)=\mathbb E(t-X)_+\) and \(b(t)=\mathbb E(X-t)_+\). Splitting the two possible orientations of a crossing pair gives
\[
C_f(t)=2\bigl[(1-F(t))a(t)+F(t)b(t)\bigr].
\]
Since \(a'(t)=F(t)\), \(b'(t)=-(1-F(t))\), and \(b(t)-a(t)=\mu-t\), differentiation yields \(C_f'(t)=2f(t)(\mu-t)\) almost everywhere. The function is increasing below \(\mu\) on the density support and decreasing above \(\mu\); consequently its maximum is uniquely at \(\mu\) for a nondegenerate log-concave density. For even \(f\), \(\mu=0\), and evaluating at the symmetry center gives
\[
C_f(0)=\mathbb E|X|=\int_0^\infty g(t)\,dt=:I_1.
\]

**2. Reducing total segment length to a survival integral.** For any continuous distribution \(\mathbb E|X-Y|=2\int_{\mathbb R}F(t)(1-F(t))\,dt\). By symmetry, \(F(t)=1-g(t)/2\) on \(t\ge0\), giving
\[
L_f=2I_1-I_2,\qquad I_2=\int_0^\infty g(t)^2\,dt.
\]

**3. The Laplace endpoint and its rigidity.** The right survival function \(g\) is log-concave: for any \(u\ge0\), the ratio \(f(t+u)/f(t)\) is nonincreasing in \(t\) on the positive support by concavity of \(\log f\). Thus \(g(t)/f(t)=\int_0^\infty f(t+u)/f(t)\,du\) is nonincreasing and the hazard rate \(f(t)/g(t)\) is nondecreasing; hence \(\log g\) is concave. The same conclusion holds by continuity at support endpoints. With \(g(0)=1\), midpoint log-concavity yields \(g(t)^2\ge g(2t)\) for all \(t\ge0\). Integrating and substituting \(u=2t\) shows \(I_2\ge I_1/2\), so \(L_f\le3I_1/2\). This is exactly \(\eta_f\ge2/3\), with the first displayed defect identity.

If equality holds, the continuous nonnegative defect \(g(t)^2-g(2t)\) vanishes throughout the positive support. Consequently \(h(t)=-\log g(t)\) is continuous, convex, and obeys \(h(2t)=2h(t)\). **Convexity plus this doubling equation alone is enough to make \(h\) linear:** the slopes of the chords from the origin are monotone in \(t\), while their values at \(t\) and \(2^k t\) coincide for every integer \(k\) before the support endpoint; for unbounded support any two arguments can be bracketed by dyadic rescalings. For bounded support the equality is impossible because for \(t\) in the upper half of the support, \(g(2t)=0<g(t)^2\). Therefore \(g(t)=e^{-t/b}\) for some \(b>0\). Since \(g'(t)=-2f(t)\) almost everywhere, \(f\) is precisely the centered Laplace density. Conversely that density has \(I_2=I_1/2\), establishing equality.

**4. The uniform endpoint and its rigidity.** Let \(f\) be an even unimodal density with \(\mathbb E|X|<\infty\). Such a density has a representative that is nonincreasing for positive arguments, so its positive half-line profile has the Stieltjes mixture representation (as an identity of densities almost everywhere)
\[
f(x)=\int_{(0,\infty)}\frac{\mathbf1_{\{|x|\le a\}}}{2a}\,H(da),\qquad H(da)=-2a\,df(a).
\]
The boundary mass identity \(\int H(da)=2\int_0^\infty f(x)dx=1\) follows by integration by parts; boundary terms vanish for every integrable nonincreasing density. Therefore \(X=AU\) in law, with \(U\sim\operatorname{Unif}[-1,1]\) and \(A\sim H\) independent. In particular \(\mathbb EA=2\mathbb E|X|<\infty\). The cut formula in Step 1 still gives a maximum of \(I_1\) at \(0\) in this setting. Conditioning on radii \(a,b>0\), with \(a\ge b\), elementary integration gives
\[
\mathbb E|aU-bU'|=\frac a2+\frac{b^2}{6a},\qquad
\mathbb E|aU|=\frac a2.
\]
Subtracting \(\frac43\) times the average of the two single-radius absolute moments gives exactly \((a-b)^2/(6\max(a,b))\). Averaging over independent radii \(A,A'\) proves
\[
L_f-\frac43I_1=\frac16\mathbb E\frac{(A-A')^2}{\max(A,A')}.
\]
Thus \(L_f\ge4I_1/3\), equivalently \(\eta_f\le3/4\). Equality holds if and only if \(A=A'\) almost surely; independence then forces \(A\) to be deterministic, hence \(X\) uniform on a symmetric interval. Conversely the uniform law realizes equality.

**5. Complete realization of the interval.** For every \(p\ge0\), the density
\[
f_p(x)=\frac{p+1}{2}(1-|x|)^p\,\mathbf1_{\{|x|\le1\}}
\]
is even, log-concave and nondegenerate. Its survival function is \(g_p(t)=(1-t)^{p+1}\) for \(0\le t\le1\), zero beyond. Consequently
\[
I_1=\frac1{p+2},\qquad I_2=\frac1{2p+3},\qquad
\eta_{f_p}=\frac{2p+3}{3p+4}.
\]
This fraction decreases continuously and strictly from \(3/4\) at \(p=0\) to its limit \(2/3\) as \(p\to\infty\); the limit is attained by a centered Laplace density (not by finite \(p\)).

## Verification

The enclosed standalone standard-library checker (`check.py`) verifies the finite rational algebra in the interpolation family, the endpoint ratios, the exact two-radius uniform convolution formula for several rational pairs, and the resulting mixing-radius deficit formula. No finite numerical or symbolic tests are used to justify the universal quantifiers: the proofs of the universal inequalities and equality cases are analytic and given above. Run `python3 check.py` in the package directory; its successful exit code and printed count report the checks.

## Relationship to prior work

Correa, Griesbach, Harb, and Hommelsheim (2026) study total-length-weighted separation of pairs of measures in Euclidean space and establish one-dimensional general guarantees for two potentially *different* endpoint laws. Their Section 3.1 addresses the unrestricted problem, not the exact sharp interval and equality classification for two independent samples from the **same symmetric log-concave** law. Earlier work of Lambert and Yitzhaki on Gini mean differences versus absolute deviations from a quantile already contains the crucial crossing-weight/mean-absolute-deviation relation in equivalent notation; neither that general relation nor individual table values for Laplace and uniform laws imply the new all-distribution inequalities, extremizer rigidity, or nonnegative defect formulas. The derivative calculation for the best centered threshold and the standard uniform-mixture representation themselves are background ingredients, not asserted as new discoveries.

## Limitations

This result is restricted to one-dimensional iid samples of a common symmetric log-concave law; the upper inequality extends to even unimodal densities of finite first absolute moment. The lower inequality is proved using log-concavity of the tail. The equality proofs require nondegeneracy. No extension to dissimilar endpoint distributions, higher-dimensional cutting hyperplanes or non-length segment weights is asserted. The historical-priority comparison is based on accessible scientific sources and semantic record searches; older literature using different names for the Gini–absolute-deviation ratio remains a possibility.

## References

- J. Correa, S. M. Griesbach, E. Harb, F. Hommelsheim, R. Jlibene, V. Livanos, and E. Solan, *Separating Measures by Hyperplanes*, arXiv:2611.09166v1 (first public posting 2026-11-06). https://arxiv.org/abs/2611.09166 . In particular Section 3.1 on one-dimensional length-weighted separation.
- S. Yitzhaki and P. J. Lambert, *The relationship between the absolute deviation from a quantile and Gini’s mean difference*, *Metron* (2013), DOI:10.1007/s40300-013-0015-y. https://doi.org/10.1007/s40300-013-0015-y . See the quantile-deviation and between-group Gini identities.
- C. Gerstenberger and D. Vogel, *On the efficiency of Gini’s mean difference*, arXiv:1405.5027 (2014), https://arxiv.org/abs/1405.5027 . Background on the Gini mean difference as a dispersion statistic; not an extremal characterization of the present form.
