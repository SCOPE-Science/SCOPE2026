# Sharp Lorentz endpoint for weakly degenerate Grushin harmonic gradients

## Finding

Consider
\[
L=-\partial_x\!\left(|x|^{2\alpha}\partial_x\right)+|x|^{2\beta}\Delta_y
\]
on
\[
\mathbb R\times\mathbb R^m,
\]
with
\[
m\ge1,\qquad 0<\alpha<\frac12,\qquad \beta\ge0,
\]
and intrinsic gradient
\[
\nabla_L=
\left(
|x|^\alpha\partial_x,\,
|x|^\beta\nabla_y
\right).
\]
Set
\[
q_\alpha=\frac1\alpha.
\]

There are constants \(C>0\) and \(\kappa>1\), depending only on \(\alpha,\beta,m\), such that the following endpoint estimate holds. If \(B\) is a Grushin ball centered on the singular set \(\{x=0\}\), \(u\) is locally finite-energy and \(L\)-harmonic on \(\kappa B\), and \(r(B)\) is the intrinsic radius, then
\[
\sup_{\lambda>0}
\lambda
\left(
\frac{
\left|
\left\{
\xi\in B:
|\nabla_Lu(\xi)|>\lambda
\right\}
\right|
}{|B|}
\right)^\alpha
\le
\frac{C}{r(B)}
\fint_{\kappa B}|u(\xi)|\,d\xi.
\]
Equivalently,
\[
\nabla_Lu
\in
L^{1/\alpha,\infty}_{\mathrm{loc}}
\]
at the singular set with the same scale-invariant control as the strong reverse-Hölder estimates below the endpoint.

This Lorentz exponent is optimal. The explicit harmonic profile
\[
u_*(x,y)
=
\operatorname{sgn}(x)|x|^{1-2\alpha}
\]
satisfies
\[
|\nabla_Lu_*(x,y)|
=
(1-2\alpha)|x|^{-\alpha}.
\]
Hence, on every anchored ball,
\[
\nabla_Lu_*
\in
L^{1/\alpha,\infty}
\setminus
L^{1/\alpha},
\]
and for every
\[
q>\frac1\alpha
\]
one has
\[
\nabla_Lu_*
\notin
L^{q,\infty}.
\]

Thus the strong threshold
\[
p<\frac1\alpha
\]
has an exact weak endpoint for local harmonic gradients.

## Assumptions and scope

The harmonicity is with respect to the Friedrichs form used for the degenerate operator. In the weakly degenerate regime
\[
0<\alpha<\frac12,
\]
the form domain has a common trace across \(\{x=0\}\), and weak harmonicity imposes matching conormal flux.

The weak Lorentz quantity used above is the normalized local quasi-norm
\[
\sup_{\lambda>0}
\lambda
\left(
\frac{
|\{\xi\in B:|F(\xi)|>\lambda\}|
}{|B|}
\right)^{1/q}.
\]

The result concerns the local reverse-Hölder scale for gradients of harmonic functions. It does not claim restricted weak type or weak type at the endpoint for the global Riesz transform
\[
\nabla_LL^{-1/2}.
\]

## Proof

The 2026 kernel argument for the one-dimensional weakly degenerate case contains a pointwise estimate stronger than the strong \(L^p\) statement extracted from it.

After translating in the \(y\)-variable and applying the intrinsic Grushin dilation, an anchored ball is reduced to a fixed product box. In the normalized box, the localized harmonic function is split into even and odd Poisson and Green pieces. The source estimates show that the even pieces have bounded intrinsic gradient, while the odd pieces satisfy
\[
|x|^\alpha
|\nabla_L(\text{odd piece})|
\le
C\|u\|_{L^\infty}
\]
for
\[
0<|x|\le1.
\]
Consequently,
\[
|\nabla_Lu(x,y)|
\le
C A |x|^{-\alpha}
\]
on the inner normalized box, where local boundedness for harmonic functions gives
\[
A
\le
C
\fint_{\text{outer box}}|u|.
\]

Let
\[
q_\alpha=\frac1\alpha.
\]
For every \(t>0\),
\[
\left\{
(x,y):
C A |x|^{-\alpha}>t
\right\}
\]
is contained in a strip whose \(x\)-width is at most
\[
C
\left(
\frac{A}{t}
\right)^{1/\alpha}.
\]
The \(y\)-cross-section of the fixed box has bounded measure. Therefore
\[
\frac{
\left|
\left\{
|\nabla_Lu|>t
\right\}
\right|
}{
|\text{inner box}|
}
\le
C
\min
\left\{
1,\,
\left(
\frac{A}{t}
\right)^{q_\alpha}
\right\}.
\]
Multiplying by \(t\) and taking the \(q_\alpha\)-root of the normalized distribution function gives
\[
\|\nabla_Lu\|_{L^{q_\alpha,\infty}(\text{inner box})}
\le
C A.
\]

