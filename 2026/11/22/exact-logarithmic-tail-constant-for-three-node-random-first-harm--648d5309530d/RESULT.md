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
In particular, for every \(p>0\), \(\mathbb E W^p<\infty\) exactly when \(p<1\). If independent, centered sample-observation errors have common variance \(\sigma^2>0\), their conditional quadrature error variance is \(\sigma^2 W^2\) and their unconditional noise variance is infinite. For comparison, the probability that all three exactness weights are strictly positive is exactly \(1/4\); that familiar geometric consequence is not asserted as the new contribution.

## Assumptions and scope

Quadrature represents the normalized circle integral \((2\pi)^{-1}\int_0^{2\pi}f(\theta)\,d\theta\) and is exact on \(\operatorname{span}\{1,\cos\theta,\sin\theta\}\). The three node angles are independently and continuously uniform, without stratification, separation, resampling or imposed positivity. The completed weights are the unique interpolatory weights; no alternate choice of positive feasible weights is optimized. The limit holds for a fixed sample count of three. Moment statements concern the norm of weights under node randomness. Measurement errors are independent of nodes and of one another for the variance consequence.

## Proof

**1. Exact cyclic-gap formula and probability density.** Rotate the circle so the three points in cyclic order are \(0,a,a+b\), with strictly positive gaps \(a,b,c=2\pi-a-b\). Exchangeability and rotational invariance imply that \((a,b,c)/(2\pi)\) has the \(\operatorname{Dirichlet}(1,1,1)\) law, whose density in \((a,b)\) on \(a>0,b>0,a+b<2\pi\) is \(1/(2\pi^2)\). Solving the moment equations gives the ordered weight triple
\[
(w_1,w_2,w_3)=\frac{(\sin b,\sin c,\sin a)}{\sin a+\sin b+\sin c},
\quad \sin a+\sin b+\sin c=4\sin\frac a2\sin\frac b2\sin\frac c2>0.
\]
Therefore \(W=\sqrt{\sin^2a+\sin^2b+\sin^2c}/(\sin a+\sin b+\sin c)\), a cyclically symmetric continuous function on the open simplex. Positivity requires all three gaps to be smaller than \(\pi\). The events that one gap exceeds \(\pi\) are disjoint and each has probability \(1/4\), establishing the stated positive-weight probability.

**2. Localization of the large-norm event.** Fix an angular cutoff \(0<\delta<\pi/4\). The closed interior where every gap is at least \(\delta\) has bounded \(W\). In each noncorner boundary strip, for example \(0<a<\delta\) and \(\delta\le b,c\), the sine formula gives \(W\le C_\delta/a\). Integrating this upper bound against the constant gap density shows that all these strips together contribute at most \(O_\delta(T^{-1})\) to \(\mathbb P(W>T)\). Thus only the three pairwise-small-gap corners can contribute to the coefficient of \((\log T)/T\).

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

**4. Moment and noise consequences.** The tail-integral identity \(\mathbb E W^p=p\int_0^\infty T^{p-1}\mathbb P(W>T)\,dT\) for \(p>0\) gives the sharp integrability threshold \(p<1\), since the tail is asymptotic to a positive constant times \((\log T)/T\). Conditional on the nodes, the sum of independent centered observation errors weighted by \(w_j\) has variance \(\sigma^2\sum_jw_j^2\); the unconditional variance is therefore infinite. This does not assert that a particular deterministic input function necessarily suffers a divergent quadrature error. \(\square\)

## Verification

The accompanying `verify.py` checks the exact trigonometric weight formula against independently solved moment equations, checks near-corner normalization for samples across multiple length scales, and evaluates the homogeneous-region integral numerically to test its predicted logarithmic coefficient. These are finite diagnostics; the infinite limit follows only from the area-decomposition argument above. Execute `python verify.py` using standard Python with NumPy and SciPy.

## Relationship to prior work

Bělík, Narayan and Turnage (2026) establish randomized least-squares concentration and stable quadrature construction under sufficient sampling assumptions. At exactly three independent circle nodes, no oversampling or positivity safeguard is imposed; the present question is the exact *rare-event* tail constant of the unique first-harmonic quadrature weights, not a large-sample success guarantee. The source's abstract, introduction and contribution summary were accessible, but full theorem-level comparison with its later sections was limited.

Xu and Shen (2026) study divergent expected spectral reconstruction risk for independently sampled trigonometric polynomial models; their accessible abstract does not identify the normalized *quadrature functional's* exact sharp tail coefficient. A separately inspected published result, *Critical inverse moments and logarithmic tails of random Fourier interpolation* (2026), proves upper and lower bounds of order \((\log T)/T\) for the complete inverse-Frobenius norm when three nodes are sampled, but explicitly **does not claim an exact leading constant** even for that different full-matrix norm. Here the row-functional reduction and exact constant are essential: full-inverse norm bounds alone do not determine it. Another inspected published result on three-node trigonometric quadrature treats *stratified bounded jitters* rather than independent full-circle nodes, and obtains a different moment threshold. These comparisons identify the distinct object and sharp coefficient; they cannot rule out all earlier unindexed equivalent formulas.

## Limitations

The exact coefficient is for one fixed sample count, independent uniform full-circle nodes, normalized circle integration, and the Euclidean norm of the **interpolatory** first-harmonic weights. It is not the inverse-Frobenius norm of the full Fourier sampling matrix, and does not cover overdetermined, separated, jittered or positivity-optimized quadrature. A full-text historical priority comparison with all possibly relevant sources has not been completed. Independent mathematical review has not been performed.

## References

1. F. Bělík, A. Narayan and J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506, first public 2026-09-08. https://arxiv.org/abs/2609.09506
2. H. Xu and Y. Shen, *Non-asymptotic Analysis of Expected Reconstruction Risk for Trigonometric Polynomial Models*, arXiv:2609.29286, first public 2026-09-24. https://arxiv.org/abs/2609.29286
3. *Critical inverse moments and logarithmic tails of random Fourier interpolation* (2026), publicly accessible result and proof. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-critical-inverse-moments-and-logarithmic-tails-of-random-fourier--323dcae74731
4. *Sharp positivity and logarithmic noise barrier in three-node perturbed trigonometric quadrature* (2026), publicly accessible result and proof. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-positivity-and-logarithmic-noise-barrier-in-three-node-per--fd84114e8959
