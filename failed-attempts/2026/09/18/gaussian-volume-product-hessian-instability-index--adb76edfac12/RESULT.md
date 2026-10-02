# Exact spherical-harmonic Hessian and instability index for the Gaussian volume product

## Statement

Let
\[
G_\sigma(K)=\gamma_\sigma^n(K)\,\gamma_\sigma^n(K^\circ),
\qquad
\gamma_\sigma^n(dx)=(2\pi\sigma^2)^{-n/2}e^{-|x|^2/(2\sigma^2)}\,dx,
\]
for convex bodies \(K\subset\mathbb R^n\) with \(0\in\operatorname{int}K\).  Put
\[
B=B_2^n,\qquad M_\sigma=\gamma_\sigma^n(B),\qquad
a_\sigma=(2\pi\sigma^2)^{-n/2}e^{-1/(2\sigma^2)}.
\]

For \(f\in C^\infty(S^{n-1})\), let \(K_t\) be the smooth strictly convex body whose support function is
\[
h_t=1+t f
\]
for all sufficiently small \(|t|\).  Then \(B\) is a critical point of \(G_\sigma\) in every smooth support-function direction and
\[
\boxed{
\frac{d^2}{dt^2}G_\sigma(K_t)\bigg|_{t=0}
=
M_\sigma a_\sigma
\left[
-\int_{S^{n-1}}|\nabla_S f|^2\,d\omega
+2\left(n-\frac1{\sigma^2}\right)\int_{S^{n-1}}f^2\,d\omega
\right]
-2a_\sigma^2\left(\int_{S^{n-1}}f\,d\omega\right)^2 .
}
\]

Write
\[
f=\bar f+\sum_{\ell\ge1}f_\ell
\]
for the orthogonal spherical-harmonic decomposition, where \(f_\ell\) has degree \(\ell\) and
\[
-\Delta_S f_\ell=\lambda_\ell f_\ell,\qquad
\lambda_\ell=\ell(\ell+n-2).
\]
Define
\[
\tau_\sigma
=
\frac{a_\sigma |S^{n-1}|}{M_\sigma}
=
\frac{e^{-1/(2\sigma^2)}}
{\int_0^1e^{-r^2/(2\sigma^2)}r^{n-1}\,dr}.
\]
Then
\[
\frac{G_\sigma''(0)}{M_\sigma a_\sigma}
=
2\left(n-\frac1{\sigma^2}-\tau_\sigma\right)\|\bar f\|_2^2
+
\sum_{\ell\ge1}
\left[
2\left(n-\frac1{\sigma^2}\right)-\lambda_\ell
\right]\|f_\ell\|_2^2.
\]

The constant-mode coefficient is always strictly negative.  Among all nonconstant modes, the degree-one coefficient is
\[
n+1-\frac{2}{\sigma^2},
\]
while the degree-two coefficient is
\[
-\frac{2}{\sigma^2},
\]
and all higher coefficients are still smaller.  Consequently:

1. If
   \[
   \sigma^2<\frac{2}{n+1},
   \]
   the Hessian of \(G_\sigma\) at \(B\) is strictly negative in every nonzero smooth support-function direction.

2. If
   \[
   \sigma^2=\frac{2}{n+1},
   \]
   its nullspace is exactly the \(n\)-dimensional space of degree-one spherical harmonics, i.e. infinitesimal translations; every other direction is strictly negative.

3. If
   \[
   \sigma^2>\frac{2}{n+1},
   \]
   the positive index of the Hessian is exactly \(n\), with positive eigenspace precisely the degree-one harmonics.  All genuine shape modes of degree at least two remain strictly negative.

Thus the threshold \(2/(n+1)\) found by Artstein-Avidan, Fradelizi and Wyczesany from a single translated-ball perturbation is the exact full second-variation threshold: no hidden higher spherical-harmonic instability appears earlier.

In particular, for \(n\ge3\) throughout the unresolved global interval
\[
\frac1n<\sigma^2<\frac{2}{n+1},
\]
the unit ball is a strict infinitesimal local maximizer in every smooth support-function direction.  Any failure of global optimality in this interval, should one exist, therefore cannot be detected by a nonzero quadratic variation at the ball.

## Proof

For small \(|t|\),
\[
\nabla_S^2 h_t+h_tI
=
I+t(\nabla_S^2f+fI)
\]
is positive definite, so \(h_t\) is the support function of a smooth strictly convex body.  Its boundary point with outer normal \(u\) is
\[
x_t(u)=h_t(u)u+\nabla_Sh_t(u)
=u+t(fu+\nabla_Sf).
\]

The Gaussian surface-area formula and first variation give
\[
\frac{d}{dt}\gamma_\sigma^n(K_t)
=
\int_{S^{n-1}}f\,dS_{\gamma_\sigma,K_t},
\]
with density
\[
dS_{\gamma_\sigma,K_t}(u)
=
(2\pi\sigma^2)^{-n/2}
e^{-|x_t(u)|^2/(2\sigma^2)}
\det(\nabla_S^2h_t+h_tI)\,d\omega(u).
\]
At \(t=0\),
\[
\frac{d}{dt}|x_t|^2\bigg|_{0}=2f
\]
and
\[
\frac{d}{dt}\det(\nabla_S^2h_t+h_tI)\bigg|_{0}
=
\Delta_Sf+(n-1)f.
\]
Hence
\[
A(t):=\gamma_\sigma^n(K_t)
\]
satisfies
\[
A(0)=M_\sigma,\qquad
A'(0)=a_\sigma\int f\,d\omega
\]
and, after integration by parts,
\[
A''(0)
=
a_\sigma\left[
-\int|\nabla_Sf|^2\,d\omega
+
\left(n-1-\frac1{\sigma^2}\right)\int f^2\,d\omega
\right].
\]

