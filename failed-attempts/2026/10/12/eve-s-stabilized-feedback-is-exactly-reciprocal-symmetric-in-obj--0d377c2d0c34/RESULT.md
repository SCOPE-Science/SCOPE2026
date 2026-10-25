# Eve's stabilized feedback is exactly reciprocal-symmetric in objective-gap ratios
## Finding

Eve adapts Adam's global learning rate using consecutive objective values. Its stabilization replaces the current objective gap in the raw ratio by the smaller of the current and previous objective gaps. That choice creates an exact symmetry that is not visible from the algorithm's informal motivation.

Let
\[
\Delta_t=f_t-f^\star>0
\]
be the objective gap and define the consecutive gap ratio
\[
q_t=\frac{\Delta_t}{\Delta_{t-1}}>0.
\]
Eve's stabilized raw feedback is
\[
d_t
=
\frac{|f_t-f_{t-1}|}
{\min\{f_t,f_{t-1}\}-f^\star}.
\]
Therefore
\[
\boxed{
d_t
=
\max\{q_t,q_t^{-1}\}-1
}.
\]

Hence
\[
\boxed{
d(q)=d(q^{-1})
}.
\]
A multiplicative improvement by a factor \(q<1\) and a reciprocal multiplicative worsening by \(1/q>1\) are indistinguishable to Eve's raw global-feedback signal.

With clipping parameter
\[
c>1,
\]
Eve uses
\[
\widehat d_t
=
\operatorname{clip}
\left(
d_t,
[1/c,c]
\right)
\]
and then smooths it by
\[
\widetilde d_t
=
\beta_3\widetilde d_{t-1}
+
(1-\beta_3)\widehat d_t,
\qquad
0\le\beta_3<1,
\]
starting from
\[
\widetilde d_1=1.
\]
The global learning rate is
\[
\alpha_t=\frac{\alpha_1}{\widetilde d_t}.
\]
Consequently the reciprocal symmetry survives clipping and smoothing whenever the previous smoothed state is the same.

Now suppose the positive objective gaps form a geometric trace,
\[
\Delta_t=q^{t-1}\Delta_1,
\qquad
q>0.
\]
Then the clipped feedback is constant:
\[
\widehat d
=
\operatorname{clip}
\left(
\max\{q,q^{-1}\}-1,
[1/c,c]
\right).
\]
The smoothing recurrence has the exact solution
\[
\boxed{
\widetilde d_t
=
\widehat d
+
(1-\widehat d)\beta_3^{t-1}
}.
\]
Hence
\[
\boxed{
\alpha_t
\longrightarrow
\frac{\alpha_1}{\widehat d}
}.
\]

The clipping thresholds give a complete phase diagram. The largest possible limiting global rate,
\[
c\alpha_1,
\]
occurs exactly when
\[
\boxed{
\frac{c}{c+1}
\le q\le
\frac{c+1}{c}
}.
\]
The smallest possible limiting rate,
\[
\frac{\alpha_1}{c},
\]
occurs exactly when
\[
\boxed{
q\le\frac1{c+1}
\quad\text{or}\quad
q\ge c+1
}.
\]
Between those regions the clipping is inactive.

For a strictly improving geometric trace,
\[
0<q<1,
\]
the limiting rate is
\[
\boxed{
\alpha_\infty(q)
=
\begin{cases}
\alpha_1/c,
&0<q\le 1/(c+1),\\[4pt]
\alpha_1 q/(1-q),
&1/(c+1)<q<c/(c+1),\\[4pt]
c\alpha_1,
&c/(c+1)\le q<1.
\end{cases}
}
\]
Thus faster multiplicative improvement, meaning smaller \(q\), receives a weakly smaller asymptotic global learning rate.

At the source default
\[
c=10,
\]
the maximum-rate band is
\[
\frac{10}{11}
\le q\le
\frac{11}{10},
\]
while the minimum rate is reached for
\[
q\le\frac1{11}
\quad\text{or}\quad
q\ge11.
\]
A ten-fold improvement,
\[
q=0.1,
\]
and a ten-fold worsening,
\[
q=10,
\]
both have
\[
d=9
\]
and therefore the same asymptotic global rate
\[
\frac{\alpha_1}{9}.
\]

## Assumptions and scope

The claim uses Eve's defining stabilized objective-feedback equations and assumes the true global minimum \(f^\star\) is known.

All consecutive gaps are strictly positive, so Eve's denominator is nonzero.

The geometric-trace result is an input-response theorem for Eve's global feedback channel. It does not assert that the full Adam-plus-Eve parameter dynamics generate a geometric objective sequence.

