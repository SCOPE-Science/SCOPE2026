# An exact positivity-confidence law and heavy-tail bandwidth threshold for two-node Gaussian kernel quadrature

## Finding

For the unregularized two-node Gaussian-kernel Bayesian quadrature rule with two independent Gaussian integration nodes, there is an exact confidence formula for the event that **both optimized weights are positive** in every dimension. With \(a=1+2h\), the probability is
\[
P_{d,h}=I_{a^2/(1+a^2)}(1/2,d/2),
\]
where \(I_z(\alpha,\beta)=B(z;\alpha,\beta)/B(\alpha,\beta)\) is the regularized incomplete beta function. The law is invariant under affine transformations of the Gaussian measure when the kernel metric is whitened by its covariance. It increases strictly with positive shape \(h\) and integer dimension \(d\).

More strongly, almost every pair of nodes has a sharp threshold shape \(H\ge0\) at which its weight sign changes. The exact distribution is
\[
\Pr(H>t)=I_{1/(1+(1+2t)^2)}(d/2,1/2),\qquad t\ge0.
\]
Writing
\[
c_d=\frac{\Gamma((d+1)/2)}{2^d\sqrt\pi\,\Gamma(d/2+1)},
\]
one has \(\Pr(H>t)\sim c_d t^{-d}\), with the **sharp moment frontier** \(\mathbb E H^p<\infty\) if and only if \(0<p<d\). In particular the mean threshold is infinite in one dimension, but finite in every dimension at least two; its variance is finite precisely from dimension three onward.

The broad-bandwidth, nearly flat-kernel limit obeys
\[
\inf_{h>0}P_{d,h}=I_{1/2}(1/2,d/2).
\]
The smallest integer dimension in which this infimum is at least 95% is **six**, with \(I_{1/2}(1/2,3)=0.950174737219423\ldots\). The exact risk at fixed \(h\), as \(d\to\infty\), is
\[
1-P_{d,h}\sim\sqrt{\frac{2[1+(1+2h)^2]}{\pi d(1+2h)^2}}
[1+(1+2h)^2]^{-d/2}.
\]
These are probabilities of positive **unconstrained** Bayesian weights, not probabilities of existence of alternative, explicitly constrained positive quadrature weights.

## Assumptions and scope

Fix an integer \(d\ge1\), a mean \(\mu\in\mathbb R^d\), a symmetric positive-definite covariance \(\Sigma\) and a shape \(h>0\). The integration measure is \(\nu=N(\mu,\Sigma)\). Two locations \(X,Y\) are drawn independently from \(\nu\); thus \(X\ne Y\) almost surely. Use the covariance-whitened Gaussian kernel
\[
k_h(x,y)=\exp[-h(x-y)^T\Sigma^{-1}(x-y)].
\]
For \(x_1=X,x_2=Y\), define the Gram matrix \(K_{ij}=k_h(x_i,x_j)\), the vector of kernel means \(q_i=\int k_h(x_i,z)\nu(dz)\), and the exact interpolatory Bayesian quadrature weights \(w=K^{-1}q\). No point optimization, positivity projection, additional moment conditions, polynomial augmentation, diagonal nugget, or observation noise is imposed.

Let \(z_i=\Sigma^{-1/2}(x_i-\mu)\). The positive-definite Gram matrix has diagonals one and off-diagonal \(\kappa=\exp[-h\|z_1-z_2\|^2]\) in \((0,1)\). The Gaussian convolution formula gives
\[
q_i=(1+2h)^{-d/2}\exp\left[-\frac{h\|z_i\|^2}{1+2h}\right].
\]
We use the positive-part notation \(v_+=\max(v,0)\) and the regularized beta function \(I_z\) defined above. All parameter and node statements are exact-arithmetic assertions.

## Proof

