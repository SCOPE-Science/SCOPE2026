# Sharp cubic near-diameter distance law for uniformly sampled arbelos

## Finding

Let \(a,b>0\), \(R=a+b\), \(\alpha=a/R\), and \(\beta=b/R=1-\alpha\). The *arbelos* \(K_{a,b}\) is the region in the upper half-plane inside the radius-\(R\) semicircle with horizontal diameter \([0,2R]\) and outside both mutually tangent inner semicircles with respective horizontal diameters \([0,2a]\) and \([2a,2R]\). Its area is \(A=\pi ab\). Choose \(X,Y\) independently and uniformly by planar area in \(K_{a,b}\). Write \(D=\lVert X-Y\rVert\). For each fixed \(\alpha\in(0,1)\),

\[
\Pr\{D>2R-\varepsilon\}=\mathcal C(\alpha)(\varepsilon/R)^3+o_{\alpha}((\varepsilon/R)^3)\qquad(\varepsilon\downarrow0).
\]

Define \(c_\alpha=\beta/(2\alpha)\), \(c_\beta=\alpha/(2\beta)\),

\[
I_\alpha=\frac{2}{\sqrt{c_\alpha}}\arctan(2\sqrt{c_\alpha}),\qquad
I_\beta=\frac{2}{\sqrt{c_\beta}}\arctan(2\sqrt{c_\beta}),
\]
\[
I_{\alpha\beta}=\sqrt{8\alpha\beta}\left(\arctan\sqrt{\frac{2\alpha^3}{\beta}}+\arctan\sqrt{\frac{2\beta^3}{\alpha}}\right).
\]

Then the sharp coefficient is

\[
\boxed{\mathcal C(\alpha)=\frac{4-I_\alpha-I_\beta+I_{\alpha\beta}}{6\pi^2\alpha^2\beta^2}.}
\]

It is strictly positive, symmetric under \(\alpha\leftrightarrow\beta\), and has the endpoint behavior

\[
\mathcal C(\alpha)\sim\frac4{9\pi^2\alpha}\quad\text{as }\alpha\downarrow0,
\qquad \mathcal C(\alpha)=\mathcal C(1-\alpha).
\]

For the equal-inner-radii arbelos, \(\mathcal C(1/2)=\frac8{3\pi^2}(4+\sqrt2\pi-6\sqrt2\arctan\sqrt2)=0.0909871340196015\ldots\).

## Assumptions and scope

The region is closed, but its boundary has planar measure zero. Sampling is independent, absolutely continuous and *uniform by area*, not uniform along the semicircles. Distances are Euclidean, not intrinsic obstacle-avoiding geodesics. The ratio \(\alpha\) is fixed strictly between zero and one before the \(\varepsilon\downarrow0\) limit. An arbelos has outer diameter \(2R\), realized by the two extreme points of its base; the ordered diameter pairs are exactly these two orientations. No uniform error estimate as \(\alpha\) approaches zero is asserted.

## Proof

**1. Geometry and localization.** Rescale to \(R=1\), so the outer semicircle has center \((1,0)\) and radius one. The inner radii are \(\alpha\) and \(\beta\), with outermost tips \(L=(0,0)\) and \(H=(2,0)\). Because \(K_{a,b}\) lies in the outer disk, its diameter is at most two. Equality in the disk's diameter inequality requires antipodal points on the outer circle. The upper semicircle has no antipodal pair except its two base tips, hence these and only these are the ordered maximizers.

For any fixed small disjoint neighborhoods of \(L\) and \(H\), compactness provides a strict gap below two elsewhere. The deficit \(2-|X-Y|\) near these tips is coercive at first order in their respective inward horizontal displacements: the outer semicircle bounds their vertical coordinates by the square roots of twice these displacements, and the exact chord expansion shows a strictly positive lower bound proportional to their sum. Consequently near-maximal pairs have horizontal deviations \(O(\varepsilon)\) and vertical deviations \(O(\sqrt\varepsilon)\). This also permits a uniform bounded dominating domain in the scaled variables below.

**2. One ordered-tip scaling.** Near \(L,H\), write

\[
X=(\varepsilon u,\sqrt\varepsilon v),\qquad
Y=(2-\varepsilon z,\sqrt\varepsilon w),\qquad v,w\ge0.
\]

The outer and inner circular inequalities yield, on every bounded scaled window,

\[
\frac{v^2}{2}\le u\le\frac{v^2}{2\alpha},\qquad
\frac{w^2}{2}\le z\le\frac{w^2}{2\beta}
\]

in the limit; the exact corresponding bounds replace \(v^2\le2u\) by \(v^2\le2u-\varepsilon u^2\), and similarly for the inner circles, so convergence of the scaled feasible domains is valid away from null boundaries. The Euclidean distance expansion, uniformly on bounded scaled sets, is

\[
\frac{2-\lVert X-Y\rVert}{\varepsilon}
=u+z-\frac{(v-w)^2}{4}+O(\varepsilon).
\]

Put \(s=u-v^2/2\) and \(t=z-w^2/2\). Then

\[
0\le s\le c_\alpha v^2,\quad0\le t\le c_\beta w^2,
\qquad u+z-\frac{(v-w)^2}{4}=s+t+\frac{(v+w)^2}{4}.
\]

The limiting ordered-tip volume is thus the finite positive four-dimensional integral

\[
J=\int_{v,w,s,t\ge0}
\mathbf 1\!\left\{s+t+\frac{(v+w)^2}{4}<1,\ s\le c_\alpha v^2,\ t\le c_\beta w^2\right\}\,dv\,dw\,ds\,dt.
\]

