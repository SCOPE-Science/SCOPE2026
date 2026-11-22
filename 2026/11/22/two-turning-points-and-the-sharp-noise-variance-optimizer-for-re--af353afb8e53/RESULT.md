# Two turning points and the sharp noise-variance optimizer for reflection-symmetric three-bin histograms

## Finding

Let \(X=(X_1,X_2,X_3)\sim\operatorname{Mult}(N;a,1-2a,a)\), where \(N\) is a positive integer and \(0<a<1/2\). Define the matched-reference discrete roughness
\[
T_{N,a}=\left|X_2-X_1-N(1-3a)\right|+\left|X_3-X_2-N(3a-1)\right|.
\]
Its asymptotic variance coefficient \(V(a)=\lim_{N\to\infty}N^{-1}\operatorname{Var}(T_{N,a})\) exists. On the entire open interval \(0<a<1/2\), **\(V\) has exactly two stationary points**. The first, at \(a_-=0.240033242514835856\ldots\), is the unique strict global maximizer, with \(V(a_-)=0.684872023385757119\ldots\); the second, at \(a_+=0.474914471760339773\ldots\), is a strict local minimum, with \(V(a_+)=0.282216149055267041\ldots\). Thus the leading null variance first rises, then falls, then rises again as the equal endpoint masses approach \(1/2\).

These locations are **exactly characterized**, without reliance on the decimal approximations, by the two distinct roots of the function \(H\) in the intervals \((-4/5,0)\) and \((0,1)\), defined below. The limiting boundary values are \(V(0)=0\) and \(V(1/2)=1-2/\pi\), so neither boundary displaces the interior global maximum. The center mass at that maximum is \(1-2a_-=0.519933514970328287\ldots\).

## Assumptions and scope

The bin ordering is fixed as \(1,2,3\), and the reference is the *true* multinomial probability vector, not an alternative. The sample size \(N\) tends to infinity with \(a\) fixed; the theorem does not assert that the same optimizer maximizes the finite-\(N\) variance for each \(N\), nor does it optimize over nonsymmetric three-bin profiles. Endpoint values refer to the continuous extensions of the limiting coefficient and are not covered by the strictly positive-bin formulation.

This minimal reflection-symmetric three-bin family is a natural calibration testbed for a roughness statistic with two interacting adjacent differences. The exact maximizing null shape and the unexpected second turning point determine how its Gaussian-scale noise depends on the center-to-endpoint mass contrast.

## Proof

**1. Gaussian limit and exact edge covariance.** The multinomial sample is a sum of \(N\) independent categorical vectors. By the multivariate central limit theorem, its centered, scaled count vector tends to a Gaussian vector with covariance \(\operatorname{diag}(p)-pp^\top\). Writing the two centered adjacent differences as \(D_1\) and \(D_2\), their limiting variances are equal and their covariance is
\[
 v(a)=a(5-9a),\qquad c(a)=a(9a-4).
\]
Indeed the diagonal variance is \((a+(1-2a))-((1-2a)-a)^2\), and the covariance is \(-(1-2a)-((1-2a)-a)(a-(1-2a))\). Therefore the Gaussian correlation is
\[
 r(a)=\frac{9a-4}{5-9a},\qquad r'(a)=\frac{9}{(5-9a)^2}>0.
\]
It runs bijectively from \(-4/5\) to \(1\) as \(a\) runs from \(0\) to \(1/2\). Positive definiteness follows from \(v(a)^2-c(a)^2=9a^2(1-2a)>0\).

The scaled statistic \(T_{N,a}/\sqrt N\) converges in law to \(|Y_1|+|Y_2|\), where \(Y_1,Y_2\) are centered Gaussian with the covariance above. Their standardized fourth moments are uniformly bounded in \(N\), since they are sums of bounded independent centered categorical increments. Hence the squares of the scaled statistics are uniformly integrable, so their variances converge and the asserted limit \(V(a)\) exists.

**2. Folded-Gaussian variance.** For two standard jointly Gaussian variables with correlation \(r\),
\[
 \mathbb E(|G_1G_2|)=\frac2\pi\bigl(\sqrt{1-r^2}+r\arcsin r\bigr).
\]
For completeness, differentiation in \(r\) of the Gaussian joint-density integral followed by integration by parts gives derivative \(\mathbb E(\operatorname{sgn}G_1\operatorname{sgn}G_2)=2\arcsin(r)/\pi\); integration from \(r=0\), where \(\mathbb E|G_1G_2|=2/\pi\), proves the identity. Consequently
\[
 V(a)=2v(a)\left[1-\frac4\pi+\frac2\pi\left(\sqrt{1-r(a)^2}+r(a)\arcsin r(a)\right)\right].\tag{1}
\]
No asymptotic remainder from a previous theorem is needed for this limiting identity.

