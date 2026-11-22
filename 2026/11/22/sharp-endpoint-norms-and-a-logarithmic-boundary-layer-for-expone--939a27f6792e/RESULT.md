# Sharp endpoint norms and a logarithmic boundary layer for exponential least-squares projection

## Finding
Fix \(\lambda>0\). Let \(P_\lambda\) be the real \(L^2([0,1],dt)\)-orthogonal projection onto \(E_\lambda=\operatorname{span}\{1,e^{-\lambda t}\}\), acting from real \(L^\infty([0,1])\) to continuous functions on \([0,1]\). Define
\[
q=e^{-\lambda},\quad m=\frac{1-q}{\lambda},\quad
v=\frac{1-q^2}{2\lambda}-m^2,\quad
k_+=\frac{1-m}{v},\quad k_- =\frac{q-m}{v}.
\]
Let \(z_\pm=m-1/k_\pm\), \(t_\pm=-\lambda^{-1}\log z_\pm\), and
\[
F_k(t)=(1-km)t+\frac{k}{\lambda}(1-e^{-\lambda t}).
\]
Then \(0<q<z_+<m<z_-<1\), \(0<t_-<t_+<1\), and the exact operator norm is
\[
\boxed{\|P_\lambda\|_{L^\infty\to L^\infty}
 =\max\{2F_{k_+}(t_+)-1,\ 1-2F_{k_-}(t_-)\}.}
\]
The norm is attained on real bounded measurable functions taking values in \(\{-1,1\}\) almost everywhere, with the maximum output occurring at an endpoint. The largest possible negative value at an arbitrary point of \(P_\lambda f\) among all data \(0\le f\le1\) is exactly \(-(\|P_\lambda\|-1)/2\).

There are two exact scale limits:
\[
\|P_\lambda\|=\frac53+\frac4{27}\lambda+O(\lambda^2)\qquad(\lambda\downarrow0),
\]
\[
\|P_\lambda\|=3-\frac{2\log(2\lambda)-2}{\lambda}
   +O\!\left(\frac{\log\lambda}{\lambda^2}\right)
\qquad(\lambda\to\infty).
\]
Thus the strongly decaying mode produces a logarithmic transition layer at \(t_+\sim\log(2\lambda)/\lambda\), while its sharp worst-case uniform-data amplification approaches three. The claim is about the displayed orthogonal projection, not an optimal projection among all maps onto \(E_\lambda\).

## Assumptions and scope
All scalars and functions are real. The sampling measure is Lebesgue measure on \([0,1]\), the exponential decay rate is positive, and both input and output are measured in the essential/supremum norm. The basis is nonconstant for every fixed positive rate, so \(v>0\). Values at the endpoints refer to the continuous representative of the output. The two asymptotic statements are one-sided in the indicated limits, not finite-rate upper/lower bounds.

## Proof
1. Put \(u(t)=e^{-\lambda t}\). Gram orthogonalization of \(1,u\) gives the projection kernel
   \[
   K_\lambda(x,t)=1+\frac{(u(x)-m)(u(t)-m)}{v},\qquad
   (P_\lambda f)(x)=\int_0^1K_\lambda(x,t)f(t)\,dt.
   \]
   Its integral with respect to \(t\) is exactly one. Hence the operator norm equals \(\max_{x\in[0,1]}\int_0^1|K_\lambda(x,t)|\,dt\): the upper bound is immediate and a sign choice for the row kernel realizes the lower bound in \(L^\infty\).
2. For fixed \(t\), the kernel is affine in the scalar \(u(x)\). Thus \(s\mapsto\int_0^1|1+(s-m)(u(t)-m)/v|\,dt\) is convex on \([q,1]\). A convex function on a compact interval is never larger than its largest endpoint value, so the norming rows occur at \(x=0\) or \(x=1\).
3. The random variable \(u(T)\) for uniform \(T\in[0,1]\) lies strictly between \(q\) and \(1\) almost surely, and its variance obeys the strict Bhatia–Davis inequality \(0<v<(1-m)(m-q)\). The inequality also follows directly by integrating \((1-u)(u-q)>0\), whose expectation is \((1-m)(m-q)-v\). Consequently \(K_\lambda(0,0)>0>K_\lambda(0,1)\) and \(K_\lambda(1,0)<0<K_\lambda(1,1)\). Each endpoint kernel has exactly one zero because \(u(t)\) is strictly decreasing. Solving \(1+k_\pm(u(t)-m)=0\) locates those zeros at \(t_\pm\) and establishes all stated inequalities for \(z_\pm,t_\pm\).
4. The primitive of the endpoint kernel is \(F_{k_\pm}\). Since \(F_k(1)=1\), integrating the absolute value across its unique zero gives the two exact branch formulas \(2F_{k_+}(t_+)-1\) and \(1-2F_{k_-}(t_-)\). The first comes from the positive initial portion of the row; the second from its negative initial portion. This completes the exact norm formula. Since the kernel row has integral one, the minimum response for data in \([0,1]\) is the integral of its negative part, \((1-\int|K|)/2\), which proves the sharp positivity-loss statement.
5. For small \(\lambda\), replace the nonconstant basis vector by \(g_\lambda(t)=(1-e^{-\lambda t})/\lambda=t-\lambda t^2/2+O(\lambda^2)\), which spans the same space along with constants. Uniform Taylor expansion of the Gram formula yields
   \[
   K_\lambda(0,t)=4-6t+\lambda(3t^2-4t+1)+O(\lambda^2),
   \]
   \[
   K_\lambda(1,t)=6t-2+\lambda(2t-3t^2)+O(\lambda^2).
   \]
   At \(\lambda=0\), the zeros are respectively \(2/3\) and \(1/3\) and are simple. Differentiating their absolute kernel integrals (zero motion adds no first-order boundary term) gives the opposite derivatives \(+4/27\) and \(-4/27\). Both zeroth-order row norms are \(5/3\). Taking the larger branch proves the first expansion.
