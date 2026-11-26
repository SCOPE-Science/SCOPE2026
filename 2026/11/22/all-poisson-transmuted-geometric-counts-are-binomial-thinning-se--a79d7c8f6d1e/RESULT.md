# Positive compound-Poisson innovations for transmuted-geometric thinning

## Finding

The fixed-marginal transmuted-geometric INAR construction of Ghodake et al. [1, §2] uses a rational expression for the thinning innovation. Its interpretation as a positive mixture of a point mass and three geometric laws is not in general valid, **even for positive transmutation**. Here is a positive compound-Poisson construction on the whole positive range, together with exact witnesses distinguishing the mixture error from failure of the underlying construction.

Let \(0<q<1\), \(0\le\alpha\le1\), \(\lambda\ge0\), and let \(Y=N+T\) with independent \(N\sim\mathrm{Poisson}(\lambda)\) and \(\Pr(T=k)=(1-\alpha)(1-q)q^k+\alpha(1-q^2)q^{2k}\) for \(k\ge0\). Write \(P\) for its PGF, put \(r=q(q+\alpha)/(1+\alpha q)\), and define \(x_c=cx/[1-(1-c)x]\) for \(0<c<1\) and \(0<x<1\). The PGF of the independent innovation for binomial thinning with retention \(c\) is \(P(z)/P(1-c+cz)\). It is compound Poisson with **strictly positive rates for every jump size** \(j\ge1\):

\[
\eta_j(c)=\lambda(1-c)\mathbf 1_{j=1}
+\frac{q^j-q_c^j+(q^2)^j-(q^2)_c^j-r^j+r_c^j}{j}.
\]

In particular the construction includes the transmuted-geometric marginal itself (\(\lambda=0\)). For \(q=\alpha=1/2\) and \(c=2/5\) that marginal innovation has a **negative** weight \(-3/10\) at the geometric survival ratio \(1/4\) in the three-pole decomposition used in [1, Eq. (8)]; nevertheless its PGF and each of its compound-Poisson rates are positive in the senses above. In contrast, the same fixed-marginal construction cannot work at every thinning coefficient for \(q=1/2,\alpha=-9/10\), which is inside the negative transmutation range considered in [1].

## Proof

For the specified nonnegative parameters, elementary factorization gives
\[
P(z)=e^{\lambda(z-1)}\frac{(1-q)(1+\alpha q)(1-rz)}{(1-qz)(1-q^2z)},\qquad q^2\le r\le q.
\]
Expanding the logarithm gives \(P(z)=\exp(\sum_{j\ge1}a_j(z^j-1)/j)\), where \(a_j=\lambda\mathbf 1_{j=1}+q^j+q^{2j}-r^j\). These terms are positive and tend to zero geometrically. Define \(w_j=a_j-a_{j+1}\). To prove strict positivity of \(w_j\), put \(f(x)=x^j(1-x)\), which has its unique maximum at \(p=j/(j+1)\). If \(p\notin[q^2,q]\), monotonicity bounds \(f(r)\) by the larger endpoint value, which is strictly smaller than the sum of the endpoint values. Otherwise \(p\le q\le\sqrt p\) and \(p^2\le q^2\le p\). Hence
\[
f(q)\ge f(\sqrt p)>f(p)/2,\qquad f(q^2)\ge f(p^2)>f(p)/2.
\]
Indeed the two lower-bound ratios to \(f(p)\) are \(p^{-j/2}/(1+\sqrt p)>1/2\) and \(p^j(1+p)>3/(2e)>1/2\). Thus \(w_j=\lambda\mathbf1_{j=1}+f(q)+f(q^2)-f(r)>0\) for every \(j\), also at \(\alpha=0,1\).

Let \(\phi_t(z)=1-e^{-t}+e^{-t}z\) and \(D=-\log c>0\). Differentiating \(\log P(\phi_t(z))\) and telescoping gives
\[
\log\frac{P(z)}{P(\phi_D(z))}
=\int_0^D\sum_{\ell\ge1}w_\ell(\phi_t(z)^\ell-1)\,dt.
\]
This yields the nonnegative representation
\[
\eta_j(c)=\int_0^D\sum_{\ell\ge j}w_\ell\binom{\ell}{j}e^{-tj}(1-e^{-t})^{\ell-j}\,dt.
\]
The terms sum to a finite value since their sum over \(j\ge1\) is bounded by \(D\sum_{\ell\ge1}w_\ell=D a_1\). The term \(\ell=j\) shows \(\eta_j(c)\ge w_j(1-c^j)/j>0\). Thus exponentiation gives an actual innovation law, which may be sampled independently of \(Y\) and its Bernoulli thinnings. On the other hand \(1-x\phi_D(z)=[1-(1-c)x](1-x_c z)\); coefficient extraction from the rational logarithm gives the displayed closed form for \(\eta_j(c)\).

