# Exact period-two stability window for asynchronous AdaShift
## Finding

AdaShift separates the gradient used in the numerator from older gradients used in its adaptive denominator. For the one-step asynchronous form, this delay creates an exactly solvable nonlinear oscillation on a scalar quadratic.

Consider
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]
Use the constant-step \(n=1\) asynchronous AdaShift recurrence
\[
x_{t+1}
=
x_t-
\alpha\frac{\lambda x_t}{\sqrt{v_t}+\varepsilon},
\]
\[
v_{t+1}
=
\beta_2v_t
+
(1-\beta_2)\lambda^2x_t^2,
\]
where
\[
0<\beta_2<1,
\qquad
\alpha>0,
\qquad
\varepsilon\ge0.
\]
Here \(v_t\) is the asynchronous denominator state available before the current gradient is inserted into \(v_{t+1}\). This is the \(n=1\) form used in later convergence analysis of AdaShift-type asynchronous methods.

A nonzero sign-flip period-two state exists exactly when
\[
\alpha\lambda>2\varepsilon.
\]
Its radius is
\[
r
=
\frac{\alpha}{2}
-
\frac{\varepsilon}{\lambda},
\]
and the exact orbit is
\[
x_t=(-1)^t r,
\qquad
v_t=\lambda^2r^2.
\]

Define the dimensionless saturation parameter
\[
c
=
\frac{\lambda r}{\lambda r+\varepsilon}
=
1-
\frac{2\varepsilon}{\alpha\lambda}.
\]
Existence is exactly
\[
0<c<1.
\]
The two Floquet multipliers over one full period are the roots of
\[
z^2
-
\left[
1+\beta_2^2-4c(1-\beta_2)
\right]z
+
\left[
\beta_2+2c(1-\beta_2)
\right]^2
=
0.
\]

The stability classification is sharp:
\[
2\varepsilon<\alpha\lambda<4\varepsilon
\]
if and only if the period-two orbit is asymptotically stable,
\[
\alpha\lambda=4\varepsilon
\]
is the neutral boundary, and
\[
\alpha\lambda>4\varepsilon
\]
makes the orbit unstable.

Thus the denominator constant is dynamically active. A positive \(\varepsilon\) creates a finite window of stable nonzero oscillations. With
\[
\varepsilon=0,
\]
the same sign-flip orbit exists for every positive base step but is always unstable.

The Floquet discriminant factors exactly as
\[
(\beta_2-1)(\beta_2+1)^2(\beta_2+8c-1).
\]
Whenever
\[
c>
\frac{1-\beta_2}{8},
\]
the multipliers are complex conjugates and have exact two-step modulus
\[
\beta_2+2c(1-\beta_2).
\]
In the zero-denominator limit \(c=1\), this becomes
\[
2-\beta_2>1.
\]
Hence the unstable cycle has an exact two-step growth factor \(2-\beta_2\), which approaches neutrality only as \(\beta_2\uparrow1\).

For example, with
\[
\lambda=1,
\qquad
\varepsilon=1,
\qquad
\beta_2=0.9,
\]
choosing
\[
\alpha=3
\]
gives the stable cycle radius \(r=1/2\), while
\[
\alpha=5
\]
gives an unstable cycle. The transition occurs exactly at \(\alpha=4\).

## Assumptions and scope

The recurrence is the \(n=1\) asynchronous AdaShift form in which the current numerator uses the current gradient while the denominator contains only earlier second-moment information. With a one-gradient numerator window, the first-moment weighting parameter drops out.

The result is for a deterministic scalar quadratic and a constant base step. The convergence results in the cited papers use stochastic or online settings and, in key theorems, decaying learning-rate schedules; there is no contradiction.

The theorem classifies the nonzero period-two state, not every trajectory. It does not claim global attraction of the stable cycle.

The original AdaShift paper also studies longer delays and blockwise spatial operations. Those variants have higher-dimensional state and are outside this theorem.

## Proof

Seek a sign-alternating state
\[
x_t=(-1)^t r,
\qquad
r>0,
\]
with constant
\[
v_t=\lambda^2r^2.
\]
The second-moment recurrence is then satisfied identically because
\[
v_{t+1}
=
\beta_2\lambda^2r^2
+
(1-\beta_2)\lambda^2r^2
=
\lambda^2r^2.
\]

The parameter update flips sign exactly when
\[
1-
\frac{\alpha\lambda}{\lambda r+\varepsilon}
=
-1.
\]
Therefore
\[
\lambda r+\varepsilon
=
\frac{\alpha\lambda}{2},
\]
which gives
\[
r
=
\frac{\alpha}{2}
-
\frac{\varepsilon}{\lambda}.
\]
A nonzero radius exists exactly when
\[
\alpha\lambda>2\varepsilon.
\]

