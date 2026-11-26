# Sharp negative-weight failure rate for affine randomized least-squares quadrature

## Finding

Let \(X_1,\ldots,X_m\) be independent samples from a symmetric atomless probability measure \(\nu\) on \([-R,R]\), where \(R>0\) is the essential upper endpoint and \(\nu((0,R))>0\). In the ordinary unweighted least-squares quadrature rule on \(\operatorname{span}\{1,x\}\), fit an affine function by least squares on the sampled nodes, then integrate the fit against \(\nu\). The rule's weight vector exists uniquely almost surely for \(m\ge2\). If \(F_m\) denotes the event that some weight is strictly negative, then
\[
\Pr(F_m)\le 2e^{-m I_\nu}\quad(m\ge2),\qquad
\lim_{m\to\infty}-\frac1m\log\Pr(F_m)=I_\nu,
\qquad I_\nu=-\log\min_{t\ge0}\mathbb E_\nu e^{-t(X^2-RX)}\in(0,\infty).
\]
The minimizer is unique and strictly positive. For uniform sampling on \([-1,1]\), the exponent is approximately \(0.172761450635\), attained at \(t_*\approx1.2631644033\).

## Assumptions and scope

The sampling and integration measures are identical. The least-squares fit is unregularized and unconstrained, with no pruning, clipping, or other weight postprocessing. The assertion concerns the weights of this particular rule, not uniqueness among all vectors exact on affine functions. The endpoint \(R\) being essential means \(\nu([R-\delta,R])>0\) for every \(\delta>0\). The result is a logarithmic rate: it gives no asymptotic prefactor or exact finite-sample distribution.

## Proof

**Weights and sign test.** Write \(S=\sum_i X_i\) and \(Q=\sum_i X_i^2\). Since the integral of a fitted affine function is its intercept, the two normal equations give
\[
w_i=\frac{Q-SX_i}{mQ-S^2}.
\]
The denominator is \(m\sum_i(X_i-S/m)^2>0\) almost surely, by atomlessness and independence. For \(S>0\), a negative weight occurs exactly when \(Q<S\max_i X_i\); for \(S<0\), it occurs exactly when \(Q<S\min_i X_i\). For \(S=0\) every weight is \(1/m\).

**Upper bound and optimization.** Since \(|X_i|\le R\), in the two sign cases failure implies a negative sum of \(X_i^2-RX_i\) or \(X_i^2+RX_i\), respectively. These sums have the same distribution by symmetry. Put \(Y=X^2-RX\). The exponential Markov bound therefore gives, for every \(t\ge0\),
\[
\Pr(F_m)\le2\Pr\!\left(\sum_{i=1}^m Y(X_i)<0\right)\le 2(\mathbb E e^{-tY})^m.
\]
The mean \(\mathbb EY=\mathbb EX^2\) is positive, and \(Y\) is strictly negative with positive probability. Thus the derivative of \(\log\mathbb E e^{-tY}\) at zero is negative; its second derivative is the strictly positive variance under the exponential tilt. This convex function tends to \(+\infty\) as \(t\to\infty\), since \(Y\) is bounded above by a negative constant on a set of positive probability. It follows that its unique minimizer is strictly positive and the minimum of \(\mathbb Ee^{-tY}\) is strictly between 0 and 1. This proves the bound with \(I_\nu\) and gives the lower bound on the logarithmic exponent.

**Matching logarithmic bound.** Put \(Y_\delta=X^2-(R-\delta)X\). Fix \(\delta>0\) sufficiently small that \(R-\delta>0\) and \(\Pr(Y_\delta<0)>0\). On the event that \(X_1\in[R-\delta,R]\) and \(\sum_{i=2}^m Y_\delta(X_i)<-2R^2\), we have \(Q<(R-\delta)S\) because \(|Y_\delta|\le2R^2\). Hence \(S>0\), and the designated node ensures \(\max_i X_i\ge R-\delta\), so the sign test forces failure. Independence of the designated node and the other nodes gives
\[
\Pr(F_m)\ge \nu([R-\delta,R])\Pr\!\left(\sum_{i=2}^m Y_\delta(X_i)<-2R^2\right).
\]
Zero lies in the interior of the convex hull of the law of \(Y_\delta\), with \(\mathbb E Y_\delta=\mathbb EX^2>0\). Its Cramér rate function \(J_\delta\) is finite and continuous there, and \(J_\delta(0)=-\log\min_{t\ge0}\mathbb E e^{-tY_\delta}\), since the maximizing tilt at zero is negative. For each fixed small \(\eta>0\), an open interval around \(-\eta\) lying below \(-\eta/2\) is included in the designated sum event for the mean of the last \(m-1\) nodes once \(m\) is large. The Cramér lower bound gives a limit superior of the negative logarithm divided by \(m\) at most \(J_\delta(-\eta)\). The constant node probability has zero logarithmic cost per sample. Sending \(\eta\downarrow0\) bounds the limit superior by \(J_\delta(0)\).

To take \(\delta\downarrow0\), choose \(0<a<b<R\) with \(\nu([a,b])>0\), which exists by exhaustion of \((0,R)\) by compact subintervals. For \(0\le\delta\le (R-b)/2\) and \(X\in[a,b]\), \(Y_\delta\le-a(R-b)/2<0\). Consequently \(\mathbb Ee^{-tY_\delta}\) exceeds 1 for all sufficiently large \(t\), uniformly in these \(\delta\). The minimizations can all be taken over one compact \(t\)-interval, where the expectations converge uniformly as \(\delta\downarrow0\) by boundedness. Thus \(J_\delta(0)\to I_\nu\). Together with the exponential upper bound on failure this gives the claimed limit.

**Uniform example.** For \(t>0\), completing the square gives
\[
\frac12\int_{-1}^1 e^{-t(x^2-x)}\,dx
=\frac{\sqrt\pi\,e^{t/4}}{4\sqrt t}
\left[\operatorname{erf}(\sqrt t/2)+\operatorname{erf}(3\sqrt t/2)\right].
\]
The derivative vanishes at the unique minimizer; the reported decimals are numerical illustrations, not certified intervals.

## Verification

The proof gives the rate for all laws in scope. Finite exact-rational checks of the weights and sign test, and numerical evaluations for the uniform law, are described in `VERIFICATION.md`.

## Relationship to prior work

- F. Bělík, A. Narayan and J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, [arXiv:2609.09506v1](https://arxiv.org/html/2609.09506v1), §§2.2, 2.5–2.6 and 3.3. Their weighted construction includes this rule. Their sufficient high-probability positivity conditions do not supply a matching logarithmic failure rate in the affine setup.
- G. Migliorati and F. Nobile, *Stable high-order randomized cubature formulae in arbitrary dimension*, [arXiv:1812.07761](https://arxiv.org/abs/1812.07761), Theorem 6 and Corollary 4. Theorem 6 concerns induced sampling; Corollary 4 gives sufficient positivity bounds for standard least squares with Jacobi sampling, including the uniform law, but not a sharp failure exponent.
- *Heavy-tail and positivity laws for random affine least-squares quadrature*, [Resultary, 26 October 2026](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-heavy-tail-and-positivity-laws-for-random-affine-least-squares-q--6eba4b8f5a9c), gives the exact three-node positivity probability for the uniform law. That finite-sample identity is prior work and is not part of the finding here.

The affine weight formula and Cramér's theorem are standard. The rate requires a matching lower bound for failure involving the observed extremes, not just an exponential estimate after substituting the support endpoint. No claim of exhaustive historical priority is made.
