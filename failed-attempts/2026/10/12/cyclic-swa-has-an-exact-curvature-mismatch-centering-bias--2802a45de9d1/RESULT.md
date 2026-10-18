# Cyclic SWA has an exact curvature-mismatch centering bias
## Finding

Let
\[
f_1(x)=\frac12a(x-u)^2,\qquad f_2(x)=\frac12b(x-v)^2,\qquad a,b>0.
\]
Run constant-step cyclic SGD, applying \(f_1\) then \(f_2\):
\[
q_k=(1-\eta a)p_k+\eta au,\qquad
p_{k+1}=(1-\eta b)q_k+\eta bv.
\]
Assume
\[
|(1-\eta a)(1-\eta b)|<1.
\]
Then the two phase subsequences converge to
\[
p=\frac{a(1-\eta b)u+bv}{a+b-ab\eta},\qquad
q=\frac{au+b(1-\eta a)v}{a+b-ab\eta}.
\]

For
\[
F(x)=\frac12(f_1(x)+f_2(x)),
\qquad
x_\star=\frac{au+bv}{a+b},
\]
equal-weight SWA over all post-update iterates converges to
\[
\bar x_{\rm SWA}=\frac{p+q}{2}.
\]
Its exact bias is
\[
\boxed{\bar x_{\rm SWA}-x_\star=
\frac{ab\eta(a-b)(u-v)}{2(a+b)(a+b-ab\eta)}}.
\]
Hence, for \(\eta>0\),
\[
\boxed{\bar x_{\rm SWA}=x_\star\iff(a-b)(u-v)=0}.
\]

The exact objective excess is
\[
\boxed{F(\bar x_{\rm SWA})-F(x_\star)=
\frac{a^2b^2\eta^2(a-b)^2(u-v)^2}{16(a+b)(a+b-ab\eta)^2}}.
\]

A cross-phase curvature weighting removes the entire bias:
\[
\boxed{\frac{ap+bq}{a+b}=x_\star}.
\]
Thus the post-\(f_2\) phase receives weight \(a\), while the post-\(f_1\) phase receives weight \(b\).

## Assumptions and scope

The model is one-dimensional, has two strongly convex quadratic components, deterministic alternating component order, and a constant step satisfying the exact two-step stability condition above.

The SWA average is the equal-weight average of all post-update iterates in the stable constant-step regime. Independent sampling and random reshuffling have different stationary behavior and are outside this theorem.

## Proof

Combining the two updates gives the affine map
\[
p_{k+1}=(1-\eta a)(1-\eta b)p_k+\eta a(1-\eta b)u+\eta bv.
\]
The assumed multiplier has modulus below one, so the fixed point is the displayed \(p\); substituting it into the first update gives \(q\).

Also,
\[
1-(1-\eta a)(1-\eta b)=\eta(a+b-ab\eta)>0.
\]
Direct subtraction of \(x_\star\) from \((p+q)/2\) gives the stated bias.

Since
\[
F''(x)=\frac{a+b}{2},
\]
quadratic completion gives
\[
F(x)-F(x_\star)=\frac{a+b}{4}(x-x_\star)^2,
\]
which yields the objective excess.

Finally, expanding \(ap+bq\) shows its \(u\)-coefficient is \(a(a+b-ab\eta)\) and its \(v\)-coefficient is \(b(a+b-ab\eta)\). Dividing by \((a+b)(a+b-ab\eta)\) gives \(x_\star\).

## Verification

`verify.py` checks random stable parameter choices, simulates convergence to the two-cycle, verifies the exact SWA bias and objective excess, confirms the curvature-weighted identity, and tests the equal-curvature zero-bias case.

The computation is a transcription guard; the theorem is proved algebraically above.

## Relationship to prior work

Izmailov and coauthors define SWA as equal-weight averaging of SGD iterates gathered under constant or cyclical learning rates. Their convex-minimization discussion uses a simplifying picture in which fixed-step SGD samples around a minimizer and averaging recovers that center.

Classical incremental-gradient and random-reshuffling theory already establishes order-dependent bias and phase effects for finite-sum optimization. Those broad phenomena are prior work.

The inspected primary sources do not state this exact stable constant-step two-component SWA center, its closed objective gap, or the cross-phase curvature weighting that recovers the finite-sum minimizer for every stable step.

## Limitations

The theorem is restricted to one scalar parameter and two quadratic components.

The component order is deterministic. Randomized component order has different averaging behavior.

The exact correction uses component curvature information, which may be unavailable in large models.

No claim is made about SWA's separate generalization benefits in nonconvex neural networks.

## References

1. Pavel Izmailov, Dmitrii Podoprikhin, Timur Garipov, Dmitry Vetrov, and Andrew Gordon Wilson, “Averaging Weights Leads to Wider Optima and Better Generalization,” arXiv:1803.05407v1, first submitted 2018-03-14; UAI 2018.
2. Mert Gürbüzbalaban, Asuman Ozdaglar, and Pablo Parrilo, “Why Random Reshuffling Beats Stochastic Gradient Descent,” arXiv:1510.08560v4.
