# Fixed-centroid Blaschke speed variance: a factorial leakage law and truncated-exponential zero geometry

## Finding
Fix an integer \(n\ge2\). There is \(\varepsilon_n>0\) such that for every complex \(s\) with \(0<|s|<\varepsilon_n\), among all degree-\(n\) finite Blaschke products whose zeros \(a_1,\ldots,a_n\in\mathbb D\), counted with multiplicity, satisfy \(\sum_{j=1}^n a_j=s\), the variance
\[
V(B)=\frac1{2\pi}\int_0^{2\pi}\bigl(|B'(e^{it})|-n\bigr)^2\,dt
\]
has a unique minimizing zero multiset (and hence a unique minimizing Blaschke product up to unimodular multiplication). Its zeros are simple. With \(S_k=\sum_{j=1}^n a_j^k\), their power sums obey, for \(2\le k\le n\),
\[
S_k^{\mathrm{opt}}(s)=\frac{(-1)^k(n+1)}{k\,n!\,(n+1-k)!}\,s^k|s|^{2n+2-2k}+O_n\bigl(|s|^{2n+4-k}\bigr).
\]
The sharp minimum has the factorial defect
\[
\boxed{\min V(B)=2|s|^2+\frac{2}{(n!)^2}|s|^{2n+2}+O_n(|s|^{2n+4}).}
\]
In any consistent labeling, the optimizing zeros satisfy
\[
a_j(s)=s\xi_j+O_n(|s|^3),\qquad
\prod_{j=1}^n(z-\xi_j)=\sum_{k=0}^{n}\frac{(-1)^k}{k!}z^{n-k}.
\]
The \(\xi_j\) are distinct and nonzero. Thus the limiting optimizing geometry is governed by the reciprocal zeros of a truncated exponential polynomial, not by equal or collinear zeros.

## Assumptions and scope
A finite Blaschke product is \(B(z)=\gamma\prod_{j=1}^n(z-a_j)/(1-\overline{a_j}z)\), with \(|\gamma|=1\). Its boundary derivative is the positive angular speed \(|B'(e^{it})|\). All zero multisets are unordered; repeated zeros are permitted in the admissible class. The minimization fixes the *complex arithmetic sum* of the zeros, equivalently the first nonconstant Fourier coefficient of the boundary speed, not the product, the outermost radius, or the common radius. The theorem concerns each fixed \(n\) in a sufficiently small neighborhood of \(s=0\); no degree-uniform effective \(\varepsilon_n\) is claimed.

## Proof
**1. Parseval and coercivity.** The Poisson-kernel identity on the circle gives
\[
|B'(e^{it})|=\sum_{j=1}^n\frac{1-|a_j|^2}{|e^{it}-a_j|^2}
=n+2\operatorname{Re}\sum_{k\ge1}S_ke^{-ikt},\qquad
V(B)=2\sum_{k\ge1}|S_k|^2.
\]
The sum is absolutely convergent for all fixed zeros in the disk. Equivalently,
\[
\sum_{k\ge1}|S_k|^2
=\sum_{j,\ell=1}^n\operatorname{Re}\frac{a_j\overline{a_\ell}}{1-a_j\overline{a_\ell}}.
\]
For any \(|q|<1\), \(\operatorname{Re}(q/(1-q))>-1/2\). Hence the cross terms are bounded below uniformly, while each diagonal term \(|a_j|^2/(1-|a_j|^2)\) diverges when a zero approaches the circle. The objective is therefore coercive on the closed zero-constraint family and attains a minimum inside the disk for every sufficiently small \(s\).

**2. Newton coordinates and a sharp comparison configuration.** Set \(S_1=s\) and use \(S_2,\ldots,S_n\) as complex coordinates on unordered zero multisets. Newton's identities give
\[
e_0=1,\qquad ke_k=\sum_{j=1}^k(-1)^{j-1}e_{k-j}S_j\quad(1\le k\le n),
\]
where \(\prod_j(z-a_j)=\sum_{k=0}^n(-1)^ke_kz^{n-k}\). In particular, taking \(S_2=\cdots=S_n=0\) gives \(e_k=s^k/k!\), so the associated polynomial has all roots \(O_n(|s|)\) and is admissible for small \(s\). Its first unforced power sum is
\[
S_{n+1}^{(0)}=\frac{(-1)^{n-1}}{n!}s^{n+1}.
\]
All subsequent power sums are \(O_n(|s|^m)\) at order \(m\). Consequently this comparison configuration has energy \(\sum_{k\ge1}|S_k|^2=|s|^2+|s|^{2n+2}/(n!)^2+O_n(|s|^{2n+4})\).

**3. Global localization and uniqueness.** Every minimizer has \(\sum_{k=2}^n|S_k|^2=O_n(|s|^{2n+2})\). Thus \(S_k=O_n(|s|^{n+1})\) for \(2\le k\le n\). Newton's identities then imply \(e_k=O_n(|s|^k)\), hence all roots are \(O_n(|s|)\) by rescaling the polynomial. For small \(|s|\), the tail
\[
\mathcal T(s,S_2,\ldots,S_n)=\sum_{m>n}|S_m|^2
\]
is a real-analytic function in a full neighborhood of the origin in Newton coordinates, since all roots there have uniformly small modulus and each \(S_m\) is a polynomial in \(S_1,\ldots,S_n\). Every \(S_m\) for \(m>n\) has zero linear part at the origin; therefore the real Hessian of \(\mathcal T\) vanishes at the origin. The full energy \(|s|^2+\sum_{k=2}^n|S_k|^2+\mathcal T\) is strictly convex on a sufficiently small coordinate ball. All global minimizers eventually lie in that ball, which is itself feasible. Hence their Newton coordinates, and the zero multiset, are unique.

**4. The first correction.** The identity
\[
Q(z):=\prod_j(1-a_jz)=\left[\exp\left(-\sum_{k=1}^n\frac{S_kz^k}{k}\right)\right]_{\le n},\qquad
\sum_{m\ge1}S_mz^m=-z\frac{Q'(z)}{Q(z)},
\]
where brackets mean truncation through degree \(n\), yields at \(S_2=\cdots=S_n=0\)
\[
\left.\frac{\partial S_{n+1}}{\partial S_k}\right|_0
=-\frac{(n+1)(-s)^{n+1-k}}{k(n+1-k)!},\qquad 2\le k\le n.
\]
This follows directly by differentiating the truncated exponential and extracting the coefficient of \(z^{n+1}\). Since \(S_m\) has weighted degree \(m\) when \(S_k\) has weight \(k\), at a minimizer \(S_m=O_n(|s|^m)\) and \(\partial S_m/\partial S_k=O_n(|s|^{m-k})\) for \(m>n\). The stationarity equations
\[
0=S_k+\sum_{m>n}S_m\,\overline{\frac{\partial S_m}{\partial S_k}}
\]
first yield \(S_k=O_n(|s|^{2n+2-k})\), then, isolating \(m=n+1\), produce the displayed exact leading term with an \(O_n(|s|^{2n+4-k})\) remainder. The complex phase is fixed by rotational covariance \(S_k(e^{i\theta}s)=e^{ik\theta}S_k(s)\). Substitution gives the stated sharp energy defect; the remaining squared power sums are \(O_n(|s|^{2n+4})\).

**5. Simple-root geometry.** Divide the optimizer polynomial by \(s^n\) after writing \(z=s\xi\). Its coefficients converge to the displayed reverse truncated exponential polynomial, with errors \(O_n(|s|^2)\). This limiting polynomial has no repeated roots: if \(T_n(w)=\sum_{j=0}^n w^j/j!\) and \(T_n(w)=T_n'(w)=T_{n-1}(w)=0\), then \(w^n/n!=T_n(w)-T_{n-1}(w)=0\), contradicting \(T_n(0)=1\). The reverse polynomial also has no zero at the origin. Continuous root perturbation therefore gives simple optimizing zeros and the stated \(O_n(|s|^3)\) displacement.

## Verification
The accompanying `check.py` verifies Newton's identities and the first unforced-tail derivatives symbolically for degrees \(2\) through \(9\); checks the Poisson/Parseval identity on nonregular configurations; and performs finite small-centroid numerical diagnostics. At package preparation it passed 118 checks. These checks corroborate, but do not replace, the all-degree convexity and asymptotic proof above. The sharp factorial coefficient follows analytically from the unavoidable first unforced power sum, not from fitted numerics.

## Relationship to prior work
Kovalev and Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials* (first arXiv posting 19 July 2020), classify pointwise boundary-speed extreme values \(m(B)\) and \(M(B)\); their main theorem does not give a fixed-centroid integrated-variance minimizer. Gluchoff and Hartmann (2013) study interior Hardy means of finite Blaschke products and the effect of angular separation at prescribed common zero radius. Those results concern different objectives and restrictions. In particular, equal-radius angular and fixed-outermost-radius variance results do not imply an all-degree fixed-complex-centroid factorial asymptotic or a truncated-exponential optimizer. No dominating statement was identified in the checked prior-finding records or targeted literature searches; an unlocated equivalent moment-optimization formulation remains a priority risk.

## Limitations
The theorem proves local-in-centroid global uniqueness for each fixed degree, not an explicit optimal threshold or a classification for all allowed centroid values. The asymptotic expansions are not uniform as degree grows. The circle-speed variance is different from the interior Hardy mean of the Blaschke product. Historical novelty is best-knowledge, not independently established priority, and no independent mathematical audit has been performed.

## References
1. L. V. Kovalev and X. Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials*, arXiv:2007.09760 (initial version 19 July 2020); *Bull. Sci. Math.* 169 (2021), 102979. https://arxiv.org/abs/2007.09760
2. A. Gluchoff and F. Hartmann, *Hardy Means of a Finite Blaschke Product and Its Derivative*, in *Blaschke Products and Their Applications*, Fields Institute Communications 65 (2013), pp. 175–195. https://doi.org/10.1007/978-1-4614-5341-3_9
3. A. D. Baranov and I. R. Kayumov, *Estimates for the integrals of derivatives of rational functions in multiply connected domains in the plane*, *Izv. Math.* 86 (2022), 839–851. https://doi.org/10.4213/im9248e
