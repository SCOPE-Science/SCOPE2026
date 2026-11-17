# Sharp asymmetric large-deviation spectrum of the three-dimensional twisted baker map

## Finding

For the three-dimensional twisted baker map specified below and normalized Lebesgue initial data, the logarithmic largest and smallest finite-time singular values obey an **explicit, asymmetric** large-deviation law. Define, for \(y>0\),
\[
u(y)=\frac{y^2(1+y)}{1+y^2},\qquad
x(y)=\frac{y(1+y^2)}{y^3+3y+2},\qquad
I(x(y))=x(y)\log u(y)-\log\frac{1+y}{2}.
\]
The function \(x:(0,\infty)\to(0,1)\) is a strictly increasing bijection, so this defines a unique continuous rate \(I:[0,1]\to[0,\infty)\) by extending to the endpoints. In particular,
\[
I(0)=I(1)=\log2,\qquad I(1/3)=0.
\]
For every \(t\in(1/3,1)\),
\[
\lim_{n\to\infty}-\frac1n\log m\!\left\{z:\frac1n\log_2\|DF^n(z)\|_2\ge t\right\}=I(t).
\]
For every \(t\in(0,1/3)\),
\[
\lim_{n\to\infty}-\frac1n\log m\!\left\{z:\frac1n\log_2\sigma_{\min}(DF^n(z))\le t\right\}=I(t).
\]
Here \(m\) is normalized Lebesgue probability and the derivative is defined off the zero-measure exceptional branch set. The same rate applies to any fixed coordinate's logarithmic stretch. At both endpoints the rate is \(\log2\).

Although the centered stretch vector has exactly the same asymptotic Gaussian covariance as independent uniform allocation into three boxes, its **rare-event tails differ exponentially and with opposite signs**. Write the independent-box marginal rate
\[
I_{\mathrm{iid}}(x)=x\log(3x)+(1-x)\log\frac{3(1-x)}2,
\]
with the convention \(0\log0=0\). Then
\[
\boxed{\ I(x)>I_{\mathrm{iid}}(x)\text{ for }0\le x<1/3,\qquad
I(x)<I_{\mathrm{iid}}(x)\text{ for }1/3<x\le1.\ }
\]
Thus extreme expansion is exponentially *more common*, but extreme underexpansion is exponentially *less common*, than in the tempting independent-box approximation. For example, \(x(2)=5/8\), and \(I(5/8)\approx0.14170285\) whereas \(I_{\mathrm{iid}}(5/8)\approx0.17711886\).

## Assumptions and scope

Let \(X=[-1,1]\times[0,1]^2\) and define \(F:X\to X\) by
\[
F(x_1,x_2,x_3)=\begin{cases}
(1+2x_1,x_2,x_3),&x_1<0,\\
(1-2x_3,x_1,x_2),&x_1\ge0.
\end{cases}
\]
The probability \(m\) is normalized three-dimensional Lebesgue measure on \(X\). For every integer \(n\ge1\), compute \(DF^n\) away from branch boundaries and their preimages. These exceptional points have \(m\)-measure zero. Singular values use the Euclidean metric and \(\|\cdot\|_2\) denotes the Euclidean operator norm. All limits hold for this fixed dimension, with \(n\to\infty\); probabilities are over initial conditions, not over uniformly selected periodic orbits. All logarithms without the subscript \(2\) are natural.

## Proof

**1. Exact derivative and occupation reduction (previously established machinery).** Put \(D=\operatorname{diag}(2,1,1)\), and let \(Qe_1=e_2\), \(Qe_2=e_3\), \(Qe_3=-e_1\). The branch Jacobians are \(D\) and \(DQ\). Each prescribed binary itinerary of length \(n\) has normalized Lebesgue probability \(2^{-n}\), a basic-rectangle fact of Saiki–Takahasi–Yorke. Since the Jacobians are signed monomial matrices, reordering the cyclic permutation factors shows the logarithms base two of the three singular values equal, up to permutation, the occupation counts \((C_0(n),C_1(n),C_2(n))\) of the lazy directed three-state walk
\[
W_0=0,\qquad W_{k+1}=W_k+\xi_k\pmod3,\qquad
\Pr(\xi_k=0)=\Pr(\xi_k=1)=\frac12,
\]
where \(C_j(n)=\sum_{k=0}^{n-1}\mathbf 1_{\{W_k=j\}}\) and \(\sum_jC_j(n)=n\). The equality here is in distribution for the occupation counts, and an exact multiset identity holds for each itinerary using suffix residues. This reduction and the Gaussian occupation limit are already available in the cited earlier work; neither is claimed as new.

