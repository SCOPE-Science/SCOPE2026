# A quantitative log-curvature gap separates biphasic DNA loss from relaxing removal

## Finding

Let \(C_j=C(t_0+jh)>0\) for \(j=0,\ldots,4\), \(t_0\ge0\) and \(h>0\), and set \(K_j=\log(C_jC_{j+2}/C_{j+1}^2)\) for \(j=0,1,2\). If
\[
C(t)=A\big[w e^{-\lambda t}+(1-w)e^{-\mu t}\big],\qquad A>0,\quad 0<w<1,\quad 0<\lambda<\mu,
\]
put \(q=e^{-(\mu-\lambda)h}\) and \(s=((1-w)/w)e^{-(\mu-\lambda)t_0}\). Then \(K_j>0\) and
\[
\boxed{\displaystyle \log\frac{K_1^2}{K_0K_2}>(\log q)^2\min_{z\in\{s,sq^2\}}\frac{2qz}{(1+z)(1+q^2z)}>0.}\tag{1}
\]
For the comparison profile
\[
C(t)=A\exp[-at-\beta(1-e^{-\kappa t})],\qquad A,a,\beta,\kappa>0,
\]
the same curvatures are positive and the log ratio on the left of (1) is exactly zero. The contribution is the explicit strictly positive lower bound (1). The sharp qualitative sample count is context: classical moment rank and Gaussian quadrature already give separation at five observations and overlap at four in this design.

## Assumptions and scope

Observations are equally spaced and exact, with no additive background or continuing input. The first profile is a positive sum of two fixed exponential losses. The second represents a single population with removal rate \(a+\beta\kappa e^{-\kappa t}\). The amplitudes cancel from the statistic. Neither the separation nor its quantitative margin is claimed for general biphasic mechanisms, data with noise, arbitrary sampling designs, or models with additional terms.

## Proof of the bound

Factoring out the slow exponential and canceling affine terms in the log gives \(K_j=H(sq^j)\), where
\[
H(z)=\log\frac{(1+z)(1+q^2z)}{(1+qz)^2}=\log\left(1+\frac{(1-q)^2z}{(1+qz)^2}\right)>0.
\]
For \(u=\log z\), write \(G(u)=\log H(e^u)=F(U(u))\), where
\[
F(v)=\log\log(1+e^v),\qquad U(u)=2\log(1-q)+u-2\log(1+qe^u).
\]
Putting \(y=e^v\), differentiation gives
\[
F'(v)=\frac{y}{(1+y)\log(1+y)}>\frac1{1+y},\qquad
F''(v)=\frac{y(\log(1+y)-y)}{(1+y)^2\log^2(1+y)}<0,
\]
and \(-U''(u)=2qe^u/(1+qe^u)^2>0\). The chain rule and \(1+e^{U(u)}=(1+e^u)(1+q^2e^u)/(1+qe^u)^2\) therefore give
\[
-G''(u)\ge F'(U(u))[-U''(u)]>\frac{2qe^u}{(1+e^u)(1+q^2e^u)}.
\]
With \(d=-\log q\) and \(u_1=\log(sq)\), the left side of (1) equals
\[
\int_{-d}^d(d-|v|)[-G''(u_1+v)]\,dv.
\]
The weight integrates to \(d^2\). The derivative of \(z/[(1+z)(1+q^2z)]\) has the sign of \(1-q^2z^2\), so the minimum on \([sq^2,s]\) is at an endpoint. This proves the strict bound. For the relaxing-hazard curve, direct second differencing gives \(K_j=\beta e^{-\kappa(t_0+jh)}(1-e^{-\kappa h})^2>0\). This is geometric, proving the zero comparison.

## Classical sample-count context

The two-pool samples are the moments of a positive measure on two points in \((0,1)\). Expanding the exponential in the relaxing-hazard samples gives the moment representation
\[
C_j=\sum_{m\ge0} b_m x_m^j,\qquad
b_m=Ae^{-\beta-at_0}\frac{(\beta e^{-\kappa t_0})^m}{m!},\qquad
x_m=e^{-(a+m\kappa)h}.
\]
This measure has positive mass at infinitely many distinct points in \((0,e^{-ah}]\). Its \(3\times3\) Hankel moment matrix from five observations is positive definite, since it integrates the square of each nonzero polynomial of degree at most two to a positive number. The corresponding two-point matrix has rank two.

