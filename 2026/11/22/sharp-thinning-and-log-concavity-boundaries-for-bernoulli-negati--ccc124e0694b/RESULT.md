# Sharp Bernoulli-thinning boundary for Bernoulli–negative-binomial counts

## Finding

Let \(X=B+N\) with independent \(B\sim\operatorname{Bernoulli}(p)\) and \(N\) having masses \(\Pr(N=k)=(1-\theta)^\nu(\nu)_k\theta^k/k!\), where \(0<p,\theta<1\), \(\nu>0\), and \(k\ge0\). Write \(r=p/(1-p)\). Then \(X\) is self-decomposable under independent Bernoulli thinning at every retention probability if and only if
\[
\boxed{r\le\theta\quad\text{and}\quad \nu(1-\theta)\theta^2\ge(1+r)r^2.}
\]
Both inequalities are inclusive. The class is strictly smaller than the ordinary additive infinitely divisible class, even among overdispersed laws of this family.

## Assumptions and scope

The normalized probability generating function is \(G(z)=(1-p+pz)((1-\theta)/(1-\theta z))^\nu\). At retention \(a\in(0,1)\), the thinned copy of \(X\) retains each counted item independently with probability \(a\). Self-decomposability means that \(H_a(z)=G(z)/G(1-a+az)\) is a probability generating function for every \(a\in(0,1)\), i.e. there is an independent count-valued remainder for each \(a\). The remainder need not belong to the original parametric family. This is not ordinary real-line self-decomposability.

## Proof

Let \(L=\log G\) denote the branch real near zero. In a neighborhood of zero
\[
L'(z)=\sum_{k\ge1} b_k z^{k-1},\qquad b_k=\nu\theta^k+(-1)^{k-1}r^k.
\]
Put \(d_k=b_k-b_{k+1}\). For each \(k\ge1\), differentiating the coefficient of \(z^k\) in the quotient at \(a=1\) gives
\[
[z^k]H_a(z)=(1-a)d_k+O((1-a)^2).
\]
Indeed, on a sufficiently small closed disk about zero, both denominators in the quotient construction remain nonzero for real \(a\) close to one, and \(H_a(z)=1+(1-a)(z-1)L'(z)+O((1-a)^2)\) uniformly there. Nonnegativity for all \(a<1\) forces \(d_k\ge0\). This is the necessity direction of the classical canonical-sequence criterion (Steutel and van Harn, 1979).

For odd \(k\), \(d_k=\nu(1-\theta)\theta^k+(1+r)r^k>0\); for even \(k\), \(d_k=\nu(1-\theta)\theta^k-(1+r)r^k\). If \(r>\theta\), sufficiently large even indices have \(d_k<0\). If \(r\le\theta\), then \((r/\theta)^k\) on even indices is largest at \(k=2\); hence \(d_2\ge0\) implies all the even-index inequalities, including when \(r=\theta\).

For sufficiency, under the two displayed conditions \(b_k\to0\) geometrically and \(d_k\ge0\). Thus \(\sum_{k\ge1}d_k=b_1\) and \((u-1)L'(u)=\sum_{k\ge1}d_k(u^k-1)\) on \(|u|\le1\). With \(u_s=1-s+sz\), the log pgf quotient is
\[
\log H_a(z)=\int_a^1\sum_{k\ge1}d_k(u_s^k-1)\,\frac{ds}{s}.
\]
Each \(u_s^k\) is a binomial probability generating function. The positive-degree coefficients in the integral are nonnegative and sum to at most \(b_1\log(1/a)\); evaluating at one supplies the normalizing constant. Exponentiating therefore gives a compound-Poisson pgf. This argument proves both directions at all indices and rates.

## Comparison with ordinary infinite divisibility

The ordinary additive criterion for this family (Letac, Malouche and Maurer, 2002) is \(r\le\theta\) and \(r^2\le\nu\theta^2\). It also follows from the signs of the logarithmic coefficients \(b_k/k\): odd terms are positive, and if \(r\le\theta\), the first even term is decisive; otherwise some even term is negative. These coefficients are summable in the nonnegative case. The thinning inequality is stronger by its factor \((1+r)/(1-\theta)>1\). For example with \(\theta=1/2\), \(p=1/4\), \(\nu=1\), the ordinary condition holds but \(\nu(1-\theta)\theta^2=1/8<4/27=(1+r)r^2\). Here \(\operatorname{Var}(X)-\mathbb EX=\nu\theta^2/(1-\theta)^2-p^2=15/16>0\). With the same \(\theta,p\) and \(\nu=2\), both criteria hold.

## Verification and limits

The accompanying `verify.py` supplies exact-rational illustrations of boundary equality, strict inclusion and obstructions at low and high indices. It does not prove statements about every index or thinning rate. The proof above covers those quantifiers. Only the explicit thinning criterion is contributed here; the ordinary additive boundary is established literature, and mass-curvature and hazard classifications are outside the claim. No conclusion is asserted for other finite mixtures, multivariate laws, or estimation performance.

## References

- F. W. Steutel and K. van Harn, “Discrete Analogues of Self-Decomposability and Stability,” *Annals of Probability* **7** (1979), 893–899, Theorem 2.2. https://doi.org/10.1214/aop/1176994950
- G. Letac, D. Malouche and S. Maurer, “The Real Powers of the Convolution of a Negative Binomial Distribution and a Bernoulli Distribution,” *Proc. Amer. Math. Soc.* **130** (2002), 2107–2114. https://doi.org/10.1090/S0002-9939-02-05352-2
- S. H. Ong, S. Z. Sim, S. Liu and H. M. Srivastava, “A Family of Finite Mixture Distributions for Modelling Dispersion in Count Data,” *Stats* **6** (2023), 942–955. https://doi.org/10.3390/stats6030059
- N. Ben Salah, “Generalized Convolution Product of an Infinitely Divisible Distribution and a Bernoulli Distribution,” *Communications in Statistics – Theory and Methods* **51** (2022), 7297–7304. https://doi.org/10.1080/03610926.2021.1879863
- “Sharp mass-curvature and hazard transitions for Bernoulli–negative-binomial counts,” Resultary. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-mass-curvature-and-hazard-transitions-for-bernoulli-negati--eb5c7d74b649