Undoing the intrinsic dilation contributes exactly one factor
\[
r(B)^{-1}
\]
to the gradient. Standard anchored ball-box comparability then yields
\[
\sup_{\lambda>0}
\lambda
\left(
\frac{
|\{\xi\in B:|\nabla_Lu(\xi)|>\lambda\}|
}{|B|}
\right)^\alpha
\le
\frac{C}{r(B)}
\fint_{\kappa B}|u|.
\]

For sharpness, set
\[
u_*(x,y)
=
\operatorname{sgn}(x)|x|^{1-2\alpha}.
\]
It has locally finite Friedrichs energy because
\[
|x|^{2\alpha}
|\partial_xu_*|^2
=
(1-2\alpha)^2|x|^{-2\alpha}
\]
is locally integrable precisely when
\[
\alpha<\frac12.
\]
Moreover,
\[
|x|^{2\alpha}\partial_xu_*
=
1-2\alpha
\]
on both sides of the singular set. Thus the conormal flux matches, and integration by parts shows
\[
Lu_*=0
\]
weakly across \(x=0\).

Its intrinsic gradient is exactly
\[
|\nabla_Lu_*|
=
(1-2\alpha)|x|^{-\alpha}.
\]
On any anchored ball, ball-box comparability gives, for all sufficiently large \(\lambda\),
\[
c\lambda^{-1/\alpha}
\le
\left|
\left\{
|\nabla_Lu_*|>\lambda
\right\}
\right|
\le
C\lambda^{-1/\alpha}.
\]
Therefore the weak
\[
L^{1/\alpha}
\]
quasi-norm is finite. The strong endpoint integral diverges logarithmically:
\[
\int_0^\varepsilon
x^{-\alpha(1/\alpha)}\,dx
=
\int_0^\varepsilon
\frac{dx}{x}
=
\infty.
\]
If
\[
q>\frac1\alpha,
\]
then
\[
\lambda
\left|
\left\{
|\nabla_Lu_*|>\lambda
\right\}
\right|^{1/q}
\gtrsim
\lambda^{1-\frac{1}{\alpha q}}
\longrightarrow\infty,
\]
so the weak exponent cannot be increased.

## Verification

The critical proof input was checked in the full primary text. In the proof of the weakly degenerate reverse-Hölder theorem, the odd Poisson and Green pieces carry exactly the factor
\[
|x|^{-\alpha}
\]
in their intrinsic-gradient bounds. The paper then integrates this factor to obtain strong \(L^p\) estimates for
\[
p<\frac1\alpha.
\]
Keeping the pointwise estimate instead of integrating it gives the endpoint distribution estimate above.

The sharpness profile was also checked in the full primary text: the same function
\[
u_*(x,y)
=
\operatorname{sgn}(x)|x|^{1-2\alpha}
\]
is used there to prove failure of the strong reverse-Hölder condition for
\[
p\ge\frac1\alpha.
\]
Its distribution function is elementary and gives the stronger Lorentz classification stated here.

No numerical experiment and no unproved endpoint interpolation are used.

## Relationship to prior work

The motivating 2026 paper proves that, in the weakly degenerate one-dimensional regime, the Riesz transform is bounded exactly for
\[
1<p<\frac1\alpha.
\]
Its local harmonic analysis proves strong reverse-Hölder estimates below that threshold and exhibits the singular harmonic profile above to show failure at and beyond the endpoint. It does not state the weak
\[
L^{1/\alpha,\infty}
\]
endpoint for harmonic gradients.

The same author has obtained Lorentz endpoint results for Riesz transforms on metric cones and on other noncompact geometries. Those are global endpoint operator estimates in different settings; they do not imply the local Grushin harmonic-gradient estimate here.

General weak reverse-Hölder inequalities for other elliptic systems and for weights use different hypotheses and exponents. The present endpoint is tied to the exact Friedrichs odd branch
\[
|x|^{1-2\alpha}
\]
and to the singular intrinsic-gradient scale
\[
|x|^{-\alpha}.
\]

Targeted searches for Grushin harmonic gradients, Lorentz endpoints, weak reverse-Hölder estimates, and the exact source identifier did not locate a published statement equivalent to this endpoint classification.

## Limitations

The theorem is local and concerns harmonic gradients. It does not establish endpoint weak type for
\[
\nabla_LL^{-1/2}.
\]

The proof is specific to
\[
n=1,
\qquad
0<\alpha<\frac12,
\]
where the odd Friedrichs branch crosses the singular set with finite energy.

No best numerical constant is claimed.

## References

1. D. He, *Riesz transform and its related inequalities for degenerate elliptic operators of Grushin type*, arXiv:2607.15599v1, 2026.
2. D. He, *On the Reverse Inequality of Riesz transform on metric cone with potential*, arXiv:2511.18365v1, 2025.
3. E. M. Robinson and A. Sikora, foundational work on degenerate elliptic operators and Grushin geometry cited in the primary source.