**1. Two-by-two sign criterion.** Direct inversion gives
\[
w_1=\frac{q_1-\kappa q_2}{1-\kappa^2},\qquad
w_2=\frac{q_2-\kappa q_1}{1-\kappa^2}.
\]
Both numerators are strictly positive exactly when \(\kappa<\min(q_1/q_2,q_2/q_1)\). Substituting the positive Gaussian means and taking logarithms, with \(h>0\) fixed, makes this equivalent to
\[
\left|\|z_1\|^2-\|z_2\|^2\right|<(1+2h)\|z_1-z_2\|^2.
\]
For any distinct node pair define \(R_{x,y}=|\|z_1\|^2-\|z_2\|^2|/\|z_1-z_2\|^2\). As \(h\) increases, the inequality is strict exactly for \(h>(R_{x,y}-1)/2\); when \(R_{x,y}\le1\), every positive shape works. Thus the critical threshold is
\[
H=\tfrac12(R_{x,y}-1)_+.
\]
For \(H>0\), exactly one weight is negative for \(0<h<H\), exactly one is zero at \(h=H\), and both are positive for \(h>H\). When \(H=0\), both are positive for every \(h>0\). At \(h=0\) the Gram matrix is singular, so all limits are explicitly one-sided.

**2. Exact distribution of the threshold.** The standardized vectors \(z_1,z_2\) are independent \(N(0,I_d)\). Set \(U=(z_1+z_2)/\sqrt2\), \(V=(z_1-z_2)/\sqrt2\), so \(U,V\) are independent standard Gaussian vectors. Since
\[
\|z_1\|^2-\|z_2\|^2=2U^TV,\quad
\|z_1-z_2\|^2=2\|V\|^2,
\]
the ratio \(R_{x,y}\) equals \(|U^TV|/\|V\|^2\). Conditional on \(V\), the scalar \(Z=U^TV/\|V\|\) is exactly standard normal with a conditional law independent of \(V\). Therefore \(Z\) and \(R=\|V\|\) are independent, with \(R^2\sim\chi^2_d\), and
\[
R_{x,y}\stackrel{\rm law}=|Z|/R.
\]
The independent chi-square ratio \(Z^2/(Z^2+R^2)\) has the \(\mathrm{Beta}(1/2,d/2)\) law. For every \(a>0\),
\[
\Pr(|Z|/R<a)=I_{a^2/(1+a^2)}(1/2,d/2).
\]
The distribution is continuous for positive \(a\); substituting \(a=1+2h\) proves the exact weight-positivity law. Likewise, for \(t\ge0\), \(H>t\) if and only if \(|Z|/R>1+2t\), yielding the stated survival function. The threshold has a positive atom at zero, whose mass equals \(I_{1/2}(1/2,d/2)\), and is otherwise continuously distributed.

**3. Heavy tail, moments and dimension limit.** As \(z\downarrow0\),
\[
I_z(d/2,1/2)\sim \frac{z^{d/2}}{(d/2) B(d/2,1/2)}.
\]
With \(z=[1+(1+2t)^2]^{-1}\sim(4t^2)^{-1}\), the coefficient simplifies by the gamma identity to \(c_d\), proving \(\Pr(H>t)\sim c_d t^{-d}\). The layer-cake formula \(\mathbb EH^p=p\int_0^\infty t^{p-1}\Pr(H>t)\,dt\) then yields finite moments exactly below \(d\), including divergence at equality. At fixed \(a=1+2h\), let \(b=d/2\) and \(z=(1+a^2)^{-1}<1\). Endpoint integration of the incomplete beta and the gamma-ratio asymptotic imply
\[
I_z(b,1/2)\sim\frac{z^b(1-z)^{-1/2}}{\sqrt{\pi b}}
=\sqrt{\frac{2(1+a^2)}{\pi d a^2}}(1+a^2)^{-d/2},
\]
which is the asserted growing-dimension failure probability.

**4. Sharp dimension-six reliability boundary.** Coupling \(R_d^2\sim\chi_d^2\) and \(R_{d+1}^2=R_d^2+G^2\) with an independent standard normal \(G\) shows that \(\Pr(|Z|/R_d<a)\) is strictly increasing in integer \(d\) for all finite positive \(a\). It is also strictly increasing in \(a\), since the positive ratio \(|Z|/R_d\) has a positive density. Hence \(\inf_{h>0}P_{d,h}=\lim_{h\downarrow0}P_{d,h}=I_{1/2}(1/2,d/2)\). The exact beta values satisfy
\[
I_{1/2}(1/2,5/2)=0.924413181578\ldots<0.95,
\quad I_{1/2}(1/2,3)=0.950174737219\ldots>0.95.
\]
Strict monotonicity makes six the first dimension with uniformly at least 95% probability of both weights being positive over every \(h>0\). In dimension one, \(P_{1,h}=(2/\pi)\arctan(1+2h)\); in dimension two, \(P_{2,h}=(1+2h)/\sqrt{1+(1+2h)^2}\), independently checking the normalization.