For stability, use normalized perturbations
\[
u_t=\frac{\delta x_t}{r},
\qquad
w_t=\frac{\delta v_t}{\lambda^2r^2}.
\]
At the phase
\[
x_t=s r,
\qquad
s\in\{-1,1\},
\]
the one-step Jacobian in \((u,w)\) coordinates is
\[
J_s
=
\begin{bmatrix}
-1&s c\\
2(1-\beta_2)s&\beta_2
\end{bmatrix},
\]
where
\[
c
=
\frac{\lambda r}{\lambda r+\varepsilon}.
\]

The two-step monodromy matrix is
\[
M=J_{-1}J_{1}.
\]
Its trace and determinant are
\[
\operatorname{tr}M
=
1+\beta_2^2-4c(1-\beta_2),
\]
\[
\det M
=
\left[
\beta_2+2c(1-\beta_2)
\right]^2.
\]
This proves the displayed Floquet polynomial.

For a real monic quadratic
\[
z^2-Tz+D,
\]
the Jury conditions are
\[
1-D>0,
\qquad
1-T+D>0,
\qquad
1+T+D>0.
\]
Here write
\[
d
=
\beta_2+2c(1-\beta_2),
\qquad
D=d^2.
\]
Since \(0<\beta_2<1\),
\[
1-D>0
\quad\Longleftrightarrow\quad
c<\frac12.
\]
The second condition simplifies to
\[
4c(1-\beta_2)
\left[
1+\beta_2+c-\beta_2c
\right]
>0,
\]
and is automatic. The third condition is
\[
1+T+D
=
(1-d)^2+(1+\beta_2)^2
>0.
\]
Thus the cycle is asymptotically stable exactly when
\[
c<\frac12.
\]
Using
\[
c=1-rac{2\varepsilon}{\alpha\lambda}
\]
and the existence condition \(c>0\), this is exactly
\[
2\varepsilon
<
\alpha\lambda
<
4\varepsilon.
\]
At \(c=1/2\), the multiplier product is one and the cycle is neutral. For \(c>1/2\), the multiplier product exceeds one, so the cycle is unstable.

Finally, direct expansion gives the Floquet discriminant
\[
(\beta_2-1)(\beta_2+1)^2(\beta_2+8c-1).
\]
When it is negative, the two roots are complex conjugates, and their common modulus is the square root of the determinant,
\[
d
=
\beta_2+2c(1-\beta_2).
\]
At \(\varepsilon=0\), \(c=1\), so this modulus is exactly \(2-\beta_2\).

## Verification

The accompanying `verify.py` checks the exact period-two state, compares the analytic one-step Jacobians with finite differences, verifies the two-step characteristic polynomial, and tests both sides of the sharp stability boundary over many parameter choices.

The finite calculations are transcription guards. Existence and the complete Floquet classification are proved analytically above.

## Relationship to prior work

Zhou, Zhang, Lu, Wang, Zhang, and Yu introduced AdaShift to decorrelate the current gradient from its adaptive denominator by using temporally shifted gradients. Their paper gives the shifted second-moment recurrence, the truncated recent-gradient first moment, and the full queue-based algorithm. It also reports that the temporal-only variant can be less stable and can suffer explosive gradients on some tasks, requiring a smaller learning rate.

Zhuang, Ding, Tang, Dvornek, Tatikonda, and Duncan later formalized AdaShift as an asynchronous uncentered adaptive method. For \(n=1\), they write the denominator as information available before the current gradient, contrast this with synchronous Adam-type methods, and prove convergence on specific online problems under decaying step schedules. They also report that larger AdaShift delays can cause nonconvergence and that no single delay choice is uniformly best across their examples.

Neither inspected source analyzes constant-step deterministic scalar quadratic period-two states, supplies the exact \(2\varepsilon\) to \(4\varepsilon\) stability window, or gives the Floquet factor \(2-\beta_2\) at zero denominator constant.

## Limitations

The theorem is specific to the one-step asynchronous, uncentered scalar recurrence.

It studies a nonzero periodic orbit and does not classify global basins of attraction.

Longer AdaShift delays and spatial operations introduce additional state variables and can have different periodic structures.

Constant-step behavior can differ substantially from the decaying-step regimes used in published convergence guarantees.

## References

1. Zhiming Zhou, Qingru Zhang, Guansong Lu, Hongwei Wang, Weinan Zhang, and Yong Yu, “AdaShift: Decorrelation and Convergence of Adaptive Learning Rate Methods,” arXiv:1810.00143v1, 2018.
2. Juntang Zhuang, Yifan Ding, Tommy Tang, Nicha Dvornek, Sekhar Tatikonda, and James S. Duncan, “Momentum Centering and Asynchronous Update for Adaptive Gradient Methods,” arXiv:2110.05454v1, 2021.
