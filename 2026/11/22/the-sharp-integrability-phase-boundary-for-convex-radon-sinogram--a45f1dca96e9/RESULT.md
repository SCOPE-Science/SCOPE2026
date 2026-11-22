# The sharp integrability phase boundary for convex Radon sinograms on Euclidean balls

## Finding

Let \(d\ge2\) be an integer, let \(B_d=\{x\in\mathbb R^d:|x|<1\}\), and write \(\mathcal R f(\theta,t)\) for the ordinary hyperplane Radon transform of the zero extension of a real function \(f\in L^1(B_d)\), with hyperplane measure \(d\mathcal H^{d-1}\). Call \(f\) *section-convex* if, for almost every \(\theta\in S^{d-1}\), the function \(t\mapsto\mathcal R f(\theta,t)\), initially defined almost everywhere, agrees with a finite convex function on \((-1,1)\).

**Theorem.** For every \(1\le p\le\infty\), a nonzero real section-convex \(f\in L^p(B_d)\) exists **if and only if**
\[
  d\in\{2,3\}\quad\text{or}\quad(d=4\text{ and }1\le p<2).
\]
In particular, in dimension four the Hilbert exponent \(p=2\) is the sharp, excluded endpoint; in every dimension at least five, no nonzero integrable example exists, even without radiality, smoothness, or a sign condition on \(f\).

For \(d=2,3,4\), explicit witnesses are
\[
 f_d(x)=-(1-|x|^2)^{(3-d)/2}\quad (|x|<1),
 \qquad\mathcal R f_d(\theta,t)=-C_d(1-t^2)\quad (|t|<1),
\]
where
\[
 C_d=\frac{\pi^{(d-1)/2}\Gamma((5-d)/2)}{\Gamma(2)}
  =\begin{cases}\pi/2,&d=2,\\\pi,&d=3,\\\pi^2,&d=4.\end{cases}
\]
Thus the section profiles are strictly convex, and \(f_4\in L^p(B_4)\) holds precisely for \(1\le p<2\).

A quantitative structural ingredient is that if \(d\ge3\) and a nonzero integrable section-convex function has a convex profile \(g_\theta\) in almost every direction, then
\[
 \int_{S^{d-1}}|g_\theta(t)|\,d\sigma(\theta)
 \ge (1-t)\int_{S^{d-1}}|g_\theta(0)|\,d\sigma(\theta)>0
 \quad(0\le t<1),
\]
where \(d\sigma\) is ordinary sphere surface measure; the last integral is strictly positive, possibly infinite. For the dimensions and integrability exponents ruled out in the theorem, the same left side is \(o(1-t)\) as \(t\uparrow1\), giving the contradiction.

## Assumptions and scope

Hyperplanes are \(H_{\theta,t}=\{x\in\mathbb R^d:x\cdot\theta=t\}\), \(\theta\in S^{d-1}\), and
\[
\mathcal R f(\theta,t)=\int_{H_{\theta,t}}f(x)\,d\mathcal H^{d-1}(x).
\]
The zero extension is supported in the unit ball. The transform is defined for almost every \((\theta,t)\) by Fubini; the convex representative in a given direction, when it exists, is unique by continuity. Convexity is required only on the open interval \((-1,1)\), never across its zero extension to all \(\mathbb R\). Real-valuedness is necessary for the order relation in convexity. For finite-measure balls, \(L^p(B_d)\subset L^1(B_d)\) for every \(p\ge1\). No positivity, radiality, differentiability, or boundary trace is assumed for the nonexistence statement.

## Proof