6. For large \(\lambda\), set \(q=e^{-\lambda}\). The direct expansions are
   \[
   m=\lambda^{-1}+O(q/\lambda),\quad
   v=(2\lambda)^{-1}-\lambda^{-2}+O(q/\lambda),\quad
   k_+=2\lambda+2+O(\lambda^{-1}),
   \]
   \[
   z_+=(2\lambda)^{-1}+O(\lambda^{-2}),\qquad
   t_+=\frac{\log(2\lambda)}{\lambda}+O(\lambda^{-2}),
   \]
   and therefore
   \[
   2F_{k_+}(t_+)-1
   =3-\frac{2\log(2\lambda)-2}{\lambda}
    +O\!\left(\frac{\log\lambda}{\lambda^2}\right).
   \]
   On the opposite endpoint \(k_-=-2+O(\lambda^{-1})\), \(z_-=1/2+O(\lambda^{-1})\), \(t_-=(\log2)/\lambda+O(\lambda^{-2})\), so \(1-2F_{k_-}(t_-)=1+O(\lambda^{-1})\). Thus the first branch is larger for all sufficiently large rates and gives the stated second expansion. These are ordinary expansions of explicit functions; no sampled finite-rate calculation is needed for the asymptotic claims.

## Verification
The standalone `check.py` performs high-precision direct integrations of the exact kernel, checks both branch formulas and interior evaluation rows at several rates, and tests the displayed small- and large-rate expansions. It passed 243 supplementary assertions. Numerical comparisons are illustrative: the infinite-dimensional norm is proved by the convexity and sign arguments above, not by enumeration.

## Relationship to prior work
Themistoclakis and Van Barel (2018, arXiv:1806.00439 and arXiv:1808.03530) analyze least-squares Lebesgue constants for polynomial projection on spheres, establishing the importance of the maximum row integral of a projection kernel. Their objects are spherical polynomial spaces with discrete quadrature nodes, not the two-mode nonsymmetric exponential span on an interval. Kayumov (2004, arXiv:math/0408418) treats global orthogonal projection on second-order exponential-spline spaces and proves a sharp *mesh-uniform* constant of three for the symmetric-exponent family, along with boundedness for unequal opposite-sign exponents. The present fixed-interval, one-zero-exponent formula and its logarithmic finite-rate boundary layer do not follow from that mesh-uniform bound. It would be incorrect to claim that three as a general exponential-spline envelope is new. The distinctions are a fixed exponential rate, an exact rate-dependent formula, endpoint zero positions, and the sharp correction to the limiting value.

## Limitations
No assertion is made that the initial-endpoint formula dominates the terminal-endpoint formula at every positive rate; the exact norm deliberately retains their maximum. No claim is made about variable sampling weights, arbitrary knots, polynomial or multiparameter exponential spaces, complex inputs, or minimum-norm projections. Uninspected or incompletely indexed older exponential-approximation literature remains a historical-priority risk. Numerical tests do not substitute for the analytic argument.

## References
- W. Themistoclakis and M. Van Barel, *Uniform approximation on the sphere by least squares polynomials*, arXiv:1806.00439 (first public June 1, 2018), https://arxiv.org/abs/1806.00439 .
- W. Themistoclakis and M. Van Barel, *Optimal Lebesgue constants for least squares polynomial approximation on the (hyper)sphere*, arXiv:1808.03530 (first public August 10, 2018), https://arxiv.org/abs/1808.03530 .
- A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418 (first public August 30, 2004), https://arxiv.org/abs/math/0408418 .
- X. Xu, *On the perturbation of an L2-orthogonal projection*, arXiv:1809.00200 (first public September 1, 2018), https://arxiv.org/abs/1809.00200 .
