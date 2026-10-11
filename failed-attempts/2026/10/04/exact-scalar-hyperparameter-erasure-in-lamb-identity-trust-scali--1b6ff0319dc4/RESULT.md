# Exact scalar hyperparameter erasure in LAMB identity trust scaling
## Finding

Consider paper-form LAMB on one scalar layer, with zero weight decay and identity layer scaling
\[
\phi(z)=z.
\]
Let
\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,\qquad
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2,
\]
where
\[
m_0=v_0=0,\qquad 0\le\beta_1,\beta_2<1,
\]
and let
\[
r_t=\frac{\widehat m_t}{\sqrt{\widehat v_t}+\varepsilon},
\qquad \varepsilon>0,
\]
with the usual positive bias-correction factors when used.

Assume that the deterministic differentiable objective satisfies
\[
x f'(x)>0
\]
for every \(x\ne0\), and use learning rates
\[
0<\eta_t<1.
\]
Then for every \(x_0\ne0\), LAMB obeys the exact recurrence
\[
x_{t+1}=(1-\eta_t)x_t
\]
at every iteration. Therefore
\[
x_t=x_0\prod_{s<t}(1-\eta_s).
\]

The trajectory is exactly independent of gradient magnitude, \(\beta_1\), \(\beta_2\), and \(\varepsilon\). These quantities affect the magnitude of \(r_t\), but scalar LAMB normalization cancels that magnitude before the parameter update.

For a constant learning rate
\[
0<\eta<1,
\]
the global parameter rate is exactly
\[
|x_t|=(1-\eta)^t|x_0|.
\]

For the scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,\qquad \lambda>0,
\]
one obtains
\[
\frac{f(x_{t+1})}{f(x_t)}=(1-\eta_t)^2.
\]
Thus the curvature \(\lambda\) is completely absent from the parameter dynamics.

## Assumptions and scope

The theorem uses the defining LAMB update with one scalar layer, zero weight decay, and the identity scaling \(\phi(z)=z\) explicitly discussed in the source paper.

The restriction
\[
0<\eta_t<1
\]
ensures that the iterate never crosses the minimizer. After a sign reversal, the momentum state can temporarily disagree with the new gradient sign and the moment hyperparameters can again affect the trajectory.

Trust-ratio clipping is excluded. An active trust-ratio clip, such as in LAMBC, can interrupt the exact normalization identity.

The theorem is one-dimensional. In higher-dimensional layers, layer normalization removes the update norm but not its direction, so the adaptive moments can still change the trajectory.

## Proof

Suppose first that \(x_0>0\). The sign-coherence condition gives \(g_0=f'(x_0)>0\). Starting from \(m_0=0\), every first-moment update is a positive weighted average of positive gradients, so \(m_t>0\). Bias correction preserves its sign. The second-moment denominator is positive, hence \(r_t>0\).

For a scalar layer with zero weight decay, LAMB updates as
\[
x_{t+1}
=
x_t-\eta_t\frac{\phi(|x_t|)}{|r_t|}r_t.
\]
With \(\phi(z)=z\) and \(r_t>0\),
\[
x_{t+1}=x_t-\eta_t|x_t|=(1-\eta_t)x_t.
\]
Because \(0<\eta_t<1\), the next iterate remains positive. Induction proves the recurrence for all time.

If \(x_0<0\), the same argument gives negative gradients, negative first moments, and \(r_t<0\). Then
\[
|x_t|\frac{r_t}{|r_t|}=x_t,
\]
so again
\[
x_{t+1}=(1-\eta_t)x_t,
\]
and the sign remains negative.

Iterating proves the product formula. For the quadratic, substituting the recurrence into \(f(x)=\lambda x^2/2\) gives the exact squared objective factor.

## Verification

The accompanying `verify.py` evaluates the complete scalar moment recurrences with bias correction for multiple curvatures, nonlinear sign-coherent objectives, moment parameters, and epsilon values. It compares every iterate with the exact product law.

The computations are transcription guards. The infinite-time identity follows from the sign induction and exact scalar normalization above.

## Relationship to prior work

You et al. introduced LAMB as Adam-style elementwise adaptation followed by layerwise normalization. Their general strategy explicitly says that normalization ignores update magnitude while preserving direction, and they discuss the identity choice
\[
\phi(z)=z
\]
as an inverse-curvature proxy. Their LAMB theorem gives a general nonconvex stationarity rate, but the inspected paper does not state the exact scalar trajectory or the resulting complete erasure of Adam magnitude hyperparameters on a sign-coherent class.

Fong, Chen, and Chen later observed that LAMB and LARS can develop extreme trust ratios and introduced LAMBC, which clips them. Their formulation makes the layerwise trust normalization explicit. An active clip is also a precise mechanism that breaks the exact scalar cancellation proved here.

## Limitations

The identity relies on one scalar layer, zero weight decay, identity layer scaling, and no sign reversal.

The clipped scaling function also discussed in the defining paper behaves differently when its bounds are active.

The result is an exact dynamical benchmark, not a claim that one-dimensional LAMB is representative of all neural-network training behavior.

## References

1. Yang You, Jing Li, Sashank Reddi, Jonathan Hseu, Sanjiv Kumar, Srinadh Bhojanapalli, Xiaodan Song, James Demmel, Kurt Keutzer, and Cho-Jui Hsieh, “Large Batch Optimization for Deep Learning: Training BERT in 76 minutes,” arXiv:1904.00962v1, 2019.
2. Jeffrey Fong, Siwei Chen, and Kaiqi Chen, “Improving Layer-wise Adaptive Rate Methods using Trust Ratio Clipping,” arXiv:2011.13584v1, 2020.