**3. A strictly convex derivative numerator.** Invert the correlation parametrization:
\[
 a=\frac{5r+4}{9(1+r)},\qquad v(a)=\frac{5r+4}{9(1+r)^2}.
\]
Put
\[
 G(r)=\frac\pi2-2+\sqrt{1-r^2}+r\arcsin r,
 \quad H(r)=(5r+4)(1+r)\arcsin r-(5r+3)G(r).
\]
Equation (1) becomes
\[
 V(r)=\frac4{9\pi}\frac{5r+4}{(1+r)^2}G(r),\qquad
 \frac{\mathrm d V}{\mathrm dr}=\frac4{9\pi}\frac{H(r)}{(1+r)^3}.
\]
Since \(G'(r)=\arcsin r\), direct differentiation and simplification give the strict-convexity identity
\[
 H''(r)=\frac{(1+r)(15+4r-10r^2)}{(1-r^2)^{3/2}}>0\qquad(-4/5<r<1).\tag{2}
\]
The quadratic is concave and positive at both ends of \([-4/5,1]\), hence positive throughout. The relevant signs are
\[
 H(-4/5)=\frac\pi2-\frac75+\frac45\arcsin(4/5)>0,\quad
 H(0)=-3\left(\frac\pi2-1\right)<0,\quad
 H(1)=\pi+16>0.
\]
Here endpoint signs mean one-sided limits. By continuity there is a root in each of \((-4/5,0)\) and \((0,1)\). A strictly convex function cannot have three distinct zeroes: if three existed, strict convexity at the middle one would force its value below zero. Hence these are the only two roots. By the displayed derivative formula and the positive derivative of \(r(a)\), the signs of \(V'(a)\) are \(+,-,+\) on the three intervals cut out by those roots. Thus the first is a strict local maximum, and the second a strict local minimum.

**4. Global optimality.** At \(a=0\) the limiting variance is zero. At \(a=1/2\) the two Gaussian edge variables coincide, each with variance \(1/4\), whence \(V(1/2)=1-2/\pi\). At the admissible trial point \(a=1/4\), each edge variance is \(11/16\) and the covariance of the absolute values is nonnegative: for a Gaussian pair the folded covariance factor \(\sqrt{1-r^2}+r\arcsin r-1\) is nonnegative because it is even and increases on \([0,1]\). Thus
\[
 V(1/4)\ge\frac{11}{8}\left(1-\frac2\pi\right)>V(1/2).
\]
Since the only interior local maximum is the first root, and it exceeds both boundary values, it is the unique global maximum on the closed limiting parameter interval. Numerical values can be reproduced by the accompanying checker, but none is needed for the uniqueness or global comparison proof.

## Verification

Run `python3 verify.py` from the extracted package directory. The script (standard library only) checks the covariance identities from independent categorical one-step support, positivity of the quadratic in (2), root brackets and stationary values, boundary comparisons, and exact rational multinomial moments at several finite sample sizes. It does not substitute finite testing for the calculus proof of exactly two stationary points. The proof establishes the infinite family directly.

## Relationship to prior work

Banić and Elezović, *Discrete total variation under the multinomial, Part 4* (arXiv:2611.09592v1, first public 2026-11-06), determine the general fixed-bin Gaussian-scale variance coefficient, including the special treatment of three bins in §6. Their §4.2 treats period-two symmetric combs with **even bin count**, a different family; neither that section nor their three-bin treatment classifies optimizer locations or the two-turning-point structure along the reflection-symmetric three-bin probability path. Their general formula is compatible with, and can alternatively be specialized to obtain, equation (1), but the global extremum and strict-convexity result in steps 3–4 require further analysis.

Banić and Elezović, *Part 5: cyclic total variation* (arXiv:2611.14735v1, first public 2026-11-10), study a statistic with a third wrap-around edge, and do not imply this two-edge optimization. Classical Hoel–Kamat mean absolute successive-difference variance work addresses the uniform normal benchmark, not the parameter optimization here. Related published probability findings on histogram large deviations, uniform fixed-sample corrections, and alternating multinomial local power concern different questions and do not compare leading matched-null variance over this one-parameter profile.

## Limitations

The optimizer is exact only for the asymptotic variance coefficient on the specified reflection-symmetric three-bin family. The result does not claim a sharp maximizing probability vector over the whole two-dimensional three-bin simplex, a finite-sample global optimizer, a test power optimum, or an optimal universal critical threshold. Its limiting coefficient is implied numerically by the existing general moment theorem; the additional assertion is the complete and analytically proved shape/optimizer classification. Historical results not found in the literature checks may still contain the same parameter optimization.

## References

1. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 4: variance under a general distribution*, arXiv:2611.09592v1, first submitted November 6, 2026. https://arxiv.org/abs/2611.09592
2. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 5: cyclic total variation*, arXiv:2611.14735v1, first submitted November 10, 2026. https://arxiv.org/abs/2611.14735
3. S. Nabeya, *Absolute moments in 2-dimensional normal distribution*, Annals of the Institute of Statistical Mathematics 3 (1951), 2–6.
4. P. G. Hoel, *The efficiency of the mean moving range*, Annals of Mathematical Statistics 17 (1946), 475–482; A. R. Kamat, *On the mean successive difference and its ratio to the root mean square*, Biometrika 40 (1953), 116–127.
