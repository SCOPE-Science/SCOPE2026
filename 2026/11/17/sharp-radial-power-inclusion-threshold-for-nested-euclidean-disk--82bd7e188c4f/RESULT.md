# Sharp radial-power inclusion threshold for nested Euclidean disks

## Finding
For a closed Euclidean disk \(D(c,r)\subset\mathbb R^2\), \(r>0\), and a real exponent \(p>-1\), set
\[
 W_p(D(c,r))=\int_{\partial D(c,r)}\|x\|_2^p\,d\mathcal H^1(x).
\]
The integral is finite, even if the circle passes through the origin. The following **sharp inclusion threshold** holds: for every \(p>-1\),
\[
 \bigl(\forall\ D(c,r)\subseteq D(C,R),\quad W_p(D(c,r))\le W_p(D(C,R))\bigr)
 \quad\Longleftrightarrow\quad p\ge0.
\]
For every \(p>0\), every proper inclusion gives a **strict** inequality, regardless of whether either disk contains the origin. At \(p=0\), it is the usual strict perimeter monotonicity. For every \(-1<p<0\), there exist properly nested positive-radius disks **both containing the origin** for which weighted perimeter *decreases*.

The newly proved positive range is \(0<p<1\); the previously established range \(p\ge1\) is explicitly credited to the convex-ridge theorem for disks. The negative-exponent construction supplies the sharp opposite boundary. The theorem does not assert inclusion monotonicity over arbitrary convex bodies.

## Assumptions and scope
All geometric measurements use standard Euclidean norm and one-dimensional Hausdorff measure, with no normalization of circumference. Disks are full-dimensional, closed, and have strictly positive radii; proper containment is \(D(c,r)\subsetneq D(C,R)\). For \(p<0\), the value at the origin is singular, but a circle through the origin has integrable power \(p>-1\). Only planar disks are considered. The primary mathematical classification is MSC2020 52A20.

For \(p\in(0,1)\), define
\[
 I_p(t)=\int_0^{2\pi}\bigl(1+t^2+2t\cos\theta\bigr)^{p/2}\,d\theta,\qquad t\ge0.
\]
Rotational symmetry and scaling give the exact identity
\[
 W_p(D(c,r))=r^{p+1}I_p(\|c\|_2/r).
\]

## Proof
**1. A positive derivative for fractional powers.** Fix \(0<p<1\), and write \(\alpha=p/2\). For \(0\le t<1\), multiplication of the absolutely convergent generalized binomial series and angular orthogonality yield
\[
 I_p(t)=2\pi\sum_{k=0}^\infty \binom{\alpha}{k}^{\!2}t^{2k}.
\]
Every summand is nonnegative, and the term of index one is positive. Thus \(I'_p(t)>0\) for \(0<t<1\), with \(I'_p(0)=0\). The integral defining \(I_p\) is differentiable at \(t=1\): near the potential zero of the integrand the differentiated integrand is bounded by a constant times \(|\theta-\pi|^p\), which is locally integrable. Directly substituting \(t=1\) gives \(I'_p(1)=(p/2)I_p(1)>0\).

**2. The decisive slope bound for \(t<1\).** Write \(X=1+t^2+2t\cos\theta\), and define
\[
 B_p(t)=\int_0^{2\pi}X^{\alpha-1}\,d\theta.
\]
Because \(X\mapsto X^{\alpha-1}\) is decreasing, the elementary reverse-Chebyshev covariance inequality for an arbitrary positive random variable gives
\[
 \frac1{2\pi}\int_0^{2\pi}X^{\alpha}\,d\theta
 \le\left(\frac1{2\pi}\int_0^{2\pi}X\,d\theta\right)
 \left(\frac1{2\pi}\int_0^{2\pi}X^{\alpha-1}\,d\theta\right).
\]
Indeed the covariance is half the expectation of \((X-X')(X^{\alpha-1}-{X'}^{\alpha-1})\le0\) for independent copies. As the average of \(X\) equals \(1+t^2\), we obtain \(B_p(t)\ge I_p(t)/(1+t^2)\).

