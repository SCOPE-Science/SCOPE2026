# A sharp lengthscale-uniform positivity frontier for three-node Matérn quadrature

## Finding

Consider the Matérn-\(3/2\) covariance
\[
 k_t(x,y)=(1+t|x-y|)e^{-t|x-y|},\qquad t>0,
\]
with normalized uniform integration \(I(f)=\frac12\int_{-1}^1f(x)\,dx\). The *unaugmented, unconstrained* kernel-interpolatory quadrature uses the three nodes \((-a,0,a)\), \(0<a\le1\), and exact kernel weights \(w_-=w_+\) and \(w_0\).

**Theorem.** Both outer weights \(w_-\) and \(w_+\) are strictly positive for every \(0<a\le1\) and \(t>0\). All three weights are strictly positive for **every** finite inverse lengthscale \(t>0\) if and only if
\[
 \boxed{a\ge a_*:=6-\sqrt{30}=0.52277442494833886543\ldots.}
\]
For every \(0<a<a_*\), the central weight is strictly negative for all sufficiently small positive \(t\), and strictly positive for all sufficiently large \(t\). At equality \(a=a_*\), it is strictly positive for each finite \(t>0\) but tends to zero as \(t\downarrow0\). No uniqueness of a finite-lengthscale crossing is asserted below the threshold.

The exact flat-kernel limits are
\[
\boxed{\lim_{t\downarrow0}w_0=\frac{-a^2+12a-6}{8a},\qquad
\lim_{t\downarrow0}w_\pm=\frac{a^2-4a+6}{16a}.}
\]

## Assumptions and scope

The domain is \([-1,1]\), the integration probability is \(dx/2\), and the kernel has the displayed Matérn-\(3/2\) form, equivalent to conventional lengthscale \(\ell=\sqrt3/t\). Sites are exactly \((-a,0,a)\), with the endpoint sites allowed for \(a=1\). There is no observation noise, diagonal nugget, polynomial augmentation, positive-weight projection, or adaptive node placement. Positivity is positivity of coefficients, not a statement of numerical accuracy; these weights need not integrate constants exactly.

Put
\[
 k=(1+ta)e^{-ta},\qquad j=(1+2ta)e^{-2ta},\qquad
 M(u)=\int_0^u(1+ts)e^{-ts}\,ds=\frac{2-(2+tu)e^{-tu}}t.
\]
Let \(m_0=M(1)\), \(m_a=[M(1+a)+M(1-a)]/2\), and
\[
D=1+j-2k^2=1-(1+2ta+2t^2a^2)e^{-2ta}.
\]
The strictly positive-definite three-node kernel system \(Kw=m\) gives exactly
\[
\boxed{w_\pm=\frac{m_a-km_0}{D},\qquad
 w_0=\frac{(1+j)m_0-2km_a}{D}.}
\]

## Proof

**Denominator positivity.** Let \(z=ta>0\). Since \(e^{2z}>1+2z+2z^2\), the denominator \(D=1-(1+2z+2z^2)e^{-2z}\) is strictly positive.

**Outer-weight positivity.** By symmetry,
\[
2(m_a-km_0)=\int_0^1\left[k_t(a-s)+k_t(a+s)-2k_t(a)k_t(s)\right]ds,
\]
where the scalar-displacement notation uses absolute distance. For each \(s>0\), set \(u=t\min(a,s)>0\), \(v=t\max(a,s)\ge u\). The bracketed integrand is
\[
e^{-u-v}\left[(1+v-u)(e^{2u}-1)-2u(1+v)\right].
\]
The square bracket strictly increases in \(v\) because \(e^{2u}-1-2u>0\); its value at \(v=u\) is \(e^{2u}-1-2u-2u^2>0\). Thus the integrand is strictly positive for all \(s>0\), proving \(w_\pm>0\).

**Exact central sign.** Set \(z=ta\), \(b=(1-a)/a\ge0\); then \(t=(1+b)z\). Define
\[
F_b(z)=2(e^z-1-2z)+z(1+e^{-z})(1+bz)e^{-bz}.
\]
Inserting the primitive \(M\) into the center numerator and combining the displaced boundary exponentials yields the exact identity
\[
t\big[(1+j)m_0-2km_a\big]=(1-e^{-z})e^{-z}F_b(z).
\]
Thus \(\operatorname{sgn}w_0=\operatorname{sgn}F_b(z)\). Taylor expansion gives
\[
F_b(z)=\left(\frac56-b^2\right)z^3+O_b(z^4).
\]
If \(b>\sqrt{5/6}\), equivalently \(a<1/(1+\sqrt{5/6})=6-\sqrt{30}\), the center weight is strictly negative at every sufficiently small positive \(z\). For each fixed \(b\ge0\), the \(2e^z\) contribution eventually dominates and makes \(F_b(z)>0\) for sufficiently large \(z\). This proves necessity and the subcritical two signs without presuming a single crossing.

