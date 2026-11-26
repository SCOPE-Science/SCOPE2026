# Independent mathematical audit

## correctness

PASS

With M=n−1, the dimensionless generator is w^(-1) times the divergence of x(1−x)^M times the derivative, where w=(1−x)^(M−1). Bounded regularity at zero removes the integration constant (the other local branch is logarithmic). The forward-integral inverse K is positive and m(b)=(K1)(b) is the mean by stopping the bounded mean-passage solution. Tonelli gives the full weighted mean as (1/M) times the integral of W(u)/u, where W=[1−(1−u)^M]/M. The integral evaluates to H_M/M². Therefore (Km)'/m'=J/W rises strictly to alpha=H_M/M, and (Km)/m tends to alpha since m diverges. Positivity gives K^j1<=alpha^(j−1)m. For s=theta/m with s alpha<1 the uniformly convergent regular solution solves f=1+sKf and is bounded before passage; stopping gives the reciprocal transform. The Laplace difference is R/[(1+theta)(1+theta+R)], where R starts with s²Km and has a geometrically bounded tail. Moment differentiation gives the variance deficit 2Km/m²; strict positive variance also follows directly because (Km)'/m'<m(x) before b. The mean expression gives the different logarithmic and power-law infidelity scalings. The assertions are for each fixed n and for the stated time and boundary normalization.

## originality

FAIL

The signed estimate and harmonic corrections are not quoted verbatim in the inspected prior text, but are direct coefficient corollaries of the known regular hypergeometric solution for the same Brownian fidelity model, not just consequences of prior qualitative exponentiality. Tóth Appendix (A.6)–(A.8) gives the regular Gauss solution with c=1, a+b=M and ab=lambda/4. For the Laplace BVP put lambda=4s and divide the solution by its value at b; this yields exactly the reciprocal transform from zero. In its Gauss series the degree-j coefficient is s times a positive s-independent weight times the product over k=1..j−1 of [1+s/(k(k+M))]. The partial sum of the linear factors' coefficients increases to sum 1/[k(k+M)]=H_M/M by telescoping. The product is between 1 and exp(s alpha), hence at most 1/(1−s alpha) on the claimed range. Summing immediately gives the signed finite bound, including strictness from j>=2. The quadratic coefficient divided by the mean is a positive weighted average of those partial sums, with weights the coefficients of the mean series times b^j. Because the known mean diverges, the weight on each fixed finite set of j goes to zero, so the ratio tends to alpha. The same exponential majorant bounds all higher orders uniformly and gives the fixed-theta correction; the variance deficit is the second derivative of the reciprocal series. Thus all decisive quantitative parts are already mechanically extractable, even with a better finite envelope. No claim is made that the prior author explicitly printed them.

## value

PASS

As quantitative information, a mean-normalized signed Laplace estimate and an explicit leading error at high fidelity calibrate how good an exponential approximation is; a long-time tail at fixed threshold cannot do this. The harmonic factor distinguishes dimension and the ideal diffusion application is natural. This utility does not make the coefficient corollaries original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