The Adam first- and second-moment states do not enter the algebra because Eve's global scalar feedback is computed entirely from objective values before multiplying the Adam direction.

## Proof

Write
\[
\Delta_t=f_t-f^\star,
\qquad
\Delta_{t-1}=f_{t-1}-f^\star.
\]
Then
\[
d_t
=
\frac{|\Delta_t-\Delta_{t-1}|}
{\min\{\Delta_t,\Delta_{t-1}\}}.
\]
Substituting
\[
\Delta_t=q_t\Delta_{t-1}
\]
gives
\[
d_t
=
\frac{|q_t-1|}{\min\{q_t,1\}}.
\]
If \(q_t\ge1\), this is \(q_t-1\). If \(0<q_t\le1\), it is \(q_t^{-1}-1\). Thus
\[
d_t=\max\{q_t,q_t^{-1}\}-1,
\]
which proves reciprocal symmetry.

For a geometric trace, \(q_t=q\) is constant, so \(\widehat d_t=\widehat d\) is constant. Solving
\[
\widetilde d_t
=
\beta_3\widetilde d_{t-1}
+
(1-\beta_3)\widehat d,
\qquad
\widetilde d_1=1,
\]
gives
\[
\widetilde d_t
=
\widehat d
+
(1-\widehat d)\beta_3^{t-1}.
\]
Because \(0\le\beta_3<1\), this converges to \(\widehat d\).

The lower clipping branch is active when
\[
\max\{q,q^{-1}\}-1\le\frac1c.
\]
Equivalently,
\[
\max\{q,q^{-1}\}\le1+\frac1c,
\]
which is exactly
\[
\frac{c}{c+1}
\le q\le
\frac{c+1}{c}.
\]
There \(\widehat d=1/c\), so the limiting rate is \(c\alpha_1\).

The upper clipping branch is active when
\[
\max\{q,q^{-1}\}-1\ge c,
\]
which is equivalent to
\[
q\le\frac1{c+1}
\quad\text{or}\quad
q\ge c+1.
\]
There \(\widehat d=c\), so the limiting rate is \(\alpha_1/c\).

For \(0<q<1\) in the unclipped region,
\[
d=q^{-1}-1=\frac{1-q}{q},
\]
so
\[
\alpha_\infty
=
\frac{\alpha_1}{d}
=
\alpha_1\frac{q}{1-q}.
\]
This is strictly increasing in \(q\), and the clipped branches preserve weak monotonicity.

## Verification

The accompanying `verify.py` checks the reciprocal identity, clipping thresholds, smoothing closed form, default \(c=10\) phase boundaries, and the exact ten-fold reciprocal example over randomized positive gap ratios.

The computation is a transcription guard. The identities are proved algebraically above.

## Relationship to prior work

Hayashi, Koushik, and Neubig introduce Eve as Adam with a globally adaptive scalar learning rate. Their motivation separates two effects: large variation in consecutive objective evaluations should reduce the learning rate, while large suboptimality should increase it. They then stabilize the raw rule by replacing the current objective value in the numerator with the smaller of the current and previous objective values, clipping the resulting coefficient to \([1/c,c]\), and exponentially smoothing it.

The defining paper states the stabilized equations and the resulting learning-rate range, but it does not state that the stabilized coefficient depends only on the multiplicative gap-change magnitude
\[
\max\{q,q^{-1}\}-1,
\]
or that reciprocal improvement and worsening traces are exactly indistinguishable to the global-feedback channel.

The paper's default is
\[
c=10,
\qquad
\beta_3=0.999.
\]
The exact phase boundaries above therefore turn those hyperparameters into objective-gap thresholds rather than only abstract clipping constants.

Focused published-record searches for Eve under reciprocal loss ratios, geometric objective decay, clipping thresholds, and exact global-feedback symmetries did not identify an implication-equivalent result.

## Limitations

The result characterizes the global objective-feedback channel, not the complete parameter trajectory.

Stochastic loss noise can make successive gap ratios fluctuate rather than remain geometric.

The theorem assumes the true minimum \(f^\star\) is known and that all observed gaps stay positive.

The symmetry is a mathematical property of the stabilized defining formula; it does not by itself establish that the symmetry is harmful on a particular application.

## References

1. Hiroaki Hayashi, Jayanth Koushik, and Graham Neubig, “Eve: A Gradient Based Optimization Method with Locally and Globally Adaptive Learning Rates,” arXiv:1611.01505v1, first submitted 2016-11-04; later revised as arXiv:1611.01505v3.
