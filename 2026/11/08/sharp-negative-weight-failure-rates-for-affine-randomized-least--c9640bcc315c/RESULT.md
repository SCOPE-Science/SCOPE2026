# Sharp negative-weight failure rates for affine randomized least-squares quadrature

## Finding

Consider the unweighted randomized least-squares quadrature rule that integrates the two-dimensional space \(V=\operatorname{span}\{1,x\}\) exactly. Let \(X_1,\ldots,X_m\) be independent samples from a symmetric, atomless probability measure \(\nu\) supported on \([-R,R]\), where \(R>0\) is its essential upper endpoint, and suppose \(\nu((0,R))>0\). Let \(F_m\) be the event that at least one of the resulting \(m\) quadrature weights is negative. For every integer \(m\ge2\), the weights exist uniquely almost surely, and

\[
\lim_{m\to\infty}-\frac1m\log\Pr(F_m)
=I_\nu
:=-\log\min_{t\ge0}\mathbb E_\nu\!\left[e^{-t(X^2-RX)}\right]>0.
\]

The minimum is attained at a unique positive \(t\). The finite-sample bound \(\Pr(F_m)\le2e^{-mI_\nu}\) holds for every \(m\ge2\). For uniform sampling on \([-1,1]\), there is additionally an exact three-node law,

\[
\Pr(F_3)=\frac{2+\pi}{16},\qquad
\Pr(\text{all three weights positive})=\frac{14-\pi}{16}.
\]

For this uniform law, \(I_\nu=0.172761450635\ldots\) and the minimizing parameter is \(t_*=1.2631644033\ldots\). In particular, the failure probability is \(\exp[-I_\nu m+o(m)]\) on the logarithmic scale. The finite three-node identity and the general exponential-rate theorem are complementary descriptions of the same positivity event.

## Assumptions and scope

The integration functional is \(\mathcal L(f)=\int f(x)\,d\nu(x)\); the sampling and integration measures coincide. Each integrand is fitted on the sampled nodes by ordinary, unregularized least squares in \(V\), and the integral of that fitted affine function defines the quadrature rule. No positivity constraint, postprocessing, node pruning, induced sampling, or weight clipping is applied. The measure \(\nu\) is symmetric about zero, nonatomic, supported in \([-R,R]\) with essential upper endpoint \(R>0\), and has positive mass on the open interval \((0,R)\). The latter assumption guarantees a nondegenerate strictly negative region for \(X^2-RX\). All assertions concern exact real arithmetic and independently sampled nodes. The three-node constant and explicit error-function formula specialize to \(\nu=\operatorname{Uniform}[-1,1]\).

## Proof

**1. Exact weight and sign formula.** Write \(S=\sum_{j=1}^m X_j\) and \(Q=\sum_{j=1}^m X_j^2\). The ordinary least-squares design matrix has rows \((1,X_j)\). As \(\mathcal L(1)=1\) and \(\mathcal L(x)=0\), inversion of the \(2\times2\) normal matrix gives

\[
w_i=\frac{Q-SX_i}{mQ-S^2},\qquad i=1,\ldots,m.
\]

The denominator equals \(m\sum_j(X_j-S/m)^2\) and is positive almost surely because \(\nu\) is nonatomic and \(m\ge2\). Consequently, if \(S>0\), a negative weight occurs exactly when \(Q<S\max_iX_i\); if \(S<0\), exactly when \(Q<S\min_iX_i\). For \(S=0\), all weights are \(1/m\). These statements are exact finite-sample equivalences, not probability approximations.

**2. Exponential upper bound.** If \(S>0\), then \(\max_iX_i\le R\), so the failure event implies \(\sum_j(X_j^2-RX_j)<0\). If \(S<0\), it implies \(\sum_j(X_j^2+RX_j)<0\). Symmetry makes these two sums identically distributed. Therefore, for any \(t\ge0\), Markov's inequality gives

\[
\Pr(F_m)\le2\Pr\!\left(\sum_j(X_j^2-RX_j)<0\right)
\le2\left(\mathbb E e^{-t(X^2-RX)}\right)^m.
\]

Minimizing over \(t\ge0\) gives the asserted nonasymptotic bound. The bounded random variable \(Y=X^2-RX\) has \(\mathbb EY=\mathbb EX^2>0\) and takes strictly negative values on a set of positive probability in \((0,R)\). Thus \(\log\mathbb Ee^{-tY}\) has negative derivative at zero, strictly positive second derivative for every finite \(t\), and positive derivative at sufficiently large \(t\). It has precisely one minimizer \(t_*>0\), with a minimum strictly between zero and one; hence \(0<I_\nu<\infty\).

**3. Matching exponential lower bound.** Fix \(0<\delta<R\) small enough that \(\nu((0,R-\delta))>0\), and set \(Y_\delta=X^2-(R-\delta)X\). The designated-node event \(X_1\in[R-\delta,R]\) has probability \(c_\delta>0\), by the essential-endpoint assumption. For \(|X|\le R\), \(|Y_\delta|\le2R^2\). Hence, on the independent intersection

\[
X_1\in[R-\delta,R],\qquad
\sum_{j=2}^{m}Y_\delta(X_j)<-2R^2,
\]

we have \(Q<(R-\delta)S\), which forces \(S>0\); also \(\max_jX_j\ge R-\delta\). The exact sign formula then forces a negative weight. Thus

\[
\Pr(F_m)\ge c_\delta\Pr\!\left(\sum_{j=2}^{m}Y_\delta(X_j)<-2R^2\right).
\]

