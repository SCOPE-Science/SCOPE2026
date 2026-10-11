# Exact second-step curvature-activation gate in Apollo
## Finding

Apollo is designed to learn a diagonal quasi-Newton curvature approximation from first-order information and then rectify that approximation below by a positive floor.

On the simplest scalar quadratic, its zero initialization produces an exact and sharp curvature-activation gate.

Consider
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]
Use the source Apollo recurrence with constant learning rate
\[
\eta>0,
\]
momentum coefficient
\[
0<\beta<1,
\]
rectification floor
\[
\sigma>0,
\]
Hessian-update regularizer
\[
\varepsilon>0,
\]
and source initialization
\[
m_0=d_0=B_0=0.
\]

Define the two dimensionless quantities
\[
q=\frac{\eta\lambda}{\sigma},
\qquad
u=\frac{\lambda|x_0|}{\sigma}.
\]

At the first iteration,
\[
m_1=\lambda x_0,
\qquad
B_1=0,
\qquad
D_1=\sigma,
\qquad
d_1=\frac{\lambda x_0}{\sigma}.
\]
Therefore
\[
x_1=(1-q)x_0.
\]

The first nonzero Hessian estimate appears only at the next iteration. It is exactly
\[
B_2
=
\frac{\eta\lambda}{1+\beta}
\left(
\frac{u}{u+\varepsilon}
\right)^4.
\]

This immediately gives the sharp activation dichotomy.

If
\[
q\le1+\beta,
\]
then for every finite nonzero initialization
\[
B_2<\sigma,
\]
so
\[
D_2=\sigma.
\]
The learned curvature cannot escape the rectification floor by the second step, regardless of the size of \(x_0\).

If
\[
q>1+\beta,
\]
then
\[
B_2>\sigma
\]
holds exactly when
\[
|x_0|
>
\frac{
\sigma\varepsilon
}{
\lambda
\left[
(q/(1+\beta))^{1/4}-1
\right]
}.
\]

Thus the source zero-initialized Apollo recurrence has a sharp dimensionless second-step curvature threshold
\[
q=1+\beta.
\]

There is also a simple exact formula for the floor-controlled second iterate. On the branch
\[
D_2=\sigma,
\]
the bias-corrected moving gradient is
\[
m_2
=
\lambda x_0
\left(
1-\frac{q}{1+\beta}
\right),
\]
and therefore
\[
x_2
=
\left[
1-2q+\frac{q^2}{1+\beta}
\right]x_0.
\]

So before the curvature estimate clears the rectification floor, the first two parameter updates are completely determined by the floor scale and momentum coefficient. The quasi-Newton estimate has not yet altered the second update.

The learned estimate also has an exact saturation ceiling:
\[
\frac{B_2}{\sigma}
<
\frac{q}{1+\beta},
\]
with equality approached only in the large-initialization limit
\[
|x_0|\to\infty.
\]

Using the paper's values
\[
\beta=0.9,
\qquad
\sigma=0.01,
\qquad
\varepsilon=10^{-4},
\]
and a constant learning rate
\[
\eta=0.01,
\]
one has
\[
q=\lambda.
\]
Hence second-step curvature activation is impossible for every finite initialization whenever
\[
\lambda\le1.9.
\]

This exact gate gives a concrete mechanism behind Apollo's sensitivity to initialization and warmup: zero initialization forces at least the first update onto the rectification floor, and the next curvature estimate can become active only after a quantitative curvature-step threshold is crossed.

## Assumptions and scope

The theorem analyzes Algorithm 1 in the defining Apollo paper with the general rectification floor \(\sigma\), constant learning rate, zero weight decay, and deterministic scalar quadratic gradients.

The source algorithm uses
\[
m_0=d_0=B_0=0,
\]
a bias-corrected exponential moving average for the gradient, a diagonal Hessian update regularized by
\[
(\|d_t\|_4+\varepsilon)^4,
\]
rectification
\[
D_t=\max(|B_t|,\sigma),
\]
and parameter update
\[
x_{t+1}=x_t-\eta d_{t+1}.
\]

The finding concerns only the first two informative iterations. It does not classify long-run Apollo dynamics.

The numerical example uses a constant learning rate equal to the paper's later-stage scale. The repository recommends linear warmup from a much smaller initial learning rate; a varying schedule changes the numerical value of \(q\) from step to step.

## Proof

At the initial iteration the bias-corrected moving average is exactly the first gradient:
\[
m_1=g_1=\lambda x_0.
\]