Two-node Gaussian quadrature matches the relaxing-hazard moments of degrees 0 through 3 with two positive masses at distinct nodes in \((0,e^{-ah})\). In this discrete case, let \(p_2\) be the monic quadratic orthogonal to constants and linear polynomials in the moment measure. If it had fewer than two sign-changing zeros in \((0,e^{-ah})\), multiplying it by the product of the linear factors at those zeros would give a polynomial of constant sign on the support and nonzero integral, contrary to orthogonality. The two interior zeros are thus distinct. For a polynomial of degree at most three, divide by \(p_2\); the quotient has degree at most one and its term integrates to zero. The remainder is linear and its integral is the weighted sum at the two nodes with weights given by the integrals of their Lagrange basis polynomials. The weights are strictly positive because applying this exact formula to a squared basis polynomial gives its positive integral. A node \(x\) corresponds to a positive rate \(-\log(x)/h\); each node's positive quadrature weight is the corresponding exponential mass at time \(t_0\). This yields an admissible two-pool curve agreeing at any given four-sample relaxing-hazard grid. Both sample-count facts are direct applications of standard moment arguments, not new claims.

For a concrete illustration with \(h=1,t_0=0\), the pool \(A=1,w=1/2,\lambda=\log2,\mu=\log4\) gives \(1,3/8,5/32,9/128,17/512\). Put \(k_0=\log(10/9), k_1=\log(27/25), r=k_1/k_0\). The relaxing profile with \(A=1\), \(\kappa=-\log r\), \(\beta=k_0/(1-r)^2\) and \(a=\log(8/3)-k_0/(1-r)\) matches the first four values: it has the same initial value, first log decrement and first two log curvatures. Here \(0<r<1\), and \(k_0/(1-r)=k_0^2/(k_0-k_1)<250/567<1/2<\log(8/3)\), using \(k_0<1/9\) and \(k_0-k_1=\log(250/243)>7/250\). Thus all its rates are positive. For this illustration the log ratio for the pool is approximately 0.15380809, versus the lower bound 0.09043821.

## Verification and limitations

The derivative calculation, exact tent identity, and endpoint minimum prove (1) for all parameters specified. The companion `checker.py` uses standard Python 3.11+ to check the illustration at high precision and run supplementary finite numerical comparisons; these do not replace the analytic proof. The margin is parameter-dependent and can be arbitrarily small when the rates coalesce, a mixture component vanishes, or the sampling window shifts far into the slow tail. The test is not field-calibrated and cannot distinguish other mechanisms that generate the same curves.

## Relationship to prior work and references

- NIST Digital Library of Mathematical Functions, [§3.5(v), Gauss quadrature](https://dlmf.nist.gov/3.5#v), especially (3.5.18)–(3.5.20_1), and [§18.2(i), orthogonality on general sets](https://dlmf.nist.gov/18.2#i), (18.2.4_5). The degree-three exactness and positive nodes and weights argument explains the four-point ambiguity. Hankel rank explains qualitative five-point separation. Neither rank nor quadrature exactness gives the log-curvature lower bound.
- A. F. Brouwer et al., *Modeling Biphasic Environmental Decay of Pathogens and Implications for Risk Analysis* (2017), DOI [10.1021/acs.est.6b04030](https://doi.org/10.1021/acs.est.6b04030); B. C. Augustine et al., *A hierarchical model for eDNA fate and transport dynamics accommodating low concentration samples* (2024), DOI [10.1101/2024.03.27.586987](https://doi.org/10.1101/2024.03.27.586987); M. Y. Zanni et al., *Beyond Exponential Decay: How Biphasic and Delayed Decay Dynamics Shape Marine eDNA Dispersal* (2026), DOI [10.1002/ece3.72987](https://doi.org/10.1002/ece3.72987). These are modeling context, not evidence of priority for (1).
- M. F. Faddy and M. C. Jones, *Modelling and Analysis of Data that Exhibit Temporal Decay* (1999), DOI [10.1111/1467-9876.00151](https://doi.org/10.1111/1467-9876.00151). A potentially relevant model comparison; original full text was not available for this assessment. No definitive historical-priority claim is made for (1).