The ordinary Cramér large-deviation theorem for bounded independent variables, together with the open-set lower bound at a threshold approaching zero, gives

\[
\lim_{m\to\infty}-\frac1m\log\Pr\!\left(\sum_{j=2}^{m}Y_\delta(X_j)<-2R^2\right)
=I_\delta:=-\log\min_{t\ge0}\mathbb Ee^{-tY_\delta}.
\]

Indeed, \(\mathbb EY_\delta=\mathbb EX^2>0\) and \(\Pr(Y_\delta<0)>0\), so zero is an interior left-tail point. Boundedness makes the moment-generating functions continuous in \((t,\delta)\); their unique minimizers remain uniformly bounded for all sufficiently small \(\delta\), because a fixed interval inside \((0,R)\) has negative \(Y_\delta\). Thus \(I_\delta\to I_\nu\) as \(\delta\downarrow0\). Combining this lower estimate with Step 2 proves the exact logarithmic rate.

**4. The three-node uniform probability.** For three independent uniform nodes, all three signs agree with probability \(1/4\); in that event exactness for \(x\) forces a negative weight. Otherwise, by reflection symmetry, it suffices to consider one negative node \(-U\) and two positive nodes \(V<W\), where their three absolute values were independent \(\operatorname{Uniform}(0,1)\). From the weight formula, the weight associated with \(-U\) is positive, and the weight at \(W\) is negative precisely when

\[
U(U+W)<V(W-V).
\]

Writing \(v=V/W\), this is \(U<W h(v)\) with \(h(v)=(\sqrt{1+4v(1-v)}-1)/2\). The ordered positive pair has density \(2\) on \(0<V<W<1\). The conditional failure probability for this mixed-sign pattern therefore equals

\[
2\int_0^1\int_0^W W h(V/W)\,dV\,dW
=\frac23\int_0^1h(v)\,dv
=\frac23\left(\frac\pi8-\frac14\right)
=\frac\pi{12}-\frac16.
\]

The two mixed-sign categories have combined probability \(3/4\), giving

\[
\Pr(F_3)=\frac14+\frac34\left(\frac\pi{12}-\frac16\right)
=\frac{2+\pi}{16}.
\]

All boundary cases have probability zero because the law is continuous.

**5. Explicit uniform-law exponent.** Completing the square yields, for \(t>0\),

\[
M(t):=\mathbb E e^{-t(X^2-X)}
=\frac{\sqrt\pi\,e^{t/4}}{4\sqrt t}
\left[\operatorname{erf}\left(\frac{\sqrt t}{2}\right)
+\operatorname{erf}\left(\frac{3\sqrt t}{2}\right)\right].
\]

The unique solution of \(M'(t)=0\) determines \(I_\nu=-\log M(t_*)\), with numerical values reported above. This closed one-variable minimization is the exact rate; decimal values are illustrative rather than part of a numerical certificate.

## Verification

The accompanying `verify.py` is a standalone Python 3 standard-library checker. It verifies \(4,648\) nonsingular rational node configurations (including exact constant and first-moment reproduction and the sign-event equivalence), numerically evaluates the three-node integration identity, cross-checks the error-function moment generating function against direct quadrature, brackets the stationary point of its derivative, and performs a seeded simulation of the three-node event. Running `python3 verify.py` returns `VERIFY_OK`. Neither numerical integration nor simulation substitutes for Steps 1–5, which prove the exact identities and infinite-sample statement.

## Relationship to prior work

Bělík, Narayan and Turnage (2026, arXiv:2609.09506v1), Sections 2.2, 2.6, 3.3 and 4, introduce and analyze the weighted least-squares quadrature construction, prove finite-sample weight-concentration bounds and sufficient high-probability positivity, and discuss Carathéodory–Steinitz pruning. Their formula includes this unweighted symmetric sampling specialization; they do not give the exact three-draw probability or the sharp logarithmic failure exponent in the general symmetric affine class.

Migliorati and Nobile (arXiv:1812.07761, subsequently Journal of Approximation Theory 275, 105706) establish high-probability positivity under a sample-size bound for their induced-sampling cubature rule. This does not identify the exact negative-weight probability or its Cramér rate for the unweighted sampler considered here. The affine normal-equation identity and the classical Cramér theorem are standard ingredients; the new mathematical statement is their sharp combination for the sign of randomized least-squares quadrature weights, including the exact finite-size calibration.

## Limitations

The rate is logarithmic only: no multiplicative prefactor, finite-sample distribution for every \(m\), or universally monotone failure probability is asserted. The symmetric nonatomic bounded-support hypothesis is essential to the stated proof, and the three-node constant assumes uniform sampling. The result concerns the original unconstrained least-squares weights, not positive-weight pruning, an induced sampler, or arbitrary higher-degree trial spaces. Independent validation of the mathematical result has not been performed.

## References

1. F. Bělík, A. Narayan and J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506v1 (first public version 2026-09-08), https://arxiv.org/html/2609.09506v1 .
2. G. Migliorati and F. Nobile, *Stable high-order randomized cubature formulae in arbitrary dimension*, arXiv:1812.07761 (first public version 2018-12-19), https://arxiv.org/abs/1812.07761 ; Journal of Approximation Theory 275 (2022), 105706.
3. H. Cramér, classical large-deviation theorem for independent bounded random variables (standard theorem; an application to the displayed node-functional is proved above).