**1. Explicit construction and exact integrability.** For any dimension \(d\ge2\) and real \(\alpha>-1\), put \(h_{d,\alpha}(x)=-(1-|x|^2)^\alpha\) inside \(B_d\). Writing \(x=t\theta+y\), with \(y\in\theta^\perp\), and using polar integration in \(\mathbb R^{d-1}\),
\[
\begin{aligned}
\mathcal R h_{d,\alpha}(\theta,t)
 &=-\int_{|y|<\sqrt{1-t^2}}(1-t^2-|y|^2)^\alpha\,dy\\
 &=-\frac{\pi^{(d-1)/2}\Gamma(\alpha+1)}{\Gamma(\alpha+(d+1)/2)}
 (1-t^2)^{\alpha+(d-1)/2}.
\end{aligned}
\]
Take \(\alpha=(3-d)/2\); this is greater than \(-1\) exactly when \(d<5\), and the exponent of \(1-t^2\) becomes one. The stated constants and strictly positive second derivative \(2C_d\) follow. Near the boundary, polar coordinates show
\[
 \|h_{d,\alpha}\|_p^p<\infty\quad\Longleftrightarrow\quad
 \alpha p>-1\qquad(1\le p<\infty),
\]
where \(\alpha=0\) is harmless, and \(h_{d,\alpha}\in L^\infty\) when \(\alpha\ge0\). These facts give every existence case in the theorem.

**2. An angular boundary-layer estimate for arbitrary integrable functions.** Fix \(d\ge3\) and \(0<t<1\). By the hyperplane/coarea identity, the spherical integral of the absolute Radon transform is bounded by
\[
\begin{aligned}
 A_f(t)&:=\int_{S^{d-1}}|\mathcal R f(\theta,t)|\,d\sigma(\theta)\\
 &\le |S^{d-2}|\int_{\{t<|x|<1\}}
  \frac{|f(x)|}{|x|}
 \left(1-\frac{t^2}{|x|^2}\right)^{(d-3)/2}dx.
\end{aligned}
\tag{1}
\]
To see the kernel, rotate a nonzero \(x\) to the pole, write \(r=|x|\), and integrate \(\delta(t-r\cos\varphi)\) over \(S^{d-1}\); the resulting density is
\[
\frac{|S^{d-2}|}{r}\left(1-\frac{t^2}{r^2}\right)^{(d-3)/2}
\mathbf 1_{\{|t|<r\}}.
\]
This computation is a coarea identity and is valid for integrable \(f\) for almost every \(t\). If \(1/2<t<1\), then \(r^{-1}<2\) and \(0<1-t^2/r^2\le4(1-t)\). Hence
\[
 A_f(t)\le K_d(1-t)^{(d-3)/2}
 \|f\mathbf1_{\{|x|>t\}}\|_1,
 \qquad K_d=2\,|S^{d-2}|\,4^{(d-3)/2}.
\tag{2}
\]
As \(t\uparrow1\), the terminal shell integral tends to zero for every \(f\in L^1\). Therefore, for \(d\ge5\),
\[
 A_f(t)=o(1-t).
\tag{3}
\]
In \(d=4\), if \(f\in L^2(B_4)\), Hölder and the unit-ball shell-volume estimate give
\[
\|f\mathbf1_{\{|x|>t\}}\|_1
\le |\{t<|x|<1\}|^{1/2}
\|f\mathbf1_{\{|x|>t\}}\|_2
=o((1-t)^{1/2}).
\]
Equation (2) again gives (3). All higher \(L^p\) spaces, including \(L^\infty\), embed in \(L^2(B_4)\). The same estimates apply at the left endpoint because \(\mathcal R f(\theta,-t)=\mathcal R f(-\theta,t)\).

**3. A rigidity lemma for convex section profiles.** Suppose \(f\in L^1(B_d)\) is section-convex and (3) holds. The unique finite convex representatives \(g_\theta\) are measurable in \(\theta\) at each interior \(t\), as they can be recovered by limits of local averages of the jointly measurable Radon transform. By Fubini, (3) holds with \(\mathcal R f\) replaced by \(g_\theta\) for almost every \(t\) arbitrarily close to \(\pm1\).