Differentiation and the identity \(2t(t+\cos\theta)=X+t^2-1\) give
\[
 I'_p(t)=\frac{p}{2t}\bigl(I_p(t)+(t^2-1)B_p(t)\bigr).
\]
Because \(t<1\), the bound on \(B_p\), combined with Step 1, yields the *two-sided* estimate
\[
 0<I'_p(t)\le\frac{pt}{1+t^2}I_p(t),\qquad 0<t<1.
\]
Consequently, with \(J_p(t)=(p+1)I_p(t)-(t+1)I'_p(t)\),
\[
 J_p(t)\ge \left(p+1-\frac{pt(t+1)}{1+t^2}\right)I_p(t)
 \ge I_p(t)>0,\qquad0\le t\le1.
\]
The last inequality uses \(t(t+1)\le1+t^2\) for \(t\le1\); the endpoints follow by continuity.

**3. Outside the unit center-to-radius ratio.** For \(t>1\), set \(u=1/t<1\). The exact inversion identity is \(I_p(t)=t^pI_p(u)\). Differentiate to obtain
\[
 I'_p(t)=t^{p-1}\bigl(pI_p(u)-uI'_p(u)\bigr)>0,
\]
by the upper bound of Step 2. Furthermore,
\[
 J_p(t)=t^{p-1}\bigl((t-p)I_p(u)+(1+u)I'_p(u)\bigr)>0,
\]
where \(t>1>p\). We have therefore proved \(I'_p(t)\ge0\) and \(J_p(t)>0\) for every \(t\ge0\).

**4. Every nested pair, including moving centers.** Write \(D(c,r)\subseteq D(C,R)\). Elementary Euclidean geometry gives \(R-r\ge\|C-c\|_2\). Along the linear path
\[
 c_s=c+s(C-c),\qquad r_s=r+s(R-r),\qquad0\le s\le1,
\]
we have \(\|dc_s/ds\|_2\le dr_s/ds\). Wherever \(c_s\ne0\), let \(t_s=\|c_s\|_2/r_s\). The chain rule gives
\[
 \frac d{ds}W_p(D(c_s,r_s))
 =r_s^p\left[\frac{dr_s}{ds}\bigl((p+1)I_p(t_s)-t_sI'_p(t_s)\bigr)
 +\frac{\langle c_s,dc_s/ds\rangle}{\|c_s\|_2}I'_p(t_s)\right]
 \ge r_s^p\frac{dr_s}{ds}J_p(t_s).
\]
At a zero center the same inequality follows by continuity since \(I'_p(0)=0\). Proper containment implies \(R>r\), so \(dr_s/ds=R-r>0\), and the derivative is strictly positive throughout. This proves the new claim for all \(0<p<1\). For \(p=0\), the identity \(W_0(D(c,r))=2\pi r\) proves strictness. The published convex-ridge theorem [3] establishes the corresponding disk result for all \(p\ge1\); combining it with the new fractional range gives sufficiency for every \(p\ge0\).

**5. Failure for *every* integrable negative power.** Fix \(-1<p<0\), and consider \(I_p(t)\) at \(t=1-\delta\), \(\delta\downarrow0\). Near \(\theta=\pi+y\),
\[
 X=\delta^2+2(1-\delta)(1-\cos y),\qquad
 t+\cos\theta=-\delta+(1-\cos y).
\]
For \(|y|\le\delta\), the differentiated integrand \(p(t+\cos\theta)X^{p/2-1}\) is positive and its integral is bounded below by a positive multiple of \(\delta^p\), which diverges. Wherever the differentiated integrand is negative, \(1-\cos y\ge\delta\), and its absolute value is at most a constant times \(|y|^p\), whose integral remains bounded uniformly in \(\delta\) because \(p>-1\). Thus
\[
 I'_p(1-\delta)\longrightarrow+\infty,
 \qquad I_p(1-\delta)=O_p(1).
\]
The second bound follows from \(X\ge c y^2\) and the integrability of \(|y|^p\). Consequently \(J_p(t)<0\) for some \(t\in(0,1)\) sufficiently close to one. For such a \(t\), set
\[
 A=D((t,0),1),\qquad B_\varepsilon=D((t-\varepsilon,0),1+\varepsilon).
\]
For all sufficiently small positive \(\varepsilon\), these are properly nested and both contain the origin in their interiors. Differentiating at \(\varepsilon=0\) gives
\[
 \left.\frac d{d\varepsilon}W_p(B_\varepsilon)\right|_{\varepsilon=0}=J_p(t)<0,
\]
so \(W_p(B_\varepsilon)<W_p(A)\). This excludes every \(-1<p<0\) and completes the sharp threshold.

## Verification
The standalone `verify.py` runs deterministic midpoint quadrature tests on the fractional exponent range, compares both sides of the key derivative inequalities, and checks hundreds of independently generated nested-disk pairs. It also checks the negative-exponent contact behavior diagnostically. Execute `python verify.py` with Python 3 standard library; one execution passed 593 assertions. The numerical calculations are finite consistency tests, not a proof of the universal inequalities. Steps 1–5 supply the analytical proof.

## Relationship to prior work
Csató and Giovagnoli [1] prove monotonicity of increasing radial weighted perimeter for convex bodies under the extra condition that the smaller body contains the weight origin. This is inapplicable to the nested disks here that may both miss the origin. Saracco and Stefani [2] characterize weights monotone under *all* convex-body inclusions; that stronger geometric requirement does not provide the present disk-specific sharp exponent classification.

The published disk-specific convex-ridge theorem [3] already proves all radial powers \(p\ge1\) for nested disks without origin restrictions. Its published text explicitly leaves \(0<p<1\) untreated; in that interval the one-dimensional ridge power is concave rather than convex, so its stated argument does not imply the present result. The fixed-center expanding-sphere monotonicity result [4] establishes monotonicity for \(p\ge0\) while *holding the center fixed*, not while arbitrary disk centers move under inclusion. The origin-contained outer-parallel weighted-perimeter result [5] likewise does not settle the unrestricted moving-center problem. The present new proof resolves the missing fractional range and makes the disk exponent threshold exact, including failures for negative powers.

## Limitations
The claim is restricted to Euclidean disks in dimension two, and \(p>-1\) is required for finiteness at a circle crossing the weight origin. The arguments do not establish monotonicity of fractional-power weighted perimeters under inclusion for arbitrary convex bodies or for arbitrary increasing radial weights. Historical novelty is based on accessible primary results, published mathematical records, and targeted searches, not a guarantee that every differently named inequality has been indexed. The full manuscript of [1] was not available to inspect here; its stated origin-contained hypothesis was corroborated through accessible mathematical literature. Independent external mathematical audit has not been performed.

## References
1. G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1, first public October 8, 2026, https://arxiv.org/abs/2610.11677 .
2. G. Saracco and G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, arXiv:2306.07770 (2023), Math. Nachr. 297 (2024), 1444–1450, https://doi.org/10.1002/mana.202300280 .
3. *Convex ridge weights restore inclusion monotonicity on nested circles*, publicly accessible November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-convex-ridge-weights-restore-inclusion-monotonicity-on-nested-ci--cea80ae7d678 .
4. *A sharp radial-power threshold and universal cusp for expanding translated spheres*, publicly accessible October 25, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-radial-power-threshold-and-universal-cusp-for-expanding--f628e9f7823f .
5. *Sharp Hausdorff Lipschitz constants for radial-subharmonic weighted perimeters*, publicly accessible October 18, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-hausdorff-lipschitz-constants-for-radial-subharmonic-weigh--a7dba9412443 .
