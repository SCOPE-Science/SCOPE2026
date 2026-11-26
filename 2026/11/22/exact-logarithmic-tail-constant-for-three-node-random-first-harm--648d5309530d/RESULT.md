# Exact logarithmic tail constant for three-node random first-harmonic quadrature

## Finding

Let \(\Theta_1,\Theta_2,\Theta_3\) be independent uniform angles in \([0,2\pi)\), and let the unique real weights \(w_1,w_2,w_3\) satisfy
\[
\sum_{j=1}^3 w_j=1,\qquad
\sum_{j=1}^3 w_j\cos\Theta_j=\sum_{j=1}^3 w_j\sin\Theta_j=0.
\]
The weights exist almost surely. For their Euclidean norm \(W=(\sum_{j=1}^3w_j^2)^{1/2}\), the exact sharp tail is
\[
\boxed{\lim_{T\to\infty}\frac{T}{\log T}\,\mathbb P\{W>T\}=\frac{3\sqrt2}{\pi^2}.}
\]
In particular, for every \(p>0\), \(\mathbb E W^p<\infty\) exactly when \(p<1\). If independent, centered sample-observation errors have common variance \(\sigma^2>0\), the conditional quadrature noise variance is \(\sigma^2 W^2\). The unconditional noise has infinite second moment and no well-defined mean. For comparison, the probability that all three exactness weights are strictly positive is exactly \(1/4\); that familiar geometric consequence is not asserted as the new contribution.

## Assumptions and scope

Quadrature represents the normalized circle integral \((2\pi)^{-1}\int_0^{2\pi}f(\theta)\,d\theta\) and is exact on \(\operatorname{span}\{1,\cos\theta,\sin\theta\}\). The three node angles are independently and continuously uniform, without stratification, separation, resampling or imposed positivity. The completed weights are the unique interpolatory weights; no alternate choice of positive feasible weights is optimized. The limit holds for a fixed sample count of three. Moment statements concern the norm of weights under node randomness. Measurement errors are independent of nodes and of one another for the variance consequence.

## Proof

**1. Exact cyclic-gap formula and probability density.** Rotate the labelled first sample to zero and sort the other two samples counterclockwise at \(a,a+b\), with strictly positive gaps \(a,b,c=2\pi-a-b\) almost surely. The other two angles relative to the first are still independent uniform angles. Thus the density of their ordered values on the ordered triangle is \(2/(2\pi)^2\); the gap change of variables has unit Jacobian and gives density \(1/(2\pi^2)\) on \(a>0,b>0,a+b<2\pi\). Solving the moment equations gives the cyclically ordered weight triple
\[
(w_1,w_2,w_3)=\frac{(\sin b,\sin c,\sin a)}{\sin a+\sin b+\sin c},
\quad \sin a+\sin b+\sin c=4\sin\frac a2\sin\frac b2\sin\frac c2>0.
\]
Therefore \(W=\sqrt{\sin^2a+\sin^2b+\sin^2c}/(\sin a+\sin b+\sin c)\), a cyclically symmetric continuous function on the open simplex. Positivity requires all three gaps to be smaller than \(\pi\). The events that one gap exceeds \(\pi\) are disjoint and each has probability \(1/4\), establishing the stated positive-weight probability.

**2. Localization of the large-norm event.** Fix an angular cutoff \(0<\delta<\pi/4\) and take the three disjoint corners defined by \(a+b<\delta\), \(b+c<\delta\), or \(c+a<\delta\). On their complement at most one gap is less than \(\delta/2\). The closed interior where every gap is at least \(\delta/2\) has bounded \(W\). If \(0<a<\delta/2\) and the other two gaps are at least \(\delta/2\), both lie in \([\delta/2,2\pi-\delta/2]\). The sine formula gives \(W\le C_\delta/a\), and cyclically the same bound holds with another gap as the small parameter. The regions where these bounds exceed \(T\) have area \(O_\delta(T^{-1})\). Thus only the three corners can contribute to the coefficient of \((\log T)/T\).

**3. Universal corner asymptotic.** At the corner \(a,b>0\), \(a+b=r<\delta\), set \(x=a/(a+b)\in(0,1)\). Taylor expansion, uniformly for all \(x\in(0,1)\), gives
\[
W=\frac{2\sqrt{2(x^2-x+1)}}{r^2x(1-x)}\bigl(1+O(\delta^2)\bigr).
\]
The relative error is uniform even as \(x\) approaches the endpoints: factor the denominator into its three half-angle sines and use the inequality \(\sin t/t=1+O(\delta^2)\) for all three small angles; similarly the squared-sine numerator differs by a relative \(O(\delta^2)\) from \(a^2+b^2+(a+b)^2\). Put
\[
H(x)=\frac{\sqrt{2(x^2-x+1)}}{x(1-x)}.
\]
The area of the corresponding *homogeneous* superlevel set inside \(0<r<\delta\), using the Jacobian \(da\,db=r\,dr\,dx\), is exactly
\[
\frac1T\int_0^1\min\left\{\frac{T\delta^2}{2},H(x)\right\}\,dx.
\]
As \(x\downarrow0\), \(H(x)=\sqrt2/x+O(1)\), and as \(x\uparrow1\), \(H(x)=\sqrt2/(1-x)+O(1)\). Splitting the integral into these two endpoint regions and their compact complement, and integrating \(\min\{K,\sqrt2/x\}\), gives
\[
\int_0^1\min\left\{\frac{T\delta^2}{2},H(x)\right\}\,dx
=2\sqrt2\log T+O_\delta(1).
\]
The uniform relative-error estimate squeezes the true corner area between homogeneous areas at the thresholds \(T/(1\pm C\delta^2)\). After division by \((\log T)/T\), its limiting inferior and superior are between \(2\sqrt2(1-C\delta^2)\) and \(2\sqrt2(1+C\delta^2)\). The three corners have identical contributions by cyclic symmetry. Multiply by gap density \(1/(2\pi^2)\) and then let \(\delta\downarrow0\), obtaining \(3\cdot2\sqrt2/(2\pi^2)=3\sqrt2/\pi^2\), as claimed.