For the positive-transmutation witness, write \(G_x(z)=(1-x)/(1-xz)\). At \(\lambda=0,q=\alpha=1/2,c=2/5\) one has \(r=2/5\), \(r_c=4/19\), and exact partial fractions give
\[
\frac{P(z)}{P(1-c+cz)}=\frac25+\frac35\left(\frac{13}{22}G_{1/2}(z)-\frac12G_{1/4}(z)+\frac{10}{11}G_{4/19}(z)\right).
\]
The three poles are distinct, so this is not a positive mixture at those rates. This sign agrees with the \(G_{q^2}\) term in [1, Eq. (8)]: its sign is the sign of \(((1-c)q-c)/((1-c)q-\alpha c)\) in this interior example. The rational identity is not itself the problem; its use as a positive mixture is. The integral representation above establishes existence without relying on those signed weights.

For the negative-transmutation witness, the transmuted-geometric law is still a probability law with exactly the same rational PGF, but \(r=-4/11\). Its log coefficients give \(a_3-a_2=719/85184>0\) (also with any independent Poisson summand). In the ratio \(P(z)/P(\phi_t(z))\), the coefficient of \(z^2\) is zero at \(t=0\) and has derivative \(a_2-a_3<0\) there, by the same differentiated PGF identity locally at zero. Hence that coefficient is negative for all sufficiently small positive \(t\); the ratio is not a PGF for all retention probabilities. This witness is not a classification of negative transmutation.

## Relationship to prior work and limits

Ghodake et al. [1, Definition 1 and Eqs. (6)–(10)] already give the fixed-marginal binomial-thinning formulation and rational innovation quotient for the geometric parent; a positive-domain self-decomposability assertion for the Poisson convolution is not separately claimed as new. Indeed a Poisson component adds an independent Poisson innovation of rate \(\lambda(1-c)\). Their Appendix A.1 starts from the recursion with innovations and addresses the stationary series; this does not address the nonnegative-coefficient issue in the preceding construction. The distinct contribution here is a rigorous positive-domain construction with all jump rates strictly positive and explicit, even when the proposed geometric weights have mixed signs. The standard decreasing-canonical-sequence characterization is prior [4]. The negative witness illustrates the need for a parameter distinction; a separate negative-range criterion is given in [5]. The underlying parent law and its ordinary infinite divisibility on the positive range, and the Poisson convolution itself, are prior [2,3]. We make no claim about continuous scaling or the whole negative-transmutation classification.

Run `python3 verify.py` for exact rational checks of the signed decomposition witness, the negative-range obstruction, and the innovation log coefficients at finite parameter samples. The all-parameter positivity and every jump size are established analytically, not by the samples.

## References

1. A. Ghodake, M. Awale, H. S. Bakouch, G. Alomair and A. F. Daghestani, “A Seasonal Transmuted Geometric INAR Process: Modeling and Applications in Count Time Series,” *Mathematics* 13 (2025), 2334, §2 and Appendix A.1, https://doi.org/10.3390/math13152334.
2. S. Chakraborty and D. Bhati, “Transmuted geometric distribution with applications in modeling and regression analysis of count data,” *SORT* 40 (2016), 153–176, §3.2, https://www.idescat.cat/sort/sort401/40.1.7.chakraborty-bhati.pdf.
3. A. Nandi, S. Chakraborty and S. Biswas, “A new count model based on Poisson-Transmuted Geometric convolution,” arXiv:2306.07219v1, https://arxiv.org/abs/2306.07219.
4. F. W. Steutel and K. van Harn, “Discrete analogues of self-decomposability and stability,” *Ann. Probab.* 7 (1979), 893–899, https://doi.org/10.1214/aop/1176994950.
5. “A two-index thinning self-decomposability criterion with reentrant negative-transmutation phases,” https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-two-index-thinning-self-decomposability-criterion-with-reentra--2fdc7de1a76a/RESULT.md.
