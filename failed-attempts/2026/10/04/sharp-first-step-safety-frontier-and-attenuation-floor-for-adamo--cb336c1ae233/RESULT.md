# Sharp first-step safety frontier and attenuation floor for AdaMod
## Finding

AdaMod smooths Adam's coordinatewise learning rates and then clips each current rate by that smoothed value. This creates an exact structural limitation: the clip is relative, not absolute.

Let
\[
\eta_t\ge0,
\]
\[
s_t=\beta_3s_{t-1}+(1-\beta_3)\eta_t,
\qquad 0<\beta_3<1,
\qquad s_0=0,
\]
and
\[
\widehat\eta_t=\min(\eta_t,s_t).
\]
Then for every time and every nonnegative raw-rate history,
\[
(1-\beta_3)\eta_t\le\widehat\eta_t\le\eta_t.
\]
The lower bound is sharp, and at the first update
\[
\widehat\eta_1=(1-\beta_3)\eta_1.
\]
Thus AdaMod can attenuate an isolated raw Adam learning rate by at most the multiplicative factor \(1-\beta_3\); it does not impose an absolute cap independent of the raw rate.

Now consider
\[
f(x)=\frac h2x^2,
\qquad h>0,
\]
with arbitrary \(0\le\beta_1,\beta_2<1\), constant Adam base step \(\alpha>0\), denominator constant \(\varepsilon>0\), and no weight decay. First-step bias correction gives
\[
\widehat m_1=h x_0,
\qquad
\widehat v_1=h^2x_0^2,
\]
so
\[
\eta_1=\frac{\alpha}{h|x_0|+\varepsilon},
\qquad
\widehat\eta_1=(1-\beta_3)\frac{\alpha}{h|x_0|+\varepsilon}.
\]
Hence
\[
x_1=x_0\left[1-\frac{(1-\beta_3)\alpha h}{h|x_0|+\varepsilon}\right],
\]
and therefore
\[
\frac{f(x_1)}{f(x_0)}=
\left[1-\frac{(1-\beta_3)\alpha h}{h|x_0|+\varepsilon}\right]^2.
\]

Define
\[
A=(1-\beta_3)\alpha h.
\]
Then
\[
f(x_1)\le f(x_0)
\quad\text{for every }x_0\ne0
\]
if and only if
\[
A\le2\varepsilon,
\]
or equivalently
\[
h\le\frac{2\varepsilon}{(1-\beta_3)\alpha}.
\]
If \(A>2\varepsilon\), objective increase occurs exactly on
\[
0<|x_0|<\frac{A/2-\varepsilon}{h}.
\]
Moreover,
\[
\sup_{x_0\ne0}\frac{f(x_1)}{f(x_0)}
=
\left(\frac{A}{\varepsilon}-1\right)^2,
\]
with the supremum approached as \(x_0\to0\).

For the implementation-scale values
\[
\alpha=10^{-3},\qquad \varepsilon=10^{-8},
\]
with \(\beta_3=0.999\) and \(h=1\), the amplification supremum is \(99^2=9801\). With \(\beta_3=0.9999\), it is \(9^2=81\).

## Assumptions and scope

The attenuation-floor theorem uses only AdaMod's published smoothing and minimum-based clipping equations and is independent of any objective.

The quadratic theorem uses the source Adam bias corrections inside AdaMod. It is exact for arbitrary first- and second-moment coefficients because both bias-corrected moments reduce to the current gradient and its square at the first iteration.

The numerical examples use parameter scales documented in common AdaMod implementations. They illustrate the formula and are not claims about every experiment in the defining paper.

The theorem is a first-step safety statement. It does not assert divergence of the entire AdaMod trajectory.

## Proof

Since \(s_{t-1}\ge0\) and \(\eta_t\ge0\),
\[
s_t=\beta_3s_{t-1}+(1-\beta_3)\eta_t\ge(1-\beta_3)\eta_t.
\]
Therefore
\[
\widehat\eta_t=\min(\eta_t,s_t)\ge(1-\beta_3)\eta_t,
\]
while \(\widehat\eta_t\le\eta_t\) follows immediately from the minimum. At \(t=1\), \(s_0=0\) gives exact equality on the lower side.

For the quadratic, \(g_1=h x_0\). The Adam recurrences give
\[
m_1=(1-\beta_1)g_1,
\qquad
v_1=(1-\beta_2)g_1^2,
\]
and bias correction yields \(\widehat m_1=g_1\), \(\widehat v_1=g_1^2\). Substitution produces the displayed first-step formula.

Write
\[
K(x_0)=\frac{A}{h|x_0|+\varepsilon}.
\]
Then the objective ratio is \((1-K)^2\), and for positive \(K\),
\[
(1-K)^2\le1
\quad\Longleftrightarrow\quad
K\le2.
\]
Since \(K\) decreases strictly with \(|x_0|\) and has supremum \(A/\varepsilon\), uniform nonincrease is equivalent to \(A\le2\varepsilon\). If \(A>2\varepsilon\), solving \(K>2\) gives the exact expanding neighborhood. The supremum formula follows by taking \(x_0\to0\).

## Verification

The accompanying `verify.py` checks the attenuation floor on generated nonnegative raw-rate histories, directly replays the first AdaMod update over many values of \(\beta_1\), \(\beta_2\), and \(\beta_3\), verifies both sides of the sharp quadratic frontier, and reproduces the implementation-scale amplification factors.

The finite calculations are transcription guards. The all-history attenuation floor and the all-initialization first-step frontier are proved symbolically above.

## Relationship to prior work

Ding, Ren, Luo, and Sun introduced AdaMod to suppress unexpectedly large adaptive learning rates in the early training stage. Their Algorithm 2 forms an exponential moving average of Adam's raw coordinate rates,
\[
s_t=\beta_3s_{t-1}+(1-\beta_3)\eta_t,
\]
does not bias-correct this smoothing state, and applies
\[
\widehat\eta_t=\min(\eta_t,s_t).
\]
The paper emphasizes smoothing, long-term memory, and empirical stabilization.

The inspected defining paper does not state the universal lower bound
\[
\widehat\eta_t\ge(1-\beta_3)\eta_t,
\]
does not give a curvature-sensitive first-step safety condition, and does not analyze objective amplification on a scalar quadratic.

Public AdaMod implementations document learning-rate and epsilon scales such as \(10^{-3}\) and \(10^{-8}\), with smoothing coefficients around \(0.999\) to \(0.9999\). Those values make the exact dimensionless safety ratio \((1-\beta_3)\alpha h/\varepsilon\) large for order-one curvature, illustrating why rate smoothing and dynamical stability are distinct notions.

Focused published-record searches for AdaMod first-step stability, scalar-quadratic amplification, attenuation floors, and exact \(\beta_3\)-dependent safety conditions found no covering statement.

## Limitations

Later AdaMod states depend on complete histories of gradients, moments, and smoothed rates, so this theorem does not classify later-time stability.

A first-step objective increase does not by itself imply eventual divergence.

The scalar quadratic isolates curvature safety; multidimensional and stochastic behavior require separate analysis.

Implementation defaults vary slightly across packages, so the numerical examples are illustrative rather than canonical.

## References

1. Jianbang Ding, Xuancheng Ren, Ruixuan Luo, and Xu Sun, “An Adaptive and Momental Bound Method for Stochastic Learning,” arXiv:1910.12249v1, 2019.
2. `torch-optimizer` AdaMod implementation documentation.