## Verification

Run \(\texttt{python verify.py}\) with Python 3, NumPy and SciPy (version requirements in \(\texttt{requirements.txt}\)). The independent checker numerically integrates the Gaussian kernel mean, directly solves 6,000 two-node kernel systems and tests their signs, compares Monte Carlo positivity frequencies against the exact beta probabilities, checks closed low-dimensional formulas, monotonicity, tail coefficients, the dimension-six threshold, and the large-dimension approximation. In the documented replay it passed **6,163 finite tests**. Deterministic algebraic identities and distributional arguments above, rather than the finite tests, establish the result for all dimensions, nodes, shapes and positive moments.

## Relationship to prior work

Huszár and Duvenaud [1, §3.1.1] give the general Bayesian quadrature weight formula and explicitly note negative weights, but do not supply the exact two-node Gaussian random-design sign probability or its dimensional threshold law. Särkkä et al. [2, §§III–IV] develop Gaussian-process sigma-point quadrature and Gaussian-kernel integration under Gaussian measures, but do not give this stochastic positive-weight classification. Karvonen, Kanagawa and Särkkä [3, §3.9] study the same general problem of positivity; their multivariate Gaussian random-node case is a numerical experiment in four dimensions, without the present exact two-node confidence and tail distribution. Their positive-weight results for locally optimizing nodes do not imply positivity probabilities for independent Gaussian nodes.

A published three-node symmetric Gaussian-kernel positivity theorem [4] treats a fixed symmetric point set against a *uniform bounded-interval* measure, with a different one-crossing shape criterion. A separate two-node power-exponential study [5] treats uniform nodes on an interval and the weight-amplified tails of noisy quadrature, not the distribution of the Gaussian kernel's critical positive-weight shape under multivariate Gaussian sampling. A separate affine-exact random-node result [6] optimizes polynomial moment weights, not the inverse Gaussian-kernel interpolation matrix. The exact result here is not claimed as a consequence of their titles or parameter matches; their differing objects and claims have been compared at the level of their formulas and hypotheses.

## Limitations

This theorem covers **exactly two independently Gaussian-distributed nodes** and a Gaussian kernel whose metric is matched to the integration covariance, with no regularization or positivity constraints. The 95% threshold is for probability that the *unconstrained coefficients* are strictly positive, not accuracy, consistency, optimal shape selection, or numerical stability in near-singular flat limits. Increasing \(h\) narrows the kernel; the resulting positivity gain need not imply reduced integration error. The heavy-tailed variable \(H\) is the random critical shape, not a claim that the actual quadrature weights have the same tails. The minimum dimension statement is within this Gaussian family and does not assert anything for arbitrary non-Gaussian integration measures or more than two nodes. Specialized unindexed equivalent results may exist; no independent external mathematical audit has been performed.

## References

[1] F. Huszár and D. Duvenaud, *Optimally-Weighted Herding is Bayesian Quadrature*, arXiv:1204.1664, first public 2012-04-07. https://arxiv.org/abs/1204.1664

[2] S. Särkkä, J. Hartikainen, L. Svensson, F. Sandblom, *On the relation between Gaussian process quadratures and sigma-point methods*, arXiv:1504.05994, first public 2015-04-22. https://arxiv.org/abs/1504.05994

[3] T. Karvonen, M. Kanagawa, S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509, first public 2018-12-20. https://arxiv.org/abs/1812.08509

[4] *A one-crossing positivity diagram for symmetric three-node Gaussian kernel quadrature*, published 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-one-crossing-positivity-diagram-for-symmetric-three-node-gauss--bf59562e8e52

[5] *A roughness threshold and exact noise tails for colliding-node kernel quadrature*, published 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-roughness-threshold-and-exact-noise-tails-for-colliding-node-k--841cfe0433d1

[6] *A density-universal collision law and exact Gaussian positivity benchmark for affine least-squares quadrature*, published 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-density-universal-collision-law-and-exact-gaussian-positivity--c97a80bc1618