There are *two* disjoint orderings, each with Jacobian \(\varepsilon^3\). Dominated convergence, using the localization bound from step 1, gives

\[
\Pr(D>2-\varepsilon)=\frac{2J}{\pi^2\alpha^2\beta^2}\varepsilon^3+o_\alpha(\varepsilon^3).
\]

**3. Exact integration.** Substitute \(q=v+w\), \(p=v/q\) (the set \(q=0\) has measure zero). The Jacobian is \(q\,dq\,dp\). Set \(L=1-q^2/4\), \(A=c_\alpha q^2p^2\), \(B=c_\beta q^2(1-p)^2\). The \((s,t)\)-area in \([0,A]\times[0,B]\) satisfying \(s+t<L\) is, by inclusion-exclusion,

\[
\tfrac12\big[L_+^2-(L-A)_+^2-(L-B)_+^2+(L-A-B)_+^2\big].
\]

Using \(\int_0^\infty\frac q2(1-kq^2)_+^2\,dq=1/(12k)\) for \(k>0\),

\[
J=\frac1{12}\int_0^1\left[4-
\frac1{1/4+c_\alpha p^2}-\frac1{1/4+c_\beta(1-p)^2}
+\frac1{1/4+c_\alpha p^2+c_\beta(1-p)^2}\right]dp.
\]

The first two reciprocal integrals evaluate to \(I_\alpha,I_\beta\). Completing the square in the final denominator yields \(I_{\alpha\beta}\). To check the latter directly, let \(c=c_\alpha+c_\beta\); then \(1/4+c_\alpha p^2+c_\beta(1-p)^2=c(p-c_\beta/c)^2+1/4+c_\alpha c_\beta/c\), and elementary arctangent integration simplifies to the stated expression. Hence \(J=(4-I_\alpha-I_\beta+I_{\alpha\beta})/12\). Substitution proves the boxed coefficient. Positivity follows from the positive-volume interior of the integral defining \(J\).

**4. Thin-arbelos coefficient.** As \(\alpha\downarrow0\), the difference of reciprocal integrals satisfies \(I_{\alpha\beta}-I_\alpha=o(\alpha)\): indeed it is the negative integral of \(c_\beta(1-p)^2/[(1/4+c_\alpha p^2)(1/4+c_\alpha p^2+c_\beta(1-p)^2)]\), whose absolute value is \(O(\alpha^{3/2})\) after scaling \(p=\sqrt\alpha z\). (Each integral individually has order \(\sqrt\alpha\), so the cancellation is essential.) The remaining expression has \(4-I_\beta=(8/3)\alpha+o(\alpha)\), by differentiating the elementary integral at \(\alpha=0\). Thus \(J\sim2\alpha/9\), giving \(\mathcal C(\alpha)\sim4/(9\pi^2\alpha)\). Interchange the inner semicircle radii for symmetry.

Restoring \(R\) replaces \(\varepsilon\) by \(\varepsilon/R\), completing the proof.

## Verification

The accompanying standalone `verification_check.py` (Python standard library only) independently evaluates the coefficient by numerical Simpson quadrature of the unsimplified one-dimensional integral, checks the symmetric closed form, and compares the exact finite-deficit four-dimensional event integral approximated by deterministic Halton quadrature to the limiting coefficient at two distinct shapes and two decreasing deficits. Run `python verification_check.py`; the observed success marker is `ARBELOS_CHORD_CHECKS_OK`. These checks corroborate constants; the infinite asymptotic statement follows from the analytic proof, not the numerical integration.

## Relationship to prior work

The classical arbelos and Archimedean-circle identities describe the object but do not evaluate this two-point distance-tail constant. Oller-Marcén's arbelos generalization is geometric, not probabilistic. Mayer–Molchanov's 2006 ball-diameter work derives probabilistic limits for rotationally symmetric bodies and analyzes broader maximum-distance limits; it does not state this parabolic-cusp arbelos coefficient. The historical Appel–Najim–Russo diameter-limit work may offer general endpoints techniques, but abstract-level inspection alone does not settle all possible implications, so priority risk remains. General compact-set distance convolution formulas permit an integral representation but do not automatically evaluate the present nonconvex shape's sharp arctangent coefficient. Related published results for annuli, Reuleaux bodies and disk-clipped squares concern distinct contact geometry or sampling metrics, and their formulas do not imply the arbelos coefficient.

## Limitations

The ratio is fixed within \((0,1)\); the divergent thin-shape coefficient is **not** a uniform double-scaling theorem. No closed form for the entire distance distribution, no inference claim for arbitrary deformed shoemaker-knife shapes and no theorem about intrinsic geodesic distances is established. Novelty is assessed against consulted and accessible sources, not by an exhaustive historical-priority certificate. Independent mathematical review has not been performed.

## References

- M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, first arXiv version 2006-05-11. https://arxiv.org/abs/math/0605289
- A. M. Oller-Marcén, *The f-belos*, first arXiv version 2012-10-30. https://arxiv.org/abs/1210.8047
- H. Okumura, *Ubiquitous Archimedean circles*, 2012. https://journals.azbuki.bg/en/mathinfo/ubiquitous-archimedean-circles/view
- M. J. Appel, J. Najim and R. P. Russo, *Limit laws for the diameter of a random point set*, Advances in Applied Probability, 2002. https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/limit-laws-for-the-diameter-of-a-random-point-set/ACCF0CA4482E1687FED4782F26325C46
- S. Lellouche and M. Souris, *Distribution of Distances between Elements in a Compact Set*, 2019. https://www.mdpi.com/2571-905X/3/1/1