For the polar body,
\[
\rho_{K_t^\circ}(u)=\frac1{h_t(u)}.
\]
Let
\[
F(r)=(2\pi\sigma^2)^{-n/2}
\int_0^r e^{-s^2/(2\sigma^2)}s^{n-1}\,ds.
\]
Then
\[
B(t):=\gamma_\sigma^n(K_t^\circ)
=
\int_{S^{n-1}}F\!\left(\frac1{1+tf}\right)d\omega,
\]
and
\[
F'(1)=a_\sigma,\qquad
F''(1)=a_\sigma\left(n-1-\frac1{\sigma^2}\right).
\]
Differentiating twice yields
\[
B(0)=M_\sigma,\qquad
B'(0)=-a_\sigma\int f\,d\omega,
\]
and
\[
B''(0)
=
a_\sigma\left(n+1-\frac1{\sigma^2}\right)
\int f^2\,d\omega.
\]

The first derivatives cancel in the product \(G_\sigma(K_t)=A(t)B(t)\), proving criticality.  Combining the second derivatives gives
\[
G_\sigma''(0)
=
M_\sigma(A''(0)+B''(0))
+2A'(0)B'(0),
\]
which is the displayed Hessian formula.

It remains to determine its signs.  The only term coupling different spherical harmonics is the square of the mean, so the decomposition is diagonal.  For every degree \(\ell\ge1\), the coefficient is
\[
\mu_\ell
=
2\left(n-\frac1{\sigma^2}\right)-\ell(\ell+n-2).
\]
Thus
\[
\mu_1=n+1-\frac2{\sigma^2},
\qquad
\mu_2=-\frac2{\sigma^2},
\]
and \(\mu_\ell<\mu_2<0\) for every \(\ell>2\).

For constants, set
\[
J=\int_0^1e^{-r^2/(2\sigma^2)}r^{n-1}\,dr,\qquad
J_2=\int_0^1e^{-r^2/(2\sigma^2)}r^{n+1}\,dr.
\]
Integrating the derivative of
\[
r^ne^{-r^2/(2\sigma^2)}
\]
over \([0,1]\) gives
\[
e^{-1/(2\sigma^2)}
=
nJ-\frac1{\sigma^2}J_2.
\]
Since \(0<J_2<J\),
\[
\tau_\sigma
=
n-\frac1{\sigma^2}\frac{J_2}{J}
>
n-\frac1{\sigma^2}.
\]
Therefore the constant-mode coefficient
\[
2\left(n-\frac1{\sigma^2}-\tau_\sigma\right)
\]
is strictly negative for every \(\sigma>0\).  The three cases follow immediately from the sign of \(\mu_1\).

## Relation to prior work

Artstein-Avidan, Fradelizi and Wyczesany introduced and analyzed this uncentered Gaussian volume-product maximization problem in arXiv:2609.18472.  They prove that the unit ball is the unique global maximizer for \(\sigma^2\le1/n\) in dimensions \(n\ge3\), while a translated-ball calculation proves that it is not a maximizer for \(\sigma^2>2/(n+1)\); in dimension two the global threshold is \(2/3\).  Their paper explicitly leaves the interval
\[
1/n<\sigma^2<2/(n+1)
\]
open for \(n\ge3\).

The degree-one term above recovers their translated-ball coefficient exactly.  The new point is the full support-function Hessian and its complete spectral diagonalization: it rules out every other second-order instability, identifies the exact nullspace at the transition, and shows that the translated mode exhausts the entire positive index above the transition.

Targeted searches for the Gaussian volume product together with second variation, Hessian, spherical harmonics, Morse index, local stability and translation modes did not locate a prior statement of this spectral theorem.  Searches of the current SCOPE archive likewise found no overlapping record.

## Limitations

This is a second-variation theorem, not a solution of the remaining global maximization problem for \(n\ge3\).  Strict negativity of the Hessian in the open gap establishes infinitesimal stability along every fixed smooth support-function direction, but no uniform infinite-dimensional nonlinear local-maximality theorem is asserted here.  At the critical value \(\sigma^2=2/(n+1)\), the quadratic form vanishes on translations, and no higher-order sign is claimed.  The calculation is for smooth support-function perturbations of the unit ball.  The motivating preprint is very recent, so unindexed parallel work remains a residual originality risk.

## References

1. S. Artstein-Avidan, M. Fradelizi, K. Wyczesany, *Uncentered Blaschke-Santaló inequalities for the Gaussian measure*, arXiv:2609.18472 (2026). https://arxiv.org/abs/2609.18472
2. Y. Huang, D. Xi, Y. Zhao, *The Minkowski problem in Gaussian probability space*, Advances in Mathematics 385 (2021), 107769. https://doi.org/10.1016/j.aim.2021.107769
3. R. Schneider, *Convex Bodies: The Brunn-Minkowski Theory*, 2nd expanded ed., Cambridge University Press, 2014.
