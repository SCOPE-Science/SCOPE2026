# SPI-Optimizer exactly erases momentum after a scalar overshoot
## Finding

SPI-Optimizer keeps the momentum term only while the current gradient and the stored momentum have consistent signs. On a scalar positive quadratic, one overshooting step can therefore switch the method permanently into exact gradient descent.

Let
\[
f(\theta)=\frac12\lambda\theta^2,
\qquad
\lambda>0.
\]
Use source-form SPI-Optimizer with learning rate
\[
r>0,
\]
momentum coefficient
\[
0\le\alpha<1,
\]
standard initialization
\[
v_0=0,
\]
and
\[
\theta_0\ne0.
\]

Write
\[
s=r\lambda.
\]
The source scalar update is
\[
v_{t+1}
=
\alpha v_t I_t+s\theta_t,
\qquad
\theta_{t+1}
=
\theta_t-v_{t+1},
\]
where
\[
I_t=
\begin{cases}
1,& \theta_t v_t>0,\\
0,& \theta_t v_t\le0.
\end{cases}
\]
The zero case does not affect the first step because \(v_0=0\).

Assume
\[
s>1.
\]
The first step is
\[
v_1=s\theta_0,
\qquad
\theta_1=(1-s)\theta_0.
\]
Therefore
\[
\theta_1v_1<0,
\]
so the momentum term is discarded at the next update.

In fact, it is discarded forever. For every
\[
t\ge1,
\]
\[
\boxed{
\theta_t=(1-s)^t\theta_0,
\qquad
v_t=s(1-s)^{t-1}\theta_0.
}
\]
Hence
\[
\theta_t v_t
=
s(1-s)^{2t-1}\theta_0^2<0,
\]
so the sign-consistency gate remains off permanently.

Thus, throughout the entire overshoot regime,
\[
\boxed{
\theta_{t+1}=(1-s)\theta_t,
}
\]
exactly the scalar gradient-descent recurrence.

This yields a sharp phase diagram:

\[
\boxed{
1<s<2
}
\]
gives geometric convergence with factor
\[
s-1.
\]

At
\[
\boxed{
s=2,
}
\]
\[
\theta_t=(-1)^t\theta_0,
\]
so the method has a neutral two-cycle.

For
\[
\boxed{
s>2,
}
\]
\[
|\theta_t|=(s-1)^t|\theta_0|,
\]
so the method diverges.

The result is independent of the momentum coefficient \(\alpha\).

For comparison, ordinary momentum with the same \(r,\lambda,\alpha\) obeys
\[
\theta_{t+1}
=
(1+\alpha-s)\theta_t-\alpha\theta_{t-1}.
\]
Its scalar Schur-stability region is
\[
\boxed{
0<s<2(1+\alpha).
}
\]
Therefore, whenever
\[
\alpha>0,
\]
the interval
\[
\boxed{
2<s<2(1+\alpha)
}
\]
is stable for ordinary momentum but unstable for SPI-Optimizer.

So the source sign gate does exactly eliminate stale momentum after a sign reversal, but it also removes momentum's enlarged scalar linear-stability interval once the first step overshoots.

## Assumptions and scope

The theorem concerns the source coordinatewise SPI update on one deterministic scalar quadratic mode.

The standard zero-momentum initialization is used.

The sign gate is interpreted exactly as described by the source text: momentum is retained only when the gradient and stored momentum have the same sign, and is discarded when their signs are inconsistent.

The result classifies the regime
\[
s=r\lambda>1,
\]
where the first step crosses the scalar optimum. It does not classify every possible branch sequence for
\[
0<s\le1.
\]

The comparison with ordinary momentum is deterministic and scalar. It does not contradict the source's empirical results on stochastic neural-network training.

## Proof

Because
\[
v_0=0,
\]
the first update contains no inherited momentum:
\[
v_1=s\theta_0.
\]
Hence
\[
\theta_1
=
\theta_0-v_1
=
(1-s)\theta_0.
\]
For
\[
s>1,
\]
the factors \(s\) and \(1-s\) have opposite signs, so
\[
\theta_1v_1<0.
\]
The source gate therefore sets the momentum contribution to zero at the next step.

Suppose for some
\[
t\ge1
\]
that
\[
\theta_t=(1-s)^t\theta_0,
\qquad
v_t=s(1-s)^{t-1}\theta_0.
\]
Then
\[
\theta_t v_t
=
s(1-s)^{2t-1}\theta_0^2<0.
\]
Thus the momentum gate is again off, giving
\[
v_{t+1}=s\theta_t
=
s(1-s)^t\theta_0
\]
and
\[
\theta_{t+1}
=
\theta_t-v_{t+1}
=
(1-s)^{t+1}\theta_0.
\]
Induction proves the closed form.

The convergence, neutral-cycle, and divergence cases follow from the modulus of
\[
1-s.
\]

For ordinary momentum,
\[
v_{t+1}=\alpha v_t+s\theta_t,
\qquad
\theta_{t+1}=\theta_t-v_{t+1}.
\]
Using
\[
v_t=\theta_{t-1}-\theta_t
\]
gives
\[
\theta_{t+1}
=
(1+\alpha-s)\theta_t-\alpha\theta_{t-1}.
\]
Its characteristic polynomial is
\[
z^2-(1+\alpha-s)z+\alpha.
\]
The second-order Jury conditions reduce, for
\[
0\le\alpha<1,
\]
to
\[
s>0
\]
and
\[
s<2(1+\alpha).
\]
This proves the strict comparison interval.

## Verification

The accompanying `verify.py` replays the source sign-gated momentum update over deterministic scalar quadratics.

It checks the exact closed form for many learning-rate and momentum choices in the overshoot regime, verifies permanent momentum erasure, confirms the neutral two-cycle at
\[
s=2,
\]
and compares the SPI phase boundary against direct eigenvalue calculations for ordinary momentum.

The computations are transcription guards. The phase diagram is proved analytically above.

## Relationship to prior work

Wang and coauthors introduce SPI-Optimizer as an integral-separated PI controller for stochastic optimization. Their source recurrence conditionally keeps the momentum term only when the current gradient and stored momentum have consistent signs.

The defining paper motivates this rule by overshoot: once a parameter crosses the optimum, historical momentum can point in the stale direction, so SPI discards that integral component and reduces the state delay to the gradient-descent value.

The source supplement proves convergence under a conservative strongly-convex smooth sufficient condition. The inspected full text does not state the exact scalar overshoot recurrence above, the permanent reduction to gradient descent after one crossing, or the resulting loss of ordinary momentum's larger scalar Schur-stability interval.

The result here therefore sharpens the intended mechanism rather than disputing it. In the scalar overshoot regime the safeguard works maximally: after the first crossing it removes momentum at every subsequent step. That exact behavior explains both its reduced stale-momentum oscillation and its inability, in this regime, to retain momentum's enlarged deterministic stability range.

Focused published-record searches for an SPI scalar quadratic reset law, permanent momentum erasure, and an exact large-step stability comparison did not identify an implication-equivalent result.

## Limitations

Only the first-overshoot regime
\[
r\lambda>1
\]
is classified.

The theorem uses a deterministic scalar quadratic and zero initial momentum.

It does not analyze noisy sign errors, multidimensional coordinates with differing curvatures, or nonquadratic objectives.

The result concerns linear stability, not generalization or empirical training speed.

## References

1. Dan Wang, Mengqi Ji, Yong Wang, Haoqian Wang, and Lu Fang, “SPI-Optimizer: an integral-Separated PI Controller for Stochastic Optimization,” arXiv:1812.11305v1, first submitted 2018-12-29; ICIP 2019.