Choose sequences of such \(t\)'s approaching each endpoint. Every finite convex function on an open bounded interval has one-sided endpoint limits in \(\mathbb R\cup\{+\infty\}\) (it is bounded below by any interior supporting affine function). Fatou's lemma and \(A_f(t)\to0\) show that these limits are zero for almost every \(\theta\) at both endpoints. Convexity then places \(g_\theta(t)\) below the chord joining its two zero endpoint limits, so \(g_\theta(t)\le0\) for every \(-1<t<1\). Furthermore, for \(0\le t<1\), the chord between \((0,g_\theta(0))\) and \((1,0)\) gives
\[
 -g_\theta(t)\ge(1-t)(-g_\theta(0)).
\tag{4}
\]
Integrating (4) and applying (3), we obtain \(\int_{S^{d-1}}(-g_\theta(0))\,d\sigma=0\); thus \(g_\theta(0)=0\) almost everywhere. A convex function with zero values at the two endpoints and an interior point must vanish identically: equality in the midpoint convexity/chord inequality forces affinity on either side and therefore throughout. Consequently \(\mathcal R f(\theta,t)=0\) for almost every \((\theta,t)\). The Fourier slice identity and uniqueness of the Fourier transform of an \(L^1\) function give \(f=0\) almost everywhere.

Applying this lemma to (3) proves nonexistence for \(d\ge5\) in \(L^1\), and for \(d=4\) in \(L^2\). Together with Step 1 and the inclusions of \(L^p\) spaces on a finite-volume ball, the theorem follows.

## Verification

The standalone file `verify.py` uses exact symbolic Gamma/Beta reduction to check the constants \(C_2=\pi/2\), \(C_3=\pi\), \(C_4=\pi^2\), that the Radon power is exactly one, the critical radial integrability exponents, and the angular-kernel exponents for sample dimensions. Running `python verify.py` exits successfully with `Radial constants, convexity, critical exponents and spherical kernel: PASS`. The all-dimension, all-data impossibility conclusion is established by inequalities (1)–(4) and Radon injectivity, not by finite computation; the checker is supplemental.

## Relationship to prior work

Hansen, arXiv:2603.10804v1 (first public March 11, 2026), proves polyhomogeneous boundary mapping rules for the ball Radon transform, including that a radial boundary exponent \(\alpha\) produces section decay exponent \(\alpha+(d-1)/2\). Its Theorem 1 is consistent with the construction in Step 1 and already encompasses the power-weight exponent calculation for polyhomogeneous data, but does **not** state or imply the complete arbitrary-\(L^p\) convexity existence/nonexistence classification: no convex sign assumption or angular-averaged rigidity is imposed there.

Iosevich and Liflyand, arXiv:2611.22521v1 (first public November 17, 2026), study convex Radon transforms and Fourier estimates on slabs and bounded convex sets. Their Section 6.2 gives the planar example \(-\sqrt{1-|x|^2}\) and its quadratic chord profile; that example is therefore **not claimed as new**. Their Theorem 6.4 is a Fourier integrability estimate for \(W^{1,1}\) data with convex Radon sections, not the present all-dimensional \(L^p\) existence phase boundary. This later paper was used for coverage comparison, not for establishing eligibility of the motivating source. Other Radon stability and classical Fourier slice results concern mapping norms and invertibility rather than this universal convexity obstruction.

## Limitations

The domain is the Euclidean unit ball; no result is asserted for general convex bodies. Convexity must hold for almost every direction and across the whole interval \((-1,1)\), not just on a subinterval. The theorem concerns real, not complex, functions. It does not characterize every convex-section function in the allowable dimensions or optimal norms within those classes. The proof uses standard Radon/Fourier injectivity and is mathematical, not an independent audit or an assertion that exhaustive literature coverage has been achieved. A not-yet-indexed equivalent theorem remains possible.

## References

1. S. Hansen, *Polyhomogeneous mapping properties of the Radon transform and backprojection operator on the unit ball*, arXiv:2603.10804v1, first public March 11, 2026. https://arxiv.org/html/2603.10804v1
2. A. Iosevich and E. Liflyand, *Subharmonic functions and convexity of the Radon transform, with applications to the Fourier transform*, arXiv:2611.22521v1, first public November 17, 2026. https://arxiv.org/html/2611.22521v1
3. S. Kindermann and S. Hubmer, *Norms in sinogram space and stability estimates for the Radon transform*, arXiv:2403.07466v1 (first public March 12, 2024), *Inverse Problems* 41 (2025), 025008. https://arxiv.org/abs/2403.07466