**4. Moment and noise consequences.** The tail-integral identity \(\mathbb E W^p=p\int_0^\infty T^{p-1}\mathbb P(W>T)\,dT\) for \(p>0\) gives the sharp integrability threshold \(p<1\), since the tail is asymptotic to a positive constant times \((\log T)/T\). Write \(Y=w\cdot\varepsilon\) for the noise contribution of the observation errors \(\varepsilon\). Conditionally on the nodes, the mean is zero and the second moment is \(\sigma^2 W^2\), so the unconditional second moment is infinite. To see why unconditional centering is not available, the function \(u\mapsto \mathbb E|u\cdot\varepsilon|\) on the Euclidean unit sphere is continuous, by the bound \(\mathbb E\|\varepsilon\|_2<\infty\). It is strictly positive at every unit \(u\) because \(\operatorname{Var}(u\cdot\varepsilon)=\sigma^2>0\). Its minimum is therefore positive. Conditional on the nodes, \(\mathbb E(|Y|\mid\Theta)\) is at least that minimum times \(W\), so \(\mathbb E|Y|=\infty\). The conditional positive and negative parts have equal expectations, since the conditional mean is zero; integrating gives \(\mathbb E Y^+=\mathbb E Y^-=\infty\) and hence no unconditional mean. This does not assert that a particular deterministic input function necessarily suffers a divergent quadrature error. \(\square\)

## Verification

The accompanying `verify.py` checks the trigonometric weight formula against independent numerical solutions of the moment equations, checks near-corner normalization at several length scales, and evaluates the homogeneous-region integral numerically to test its predicted logarithmic coefficient. These are finite diagnostics; the infinite limit follows from the area-decomposition argument above. The diagnostic uses Python and NumPy 2.0 or later (`python verify.py`).

## Relationship to prior work

Bělík, Narayan and Turnage (2026, Theorem 6) establish stability of intermediate randomized least-squares quadrature rules with high probability under admissibility, reference-weight concentration and sample-size conditions. At exactly three independent circle nodes, no oversampling or positivity safeguard is imposed; the present question is the exact *rare-event* tail constant of the unique first-harmonic weights.

Xu and Shen (2026, Theorems 1 and 6) give an inverse-singular-value representation of reconstruction risk and prove divergence of expected reconstruction risk under independent uniform sampling. That concerns full spectral recovery rather than the weight norm of the normalized *quadrature functional*. *Critical inverse moments and logarithmic tails of random Fourier interpolation* (2026) proves two-sided bounds of order \((\log T)/T\) for the inverse-Frobenius norm at three nodes but does not give its exact leading constant. Bounds on that full-matrix norm do not determine the exact constant for a row functional. A sharp two-gap logarithmic tail for *polynomial point evaluation on an interval* also uses three independent nodes, but its leading coefficient depends on the evaluation point. The trigonometric quadrature result on stratified bounded jitters uses a different node law and has a different moment threshold. These comparisons distinguish the exact coefficient here; they cannot rule out all earlier unindexed equivalent formulas.

## Limitations

The exact coefficient is for one fixed sample count, independent uniform full-circle nodes, normalized circle integration, and the Euclidean norm of the **interpolatory** first-harmonic weights. It is not the inverse-Frobenius norm of the full Fourier sampling matrix, and does not cover overdetermined, separated, jittered or positivity-optimized quadrature. A full-text historical priority comparison with all possibly relevant sources has not been completed. Independent mathematical review has not been performed.

## References

1. F. Bělík, A. Narayan and J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506, first public 2026-09-08. https://arxiv.org/abs/2609.09506
2. H. Xu and Y. Shen, *Non-asymptotic Analysis of Expected Reconstruction Risk for Trigonometric Polynomial Models*, arXiv:2609.29286, first public 2026-09-24. https://arxiv.org/abs/2609.29286
3. *Critical inverse moments and logarithmic tails of random Fourier interpolation* (2026). https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-critical-inverse-moments-and-logarithmic-tails-of-random-fourier--323dcae74731/RESULT.md
4. *Sharp positivity and logarithmic noise barrier in three-node perturbed trigonometric quadrature* (2026). https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-sharp-positivity-and-logarithmic-noise-barrier-in-three-node-per--fd84114e8959/RESULT.md
5. *A logarithmic collision tail for three-node random quadratic interpolation* (2026). https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-a-logarithmic-collision-tail-for-three-node-random-quadratic-int--31e79eafd4fb/RESULT.md