The coefficient used to update \(B_0\) contains the previous direction \(d_0\), so zero initialization gives
\[
B_1=0.
\]
Rectification therefore yields
\[
D_1=\sigma.
\]
Hence
\[
d_1=\frac{m_1}{D_1}
=
\frac{\lambda x_0}{\sigma},
\]
and
\[
x_1
=
x_0-\eta d_1
=
(1-q)x_0.
\]

At the next iteration the source bias-corrected momentum recurrence gives
\[
m_2
=
\frac{\beta}{1+\beta}m_1
+
\frac{1}{1+\beta}g_2.
\]
Since
\[
g_2=\lambda x_1=\lambda(1-q)x_0,
\]
we obtain
\[
m_2
=
\lambda x_0
\left(
1-\frac{q}{1+\beta}
\right).
\]
Therefore
\[
m_2-m_1
=
-\frac{q}{1+\beta}\lambda x_0.
\]

Because \(B_1=0\), the scalar Hessian-update coefficient is
\[
a_1
=
\frac{
d_1(m_2-m_1)
}{
(|d_1|+\varepsilon)^4
}.
\]
The source update is
\[
B_2
=
B_1-a_1d_1^2.
\]
Substituting
\[
d_1=\frac{\lambda x_0}{\sigma}
\]
gives
\[
B_2
=
\frac{\sigma q}{1+\beta}
\frac{|d_1|^4}{(|d_1|+\varepsilon)^4}.
\]
Since
\[
\sigma q=\eta\lambda
\]
and
\[
|d_1|=u,
\]
this becomes
\[
B_2
=
\frac{\eta\lambda}{1+\beta}
\left(
\frac{u}{u+\varepsilon}
\right)^4.
\]

The ratio
\[
u/(u+\varepsilon)
\]
lies strictly between zero and one for every finite nonzero \(u\). Hence
\[
\frac{B_2}{\sigma}
<
\frac{q}{1+\beta}.
\]
If
\[
q\le1+\beta,
\]
this proves
\[
B_2<\sigma
\]
for every finite initialization.

For
\[
q>1+\beta,
\]
the inequality
\[
B_2>\sigma
\]
is equivalent to
\[
\frac{u}{u+\varepsilon}
>
\left(
\frac{1+\beta}{q}
\right)^{1/4}.
\]
Solving for \(u\) and then using
\[
u=\lambda|x_0|/\sigma
\]
gives the stated activation threshold.

Finally, when
\[
D_2=\sigma,
\]
one has
\[
d_2=\frac{m_2}{\sigma},
\]
so
\[
x_2
=
x_1-\eta d_2
=
\left[
1-2q+\frac{q^2}{1+\beta}
\right]x_0.
\]

## Verification

The accompanying `verify.py` directly replays the source scalar recurrence and compares it with the closed forms for \(x_1\), \(m_2\), \(B_2\), the activation threshold, and the floor-controlled \(x_2\).

It also stress-tests both sides of the sharp condition
\[
q=1+\beta
\]
over randomized parameters and initializations.

The numerical checks are transcription guards. The activation dichotomy and all formulas are proved algebraically above.

## Relationship to prior work

Ma introduced Apollo as a parameter-wise diagonal quasi-Newton method for nonconvex stochastic optimization. The defining paper states the zero initialization
\[
m_0=d_0=B_0=0,
\]
the diagonal Hessian update, rectification by a positive floor, and the bias-corrected gradient moving average. It also explicitly notes that bias correction is unavailable for the initial direction and Hessian estimate and reports that learning-rate warmup improves training stability.

The official implementation documentation goes further operationally: it recommends a small initial learning rate, a long warmup, and states that warmup plays an important role in stable Apollo training.

The inspected defining paper proves that learning rate and rectification floor are coupled under its initialization, but it does not state the exact second-step curvature estimate on a quadratic, the ceiling
\[
B_2/\sigma<q/(1+\beta),
\]
or the sharp activation threshold
\[
q=1+\beta.
\]

Focused published-record searches for Apollo quadratic dynamics, delayed Hessian activation, zero-initialized curvature learning, and second-step rectification did not identify an implication-equivalent result.

## Limitations

The theorem is a two-step local initialization result, not a long-time convergence theorem.

It assumes a scalar deterministic quadratic and constant learning rate.

A time-varying warmup schedule changes the step-specific value of
\[
q=\eta\lambda/\sigma.
\]

The Hessian-update regularizer \(\varepsilon\) affects the initialization threshold but not the universal condition
\[
q\le1+\beta
\]
that blocks second-step activation for every finite initialization.

## References

1. Xuezhe Ma, “Apollo: An Adaptive Parameter-wise Diagonal Quasi-Newton Method for Nonconvex Stochastic Optimization,” arXiv:2009.13586v1, 2020.
2. Official `XuezheMax/apollo` implementation documentation.