**2. A three-state characteristic equation.** Fix coordinate \(j=0\) and \(u=e^\theta>0\). Define \(P=(I+S)/2\), with \(S\) the clockwise three-cycle permutation, and \(D_u=\operatorname{diag}(u,1,1)\). Then the exact finite-horizon moment-generating function is
\[
\mathbb E[e^{\theta C_0(n)}]=e_0^{\mathsf T}(D_uP)^n\mathbf1.
\]
The nonnegative matrix \(D_uP\) is primitive for every \(u>0\), and its Perron eigenvalue \(\lambda(u)\) is simple and strictly positive. Direct determinant expansion yields
\[
\boxed{(2\lambda-u)(2\lambda-1)^2=u.}
\]
By Perron–Frobenius, the scaled cumulant-generating function for \(C_0(n)\) is
\[
\Lambda(\theta):=\lim_{n\to\infty}\frac1n\log\mathbb E[e^{\theta C_0(n)}]=\log\lambda(e^\theta),
\]
independently of the fixed initial state. The same function governs the other coordinates by cyclic conjugacy.

**3. Explicit parametric Legendre transform.** Put \(y=2\lambda-1\). Since \(\lambda>1/2\), \(y>0\). The characteristic equation becomes \(y^2(1+y-u)=u\), so
\[
u=\frac{y^2(1+y)}{1+y^2},\qquad \lambda=\frac{1+y}{2}.
\]
Differentiating the two logarithms gives
\[
\Lambda'(\theta)=\frac{d\log\lambda/dy}{d\log u/dy}
=\frac{y(1+y^2)}{y^3+3y+2}=x(y),
\]
and
\[
\frac{dx}{dy}=\frac{2(2y^3+3y^2+1)}{(y^3+3y+2)^2}>0.
\]
Moreover \(u(y)\) increases strictly from zero to infinity, \(x(y)\) increases from zero to one, and \(u(1)=1\), \(x(1)=1/3\). Therefore \(\Lambda\) is differentiable and strictly convex on the real line; the Fenchel–Legendre rate is uniquely
\[
I(x(y))=x(y)\log u(y)-\log((1+y)/2).
\]
The limits \(y\downarrow0\) and \(y\to\infty\) yield \(I(0)=I(1)=\log2\). The mean and second cumulant are \(\Lambda'(0)=1/3\), \(\Lambda''(0)=2/9\), matching the independent \(\operatorname{Bernoulli}(1/3)\) benchmark at the Gaussian scale.

**4. Large deviations for singular-value extremes.** The differentiable scaled log moment-generating function and compact support permit the standard finite-state Markov additive large-deviation theorem (or the Gärtner–Ellis theorem, with endpoint bounds obtained by approximation from the interior). It gives a speed-\(n\) large-deviation principle for each \(C_j(n)/n\) with the good rate \(I\) just calculated. Strict convexity and unique minimizer \(1/3\) imply
\[
\lim_{n\to\infty}\frac1n\log\Pr(C_j(n)/n\ge t)=-I(t)\quad(t>1/3)
\]
and the analogous lower-tail formula for \(t<1/3\). Because all three coordinate rates coincide, each event for the maximum is the union of three coordinate-tail events; it is bounded below by one such event and above by their sum. The same argument for the minimum proves both singular-value formulas. For the endpoints, \(I\) is continuous; upper estimates follow by Chernoff optimization, while trajectories having asymptotically total occupation in one state, or asymptotically none, furnish matching limiting lower bounds. This proves the announced \(\log2\) endpoint rates without assuming that a finite path can have exactly zero visits to its initial state.

**5. Strict asymmetric departure from independent sampling.** An independent uniform-box count has marginal cumulant-generating function \(\Lambda_{\mathrm{iid}}(\theta)=\log[(e^\theta+2)/3]\). To compare Perron eigenvalues write \(z=(u+2)/3\) and \(f_u(\lambda)=(2\lambda-u)(2\lambda-1)^2-u\). Exact algebra gives
\[
f_u(z)=-\frac{4(u-1)^3}{27}.
\]
For \(0<u<1\), both \(z\) and \(\lambda(u)\) lie above \(1/2\), where \(f_u\) is strictly increasing, hence \(\lambda(u)<z\). For \(1<u<4\) both lie above \(u/2\), again in the strictly increasing region, hence \(\lambda(u)>z\); for \(u\ge4\), one has \(z\le u/2<\lambda(u)\) directly. Thus
\[
\Lambda(\theta)<\Lambda_{\mathrm{iid}}(\theta)\quad(\theta<0),\qquad
\Lambda(\theta)>\Lambda_{\mathrm{iid}}(\theta)\quad(\theta>0),
\]
with equality only at zero. For \(x<1/3\), insert the negative independent-model optimizing tilt into \(I(x)=\sup_\theta\{x\theta-\Lambda(\theta)\}\), obtaining strict \(I(x)>I_{\mathrm{iid}}(x)\). For \(x>1/3\), insert the positive true-model optimizing tilt into the same variational formulas to get strict \(I(x)<I_{\mathrm{iid}}(x)\). The same strict inequalities hold at both endpoints by taking limits: \(I(0)=I(1)=\log2\), whereas \(I_{\mathrm{iid}}(0)=\log(3/2)\) and \(I_{\mathrm{iid}}(1)=\log3\). This completes the proof.

## Verification

Run `python3 checker.py` from the folder containing this document. The standard-library checker multiplies signed integer Jacobians for every one of the \(1022\) binary words of lengths one through nine, verifies the singular exponent/occupation correspondence, compares exact rational moment-generating functions against independent word enumeration at \(30\) cases, and checks seven rational points on the Perron characteristic curve. It evaluates the strict rate comparison at six rationally parametrized values. The executed summary is:

`TWISTED_BAKER_THREE_STATE_LDP_CHECK_OK words=1022 exact_mgfs=30 cubic_parameters=7 strict_iid_comparisons=6`

The independent symbolic calculation factors the benchmark characteristic polynomial as \(-4(u-1)^3/27\) and differentiates the parametric rate map. Finite checks corroborate rather than establish the infinite-time large-deviation theorem; that assertion is proved above from the Perron eigenvalue and finite-state Markov large deviations.

## Relationship to prior work

Saiki, Takahasi and Yorke introduced this map, established its binary basic-rectangle coding and equidistribution of its real- and complex-spectrum periodic points, and studied nonuniform periodic-orbit expansion. Published follow-up results derive the exact cyclic-walk representation of finite-time singular values and their all-dimensional Gaussian limit. These are acknowledged prerequisites. The present contribution is the *three-dimensional explicit non-Gaussian rate for extreme stretching and underexpansion and the strict, direction-dependent comparison with independent-box tails*. Neither the originating paper's periodic-orbit results nor the inspected Gaussian statements imply this exponential comparison. Classical finite-state Markov large-deviation principles provide the general proof method; they are not new. A general formula in other work may imply the calculation even without matching terminology, so publication priority is not claimed as independently certified.

## Limitations

The result concerns the fixed three-dimensional full-height map, normalized Lebesgue initial data, and finite-time singular values. It does not classify multiplier eigenvalues of periodic orbits, non-Lebesgue initial distributions, sharp polynomial prefactors, perturbations, or a dimension-uniform rate. The asymptotic rates do not imply finite-horizon inequalities between the two models. The finite checker is corroborative, not an infinite certificate, and literature coverage cannot exclude unindexed equivalents. No independent mathematical audit has been performed.

## References

1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, publicly submitted 9 February 2022, https://arxiv.org/abs/2202.04304; §§1–3 and the basic rectangles.
2. *Multinomial Gaussian singular-spectrum law for the twisted baker map*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-multinomial-gaussian-singular-spectrum-law-for-the-twisted-baker--589db8b1cf2b .
3. *Isotropic Gaussian splitting of finite-time singular values in the twisted baker map*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-isotropic-gaussian-splitting-of-finite-time-singular-values-in-t--11d620ed5ef6 .
4. A. Dembo and O. Zeitouni, *Large Deviations Techniques and Applications*, second edition, Springer, 1998, standard finite-state exponential tilting and large-deviation principles.
