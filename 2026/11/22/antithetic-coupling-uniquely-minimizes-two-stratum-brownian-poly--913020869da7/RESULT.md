# Antithetic coupling uniquely minimizes two-stratum Brownian polynomial-moment quadrature risk

## Finding
For standard Brownian motion \(B\) on \([0,1]\), consider the first centered polynomial moment
\[
J=\int_0^1(t-\tfrac12)B_t\,dt.
\]
Choose observation times \(X=U/2\) and \(Y=(1+V)/2\), where \(U,V\) each have a uniform \([0,1]\) marginal, their joint law is arbitrary, and the pair is independent of \(B\). Observe exactly \(B_X,B_Y\) and use the conditional mean to estimate \(J\). The expected posterior mean-square error \(\mathcal R\) satisfies
\[
\mathcal R\ge\frac{41}{23040},
\]
with equality **if and only if** \(V=1-U\) almost surely. More precisely, the exact nonnegative optimality gap is
\[
\boxed{\mathcal R-\frac{41}{23040}=
\frac{\mathbb E\!\left[V(1-U)(1+V-U)(U+V-1)^2\right]}{1152}.}
\]
Both independent offsets and a common offset \(V=U\) instead have risk \(25/13824\), which exceeds the optimum by exactly \(1/34560\). The optimal law is the unique coupling over **all** copulas with the prescribed marginal distributions, not just within a parametric family.

## Assumptions and scope
The Brownian motion is centered, has unit diffusion variance, and starts at zero. The two random observation positions are disclosed to the estimator, are exogenous and independent of the path, and contain no observation noise. Only the coupling between the two uniform offsets may be designed. The loss is mean squared error for the single signed first-degree polynomial time moment; the conditional mean is the unrestricted Bayes estimator under this loss. Endpoint cases have zero probability under the uniform marginals and are understood by continuity.

## Proof
Write \(q(s)=s(1-s)/2\). Stochastic Fubini gives \(J=\int_0^1 q(s)\,dB_s\) and \(\operatorname{Var}(J)=\int_0^1q(s)^2\,ds=1/120\). For fixed \(0<x<y<1\), the two observations reveal the independent Brownian increments over \([0,x]\) and \([x,y]\). Orthogonal projection of \(q\) onto their indicator functions gives the exact posterior variance
\[
R(x,y)=\frac1{120}-\frac{Q(x)^2}{x}-\frac{(Q(y)-Q(x))^2}{y-x},\qquad
Q(z)=\frac{z^2}{4}-\frac{z^3}{6}.
\]
Equivalently, the residual integral on \([0,x]\) and \([x,y]\) consists of independent Brownian bridges, and the remaining tail is an unobserved Brownian increment. For a bridge interval \([a,b]\), the conditional variance of its weighted time integral is
\[
C(a,b)=\frac{(b-a)^3}{12}\left(\frac{a+b}{2}-\frac12\right)^2+\frac{(b-a)^5}{720}.
\]
This follows by integrating the bridge covariance \(\min(s,t)-a-(s-a)(t-a)/(b-a)\) against \((s-1/2)(t-1/2)\), or by computing the \(L^2\) variance of the quadratic function \(q\) after removing its interval average.

Substituting \(x=u/2\), \(y=(1+v)/2\), the posterior variance splits as \(R=A(u)+M(u,v)+T(v)\), where
\[
\begin{aligned}
A(u)&=\frac{u^3(4u^2-15u+15)}{5760},\\
T(v)&=\frac{(1-v)^3(3v^2+9v+8)}{1920},\\
M(u,v)&=C(u/2,(1+v)/2).
\end{aligned}
\]
The terms \(A,T\) depend on single marginals only. Their expectation is \(107/69120\), regardless of the copula. The crucial exact polynomial identity on the unit square is
\[
\boxed{M(u,v)=\frac{(1-u)^5+v^5}{1440}
+\frac{v(1-u)(1+v-u)(u+v-1)^2}{1152}.}
\]
The first two terms have fixed expectation \(1/4320\). All factors in the last term are nonnegative on the unit square. At points with \(0<u,v<1\), this term vanishes precisely when \(u+v=1\). Because both marginals are atomless uniform, equality of expected risk is therefore equivalent to \(V=1-U\) almost surely. Adding the fixed endpoint contribution proves the stated risk and exact gap. Direct polynomial integration for \(V=U\) and for independent \(U,V\) gives \(25/13824\) in both cases, proving the comparisons.

The argument is a constructive transport-dual certificate. In particular it does not rely on the cost being globally Monge: the mixed derivative of \(C(a,b)\) is proportional to \((a-b)(a+2b-3/2)(2a+b-3/2)\), whose sign changes across the admissible rectangle.

## Verification
Run `python check.py` with Python 3 and SymPy. It symbolically verifies the covariance/projection equality, the exact nonnegative polynomial factorization, three rational expected risks, and 841 exact-rational interior test pairs. The script is a reproducibility check and is not the mathematical proof; the displayed factor identity, its nonnegative factors and equality analysis establish the continuum result.

## Relationship to prior work
Foster, Lyons and Oberhauser (arXiv:1904.06998) motivate polynomial moment information for Brownian path approximation, including the integral and first polynomial coefficients. Karvonen, Kanagawa and Särkkä (arXiv:1812.08509) present the general Gaussian-process Bayesian quadrature posterior-variance framework, but study weight positivity, not dependence design of randomly stratified nodes. The published mathematical-record result titled *Exact design loss and Gaussian fluctuations for stratified Brownian kernel quadrature* studies independent uniformly jittered nodes and the unweighted integral; it does not assert the signed-moment all-copula antithetic optimality certificate here. The standard principle of antithetic coupling is established prior practice; only this precise signed-Brownian functional, its global uniqueness and exact non-Monge factor certificate are assessed as potentially new. Publication priority is not independently established.

## Limitations
The result is specific to standard Brownian covariance, a centered linear weight, one sample in each of two equal strata, no observation noise, and exogenous sampling sites. It does not assert that these marginals are globally best among arbitrary sampling designs. The relative posterior-risk improvement over independent/common offsets is \(2/125\), so the main contribution is the global dependence classification and certificate rather than a large numerical saving. Mathematical priority relative to historical stochastic-design and transport literature remains open to independent investigation.

## References
- J. Foster, T. Lyons and H. Oberhauser, *An optimal polynomial approximation of Brownian motion*, first public version 2019-04-15, arXiv:1904.06998, https://arxiv.org/abs/1904.06998.
- T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, first public version 2018-12-20, arXiv:1812.08509, https://arxiv.org/abs/1812.08509.
- *Exact design loss and Gaussian fluctuations for stratified Brownian kernel quadrature*, mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-design-loss-and-gaussian-fluctuations-for-stratified-brown--f119d713d36c (abstract-level comparison; full text not verified).