**Universal positivity above the frontier.** Suppose \(0\le b\le\sqrt{5/6}\). For all \(u\ge0\),
\[
(1+u)e^{-u}\ge1-\frac{u^2}{2}.
\]
Indeed, the difference vanishes at zero and has derivative \(u(1-e^{-u})\ge0\). Therefore
\[
F_b(z)\ge H(z):=2(e^z-1-2z)+z(1+e^{-z})\left(1-\frac{5z^2}{12}\right).
\]
A globally convergent exponential series gives
\[
e^zH(z)=2e^{2z}-\left(2+3z+\frac{5z^3}{12}\right)e^z+z-\frac{5z^3}{12}
=\sum_{n=4}^{\infty}\frac{A_n}{n!}z^n,
\]
where
\[
A_n=2^{n+1}-P_n,\qquad P_n=2+3n+\frac5{12}n(n-1)(n-2).
\]
Every \(A_n>0\) for integers \(n\ge4\). To prove it, \(A_4=8\), and for \(n\ge4\)
\[
2P_n-P_{n+1}=3n-1+\frac5{12}n(n-1)(n-5)>0
\]
(the value at \(n=4\) is 6; for \(n\ge5\) positivity is immediate). Hence \(A_{n+1}=2A_n+(2P_n-P_{n+1})>0\) inductively. Thus \(H(z)>0\) for every \(z>0\). Consequently \(F_b(z)>0\) and \(w_0>0\), *including equality* \(b=\sqrt{5/6}\).

**Flat limits.** The exact series imply \(D=\frac43z^3+O(z^4)\). The central identity gives
\[
\lim_{z\downarrow0} w_0=\frac3{4(1+b)}\left(\frac56-b^2\right)
=\frac{-a^2+12a-6}{8a}.
\]
The center kernel equation \(2kw_\pm+w_0=m_0\) and \(k,m_0\to1\) yield \(\lim w_\pm=(1-\lim w_0)/2\), the stated outer formula. This finishes all cases.

## Verification

The accompanying standalone script `verify.py` requires Python 3, `sympy`, and `mpmath`; `requirements.txt` records dependencies. It checks the exact numerator factorization, denominator reduction, and two leading series identities; checks the coefficient induction numerically at 96 successive indices; compares closed weight expressions with independent 90-digit three-by-three Gram-system solutions on 360 seeded parameter choices; tests 12 small-lengthscale limits; and checks a subcritical negative/positive pair and the boundary case. Observed execution:

```
PASS: 4 symbolic identities/series, 96 positive series coefficients, 372 high-precision linear-system and limit checks; both subcritical signs.
critical spacing: 0.5227744249483388654303021719919786604726
```

The infinite quantifiers and strict positivity at the critical spacing are established by the preceding analytic inequalities, **not** by finite experiments. Numerical ill-conditioning near the flat limit is bypassed by the symbolic series argument.

## Relationship to prior work

Karvonen, Kanagawa, and Särkkä [1] define the kernel-weight positivity problem, prove positivity under total-positivity and locally optimal-node hypotheses, and in their Section 4.5 specifically examine Matérn-\(3/2\) quadrature numerically. They explicitly say that existing general theory does not explain their observed Matérn positive weights. Their claims do not imply a sharp all-lengthscale positivity threshold for a prescribed symmetric three-node configuration. Glaubitz and Reeger [2] analyze compact-support, asymptotic, and oversampled least-squares stability for RBF quadrature, rather than the present unaugmented fixed-three-node Matérn classification. A previously published exact Gaussian-kernel three-node classification [3] obtains an all-scale threshold \(1/\sqrt3\) for the distinct squared-exponential kernel and does not imply the Matérn-specific threshold \(6-\sqrt{30}\). The latter requires the separate central numerator identity and global power-series bound proved above.

## Limitations

Only three symmetric sites, a bounded uniform integration law, noiseless Matérn-\(3/2\) interpolation, and exact arithmetic are treated. No classification of asymmetric nodes, polynomial augmentation, other Matérn smoothness orders, arbitrary grids, floating-point stability, or uniqueness of subcritical lengthscale crossings is claimed. Positive weights do not ensure exactness on constants or a particular accuracy order. Targeted prior-literature and research-record comparisons support novelty to the best of available evidence but cannot exclude every difficult-to-find earlier special-case result. No independent mathematical or priority validation has been performed.

## References

[1] T. Karvonen, M. Kanagawa, and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509, first public 2018-12-20; *Statistics and Computing* 29 (2019), DOI:10.1007/s11222-019-09901-0. https://arxiv.org/abs/1812.08509 ; https://link.springer.com/article/10.1007/s11222-019-09901-0

[2] J. Glaubitz and J. A. Reeger, *Towards stability results for global radial basis function based quadrature formulas*, arXiv:2301.12998, first public 2023-01-30. https://arxiv.org/html/2301.12998v1

[3] *A one-crossing positivity diagram for symmetric three-node Gaussian kernel quadrature* (published research record, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-one-crossing-positivity-diagram-for-symmetric-three-node-gauss--bf59562e8e52
